#!/usr/bin/env python3
"""Macro data fetcher for the decade-x-investing skill.

A self-contained, stdlib-only tool for pulling macroeconomic reference data.

Sources
-------
* **Treasury** (default, FREE, NO API KEY):
  U.S. Treasury Fiscal Data API ``fiscaldata.treasury.gov``. Returns the
  latest "Average Interest Rates" on marketable & non-marketable Treasury
  securities (Bills / Notes / Bonds / TIPS / etc.) -- a clean proxy for the
  prevailing cost of government borrowing across the curve.

* **FRED** (optional, FREE key): Federal Reserve Economic Data. Used for
  named series such as ``CPIAUCSL`` (CPI) or ``GDP``. Requires a free API
  key supplied via the ``FRED_API_KEY`` environment variable. If the key is
  absent the FRED command exits cleanly with a helpful message; the Treasury
  command never needs a key.

Design notes
------------
* Python 3 standard library only (``urllib``, ``json``, ``argparse``). No pip.
* Pure / immutable style: helpers return new dicts/tuples, nothing is mutated
  in place.
* No hardcoded secrets. The optional FRED key is read from the environment.
* Comprehensive error handling with actionable messages.

CLI examples
------------
    python3 tools/fetch_macro.py treasury
    python3 tools/fetch_macro.py treasury --raw
    python3 tools/fetch_macro.py fred CPIAUCSL
    python3 tools/fetch_macro.py fred GDP --limit 5
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Mapping, Sequence, Tuple

__all__ = [
    "fetch_treasury_rates",
    "fetch_fred_series",
    "main",
]

# --- Constants -------------------------------------------------------------

TREASURY_BASE = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    "/v2/accounting/od/avg_interest_rates"
)
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

USER_AGENT = "decade-x-investing/fetch_macro (stdlib urllib)"
DEFAULT_TIMEOUT = 30  # seconds


# --- Errors ----------------------------------------------------------------


class MacroFetchError(Exception):
    """Raised for any recoverable failure while fetching macro data."""


# --- HTTP helper -----------------------------------------------------------


def _http_get_json(
    base_url: str,
    params: Mapping[str, Any],
    *,
    timeout: int = DEFAULT_TIMEOUT,
) -> Mapping[str, Any]:
    """GET ``base_url?params`` and decode the JSON body.

    Returns a freshly parsed JSON object. Network, HTTP and decoding failures
    are normalized into :class:`MacroFetchError` with a helpful message.
    """
    query = urllib.parse.urlencode(dict(params), doseq=True)
    url = f"{base_url}?{query}" if query else base_url
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            payload = response.read().decode(charset)
    except urllib.error.HTTPError as exc:
        # Server replied with a non-2xx status.
        detail = ""
        try:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
        except Exception:  # noqa: BLE001 - best-effort body capture
            detail = ""
        raise MacroFetchError(
            f"HTTP {exc.code} from {base_url}: {exc.reason}. "
            f"{detail.strip()}".strip()
        ) from exc
    except urllib.error.URLError as exc:
        raise MacroFetchError(
            f"Network error reaching {base_url}: {exc.reason}. "
            "Check your internet connection or proxy settings."
        ) from exc
    except TimeoutError as exc:  # pragma: no cover - timing dependent
        raise MacroFetchError(
            f"Request to {base_url} timed out after {timeout}s."
        ) from exc

    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise MacroFetchError(
            f"Could not decode JSON from {base_url}: {exc}. "
            f"First 200 chars of body: {payload[:200]!r}"
        ) from exc

    if not isinstance(parsed, Mapping):
        raise MacroFetchError(
            f"Unexpected JSON shape from {base_url}: expected object, "
            f"got {type(parsed).__name__}."
        )
    return parsed


# --- Treasury --------------------------------------------------------------


def fetch_treasury_rates(
    *,
    timeout: int = DEFAULT_TIMEOUT,
) -> Tuple[Mapping[str, Any], ...]:
    """Fetch the latest Treasury average interest rates.

    The Fiscal Data API exposes one row per security on each month-end record
    date. We request the most recent records (sorted descending by date) and
    keep only the rows belonging to the single newest ``record_date``.

    Returns
    -------
    A tuple of immutable row dicts, each containing at least::

        record_date, security_type_desc, security_desc, avg_interest_rate_amt

    Raises
    ------
    MacroFetchError
        If the request fails or the response contains no usable data.
    """
    params = {
        "fields": (
            "record_date,security_type_desc,security_desc,avg_interest_rate_amt"
        ),
        "sort": "-record_date",
        "page[size]": 200,
    }
    body = _http_get_json(TREASURY_BASE, params, timeout=timeout)

    rows = body.get("data")
    if not isinstance(rows, Sequence) or not rows:
        raise MacroFetchError(
            "Treasury API returned no data rows. The endpoint may have "
            "changed or be temporarily unavailable."
        )

    latest_date = rows[0].get("record_date")
    if not latest_date:
        raise MacroFetchError(
            "Treasury API rows are missing 'record_date'; cannot determine "
            "the latest period."
        )

    # Keep only rows for the newest record_date. Build new dicts (no mutation).
    latest_rows = tuple(
        dict(row) for row in rows if row.get("record_date") == latest_date
    )
    return latest_rows


def _format_treasury(rows: Sequence[Mapping[str, Any]]) -> str:
    """Render Treasury rows as a compact aligned table (pure function)."""
    if not rows:
        return "No Treasury rows."

    record_date = rows[0].get("record_date", "?")
    header = f"U.S. Treasury Average Interest Rates -- as of {record_date}"
    separator = "-" * len(header)

    type_width = max(len(str(r.get("security_type_desc", ""))) for r in rows)
    desc_width = max(len(str(r.get("security_desc", ""))) for r in rows)

    lines = tuple(
        f"{str(r.get('security_type_desc', '')):<{type_width}} | "
        f"{str(r.get('security_desc', '')):<{desc_width}} | "
        f"{str(r.get('avg_interest_rate_amt', '?')):>7}%"
        for r in rows
    )
    return "\n".join((header, separator, *lines))


# --- FRED ------------------------------------------------------------------


def fetch_fred_series(
    series_id: str,
    *,
    api_key: str,
    limit: int = 10,
    timeout: int = DEFAULT_TIMEOUT,
) -> Tuple[Mapping[str, Any], ...]:
    """Fetch the most recent observations for a FRED ``series_id``.

    Parameters
    ----------
    series_id:
        e.g. ``"CPIAUCSL"`` (CPI, all urban consumers) or ``"GDP"``.
    api_key:
        A free FRED API key (https://fredaccount.stlouisfed.org/apikeys).
    limit:
        Number of most-recent observations to return (newest first).

    Returns a tuple of ``{"date": ..., "value": ...}`` dicts, newest first.
    """
    if not series_id or not series_id.strip():
        raise MacroFetchError("A FRED series id is required (e.g. CPIAUCSL).")
    if not api_key:
        raise MacroFetchError(
            "No FRED API key provided. Set the FRED_API_KEY environment "
            "variable (free key: https://fredaccount.stlouisfed.org/apikeys)."
        )

    params = {
        "series_id": series_id.strip(),
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": max(1, int(limit)),
    }
    body = _http_get_json(FRED_BASE, params, timeout=timeout)

    observations = body.get("observations")
    if not isinstance(observations, Sequence):
        raise MacroFetchError(
            f"FRED response for '{series_id}' contained no observations. "
            "Verify the series id is correct."
        )

    return tuple(
        {"date": obs.get("date"), "value": obs.get("value")}
        for obs in observations
    )


def _format_fred(series_id: str, rows: Sequence[Mapping[str, Any]]) -> str:
    """Render FRED observations as an aligned table (pure function)."""
    if not rows:
        return f"FRED series '{series_id}': no observations."

    header = f"FRED series {series_id} -- {len(rows)} most recent observations"
    separator = "-" * len(header)
    lines = tuple(
        f"{r.get('date', '?'):<12} | {str(r.get('value', '?')):>14}"
        for r in rows
    )
    return "\n".join((header, separator, "Date         |          Value", *lines))


# --- CLI -------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fetch_macro.py",
        description=(
            "Fetch macro reference data. Treasury yields are free and need no "
            "key; FRED series need a free FRED_API_KEY environment variable."
        ),
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"HTTP timeout in seconds (default: {DEFAULT_TIMEOUT}).",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    treasury = subparsers.add_parser(
        "treasury",
        help="Latest U.S. Treasury average interest rates (free, no key).",
    )
    treasury.add_argument(
        "--raw",
        action="store_true",
        help="Emit raw JSON instead of a formatted table.",
    )

    fred = subparsers.add_parser(
        "fred",
        help="Recent observations for a FRED series (needs FRED_API_KEY).",
    )
    fred.add_argument("series_id", help="FRED series id, e.g. CPIAUCSL or GDP.")
    fred.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of recent observations to return (default: 10).",
    )
    fred.add_argument(
        "--raw",
        action="store_true",
        help="Emit raw JSON instead of a formatted table.",
    )
    return parser


def _run_treasury(args: argparse.Namespace) -> int:
    rows = fetch_treasury_rates(timeout=args.timeout)
    if args.raw:
        print(json.dumps(list(rows), indent=2))
    else:
        print(_format_treasury(rows))
    return 0


def _run_fred(args: argparse.Namespace) -> int:
    api_key = os.environ.get("FRED_API_KEY", "").strip()
    if not api_key:
        print(
            "FRED_API_KEY is not set. The Treasury command works without a "
            "key; for FRED series get a free key at "
            "https://fredaccount.stlouisfed.org/apikeys and export it:\n"
            "  export FRED_API_KEY=your_key_here",
            file=sys.stderr,
        )
        return 2

    rows = fetch_fred_series(
        args.series_id,
        api_key=api_key,
        limit=args.limit,
        timeout=args.timeout,
    )
    if args.raw:
        print(json.dumps(list(rows), indent=2))
    else:
        print(_format_fred(args.series_id, rows))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point. Returns a process exit code."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    handlers = {"treasury": _run_treasury, "fred": _run_fred}
    handler = handlers.get(args.command)
    if handler is None:  # pragma: no cover - argparse enforces choices
        parser.error(f"Unknown command: {args.command}")
        return 2

    try:
        return handler(args)
    except MacroFetchError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:  # pragma: no cover - interactive
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
