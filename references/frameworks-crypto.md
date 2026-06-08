# DecadeX Crypto Frameworks

*Named frameworks, house views, and key conclusions from DecadeX's crypto reports (public chains, exchanges, stablecoins, DeFi, L2, PerpDex). Apply with numbers. Educational.*

---

## A. Foundational lens (apply first)

- **Crypto = upgrade & fusion of TradFi, NOT Web3.** Crypto points to **assets**; Web3 points to **traffic/流量**. Analyze with a finance lens, not an internet lens. Crypto is at the internet's **~1995-1998 moment** (low penetration, cyclically oscillating up).
- **资产渗透率 (asset penetration) is the North Star, not user penetration.** Crypto penetration = on-chain asset value / total global asset value (vs Web's user/population). Low penetration ⇒ long runway ("≥10x room"). Per-country crypto ownership: US 15.5%, Vietnam 21%, India 6.5%, China 0.35%; BTC+ETH only ~3% of global spot volume.
- **资产先于用户 (assets precede users).** Today's binding constraint is *new assets*, not users. Growth funnel: **搏流量靠资产 → 保留存靠叙事 → 真用户靠应用** (acquire via star assets, retain via narrative, convert to real users via apps).
- **Crypto is cyclical (穿越牛熊).** Don't extrapolate linearly — model "the next cycle." Validity test = **bear-market stress test**: does non-subsidized TVL + DAU survive the bear? (ETH TVL -50%, SOL -85%, Tron stable.)
- **第一性原理 = 点对点公开透明全球公共账本 (a peer-to-peer, transparent, global public ledger).** Signature accounting-ledger narrative: **三次记账范式变革 (单式 → 复式 → 分布式记账)** and **四次资本范式 (财团 → 华尔街 → 硅谷 → 加密).** Two 胜负手 of Crypto = **资产流量 + 合规** (合规三层: 牌照层 / 商业模式层 / 基因层).
- **三大资产属性: 流动性 / 安全性 / 效率** (效率是敲门砖, 安全性是刚需). **五个创新原则/趋势:** 从边缘到核心 / 从原生到孪生 / 从本性到显性 / 从第一性原理出发 / 寻找 Mass Adoption 神器. These are signature DecadeX scaffolds for any crypto deep-dive.

---

## B. 不可能三角 (Blockchain Trilemma) — and DecadeX's re-ordering

**Classic:** 去中心化 / 安全性 / 可扩展性 — optimize at most two. DecadeX adds:

- **Measurement methods.** 去中心化 = 思想去中心 (open/permissionless/global) + 结构去中心 (node distribution, governance). 安全 = Nakamoto Coefficient, Finality Time, TVL, track record. **可扩展性 ≝ Scalability = TPS / Cost-to-validate-all-txs.**
- **The choice is SCENARIO-DEPENDENT.** Meme users want efficiency on a *safety floor* (decentralization optional); RWA/2B users want safety on an *efficiency floor*. ⇒ "the main contradiction now is **资产发行效率 (asset-issuance efficiency)**, not decentralization."
- **Re-ordering (Ethereum-evolution view):** drop the symmetric trade-off; impose a *priority* — **去中心化是目的 (purpose) >> 可扩展性是加分项 >> 安全是可退让的底线**. Re-derive value from a *user-experience* angle (decentralization = global/permissionless; security = assets-not-lost/always-available).
- **3-system matrix:** 支付宝 = 安全+可扩展 (sacrifices decentralization); BTC = 去中心化+安全; ETH = 去中心化+可扩展 (smart contracts add risk, lower security).
- **CAP origin:** trilemma derives from CAP (partition P is given on a blockchain ⇒ choose C vs A). Single-chain can only *improve*, not solve ⇒ **multi-chain is inevitable** and **scaling is the main contradiction**.

---

## C. 协议层 vs 应用层 (Protocol-layer vs Application-layer split) — DecadeX 独创

Split the public-chain track into two layers, each judged by **differently-weighted metrics**:

- **协议层 weights:** TVL > Volume > Core Dev > MAU.
- **应用层 weights:** Volume > TVL > MAU > Core Dev.
- **Verdict:** **协议层大局已定** (ETH-dominated oligopoly; moat = two-sided effects + 0-to-1 PoS consensus difficulty); **应用层未成定数** (new chains can still erupt with differentiated scenarios).
- **Endgame split:** 协议层公链 (key = TVL) vs 应用层公链 (key = scenario + differentiation).

## D. 清算行 / 经纪撮合层 + 收单/执行/清结算分层 (settlement-stack)

- **L1 tiering:** 第一梯队 L1 = bank/clearing layer (issues compliant stablecoins, holds RWA collateral, final settlement, earns seigniorage/float — "on-chain commercial bank", e.g. ETH, rising SOL). 第二梯队 L1/L2 = broker/matching layer (fast cheap matching, pulls liquidity via bridges/subsidies, earns matching fees/MEV — "lacks 沉淀性收入", e.g. Arbitrum/Base). Tier-2 moat (TPS, low Gas) is copyable; liquidity flows back to head chains when subsidies stop.
- **TradFi role decomposition (for exchanges):** 收单 (brokers, 2C, KYC, 30-40% profit) / 执行 (exchanges, 2B, matching, 40-50%) / 清结算 (NSCC/FICC/DTC — public-good infra, low/no profit). **In Crypto the public chain commercializes the clearing-settlement layer that TradFi keeps as a public good ⇒ Crypto is inherently a revolution against TradFi**, and efficiency-RWA is a 伪命题 (forces running two settlement systems). Custody/clearing licenses are the highest-value (托管/清结算牌照含金量最高).

## E. 链上GDP / REV / 税权 (on-chain GDP, REV, tax-power)

- **链上GDP** = total fees end-users pay to DApps (excl. L1 Gas; incl. LP fees even at 0% commission like Uniswap).
- **REV (Real Economic Value)** = total Gas + MEV (MEV via Jito-Flashbot fees).
- **REV/GDP = the L1 token's ability to CAPTURE DApp-layer value = its 税权 (tax power).** **SOL ~65% vs ETH low** ⇒ "SOL的税权远高于ETH". ETH's strategy = deliberately *low* tax to pull in assets/devs first, monetize later (early-internet playbook).

## F. 价值创造 vs 价值捕获 (Ethereum ≠ ETH)

Investment value = ability to **CREATE** value + ability to **CAPTURE** value; divergence = strong creation, weak capture.

- **The textbook case:** post-modularization the ETH ecosystem (L1+L2) grew ~10x MAU/volume (created value), but the *token* lost capture — L1 fees down ~95% (~$30M→~$0.5M at Dencun), burn ~100 ETH/day, inflation +0.79%. **"ETH's problem is now DEMAND, not supply."**
- **L1代币 = 数字主权的原生货币:** model a chain as a digital nation (DApps=economy, validators=judiciary/military, token=tax medium). ETH lacks sovereign-money *compulsion* (you can trade USD-denominated, using the chain is optional) ⇒ can't capture full value.

## G. L1 × L2 — period-lock the thesis (complementary vs competitive)

**The polarity is DATE-dependent — reconstruct the period thesis, do not impose a later inversion.**

- **2024 L2-ecosystem thesis = COMPLEMENTARY (协议层 × 应用层 互补).** L2 helps the EVM ecosystem capture more users/assets *with ETH as the core currency*; L1 provides security, L2 provides TPS-dependent consumer apps. Capture the *bull case for ETH-as-protocol-layer first*; flag tax-capture risk only as a *secondary caveat*, not the headline. (House view at the time: "本应互补", though L1/L2 currently somewhat 相互束缚 — L2 分散社区, L1 限制L2 生态.) **理想分工: L1 = 安全 + 不依赖TPS的金融应用; L2 = 依赖TPS的消费者应用.**
- **Signature metaphors (required vocabulary):** **L2 = 以太坊的外接硬盘 (external hard drive)**; **L2 商业模式本质是云计算 (cloud computing — selling cheaper compute/storage)**; **L2 像应用发行商 (application publisher)**; **Killer Apps 未来会倾向于自建应用链 (super-apps build their own app-chains).**
- **Empirical anchor the human leaned on:** by 2024 L2 had surpassed ETH in tx-count and was near-parity on active addresses, **BUT 资产流量/TVL 并未明显从 L1 迁移** (asset/TVL flow did NOT migrate from L1 to L2). Use this asymmetry to argue **value (assets) stays on L1 while activity moves to L2.**
- **Four-factor L2 evaluation (ordered): 生态 > 市场运营策略 > 资本与团队 > 技术** (importance递减); three core L2 metrics = **用户规模/活跃度, TVL, 项目生态.** Continuous-observation angles: 跨链交互能力 / 独特品牌 / 性能能否超高性能L1 / 是否长出DeFi之外的应用.
- **Head-to-head Arbitrum vs Optimism (required module):** score 生态开放性 (OP Stack B2B2C vs Arb B2C), 团队正统性/资本 (EF roots, Paradigm/a16z), 技术进度, 中心化风险 — with a clear verdict (house: **OP > Arbitrum**).
- **Op-Rollup vs ZK-Rollup verdict (with reasoning):** Op remains mainstream for the next ~12 months; ZK held back by **Cairo / 电路语言门槛, 流动性差, V神个人意志 vs 社区支持, 生成证明慢.** Don't dismiss ZK in one line.
- **Bottom-up ETH revenue build (match the human's structure):** **ETH revenue = L1 gas 收入 + L2 上交的数据存储费**; build per-transaction: 单次交易收入 × 交易次数 × 下降/上升倍数. Then PS bands (e.g. 熊市 120-150 / 牛市 40-50). Price band for the next-cycle high: **~$6000-8000.**

### G2. 主网牺牲税收的营销 (later/competitive-frame view — use only when the period supports it)

- For *later* (≈2025, post-modularization) reports, the reframe flips: the mainnet trades ETH's capital-asset tax power for broader use-cases (a *marketing expense*); test if it's a Nash equilibrium — it isn't.
- **Post-EIP-4844 numbers:** cost/tx dropped 95-99.99% (Arbitrum -98%, Base -99.99%, Starknet -96%); ETH's capture of OP-Rollup value fell **77% → 8%**; L2 tax now **<2% of mainnet revenue**. Base captured 95% of ~$100M user fees, paid only ~$5M to mainnet (10x adoption).
- **Verdict (later view):** in 1-3 years L1 & L2 are **COMPETITORS**, not complements; **扩L1 = 抢L2的生意**. The next app innovation likely happens on *neither* ETH nor today's fragmented L2s (伪跨链 — only assets cross; no performance edge; no native-token stickiness flywheel). **Do not back-port this 8%/competitive frame onto a 2024 complementary-era report.**

## H. 外部性指标: Stable/Total Mcap (risk barometer)

Treat **stablecoin market cap (+ ETF net inflows) as the EXTERNAL demand that prices the whole market.** **Stable/Total Mcap = risk-pricing barometer; lower ratio = bigger bubble.** Bear 10-20%, bull 5-10%. Correlation Stable Mcap vs Top-4 chain mcap = 0.7-0.85 ("significantly correlated"). Stablecoin total mcap is the key 抓手 for the bullish 3-5yr sector view.

## I. PS / PE cyclical valuation (L1 tokens)

- **PS = market cap / on-chain fees.** Bear ⇒ activity collapses ⇒ PS spikes but price is *under*valued; bull ⇒ PS reverts to a band.
- **Bands:** ETH bull 100-200x (historic 40-100x). SOL 2021 bull 300-800x (tiny denominator); 2024Q4-25Q1 30-150x (fees grew 3-5x ⇒ more cash-flow-driven); future bull compresses to tens of x.
- **Yield-vs-fee correlation:** ETH 0.4-0.5 (shifting to fee-based pricing); SOL 0.15 (still narrative/macro driven).

---

## J. Exchanges — frameworks

> **Polarity is DATE-dependent (period-lock first).** The **2024 "Coinbase不仅仅是交易所" view is BULLISH on the compliance moat** (合规护城河权重 ~50%; "2024是合规元年"; "合规价值终于凸显但市场仍然低估了Coinbase"; two growth engines = 行业Beta + **地区事实性垄断**). It is a **SuperApp / undervalued** call (≥5x, ~$100B bull target) — *not* a contrarian-bearish "护城河融化" thesis. Only the *later 2025 deregulation view* erodes the moat (three bills remove the regulatory-ambiguity barrier; ETF ~50% spot; fees → 0). **Do not invent a 2026 "moat is melting / compliance退化为β" inversion on a 2024 report.**

- **Two cores: 资产流量 + 合规.** Licenses = the *threshold/necessary condition*; the actual **胜负手 = new asset flow.** Compliance's essence = **吸纳传统金融机构的资产流量** (its new flow is more ToB than retail). Compliance importance is *rising* and *underestimated*.
- **合规牌照 → 地域事实性垄断 + 美国用户垄断 (牌照与用户双垄断) = the load-bearing moat.** For the 2024 bull case this is Coinbase's single most-emphasized advantage. The bull case = compliance value finally being recognized but the market still underpricing it. Do NOT invert it into "缺垄断 / 护城河融化."
- **合规势能递减序列: 交易所 (航空母舰) > 稳定币 (Killer App, 天花板更高) > RWA (孪生资产, 需时间).** The three compliance tracks = 交易所 / 稳定币 / **RWA** — include RWA, with the seniority/势能 ordering.
- **怎么做合规 = 运营 + 基因 + 商业模式 + 用户心智 (four dimensions, not just an ops problem).** Plus: **非合规 → 合规几乎不可能** (向左走做合规 vs 向右走做链上 — a bifurcation, can't convert); team-background insight (美国白人背景最有可能做成合规; 亚洲背景很难).
- **三分类 (by edge):** Binance & others = **规模 (scale)**; Coinbase = **合规 (compliance)**; Uniswap & Curve = **去中心化**. (Security is an exchange's necessary rigid demand 必要刚需.)
- **混业 → 分业经营.** A crypto exchange is bank+broker+exchange in one; separation (分业) is inevitable (US securities precedent: only 24 SEC-registered exchanges; ~3600 introducing brokers, ~100 self-clearing). 托管/清结算 spun off first. For Coinbase this is a long-term systemic (拆分) risk.
- **North Star (Coinbase) = 合规护城河 / MTU 市占率** (or, in the deregulated 2025 view, **入金用户数 + AUM**). Core revenue = **MTU × per-MTU ARPU**.
- **Exchange operating playbook (granular):** **现货 = 资产 (多/快/新/稳)**, acquired via 公链 / Launchpad / Venture three手段 (优质资产带10万+新用户); **合约 = 渠道 + 代理** (KOL, 首单返佣 70%, 类比直播). **国际站 (百慕大) 本质 = 存量用户变现, NOT 拉新海外用户** — key差异化 = 自主上币权 + 合约.
- **Banking-revenue sub-breakdown (data anchors) + cyclicality mechanism:** 散户 55% / 机构 4% of revenue (散户占交易量 94-95%); 稳定币 ~19% / 质押 ~10% / 托管 ~2% / 利息 ~5%. Banking业务 lowers cycle-correlation. Forward P&L build (not just PS bands): e.g. 24Q1 收入 >$15亿 (零售交易 >$10亿), bull-market peak 平均季度收入 ~$46亿, 市值看 >$1000亿; driver model = ETF ~90% 净流入在CB托管, USDC 利息分润 60% (80% 买国债), 零售费率 1.7% / 机构 0.03%.
- **价格升值 vs 价格中性收入 decomposition:** split transaction revenue into the part driven by BTC price-appreciation vs the price-neutral platform-intrinsic part. (2021: ~80% / ~6:1 BTC-driven ⇒ "Coinbase NOT yet decoupled from crypto行情".)
- **The valuation contradiction:** under a pure trading-fee model, **owning CB stock never beats holding BTC** (BTC CAGR 30% → CB ~20.7%; downside more cushioned). ⇒ must find *price-decorrelated, high-margin* revenue (Base/Super-App, USDC, derivatives).
- **流量 × 流动性 (2x2 quadrant):** value = traffic entrance × liquidity reservoir (a *multiplier*). Only CEX have **both**; Pump.fun/GMGN = traffic, no liquidity; Hyperliquid/Uniswap = liquidity, no traffic. 链=资产发行源头, 所=资产退出终点. "做一条链比做一个所更难."
- **流动性是果不是因 (liquidity is a result, not a cause):** efficiency (asset variety + fee) + security → volume → liquidity depth → more volume (a flywheel).
- **Endgame:** CEX consolidates to an oligopoly (3-5 exchanges hold 80%+), with geographic character; trillion-$ companies possible. CEX survives because KYC/AML must exist; **PerpDex becomes the back-end execution layer**.

## K. Stablecoins — frameworks

- **稳定币不可能三角:** can't have price-stability + decentralization + capital-efficiency together. Centralized cash-backed (USDC/USDT) = stable+efficient but centralized/most-regulated; over-collateralized (DAI) = stable+decentralized, low efficiency; algorithmic = decentralized+efficient, unstable.
- **稳定币 = gateway 业务 / Crypto's Killer App.** USDC = "the digital mapping of the traditional US dollar"; USD-stablecoin dominance is decided by the *dollar*, not the issuer.
- **Two scenarios:** trading (first large scenario, >90% of stablecoin volume on CEX, USDT-dominated) and **payment** (second, strong late-mover advantage — "如重力般不可阻挡" in countries with backward finance; compliant 1:1-reserve stablecoins win here).
- **货币层级:** stablecoin ≈ M0 (private/commercial-bank-issued, issuer commercial credit); CBDC ≈ M2 (central-bank liability). Stablecoins decoupling from exchanges: since 2021/12 CEX volume -64% while stablecoin volume only -11%.
- **Market space:** vs 35万亿 payment market / 130万亿 M2 vs ~$125B current ⇒ "~100x" runway; first track to be regulated.

## L. PerpDex / Hyperliquid — frameworks

- **Treat as a 链上交易所 (类 Binance/Coinbase), not a public chain.** Vertical integration (own L1 = 链-所闭环) lets it grab 议价权; chain-side execution captures 75-85%, settlement 15-25%.
- **双边平台: 需求侧是因, 供给侧是果.** Demand (retail traders) drives supply (MM); demand is the core 抓手. North Star = **独立访客数 + Vol**. Pro-MM's two demands: (1) Retail Volume, (2) platform infra performance.
- **Organic-vs-wash test (key DecadeX move):** **OI/Vol** (HL 1.12 = organic vs edgeX 0.17/Aster 0.32 = wash/airdrop); Vol/Tx振幅 (HL stable 9-20 vs peers 1100-9100); 日均Vol/TVL (HL 1/5–1/15 of peers = retail small-and-frequent). **Pearson correlation** of volume series proves "不是一波人" (CEX-CEX 0.92-0.97 vs CEX-HL 0.63-0.64 ⇒ HL brought *new* users). **Vampire-attack counterfactual:** no 一增一减 (vs Sushiswap-on-Uniswap) ⇒ Aster/Lighter surge is external increment, not 分流.
- **Valuation:** because **99% of revenue buys back HYPE + ~100% margin ⇒ use PE-style** (类美股交易所), not pure PS. Dual-track (historical PS band 30-50 vs comp PE vs Coinbase+SOL), apply 监管折价 (-25/-15/-10%, keyed to BNB/XRP enforcement drops), probability-weight 20/60/20. Forecast each line as **% of Binance** (合约 10/15/20%, 现货 1.5/2.25/3%, USDH vs FDUSD, gas vs SOL).
- **Biggest risk = regulation (达摩克利斯之剑):** 35-40% users from US/EU, no KYC/AML ⇒ red line; but "if fundamentals hold, the regulatory-landing moment may be the best entry."

---

## M. Asset-discovery & primary-market frameworks

- **资产生命周期 / 一横一纵:** vertical = 资产供给 (issuance), horizontal = 资产交易 (trading); lifecycle 资产发行 → 资产交易 → 资产沉淀. Sector arc: 爆发前夜→爆发期→转折期→协同期→成熟期; infra → 神器(Dex/Oracle/Lending) → 衍生应用. Eras: BTC → NFT → RWA → ?
- **Game-investing analogy (primary market):** fast/explosive rise, short user lifecycle, high cash flow ⇒ invest at the earliest base-platform stage around new-asset issuance-trading, take *equity only*, exit via IPO/dividends (drop "exchange listing is the only exit"). **Founder filter: back finance-background founders** (Fred Ehrsam/Coinbase, Alon Cohen/Pump.fun, Jeff Yan/Hyperliquid ex-HRT) over internet-background ones.
- **First-principle portfolio scaffold (两抓手/三标准/四赛道):** first principle = peer-to-peer transparent public ledger. **两抓手** = 流量 + 流动性. **三判断标准** = 独立产品价值 / 独立商业价值 / 能否穿越牛熊. **四赛道** = 交易所 / 公链 / RWA(or 稳定币) / DeFi. Strategy: invest in the **品类定义者** within each track. Map: 新资产→BTC/Coinbase/公链; 合规→Coinbase/Robinhood/Circle/Securitize; 融合→ETH/Solana/Base/Pendle/AAVE/Uniswap/Hyperliquid.

---

## N1. BTC mining / 算力 industry (Marathon-type miners)

The native lens for a pure BTC miner — DecadeX miner reports are **bullish-with-a-NUMBER**, expressed as a *leverage multiple vs the underlying*, NOT an abstract "long-term underperforms BTC" hedge.

- **Leverage-ratio regression (the analytical centerpiece).** Regress miner stock % change against BTC % change *separately for bull and bear* and report the slope (y = kx) per peer. Empirical anchors: MARA bull 6x (prior cycle) → ~1.5x (this cycle); CLSK ~3x; MSTR ~0.6x; bear ~1x. Use it to project cycle returns (e.g. leverage 1.5x, BTC $150K ⇒ MARA ~3x+; full upside ~8-10x from the BTC-$16K low). Miner equity has **MORE** upside elasticity than BTC in the cycle, not less.
- **Canonical peer set = MARA vs CLSK vs MSTR ("BTC's mapping in fiat").** Primary-market discount buying (MARA/CLSK mine below spot) vs secondary-market (MSTR buys spot). Require a relative pick with the reason (e.g. **CLSK = lower average production cost + smaller size ⇒ higher elasticity**). Do NOT default to IPP/REIT/CoreWeave peers.
- **P/B as the PRIMARY valuation** (assets = BTC holdings + PP&E), with a peer P/B table (e.g. MARA 4.84 vs CLSK 4.09). **Warn against anachronistic/forward concepts** — mNAV, AI/HPC pivot, REIT/EV-EBITDA multiples — unless the corpus date supports them (a 2024 miner report never mentions AI/HPC).
- **4-stage halving cycle model:** The Rising Bull → Mining Goldrush → Inventory Flush → Shake Out; plus the empirical **hashrate-lags-price by 60-120 days (2-4 months)** anchor. State which stage the cycle is in — the halving cycle IS the organizing framework, not a "priced-in" footnote.
- **Miner second/new revenue curve = transaction fees + 铭文 (inscriptions/Ordinals) / ecosystem** — the post-halving answer to declining block subsidy. (This is the house's actual second-curve, distinct from any AI angle.)
- **Contrarian "wealth-effect weakening" check:** each successive halving cycle produces a smaller BTC price gain (e.g. 312% → 134% → 18% pre-halving) ⇒ temper the leverage call, surface as a risk.
- **Management/ownership + survival diligence (required α inputs):** CEO background (tech operator vs capital-markets operator), insider ownership % (low = governance flag), top external holders; hosting model (third-party-hosted vs self-operated %) and machine-mix economics (weak-profitability rigs). Include a **bankruptcy case study** (an over-levered cautionary peer, e.g. Core Scientific) — contrast its D/E trajectory with the subject's as the survival test.
- **Period-accurate data anchors** (penalize generic/forward numbers): hashrate (EH/s), BTC held vs produced vs bought, avg production cost with/without depreciation, marginal cost, D/E, employee count.

## N. Selected house conclusions (precedent — update, don't repeat blindly)

- 现阶段公链主要矛盾 = **资产发行效率** (trilemma choice is scenario-dependent).
- 协议层是 ETH 寡头定局; 应用层仍开放; 看好整个板块 3-5 年 (Stable Mcap = 抓手).
- SOL 本轮赢在 C端资产发行 niche + **超高组织运行效率** (Foundation+Labs, regional-GDP KPIs, Superteam) + Meme as a marketing flywheel.
- L1-L2 现为竞争关系; L2 = tax-sacrificing marketing; ETH 扩L1 = 抢L2的生意.
- **Ethereum ≠ ETH** — creation without capture; ETH's problem is demand not supply. Still bullish on ETH as category-definer *conditional on* 天时(next asset eruption lands in ETH)/地利(fix L2 诸侯割据, reclaim execution to L1)/人和(org efficiency). ETH 3-5yr: $3k/$6k/$10k; SOL $250/$500.
- Coinbase: compliance is the moat (a double-edged sword limiting product innovation); from a compliance angle Coinbase is *undervalued* post-FTX; future 3-5yr 4-10x — but must decorrelate from BTC price.
- 2025 deregulation view: the three US crypto bills *remove* the compliance barrier → Coinbase retail moat (which was *regulatory ambiguity itself*) erodes; **ETF becomes the largest US spot channel** (~50%, surpassing #2 exchange); fees converge toward zero; both Coinbase ("new finance / AWS") and Robinhood ("new generation of users") could become >$300B over 5-10yr.
- Hyperliquid: Tier-1 category-definer that can cross cycles near-term; great company at a *fair* (priced-in) price; regulation is the black swan.
- Stablecoins: ~100x runway; compliant 1:1 stablecoins win payments; the Coinbase-Circle alliance (≈3% equity but >50% of Circle revenue as distribution) is structurally unstable.
