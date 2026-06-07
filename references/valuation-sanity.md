# Valuation Sanity Checks

> **Educational only. Not financial advice. Investing involves risk of loss. These frameworks do not produce price targets or buy/sell recommendations.**

The goal here is not precision — it is to identify whether a price implies assumptions that are plausible, stretched, or absurd given base rates. A valuation sanity check asks: "What does this price require me to believe, and how often does that happen?"

---

## Framework 1 — Reverse DCF Intuition

Instead of projecting cash flows forward to justify a price, work backward from the current price to discover the implied assumptions.

**Steps:**

1. Find (or estimate) current owner earnings or free cash flow (FCF).
2. Assume a long-run discount rate (use 8–10% as a base; adjust for risk).
3. Assume a terminal growth rate (use GDP growth — roughly 2–3% nominal — as a ceiling for most mature businesses; faster-growing businesses might justify 4–5% for the first phase).
4. Solve for: what revenue growth and margin expansion are required to justify the current price?

**Key question:** Is the implied growth rate in the top decile of historical outcomes for this industry? What percentage of comparable companies achieved it over 10 years?

**Reference base rates (rough):**
- S&P 500 median 10-year revenue CAGR: 5–7%
- Top-quartile growers: 12–15%
- Top-decile growers: 18%+
- Companies sustaining 20%+ revenue CAGR for 10 years: fewer than 5% of public companies

If the current price requires top-5% historical performance, that is a stretched valuation — not necessarily wrong, but the margin of safety is slim.

**Disconfirmation prompt:** Under the bear scenario (revenue grows at base rate, margins compress 200bps), what is the implied return at the current price?

---

## Framework 2 — Owner Earnings Yield

Owner earnings = Net income + Depreciation/amortization − Maintenance capex − Working capital increases required by growth.

Owner earnings yield = Owner earnings / Market cap

**Why owner earnings instead of earnings per share:**
- EPS can be inflated by excessive D&A add-backs, stock comp exclusions, and one-time items.
- Owner earnings better approximate the cash a long-term owner actually captures.

**Benchmarks:**
- 10-year US Treasury yield: current risk-free rate (look this up; do not use a stale figure).
- S&P 500 earnings yield: approximately 1 / (market P/E).
- Adequate premium over risk-free for equities: historically ~3–5 percentage points, reflecting equity risk and illiquidity.

**Quick test:** If owner earnings yield < risk-free rate, you are paying a large premium for future growth. That premium is justified only if the durability score is high and the reverse-DCF assumptions are plausible.

---

## Framework 3 — Three-Scenario Range

Build three scenarios and estimate a range of intrinsic value, not a point estimate.

| Scenario | Revenue CAGR (10yr) | Terminal Margin | Implied Value Range |
|---|---|---|---|
| Bear | Flat to 2% | Compresses 200–300bps | $ |
| Base | Historical company average | Stable | $ |
| Bull | Top-quartile for sector | Expands 100–200bps | $ |

**Assign rough probabilities.** The expected value is the probability-weighted average of the three scenarios, not the base case alone.

Questions:
- What is the current market price relative to each scenario's value?
- If the bear case value is 40% below the current price, can you tolerate that drawdown? (See risk-and-sizing.md.)
- Is the bull case value more than 3x the current price? If not, the upside may not compensate for the concentration risk.

---

## Framework 4 — Margin of Safety

Margin of safety = (Intrinsic value estimate − Current price) / Intrinsic value estimate

The margin of safety concept (Graham, Klarman) acknowledges that valuation models are imprecise — the discount compensates for model error, forecasting error, and adverse surprises.

**General thresholds (illustrative, not prescriptive):**
- High confidence, durable business, wide moat: 20–30% discount may be sufficient.
- Moderate confidence, some cyclicality: 30–50% discount appropriate.
- Low confidence, high disruption risk, turnaround story: 50%+ discount; or avoid.

**Common mistake:** Anchoring the intrinsic value estimate to the current price and working backward to justify it. Your estimate should be derived from first principles (Framework 1–3) before you look at the current price.

---

## What Valuation Sanity Does NOT Do

- It does not produce a specific buy or sell price.
- It does not tell you when to buy — timing markets over 10 years is largely noise.
- It does not account for your personal tax situation, liquidity needs, or existing portfolio.
- It cannot predict macro events, interest rate changes, or regulatory actions.

A business that is fundamentally durable (high durability score) bought at a reasonable margin of safety has the structural elements for a good long-term outcome — but outcomes are probabilistic, not guaranteed.

---

*Educational framework only. Not financial advice.*
