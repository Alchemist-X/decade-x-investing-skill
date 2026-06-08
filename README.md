# decade-x-investing-skill

A Claude skill that distills the **research methodology of DecadeX (未来十年投资学堂, [decadex.org](https://decadex.org))** so an analyst — or Claude — can produce DecadeX-style long-horizon investment research across Crypto, AI, Consumer, and Funds/Capital.

**Educational only.** This skill is sourced from DecadeX's own public research and packages *how they reason* (their named frameworks, house worldview, and report structure). It is **NOT financial advice, NOT a buy/sell recommendation, NOT affiliated with or endorsed by DecadeX**, and reproducing a house's reasoning style does not make its conclusions correct. All investing carries substantial risk including loss of principal. Consult a licensed advisor.

---

## What It Is

`decade-x-investing` gives Claude the DecadeX research process: open with a **理解更新 (understanding update / versioned self-critique)**, re-derive the category from **first principles**, deploy DecadeX's **named frameworks applied with numbers**, build a benchmark-anchored **head-to-head comparison**, run the **尽调十问 (β/α/Timing)** scorecard, value with a **three-scenario probability-weighted PS/PE model**, and close with **conditional, falsifiable conclusions**.

It encodes the cross-cutting frameworks that recur across DecadeX's reports — 不可能三角 (and its re-ordering), 北极星指标, 价值创造 vs 价值捕获 (Ethereum≠ETH), 流量×流动性, 资产渗透率, 技术革命与金融资本 (Perez cycle), 收单/执行/清结算 settlement-stack, 能力圈映射, 三情景估值 — plus sector-specific frameworks for Crypto, AI, Funds/Capital, and Consumer.

It also ships **free, no-key data tooling** so the analysis is numbers-anchored (DecadeX's "hard business anchors before jargon" discipline): fetchers for SEC EDGAR, CoinGecko, DefiLlama, and US Treasury/FRED, plus a pure (offline) calculator for reverse-DCF, three-scenario probability-weighted valuation, and owner-earnings (FCF) yield. See `tools/README.md`, `references/data-sources.md` (where to get data), and `references/data-analysis.md` (what to compute).

---

## Sourcing & Provenance

The skill is distilled from **DecadeX's public research corpus** (see [decadex.org/research](https://decadex.org/research)). The corpus itself is **gitignored and not republished**; only the *methodology* (frameworks, conclusions, analytical moves) is encoded in the reference files.

- `corpus/fetch_corpus.py` — rebuilds the corpus locally (`corpus/corpus.json` + `corpus/text/<slug>.txt`) from DecadeX's public endpoint, for the eval pipeline. Requires `uv` (for `pymupdf`).
- `eval/split.json` — the train/test split of DecadeX reports. The **train** set (24 reports) was distilled into the reference files; the **test** set (NVIDIA, Microsoft, Benchmark, sogo-shosha, eth-layer2, Coinbase, Marathon) is held out to evaluate whether applying this skill reproduces DecadeX-style reasoning on unseen reports.

---

## File Structure

```
decade-x-investing-skill/
├── SKILL.md                          # Main skill — worldview, workflow, cross-cutting frameworks, file guide
├── README.md                         # This file
├── LICENSE                           # MIT License
├── cheatsheet.html                   # Visual one-pager — DecadeX frameworks at a glance
├── .gitignore                        # (gitignores corpus/)
├── references/
│   ├── methodology.md                # End-to-end DecadeX research + writing process (the house arc, analytical moves)
│   ├── data-sources.md               # 数据获取 — per-sector catalog of WHERE/HOW to get data (free vs key) + matching tools/ script
│   ├── data-analysis.md              # 数据分析 — quantitative playbook: metrics per sector (formula+signal) + methods (penetration, unit economics, take-rate, reverse-DCF, 3-scenario, SOTP, sensitivity)
│   ├── frameworks-crypto.md          # Crypto frameworks: trilemma re-ordering, 协议层vs应用层, REV/GDP 税权, settlement-stack, exchange 三分类, stablecoin trilemma, PerpDex, asset-lifecycle
│   ├── frameworks-ai.md              # AI frameworks: 大模型=逻辑输出机器, Pre×Post×TTS, Scaling Law, ad-revenue decomposition, Core/Gen AI, AI+ vs +AI, Y=M·X compute lens
│   ├── frameworks-investing.md       # Funds/capital/macro: 技术革命与金融资本, 能力圈映射, 幂数定律/Vintage, LP三诉求, 渗透率TAM, fund北极星
│   ├── frameworks-consumer.md        # Consumer: 硬件→SaaS迁移, 两阶段时点, 平台vs品牌/船票, 直播电商=沉浸式广告, GMV双路径, 组织架构→渗透率
│   ├── report-index.md               # House knowledge base — one line per DecadeX report
│   └── writing-template.md           # The DecadeX report skeleton to reproduce
├── tools/                            # Free, no-key (stdlib-only) data + analysis scripts — see tools/README.md
│   ├── README.md                     # CLI docs for all four tools (free/no-key; optional env keys noted)
│   ├── fetch_edgar.py                # SEC EDGAR financials (revenue/net income/CFO/CapEx/shares) — no key
│   ├── fetch_crypto.py               # CoinGecko price/mktcap/volume + DefiLlama chain/protocol TVL — no key
│   ├── fetch_macro.py                # US Treasury avg rates (no key) + FRED series (free key)
│   └── analyze.py                    # Pure (offline) reverse-DCF / 3-scenario weighting / owner-earnings yield
├── corpus/
│   ├── fetch_corpus.py               # Rebuild the DecadeX corpus locally (gitignored output)
│   ├── corpus.json                   # Corpus metadata
│   └── text/                         # Extracted report text (gitignored)
└── eval/
    └── split.json                    # Train/test split of DecadeX reports
```

---

## How to Install as a Claude Code Skill

### Project-level (recommended)

```bash
git clone <this-repo> .claude/skills/decade-x-investing
```

Claude Code auto-discovers skills in `.claude/skills/`. The `SKILL.md` frontmatter registers the name and trigger description.

### User-level (all projects)

```bash
git clone <this-repo> ~/.claude/skills/decade-x-investing
```

### Manual reference

Copy `SKILL.md`, `references/`, and `cheatsheet.html` anywhere and reference them directly. Open `cheatsheet.html` for the one-pager.

---

## How to Use

Invoke by asking for DecadeX-style / 未来十年-style long-horizon research in Crypto / AI / Consumer / Funds. Example prompts that trigger the skill:

- "Write a DecadeX-style deep-dive on [token/company/sector]."
- "Apply DecadeX's 不可能三角 / REV/GDP 税权 / 流量×流动性 framework to [X]."
- "Value [token] the DecadeX way — three-scenario PS/PE with a regulatory discount."
- "Run the 尽调十问 (β/α/Timing) on [company]."
- "Give me the 理解更新 vs DecadeX's prior view on [topic]."
- "Reproduce a DecadeX report on [X] in their 理解更新→核心结论→框架展开 structure."

Claude follows the workflow in `SKILL.md`, pulling the matching `references/frameworks-*.md`, grounding against `references/report-index.md`, and drafting with `references/writing-template.md`. For the **data steps** it consults `references/data-sources.md` (where to get the numbers) and `references/data-analysis.md` (what to compute), running the bundled `tools/` fetchers and `tools/analyze.py` — all free and keyless.

You can also run the tools directly:

```bash
python3 tools/fetch_edgar.py NVDA --metric RevenueFromContractWithCustomerExcludingAssessedTax
python3 tools/fetch_crypto.py tvl ethereum
python3 tools/fetch_macro.py treasury
python3 tools/analyze.py reverse-dcf --mktcap 3e12 --fcf 9e10 --discount 0.10 --tgrowth 0.03
```

---

## The Eval Pipeline

The `corpus/` + `eval/` setup exists so the skill can be **measured against DecadeX's own reports**:

1. `python3 corpus/fetch_corpus.py` rebuilds the local corpus from DecadeX's public research.
2. `eval/split.json` defines the **train** reports (distilled into the references) and the held-out **test** reports.
3. To evaluate: prompt Claude (with this skill) to produce research on a *test* slug, then compare its frameworks, analytical moves, and conclusions against the held-out ground-truth report — checking whether the skill reproduces DecadeX-style reasoning on unseen material.

---

## Key Design Choices

- **Reproduce the process, not the predictions.** The skill encodes DecadeX's *reasoning style* (reframe-first, first-principles, frameworks-with-numbers, scenario valuation), not a set of price calls. Conclusions stay conditional and falsifiable.
- **Frameworks are named and concrete.** Each reference file states a framework, then *applies it with numbers* (ratios, correlations, share-of-benchmark) so following it reproduces DecadeX's reasoning rather than a vague gesture at it.
- **Train/test discipline.** Distilling only from the train split and holding out a test split lets the skill be honestly evaluated for whether it generalizes.

---

## Disclaimer

This skill and all associated files are for **educational and informational purposes only**. Nothing here is personalized financial advice, a recommendation to buy/sell/hold any security or token, a solicitation, or a guarantee of any outcome. It is a distillation of DecadeX's *public research methodology* and is not affiliated with, authorized by, or endorsed by DecadeX. Investing involves substantial risk including the possible loss of your entire principal; past performance does not predict future results. **Consult a qualified, licensed financial advisor before making any investment decision.** The authors accept no liability for decisions made using this framework.

---

## License

MIT License — see `LICENSE`.