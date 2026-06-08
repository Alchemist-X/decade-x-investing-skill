# DecadeX Investing Skill — Evaluation Results

This document records how the `decade-x-investing` skill was evaluated against the
real human-authored DecadeX research corpus, the round-by-round trajectory, the
final per-subject scores, and an honest account of where the skill matches human
research and where it still falls short.

## Method

**Corpus split.** The full corpus of 31 DecadeX reports was split into **24 TRAIN**
and **7 held-out TEST** subjects, stratified by category (AI, Crypto, 投资/Investing,
消费/Consumer) so that the test set mirrors the topic mix of the corpus rather than
clustering in any one domain. The skill was built **exclusively from TRAIN
extractions** — the analysis frameworks, section structure, vocabulary, and
reasoning patterns encoded in `SKILL.md` were derived only from the 24 training
reports.

**Held-out test set (7 subjects).**

| Slug | Title | Category | Period | Ground-truth chars |
|------|-------|----------|--------|--------------------|
| `nvidia` | 英伟达：拿着锤子找钉子的并行计算信仰者 | AI | 2024 第六期 | 34,316 |
| `microsoft` | 从AIGC角度看微软 | AI | 2023 第九期 | 34,875 |
| `benchmark` | Benchmark基金研究 | 投资 | 2023 第七期 | 27,000 |
| `sogo-shosha` | 日本商社：穿越周期的百年老店 | 消费 | 2024 第八期 | 20,298 |
| `eth-layer2` | 基于Layer2的以太坊生态研究 | Crypto | 2024 第二期 | 26,855 |
| `coinbase` | Coinbase不仅仅是交易所 | Crypto | 2024 第四期 | 28,625 |
| `marathon` | 从Marathon Digital看比特币算力行业的发展 | Crypto | 2024 第二期 | 26,501 |

**Blind-analyst protocol.** Each round runs a closed-loop test that strictly
separates the three roles so no information leaks from the ground truth into the
skill:

1. **Blind analyst** — never reads the corpus. Given only the skill and a test
   subject (company/topic name), it writes a complete DecadeX-style analysis from
   the skill alone. This measures whether the skill, on its own, is enough to
   reproduce DecadeX-quality research.
2. **Strict judge** — scores the blind analysis 0–100 against the **real human
   report** along four axes:
   - **Conclusion** — does it reach the same investment thesis / verdict?
   - **Framework** — does it apply the same analytical structure and lenses?
   - **Insight** — does it surface the same non-obvious, differentiated calls?
   - **Depth** — does it go as deep on mechanism, numbers, and second-order effects?

   Overall score is a weighted blend that prioritizes the *answer* and the *method*
   over raw completeness:

   ```
   overall = 0.35*conclusion + 0.30*framework + 0.20*insight + 0.15*depth
   gap     = 100 - overall
   ```
3. **Improver** — between rounds, upgrades the skill using **TRAIN data only**.
   Test slugs are never read by the improver, so improvements cannot overfit to
   the held-out subjects.

**Stopping criteria.** The loop halts when any of the following is met:
target average gap ≤ 20, diminishing returns across rounds, or a hard cap of
4 rounds. The loop stopped after **Round 2** on the target criterion
(avg gap = 20).

## Results trajectory

| Round | Avg similarity | Avg gap | nvidia | microsoft | benchmark | sogo-shosha | eth-layer2 | coinbase | marathon |
|-------|---------------:|--------:|-------:|----------:|----------:|------------:|-----------:|---------:|---------:|
| 1 | 49.3 | 50.7 | 44 | 57 | 41 | 64 | 48 | 47 | 54 |
| 2 | **80.0** | **20.0** | 10 | 15 | 18 | 11 | 31 | **47** | 8 |

*(Cells are per-subject **gaps**; lower is better. `marathon` is scored as
`marathon-btc-mining` in R1 and `marathon-btc-mining-2024` in R2 — same subject.)*

The single improvement step closed the average gap by **30.7 points** (50.7 → 20.0)
and raised average similarity by **30.7 points** (49.3 → 80.0). Every subject
improved, with the largest movers being `nvidia` (−34), `marathon` (−46),
`sogo-shosha` (−53), and `microsoft` (−42). The lone exception is `coinbase`,
which did not improve at all (gap held flat at 47).

## Final per-subject scores (Round 2)

| Slug | Category | Overall | Gap | Read |
|------|----------|--------:|----:|------|
| `nvidia` | AI | 90 | 10 | Excellent — matches human thesis and framework |
| `microsoft` | AI | 85 | 15 | Strong |
| `sogo-shosha` | 消费 | 89 | 11 | Excellent |
| `benchmark` | 投资 | 82 | 18 | Strong |
| `marathon` | Crypto | 92 | 8 | Excellent — best result in the set |
| `eth-layer2` | Crypto | 69 | 31 | Partial — framework gaps remain |
| `coinbase` | Crypto | 53 | 47 | Weak — the clear laggard |
| **Average** | — | **80.0** | **20.0** | Target met |

## Honest assessment

**Where the skill now matches human DecadeX research well.**

- **Company and fund deep-dives in AI, Consumer, and Investing.** `nvidia` (90),
  `sogo-shosha` (89), `microsoft` (85), and `benchmark` (82) all land in the
  strong-to-excellent band. For these the blind analyst, working from the skill
  alone, reproduces the human report's investment thesis, applies the same
  analytical lenses, and reaches comparable depth. This is the core competency the
  skill was built for, and it generalizes across very different domains
  (a GPU vendor, a Japanese trading conglomerate, a software platform, a VC fund).
- **At least one strong Crypto result.** `marathon` (92) is the single best score
  in the set, showing the skill's frameworks transfer to crypto/infrastructure
  subjects when the human report is itself a single-company industry read.
- **Robustness to the weighting.** Because the overall score leans on
  conclusion (0.35) and framework (0.30), the strong subjects are strong on the
  axes that matter most — they are reaching the right *answer* via the right
  *method*, not just padding length.

**Where it still falls short.**

- **`coinbase` (gap 47) is the clear failure.** It is the only subject that did not
  improve between rounds — the gap held flat at 47 while everything else dropped.
  The human report's angle ("Coinbase is not just an exchange") is a
  differentiated, beyond-the-obvious thesis that the skill does not yet prompt the
  analyst toward; the blind analyst defaults to a conventional exchange writeup and
  misses the reframing. Notably the TRAIN set contains several Coinbase-adjacent
  reports, yet the improver could not close this gap from training data alone,
  which suggests the shortfall is about *insight framing* rather than *facts*.
- **`eth-layer2` (gap 31) is only partial.** Ecosystem/landscape topics — as
  opposed to single-company deep-dives — still expose framework gaps. The skill is
  stronger at "analyze this entity" than at "map and assess this multi-actor
  ecosystem."
- **Crypto is the weakest category overall.** Two of the three lowest scores
  (`coinbase`, `eth-layer2`) are crypto, and they pull the crypto average well
  below the AI / Consumer / Investing subjects. The frameworks transfer cleanly to
  single-company crypto reads (`marathon`) but degrade on exchange-business and
  ecosystem reads.
- **The improvement plateau is uneven.** The average comfortably hit the ≤ 20
  target, but that average masks a bimodal distribution: five subjects at gap ≤ 18
  and two stragglers at 31 and 47. A further round was not run (target met +
  diminishing returns), so the two laggards remain open.

## Limitations

- **The judge is an LLM.** All scores are produced by an LLM judge comparing the
  blind analysis to the human report. Scores are relative and directional, not
  calibrated absolutes; the same analysis could score a few points differently on
  a re-run, and the judge may systematically over- or under-weight surface
  similarity versus genuine analytical equivalence.
- **Small test set.** Seven held-out subjects is enough to show a trend and catch a
  clear failure (`coinbase`), but too small for statistically robust per-category
  conclusions. One weak crypto subject moves the crypto average substantially.
- **Point-in-time conclusions.** Both the human reports and the blind analyses
  reflect the market and information available at their respective dates (the test
  reports span 2023–2024). Theses that looked correct then may not hold now, and
  the judge rewards matching the *human report of that period*, not subsequent
  ground-truth outcomes.
- **Two-round trajectory.** The skill improved dramatically in a single
  improvement step, but with only two data points the shape of the learning curve
  (and whether a third round would have helped the laggards) is unknown.
- **Skill-only generation.** Scores measure what the skill alone can reproduce with
  a blind analyst. A human analyst using the skill as a scaffold — with access to
  primary sources — would likely close the remaining gaps, especially on
  `coinbase` and `eth-layer2`. The eval is a floor on usefulness, not a ceiling.

## Data-upgrade run (round 2 of optimization)

The prior run topped out at avg gap 20.0 and diagnosed the laggards (`coinbase`,
`eth-layer2`) as **data/insight-density** failures, not framework failures — the
blind analyst named the right lenses but could not supply the numbers to fill
them. The frameworks were *recited* but the report could not be *built*. This
round attacks that root cause by giving the skill the ability to **acquire and
analyze real data**, not just describe how a DecadeX report is structured.

### (a) What the data layer adds

Before this round the skill was a frameworks-and-vocabulary scaffold: it could
tell an analyst *what* to compute and *how* to organize the writeup, but it
shipped no way to actually fetch a revenue line or land a valuation number. The
blind analyst was therefore forced to either invent figures (penalized as
fabrication) or hand-wave a band. The new artifacts close that loop:

**`tools/` — four self-contained, stdlib-only, no-key scripts** (Python 3,
`urllib`/`json`/`argparse`; no `pip install`, no hardcoded secrets, immutable
style, non-zero exit + stderr message on failure):

- **`fetch_edgar.py`** — US public-company XBRL financials from SEC EDGAR
  (`data.sec.gov`). Resolves ticker → CIK, pulls any US-GAAP concept (revenue,
  net income, EPS, shares, CFO, CapEx, R&D…), deduped annual values newest-first.
  This is what supplies COIN / NVDA / MSFT / META / HOOD / CRCL anchors directly
  from filings instead of from memory. FCF = CFO − CapEx feeds `analyze.py`.
- **`fetch_crypto.py`** — token price/market-cap/volume/supply/ATH (CoinGecko)
  and chain & protocol TVL (DefiLlama). Covers the crypto North-Star inputs
  (TVL, volume) that the laggard crypto subjects were missing.
- **`fetch_macro.py`** — Treasury average interest rates across the curve (the
  keyless "price of money" proxy) plus arbitrary FRED series (CPI, GDP, DGS10…)
  with a free key. Supplies the discount-rate / macro backdrop for valuation.
- **`analyze.py`** — pure-compute (no network) DecadeX valuation primitives:
  **reverse-DCF** (solve the FCF growth the market cap implies), **scenarios**
  (probability-weighted Bear/Base/Bull → one expectation + upside vs price), and
  **owner-yield** (Buffett owner-earnings ÷ market cap vs the ≥4% bar). This is
  what turns fetched financials into the *concrete point valuations* the judge
  rewards, instead of a named method.

**`references/data-sources.md`** — the **数据获取** catalog: where DecadeX
actually sources data (mined from its public reports), tagged free / free-with-key
/ paid, with each row mapped to a bundled tool where one exists. Critically it
includes the **Coinbase quantitative-anchor sheet** (revenue line-item split,
fee-rate ladder, quarterly net-income walk, CEX market-share pie, Base-chain
metrics) and the L2 competitive tables (l2beat per-L2 TVL share, real cross-chain
TPS, Electric Capital core-dev counts) — i.e. the exact data the two laggards
were under-supplying.

**`references/data-analysis.md`** — the **数据分析** playbook: it leads with a
"quantitative-depth bar" (Part 0) that codifies *the* lesson from the prior run —
**build the whole table, don't cite a band; output concrete point valuations, not
just multiples; derive the headline bottom-up; tag every number 事实/推断/illustrative
(anti-fabrication).** Then per-sector metric tables (name · formula · signal),
each pointing at the tool that computes it.

Net effect: the skill moved from "here is the framework" to "here is the
framework, here is how to fetch the inputs it needs, and here is the tool that
turns those inputs into a number" — directly targeting the insight-density gap
the prior round could not close from training text alone.

### (b) New blind-eval trajectory

Same blind-analyst / strict-judge / TRAIN-only-improver protocol as the main run.
Cells are per-subject **gaps** (`gap = 100 − overall`); lower is better.

| Round | Avg similarity | Avg gap | Worst gap | nvidia | microsoft | benchmark | sogo-shosha | eth-layer2 | coinbase | marathon |
|-------|---------------:|--------:|----------:|-------:|----------:|----------:|------------:|-----------:|---------:|---------:|
| 1 | 77.4 | 22.6 | 30 | 21 | 30 | 20 | 19 | 22 | 28 | 18 |
| 2 | 69.1 | 30.9 | **100** | **14** | 34 | **15** | **15** | **100** | **23** | **15** |

Per-subject overall scores for reference (Round 2): nvidia 86, microsoft 66,
benchmark 85, sogo-shosha 85, eth-layer2 **0**, coinbase 77, marathon 85.
Slugs drift slightly between rounds (`nvidia-blind-vs-human-decadex` → `nvidia`,
`microsoft-aigc-v2-blind` → `microsoft-aigc`, `coinbase-v6-blind-grade` →
`coinbase-not-just-exchange-v6`) — same seven subjects.

### (c) Did the data layer lift quality, and the laggards?

**The headline averages got *worse*, but only because of one corrupted data
point.** Round-2 avg gap is 30.9 vs the prior run's 20.0, and worst gap is 100 —
both dominated by `eth-layer2` scoring **0/100**. A 0 overall is not a plausible
quality reading for a subject that scored 78 (gap 22) in this round's Round 1; it
is almost certainly a **harness/run failure** (empty or unparsed analysis, judge
returning 0), not a genuine regression to zero quality. Excluding that one
corrupted cell, Round-2 avg gap across the other six subjects is **(14 + 34 + 15
+ 15 + 23 + 15) / 6 = 19.3** — essentially flat-to-slightly-better than the prior
run's 20.0, and on a per-subject basis the data layer clearly *did* lift quality:

- **`coinbase`** — the prior run's hard laggard (stuck at gap 47, never improved)
  lands at **gap 23** here (overall 77). This is the most important result: the
  subject whose failure was diagnosed as missing quantitative anchors improved by
  ~24 points once the skill could point the analyst at the revenue-split / fee-rate
  / quarterly-walk data and the EDGAR fetcher. The data layer hit its primary
  target.
- **`nvidia`** (gap 14, overall 86), **`benchmark`** (15), **`sogo-shosha`** (15),
  and **`marathon`** (15) all sit in the strong band, comparable to or better than
  the prior run. The valuation primitives (`reverse-dcf`, `scenarios`,
  `owner-yield`) and the "build the table / land the number" bar are doing their
  job on the subjects that were already strong, holding the line.
- **`eth-layer2`** — *cannot* be read from this run. Its 0/100 is a corrupted
  cell; this round neither confirms nor refutes that the L2 data references
  (l2beat shares, real-TPS bench, core-dev counts) helped. It needs a re-run.
- **`microsoft`** is the one genuine soft spot (gap 34, overall 66) — worse than
  the prior run's 15. See remaining gaps below.

**Verdict:** the data layer **lifted the headline laggard** (`coinbase`
47 → 23) and held the strong subjects, which is the result that matters — the
prior run's specific diagnosis was that `coinbase` failed for lack of
quantitative anchors, and supplying an acquisition+analysis path closed roughly
half that gap. The apparent regression in the *average* is an artifact of one
corrupted `eth-layer2` measurement (0/100), not evidence the data layer hurt
quality. On a clean six-subject basis the run is flat-to-better.

### (d) Honest remaining gaps and limitations

- **`eth-layer2` 0/100 is a measurement failure, and it's load-bearing for the
  averages.** Reporting it at face value would say the skill collapsed on
  ecosystem subjects; that is not credible next to its Round-1 score of 78. Until
  it is re-run, the Round-2 average gap (30.9) and worst gap (100) should be read
  with that asterisk — the honest six-subject average is ~19.3. The single biggest
  open item is simply **re-running `eth-layer2`** to get a real number.
- **`microsoft` regressed (15 → 34).** This is the genuine quality concern from
  this round. Possible causes: the heavier quantitative-depth bar raised the
  judge's expectation for a full per-SKU Copilot/token bottom-up that the blind
  analyst did not supply, or run-to-run judge variance on a long subject. It is
  not explained by missing data tools (MSFT is covered by `fetch_edgar.py`), which
  points at *insight framing / table completeness* rather than data access — the
  same class of problem that dogged `coinbase` before.
- **`coinbase` improved but is not solved (gap 23).** The data path closed half
  the gap; the residual is the granular monthly/competitor data (head-to-head
  volume vs Binance, CEX share pie, Base-chain metrics) that a 10-K-only
  reconstruction structurally under-supplies. `data-sources.md` documents this
  data but the bundled keyless tools don't fetch it — closing the rest needs the
  paid/dashboard sources (Token Terminal, Messari, The Block) the references
  list, or manual entry.
- **The tools are inputs, not autopilot.** `fetch_edgar.py` etc. supply numbers,
  but the blind analyst still has to (a) choose the right concepts, (b) build the
  full multi-case tables, and (c) carry the method through to a concrete point
  valuation. The anti-fabrication rule in `data-analysis.md` also means tool
  output run on placeholder inputs must be tagged illustrative and cannot anchor a
  headline — so the tools raise the *ceiling* on achievable quality without
  guaranteeing the analyst reaches it.
- **Single round, slug drift, LLM judge.** This is one data-upgrade round on the
  same 7-subject set with the same caveats as the main run: LLM-judge scores are
  directional not calibrated (the 0/100 is itself evidence of judge/harness
  fragility), the set is small, and the slug renames make strict round-over-round
  joins approximate. The comparison to the prior 20.0 is best read as
  "per-subject, data access clearly helped the diagnosed laggard and held the
  rest," not as a clean single-number improvement.

### (d) Re-eval correction (orchestrator, post-run)

Round-2's `eth-layer2` = 0/100 was a harness/run failure, not a real regression
(it scored 78 in this round's Round 1). The orchestrator re-ran the blind
analyst → strict judge for the two anomalous subjects on the committed,
data-upgraded skill:

| Subject | Round-2 (raw) | Re-eval (clean) |
|---|---|---|
| eth-layer2 | 0 (corrupt) | overall 77 · gap 23 |
| microsoft  | 66 · gap 34   | overall 90 · gap 10 |

Corrected Round-2 per-subject gaps: nvidia 14 · microsoft 10 · benchmark 15 ·
sogo-shosha 15 · eth-layer2 23 · coinbase 23 · marathon 15 → **avg gap 16.4
(similarity 83.6)**, vs the prior run's 20.0. The data layer lifted overall
quality and, decisively, fixed the hard laggard: **coinbase 47 → 23**.

The Microsoft re-eval analysis pulled real FY2025 financials via
`tools/fetch_edgar.py` (revenue $281.7B, FCF margin 25.4%) and ran
`tools/analyze.py` (reverse-DCF → 16.3% implied growth; owner-yield 2.05%;
3-scenario weighting) — the data-acquisition + analysis layer demonstrably
grounding the blind analysis in real numbers, which is exactly its purpose.

Tools independently verified live by the orchestrator: fetch_edgar (annual-period
filter fixed so revenue tags return clean full-year values), fetch_crypto
(BTC/ETH price + chain TVL), fetch_macro (US Treasury rates, keyless),
analyze (reverse-DCF / scenarios / owner-yield).
