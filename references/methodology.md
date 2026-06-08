# DecadeX Research Methodology

*How DecadeX (未来十年投资学堂) actually produces a report — the repeatable process distilled from 24+ public reports. Educational; reproduce the process, not the conclusions.*

---

## 0. The house arc (every report follows this)

```
理解更新 (what changed / versioned self-critique)
  → 第一性原理 + 重新定义品类 (re-derive what it IS, pick the lens, name the 北极星指标)
    → 框架展开 (deploy named frameworks, applied WITH numbers)
      → 竞争格局 / 头对头对标 (comparison table anchored to a benchmark)
        → 尽调十问 (β / α / Timing scorecard)
          → 三情景估值 + 风险 (Bear/Base/Bull → banded target; black-swan risks)
            → 核心结论 (numbered, conditional, falsifiable)
```

---

## 0a. Period-lock + thesis-polarity (do this BEFORE anything else — the #1 failure mode)

A DecadeX report is written *at a date, from the information available then*. The single biggest way to miss the human's conclusion is to **impose a later, contrarian, or inverted thesis** the report never reached. Guardrails:

- **Date-lock the analysis.** Pin the report's period and reason only from data/events plausibly known then. Do **NOT** assume forward regulatory events, later deals, or future metrics unless the corpus dates them. (A 2024 Coinbase report is *bullish on the compliance moat*; do not retro-fit a 2026 "moat is melting / ETF won" inversion. A 2024 ETH-L2 report's thesis is *L1×L2 complementary*; do not impose a later "L1 vs L2 competitive, tax collapsed to 8%" frame. A 2024 miner report does *not* mention an AI/HPC pivot.)
- **Recover the human's ACTUAL conclusion polarity — do not invent a contrarian one.** DecadeX is often *bullish-with-a-number*, not reflexively contrarian-bearish. Manufacturing a contrarian inversion ("护城河融化", "周期股", "L2 collapsed ETH") when the source is bullish is the most common large miss. The "non-obvious insight" you must surface is the *human's* non-obvious insight, not your own. If you reach the OPPOSITE valence from the likely house view, stop and re-derive.
- **Recover the human's ACTUAL North Star — do not substitute a self-invented metric.** Use the metric the report would have chosen (e.g. Coinbase = 合规护城河/MTU; Microsoft = "能否再造操作系统/重构流量入口"; NVIDIA = a 10x-model-or-killer-app trigger; miners = leverage-ratio vs BTC). Inventing a fresh 2026-vintage metric (e.g. "compute tax rate", "enterprise Token share", "compute-tax sovereignty %") drifts away from the human's conclusion engine.
- **Verify a subject's stated strategy from primary characterization before asserting drift/inversion.** Do not claim a fund "is forced down to seed" if it explicitly does *not* do seed; do not claim a stock is "cyclical" if the house thesis is that it temporarily escapes the cycle. Penalize speculation that contradicts documented strategy.
- **Guard against framework transfer-overreach.** Do NOT import a domain's signature mental models onto an unrelated report (no crypto 流量×流动性 / 清结算分层 / L1-L2 铸币税 / Perez-as-primary on an industrial trading-house piece; no mNAV/AI-HPC on a 2024 miner piece). Import a framework only if the source domain actually uses it.

## 0b. Native-framework discovery (infer the report's OWN scaffold before reaching for generic toolkits)

Before applying the cross-cutting toolkit, **infer the report's own native framework from the subject's history/structure** — the human usually builds a bespoke spine, and reproducing it is most of the score. Ask: *if I knew this company/sector deeply, what is the ONE organizing structure the report is built around?* Examples of native spines the generic toolkit would miss:

- **Japanese trading houses** → the **five-function sequential build-up** (商品贸易 → 信息 → 金融信用 → 产业组织 → 事业投资), each era solving a specific 核心矛盾 and "earning the spread on eliminating an asymmetry" (消除资源/信息/资金不对称). (see `frameworks-investing.md` §H)
- **VC/fund studies** → the **找得到 / 看得清 / 投得进 / 帮得上** four-stage spine, AND the lead partner's OWN named scoring models (e.g. a marketplace 10-indicator model, a "10x valuation club" model). (see `frameworks-investing.md` §C–D)
- **Incumbent platform companies (Microsoft/Google/Meta)** → the **"能否再造操作系统 / 重构流量入口"** north-star binary. (see `frameworks-ai.md` §N)
- **Title-as-question.** Many reports pose a provocative replicability/sustainability question in the title (能不能 benchmark？/ 是不是要被全端走？/ 能否基业长青？/ 能否再造操作系统？). **Lead with and explicitly ANSWER that question** rather than substituting a self-generated thesis.

---

## 1. 理解更新 — open with the reframe, not a definition

DecadeX's signature move is to *open by updating the prior understanding*.

- **Version the thesis.** Tabulate V1→Vn with explicit ✓ (got right) and ✗ (got wrong) marks. Examples actually used: public-chain V1 viewed Web3 through an internet lens (✗); EV V1-V3 bet on "software/SaaS-driven value chain" then self-corrected to "车还是车" (✗); car-online maintained 5 versions logging how the view evolved.
- **Lead with the single biggest reframe**, stated as a contrarian one-liner. Examples:
  - "公链现阶段的主要矛盾不是去中心化，而是资产发行效率."
  - "Crypto 的本质是对传统金融的升级和融合，不是 Web3 (asset vs traffic)."
  - "币圈当前最主要的矛盾不是缺用户，而是缺新资产 (assets precede users)."
  - "直播电商的本质是更沉浸的广告，不是团购/人型聚划算."
  - "大模型本质是逻辑的输出机器."
- This frames the whole report as "理解更新" and earns the reader's attention before any data.

## 2. 第一性原理 — re-derive the category, choose the lens

Before analyzing, ask **"what is this thing, really?"** and pick the correct lens. DecadeX repeatedly *rejects the lazy analogy*:

- Crypto: finance lens, **not** internet lens. ("Tesla is NOT Apple — more like Standard Oil"; "smart car ≠ smart phone".)
- Exchange = "包着交易所的一站式服务浏览器" (a one-stop browser wrapped as an exchange) → behaves like an internet brokerage.
- LLM = "逻辑的输出机器" evaluated on logic that is *fast / cheap / strong*.
- Hyperliquid = "链上交易所" (类 Binance/Coinbase), **not** a public chain.

Then **name the 北极星指标** — the single decisive metric (see frameworks files): asset penetration, MTU market-share, 独立访客, GMV, funded-users+AUM, 入金用户数, "can the fund get into the core asset".

## 3. 框架展开 — apply named frameworks WITH numbers

This is the bulk. Pull the cross-cutting frameworks (SKILL.md table) + sector frameworks (`frameworks-*.md`). The discipline that makes it DecadeX:

- **Every framework is applied, not just named.** Don't say "REV/GDP measures tax power" — compute it (SOL ~65% vs ETH low). Don't say "PS valuation" — give the band (ETH bull 100-200x).
- **Anchor relentlessly on hard ratios.** TVL %, MAU, take-rate, REV/GDP, Stable/Total Mcap, OI/Vol, DAU/MAU, penetration %, cost/tx. Prefer *ratios and shares* over absolute numbers.
- **Use correlation coefficients as evidence.** e.g. Stable Mcap vs Top-4 chain mcap r=0.7-0.85; CEX-CEX volume r=0.92-0.97 vs CEX-Hyperliquid r=0.63 ("不是一波人"); user-activity vs crypto price r=0.83.
- **Decompose into a formula, then locate the driver.** Ad revenue = DAU × 渗透率 × Impression × Adload × eCPM; GMV = MAC × ARPU; search revenue = clicks × ad price → then identify which factor is currently moving.
- **Quantify the thresholds.** 神器渗透率 > 5% = eruption; Critical Mass ~500M MAU; Scalability = TPS / cost-to-validate-all-txs; training ≈ 6NT FLOPs; mixed-precision+Adam = 16 bytes/param = 8× inference.

## 4. 竞争格局 — the head-to-head table is the backbone

DecadeX reports are built around one master comparison table with a **benchmark anchor**:

- **Anchor everything to one reference.** Hyperliquid: every line as "% of Binance" (合约 10/15/20%, 现货 1.5/2.25/3%). EV new-forces: benchmarked against *Tesla's own historical* per-vehicle valuation curve. Gemini: scored vs ChatGPT layer-by-layer (Pre 90/90, Post 90/50, TTS 80/0).
- **Distill each competitor to a one-word "核心基因".** Binance=流量(scale), Coinbase=合规(compliance), FTX=产品创新; Robinhood=trading DNA, Coinbase=crypto-native.
- **Pairwise across layers.** ETH vs SOL: protocol layer (devs EVM:SVM ≈10:1, dapps 10:1 → "已成定局") vs application layer ("未成定数").

## 5. 尽调十问 — the fixed DD scorecard

Apply the standard rubric uniformly so comparisons are apples-to-apples:

- **β (industry):** 行业能否5年翻倍? 十年后行业是什么?
- **α (company):** 竞争优势 / 用户&产品 / 商业模式 (often ×2) / 运营 / 组织&文化 / 成长潜力 (能否涨≥5x?).
- **Timing:** 为什么市场还没发现这个价值? (the contrarian payoff)

Often paired with explicit scoring weights (e.g. Coinbase: 合规护城河 50% / MTU增长 30% / 产品创新 20%; Meta: 流量规模 50% / CEO领导力 30% / AI新产品 20%).

## 6. 估值 — three-scenario, probability-weighted, banded

Never a single point. The template:

1. **Pick PS vs PE by token/equity economics.** Use **PE-style** when ~all revenue buys back the token / near-100% margin (Hyperliquid: 99% buyback). Use **PS** otherwise (internet-broker 3-5x for Coinbase; ETH bull 100-200x).
2. **Bear / Base / Bull**, each: driver metric (MTU, share-of-Binance, ad revenue) → revenue → multiple → **discount** (e.g. 监管折价 keyed to BNB/XRP enforcement drops, -10/-15/-25%) → market cap.
3. **Probability-weight** (e.g. 20/60/20 or 10/60/30 or 25/45/20/10 incl. write-off) → expectation.
4. **Cross-validate with two independent methods** (historical-PS band vs comp-PE; gold + Visa for ETH) and take the mean.
5. **Output a band**, tied to explicit *conditional* assumptions (ETH 3-5yr: $3k/$6k/$10k keyed to L1-scaling + org-efficiency + next-asset-eruption).

## 7. 风险 — name the black swan and the falsifier

- State the **disconfirming risk** explicitly (regulation as 达摩克利斯之剑; ETH's demand-not-supply problem; LLM "三无" no-network-effect).
- Run the **bear-market stress test**: does non-subsidized TVL + DAU survive? (ETH TVL -50%, SOL -85%, Tron stable.)
- Distinguish **organic vs subsidized** demand (Hyperliquid OI/Vol 1.12 organic vs peers ~0.17 wash-trading; Coinbase derivatives volume = subsidy-driven).

## 8. 核心结论 — numbered, conditional, falsifiable

Close with a tight numbered list. Each conclusion: a strong claim, its *condition*, and an observable that would falsify it. Bullish-on-X is always "conditional on (天时/地利/人和)…".

---

## Recurring analytical moves (the DecadeX "tells")

- **Reframe / de-frame consensus analogies** ("Tesla≠Apple", "smart car≠smart phone", "L2 helps ETH" → "L2 is tax-sacrificing marketing").
- **Reframe a canonical framework** rather than accept it (re-order the trilemma into 去中心化 > 可扩展性 > 安全).
- **First-principles deductive chains** (CAP → trilemma → "multi-chain inevitable" + "scaling is the main contradiction").
- **Cross-domain analogy as a reasoning tool** (chain as bank/broker; L1 token as sovereign currency; LLM as OS; Crypto1.0→2.0 paralleled to Web1.0→2.0; settlement layer = clearing house).
- **Historical-timeline overlay** to argue eruptions are right-side, observable-not-predictable ("类似潮起潮落").
- **Counterfactual / reductio** (IDFA episode reverse-proves device-data is the moat; Sushiswap vampire attack as the "一增一减" benchmark to disprove HL was bled).
- **Build a private eval when public benchmarks are flawed** (X-Eval: o3 83% vs Gemini 60%, to reverse-infer Gemini's retention problem is model capability).
- **Quantify tail risk from precedent** (regulatory discount sized to BNB -10%→-27% / XRP -63% drops).
- **Layer the universe** (应用层/中间层/系统层; 收单/执行/清结算/托管) and map named exemplars to each slot.
- **Date-stamp time-sensitive claims** (spec sheets, 1M-context deployment status) to flag shelf-life.

---

## Data-sourcing discipline

- Lead with **shares and ratios**, not raw totals (market-cap %, take-rate, REV/GDP, penetration %).
- **Hard business-anchor mandate (do the financial teardown BEFORE the framework layer).** DecadeX pairs every framework with the subject's OWN financials. Jargon-heavy, data-poor analysis is penalized. Pull the company's real numbers first: installed base / market share, segment revenue & margin, per-unit pricing, and the sector's native ratios. Worked anchors the house actually used:
  - *Platform incumbents:* installed-base & share (Windows装机 vs Android; share trend), segment revenue mix & margin (Office 365 渗透率/企业版占比, Azure 毛利 ~70%), per-seat AI pricing (Copilot $/seat).
  - *Funds:* a fund-by-fund **IRR/TVPI/DPI ladder**, AUM, dry powder, deal/exit counts, median deal-size & valuation trend, and the **named blow-up** (e.g. the oversized vintage with a poor IRR). Do NOT invent MOIC scenarios — ground them in the real fund-family ladder.
  - *Miners:* hashrate (EH/s), BTC held vs produced vs bought, avg production cost with/without depreciation, marginal cost, D/E, employee count, self-hosted vs third-party-hosted %. Penalize generic/forward-dated numbers.
  - *Hardware monopolists:* BOM teardown (cost vs price) and the up/down-stream squeeze (its own suppliers' pricing power), demand sizing in *units × $* (e.g. training/inference GPU tables off cloud-capex × a benchmark attach rate), not vague capex aggregates.
- Tag claims **事实 / 推断 / 观点 (fact / inference / opinion)** when precision matters (compute-fundamentals does this per-row).
- Honestly note **simplifications and boundaries** (the AI-compute lectures list every assumption dropped).
- Treat the existing **report corpus as precedent** — cite the house's prior conclusion and update it (see `report-index.md`).

---

## Educational guardrails (always)

- Conclusions are **conditional, banded, falsifiable** — never a certainty or a personalized call.
- Reproduce the *reasoning style*; flag that conclusions may be wrong and are not advice.
- Prefer "what would have to be true" and "what would falsify this" over point predictions.
