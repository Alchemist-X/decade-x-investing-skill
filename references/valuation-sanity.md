# Valuation Sanity Checks

> **Educational only. Not financial advice. Investing involves risk of loss. These frameworks do not produce price targets or buy/sell recommendations.**

The goal here is not precision — it is to identify whether a price implies assumptions that are plausible, stretched, or absurd given base rates. A valuation sanity check asks: "What does this price require me to believe, and how often does that actually happen in the historical record?"

**Do NOT anchor to the current price before doing this analysis.** Derive your estimate from first principles (Frameworks 1–3), then compare to the market price. Anchoring to price and working backward to justify it is one of the most common and expensive valuation errors.

---

## Framework 1 — Reverse DCF Intuition

Instead of projecting cash flows forward to justify a current price, work backward from the current price to discover the implied assumptions. This reveals what you are implicitly betting on when you pay the current market price.

**Steps:**

1. Find (or estimate) current owner earnings or free cash flow (FCF).
2. Assume a long-run discount rate: use 8–10% as a base for most equity analysis (reflects long-run equity risk premium over risk-free). Adjust upward for small-cap, pre-profitability, or high-leverage situations.
3. Assume a terminal growth rate (use nominal GDP growth — roughly 2–3% — as a ceiling for most mature businesses; technology companies with genuine platform advantages might justify 4–5% for the initial phase before decelerating).
4. Solve backward: what revenue growth rate and terminal margin are required to justify the current price at your discount rate?

**Key question:** Is the implied growth rate in the top decile of historical outcomes for this industry? What percentage of comparable companies actually achieved it over 10 years?

**Reference base rates (rough — use as calibration, not as targets):**
- S&P 500 median 10-year revenue CAGR (all companies, all decades): 5–7%
- Top-quartile revenue growers: 12–15% CAGR
- Top-decile revenue growers: 18–22% CAGR
- Companies sustaining 20%+ revenue CAGR for a full 10 years: fewer than 5% of public companies
- Companies sustaining 30%+ revenue CAGR for 10 years: fewer than 1%
- Margin expansion: most mature businesses sustain operating margins within ±300bps of their 5-year average; structural margin expansion of 500–1000bps over 10 years is achievable but uncommon

**Interpretation:**
- If the current price requires growth in the top 10% of historical outcomes: stretched but not impossible — be explicit about your conviction that this company is exceptional.
- If it requires top 5%: very stretched — the market is pricing near-perfection. This is not necessarily wrong, but your margin of safety is thin.
- If it requires something that has happened fewer than 1% of the time: implicit hubris. This is not a reason to avoid the investment, but it should be named clearly.

**Discount rate sensitivity table (illustrative):**

| Discount Rate | Effect on Implied Value |
|---|---|
| 8% (base, low risk) | Higher implied value — favors quality/stability |
| 10% (moderate risk) | Mid-range |
| 12% (higher risk, small cap) | Lower implied value — requires faster growth to justify price |
| 15%+ (pre-profitability, speculative) | Very conservative — forces high growth hurdle |

**Disconfirmation prompt:** Under the bear scenario (revenue grows at sector base rate, margins compress 200–300bps from current levels), what is the implied return at the current price? If the bear scenario produces negative or near-zero returns, you have very little margin of safety.

---

## Framework 2 — Owner Earnings Yield

Owner earnings = Net income + Depreciation/amortization − Maintenance capex − Working capital increases required by growth

Owner earnings yield = Owner earnings / Market cap

**Why owner earnings instead of reported earnings per share:**
- EPS can be inflated by excessive D&A add-backs, stock comp exclusions (non-GAAP adjustments), and one-time items.
- Reported net income often excludes significant stock-based compensation that is real dilution to shareholders.
- Owner earnings better approximate the cash a long-term owner actually captures — the residual after the business maintains its competitive position.

**A practical shortcut when detailed data is unavailable:**
Use FCF yield (FCF / market cap) as an approximation. FCF = Operating cash flow − Capex. Note that this understates true earnings for capital-light businesses (SaaS, asset-light platforms) and overstates it for capital-intensive businesses (manufacturing, energy) where maintenance capex is higher than D&A.

**Benchmarks (recalculate with current figures — do not use stale data):**
- 10-year US Treasury yield: current risk-free rate (look this up; use the current yield, not a historical average).
- S&P 500 earnings yield: approximately 1 / (market P/E). As of mid-2020s, roughly 3.5–4.5%.
- Adequate equity premium over risk-free: historically ~3–5 percentage points to compensate for equity risk, illiquidity premium, and business risk.

**Quick test:** If owner earnings yield < current risk-free rate, you are paying a large premium for future growth expectations. That premium is justified only if: (a) the durability score is high (moat is real), (b) growth is genuinely likely to be above base rate, and (c) the reverse-DCF implied assumptions are plausible given historical evidence.

**Stock-based compensation (SBC) adjustment:**
Many technology companies report "adjusted" earnings that add back SBC. This is misleading — SBC is real dilution that reduces future per-share value. Always add SBC back to costs when computing owner earnings yield. A company with a 4% FCF yield that adds back 3% in SBC actually has a 1% true owner earnings yield.

---

## Framework 3 — Three-Scenario Range

Build three scenarios and estimate a range of intrinsic value. Never use a point estimate — valuation models are imprecise and overconfidence in precision is a common error.

**Scenario construction rules:**
- The bear case should be genuinely bad — not just "growth slows a bit." Use the worst credible outcome, not the mildly disappointing one.
- The bull case should be genuinely good — not just "everything goes according to plan." What happens if the business executes better than expected AND the tailwind is stronger than expected?
- The base case should reflect the median plausible outcome — usually close to historical company performance continued, with modest trend extrapolation.

| Scenario | Revenue CAGR (10yr) | Terminal Margin vs. Today | Implied Value Range | Probability |
|---|---|---|---|---|
| Bear | Flat to 2% | Compresses 200–400bps | $ | __% |
| Base | Historical company average | Stable ±100bps | $ | __% |
| Bull | Top-quartile for sector | Expands 200–400bps | $ | __% |
| **Expected value** | | | **$** | **100%** |

**Assign rough probabilities explicitly.** The expected value is the probability-weighted average — not the base case alone. A common error is treating the base case as the fair value and ignoring the bear case's drag on expected returns.

**Coherence check — does the probability distribution make sense?**
- If you are assigning >50% probability to the bull case, examine whether you have narrative attachment.
- If your bear case probability is <10%, examine whether you are underweighting tail risk.
- For any given stock in a given sector, look at the distribution of actual outcomes for peers over the last 10 years. This is your empirical prior.

**Questions:**
- What is the current market price relative to each scenario's value?
- If the bear case value is 40%+ below the current price, can you tolerate that drawdown — and maintain your thesis — without selling? (See risk-and-sizing.md for honest self-assessment.)
- Is the bull case value more than 2–3x the current price? If not, the upside may not compensate for the binary risk of the bear case.

---

## Framework 4 — Margin of Safety

Margin of safety = (Intrinsic value estimate − Current price) / Intrinsic value estimate

The margin of safety concept (Graham, Klarman) acknowledges that valuation models are imprecise — the discount compensates for model error, forecasting error, and adverse surprises. The appropriate discount scales with uncertainty.

**General thresholds (illustrative, not prescriptive — adjust for your own uncertainty):**

| Confidence Level | Business Type | Appropriate Discount |
|---|---|---|
| High confidence | Wide moat, predictable cash flows, low disruption risk | 20–30% discount to base case intrinsic value |
| Moderate confidence | Some cyclicality, moderate disruption risk | 30–50% discount |
| Low confidence | Turnaround, pre-profitability, high disruption risk | 50%+ discount; or avoid |
| Very low confidence | Binary outcome (regulatory, clinical trial, macro-dependent) | Either avoid or accept it as a lottery ticket sized at 1–2% of portfolio |

**Margin of safety anti-patterns:**
1. **Anchoring intrinsic value to current price:** If your intrinsic value estimate is always within 10% of the current price regardless of the company, you are anchoring to market price rather than deriving it from first principles.
2. **Using optimistic scenario as intrinsic value:** Intrinsic value should be the base or probability-weighted case — not the bull case. Using the bull case as "fair value" eliminates the margin of safety conceptually.
3. **Ignoring the time cost of being early:** A stock trading at 30% below fair value but taking 5 years to re-rate still produces poor returns if you forgo a 10% per year alternative. Time is a cost.

---

## Framework 5 — Comparable Returns Analysis

Before committing to a valuation thesis, compare the expected return to alternatives.

**The opportunity cost check:**
- What is the risk-adjusted expected return from this investment at the current price?
- What would a passive broad-market index return over 10 years at current valuations? (Use a Shiller CAPE-based or earnings-yield-based estimate — these have modest but real predictive power at decade horizons.)
- What is the risk-free return (10-year Treasury yield) for the next decade?

**The hurdle rate:**
A reasonable long-horizon equity hurdle rate for an individual company (accounting for idiosyncratic risk) is typically 2–4 percentage points above the expected broad market return. If your analysis does not suggest the investment clears this hurdle, the position does not justify the concentration risk.

---

## What Valuation Sanity Does NOT Do

- It does not produce a specific buy or sell price.
- It does not tell you when to buy — timing markets over 10 years is largely noise, and trying adds mostly behavioral risk.
- It does not account for your personal tax situation, liquidity needs, or existing portfolio context.
- It cannot predict macro events, interest rate changes, geopolitical shocks, or regulatory actions that can move prices far from intrinsic value for extended periods.

A business that is fundamentally durable (high durability score), anchored to a real megatrend (strong checklist score), and bought at a reasonable margin of safety has the structural elements for a good long-term outcome — but outcomes are probabilistic, not guaranteed. Markets can stay irrational for years. Have the financial and emotional staying power to wait.

---

*Educational framework only. Not financial advice.*
