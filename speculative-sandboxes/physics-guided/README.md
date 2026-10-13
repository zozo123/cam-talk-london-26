# Evidence Frontiers — Physics-Guided Speculative Sandboxes

**Cambridge research companion** by Yossi Eliaz; an isolated follow-up to the merged [Speculative Sandboxes PR #20](https://github.com/zozo123/cam-talk-london-26/pull/20) and the [evidence-aware reduction paper](https://arxiv.org/abs/2607.09689).

> **Speculate on execution, not on the authority to declare success.**
>
> The best fork may be a cheaper diagnostic, a dependent run-ahead, a genuinely different hypothesis, or a paired experimental control. It may also be **no fork**.

## Deliverables

- [**Evidence Frontiers (PDF)**](evidence-frontiers.pdf) — four-page theoretical and systems companion, with derived equations, references, a runnable audit, a concrete runtime contract, and falsifiable experiments.
- [**LaTeX source**](main.tex) — self-contained two-column document.
- [**Independent equation audit**](verify_equations.py) — Python standard library; arithmetic, discrete examples, committor, change of measure, overlap and value of information.
- [**Evaluation protocol**](EVALUATION.md) — separate exploratory follow-up; **does not modify** the Cambridge preregistration.
- [**Review record**](FIVE-PASS-REVIEW.md) — actual substantive and production QA checks.

## One idea, three fork uses

| Fork use | What the runtime optimizes | What must not be conflated |
| --- | --- | --- |
| **Run ahead** | Hide verifier latency by drafting a dependent continuation before its parent is verified | An unverified descendant cannot advance the trusted evidence frontier |
| **Diversify** | Improve probability that at least one independent *failure mode* can produce a valid result | More same-family branches do not imply more coverage or information |
| **Pair** | Compare changed treatments under matched executable conditions to cancel shared noise | Paired evidence for **differences** is not independent evidence about a population mean |

### Decision logic (design, not measured)

```text
Pin verified work-order + checkpoint + policy + verifier + epoch
If state, fidelity, identity, authority or issue-time-effects gate fails:
    use an admissible warm / non-fork execution mode
Else choose among:
    diagnostic test | run ahead | diverse candidate | paired comparison
    warm worktree | verify now | stop
Use predicted critical-path savings, calibrated conditional success,
value of information and shared verifier load; do not assume independence.
Run in private workers; record passed, failed, censored and untested branches.
Externally check exact returned artifact bytes and dependency receipts.
Advance evidence only over checked edges; reject stale epoch and publish once.
```

**Research inspiration, not claimed invention:** EAGLE-2/OPT-Tree optimize draft structures for expected acceptance; the committor from transition-path theory predicts eventual success; adaptive multilevel splitting reuses promising prefixes; paired simulation with common random numbers removes environmental noise; decision theory prices diagnostic information. **Sherlock already executes workflow descendants while verification runs**; the novelty to test is *experiment selection + forkable executable state + coupled, auditable evidence and authority*. No unconditional priority claim is made.

## Reproduce

```bash
cd speculative-sandboxes/physics-guided
python3 verify_equations.py
latexmk -pdf -interaction=nonstopmode -halt-on-error \
    -file-line-error -jobname=evidence-frontiers main.tex
```

Requirements: Python 3 standard library, `latexmk`, `pdflatex` and common TeX Live packages (Latin Modern, microtype, geometry, amsmath/mathtools, booktabs/tabularx, enumitem, TikZ, titlesec, hyperref). The paper does not require network access or external figures.

## Claim fence

**Mathematically established under stated assumptions:** exact total-variation overlap for token speculation; accepted-prefix tail sum; finite Markov committor/Doob transform; nested-level probability identity and change of measure; paired difference variance; static fixed-set submodular coverage; simple VOI and idealized crossover inequalities.

**Built in this folder:** LaTeX paper, compiled PDF, auditable arithmetic/finite-world test script and experimental protocol. The [previous reference controller](../reference.py) remains a toy with assumed finite-world branch outcomes.

**Research design, not built or measured:** live forkable speculative agent pipeline, external checker integration, trained committor/VOI policy, experimental-control scheduler, true covariance calibration, correct adaptive selection inference and verified speedups.

**Not claimed:** Sherlock-style verification overlap is novel; a token TV formula proves software correctness; shared forks are independent measurements; an HMAC toy is a production attestation system; copied memory undoes external effects; a fixed-seed test RNG may be reused as a security identity; or the existing 57-slide Cambridge deck includes this new theory.

The original [`PREREGISTRATION.md`](../../PREREGISTRATION.md) and [`CLAIM-FENCE.md`](../../CLAIM-FENCE.md) retain their original thresholds and status. If a follow-up experiment is preregistered later, it must be separately timestamped, not retroactively appended to H1/H2.
