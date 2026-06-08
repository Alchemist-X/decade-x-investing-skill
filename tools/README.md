# tools/ — DecadeX Data & Analysis Helpers

Small, self-contained scripts that supply (and crunch) the numbers DecadeX-style research runs on. They implement the **数据获取 (data acquisition)** and **数据分析 (data analysis)** steps of the workflow.

- **Python 3 standard library only** — `urllib` / `json` / `argparse`. **No `pip install`, no third-party deps.**
- **Free and no API key required.** Every tool runs keyless. A few accept an *optional* env key purely to raise rate limits or label output — never required, never hardcoded, never committed.
- **Immutable style, robust error handling.** Functions return fresh values; failures print a specific, actionable message to stderr and exit non-zero.
- **Educational.** These reproduce a research *method*, not financial advice.

See `references/data-sources.md` (where the data comes from) and `references/data-analysis.md` (what to compute with it).

| Script | Network? | Source(s) | Optional env key |
|---|---|---|---|
| `fetch_edgar.py` | yes | SEC EDGAR | `SEC_USER_AGENT` |
| `fetch_crypto.py` | yes | CoinGecko + DefiLlama | `COINGECKO_API_KEY` |
| `fetch_macro.py` | yes | US Treasury Fiscal Data; FRED | `FRED_API_KEY` (FRED only) |
| `analyze.py` | **no** | pure compute | `DECADEX_API_KEY` (label only) |

---

## `fetch_edgar.py` — US public-company financials (SEC EDGAR)

FREE, no key. Pulls a company's reported XBRL financials from the SEC's public `data.sec.gov` API. Resolves ticker → CIK via the SEC ticker map, then fetches one metric (companyconcept). Annual (10-K, FY) values are deduped by period-end and shown newest-first.

```bash
python3 tools/fetch_edgar.py <TICKER> [--metric TAG] [--units USD] [--limit N] [--taxonomy us-gaap] [--json]
python3 tools/fetch_edgar.py --list          # list common metric tags (no network)

# Examples
python3 tools/fetch_edgar.py AAPL --metric RevenueFromContractWithCustomerExcludingAssessedTax
python3 tools/fetch_edgar.py COIN --metric NetIncomeLoss --json
python3 tools/fetch_edgar.py NVDA --metric NetCashProvidedByUsedInOperatingActivities
```

Common metric tags (any raw US-GAAP XBRL tag also works; `--list` prints them): `Revenues`, `RevenueFromContractWithCustomerExcludingAssessedTax` (current ASC-606 revenue — many firms migrated off `Revenues`), `NetIncomeLoss`, `EarningsPerShareDiluted`, `OperatingIncomeLoss`, `GrossProfit`, `Assets`, `StockholdersEquity`, `CashAndCashEquivalentsAtCarryingValue`, `NetCashProvidedByUsedInOperatingActivities` (CFO), `PaymentsToAcquirePropertyPlantAndEquipment` (CapEx), `ResearchAndDevelopmentExpense`, `CommonStockSharesOutstanding`, `WeightedAverageNumberOfDilutedSharesOutstanding`.

**For FCF:** subtract CapEx (`PaymentsToAcquirePropertyPlantAndEquipment`) from CFO (`NetCashProvidedByUsedInOperatingActivities`), then feed it to `analyze.py`.

**Optional `SEC_USER_AGENT`:** the SEC requires a descriptive User-Agent or it returns HTTP 403. A polite default is used if unset; set it to your contact info to be a good citizen:
```bash
export SEC_USER_AGENT="Your Name your.email@example.com"
```

Notes: legacy `Revenues` may stop at the year a company migrated to ASC-606 (e.g. Apple's last `Revenues` is FY2018) — that's correct, not a bug; use the ASC-606 tag instead. Invalid tickers exit 1 with a clear message.

---

## `fetch_crypto.py` — token market data + on-chain TVL (CoinGecko + DefiLlama)

FREE, no key. Price/market-cap/volume from CoinGecko; chain & protocol TVL from DefiLlama.

```bash
python3 tools/fetch_crypto.py price bitcoin ethereum          # price / mktcap / vol24h / chg24h
python3 tools/fetch_crypto.py price bitcoin --vs usd,eur      # multi-currency
python3 tools/fetch_crypto.py markets bitcoin ethereum solana # rich rows: rank, ATH, supply
python3 tools/fetch_crypto.py tvl ethereum                    # chain TVL (DefiLlama)
python3 tools/fetch_crypto.py protocol-tvl aave               # protocol TVL (DefiLlama)
python3 tools/fetch_crypto.py tvl ethereum --json            # raw JSON (works before OR after the subcommand)
```

Subcommands: `price` (simple price + mktcap + 24h vol/change), `markets` (rank/ATH/supply rows), `tvl <chain>` (chain TVL), `protocol-tvl <slug>` (single protocol TVL). Use lowercase CoinGecko ids (`bitcoin`, not `BTC`) and DefiLlama slugs (`aave`, `lido`, `uniswap`).

**Optional `COINGECKO_API_KEY`:** a free CoinGecko demo key, sent only to CoinGecko, only to raise the free-tier rate limit. HTTP 429 means you hit the public limit — wait ~60s or set the key. Bad chain/protocol names exit 1 and list valid examples.

---

## `fetch_macro.py` — interest rates & macro series (Treasury + FRED)

The Treasury path is FREE and needs **no key**; the FRED path needs a free key.

```bash
python3 tools/fetch_macro.py treasury            # latest avg interest rates across the curve (NO key)
python3 tools/fetch_macro.py treasury --raw      # same data as JSON
python3 tools/fetch_macro.py fred CPIAUCSL       # FRED series (needs FRED_API_KEY)
python3 tools/fetch_macro.py fred GDP --limit 5  # N most-recent observations
python3 tools/fetch_macro.py --help
```

`treasury` returns the latest "Average Interest Rates" on marketable & non-marketable Treasury securities (Bills/Notes/Bonds/TIPS/FRN/…) — a clean **"price of money"** proxy across the curve. `fred <SERIES>` returns the most-recent observations for any FRED series (`CPIAUCSL` CPI, `GDP`, `DGS10` 10y, `DTB3` 3M T-bill, …). Global `--timeout SECONDS` (default 30).

**`FRED_API_KEY` (FRED only):** free key from <https://fredaccount.stlouisfed.org/apikeys>. Read from the env var only — never hardcoded. Without it, the `fred` command exits cleanly (code 2) with a help message; the `treasury` command never needs it.
```bash
export FRED_API_KEY=your_key_here
```

---

## `analyze.py` — pure valuation helpers (NO network, NO key)

Deterministic DecadeX-style valuation primitives. No I/O in the math; nothing to fetch, nothing to leak.

```bash
python3 tools/analyze.py reverse-dcf --mktcap 3e12 --fcf 9e10 --discount 0.10 --tgrowth 0.03 [--years 10]
python3 tools/analyze.py scenarios [--json '[{"label":"Bear","prob":0.3,"value":100},...]'] [--price 200]
python3 tools/analyze.py owner-yield --oe 9e10 --mktcap 3e12
```

- **`reverse-dcf`** — 反向 DCF: solve for the FCF growth rate the current market cap *implies* (bisection; explicit-period growth may exceed the discount rate, only terminal growth must stay below it). Returns implied growth %, implied P/FCF multiple, convergence diagnostics. Sanity-checks whether a price's embedded expectation is plausible.
- **`scenarios`** — 三情景概率加权估值: probability-weight Bear/Base/Bull into one expectation + per-scenario upside vs `--price`. Probabilities must sum to 1.0 (a deliberate guardrail; errors otherwise). Omit `--json` to run the built-in demo.
- **`owner-yield`** — Buffett-style owner-earnings (≈FCF) yield = `owner_earnings / market_cap`, the cash-cow screen anchor (flags below the DecadeX ≥4% bar).

Output is JSON on stdout; bad input prints `error: …` to stderr and exits 2. Optional `DECADEX_API_KEY` is read for an output label only — never required, never transmitted (this tool makes no network calls).

**Typical chain:** `fetch_edgar.py` → CFO − CapEx = FCF → `analyze.py reverse-dcf` / `owner-yield`; then `analyze.py scenarios` for the banded valuation.

---

## Quick conventions

- Run from the skill root so the `tools/…` paths resolve, e.g. `python3 tools/fetch_edgar.py …`.
- All four exit non-zero on failure with a stderr message — safe to script.
- `--json` / `--raw` give machine-readable output for piping into `analyze.py` or your own notebook.
- **Educational distillation of DecadeX public methodology. Not financial advice.**
