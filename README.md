# decade-investing-skill

A Claude skill packaging a rigorous, process-driven framework for long-horizon (10-year) investment research and analysis.

**This is an educational process tooling package. It is NOT financial advice, NOT personalized recommendations, and NOT a guarantee of any investment outcome. Markets carry substantial risk, including the possible loss of your entire principal. Always consult a qualified, licensed financial advisor before making investment decisions.**

---

## What It Is

`decade-investing-skill` gives Claude a structured research workflow for evaluating whether a theme, company, or asset class has genuine 10-year durability. It covers six interconnected steps — each backed by a reference file — plus a worked fictional example and reusable scoring template:

- **Megatrend validation** — distinguishing durable secular trends from cyclical fads across six categories (demographics, energy transition, compute/AI, biotech, geopolitical restructuring, financial/macro) using base rates, Wright's Law cost curves, clinical trial data, and crowding tests.
- **Durability scoring** — structured 0–5 rubric across six dimensions: competitive moat (with ROIC and NRR benchmarks), TAM and runway (penetration rate, saturation timeline), secular tailwind alignment, balance sheet resilience (stress-tested at revenue −30%), management and capital allocation (M&A track record, vesting alignment), and disruption risk (with industry-specific disruption clocks).
- **Valuation sanity** — reverse-DCF that works backward from price to implied assumptions, owner earnings yield (SBC-adjusted) vs. live risk-free rate, three-scenario probability-weighted expected value, and margin of safety thresholds calibrated to conviction level.
- **Risk and sizing** — position sizing table calibrated to durability score and valuation margin, drawdown reference by asset class, correlation traps, time-horizon matching, and a full behavioral pitfall inventory with specific mitigations.
- **Decision journaling** — a ten-section template to log thesis, scores, falsifiers, exit conditions, and review schedule before entry — and post-mortem notes at each review date.
- **Worked fictional example** — complete end-to-end application of all five steps to the fictional NovaCure Industrial Systems (NCIS), showing real scoring decisions, valuation math, and a "do not invest at current price" conclusion driven by negative margin of safety.
- **Scoring template CSV** — structured spreadsheet covering all scoring categories, valuation fields, conviction/sizing derivation, exit conditions, and post-mortem tracking across multiple theses over time.
- **Visual cheatsheet** — a polished, standalone `cheatsheet.html` with dark theme, inline CSS (no CDN), and print-friendly layout — summarizing the full framework at a glance.

The framework emphasizes **process over prediction**, **base rates before bull cases**, **disconfirming evidence**, **second-order effects**, and **epistemic humility about long-horizon forecasting**.

---

## File Structure

```
decade-investing-skill/
├── SKILL.md                              # Main skill — workflow, principles, quick-start checklist
├── README.md                             # This file
├── LICENSE                               # MIT License
├── cheatsheet.html                       # Visual one-pager — full framework at a glance
├── .gitignore
└── references/
    ├── megatrends-checklist.md           # Secular trend vs. fad — 6 categories, base rates, fad tests
    ├── durability-rubric.md              # 10-year durability rubric — 6 dimensions, ROIC/NRR benchmarks
    ├── valuation-sanity.md               # Valuation sanity — reverse DCF, OE yield, 3-scenario, MoS
    ├── risk-and-sizing.md                # Sizing, drawdown, correlation, behavioral pitfalls, exit conditions
    ├── decision-journal-template.md      # 10-section thesis log — pre-entry and post-mortem
    ├── worked-example.md                 # End-to-end fictional example (NovaCure NCIS) — illustrative only
    └── scoring-template.csv              # Reusable structured scoring sheet for all analyses
```

---

## How to Install as a Claude Code Skill

### Option 1 — Project-level skill (recommended)

1. Clone this repo into your project's `.claude/skills/` directory (create it if it does not exist):

```bash
git clone https://github.com/Alchemist-X/decade-investing-skill.git .claude/skills/decade-investing-skill
```

2. Claude Code will automatically discover skills in `.claude/skills/`. The `SKILL.md` frontmatter registers the skill name and trigger description.

### Option 2 — User-level skill (available across all projects)

1. Clone into your user Claude skills directory:

```bash
git clone https://github.com/Alchemist-X/decade-investing-skill.git ~/.claude/skills/decade-investing-skill
```

### Option 3 — Manual reference

Copy `SKILL.md`, the `references/` directory, and `cheatsheet.html` anywhere convenient and reference them directly in your Claude conversations. Open `cheatsheet.html` in any browser for a quick-reference one-pager.

---

## How to Use

Once installed, invoke the skill in Claude by describing a long-horizon investment research task. Example prompts that trigger the skill:

- "Help me research whether the AI infrastructure theme has 10-year durability."
- "Run a decade-investing analysis on [company or sector]."
- "I want to build a 10-year investment thesis — walk me through the framework."
- "Run a megatrend check and durability score for [sector]."
- "Show me a worked example of how to use this framework."
- "Help me fill out a decision journal entry for [investment]."
- "What does this price imply about growth assumptions — run a reverse DCF sanity check."

Claude will walk you through the end-to-end workflow defined in `SKILL.md`, using the `references/` files at each step. For orientation, open `cheatsheet.html` first — it shows the complete framework at a glance.

---

## Key Design Choices

**Why no price targets?** Valuation models are imprecise. Producing a specific price target creates false precision and invites anchoring. The framework instead asks "what does this price require me to believe?" (reverse DCF) and "how wrong can I be and still achieve an adequate outcome?" (margin of safety) — questions that are both more honest and more actionable.

**Why a decision journal?** The primary cause of long-horizon underperformance is behavioral: investors confuse "price went down" with "thesis is broken," and sell at troughs. The journal creates a pre-commitment to specific falsifiers — observable conditions, not price levels — that separate thesis deterioration from price noise.

**Why base rates throughout?** Narrative is seductive; base rates are grounding. Every framework prompt asks "what percentage of comparable situations historically ended this way?" before building a forward case. This prevents the common error of treating an unusual company as if the laws of business physics do not apply.

---

## Disclaimer

**IMPORTANT — READ BEFORE USE:**

This skill and all associated files are provided for **educational and informational purposes only**. Nothing in this repository constitutes:

- Personalized financial advice.
- A recommendation to buy, sell, or hold any security.
- A solicitation or offer to invest in any fund or investment vehicle.
- A guarantee or prediction of any investment outcome.

Investing in securities involves **substantial risk, including the possible loss of your entire principal**. Past performance of any investment does not predict future results. The frameworks provided are general educational tools — they do not account for your personal financial situation, tax circumstances, risk tolerance, liquidity needs, or investment objectives.

The worked example (`references/worked-example.md`) uses a completely fictional company (NovaCure Industrial Systems / NCIS) with invented figures. It is not research on any real company and does not represent a recommendation regarding any real security.

**Before making any investment decision, consult a qualified, licensed financial advisor who understands your complete personal and financial situation.**

The authors and contributors of this repository accept no liability for investment decisions made using this framework.

---

## License

MIT License — see `LICENSE` for details.

Copyright (c) 2026 Alchemist-X
