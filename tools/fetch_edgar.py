#!/usr/bin/env python3
"""SEC EDGAR companyfacts fetcher (FREE, NO API KEY).

Pulls a US public company's reported financials (revenue, net income, EPS,
shares outstanding, cash flow components, etc.) straight from the SEC's free,
public data API at https://data.sec.gov.

Two SEC endpoints are used:
  * Ticker map:   https://www.sec.gov/files/company_tickers.json
                  (resolves a ticker symbol -> 10-digit zero-padded CIK)
  * companyconcept (one metric):
                  https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/{taxonomy}/{tag}.json
  * companyfacts (all metrics):
                  https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json

IMPORTANT: The SEC requires every request to send a *descriptive* User-Agent
header that identifies the requester (ideally with contact info). Requests
without one are rejected with HTTP 403. See:
https://www.sec.gov/os/accessing-edgar-data

The User-Agent is taken from the SEC_USER_AGENT environment variable if set,
otherwise a sensible default is used. No secrets or API keys are required or
read by this tool. (EDGAR is entirely free and keyless.)

Design notes:
  * Standard library only (urllib, json, argparse) -- no pip dependencies.
  * Immutable style: functions return new values; no in-place mutation of
    shared state.
  * Comprehensive error handling with actionable messages.

CLI examples:
  python3 tools/fetch_edgar.py AAPL --metric Revenues
  python3 tools/fetch_edgar.py AAPL --metric NetIncomeLoss --units USD
  python3 tools/fetch_edgar.py MSFT --list                # list common metrics
  python3 tools/fetch_edgar.py AAPL --metric Revenues --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants (no hardcoded secrets; only public, free endpoints)
# ---------------------------------------------------------------------------

TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
COMPANY_CONCEPT_URL = (
    "https://data.sec.gov/api/xbrl/companyconcept/"
    "CIK{cik}/{taxonomy}/{tag}.json"
)
COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

DEFAULT_USER_AGENT = (
    "decade-x-investing-skill/1.0 (contact: set SEC_USER_AGENT env var)"
)

# A small, friendly catalog of frequently used US-GAAP XBRL tags so a user does
# not have to memorize XBRL taxonomy names. The CLI still accepts any raw tag.
COMMON_METRICS: Dict[str, str] = {
    "Revenues": "Total revenue (US-GAAP: Revenues / RevenueFromContractWithCustomerExcludingAssessedTax)",
    "RevenueFromContractWithCustomerExcludingAssessedTax": "Revenue (ASC 606)",
    "NetIncomeLoss": "Net income (loss)",
    "EarningsPerShareDiluted": "Diluted EPS",
    "EarningsPerShareBasic": "Basic EPS",
    "OperatingIncomeLoss": "Operating income (loss)",
    "GrossProfit": "Gross profit",
    "Assets": "Total assets",
    "Liabilities": "Total liabilities",
    "StockholdersEquity": "Stockholders' equity",
    "CashAndCashEquivalentsAtCarryingValue": "Cash & cash equivalents",
    "NetCashProvidedByUsedInOperatingActivities": "Operating cash flow (CFO)",
    "PaymentsToAcquirePropertyPlantAndEquipment": "CapEx (for FCF = CFO - CapEx)",
    "ResearchAndDevelopmentExpense": "R&D expense",
    "CommonStockSharesOutstanding": "Common shares outstanding",
    "WeightedAverageNumberOfDilutedSharesOutstanding": "Diluted weighted-avg shares",
}

DEFAULT_TIMEOUT_SECONDS = 30


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------


def resolve_user_agent() -> str:
    """Return the User-Agent header, preferring the SEC_USER_AGENT env var.

    The SEC requires a descriptive User-Agent. There is no secret involved --
    this is contact/identification info, intentionally optional via env.
    """
    return os.environ.get("SEC_USER_AGENT", DEFAULT_USER_AGENT).strip() or DEFAULT_USER_AGENT


def fetch_json(url: str, user_agent: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:
    """Fetch and parse a JSON document from `url`.

    Raises RuntimeError with an actionable message on any failure. Returns the
    parsed JSON (dict/list). Performs no mutation of inputs.
    """
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            encoding = response.headers.get("Content-Encoding", "")
            if "gzip" in encoding:
                import gzip

                raw = gzip.decompress(raw)
            text = raw.decode("utf-8")
        return json.loads(text)
    except urllib.error.HTTPError as exc:
        if exc.code == 403:
            raise RuntimeError(
                "SEC returned HTTP 403 (Forbidden). The SEC requires a "
                "descriptive User-Agent header. Set the SEC_USER_AGENT "
                "environment variable to something like "
                "'YourName your.email@example.com' and retry.\n"
                f"URL: {url}"
            ) from exc
        if exc.code == 404:
            raise RuntimeError(
                f"SEC returned HTTP 404 (Not Found) for {url}. The company or "
                "metric may not exist with this taxonomy/tag, or the CIK is "
                "wrong."
            ) from exc
        raise RuntimeError(
            f"HTTP error {exc.code} from SEC for {url}: {exc.reason}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Network error contacting SEC ({url}): {exc.reason}. "
            "Check your internet connection."
        ) from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Failed to parse JSON from SEC ({url}): {exc}"
        ) from exc
    except Exception as exc:  # pragma: no cover - defensive catch-all
        raise RuntimeError(f"Unexpected error fetching {url}: {exc}") from exc


# ---------------------------------------------------------------------------
# Ticker -> CIK resolution
# ---------------------------------------------------------------------------


def resolve_ticker_to_cik(ticker: str, user_agent: str) -> Tuple[str, str]:
    """Resolve a ticker symbol to (zero-padded 10-digit CIK, company title).

    Uses the SEC's public company_tickers.json. Case-insensitive. Raises
    RuntimeError if the ticker is not found.
    """
    normalized = ticker.strip().upper()
    if not normalized:
        raise RuntimeError("Ticker symbol is empty.")

    data = fetch_json(TICKER_MAP_URL, user_agent)
    if not isinstance(data, dict):
        raise RuntimeError(
            "Unexpected shape for SEC ticker map (expected an object)."
        )

    # The map is keyed by an arbitrary index; each value is
    # {"cik_str": int, "ticker": str, "title": str}. Build an immutable lookup.
    matches = [
        entry
        for entry in data.values()
        if isinstance(entry, dict)
        and str(entry.get("ticker", "")).upper() == normalized
    ]
    if not matches:
        raise RuntimeError(
            f"Ticker '{normalized}' was not found in the SEC ticker map. "
            "It may be delisted, foreign-only, or misspelled."
        )

    entry = matches[0]
    cik_int = int(entry["cik_str"])
    cik_padded = str(cik_int).zfill(10)
    title = str(entry.get("title", "")).strip() or normalized
    return cik_padded, title


# ---------------------------------------------------------------------------
# Metric extraction
# ---------------------------------------------------------------------------


def pick_units_series(units: Dict[str, Any], preferred: Optional[str]) -> Tuple[str, List[Dict[str, Any]]]:
    """Choose which units series to use from a companyconcept `units` map.

    Returns (unit_key, list_of_facts). If `preferred` is given and present, use
    it; otherwise pick the unit with the most observations. Pure function.
    """
    if not isinstance(units, dict) or not units:
        raise RuntimeError("No 'units' data present for this metric.")

    if preferred and preferred in units:
        return preferred, list(units[preferred])

    # Deterministic fallback: most-populated series, tie-broken by name.
    ranked = sorted(
        units.items(),
        key=lambda kv: (-len(kv[1]) if isinstance(kv[1], list) else 0, kv[0]),
    )
    unit_key, facts = ranked[0]
    return unit_key, list(facts if isinstance(facts, list) else [])


def latest_annual_facts(facts: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    """Return up to `limit` most recent annual (form 10-K, fp=FY) facts.

    Falls back to all forms if no annual ones are found. Sorted newest-first by
    fiscal year end date. Pure function -- returns a new list.
    """
    def is_annual_period(f: Dict[str, Any]) -> bool:
        # Flow facts (revenue, income) must span ~a full year; point-in-time
        # facts (no 'start': shares outstanding, balance-sheet items) are kept.
        start, end = f.get("start"), f.get("end")
        if not start or not end:
            return True
        try:
            from datetime import date
            return (date.fromisoformat(str(end)) - date.fromisoformat(str(start))).days >= 300
        except Exception:
            return True

    annual = [
        f
        for f in facts
        if isinstance(f, dict)
        and f.get("form") == "10-K"
        and f.get("fp") == "FY"
        and is_annual_period(f)
    ]
    chosen = annual if annual else [f for f in facts if isinstance(f, dict)]

    def sort_key(f: Dict[str, Any]) -> str:
        return str(f.get("end", ""))

    sorted_desc = sorted(chosen, key=sort_key, reverse=True)

    # Deduplicate by fiscal year end ('end'), keeping the first (latest filed).
    seen: set = set()
    deduped: List[Dict[str, Any]] = []
    for f in sorted_desc:
        end = f.get("end")
        if end in seen:
            continue
        seen = seen | {end}
        deduped = deduped + [f]
    return deduped[: max(0, limit)]


def fetch_metric(
    cik: str,
    metric: str,
    user_agent: str,
    taxonomy: str = "us-gaap",
    preferred_units: Optional[str] = None,
    limit: int = 10,
) -> Dict[str, Any]:
    """Fetch a single XBRL concept for a company and shape it for display.

    Returns an immutable result dict with keys: metric, label, taxonomy,
    unit, observations (list of {fy, end, value, form, filed}).
    """
    url = COMPANY_CONCEPT_URL.format(cik=cik, taxonomy=taxonomy, tag=metric)
    data = fetch_json(url, user_agent)

    units = data.get("units", {}) if isinstance(data, dict) else {}
    unit_key, all_facts = pick_units_series(units, preferred_units)
    selected = latest_annual_facts(all_facts, limit)

    observations = [
        {
            "fy": f.get("fy"),
            "end": f.get("end"),
            "value": f.get("val"),
            "form": f.get("form"),
            "filed": f.get("filed"),
        }
        for f in selected
    ]
    return {
        "metric": metric,
        "label": data.get("label") if isinstance(data, dict) else None,
        "description": COMMON_METRICS.get(metric),
        "taxonomy": taxonomy,
        "unit": unit_key,
        "observations": observations,
    }


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------


def humanize_number(value: Any) -> str:
    """Render a numeric value with thousands separators / scaled suffix."""
    if not isinstance(value, (int, float)):
        return str(value)
    abs_v = abs(value)
    if abs_v >= 1_000_000_000:
        return f"{value:,.0f} ({value / 1_000_000_000:.2f}B)"
    if abs_v >= 1_000_000:
        return f"{value:,.0f} ({value / 1_000_000:.2f}M)"
    return f"{value:,}"


def render_human(company: str, cik: str, result: Dict[str, Any]) -> str:
    """Build a human-readable report string. Pure function."""
    lines: List[str] = []
    lines.append(f"Company : {company}")
    lines.append(f"CIK     : {cik}")
    label = result.get("label") or result.get("description") or result["metric"]
    lines.append(f"Metric  : {result['metric']} ({label})")
    lines.append(f"Unit    : {result['unit']}")
    lines.append(f"Taxonomy: {result['taxonomy']}")
    lines.append("")
    header = f"{'FY':<6} {'Period End':<12} {'Value':<28} {'Form':<6} Filed"
    lines.append(header)
    lines.append("-" * len(header))
    if not result["observations"]:
        lines.append("(no observations found)")
    for obs in result["observations"]:
        fy = str(obs.get("fy") or "")
        end = str(obs.get("end") or "")
        value = humanize_number(obs.get("value"))
        form = str(obs.get("form") or "")
        filed = str(obs.get("filed") or "")
        lines.append(f"{fy:<6} {end:<12} {value:<28} {form:<6} {filed}")
    return "\n".join(lines)


def render_metric_catalog() -> str:
    """List the built-in common metrics. Pure function."""
    lines = ["Common metrics (any raw US-GAAP XBRL tag also works):", ""]
    width = max(len(k) for k in COMMON_METRICS)
    for tag, desc in COMMON_METRICS.items():
        lines.append(f"  {tag:<{width}}  {desc}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fetch_edgar.py",
        description=(
            "Fetch US public company financials from SEC EDGAR "
            "(free, no API key). Set SEC_USER_AGENT env to your contact info."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 tools/fetch_edgar.py AAPL --metric Revenues\n"
            "  python3 tools/fetch_edgar.py AAPL --metric NetIncomeLoss\n"
            "  python3 tools/fetch_edgar.py MSFT --list\n"
            "  python3 tools/fetch_edgar.py AAPL --metric Revenues --json\n"
        ),
    )
    parser.add_argument(
        "ticker",
        nargs="?",
        help="Ticker symbol (e.g. AAPL). Resolved to CIK via the SEC map.",
    )
    parser.add_argument(
        "--metric",
        default="Revenues",
        help="XBRL concept tag (default: Revenues). See --list for common tags.",
    )
    parser.add_argument(
        "--taxonomy",
        default="us-gaap",
        help="XBRL taxonomy (default: us-gaap).",
    )
    parser.add_argument(
        "--units",
        default=None,
        help="Preferred units key (e.g. USD, shares, USD/shares). Auto if omitted.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Max number of recent annual observations to show (default: 10).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit raw JSON instead of a formatted table.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List common metric tags and exit (no network for the catalog).",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        print(render_metric_catalog())
        return 0

    if not args.ticker:
        parser.error("a ticker is required unless --list is used")

    user_agent = resolve_user_agent()

    try:
        cik, company = resolve_ticker_to_cik(args.ticker, user_agent)
        result = fetch_metric(
            cik=cik,
            metric=args.metric,
            user_agent=user_agent,
            taxonomy=args.taxonomy,
            preferred_units=args.units,
            limit=args.limit,
        )
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        payload = {
            "company": company,
            "cik": cik,
            "result": result,
        }
        print(json.dumps(payload, indent=2))
    else:
        print(render_human(company, cik, result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
