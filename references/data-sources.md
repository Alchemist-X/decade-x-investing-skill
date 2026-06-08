# Data Sources — Where & How to Get DecadeX-Style Research Data

> **Educational.** This catalogs *where DecadeX actually sources its data* (mined from its public reports) plus the concrete **free, no-key** sources the bundled `tools/` scripts cover. Not financial advice.

This is the **数据获取 (data acquisition)** reference for the workflow. The DecadeX discipline is **hard business anchors before jargon** (worldview #13): you cannot do the teardown without the numbers. Get the data first, then deploy frameworks.

**How to read the tables:** each row gives *what it provides*, *access* (🆓 free / 🆓+key free-with-key / 💲 paid), and the matching `tools/` script if one exists. Free/no-key sources with a tool are the fastest path — prefer them.

---

## TL;DR — the four bundled tools (all FREE, stdlib-only, no key required)

| Tool | Source(s) | Gives you | Key? |
|---|---|---|---|
| `tools/fetch_edgar.py` | SEC EDGAR (`data.sec.gov`) | US-company financials (revenue, net income, EPS, shares, CFO, CapEx…) | 🆓 no key (optional `SEC_USER_AGENT` for a polite UA) |
| `tools/fetch_crypto.py` | CoinGecko + DefiLlama | Token price/mktcap/volume; chain & protocol TVL | 🆓 no key (optional `COINGECKO_API_KEY`) |
| `tools/fetch_macro.py` | US Treasury Fiscal Data; FRED | Treasury avg interest rates (no key); FRED series (free key) | 🆓 Treasury; 🆓+key FRED (`FRED_API_KEY`) |
| `tools/analyze.py` | none (pure compute) | reverse-DCF, scenario weighting, owner-earnings yield | 🆓 no network |

See `tools/README.md` for full CLI. Below, sources that map to a tool are flagged **→ tool**.

---

## Crypto (公链 / 交易所 / 稳定币 / DeFi / PerpDex)

DecadeX's crypto North Star is **资产渗透率** and the spine is on-chain financials (TVL > Volume > Core-Dev > MAU at the protocol layer). Most of what it needs is free and on-chain.

### Free / no-key (start here)

| Source | What it gives | Access | Tool |
|---|---|---|---|
| **CoinGecko** | Price, market cap, 24h volume, supply, ATH, rank | 🆓 (optional demo key) | **→ `fetch_crypto.py price/markets`** |
| **DefiLlama** | TVL by chain & protocol, DEX volume, stablecoin mcap, yield/APY, ETF trade-volume | 🆓 (web + API) | **→ `fetch_crypto.py tvl/protocol-tvl`** |
| **rwa.xyz** | RWA tokenization size by asset class (Treasuries, private credit, stocks, real estate); new-issuance counts | 🆓 dashboards (paid API) | — |
| **The Block** | Exchange/ETF volume dashboards, BTC/ETH ETF flows & AUM | 🆓 dashboards (paid Pro) | — |
| **DappRadar** | Dapp counts, active addresses/users, dApp rankings per chain | 🆓 (paid Pro API) | — |
| **CoinShares fund-flows report** | Weekly institutional flows & AUM by provider (IBIT/BlackRock, Grayscale, Fidelity, Bitwise…) | 🆓 weekly report | — |
| **On-chain explorers / Dune-type dashboards** (HypurrScan, ASXN, growthepie, Etherscan) | Perp/spot volume, OI, DAU, HLP vault TVL/APR, fee splits, L2 cost/tx, ETH burn/issuance | 🆓 | — |
| **l2beat** | Per-L2 TVL$ & market-share %, rollup type, stage, sequencer/proof status, upgrade-delay — the canonical L2 competitive table (Arb ~49.6%, OP ~27.4%, Base, zkSync…) | 🆓 | — |
| **L1 gross-margin / remittance ratio** (growthepie, ultrasound.money, Token Terminal-free views) | L1 fee revenue vs issuance → gross-margin time series (the "cloud-computing model" proof, ~70-90%); L2 net-rev vs L1-paid remittance ratio over time | 🆓 (some paid) | — |
| **Solana/EVM real-TPS dashboards** (solscan, blockchair, chainspect) | Measured (not theoretical) TPS, gas$/action, DAU per chain — for the cross-chain bench (Solana ~2398 vs ETH ~16.4 TPS) | 🆓 | — |
| **L2 / project funding & founders** (Crunchbase-free, RootData, project blogs) | Founder pedigree, funding rounds & valuations (e.g. Arbitrum Series B $100M/$1.2B; Optimism Series B $150M/$1.65B), Base-OP revenue-split terms, governance-token caps | 🆓 (paid tiers) | — |
| **Jito / Flashbots** | MEV figures (for REV = Gas + MEV) | 🆓 | — |
| **Electric Capital Developer Report / GitHub / eips.ethereum.org** | Core-dev counts, commits per chain, EIP/ERC counts & authorship concentration | 🆓 | — |
| **Company filings** (Coinbase 10-Q/10-K & shareholder letters, Robinhood IR, Circle/CRCL S-1) | MTU, ARPU/ATRPU, revenue splits, AUC, USDC revenue & distribution split, reserve composition | 🆓 (SEC EDGAR) | **→ `fetch_edgar.py`** (US tickers: COIN, HOOD, CRCL) |
| **Regulatory texts** (GENIUS/STABLE/CLARITY, MiCA, HK Stablecoin Ordinance, Form PF) | Compliance scoring & timeline inputs | 🆓 (Congress.gov, regulator sites) | — |
| **Issuer disclosures** (BlackRock BUIDL, Franklin FOBXX, Ondo, Securitize, PYUSD, Visa USDC) | RWA AUM, stablecoin circulation, settlement volume | 🆓 | — |

### Paid (DecadeX uses these; substitute free equivalents above when you lack access)

| Source | What it gives |
|---|---|
| **Token Terminal** | On-chain P/S, P/E, REV, fees, revenue trends — the canonical crypto-financials terminal |
| **Messari** | Exchange spot-volume splits (US vs non-US), ETF share, protocol research |
| **Artemis** | Stablecoin issuance/circulation; stablecoin vs Visa/ACH/PayPal cross-rail comparison |
| **Token Insight** | Exchange spot/derivatives volume rankings & venue market-share |
| **App Annie / data.ai** | App MAU/DAU/downloads for Coinbase/Binance/Robinhood/Kraken |
| **SimilarWeb-style** | Web visits, UV, visit duration, bounce, app retention for exchange/PerpDex front-ends |

**Crypto metric note:** for REV/GDP 税权, combine free Gas (Etherscan/L2 dashboards) + free MEV (Jito/Flashbots). For 渗透率 use addresses-÷-population from explorers. None of these need a paid terminal.

**Exchange / Coinbase quantitative-anchor sheet (reusable example — the figures a deck-quality teardown supplies, period-locked).** A blind 10-K-only reconstruction structurally under-supplies the granular monthly/competitor data the house gathers; acknowledge that limitation rather than substituting a thesis pivot. The anchors to reproduce:
- **Revenue line-item split** (not a vague "~30-40% price-neutral"): 零售 ~55% / 机构 ~4% / 稳定币 ~19% / 质押 ~10% / 托管 ~2% / 利息 ~5% / 其他 ~5% (散户占交易量 94-95%).
- **Forward forecast engine** (fee-rate ladder): 零售费率 ~1.7%, 机构 ~0.03%, 衍生品 ~0.03%; ETF ~90% 净流入在自家托管; USDC 利息分润 ~60% to the exchange, reserves ~80% T-bills / 20% cash. → a quarterly revenue forecast (the house produces a concrete 24Q1 figure + a bull-peak quarterly figure), NOT a qualitative reframe.
- **Quarterly net-income walk** proving 穿越牛熊 (the first bull-through-bear positive quarter), monthly head-to-head volume vs Binance, the CEX market-share pie (Binance ~47 / OKX ~17 / Bybit ~14 / Coinbase ~2%), Base-chain metrics (活跃地址 / 交易笔数 / TVL / 月收入 vs Arb/OP), stablecoin sizing (Top15 mcap, USDC机构驱动, BTC-ETF净流入累计/单日峰值), cost structure (运营 ~40-50% / 销售 ~10-20% / 技术 ~40%, 合规成本 ~1/3 headcount, 牌照全套 ≥$300万), and the operational mechanism (合约靠渠道/代理, KOL 首单返佣 ~70%; 国际站 = 存量变现). **Benchmark every competitive line as "% of Binance."**

---

## AI & Equities (大模型 / 算力 / 广告平台 / 自动驾驶)

DecadeX's AI work has two halves: (1) **equity teardowns** of ad/cloud giants (Meta, Alphabet, ByteDance, Kuaishou) and (2) **model/compute capability evals**. The equity half is mostly free via filings; the eval half uses public leaderboards plus a private eval.

### Free / no-key

| Source | What it gives | Access | Tool |
|---|---|---|---|
| **Company filings** (10-K/10-Q, earnings calls) | Revenue, ad/cloud revenue, TAC, FCF, CapEx, per-product (FB/IG/Reels/Search/YouTube/GCP) revenue & growth | 🆓 (IR / SEC EDGAR) | **→ `fetch_edgar.py`** (META, GOOGL, AMZN, MSFT, NVDA…) |
| **LMArena (Chatbot Arena Elo)** | Overall + per-skill model Elo (Coding/Math/Hard Prompts/Creative/IF/Multi-Turn) | 🆓 (lmarena.ai) | — |
| **Artificial Analysis** | Model intelligence index, output tokens/s, $/M-tokens, HLE | 🆓 (artificialanalysis.ai) | — |
| **Public benchmarks** (MMLU/MMLU-CF, SimpleQA, GAIA, HLE, GPQA, Competition Math) | Logic, hallucination, PhD-science, math accuracy | 🆓 (HuggingFace/arXiv) | — |
| **HuggingFace model cards** | Layers L, hidden dim d, heads, FFN dim, context len, vocab, params N (for FLOPs/VRAM math) | 🆓 | — |
| **Chip vendor spec sheets** (NVIDIA/Google TPU/AMD/AWS/Groq/Cerebras) | FLOPS (FP4/8/16), HBM cap & bandwidth, NVLink/ICI, pod scale | 🆓 (vendor sites) | — |
| **Vendor API docs** (OpenAI/Anthropic/Google) | Context-window limits, model retirement dates | 🆓 | — |
| **arXiv** | ZeRO/Megatron/FlashAttention/Scaling-Law formulas; UX-comparison papers; data-contamination papers | 🆓 | — |
| **nuScenes** | Autonomous-driving detection accuracy (pure-vision vs sensor-fusion) | 🆓 dataset | — |
| **Tesla AI Day / filings** | FSD cumulative miles, FSD penetration, shadow-mode/4D-labeling/Dojo | 🆓 | — |
| **Electric Capital Developer Report / GitHub / NVIDIA dev pages** | Ecosystem-moat counts: developer count, GitHub contributors, app count, downloads — for the subject AND the open-source challenger (e.g. CUDA 4M devs / 32.6K contributors / 3K apps / 40M downloads vs ROCm ~5% of each). Use REAL counts; never fabricate a ratio | 🆓 | — |
| **SEC filings / proxy (DEF 14A) / 13F** | Founder voting power %, dual-class structure, insider stake, top external holders (Vanguard/BlackRock %), employee count (for per-employee mktcap vs peers) | 🆓 (SEC EDGAR) | **→ `fetch_edgar.py`** |
| **Stock-history / drawdown data** (Yahoo Finance, stockanalysis.com) | The FULL historical drawdown sequence (every peak-to-trough %), for the cyclicality fingerprint | 🆓 | — |

### Paid

| Source | What it gives |
|---|---|
| **eMarketer** | Global digital-ad/e-commerce/game market size, platform ad-share, ARPU |
| **Similarweb** | Web visits, UV, visits/UV, dwell, bounce, traffic-source mix (GPT vs Gemini vs Claude web) |
| **data.ai (App Annie)** | App MAU/DAU/retention/downloads for ChatGPT/Claude/Gemini & social apps |
| **Ahrefs** | SEO/keyword data; AI-Overview click-rate impact |
| **Forrester** | Smart-device-user TAM anchors |
| **PitchBook / CB Insights** | AI primary-market financing (deal counts, deal size, valuations) |
| **Canalys / Synergy** | Cloud market share, GenAI-platform share, per-cloud margins |
| **AppGrowing-type** | Ad-creative volume, daily advertiser counts, top advertisers |
| **Stratechery / industry interviews** | Qualitative monetization-path & strategy signals |

### Private (DecadeX-internal — replicate the *method*, not the dataset)

- **X-Eval** — DecadeX's own 138-question eval (logic/daily/deep-search), run in temporary-chat mode for `pass@1`, to dodge public-benchmark contamination. You can build your own equivalent; the lesson is *distrust leaked benchmarks, test on fresh hard prompts*.

**Big-tech-AI per-product penetration anchors (the bases the bottom-up build needs — reproduce, don't hand-wave "4亿 seats").** For incumbent-platform AI valuations (see `data-analysis.md` 2.3b/2.3c), pull the real per-surface bases from filings/IR + secondary sources:
- **Microsoft-type:** Windows 装机 (~15.6亿 vs Android ~20亿; Win 市占 97%→20%, 桌面 ~74% vs Mac ~15%), Office 365 收入占比 (~94.9%, 企业版 ~87%), Office/Copilot ARPU, GitHub 用户 (~1亿) & Copilot 渗透率 (~0.4%→1%) & 定价 ($10 个人 / $19 企业), Azure 毛利 (~70%), Copilot $/seat ($30/月 M365). Token-econ anchor: ChatGPT ~$700K/day inference, ~7万亿 tokens/day.
- **Hardware-monopolist (NVIDIA-type):** chip spec table (TFLOPS / HBM / bandwidth / price for H100/A100/4090; inference-node count vs Groq), generational interconnect (NVLink 160→900 GB/s, 4→18 GPU), Huang's-Law (~1000x AI-inference perf/decade), BOM line items ($200 die + $1500 HBM + $700 CoWoS + $500 other), top-10 H100 buyer table with the buyer-split %, HBM supplier diversification (SK Hynix → +Samsung+Micron), and the downstream-demand evidence (top-app DAU/MAU, GPT param progression GPT-1 117M → GPT-4 >1T, training tokens ~13T) used to ground a "North Star not triggered" claim.

---

## Consumer (汽车/EV / 直播电商 / 商社)

DecadeX consumer work pairs **official macro denominators** (国家统计局, 乘联会) with **expert interviews** for the non-public operating metrics (Ad Load, take-rate splits, 客单价, 复购率) that filings never show.

### Free / no-key

| Source | What it gives | Access | Tool |
|---|---|---|---|
| **国家统计局 (NBS China)** | Online-retail total & total social retail — the denominators for e-commerce/live-commerce penetration | 🆓 (stats.gov.cn) | — |
| **乘联会 (CPCA) / 中汽协 (CAAM)** | PV & NEV monthly/annual sales by brand & model, NEV penetration, exports by region | 🆓 | — |
| **CleanTechnica** | Global NEV sales, global Top-10 EV models, Tesla/BYD global share | 🆓 | — |
| **Listed-company filings** | Revenue, GMV, take-rate (ad vs commission), gross/net margin, SG&A/R&D, capex, deliveries, cash runway | 🆓 (IR / SEC / HKEX) | **→ `fetch_edgar.py`** (TSLA, RIVN…); HK/CN names via HKEX/CN IR |
| **视频号 / 淘宝 official reports & white papers** | Creator counts, daily uploads, GMV & penetration reference | 🆓 | — |
| **McKinsey China Consumer survey** | Consumer demographics & spend-share by age cohort | 🆓 report | — |
| **Company sites + review sites + owner forums** (Car&Driver, Rivian forums, Xueqiu) | Price bands, trims, expert verdicts, owner sentiment, market-segmentation grids | 🆓 | — |

### Paid

| Source | What it gives |
|---|---|
| **艾瑞 (iResearch)** | Live-commerce GMV series, online-ad format mix, app time-share |
| **QuestMobile** | App-category time-share, DAU, per-user daily minutes |
| **淘数据 / 飞瓜 (Taosj / Feigua)** | Douyin/Kuaishou category GMV breakdowns, 店播 share — inputs to the by-category TAM |
| **Wind** | Cross-company valuation/financials (mktcap, PE TTM/fwd, PS, margins) for comp tables |
| **专家访谈 (expert networks)** | Ad Load, traffic-source mix, MAC/DAU, 客单价, CPM, cohort GMV split, 复购率, 店播 share — the figures *not* in filings |

**Consumer note:** the live-commerce thesis ("it's immersive advertising") rests on **take-rate decomposed into ad + commission** — an expert-interview number. When you lack expert access, triangulate: filings give blended take-rate; published ad-load benchmarks + traffic mix let you back into the ad-vs-commission split.

---

## Funds, Capital & Macro (VC / 捐赠基金 / 技术周期 / 利率)

This domain frames "the price of money" (risk-free rate), private-market sizing, and fund performance ladders. The rate side is fully free via Treasury/FRED; fund-level data is mostly paid.

### Free / no-key

| Source | What it gives | Access | Tool |
|---|---|---|---|
| **US Treasury Fiscal Data** | Latest avg interest rates across the curve (Bills/Notes/Bonds/TIPS) — a clean "price of money" proxy | 🆓 no key | **→ `fetch_macro.py treasury`** |
| **FRED** | Named macro series (CPIAUCSL, GDP, T-bill/10y history, etc.) | 🆓 + free key | **→ `fetch_macro.py fred <SERIES>`** (needs `FRED_API_KEY`) |
| **US Treasury yield history / FRED 3M T-bill** | Risk-free-rate regime (14% 1981 → ~0 → ~5% 2025) vs VC fundraising & IRR | 🆓 | **→ `fetch_macro.py`** |
| **Company S-1 / 10-K & cap tables** | Stake-at-IPO, dilution, return multiples; NOC/CHGG fundamentals; on-chain protocol revenue | 🆓 (SEC EDGAR) | **→ `fetch_edgar.py`** |
| **Stock price history** | Long-run tech-capital-cycle charts; ARK position-vs-price overlays | 🆓 (Yahoo Finance) | — |
| **ARK holdings & "Big Ideas"** | Daily per-fund holdings & weights, expense ratios, AUM, returns, ARK's own scoring models | 🆓 (ark-funds.com) | — |
| **ETF benchmark indices** (QQQ, IWF, NASDAQ Internet, S&P 500…) | Benchmarks to judge alpha | 🆓 | — |
| **MIT / MITIMCo & NACUBO-style endowment disclosures** | Endowment allocation, team size, return ladders, peer-median returns | 🆓 (annual reports; NACUBO study) | — |
| **On-chain explorers / DeFiLlama / Dune** | BTC mktcap & node count, BTC/ETH penetration, DeFi protocol deposits & revenue | 🆓 | **→ `fetch_crypto.py`** (TVL) |
| **Economic-history datasets** | Long-run cost-of-production curves (cotton, steel, oil, transistors) for dating tech revolutions | 🆓 | — |
| **a16z / NfX / HBR / Morgan Stanley / DeepLearning.AI** | Network-effect math (Metcalfe), marketplace evaluation, HumanEval Agent vs non-Agent | 🆓 | — |
| **Crunchbase-free / company press / news archives** | Per-deal entry round, entry valuation & estimated multiple for a fund's star cases (the deal-level table the house builds — e.g. entry-round $ and the X-multiple per named portfolio company); founder/partner quotes & the source appendix | 🆓 (paid tiers) | — |
| **Japanese IR — TSE / 各社IR / EDINET / METI / 日本统计局** | Per-company segment-revenue mix (¥ + %), overseas-revenue %, DuPont inputs (margin/turnover/equity-multiplier 15-20yr), Capex/CFO & (分红+回购)/EBITDA & dividend-payout annual series, dividend yield & EV/EBITDA history (20-yr lows), JGB 10yr; investor bond-issuance amounts/dates & staged stake %s | 🆓 | — |

### Paid

| Source | What it gives |
|---|---|
| **PitchBook** | Fund IRR/TVPI/DPI/AUM by vintage, LP roster & type, deal-size median, exits — the core fund-performance source. For a fund study, build BOTH the per-fund IRR/TVPI/DPI/RVPI ladder (every fund) AND the per-deal star-case table (named partner / entry round / entry valuation / multiple) — the human's quant edge lives in the deal-level multiples, not only fund-level IRR |
| **CB Insights** | Unicorn counts & valuations, financing rounds |
| **BofA / Ibbotson SBBI** | Long-run global asset-class size (402T→545T→649T) & return quartiles |
| **Capgemini World Wealth Report** | HNW/UHNW wealth by region, millionaire density, generational-transfer estimates |
| **Synergy / Canalys** | Cloud market share & availability-zone counts |
| **Sensor Tower / QuestMobile** | App MAU & penetration for P/MAU valuation |

---

## Practical sourcing rules (DecadeX discipline)

1. **Free-first.** The four bundled tools (EDGAR, CoinGecko, DefiLlama, Treasury/FRED) cover the spine of every domain. Reach for paid terminals only for the figures they genuinely can't reconstruct (Ad Load, fund IRR ladders, web-traffic).
2. **Filings are primary.** For any US-listed name, `fetch_edgar.py` beats secondary aggregators — it's the issuer's own number. Pair `NetCashProvidedByUsedInOperatingActivities` (CFO) with `PaymentsToAcquirePropertyPlantAndEquipment` (CapEx) for FCF.
3. **Period-lock the data (worldview #11).** Pull figures as-of the report's date; don't smuggle later numbers into a period-locked thesis.
4. **Triangulate non-public metrics.** When an expert-interview figure (take-rate split, MAU share) is unavailable, reconstruct it from free primaries + published benchmarks and *flag it as inferred*.
5. **Distrust leaked benchmarks (X-Eval lesson).** For model capability, prefer fresh/hard evals over headline MMLU.
6. **No keys, no secrets.** Every bundled tool runs keyless; optional env keys (`SEC_USER_AGENT`, `COINGECKO_API_KEY`, `FRED_API_KEY`) only raise rate limits or politeness — never hardcode them.
7. **Prefer QUARTERLY over FY, and the FULL series over a single print.** Pull the quarterly net-income/margin/BTC-held walk, the 15-20yr DuPont series, the full drawdown sequence — FY aggregates are the laggard failure mode.
8. **Anti-fabrication (every number is sourced or tagged).** Do NOT invent a plausible-sounding ratio (dev ratios, fee-decline figures, mcap-% attributions) when a real figure exists — pull the real one (Electric Capital / l2beat / Token Terminal / filings) or tag it **推断/illustrative**. Never attribute a fabricated metric to a prior report version. Never let a tool output run on placeholder inputs anchor the headline.
9. **Acknowledge the data-supply limitation honestly.** When the house used proprietary primary data (monthly competitor volumes, MTU/MAU series, expert-interview take-rate splits, deal-level entry valuations) that an EDGAR/CoinGecko-only pass cannot reproduce, SAY SO — do not paper over the gap with a self-invented thesis pivot.

After acquiring data, go to **`references/data-analysis.md`** to turn it into DecadeX-style conclusions.
