# Durability Rubric

> **Educational only. Not financial advice. Investing involves risk of loss.**

Score a specific asset, company, or investment vehicle on six dimensions for 10-year durability. Each dimension is scored 0–5. The rubric surfaces where the thesis is strong and where it is fragile — it does not produce a buy/sell signal.

**Time budget:** A careful pass through all six dimensions should take 60–90 minutes of research per company. If you finish faster, you probably skipped the disconfirmation work.

---

## Scoring Scale (applied to each dimension)

| Score | Meaning | What it looks like in practice |
|---|---|---|
| 0 | Severe threat | Moat is actively eroding; debt is unsustainable; disruption is already happening |
| 1 | Significant concern | Weak competitive position; elevated leverage; management track record is poor |
| 2 | Below average | Some concern, partial mitigant; thesis could work but requires multiple things to go right |
| 3 | Average | Reasonable but not differentiated; will likely survive and earn moderate returns |
| 4 | Above average | Clearly positive, well-documented advantage; hard for competitors to replicate near-term |
| 5 | Exceptional | Rare, durable, compound-interest-generating advantage; best-in-class evidence across 5+ years |

**Rule of thumb:** 5s are rare. If you are giving 5s freely, re-examine your standards. A 5 should be supported by specific, quantifiable evidence — not general impressions.

---

## Dimension 1 — Competitive Moat

A moat is a structural advantage that allows sustained above-average returns on invested capital over time. Moats compound — a business that earns 20% ROIC while reinvesting at 20% ROIC grows intrinsic value rapidly. A business that cannot sustain above-cost-of-capital returns will not compound regardless of growth rate.

**Moat types to assess:**

| Type | Characteristics | Questions |
|---|---|---|
| Switching costs | Customer pain of leaving exceeds pain of staying | How long is the average customer lifetime? What is the cost to migrate? |
| Network effects | Value increases with user count; winner-take-all potential | Is this direct (users to users) or indirect (users to developers)? How dense is the network today? |
| Cost advantage | Structural cost advantage from scale, location, or process | Is the cost advantage driven by scale (replicable at scale) or process (harder to replicate)? |
| Intangible assets | Patents, regulatory licenses, brand with pricing power | What is the average remaining patent life? Has brand pricing power been demonstrated through a downturn? |
| Efficient scale | Market too small to attract a second competitor | What would a second entrant need to invest to reach parity? Would that investment earn an adequate return? |

**Key quantitative checks:**
- What is the gross margin trend over 5–10 years? (Declining gross margins are a moat erosion signal.)
- What is the ROIC trend over 5–10 years? (ROIC sustained above 15% over a decade is a strong moat signal; ROIC declining toward WACC is a moat-narrowing signal.)
- Has the company maintained pricing power through at least one recession? (Companies with real moats typically defend margins during downturns better than peers.)
- What is the customer retention / net revenue retention rate? (NRR >120% is an exceptional switching-cost signal.)

**Base rates:**
- ~50% of companies with 20%+ ROIC in any given year sustain it for 5+ years.
- ~25% sustain it for 10+ years.
- Industries with most durable high-ROIC: software (network/switching), medical devices (switching), branded consumer (intangibles), payment networks (network effects).

**Disconfirmation prompt:** What would cause this moat to narrow within 5 years? Specifically: (a) regulatory change removing a license or breaking up a network, (b) open-source alternative reducing switching costs, (c) platform shift making the incumbent's distribution advantage irrelevant, (d) new entrant with a 10x better cost structure or user experience. Have any of these already started?

Score: `__/5`

---

## Dimension 2 — TAM and Runway

Total Addressable Market size matters, but TAM capture trajectory matters more. A business that has captured 40% of a $10B market has less runway than one that has captured 2% of a $100B market — even if both have the same current revenue.

**Prompts:**
- What is the current penetration rate of the relevant product or service in its total market? (Source this from the company's own filings AND from third-party industry data — they often differ.)
- Is the TAM itself growing (secular expansion), stable, or shrinking (secular contraction)?
- At current growth rates, how many years until the company approaches market saturation? (Simple math: if current penetration is 15% and growing at 3 percentage points per year, saturation is ~28 years away — likely not the binding constraint. If penetration is 60% and growing at 3pp/year, saturation is ~13 years away — model the deceleration.)
- Is the company's share of TAM growing, stable, or eroding?

**Watch for these TAM inflation traps:**
- **Top-down TAM inflation:** Analyst TAM estimates are frequently 3–10x the realistically addressable market. A company selling compliance software to US mid-market banks does not have a "$50B TAM" just because global financial services software spend is $50B. Build from the bottom up: number of addressable customers × average revenue per customer.
- **Runway compression from adjacent market entry:** Competition from adjacent markets (e.g., Salesforce entering marketing, Microsoft entering security) can compress TAM faster than growth can capture it.
- **TAM that requires product expansion:** If achieving the TAM requires selling products the company has not yet built, weight the TAM accordingly.

**Base rates:**
- Market saturation deceleration is the most common cause of growth-stock multiple compression. Companies growing at 30%+ CAGR almost universally decelerate once they exceed 10–15% market penetration in their core TAM.
- Historical median time from IPO to growth deceleration (below 20% revenue growth) for tech companies: 4–6 years post-IPO.

**Disconfirmation prompt:** What substitution effect (new technology, behavioral shift, regulatory constraint) compresses this TAM within 10 years? If the total market shrinks (e.g., streaming substituting for broadcast TV, but now streaming itself is pressured by gaming and social video), does the company have a credible pivot?

Score: `__/5`

---

## Dimension 3 — Secular Tailwind Alignment

This dimension checks whether the company's business model is aligned with, or exposed against, the confirmed megatrends from the checklist.

**Prompts:**
- Which megatrend category does this company benefit from directly? Indirectly?
- If the megatrend stalls (see disconfirmation prompts in megatrends-checklist), how much of the company's revenue is directly exposed?
- Are there secular headwinds this company faces that could offset tailwinds? (E.g., a clean-energy company with a coal legacy still in the P&L, a healthcare company facing drug pricing reform that compresses its core business even as a new platform grows.)
- Is the company a "picks and shovels" play (less direct exposure to which application wins, but less upside) or a "winner-take-most" play (more upside if the thesis is correct, more downside if wrong)?

**Rigorous heuristic:** Distinguish "exposed to megatrend" from "structurally benefits from megatrend." An airline exposed to more leisure travel demand benefits from demographics — but its structurally poor economics (low switching costs, high capex, commodity fuel cost) limit how much of that tailwind it can capture. A payments network exposed to the same digitization megatrend captures far more per dollar of economic activity due to its structural position.

Score: `__/5`

---

## Dimension 4 — Balance Sheet Resilience

A 10-year thesis requires the company to survive the intervening bear markets, credit crunches, and industry dislocations. The average 10-year period for a US investor has historically included 2–3 recessions and at least one severe market drawdown (>35%). A company that requires refinancing at precisely the wrong time, or that runs out of cash during a trough, cannot compound for a decade regardless of its business quality.

**Prompts:**
- What is the net debt / EBITDA ratio at current EBITDA? What does it look like under a stress scenario (revenue −30%, EBITDA margins compressed 300–500bps)?
- Does the company generate free cash flow? What is the FCF yield? Is FCF growing and converting >80% of net income?
- What is the debt maturity profile? Are there near-term maturities (within 3 years) that require refinancing — potentially at significantly higher rates?
- Does the company have committed liquidity (undrawn revolver, cash on hand) to survive a 2-year revenue downturn without equity dilution?
- For pre-profitability companies: what is the cash runway at current burn rate? What milestones must be hit to access the next capital raise?

**Stress test heuristic:**
Apply the "2009 scenario" — revenue declines 20–30%, credit markets freeze, equity issuance is unavailable for 18 months. Does the company survive? Does it survive without catastrophic dilution? Companies that passed this test in 2009–2010 or 2020 have demonstrated real balance sheet resilience.

**Base rates:**
- Of companies with net debt/EBITDA >5x at the start of a recession, approximately 15–25% face distress (restructuring, covenant breach, bankruptcy) within 3 years.
- FCF conversion rate (FCF/Net Income) of <60% persistently is a quality concern — often signals aggressive accounting or high maintenance capex masking lower real earnings.

Score: `__/5`

---

## Dimension 5 — Management and Capital Allocation

Over a 10-year horizon, capital allocation quality often matters more than current business quality. A mediocre business run by an exceptional capital allocator can compound well. An exceptional business run by a value-destroying capital allocator will disappoint.

**What to evaluate:**

*Track record of M&A:*
- Look at acquisitions made 5+ years ago. Did they achieve stated synergies? What was the purchase price vs. current value? Overpayment on acquisitions is one of the most reliably value-destructive behaviors.
- Red flag: management that consistently uses "adjusted EBITDA" metrics that exclude acquisition costs and amortization, making poor acquisitions appear accretive.

*Buyback discipline:*
- Does management buy back stock at rational prices, or is buyback activity highest when the stock is at peak valuations? (Check buyback timing vs. historical valuation levels.)
- Share count: is it shrinking (returns capital), stable, or growing (dilutive issuance, often for stock comp or acquisitions)?

*Insider alignment:*
- Does management own significant equity — not options that are already in-the-money, but shares purchased or earned over time that represent meaningful personal wealth tied to long-term outcomes?
- What is the median vesting period for executive equity? Short vesting (1–2 years) incentivizes short-termism; longer vesting (3–5+ years) incentivizes long-term thinking.

*Transparency and communication:*
- Has management been accurate in its forecasts historically? Track stated guidance vs. actual results over 5+ quarters.
- In downturns, did management communicate clearly and take responsibility — or did they blame external factors and change accounting metrics?

**Base rates:**
- Companies in the top quintile of capital allocation quality (measured by ROIC consistency, FCF conversion, and share count trajectory) have historically outperformed their sector peers by 2–4 percentage points per year — compounding dramatically over 10 years.
- M&A as a value driver: studies consistently show 60–70% of acquisitions fail to create value for acquirers; large premiums (>30% to market) are particularly dangerous.

**Disconfirmation prompt:** What capital allocation error (overpriced acquisition, excessive leverage taken on at cycle peak, share dilution to fund growth that doesn't materialize) has this management made in the past? Is there structural incentive misalignment that would cause this to recur?

Score: `__/5`

---

## Dimension 6 — Disruption Risk

This is the most frequently underweighted factor at a 10-year horizon. Industries that looked impregnable in 2010 (retail, media, traditional banking, oil and gas) faced existential disruption by 2020. The asymmetry of disruption risk is important: the upside of being undisrupted is "continued normal business," while the downside of being disrupted is "permanent revenue impairment or terminal decline."

**The disruption assessment:**

*Technology-driven disruption:*
- Is there a technology currently in the lab or early commercial stage that could make the company's core product significantly cheaper, better, or obsolete within 10 years?
- Classic pattern: 10x cost improvement in a substitute technology typically triggers rapid adoption within 5–8 years of cost crossover.

*Business model disruption:*
- Could an existing large company with a different cost structure (e.g., a software company entering a hardware market, a platform company entering a services market) attack the company's economics?
- Disintermediation risk: does the company sit between two parties (supplier and customer) who could connect directly at lower cost if a platform enabled it?

*Regulatory disruption:*
- Is the company's business model dependent on a regulatory framework that could be unwound? (E.g., pharmacy benefit managers in a drug pricing reform environment; social media companies under content liability reform; fintech companies if bank charter requirements change.)

**The startup/competitor scan:**
- Are there venture-backed companies with >$100M raised attacking the core market? What stage are they at? (Seed = early risk; Series C/D = near-commercial risk; late-stage = serious near-term risk.)
- What is the company's own R&D as a percentage of revenue, and is it directed at disruption-proofing or merely maintaining current products?

**Base rates:**
- Of companies in the Fortune 500 in 1955, only ~12% were still in the Fortune 500 in 2023. The average S&P 500 company lifespan has declined from ~67 years (1920s) to ~15 years (2020s).
- Industries with fastest disruption cycles: media (~5–8 years), retail (~8–12 years), financial services (~10–15 years), industrials (~15–25 years), healthcare (~20–30 years). Know which clock your company is on.

**Disconfirmation prompt:** If you were running a startup with $500M to disrupt this company, what would you build, and what is your go-to-market? Does that specific attack surface already have funded players — and if so, why haven't they succeeded yet? What specifically protects the company from that attack?

Score: `__/5` (5 = very low disruption risk with documented evidence; 0 = severe and near-term disruption already occurring)

---

## Summary Scorecard

| Dimension | Score (/5) | Key Strength | Key Fragility |
|---|---|---|---|
| Competitive Moat | | | |
| TAM and Runway | | | |
| Secular Tailwind | | | |
| Balance Sheet | | | |
| Management/Capital Allocation | | | |
| Disruption Risk | | | |
| **Total** | **/30** | | |

**Interpretation (rough guide only — not a buy signal):**
- 24–30: High conviction on durability — proceed to valuation sanity check.
- 16–23: Moderate — thesis has meaningful fragilities. Document them explicitly. Size position conservatively. Consider whether one or two fragile dimensions could be thesis-ending.
- 8–15: Low durability — either avoid, or build a focused bear case as a potential hedge. Require exceptional valuation discount before proceeding.
- Below 8: Severe structural concerns — thesis as stated is fragile. If investing here, do so at very small size and with very high return requirements.

**Minimum bar rule:** Any single dimension scoring 0 or 1 should be treated as a thesis-threatening concern, regardless of the total score. A business with an excellent moat and terrible balance sheet can be destroyed by the next credit cycle. A business with strong fundamentals but severe disruption risk underway has a time limit on its durability.

**Conviction calibration:** Use the scorecard total to calibrate position size (see risk-and-sizing.md). High scores justify larger positions; moderate scores should constrain size even if the thesis is attractive.

---

*Educational framework only. Not financial advice.*
