#!/usr/bin/env python3
"""DecadeX-style quantitative valuation helpers (pure, no network).

This is a self-contained data tool for the `decade-x-investing` skill. It
implements three small, deterministic valuation primitives that recur across
DecadeX (未来十年投资学堂) reports and that an analyst is expected to compute
*with numbers* rather than merely name:

  1. reverse_dcf()       -- 反向 DCF: solve for the FCF growth rate that the
                            current market cap *implies*, so you can judge
                            whether the market's embedded expectation is sane
                            (Step 6 估值 / sanity-check on a price).
  2. scenario_value()    -- 三情景概率加权估值: Bear/Base/Bull probability
                            weighting into a single expectation + upside.
  3. owner_earnings_yield() -- Buffett-style owner-earnings (a.k.a. FCF) yield,
                            the cash-return anchor used in DecadeX's cash-cow
                            and FCF-yield screens.

Design notes
------------
* Python 3 standard library ONLY (urllib, json, argparse). No pip, no network.
  All computation is pure: no I/O happens inside the math functions.
* Immutable style: functions take inputs and return NEW dicts/values; no
  argument is ever mutated. Inputs are defensively copied where iterated.
* No hardcoded secrets. An OPTIONAL API key may be read from the environment
  (DECADEX_API_KEY) purely for forward-compatibility / labelling; it is never
  required and never transmitted (this tool makes no network calls).
* Robust validation with helpful, specific error messages.

DISCLAIMER: Educational. Reproduces a research *method*, not financial advice.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, Iterable, List, Mapping, Sequence

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_YEARS: int = 10               # DecadeX horizon: "未来十年" / a decade
_ENV_API_KEY: str = "DECADEX_API_KEY"  # optional, NOT required, never sent


# ---------------------------------------------------------------------------
# Validation helpers (pure)
# ---------------------------------------------------------------------------

def _require_positive(name: str, value: Any) -> float:
    """Return ``value`` as float, or raise a helpful ValueError if not > 0."""
    try:
        out = float(value)
    except (TypeError, ValueError):
        raise ValueError(
            f"{name!r} must be a number, got {value!r}."
        ) from None
    if out != out:  # NaN check without importing math
        raise ValueError(f"{name!r} must not be NaN.")
    if out <= 0:
        raise ValueError(f"{name!r} must be positive, got {out!r}.")
    return out


def _require_rate(name: str, value: Any, *, low: float = -0.99,
                  high: float = 1.0) -> float:
    """Return ``value`` as a float rate within (low, high], else raise."""
    try:
        out = float(value)
    except (TypeError, ValueError):
        raise ValueError(
            f"{name!r} must be a number (a rate like 0.10 = 10%), got {value!r}."
        ) from None
    if out != out:
        raise ValueError(f"{name!r} must not be NaN.")
    if not (low < out <= high):
        raise ValueError(
            f"{name!r}={out!r} is out of range; expected a rate in "
            f"({low}, {high}] (e.g. 0.10 for 10%)."
        )
    return out


# ---------------------------------------------------------------------------
# (1) Reverse DCF
# ---------------------------------------------------------------------------

def _gordon_terminal_value(final_fcf: float, discount_rate: float,
                           terminal_growth: float) -> float:
    """Gordon-growth terminal value at the end of the explicit period.

    TV = FCF_final * (1 + g_terminal) / (r - g_terminal).
    """
    spread = discount_rate - terminal_growth
    if spread <= 0:
        raise ValueError(
            "discount_rate must exceed terminal_growth for a finite terminal "
            f"value (got discount={discount_rate}, terminal_growth="
            f"{terminal_growth})."
        )
    return final_fcf * (1.0 + terminal_growth) / spread


def _intrinsic_value(fcf: float, growth: float, discount_rate: float,
                     terminal_growth: float, years: int) -> float:
    """Present value of `years` of FCF growing at `growth`, + terminal value.

    Pure function: returns a fresh float, mutates nothing.
    """
    pv_total = 0.0
    current_fcf = fcf
    for year in range(1, years + 1):
        current_fcf = current_fcf * (1.0 + growth)
        pv_total += current_fcf / ((1.0 + discount_rate) ** year)
    terminal = _gordon_terminal_value(current_fcf, discount_rate,
                                      terminal_growth)
    pv_total += terminal / ((1.0 + discount_rate) ** years)
    return pv_total


def reverse_dcf(market_cap: float, fcf: float, discount_rate: float,
                terminal_growth: float, years: int = DEFAULT_YEARS) -> Dict[str, Any]:
    """Solve for the FCF growth rate implied by today's market cap (反向 DCF).

    Standard DCF asks "given a growth assumption, what is the asset worth?".
    Reverse DCF inverts it: "given today's price, what FCF growth must the
    market be assuming?". The implied growth is then judged for plausibility
    against the asset's history and TAM (DecadeX Step 6 sanity check).

    The intrinsic value is strictly increasing in the growth rate, so we solve
    for the root with a deterministic bisection (no SciPy needed).

    Args:
        market_cap: Current enterprise/market value the asset trades at (> 0).
        fcf: Latest trailing free cash flow / owner earnings (> 0).
        discount_rate: Required return r, e.g. 0.10 for 10% (0 < r <= 1).
        terminal_growth: Perpetual growth g after the explicit period; must be
            strictly below `discount_rate` (e.g. 0.03 for 3%).
        years: Length of the explicit forecast period (default 10).

    Returns:
        A NEW dict with the implied growth rate and diagnostics::

            {
              "implied_fcf_growth": 0.1234,        # as a decimal
              "implied_fcf_growth_pct": 12.34,     # convenience, %
              "market_cap": ..., "fcf": ...,
              "discount_rate": ..., "terminal_growth": ...,
              "years": 10,
              "implied_starting_multiple": market_cap / fcf,  # P/FCF
              "converged": True,
              "iterations": 47,
              "note": "..."
            }

    Raises:
        ValueError: on invalid inputs, or if no growth rate in the searched
            range reproduces the price (e.g. the price is below the value of a
            zero-growth perpetuity floor, implying negative growth beyond the
            search bound).
    """
    mc = _require_positive("market_cap", market_cap)
    f = _require_positive("fcf", fcf)
    r = _require_rate("discount_rate", discount_rate, low=0.0, high=1.0)
    g_term = _require_rate("terminal_growth", terminal_growth,
                           low=-0.99, high=1.0)
    if g_term >= r:
        raise ValueError(
            f"terminal_growth ({g_term}) must be strictly below discount_rate "
            f"({r}) for a finite valuation."
        )
    try:
        yrs = int(years)
    except (TypeError, ValueError):
        raise ValueError(f"years must be an integer, got {years!r}.") from None
    if yrs < 1:
        raise ValueError(f"years must be >= 1, got {yrs}.")

    # Search bounds for the explicit-period growth rate. The explicit-period
    # sum is finite for ANY growth rate (it is a finite geometric sum), so the
    # explicit growth may legitimately exceed the discount rate -- only the
    # *terminal* (perpetuity) growth must stay below r, which `terminal_growth`
    # already enforces. We therefore search a wide upper bound (1000%/yr) so the
    # tool can recover the aggressive growth high-multiple names actually imply.
    lo, hi = -0.99, 10.0
    value_lo = _intrinsic_value(f, lo, r, g_term, yrs)
    value_hi = _intrinsic_value(f, hi, r, g_term, yrs)

    if mc < value_lo:
        raise ValueError(
            "market_cap is below the intrinsic value even at the most "
            f"pessimistic searched growth ({lo:.0%}); implied growth is more "
            "negative than this tool searches. The market is pricing a steeper "
            "decline than the model floor."
        )
    if mc > value_hi:
        raise ValueError(
            "market_cap exceeds the intrinsic value even at the maximum "
            f"searched explicit growth ({hi:.0%}/yr for {yrs}yr). The price "
            "implies extraordinary, almost certainly unsustainable growth; "
            "treat the asset as a pure narrative bet or revisit the inputs "
            "(discount rate, FCF base, horizon)."
        )

    # Bisection: value(growth) is monotonically increasing in growth.
    iterations = 0
    implied = lo
    for iterations in range(1, 201):
        mid = (lo + hi) / 2.0
        value_mid = _intrinsic_value(f, mid, r, g_term, yrs)
        if abs(value_mid - mc) <= max(1.0, mc * 1e-9):
            implied = mid
            break
        if value_mid < mc:
            lo = mid
        else:
            hi = mid
        implied = mid

    converged = abs(_intrinsic_value(f, implied, r, g_term, yrs) - mc) <= max(
        1.0, mc * 1e-6)

    return {
        "implied_fcf_growth": implied,
        "implied_fcf_growth_pct": implied * 100.0,
        "market_cap": mc,
        "fcf": f,
        "discount_rate": r,
        "terminal_growth": g_term,
        "years": yrs,
        "implied_starting_multiple": mc / f,
        "converged": bool(converged),
        "iterations": iterations,
        "note": (
            f"Today's price implies ~{implied * 100:.2f}% annual FCF growth for "
            f"{yrs}yr, then {g_term * 100:.1f}% perpetual. Judge this against "
            "the asset's history and TAM, not in isolation."
        ),
    }


# ---------------------------------------------------------------------------
# (2) Scenario (probability-weighted) value -- 三情景概率加权估值
# ---------------------------------------------------------------------------

def scenario_value(scenarios: Sequence[Mapping[str, Any]],
                   current_price: float | None = None,
                   *, tol: float = 1e-6) -> Dict[str, Any]:
    """Probability-weight Bear/Base/Bull scenarios into one expectation.

    DecadeX's signature valuation output (三情景概率加权估值): each scenario
    carries a probability and a per-unit value; the expectation is the
    probability-weighted mean, and the upside is measured vs `current_price`.

    Args:
        scenarios: An iterable of mappings, each with::
                {"prob": 0.5, "value": 250.0, "label": "Base"}  # label optional
            Probabilities must be non-negative and sum to ~1.0 (within `tol`).
        current_price: Optional current price; if given, expected upside and
            per-scenario upside are computed. Must be > 0 when provided.
        tol: Allowed deviation of the probability sum from 1.0.

    Returns:
        A NEW dict::
            {
              "expected_value": 237.5,
              "scenarios": [ {label, prob, value, weighted, upside?}, ... ],
              "current_price": 200.0 | None,
              "expected_upside_pct": 18.75 | None,
              "prob_sum": 1.0,
              "best_case": {...}, "worst_case": {...},
              "note": "..."
            }
        The returned scenario dicts are FRESH copies; inputs are not mutated.

    Raises:
        ValueError: empty input, bad probabilities, non-numeric values, or a
            probability sum that does not round to 1.0 within `tol`.
    """
    # Defensive immutable snapshot of the inputs.
    items: List[Mapping[str, Any]] = list(scenarios)
    if not items:
        raise ValueError("scenarios must be a non-empty list of {prob, value}.")

    cleaned: List[Dict[str, Any]] = []
    prob_sum = 0.0
    for idx, raw in enumerate(items):
        if not isinstance(raw, Mapping):
            raise ValueError(
                f"scenario #{idx} must be a mapping with 'prob' and 'value', "
                f"got {raw!r}."
            )
        if "prob" not in raw or "value" not in raw:
            raise ValueError(
                f"scenario #{idx} is missing 'prob' or 'value': {dict(raw)!r}."
            )
        try:
            prob = float(raw["prob"])
            value = float(raw["value"])
        except (TypeError, ValueError):
            raise ValueError(
                f"scenario #{idx} has non-numeric prob/value: {dict(raw)!r}."
            ) from None
        if prob < 0:
            raise ValueError(
                f"scenario #{idx} probability must be >= 0, got {prob}."
            )
        if prob != prob or value != value:
            raise ValueError(f"scenario #{idx} contains NaN.")
        label = str(raw.get("label", f"S{idx + 1}"))
        prob_sum += prob
        cleaned.append({"label": label, "prob": prob, "value": value,
                        "weighted": prob * value})

    if abs(prob_sum - 1.0) > tol:
        raise ValueError(
            f"scenario probabilities must sum to 1.0 (within {tol}); they sum "
            f"to {prob_sum:.6f}. Re-normalize the weights."
        )

    expected_value = sum(item["weighted"] for item in cleaned)

    result: Dict[str, Any] = {
        "expected_value": expected_value,
        "prob_sum": prob_sum,
        "current_price": None,
        "expected_upside_pct": None,
    }

    if current_price is not None:
        price = _require_positive("current_price", current_price)
        result["current_price"] = price
        result["expected_upside_pct"] = (expected_value / price - 1.0) * 100.0
        cleaned = [
            {**item, "upside_pct": (item["value"] / price - 1.0) * 100.0}
            for item in cleaned
        ]

    # best/worst by value (fresh copies, no mutation of `cleaned`).
    best = max(cleaned, key=lambda d: d["value"])
    worst = min(cleaned, key=lambda d: d["value"])

    result["scenarios"] = cleaned
    result["best_case"] = dict(best)
    result["worst_case"] = dict(worst)
    upside_txt = (
        f", expected upside {result['expected_upside_pct']:+.2f}% vs price"
        if result["expected_upside_pct"] is not None else ""
    )
    result["note"] = (
        f"Probability-weighted expected value {expected_value:,.2f}{upside_txt}. "
        "Band, don't point-target."
    )
    return result


# ---------------------------------------------------------------------------
# (3) Owner-earnings (FCF) yield
# ---------------------------------------------------------------------------

def owner_earnings_yield(owner_earnings: float, market_cap: float) -> Dict[str, Any]:
    """Owner-earnings (FCF) yield = owner_earnings / market_cap.

    The cash-return anchor in DecadeX's cash-cow / FCF-yield screens
    (e.g. "FCF yield >= 4%"). Owner earnings ~= FCF (Buffett: net income +
    D&A - maintenance capex - working-capital needs).

    Args:
        owner_earnings: Annual owner earnings / free cash flow (> 0).
        market_cap: Current market capitalization (> 0).

    Returns:
        A NEW dict::
            {"owner_earnings_yield": 0.045,
             "owner_earnings_yield_pct": 4.5,
             "price_to_owner_earnings": 22.2,
             "owner_earnings": ..., "market_cap": ...,
             "note": "..."}

    Raises:
        ValueError: if either input is not a positive number.
    """
    oe = _require_positive("owner_earnings", owner_earnings)
    mc = _require_positive("market_cap", market_cap)
    yield_ratio = oe / mc
    return {
        "owner_earnings_yield": yield_ratio,
        "owner_earnings_yield_pct": yield_ratio * 100.0,
        "price_to_owner_earnings": mc / oe,
        "owner_earnings": oe,
        "market_cap": mc,
        "note": (
            f"Owner-earnings yield {yield_ratio * 100:.2f}% "
            f"(P/OE {mc / oe:.1f}x). DecadeX cash-cow screen wants >= 4%."
        ),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _emit(payload: Mapping[str, Any]) -> None:
    """Pretty-print a result mapping as JSON to stdout."""
    sys.stdout.write(json.dumps(dict(payload), indent=2, ensure_ascii=False))
    sys.stdout.write("\n")


def _demo_scenarios() -> List[Dict[str, float]]:
    """Canonical Bear/Base/Bull demo (immutable fresh list each call)."""
    return [
        {"label": "Bear", "prob": 0.25, "value": 120.0},
        {"label": "Base", "prob": 0.50, "value": 250.0},
        {"label": "Bull", "prob": 0.25, "value": 480.0},
    ]


def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI parser (pure: builds and returns a new parser)."""
    parser = argparse.ArgumentParser(
        prog="analyze.py",
        description=(
            "DecadeX-style pure quantitative valuation helpers "
            "(reverse DCF, scenario weighting, owner-earnings yield). "
            "Educational, not financial advice."
        ),
        epilog=(
            "Examples:\n"
            "  python3 tools/analyze.py reverse-dcf --mktcap 3e12 --fcf 9e10 "
            "--discount 0.10 --tgrowth 0.03\n"
            "  python3 tools/analyze.py scenarios\n"
            "  python3 tools/analyze.py owner-yield --oe 9e10 --mktcap 3e12\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_rdcf = sub.add_parser(
        "reverse-dcf",
        help="Solve for the FCF growth rate implied by the current price.")
    p_rdcf.add_argument("--mktcap", required=True, type=float,
                        help="Market cap / enterprise value (e.g. 3e12).")
    p_rdcf.add_argument("--fcf", required=True, type=float,
                        help="Latest trailing free cash flow (e.g. 9e10).")
    p_rdcf.add_argument("--discount", required=True, type=float,
                        help="Discount rate r, e.g. 0.10 for 10%%.")
    p_rdcf.add_argument("--tgrowth", required=True, type=float,
                        help="Terminal growth g, e.g. 0.03 for 3%%.")
    p_rdcf.add_argument("--years", type=int, default=DEFAULT_YEARS,
                        help=f"Explicit forecast years (default {DEFAULT_YEARS}).")

    p_scn = sub.add_parser(
        "scenarios",
        help="Probability-weight scenarios. Runs the Bear/Base/Bull demo, or "
             "pass --json with your own list.")
    p_scn.add_argument(
        "--json", default=None,
        help=('JSON list of scenarios, e.g. '
              '\'[{"label":"Bear","prob":0.3,"value":100},'
              '{"label":"Bull","prob":0.7,"value":300}]\'. '
              'Omit to run the built-in demo.'))
    p_scn.add_argument("--price", type=float, default=None,
                       help="Optional current price for upside calc.")

    p_oe = sub.add_parser(
        "owner-yield",
        help="Owner-earnings (FCF) yield = owner_earnings / market_cap.")
    p_oe.add_argument("--oe", required=True, type=float,
                      help="Annual owner earnings / FCF (e.g. 9e10).")
    p_oe.add_argument("--mktcap", required=True, type=float,
                      help="Market cap (e.g. 3e12).")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point. Returns a process exit code (0 ok, 2 on error)."""
    parser = build_parser()
    args = parser.parse_args(argv)

    # Optional API key (forward-compat / labelling only; NEVER required or sent).
    api_key_present = bool(os.environ.get(_ENV_API_KEY))

    try:
        if args.command == "reverse-dcf":
            result = reverse_dcf(
                market_cap=args.mktcap, fcf=args.fcf,
                discount_rate=args.discount, terminal_growth=args.tgrowth,
                years=args.years)
        elif args.command == "scenarios":
            if args.json:
                try:
                    parsed = json.loads(args.json)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"--json is not valid JSON: {exc}") from exc
                scenarios = parsed
            else:
                scenarios = _demo_scenarios()
            result = scenario_value(scenarios, current_price=args.price)
        elif args.command == "owner-yield":
            result = owner_earnings_yield(
                owner_earnings=args.oe, market_cap=args.mktcap)
        else:  # pragma: no cover - argparse enforces choices
            parser.error(f"unknown command {args.command!r}")
            return 2
    except ValueError as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 2
    except Exception as exc:  # pragma: no cover - last-resort safety net
        sys.stderr.write(f"unexpected error: {type(exc).__name__}: {exc}\n")
        return 2

    enriched = {**result, "_api_key_detected": api_key_present}
    _emit(enriched)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
