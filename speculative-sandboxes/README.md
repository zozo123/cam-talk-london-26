# Speculative Sandboxes for Agentic Development

**Cambridge SRG companion | follow-up to merged [PR #19](https://github.com/zozo123/cam-talk-london-26/pull/19).**

The research question is **when to fork, which alternative to verify, when to abandon a family of speculative branches, and what evidence justifies promotion**. The strongest design includes **no fork** as an explicit choice whenever an equivalent warm-cache/worktree strategy wins or the fork fails admission gates.

## Artifacts

| File | Purpose |
|---|---|
| [`acceptance-aware-forkable-compute.pdf`](acceptance-aware-forkable-compute.pdf) | Final 5-page mathematical and systems companion. |
| [`physics-guided/`](physics-guided/README.md) | **Evidence Frontiers:** four-page physics-guided follow-up on committor/value-of-information scheduling, paired experiments, and a trusted evidence frontier (LaTeX + PDF + equation audit). |
| [`main.tex`](main.tex) | Reproducible LaTeX source. |
| [`reference.py`](reference.py) | Executable, deterministic **finite-world mock** of admission, conditional-acceptance scheduling, receipts and one-time promotion. |
| [`test_reference.py`](test_reference.py) | Behavioral tests: safety gates, warm baseline, identical siblings, negative evidence, timeouts, forged receipts, stale epochs and intentionally weak verifier. |
| [`verify_math.py`](verify_math.py) | Independent numerical checks for mathematical equations and examples. |
| [`SPEAKER-INSERT.md`](SPEAKER-INSERT.md) | Optional 90-second Cambridge talk/Q&A bridge (does not alter the main deck). |
| [`Makefile`](Makefile) | `make check`, `make pdf` and `make clean` recipes. |

## Thesis, without conflating distinct results

1. **Admission is a hard gate, economics is a subsequent optimization.** Check state semantics, restore fidelity, private writes, authority, issue-time effects and warm-cache comparison. A snapshot API or fast launch is not automatically a safe, useful fork.
2. **Drafting is not acceptance.** Exact speculative decoding has an acceptance theorem `alpha=1-TV(p,q)` because its target/proposal distributions and correction rule are known; patch-test pass probability must be estimated and **does not equal semantic correctness**.
3. **Choose marginal verified progress, not raw worker count.** `P(any pass)=1-prod_i(1-P(A_i | earlier failures, H))` handles arbitrary correlation via conditional probabilities. For a fixed set, union-of-success coverage is monotone submodular; **adaptive** scheduling requires assumptions and measurement.
4. **The verifier cannot be inside the child.** A controller-authenticated receipt binds exact artifact bytes, evaluator/version and epoch. A passing test still proves only what it checked. Speculative tool calls that disclose data must be governed **before** dispatch; rollback cannot unsend information.
5. **Passing forks are not independent statistical evidence.** Evidence-ID deduplication and lineage are necessary but insufficient to infer covariance or repair adaptive selection bias. Where covariance and selection assumptions are unjustified, abstain from increased precision.

## Run the reference and audit the equations

```sh
cd speculative-sandboxes
make check             # Python stdlib: independent equations + 19 behavioral tests
make pdf               # LaTeX -> compiled PDF (requires TeX Live packages)
```

Or without make:

```sh
python3 verify_math.py
python3 -m unittest -v test_reference.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -jobname=acceptance-aware-forkable-compute main.tex
```

The TeX dependencies are `lmodern`, `microtype`, `geometry`, `mathtools`, `booktabs`, `tabularx`, `enumitem`, `xcolor`, `tikz`, `titlesec`, `balance`, and `hyperref`. Compile with `pdflatex`/`latexmk` in this directory; no external images are required. Check that the output is five pages and has no overfull boxes or unresolved citations. Rendered pages have been inspected.

### Equation audit coverage

`verify_math.py` checks TV/residual-correction mass, the equal-covariance Gaussian overlap by **independent numerical integration** and KL identity, the correlated-success chain rule in a finite joint distribution, the beta-binomial example, exhaustive fixed-set submodularity, expected prefix survival, generalized least squares/`K_eff`, post-selection coverage/Bonferroni threshold, and warm-vs-fork cost algebra. The associated tests are synthetic and do **not** constitute empirical validation of an agent probability model.

### What the reference really implements

- `ForkGates` refuses admissibility if any stated hard gate fails; `WorkCosts` compares a simplified *total work-cost* model against a warm baseline; this is not a latency benchmark.
- `FiniteWorldScheduler` represents hypothetical *joint* success events as subsets of sixteen possible worlds. It can replan exactly after observed failures; a model trained on real traces cannot assume this oracle.
- `TrustedController` persists bytes, invokes an externally supplied verifier predicate, creates HMAC-authenticated receipts and accepts an exact matching artifact once per epoch. HMAC, the in-memory store and the check predicate are a **protocol mock**, not proof of durable atomicity, isolation, receipt attestation, or verifier completeness.
- Tests demonstrate a *false passing test* on deliberately wrong code, thereby proving the code **does not claim** semantic correctness from a pass.

The measured Cambridge factory run was **serial** and did **not** demonstrate this integrated forked runtime. The original evidence-aware reducer in [arXiv:2607.09689](https://arxiv.org/abs/2607.09689) rejects declared duplicate evidence IDs and transports lineage; it does **not** already estimate covariance or correct for winner selection.

## Claim boundaries and experiments

**PROVEN mathematical identities:** TV/maximal coupling, conditional chain rule, submodular *fixed-set* success coverage, Gaussian overlap special case, GLS under justified covariance and post-selection Gaussian calculation.

**BUILT IN THIS PR:** reproducible toy controller, numerical equation audit, negative behavioral tests, standalone LaTeX and compiled PDF. No real provider integration.

**DESIGN:** calibrated conditional acceptance model, adaptive fork execution, controller-owned verifier/ledger on islo or an equivalent backend, issue-time egress contract, epoch-fenced atomic publish, covariance model and selection-aware confidence.

**NOT CLAIMED:** real live-memory fork semantics, a speedup over warm caches, reliable semantic correctness from green tests, a fitted acceptance predictor, independent sibling errors, validated covariance or guaranteed confidence after adaptive search.

The existing [`PREREGISTRATION.md`](../PREREGISTRATION.md) (Gate 0, fidelity, H1 warm-cache and H2 sibling failure coupling) remains unchanged. The companion's **Phase D** is a separate *exploratory proposal*; no result is relabelled preregistered or measured. Compare warm serial, fixed fan-out, acceptance-only and lineage-aware controllers on pinned tasks and equal budgets, including explicit no-fork controls, negative failures, calibrated log-loss/Brier, exact artifact p50/p95 latency and CPU/dollar cost per verified success.

## Cambridge placement

The sidecar complements the existing **runtime -> evidence -> acceptance** arc. The optional speaker insert fits after the runtime/evidence boundary or in Q&A; it does not change the existing 57-slide/41:25 main narration, `talk.tex`, `CLAIM-FENCE.md`, or the preregistered acceptance/rejection thresholds.