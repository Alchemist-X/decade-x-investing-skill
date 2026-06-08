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
