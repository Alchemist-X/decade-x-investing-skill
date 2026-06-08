#!/usr/bin/env python3
"""Crypto market + on-chain data fetcher (FREE, NO API KEY required).

Pulls live data from two free, keyless public APIs:

  * CoinGecko  (https://api.coingecko.com)  -> price, market cap, volume
  * DefiLlama  (https://api.llama.fi)        -> protocol / chain TVL

Designed for the decade-x-investing skill. Pure Python 3 standard library
only (urllib, json, argparse) -- no pip installs, no third-party deps.

Style notes:
  * Immutable: functions return new dicts/tuples; no in-place mutation of
    caller-supplied data.
  * Robust: every network call is wrapped with helpful, specific errors.
  * No hardcoded secrets. An optional CoinGecko Pro/Demo key may be supplied
    via the COINGECKO_API_KEY environment variable; it is never required.

CLI examples:
    python3 tools/fetch_crypto.py price bitcoin ethereum
    python3 tools/fetch_crypto.py price bitcoin --vs usd,eur
    python3 tools/fetch_crypto.py markets bitcoin ethereum solana
    python3 tools/fetch_crypto.py tvl ethereum
    python3 tools/fetch_crypto.py protocol-tvl aave
    python3 tools/fetch_crypto.py price bitcoin --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #

COINGECKO_BASE = "https://api.coingecko.com/api/v3"
DEFILLAMA_BASE = "https://api.llama.fi"
USER_AGENT = "decade-x-investing/fetch_crypto (stdlib urllib)"
DEFAULT_TIMEOUT = 30  # seconds


# --------------------------------------------------------------------------- #
# HTTP helper
# --------------------------------------------------------------------------- #

def _http_get_json(url, timeout=DEFAULT_TIMEOUT):
    """Perform an HTTP GET and decode the JSON body.

    Returns the parsed JSON object. Raises RuntimeError with a clear,
    user-friendly message on any failure (network, HTTP status, JSON decode).
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}

    # Optional CoinGecko key from env -- never required, never hardcoded.
    api_key = os.environ.get("COINGECKO_API_KEY")
    if api_key and "coingecko.com" in url:
        # CoinGecko accepts the demo key via this header on the public host.
        headers["x-cg-demo-api-key"] = api_key

    request = urllib.request.Request(url, headers=headers, method="GET")

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
    except urllib.error.HTTPError as error:
        body = ""
        try:
            body = error.read().decode("utf-8", errors="replace")[:300]
        except Exception:  # noqa: BLE001 - body is best-effort only
            body = "<unavailable>"
        if error.code == 429:
            raise RuntimeError(
                "Rate limited by the API (HTTP 429). The free tier is limited; "
                "wait ~60s and retry, or set COINGECKO_API_KEY for a demo key."
            ) from error
        raise RuntimeError(
            f"HTTP {error.code} from {url}\nResponse: {body}"
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(
            f"Network error reaching {url}: {error.reason}. "
            "Check your internet connection."
        ) from error
    except TimeoutError as error:
        raise RuntimeError(
            f"Request to {url} timed out after {timeout}s."
        ) from error

    try:
        return json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as error:
        preview = raw[:200].decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Failed to parse JSON from {url}: {error}\nFirst bytes: {preview}"
        ) from error


def _build_url(base, path, params=None):
    """Return a fully-formed URL. Does not mutate inputs."""
    query = ""
    if params:
        # Drop None values, then urlencode a fresh dict.
        clean = {key: value for key, value in params.items() if value is not None}
        if clean:
            query = "?" + urllib.parse.urlencode(clean)
    return f"{base}{path}{query}"


# --------------------------------------------------------------------------- #
# CoinGecko fetchers
# --------------------------------------------------------------------------- #

def fetch_price(coin_ids, vs_currencies=("usd",)):
    """Fetch simple price + market data for one or more CoinGecko coin ids.

    Args:
        coin_ids: iterable of CoinGecko ids, e.g. ["bitcoin", "ethereum"].
        vs_currencies: iterable of fiat/crypto quote currencies, e.g. ["usd"].

    Returns:
        dict keyed by coin id; each value holds price/mktcap/vol/24h-change
        for every requested currency. Example shape:
        {"bitcoin": {"usd": 60000, "usd_market_cap": ..., ...}}
    """
    ids = ",".join(coin_ids)
    vs = ",".join(vs_currencies)
    if not ids.strip():
        raise ValueError("At least one coin id is required for 'price'.")

    url = _build_url(
        COINGECKO_BASE,
        "/simple/price",
        {
            "ids": ids,
            "vs_currencies": vs,
            "include_market_cap": "true",
            "include_24hr_vol": "true",
            "include_24hr_change": "true",
            "include_last_updated_at": "true",
        },
    )
    data = _http_get_json(url)
    if not data:
        raise RuntimeError(
            f"CoinGecko returned no data for ids='{ids}'. "
            "Are the coin ids valid? (use lowercase ids like 'bitcoin')."
        )
    return data


def fetch_markets(coin_ids, vs_currency="usd"):
    """Fetch rich market rows (rank, ATH, supply, etc.) for given coin ids."""
    ids = ",".join(coin_ids)
    if not ids.strip():
        raise ValueError("At least one coin id is required for 'markets'.")

    url = _build_url(
        COINGECKO_BASE,
        "/coins/markets",
        {
            "vs_currency": vs_currency,
            "ids": ids,
            "order": "market_cap_desc",
            "per_page": str(max(1, len(coin_ids))),
            "page": "1",
            "sparkline": "false",
            "price_change_percentage": "24h,7d,30d",
        },
    )
    data = _http_get_json(url)
    if not isinstance(data, list) or not data:
        raise RuntimeError(
            f"CoinGecko /coins/markets returned no rows for ids='{ids}'."
        )
    return tuple(data)


# --------------------------------------------------------------------------- #
# DefiLlama fetchers
# --------------------------------------------------------------------------- #

def fetch_chain_tvl(chain):
    """Fetch current total TVL (USD) for a chain, e.g. 'ethereum'.

    Uses DefiLlama's /v2/chains endpoint and selects the matching chain.
    Returns a dict: {"name": ..., "tvl": float, "tokenSymbol": ...}.
    """
    if not chain or not chain.strip():
        raise ValueError("A chain name is required for 'tvl'.")

    url = _build_url(DEFILLAMA_BASE, "/v2/chains")
    data = _http_get_json(url)
    if not isinstance(data, list):
        raise RuntimeError("DefiLlama /v2/chains returned an unexpected shape.")

    target = chain.strip().lower()
    for row in data:
        name = str(row.get("name", "")).lower()
        gecko = str(row.get("gecko_id", "")).lower()
        if target in (name, gecko):
            # Return a fresh dict; do not hand back the live API object.
            return {
                "name": row.get("name"),
                "tvl": row.get("tvl"),
                "tokenSymbol": row.get("tokenSymbol"),
                "gecko_id": row.get("gecko_id"),
                "cmcId": row.get("cmcId"),
            }

    available = sorted(str(r.get("name", "")) for r in data if r.get("name"))
    hint = ", ".join(available[:15])
    raise RuntimeError(
        f"Chain '{chain}' not found on DefiLlama. "
        f"Some valid names: {hint} ..."
    )


def fetch_protocol_tvl(protocol):
    """Fetch current TVL (USD) for a single DeFi protocol slug, e.g. 'aave'."""
    if not protocol or not protocol.strip():
        raise ValueError("A protocol slug is required for 'protocol-tvl'.")

    slug = protocol.strip().lower()
    url = _build_url(DEFILLAMA_BASE, f"/tvl/{urllib.parse.quote(slug)}")
    data = _http_get_json(url)

    # /tvl/{slug} returns a bare number on success.
    if isinstance(data, (int, float)):
        return {"protocol": slug, "tvl": float(data)}
    raise RuntimeError(
        f"Unexpected response for protocol '{slug}': {data!r}. "
        "Use the DefiLlama slug (lowercase, e.g. 'aave', 'lido', 'uniswap')."
    )


# --------------------------------------------------------------------------- #
# Formatting helpers (pure functions)
# --------------------------------------------------------------------------- #

def _fmt_usd(value):
    """Human-friendly USD formatting; tolerates None."""
    if value is None:
        return "n/a"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    if abs(number) >= 1_000_000_000:
        return f"${number / 1_000_000_000:,.2f}B"
    if abs(number) >= 1_000_000:
        return f"${number / 1_000_000:,.2f}M"
    if abs(number) >= 1:
        return f"${number:,.2f}"
    return f"${number:,.6f}"


def _render_price(data, vs_currencies):
    """Build a human-readable price report string. Pure function."""
    lines = []
    for coin_id in sorted(data.keys()):
        entry = data[coin_id]
        lines.append(f"{coin_id}:")
        for currency in vs_currencies:
            price = entry.get(currency)
            mcap = entry.get(f"{currency}_market_cap")
            vol = entry.get(f"{currency}_24h_vol")
            change = entry.get(f"{currency}_24h_change")
            change_str = f"{change:+.2f}%" if isinstance(change, (int, float)) else "n/a"
            lines.append(
                f"  {currency.upper()}  price={_fmt_usd(price)}  "
                f"mktcap={_fmt_usd(mcap)}  vol24h={_fmt_usd(vol)}  "
                f"chg24h={change_str}"
            )
    return "\n".join(lines)


def _render_markets(rows):
    """Build a human-readable markets report string. Pure function."""
    lines = []
    for row in rows:
        lines.append(
            f"{row.get('id')} ({str(row.get('symbol', '')).upper()})  "
            f"rank=#{row.get('market_cap_rank')}  "
            f"price={_fmt_usd(row.get('current_price'))}  "
            f"mktcap={_fmt_usd(row.get('market_cap'))}  "
            f"vol24h={_fmt_usd(row.get('total_volume'))}  "
            f"chg24h={row.get('price_change_percentage_24h_in_currency')}"
        )
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def _build_parser():
    parser = argparse.ArgumentParser(
        prog="fetch_crypto.py",
        description="Free, keyless crypto market + on-chain data fetcher "
                    "(CoinGecko + DefiLlama).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python3 tools/fetch_crypto.py price bitcoin ethereum\n"
            "  python3 tools/fetch_crypto.py markets bitcoin ethereum solana\n"
            "  python3 tools/fetch_crypto.py tvl ethereum\n"
            "  python3 tools/fetch_crypto.py protocol-tvl aave\n"
        ),
    )
    # A shared parent parser so --json works before OR after the subcommand.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--json",
        action="store_true",
        help="emit raw JSON instead of a formatted report",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit raw JSON instead of a formatted report",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_price = sub.add_parser(
        "price", parents=[common], help="simple price/mktcap/volume")
    p_price.add_argument("coins", nargs="+", help="CoinGecko ids, e.g. bitcoin")
    p_price.add_argument(
        "--vs", default="usd",
        help="comma-separated quote currencies (default: usd)",
    )

    p_markets = sub.add_parser(
        "markets", parents=[common], help="rich market rows")
    p_markets.add_argument("coins", nargs="+", help="CoinGecko ids")
    p_markets.add_argument("--vs", default="usd", help="quote currency (default: usd)")

    p_tvl = sub.add_parser(
        "tvl", parents=[common], help="chain TVL via DefiLlama")
    p_tvl.add_argument("chain", help="chain name, e.g. ethereum")

    p_ptvl = sub.add_parser(
        "protocol-tvl", parents=[common], help="protocol TVL via DefiLlama")
    p_ptvl.add_argument("protocol", help="protocol slug, e.g. aave")

    return parser


def _run(args):
    """Dispatch a parsed args namespace to a fetcher and print results.

    Returns a process exit code (0 == success).
    """
    if args.command == "price":
        vs_list = tuple(c.strip().lower() for c in args.vs.split(",") if c.strip())
        data = fetch_price(tuple(args.coins), vs_list)
        if args.json:
            print(json.dumps(data, indent=2))
        else:
            print(_render_price(data, vs_list))
        return 0

    if args.command == "markets":
        rows = fetch_markets(tuple(args.coins), args.vs.strip().lower())
        if args.json:
            print(json.dumps(list(rows), indent=2))
        else:
            print(_render_markets(rows))
        return 0

    if args.command == "tvl":
        result = fetch_chain_tvl(args.chain)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(
                f"{result['name']} chain TVL: {_fmt_usd(result['tvl'])}  "
                f"(token={result.get('tokenSymbol')})"
            )
        return 0

    if args.command == "protocol-tvl":
        result = fetch_protocol_tvl(args.protocol)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"{result['protocol']} protocol TVL: {_fmt_usd(result['tvl'])}")
        return 0

    raise ValueError(f"Unknown command: {args.command}")


def main(argv=None):
    """Entry point. Returns an exit code; never raises to the shell."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        return _run(args)
    except (RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
