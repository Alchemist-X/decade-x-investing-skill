# Data Analysis — The DecadeX Quantitative Playbook

> **Educational.** The metrics and methods here are mined from DecadeX's public reports. This is the **数据分析 (data analysis)** reference: how to turn the raw data from `data-sources.md` into DecadeX-style, numbers-anchored conclusions. Not financial advice.

**The DecadeX rule (worldview #13):** *apply frameworks with numbers, not just names.* A framework you only name is penalized. Every method below has (a) a concrete formula, (b) what the number *signals*, and (c) which `tools/` helper computes it where one exists.

The bundled compute tool is **`tools/analyze.py`** (pure, no network): `reverse-dcf`, `scenarios`, `owner-yield`. Data tools (`fetch_edgar.py`, `fetch_crypto.py`, `fetch_macro.py`) supply the inputs. See `tools/README.md`.

---

## Part 0 — The quantitative-depth bar (read FIRST — this is where blind analyses lose the most points)

The gap between a passing blind analysis and a real DecadeX report is almost never the *framework names* — it is the **density and specificity of the numbers**. The house produces full multi-cell tables and concrete point outputs; weak reconstructions produce a vague band and a named framework. Hold yourself to these rules:

1. **BUILD THE TABLE, don't cite a band.** Where the house has a worked table, reproduce *the whole grid*, every cell, all cases — not a one-line summary. The recurring signature tables (reproduce in full):
   - **Demand-sizing table** (units × $) in ALL THREE cases: optimistic / neutral / **pessimistic**. Do NOT drop the bear/pessimistic leg — laggard analyses routinely give only opt+neutral. (e.g. a GPU report's 3-case training/inference table: per-case training-unit count, training:inference ratio, inference-unit count, and $ for each.)
   - **Segment revenue + margin FORECAST table** per reporting segment, 2 years forward, opt+neutral, with explicit YoY% per cell — *before* any valuation. Tie the SOTP/PS to forecasted segment operating income, not to an abstract method demo.
   - **Per-product / per-SKU bottom-up build** (see 2.3b): one row per surface (Copilot SKU, token line, ad product, Coinbase revenue line).
   - **Quarterly time-series** (not FY aggregates): quarterly revenue, net income, gross/net margin, BTC-held, production cost, cash-flow. A quarterly net-income walk that shows the *first* bull-through-bear positive quarter beats any FY total.
   - **Per-deal / per-holding table** for funds: named lead partner, entry round, entry valuation, estimated return multiple — AND the fund-family IRR/TVPI/DPI/RVPI ladder (every fund, not "7x band").
   - **Competitor market-share table** with the actual % figures (CEX share pie; L2 TVL share; miner EV/Hashrate grid), not qualitative rankings.
   - **DuPont time-series** (15-20yr: net-margin / asset-turnover / equity-multiplier) for cash-cow / leverage stories — not static point estimates.
2. **OUTPUT CONCRETE POINT VALUATIONS, not just multiples/methods.** The deliverable is *specific numbers*: SOTP fair value $X.XXT, bear $Y, bull-case derived price $Z, leverage-proxy price grid (BTC $70K/$100K/$150K → equity $A/$B/$C). Producing "PE/G ~1.2, CAGR 42%" without ever landing the dollar figure the house produced is a miss. Always carry the method through to the number.
3. **DERIVE the headline, don't assert it against the precedent.** If the house concluded "~3.5x in 5 years" or "bull price ~$7331", you must *rebuild the bottom-up model* and land your own number — and if you deviate, the deviation must fall out of the rebuilt model, not be asserted. A "1.4x" downgrade with no rebuilt per-product model loses to the human's derived 3.5x.
4. **Reproduce the house's exact figures when period-locked.** Prefer the report's real anchors (developer counts, drawdown sequences, installed base, fund IRR ladder, BOM line items) over self-computed placeholders. When you must estimate, tag it (rule 5).
5. **Anti-fabrication (CRITICAL).** Every number is tagged **事实 (sourced)** / **推断 (inferred)** / **illustrative**. Do NOT (a) invent ratios that sound plausible ("~10:1 EVM:SVM devs", "$30M→$0.5M fee") when a real figure exists — pull the real one (Electric Capital dev counts, etc.); (b) fabricate a precedent metric and attribute it to a prior version (e.g. inventing "6/14/25% of mcap" as "what V1 said") — if it is your own inference, label it yours and separate it from the cited precedent; (c) let a tool's *placeholder* output (analyze.py run on made-up inputs) anchor the headline conclusion — tool outputs with no real financial inputs are illustrative-only.
6. **The signature DecadeX house stats — include them when the genre calls for them:** per-employee market cap (e.g. ~$100M/employee with the employee count vs peers), the FULL historical drawdown sequence (not just the first few), ROI-on-capital framing ("<$X capital → $Y returns"), the named blow-up/cautionary peer. These evidentiary fingerprints are cheap to add and consistently missed.

---

## Part 1 — Key metrics by sector (name · formula · signal)

### Crypto

| Metric | Formula / definition | What it signals |
|---|---|---|
| **TVL / non-subsidized TVL** | Capital in a chain/protocol's contracts; strip incentive-driven inflows for non-subsidized | Top protocol-layer ranking metric; the bear-market "立住" test (ETH −50%, SOL −85%, Tron stable). `fetch_crypto.py tvl/protocol-tvl` |
| **Volume** | On-chain / exchange traded value over a period | Top *application*-layer metric; sizing demand value. `fetch_crypto.py markets` (24h vol) |
| **MTU / MAU / DAU** | Monthly transacting users / active addresses | User-side activity; Coinbase core rev = MTU × ARPU |
| **ARPU / ATRPU** | Annual trade-volume-per-MTU × retail fee rate | Valuation driver; Web3 high-ARPU thesis (5–10× Web2) |
| **Take rate / effective fee** | Revenue ÷ volume (Perps ~0.03%, Spot ~0.025%) | Revenue projection (Vol × take rate); fee convergence |
| **PS** | Market cap ÷ annualized net revenue | Cyclical valuation (ETH 40–100×, SOL 30–800×, Hype 30–50×); cheap in bear |
| **PE** | Market cap ÷ earnings (buyback-model tokens) | Hyperliquid-style (99% rev buys back token) comp valuation |
| **REV & REV/GDP (税权)** | REV = Gas + MEV; 链上GDP = end-user fees to dApps (excl. L1 Gas); REV/GDP = L1's value-capture | L1 "taxation power" (SOL ~65% vs ETH weak) |
| **Stable/Total & Stable/Top4 mcap** | Stablecoin mcap ÷ total (and ÷ BNB+TRON+ETH+SOL) | Risk-pricing barometer (bear 10–20%, bull 5–10%) |
| **Inflation / issuance / burn** | Annualized issuance − burn (ETH ~0.79%, SOL 8%→1.5%) | Monetary scarcity / dilution |
| **OI & OI/Vol** | Open interest; OI ÷ Volume (Hype 1.12 vs Aster 0.32) | Organic trading vs wash/airdrop 刷量 |
| **Vol/TVL, Vol/MAU, Vol/Tx** | Capital-efficiency & per-user ratios | Whale/wash detection (Hype Vol/TVL ⅕–1/15 of peers = more retail) |
| **Penetration (资产 vs 用户)** | On-chain assets ÷ global assets; owners ÷ population | Mass-adoption timer ("~1995 internet") |
| **Correlation (R²)** | Pearson r / R² between series | Coupling/decoupling (MAU↔rev R²=0.961; Stable↔Top4 0.7–0.85) |
| **Cost/tx** | L2 per-tx cost pre/post EIP-4844 (Arbitrum −98%) | L1's share of rollup value (77%→8%) |
| **L1 gross margin (time series)** | L1 fee revenue − issuance cost, as % (ETH ~70-90%) | The "business model = cloud computing" PROOF; assert the model only WITH this series |
| **Gas cost per action** | units × (base fee + priority fee); per-action gas (send ETH 21000, ERC-20 65000, NFT ~85000, Uniswap swap ~184500) | Concrete cost table behind "gas collapse"; ties to the upgrade roadmap |
| **L2→L1 remittance ratio (time series)** | L2 net revenue ÷ L1-paid fee, charted over time | The real value-capture evidence (ratio shrinking) — not a single −95% figure |
| **Per-L2 TVL share** | each L2's TVL$ and % of total L2 (Arb ~49.6% $10.89B, OP ~27.4% $6.01B, Base, zkSync…; top-5 Op-Rollup ~85%) | Competitive landscape with real figures, not qualitative rank |
| **Real cross-chain TPS** | measured TPS (Solana ~2398 vs Ethereum ~16.4), not theoretical | Whether a rival is a genuine application-layer competitor |
| **Core-dev count** | core/ecosystem devs (ETH ~2000; Arb ~37, OP ~68) via Electric Capital | Protocol-layer ranking; use REAL counts, never a fabricated ratio |

### AI & equities

| Metric | Formula / definition | What it signals |
|---|---|---|
| **Ad-platform revenue** | 收入 = 广告库存 × 加载率 × CPM × CTR | Decompose growth into traffic-driven vs monetization-driven |
| **Traffic scale** | MAU × monthly avg user-hours | The core ad-platform moat; >5億 MAU = "Next Level" |
| **ARPU / ARPMAU** | Revenue ÷ users (GPT: sub-fee ÷ MAU = 0.69) | Monetization potential; scale-effect (bigger base → higher ARPU) |
| **Gross margin** | Gross profit ÷ revenue (Meta ad ~80%, Azure ~70%) | Business quality ("easy money") |
| **FCF / CapEx-to-CFO** | CFO − CapEx; CapEx ÷ CFO (Meta >50%) | GPU-arms-race commitment; AI CapEx as compute-Beta. `fetch_edgar.py` CFO & CapEx tags |
| **TAC & 赚钱倍数** | Traffic-acquisition cost; ad-rev ÷ TAC (Google ~4.6×) | Google's "buy traffic cheap, monetize dear" moat |
| **Single-query economics** | $/search (Google $0.014 vs OpenAI $0.05–0.55); $/MAU-serve vs ARPMAU | Can an LLM ad-monetize? Does a sub cover cost? |
| **Rule of 40** | Rev-growth % + op-margin % > 40 | "Burn-for-growth" → "healthy organic" (GCP 24Q2+) |
| **Retention / DAU/MAU** | D1/W1/M1 retention; stickiness ratio (GPT 0.37 vs Gemini 0.05) | Product quality; chatbot post-hoc tracking |
| **FLOPs (≈6ND)** | train-step ≈ 6·N·tokens (fwd 2N, bwd 4N); block fwd/token = 24d²+4sd | Compute need / training cost |
| **MFU** | Achieved FLOPs/s ÷ peak FLOPs/s (GPT-2×H100 ~10.3%) | Real GPU utilization / software-stack headroom |
| **VRAM (16 B/param)** | Mixed-precision + Adam = 16 bytes/param; activation ∝ s² | Memory bottleneck; long-context HBM need |
| **Scaling Law L(N,D)** | L∞ + A·N^−α + B·D^−β; D≈20–30·N, C≈6–9·N·D | Pre-training ceiling; "how many 10× left" |
| **pass@1 / hallucination** | First-try accuracy; error rate (models 15–39%) | Model quality (prefer fresh evals over leaked MMLU) |
| **Quarterly P&L margins** | gross margin & net margin per quarter (e.g. GM ~78%, NM ~57%); segment QoQ/YoY | Quarterly granularity beats FY aggregates; the depth gate |
| **Ecosystem-moat counts** | developer count / GitHub contributors / app count / downloads vs challenger % | Quantify the moat (CUDA 4M/32.6K/3K/40M vs ROCm ~5%); never assert it numberless |
| **Per-employee market cap** | mktcap ÷ employees, vs peer employee counts | Signature house stat (e.g. ~$100M/employee; subject vs AMD/Intel headcount) |
| **Historical drawdown sequence** | the FULL ordered list of peak-to-trough %s | Cyclicality fingerprint — cite ALL of them, not the first few |
| **Hardware spec table** | TFLOPS / HBM / bandwidth / price per chip; inference-node comparison; generational interconnect (NVLink GB/s, GPU-count) | Required exhibit for hardware reports (H100/A100/4090; vs Groq; Huang's-Law 1000x/decade) |
| **Founder voting power / insider %** | founder voting %, insider stake vs peers, top external holders % | Founder-as-alpha + governance flag (score it, don't skip it) |

### Consumer

| Metric | Formula / definition | What it signals |
|---|---|---|
| **GMV (退货前/退货后)** | Gross merch value, pre- and post-refund (~40% return assumption) | Live-commerce North Star; sizing & valuation |
| **Take rate = 广告 + 佣金** | Platform rev ÷ GMV, split ad vs commission (抖音 11%=9+2; 视频号 ~5%) | The core thesis: live-commerce *is* advertising (ad-take dominates) |
| **Ad Load** | Share of feed that is ads (抖音 ~10% ceiling; 视频号 ~2.8%) | Remaining monetization headroom |
| **ARPU = 客单价 × 月复购频次** | Per-buyer spend | Buyer-side GMV bridge |
| **MAC & MAC/DAU** | Monthly buyers = MAU × e-comm penetration | Buyer-base growth driver (视频号 ~8–10% vs 抖音 69%) |
| **GPM** | GMV per 1,000 livestream views | Monetization-per-view efficiency |
| **NEV penetration** | NEV sales ÷ total auto sales, by region/time | EV adoption timing (China >50%, global >30% targets) |
| **单车 economics** | Per-unit gross profit / cost / ASP / capex+R&D | "Production-side competition = cost lead" (Tesla vs BYD) |
| **市占率 / Top-N concentration** | Brand/model share; Top-3/10/20 sum | 哑铃→纺锤 structural shift |
| **单车市值** | Quarter-end mktcap ÷ (quarterly deliveries × 4) | Delivery-normalized relative valuation |
| **Cash runway** | Ending cash ÷ quarterly burn (Rivian ~7–10 quarters) | Solvency for loss-makers. `fetch_edgar.py` cash + CFO |

### Funds, capital & macro

| Metric | Formula / definition | What it signals |
|---|---|---|
| **Penetration / S-curve** | Adoption ÷ addressable; killer-product crossing **1–5% (esp. >5%)** | Dates the revolution & best entry (爆发→狂热) |
| **IRR (net)** | Money-weighted annual return; ARK n-yr = (end/begin)^(1/n) − 1 | Vintage benchmarking; fading-VC-Beta thesis |
| **TVPI / DPI / MOIC** | Total value ÷ paid-in; cash distributed ÷ paid-in; exit ÷ invested | Paper vs realized return; power-law (6% of deals → 60% of returns) |
| **P/MAU** | Valuation ÷ MAU | Network-platform comp valuation |
| **Producer:consumer ratio** | Value-producers ÷ consumers (~1:1 network, 1:20–50 scale, 1:50–100 two-sided) | Monopoly depth / effect type |
| **Network value** | n² (Metcalfe) vs k·n (scale) vs log n (two-sided); Euler paths = n(n−1) | Marginal-user value ranking |
| **FCF Yield** | FCF ÷ market cap (screen ≥4%; buy ≥5%) | Cash-cow entry trigger. **`analyze.py owner-yield`** |
| **Backlog/rev & Book-to-Bill** | Backlog ÷ annual rev (≥2); orders ÷ rev (>1) | Order security (defense cash-cows) |
| **Dividend payout & CAGR** | Dividends ÷ NI (40–60%); DPS growth (>8%) | Management cash-return willingness |
| **Forward P/E** | Price ÷ NTM EPS (buy ≤18, trim >22) | Valuation timing |
| **TAM = Σ (pool × capture-prob)** | Segment market × penetration/capture each, sum | Probability-weighted opportunity sizing |
| **Mgmt fee & carry** | 2/20 vs a16z 3/30; direct ~1.5% vs fund 2% | LP direct-investing cost edge (~60% more over 10yr) |
| **Return dispersion (值域)** | Q1 − Q3 spread (VC 43.2 vs bonds 0.5) | Wider spread ⇒ active mgmt more valuable |

---

## Part 2 — Analysis methods (the moves that turn data into theses)

### 2.1 Penetration / S-curve adoption analysis
**Do this:** plot the killer-product's penetration over time against the **1–5% / >5%** thresholds. Below 1% = too early; crossing 1–5% = 爆发期; >5% = 狂热期 (the *best entry*). For crypto use addresses÷population; for EV use NEV÷total sales; for products use MAU÷addressable.
**Signals:** the *timing* of a technology cycle and the optimal entry window. DecadeX dates "crypto ≈ 1995 internet" this way.
**Tool:** none required (ratio). Pull addresses via `fetch_crypto.py`; auto sales from CPCA.

### 2.2 Production-cost-curve analysis (Wright's Law)
**Do this:** fit cost vs cumulative output, `Y = a·X^b` (cost falls a fixed % per doubling). A sharp input-cost collapse (cotton, steel, batteries, **tokens**) + penetration >5% is the **revolution-onset signal**.
**Signals:** when a tech moves to free distribution + ad monetization (ARK's "cost decline → market expansion" thesis).

### 2.3 North-Star revenue-bridge decomposition
**Do this:** break revenue into independently trackable drivers. Ad platform: `收入 = 库存 × 加载率 × CPM × CTR`. Search ad: `MAU × 单用户查询量 × 填充率 × CTR × 展示价格`. Live commerce: see GMV driver tree (2.7). Coinbase: `核心收入 = MTU × ARPU`.
**Signals:** *where* growth comes from — traffic-driven vs monetization-driven. This is the spine of every DecadeX teardown.

### 2.3b Per-product / per-SKU bottom-up revenue build (the big-tech AI signature)
**Do this:** the house's AI-revenue depth comes from decomposing AI into EACH surface SEPARATELY, never a single blended top-line. Build one row per product, across **Upside / Base / Downside**:
`收入 = 用户数基数 × 用户数CAGR(到目标年) × 年度渗透率ladder × 单价`.
Worked structure (reproduce this shape for any big-tech AI name):
- **Seat-priced Copilot SKUs:** for each (e.g. M365 Copilot $/yr, GitHub Copilot $/yr, Windows Copilot $/yr): installed/seat base → base growth → a *penetration ladder* (e.g. 5%→15%→15%→25%→25% across years) → ARPU → revenue.
- **Token / API lines:** see 2.3c (token-economics).
- **Sum** the per-product lines, layer them ON TOP of the segment-built traditional-business forecast (2.9b), then value the total.
**Signals:** *where exactly* AI revenue comes from, and which SKU's penetration assumption the thesis hinges on. A single "$30 ARPU anchor" or "4亿 seats" hand-wave is the laggard failure mode.
**Tool:** none (spreadsheet-style); pull seat/installed bases from filings (`fetch_edgar.py`) + the per-product penetration anchors in `data-sources.md`.

### 2.3c Token / inference-economics model (Azure / cloud-AI / any token-metered line)
**Do this:** the quantitative spine of any cloud-AI or token-metered valuation:
`年推理收入 = 年推理token量 × (推理成本或价格 / 1k tokens)`, with two dynamics the house always models:
- **推理需求增长率** ramping (e.g. 50% / 100% / 150% across scenarios) → token量 compounding (e.g. 2,555 → 99,804 万亿 tokens).
- **推理成本每 N 年减半** decay (e.g. $0.002 → $0.0005 / 1k tokens) — cost/price falls geometrically.
Anchor with a vendor cost data-point (e.g. "ChatGPT ~$700K/day inference, ~7万亿 tokens/day, ~$0.0001/1k") to calibrate the base.
**Signals:** Azure-AI / OpenAI-line economics; whether unit cost decay outruns or undershoots demand growth. Posing the unit-economics *question* without this quantified model is a documented miss.
**Tool:** none required (compound the series by hand); feed the implied revenue into 2.8/2.9.

### 2.3d Demand-sizing table — units × $, ALL THREE cases (hardware / commodity / capex-driven)
**Do this:** size end-demand bottom-up as a full 3-case (optimistic / neutral / **pessimistic**) table — never a single capex aggregate, and never drop the pessimistic leg.
- **Top-down-to-bottom-up bridge:** `total demand = trailing cloud-customer GPU purchases ÷ cloud penetration`; `cloud purchase = vendor shipments × attach-rate (e.g. 40–50%)`. Build a buyer table (top-10 buyers × units) with the buyer-split %.
- **Per-case cells:** training-unit count, training:inference ratio, inference-unit count (in a common unit, e.g. A100-equiv), and the **$ figure for each case** (e.g. opt/neu/pess: 6190/4643/3095K training-units, 7/6/3× ratio, 43330/27858/12380K inference-units, $6500/4179/1857亿). Use purchase-cycle multipliers (e.g. 2.0/1.5/1.0×) and a base installed unit count + penetration as the engine.
**Signals:** the real, falsifiable size of the opportunity — and the bear case the headline must survive.
**Tool:** none (table); pull capex from `fetch_edgar.py`, shipments from vendor filings.

### 2.4 Unit economics
**Do this:** compute per-unit profitability: TAC low-buy/high-monetize ($25 in vs $65 out), $/search, ARPMAU vs $/MAU-serve, 单车毛利/成本/ASP, headcount efficiency (rev ÷ team; Hyperliquid ~$100M/person). Pull revenue/CFO/CapEx via `fetch_edgar.py`.
**Signals:** business quality and whether scale actually pays.

### 2.5 Take-rate decomposition (live commerce / platforms)
**Do this:** split take-rate into **ad + commission**; attribute the ad premium to traffic mix (推荐 vs 社交), Ad Load, and buyer purchasing power. 抖音 11% = 广告9 + 佣金2; 视频号 ~5%.
**Signals:** the DecadeX live-commerce thesis — "it's immersive *advertising*, not discount retail." When ad-take dominates, monetization quality is higher.

### 2.6 Reverse-DCF (反向 DCF) — sanity-check the price
**Do this:** instead of "given growth, what's it worth?", ask "given the price, what growth is the market assuming?" Feed market cap, trailing FCF, discount rate, terminal growth → get implied FCF growth. Judge it against the asset's history and TAM.
**Signals:** whether the embedded expectation is sane or pure narrative (a 33× P/FCF name implying ~14%/yr for 10yr).
**Tool — `analyze.py reverse-dcf`:**
```
python3 tools/analyze.py reverse-dcf --mktcap 3e12 --fcf 9e10 --discount 0.10 --tgrowth 0.03 --years 10
# → implied_fcf_growth ≈ 0.1403 (14.03%/yr), implied P/FCF = 33.33x
```
Get `--mktcap` from price × shares and `--fcf` from `fetch_edgar.py` (CFO − CapEx).

### 2.7 GMV driver-tree (two-method cross-check)
**Do this:** model live-commerce GMV two independent ways and reconcile:
- **Watch-side:** `GMV = PV × GPM`, where `PV = DAU × 日均时长 × 单位时间观看视频数 × 直播间加载率`.
- **Buyer-side:** `GMV = MAC × ARPU`, where `MAC = MAU × 电商渗透率`, `ARPU = 客单价 × 月复购频次`.
**Signals:** a cross-checked GMV base for the valuation; divergence flags a bad assumption.

### 2.8 Three-scenario probability-weighted valuation (signature output)
**Do this:** build **Bear / Base / Bull**, each: driver metric → revenue → PS or PE multiple → discount (e.g. 监管折价 −10% to −25%) → assign probabilities → weight to an **expectation**. Use **PE-style** when ~all revenue buys back the token / near-100% margin; otherwise **PS**. Give a *band*, not a point. Anchor scenarios to historical cyclical years (e.g. Binance 22/24/25).
**Signals:** the DecadeX deliverable valuation.
**Tool — `analyze.py scenarios`:**
```
python3 tools/analyze.py scenarios --json '[{"label":"Bear","prob":0.5,"value":120},{"label":"Base","prob":0.3,"value":250},{"label":"Bull","prob":0.2,"value":480}]' --price 200
# → expected_value, per-scenario weighted contribution + upside%, best/worst case
```
Probabilities must sum to 1.0 (the tool errors otherwise — a deliberate guardrail). Omit `--json` to run the built-in Bear/Base/Bull demo.

### 2.9 Comparables (comps)
**Do this:** build the apples-to-apples table anchored to a benchmark — everything as "% of Binance"; P/MAU across social platforms; fund IRR/TVPI/DPI vs peer quartiles & S&P 500; ARK ETF vs sector index; auto comps (PE/PS/margin/单车市值). This is the report's backbone (Step 4).
**Signals:** relative cheapness/richness and competitive standing.

### 2.9b Segment revenue + margin forecast table (build BEFORE valuing)
**Do this:** project EACH reporting segment separately (one CAGR per segment, e.g. PBP 16% / Intelligent Cloud 20% / MPC 7% base), across the forecast years, in Upside / Base / Downside — NOT a single company-wide top-line CAGR. Add a margin/quarterly print (e.g. gross margin ~78%, net margin ~57%) to ground it. Then layer the per-product AI build (2.3b/2.3c) on top, and tie the SOTP/PS to the *forecasted segment operating income*, not an abstract multiple. For a hardware name, the segment forecast becomes the input to the demand table (2.3d).
**Signals:** structural granularity (the human's depth) and a valuation tethered to real forecasted income rather than a method demonstration.
**Tool:** `fetch_edgar.py` for segment history (where disclosed); compound by segment.

### 2.9c Moat quantification (force a NUMBER on the moat, never just name it)
**Do this:** a named moat with zero numbers is the single hardest depth gap to close. For each moat, pull the **head-to-head metric vs the open/challenger alternative**:
- **Ecosystem / dev moat (CUDA-type):** developer count, GitHub contributors, app count, download count — vs the challenger as a % (e.g. 4M devs / 32.6K contributors / 3K apps / 40M downloads vs the open-source challenger at ~5% of each). Use Electric Capital / GitHub real counts; do NOT fabricate a ratio.
- **Compliance moat:** named license map by jurisdiction (US MSB+MTL, HK VASP, EU MiCA, SG DPT…), license cost ($ to assemble the full set), compliance cost as % of headcount, and concrete listing requirements (e.g. "asset must run ≥12 months").
- **Scale/liquidity moat:** the subject's share of the benchmark (e.g. spot volume as % of Binance), monthly head-to-head volume table.
**Signals:** converts "X has a moat" from assertion to evidence — the house's hardest quantitative layer.
**Tool:** none; sources in `data-sources.md` (Electric Capital, GitHub, regulator sites, filings).

### 2.9d Founder / governance / ownership as scored alpha (not a footnote)
**Do this:** when the founder or org design is a core alpha driver, score it with FIGURES: founder voting power %, ownership/control structure (dual-class, voting-rights代持), insider stake % vs peers, top external holders (Vanguard/BlackRock %), org structure (flat N-layer, EIR program, "role over responsibility" model), and management stake vs peers (e.g. MARA 0.58% vs CLSK 3.46%). For funds, the partnership-vs-corporate succession taxonomy + per-partner deal-share % (审美趋同 quantified). Low insider ownership = governance flag; high founder control = a deliberate alpha factor — decide which the report treats it as.
**Signals:** founder-as-alpha and governance risk, made into scored due-diligence items rather than skipped.

### 2.10 Sum-of-parts (SOTP) / un-monetized-traffic identification
**Do this:** value each segment separately (Meta: FB/IG/Reels/WhatsApp; Hyperliquid: chain-business vs SOL PE + exchange-business vs Coinbase PE), then sum. Flag un-monetized reservoirs (Reels ≈ $30B un-monetized traffic).
**Signals:** hidden value the blended multiple misses.

### 2.11 Sensitivity / scenario-matrix analysis
**Do this:** flex the load-bearing assumptions in a grid (BTC CAGR × WACC → Coinbase mktcap; take-rate ramp × MAC/DAU ramp × frequency × AOV × DAU growth → GMV). Run `analyze.py scenarios` repeatedly across the grid; or `reverse-dcf` at different discount rates.
**Signals:** which assumption the conclusion actually hinges on.

### 2.12 Correlation / regression analysis
**Do this:** compute R²/correlation between series (MAU↔revenue R²=0.961, reverse-regression Revenue = 113.9×MAU − 322.47; Stable↔Top4 0.7–0.85; ETH yield↔fee 0.4–0.5; user-activity↔price 83%).
**Signals:** quantified coupling/decoupling — e.g. ETH shifting from monetary premium to fee-driven pricing.

### 2.12b DuPont time-series (15-20yr, not a point estimate)
**Do this:** for any leverage-driven-ROE or balance-sheet-repair story (conglomerates, cash-cows, financials), decompose ROE = net-margin × asset-turnover × equity-multiplier and chart **each factor over 15-20 years**, not as one static print. The story is in the trajectory (e.g. equity-multiplier 6.85 → 2.17 as the balance sheet repairs; payout ratio 67% → 236% → … → 23% across the cycle). Pair with the cash-cow series: Capex/CFO (e.g. ~90% → 20-30%) and (分红+回购)/EBITDA annual values.
**Signals:** shows the leverage/repair/capex-turn story rather than asserting it; identifies the regime-change year.
**Tool:** `fetch_edgar.py` for the multi-year inputs; compute the three factors per year.

### 2.13 Owner-earnings / FCF-yield cash-cow screen
**Do this:** sequential gates for cash-cow equities — Backlog/rev ≥2 & Book-to-Bill >1 (orders locked) → **FCF Yield ≥4%** & FCF/rev >6% (cash convertible) → EAC not over-running → payout 40–60% & dividend CAGR >8% → only then valuation (Forward P/E, FCF-yield buy/sell triggers).
**Tool — `analyze.py owner-yield`:**
```
python3 tools/analyze.py owner-yield --oe 9e10 --mktcap 3e12
# → owner_earnings_yield = 3.00%, P/OE = 33.33x; flags below the >=4% screen
```
Compute `--oe` from `fetch_edgar.py` (CFO − CapEx); `--mktcap` from price × shares.

### 2.14 Cohort / vintage-year analysis
**Do this:** align series by *start date* — products by launch year (FB/IG vs YouTube/TikTok growth-decay), funds by vintage vs industry-IRR peak years (semis 1965–70, IT 1983–89, PC SW 1995–99, mobile/SaaS 2008–13), GMV by age cohort (都市银发 etc.).
**Signals:** separates timing-Beta from skill-alpha; finds "the next FB."

### 2.15 Value-creation vs value-capture decomposition
**Do this:** always score *creating value* and *capturing value* separately. REV/GDP 税权; L1's share of rollup value pre/post EIP-4844 (77%→8%); "Ethereum ≠ ETH."
**Signals:** a thing can create huge value while the token/equity captures little.

### 2.16 Wash-trading / airdrop detection
**Do this:** use OI/Vol, Vol/Tx amplitude, Vol/TVL, and multi-address-per-user patterns to separate organic from incentive-driven volume (Hype OI/Vol 1.12 vs Aster 0.32 = more organic).
**Signals:** whether reported volume is real demand or 刷量.

### 2.17 Bear-market stress test ("立住")
**Do this:** check whether **non-subsidized TVL + DAU** survive a deep bear and whether coin-denominated value holds (TVL drawdown −50% / −85% / stable). Pull current TVL via `fetch_crypto.py` and compare to prior-bear lows.
**Signals:** real, durable demand vs subsidy-propped activity.

### 2.18 "Price of money" / rate-regime overlay
**Do this:** chart the risk-free rate (14% 1981 → ~0 → ~5% 2025) against VC fundraising, IRR, and growth-asset multiples. Pull the live Treasury curve and FRED history.
**Signals:** the macro discount-rate backdrop that re-rates every growth asset.
**Tool — `fetch_macro.py`:**
```
python3 tools/fetch_macro.py treasury            # live avg rates across the curve (no key)
python3 tools/fetch_macro.py fred DGS10 --limit 12   # 10y history (needs FRED_API_KEY)
```

### 2.19 Leverage-proxy price grid (BTC miners / any equity that is a levered bet on an underlying)
**Do this:** for a leverage proxy (miner on BTC, MSTR on BTC), the deliverable is a **scenario GRID mapping underlying price → leverage k → equity DOLLAR price**, not just "2-3x". Steps:
1. **Anchor the cycle start** explicitly: date, underlying price, equity price (e.g. cycle start 2022-11-21, BTC $15,776, MARA $6.19) so the regression is calibratable.
2. Regress equity %Δ on underlying %Δ *separately for bull and bear*; report slope k per peer (e.g. MARA bull 6x→1.5x, CLSK 3x, MSTR 0.6x, bear ~1x).
3. Build the grid: underlying $70K/$100K/$150K × k → equity price (e.g. bull MARA $38.1/$55.8/$85.2; bear $16.3/$20.9/$28.4 at BTC $30K/$37.5K/$50K).
**Signals:** the bullish-with-a-number call; a falsifiable price target grid, not a vague multiple.

### 2.20 Bottom-up token/asset valuation worksheet (crypto L1/L2)
**Do this:** build the full per-cell worksheet, computed SEPARATELY for ETH-only and ETH+L2 (or asset-only vs asset+ecosystem):
`单次交易收入 × 交易次数 × 下降/上升倍数 → 未来收入 → × PS → 市值 → ÷ 供应量 → 价格`, in bear/base/bull.
Reproduce every cell (per-tx revenue $6/$11/$22; decline multiples 50/60/80%; future tx counts; future revenue; resulting price), plus the per-contributor sub-models (e.g. each L2's L1-paid revenue with its tx-count multiplier and per-tx L1 fee, and that L2's % of total contribution). DERIVE the end price — don't cite a round number that diverges from the derived figure.
**Signals:** the house's actual valuation table; the difference between "PS bands named" and "table built."

### 2.21 Survival ranking / distance-to-bankruptcy (commodity/infra peer screen)
**Do this:** for capex-heavy / commodity peers, RANK the peer set by runway, not just flag it as future work. Rank by D/E + marginal cash cost vs spot + on-balance-sheet asset (e.g. BTC) vs debt coverage → an explicit "distance to bankruptcy" date per company (e.g. 2024.4 … 2056.1). Include the named blow-up as the survival benchmark (contrast its D/E trajectory with the subject's).
**Signals:** who survives the bear — a required deliverable for miner/commodity reports, not a TODO.

### 2.22 Bottom-up cost / unit-economics reconstruction (don't cite cost — RECONSTRUCT it)
**Do this:** for production/mining/hardware, rebuild the cost from physics, don't quote a number:
`network hashrate + block reward + machine specs (TH/s, W, J/TH, retail price, lifespan) → EH-per-unit → CapEx + OpEx → $/unit`. (e.g. network 375 EH/s, S19 XP 140 TH/s / 3031W / 22 J/TH / $4600 / 2.5yr → ~$26,500/BTC: ~$14,300 CapEx + ~$12,200 OpEx.) Likewise the hardware BOM ($200 die + $1500 HBM + $700 CoWoS + $500 other ≈ $3000 cost vs $35000 price). Then rank peers by reconstructed cost (e.g. CoinShares: CLSK $26,927 … RIOT $65,371) and show how many are above breakeven.
**Signals:** engineering-grounded cost, the input to survival ranking (2.21) and the demand table (2.3d).

---

## Part 3 — A worked DecadeX mini-pipeline

A typical numbers-first pass, end to end:

1. **Acquire** (see `data-sources.md`): `fetch_edgar.py COIN --metric RevenueFromContractWithCustomerExcludingAssessedTax`; `fetch_edgar.py COIN --metric NetCashProvidedByUsedInOperatingActivities`; `fetch_crypto.py tvl ethereum`; `fetch_macro.py treasury`. Pull the FULL multi-year / quarterly series, not a single print (Part 0 rule 1).
2. **Build the segment forecast table** (2.9b) + **per-product / token bottom-up** (2.3b/2.3c) or the **demand-sizing table** (2.3d) — every cell, all three cases including pessimistic.
3. **Decompose** the North-Star bridge (2.3) and **unit economics** (2.4 / reconstruct cost 2.22) — locate where growth comes from.
4. **Quantify the moat** (2.9c) and **score founder/governance** (2.9d) — numbers, not names.
5. **Price-of-money overlay** (2.18) to set the discount rate; **reverse-DCF** (2.6) sanity-check.
6. **Three-scenario valuation** (2.8) — land CONCRETE point valuations (SOTP $X.XXT, bull/bear $) and, for leverage proxies, the **price grid** (2.19); for crypto, the **bottom-up worksheet** (2.20). Derive the headline, don't assert it.
7. **Comps + SOTP** (2.9, 2.10), **DuPont time-series** (2.12b), **survival ranking** (2.21) → cross-check and rank peers.
8. **Stress test + value-capture** (2.17, 2.15) → durability and who captures it.
9. **Conclude**: conditional, falsifiable, banded — and TAG every number 事实/推断/illustrative (Part 0 rule 5). Never a point target as advice.

> Every number above is a *method demonstration*, not a recommendation. Reproduce the process; the conclusions stay conditional and falsifiable.
