# DecadeX AI Frameworks

*Named frameworks, house views, and key conclusions from DecadeX's AI reports (大模型/LLMs, AI compute, ad platforms, autonomous driving). Apply with numbers. Educational.*

---

## A. 大模型 = 逻辑的输出机器 (LLM = a logic-output machine)

The master lens. Evaluate a model on its produced logic along **three axes**:

1. **逻辑快 (fast)** — speed: first-token latency, avg response time, tokens/s. (Fast enough ⇒ can stack RAG for more intelligence; enables real-time / on-device.) Gemini 2.5 Flash ~353 tok/s = fastest.
2. **逻辑便宜 (cheap)** — cost: $ per 1M tokens. Lower cost ⇒ applications spread from high-value to low-value scenarios. Google's TPU vertical integration → best $/intelligence.
3. **逻辑强 (strong)** — intelligence: LMArena, intelligence index, HLE.

Two revolutions follow: **计算革命 (computation) precedes 交互革命 (interaction)** — efficiency gains land first (low friction); interaction shifts need real-time/ecosystem/privacy preconditions.

## B. 智能三来源 + Pre × Post × TTS 乘积模型

Decompose intelligence into three independently-analyzable layers; **product experience = Pre × Post × TTS (a PRODUCT, not a sum)**:

- **预训练 (Pre):** sets the intelligence *ceiling*; the root source.
- **后训练 (Post):** carves user-perceived IQ within the ceiling; **highest marginal return now.**
- **Test-time Compute (TTS):** stack inference-time compute for stability; supplement to Post, capped by Pre's ceiling.
- **Orderings:** marginal return **TTS > Post > Pre**; technical difficulty **Pre > Post > TTS**.
- **Diagnostic use:** for each layer ask "还有十倍空间吗?" — Pre basically *no* (energy/data-limited; text pretraining has ~2-3 rounds left), multimodal yes; Post yes (esp. search); TTS diminishing. Gemini's gap = strategy mis-placed on Pre while neglecting Post/TTS → layer scores ChatGPT 90/90/80 vs Gemini 90/50/0 ⇒ ×-product collapses to a ~10x experience gap.

## C. Scaling Law + four pretraining ceilings

- **L(N,D) = L∞ + 2085.43·N^-0.3658 + 482.01·D^-0.3478.** Optimal: **D ≈ 20-30×N, C ≈ 6-9×N·D**. Plugging Grok-3 scale: params ×1000 ⇒ L drops only ~2% ⇒ no GPT-1→GPT-4-style leap visible.
- **Four physical ceilings (in order):** 能源 (energy, currently caps C to ~1e5×) / 芯片产能 / 数据 (existing 500T, largest public set 15T, industry uses 30-60T; bottleneck within 5yr) / 通信. Breakouts: algorithm so D≈15N; multimodal (but only ~GPT-4→4.5-level lift).

## D. Ad-platform frameworks (Meta / Google)

- **北极星指标 ranking: 流量规模 > 新媒体形式 > 转化率.** 流量规模 (= MAU × avg time) is the *most core moat* and decides market share; 新媒体形式 is the carrier of new traffic + source of cyclicality; 转化率 is the internal-competition KPI in the current **变现驱动 (monetization-driven)** phase.
- **Revenue decomposition (the spine):** 广告收入 = **DAU × 渗透率 × Impression × Adload × eCPM (= 竞价价格 × eCTR)**. Split flow side (广告浏览量 = f(流量规模, 新媒体形式)) from monetization side (广告价格 = 竞价价格 × 转化率). 广告加载率 (cap ~30%) and 竞价价格 = "metrics that don't affect competition." This same formula becomes the bottom-up valuation model (per product: FB / IG / Reels).
- **二流生意中的二流模式 (Meta):** advertising = a 双边垄断竞争 + 强周期 "second-tier business"; Meta is **有数无端 (has data, lacks the device/端)** ⇒ a "second-tier model" subordinate to Apple. Proven by the **IDFA episode** (reverse-proof that device-data is the moat: Meta's first negative ad-growth, 21Q4 ~$10B loss, 22Q3 CPM -18%). Thesis: "一流团队对冲二流生意" (a first-rate team hedging a second-rate business).
- **微垄断循环 (flywheel):** 抄袭新兴媒体形式 → 高基数流量吸纳 → 推广 → 更丰富内容 → 更多用户. Breaks only on a *new OS/端* where Meta has no scale advantage — the one real threat.
- **相邻用户增长 (Adjacent User Theory):** grow by converting "adjacent users" (know it, tried it, can't activate) via the dimension closest to core users — Meta's underrated Alpha (sustained 破圈).
- **AI三驾马车 (impact ranking): 投放工具 > 推荐算法 > GPU取代CPU.** Conversion-lift buckets: tools >10% (Advantage+), algorithm ~5%, chips <5%. Tools rank highest because of the long-tail (中长尾) advertiser base (UGC logic lowering the投放门槛).
- **TAC 低买高卖 (Google):** the ad business is "buy-low-sell-high on device traffic." Buy a user ~$25 (端侧买量 contributes 56% of search share) vs monetize ~$65. Search revenue = MAU × 查询量 × 填充率 × 点击率 × 价格 → click growth slowed 70%→2%, so *ad price* (CPM +100% since 2018) is the current driver.

## E. Core AI vs Gen AI (β / α split)

- **Core AI (β):** serves the main ad business (recommendation models, ad tools, chip substitution); industry-baseline, predictable (~20% YoY, 5yr 2.5x / 10yr 6x).
- **Gen AI (α):** AI-native scenarios (open-source ecosystem, AI assistant, AR/VR); excess return, hard to predict (5yr ~30x, benchmarked to OpenAI ARR ~200%/yr).
- **数据端 (data vs device) 2-axis scoring:** 数 (data): Google > Meta > Apple > MSFT; 端 (device): Apple > Google > MSFT > Meta. "有数无端是Meta最大的尴尬."
- **开源即护城河:** an open OS is a moat for a *separate* profit business (Android/Chrome precedent). Only Meta's structure supports open models (no cloud to cannibalize) ⇒ "AI周期的安卓" candidate.

## F. AI+ vs +AI

- **AI+** = AI-native, natural-language/voice, AI does the work — *true* innovation (ChatGPT is "AI+", a disruptive innovation on search).
- **+AI** = AI bolted onto legacy data/channels as a replaceable plugin → fragmented experience.
- **"AI+ 的机会远远大于 +AI"; only AI-native apps create a 10x experience.** The 10万亿 company will be a *大模型公司* (OpenAI = best positioned). Pure prompt-orchestration / public-API assistants get copied by model vendors.

## G. ToB / ToC + competition staging

- **ToB** = API/custom/private deployment — cash cow, large & fast-growing, but profit disperses across enterprise/cloud/compute/devs ⇒ **cannot monopolize.** **ToC** = Chatbot/Agent — immature model, smaller, but can form a *de-facto monopoly* via scale/brand ⇒ the investable direction. (2024: ToB ~$14B, ToC ~$2B.)
- **Chatbot 四层级 + maturity:** 技术 (80, watch GPT5/Grok4) → 产品 (30, watch first 周活过10亿) → 运营 (10) → 商业化 (10, watch a non-subscription model). Now: tech converging, product just starting, ops/monetization未展开 ⇒ **product capability is the current 胜负手; core = 更通用的智能.**
- **先验/后验 evaluation:** 先验 (product experience: 高效=快/便宜/稳定; 智能=超人类/更通用/个性化) + 后验 (用户量 + 粘性). **Most important tracking metric = 独立访客 (unique visitors).** (ChatGPT crushes on 访问量/独立访客 15.64 vs 5-8, DAU/MAU 0.37 vs 0.05, 月留 15.4% vs 1.2%.)
- **终局: two operating systems.** PC = 效率优先的统一工作台 (monopoly data + 3rd-party apps → scale + two-sided effect); phone = 个人语音助手 (NL is a GUI supplement, since phones are娱乐). Application control transfers to the model.

## H. Agent vs LLM (bit-economy lens)

- **Agent = information management + action** (vs LLM's value-poor token-in/token-out) ⇒ **Agent is a better investment target than LLM.** Agents replace pure information-management platforms (e-commerce, local life, search); content/entertainment platforms are safer (consumption still done by users).
- **Current LLMs are "三无" (no network effect):** fail the test 边际用户价值 > 边际服务成本 — (1) cloud compute ⇒ marginal cost ≠ 0, (2) user-data value low, (3) long-tail ⇒ diminishing data utility. ⇒ subscription is a poor model; monetization likely ad-based or OS-style.
- **专业性-泛化性-经济性 不可能三角:** a model can't max all three ⇒ bifurcation into B-end professional vs C-end general leaders.

## I. AI compute fundamentals (the technical investment lens)

- **Y = M · X** (model = a pile of params × one multiply; X, Y = tokens). Direct conclusions: bigger params ⇒ pricier per-inference; longer input ⇒ tighter VRAM; weights fixed ⇒ inference is cheap.
- **三个透镜: 显存 / 算力 / 通信** (can it fit / how fast / must it wait). Map to: HBM容量&带宽 (SK hynix/Micron, CoWoS); low-precision tensor-core FLOPS (FP8/FP4); NVLink/ICI (intra-node) + InfiniBand/Spectrum-X (inter-node).
- **Roofline + arithmetic intensity (FLOPs/byte):** decode = memory(HBM-bandwidth)-bound; prefill / training-forward = compute(FLOPS)-bound. ⇒ basis for prefill/decode disaggregation, and why "训练显卡" ≠ "推理显卡" demand.
- **Key formulas:** matrix mul ≈ **2MNK**; transformer block/token forward = **24d² + 4sd**; **training step ≈ 6NT** (fwd 2NT + bwd 4NT); **MFU = achieved / peak FLOPS** (GPT-2 small × H100 ≈ 10%, busts the peak illusion); training = **16 bytes/param** (mixed-precision+Adam) = **8× inference**; **activation ∝ s²** (seq 8192 ⇒ ~97GB, blows an H100). **MoE:** 8-expert top-2 ⇒ params ×8 but FLOPs/token only ×2.
- **软件杠杆 (software is a margin lever, not just hardware):** fused kernels / FlashAttention / PagedAttention / KV-quant / scheduling raise usable throughput ~2× per generation *without* new hardware. **KV cache isn't necessarily linear-explosive** ("KV 取决于模型结构和软件栈"). Agents push token consumption 1-2 orders of magnitude (and non-GPU infra: sandbox/browser farm/search backend). 长程 (GPU-hours + non-GPU) ≠ 长上下文 (HBM容量&带宽).
- **"Token 即电力" as a *discussion*, not a thesis:** "token 在计量上像电、在差异化上不像电" (metered like kWh, but quality/latency/lock-in/non-linear-upgrades break fungibility).
- **瓶颈 → 受益方 → 护城河 → 利润影响 速查表:** translate each bottleneck (HBM/算力/互联/封装/电力/软件栈/利用率) into beneficiaries, moat, and margin — tag 事实/推断/观点.

## J. Self-driving frameworks

- **两大拐杖 (two crutches):** 激光雷达 (融资267亿 vs 市场仅10亿; $1000/unit) + 高精地图 (10亿/车队; 500万km can't keep timeliness; 涉国家安危) — "拄着错误的拐杖跌跌撞撞." Tesla 纯视觉/无图 = the reverse path.
- **数据-成本恶性循环:** 成本高 → 定价高 → 没人买 → 没数据 → 数据贵. "数据决定上限,算法只是在逼近它." Tesla 影子模式 = positive data flywheel (FSD 渗透率 >25%, 32亿km).
- **端到端 vs 模块化:** 局部端到端 viable; **全局端到端 basically infeasible** (no interpretability, car-side <100ms / ≥10Hz). 世界模型 = GPT-training analogy (stronger generalization but higher hallucination ⇒ can't yet solve corner cases).
- **Verdict:** if corner cases unsolved, production cars stay **L2+ long-term**; pure-vision = highest cost-performance there.

## K. Private eval when public benchmarks are flawed (X-Eval)

Public benchmarks fail: data leakage, too easy (LMArena difficulty ≥6 < 20%), test "做题" not "解决任务", and only test API (web version already far exceeds it via tools). **Build a private eval** on web-version high-difficulty real tasks (X-Eval: 逻辑/日常/深度搜索; o3 83.3% >> Gemini 60%) to reverse-infer that, e.g., Gemini's retention problem = model capability, not just product.

---

## L. Distillation method for AI valuation (Microsoft/Meta examples)

- **三情景 PE 估值:** build revenue per product → net margin → PE → probability-weight (Meta: Upside 4.64T@10% / Neutral 2.42T@80% / Downside 0.86T@10% → exp 2.49T, ~60% upside; PE benchmarked to MSFT 37 / Google 25 / Apple 41 and own history).
- **三情景 PS 估值 (primary for revenue-growth tech names).** For names valued on revenue growth (not mature profit), the house headline is often **PS-driven**: take a peer PS band (e.g. 6x–12x) → apply to a *segment-built* revenue forecast (传统业务 + AI Copilot/助手 + 云AI) → a 5-year market-cap path Upside/Base/Downside, landing on a **"~Nx in 5 years"** headline (e.g. Microsoft 理想情况 ~3.5x). Reserve PE/SOTP/shadow-option for mature-profit or un-investable-directly cases. Always reproduce the human's actual figures/method, not larger untethered numbers.
- **影子资产投资法:** can't invest in OpenAI directly ⇒ invest the strongly-bound *shadow asset* (Microsoft). Bear/Base/Bull sensitivity: OpenAI contributes 6%/14%/25% of MSFT mcap; **strategic value > financial value** (lose OpenAI ⇒ MSFT becomes a pure ToB cloud).
- **Reconstruct the actual deal MECHANICS, not "binding strength" in the abstract.** When a giant is bound to a lab, tabulate the concrete contract terms — they are what made the human's OpenAI section credible: **profit cap multiple** (OpenAI's 100x cap), **equity %** (Microsoft ~49%), the **profit-return waterfall/order** (75% to MSFT until cost recouped, then 49%), **voting/governance** (voting-rights代持, non-profit board control), and **exclusivity**. Surface the emerging frictions too (compute under-supply → Stargate / Neo-Cloud pivot; each side hedging — MSFT扶植其他 lab, OpenAI抽佣电商变现).

## N. Incumbent-platform AI frameworks (Microsoft / Google / Meta as platform companies)

- **北极星 = "能否再造操作系统 / 重构流量入口" (can AI let this company recapture a lost, or build a NEW, platform/OS entrance?).** This is the conclusion engine for incumbent platforms. Tie the upside binary directly to it: **rebuild the OS / 重构流量入口 ⇒ ~5x; fail ⇒ max ~3x.** Weight the north star explicitly (e.g. **70% "AI rebuilds the 端/entrance" + 30% "AI ecosystem"**). Ask it of every incumbent.
- **大模型 = 下一代计算机, NOT 互联网 (it does not solve connection/connectivity).** Understand from a *computation* angle, not an internet angle. ⇒ the eruption marker is **a Windows-95-class capability leap + 算力下放到消费级硬件 (compute pushed down to consumer GPUs)** — named, checkable milestones, not a generic penetration threshold.
- **大模型竞争四维度 (priority-ranked): 场景 >> 数据 >> 算法 >> 算力.** Score each giant on the four (weighted toward 场景/数据) to produce the leadership call, and require an explicit **"who overtakes whom in 3-5 years"** verdict (the kind of named contrarian conclusion the house produces — e.g. "Microsoft暂时领先, 但被Google超越可能性大": Google wins 场景+数据, Microsoft only 算法+算力). Two players hold the 船票 (OpenAI via ToC product experience; Google via vertical 软硬件一体), each constrained by 基因 (OpenAI→ToC wants ToB; Google→ToB wants ToC).
- **开源 vs 闭源 model ecosystem.** "开源会成为安卓; 闭源赢家不超过3个." Locate the company on a model↔application ecosystem-positioning map (which category of model+app pairing it is) so you place it precisely within the AI value chain.
- **AI 是全球化机会 / 区域采纳差异.** The US adopts AI faster than China (移动互联网包袱更深 ⇒ 阻力更大); situate the company in the global diffusion picture, not only firm-level mechanics.

## O. Hardware-monopolist lens (NVIDIA-type "picks-and-shovels" compute supplier)

- **拿着锤子找钉子 (a hammer looking for nails) vs 收税官 (tax collector) — pick the RIGHT valence.** The house view of a pure compute supplier is often the *passive* one: it is a "big-compute scenario-**discovery** company" that can only build better hammers but **cannot create downstream scenarios** — its revenue is **passively determined by downstream industries**. Do not auto-invert this into an active "tax-collector empowering everyone" thesis (the opposite valence).
- **It may be a CYCLICAL stock (周期股) only temporarily escaping the "hardware cyclical curse" (硬件周期性魔咒).** 30 years of growth = computing-task concentration + scale; historically every downstream slowdown caused a valuation-logic shift + ~50% market-cap halving (the -87%/-52%/-81%/-50% drawdown chart). Do not reflexively reject the cyclical framing if that is the house anchor.
- **Scenario-picking = WHOLE-INDUSTRY trial-and-error (全行业试错), not unique foresight.** Scenarios appear randomly/suddenly; the company survives by building a scientist ecosystem and 蹭热点 (riding hot trends), not by prescient belief.
- **North Star = a next-gen qualitative (10x) model OR a 100M-DAU AI killer app**, with explicit probabilities (e.g. Killer App 70% / next-gen 10x model 30%), and the judgment that these are HARD to appear ⇒ growth is hitting a ceiling. Don't substitute an invented metric (e.g. "compute tax rate").
- **Demand sizing in units × $.** Build optimistic/neutral/pessimistic GPU-demand tables from cloud-capex × a benchmark attach rate (e.g. training ≈ 3.5M H100 ≈ $120B; inference ≈ 17M A100 ≈ $260B), not vague capex aggregates.
- **Value-chain decoupling split + BOM/squeeze.** Quantify tightly-coupled (~60%: chip/NVLink/CUDA, hard to replace) vs loosely-coupled (~40%: storage/optical/switches, replaceable) as the mechanism of value redistribution. Tear down the BOM ($200 logic die + $1500 HBM + $700 CoWoS + $500 other ≈ $3000 cost vs $35000 price) and note the monopolist faces its OWN squeeze (TSMC/CoWoS raising fees — the "英伟达税" has an upstream counterpart).
- **BETA延伸: hardware = the origin/sensor of the digitalization track.** A compute supplier covers downstream scenarios FASTER than traditional VC, and is the foundational layer for robotics/biotech/autonomous-driving/industrial automation.
- **Valuation anchors stay tethered to the house figures.** SOTP with Graphic on PS and Compute&Network on PE/G (CAGR ~42%, PE/G ~1.2); $3T fair in the wave, $1.5T the neutral "AI stops" value. Don't inflate far beyond the report's own numbers. Timing read can be that the market has *already* over-discovered/over-valued the name (still pricing exponential train+inference growth that won't materialize).

## M. Selected house conclusions (precedent)

- LLM = logic-output machine; 计算革命先于交互革命; ChatGPT ≠ 大模型 (ChatGPT is the search-disrupting product; the OS is still at "kernel" stage).
- ChatGPT has a ~10x user-experience lead, is the Chatbot 品类定义者; Gemini hard to catch (strategy mis-placed), Claude → small-but-fine coding tool, Deepseek likely missed the window.
- OpenAI: shallow moat (brand from stable high intelligence) + four org "雷" (non-profit structure, Microsoft 畸形条约, Sam, talent gap); but if tech converges it won't *lose on org*. Worth investing at $300B; best path = the Microsoft shadow asset.
- Google: search disruption is "短期 No, 长期 Yes" (Yahoo took ~10yr; LLM-search cost is ~40x and breaks even ~27H2); the real problem is "搜索与Gemini 左手打右手"; Google holds B-end via 芯片-云-模型-应用 vertical integration (TPU cost ~20% of MSFT's); market over-reacted ⇒ near-"arbitrage" at $2.09T.
- Meta: "一流团队对冲二流生意"; 有数无端; ~60% mcap upside; long-term risk = next-gen OS new species (Meta lacks 0-1/hardware gene).
- AI = a new tech cycle still in 爆发期前期 (infrastructure sub-stage: 算力/数据/能源); next milestone = 神器渗透率 > 5%, then find the representative company.
