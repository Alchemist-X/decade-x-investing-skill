# decade-investing-skill

A Claude skill packaging a structured, process-driven framework for long-horizon (10-year) investment research and analysis.

**This is an educational process tooling package. It is NOT financial advice, NOT personalized recommendations, and NOT a guarantee of any investment outcome. Markets carry substantial risk, including the possible loss of your entire principal. Always consult a qualified, licensed financial advisor before making investment decisions.**

---

## What It Is

`decade-investing-skill` gives Claude a rigorous research workflow for evaluating whether a theme, company, or asset class has genuine 10-year durability. It covers:

- **Megatrend validation** — distinguishing durable secular trends from cyclical fads.
- **Durability scoring** — structured rubric across moat, TAM, tailwinds, balance sheet, management, and disruption risk.
- **Valuation sanity** — reverse-DCF intuition, owner-earnings yield, scenario ranges, and margin of safety — without false-precision price targets.
- **Risk and sizing** — position sizing, diversification, drawdown tolerance, rebalancing, and a behavioral pitfall inventory.
- **Decision journaling** — a template to log your thesis, assumptions, falsifiers, and review dates before and after each investment decision.

The framework emphasizes **process over prediction**, **base rates**, **disconfirming evidence**, **second-order effects**, and **epistemic humility about long-horizon forecasting**.

---

## File Structure

```
decade-investing-skill/
├── SKILL.md                              # Main skill — workflow and principles
├── README.md                             # This file
├── LICENSE                               # MIT License
├── .gitignore
└── references/
    ├── megatrends-checklist.md           # Secular trend vs fad identification
    ├── durability-rubric.md              # 10-year durability scoring rubric
    ├── valuation-sanity.md               # Valuation sanity check frameworks
    ├── risk-and-sizing.md                # Position sizing and behavioral risk
    └── decision-journal-template.md      # Thesis logging and review template
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

Copy `SKILL.md` and the `references/` directory anywhere convenient and reference them directly in your Claude conversations.

---

## How to Use

Once installed, invoke the skill in Claude by describing a long-horizon investment research task. Example prompts that trigger the skill:

- "Help me research whether the AI infrastructure theme has 10-year durability."
- "Run a decade-investing analysis on [company name]."
- "I want to do a long-horizon investment thesis on biotech platforms — walk me through the framework."
- "Run a megatrend check and durability score for [sector]."

Claude will walk you through the end-to-end workflow defined in `SKILL.md`, using the `references/` files at each step.

---

## Disclaimer

**IMPORTANT — READ BEFORE USE:**

This skill and all associated files are provided for **educational and informational purposes only**. Nothing in this repository constitutes:

- Personalized financial advice.
- A recommendation to buy, sell, or hold any security.
- A solicitation or offer to invest in any fund or investment vehicle.
- A guarantee or prediction of any investment outcome.

Investing in securities involves **substantial risk, including the possible loss of your entire principal**. Past performance of any investment does not predict future results. The frameworks provided are general educational tools — they do not account for your personal financial situation, tax circumstances, risk tolerance, liquidity needs, or investment objectives.

**Before making any investment decision, consult a qualified, licensed financial advisor who understands your complete personal and financial situation.**

The authors and contributors of this repository accept no liability for investment decisions made using this framework.

---

## License

MIT License — see `LICENSE` for details.

Copyright (c) 2026 Alchemist-X
