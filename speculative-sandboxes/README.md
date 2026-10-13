# Acceptance-aware speculative sandboxes: Cambridge companion

**Scope:** A self-contained sidecar to the Cambridge SRG talk, not a change to the canonical 57-slide deck, preregistration, or reported experiments.

- **PDF:** [`acceptance-aware-forkable-compute.pdf`](acceptance-aware-forkable-compute.pdf)
- **LaTeX:** [`main.tex`](main.tex)
- **Speaker insert:** [`SPEAKER-INSERT.md`](SPEAKER-INSERT.md)
- **Math verification:** [`verify_math.py`](verify_math.py)

## Argument

A useful sandbox continuation needs explicit state semantics and fidelity, private divergence, non-inherited publication authority, external-effect discipline, and an economic comparison against the **warm** alternative. Acceptance-aware speculation then allocates forks using calibrated conditional *verifier* success, not LLM confidence or the total-variation acceptance theorem for exact token samplers. Correlated failures reduce the value of duplicate branches; selection affects statistical coverage. The controller records all outcomes and only promotes exact, verified artifacts. The numerical reducer may pool common-target estimates only when information and covariance are justified, otherwise it abstains.

## Evidence status

- **PUBLISHED mathematics:** TV/maximal coupling, Gaussian special-case overlap identity, elementary conditional success and submodularity, GLS, Gaussian selection illustration.
- **BUILT elsewhere:** the reference evidence-aware reducer rejects declared duplicate evidence IDs and transports lineage; existing artifact-bound gates are narrower than the full proposed controller.
- **DESIGN:** calibrated acceptance scheduler, fork-DAG covariance model, verifier-integrated ledger, epoch-fenced promotion, and exploratory Phase D comparison.
- **NOT CLAIMED:** a working speculative sandbox scheduler, restored process-memory fidelity, measured end-to-end acceleration, proven independent sibling evidence, or statistical coverage after adaptive selection.

The existing [`PREREGISTRATION.md`](../PREREGISTRATION.md) and [`CLAIM-FENCE.md`](../CLAIM-FENCE.md) remain authoritative; do not silently replace H1/H2 or interpret their unrun experiments as results.

## Reproduce

From this directory:

```sh
python3 verify_math.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -jobname=acceptance-aware-forkable-compute main.tex
```

Requires a standard TeX Live install with `lmodern`, `microtype`, `mathtools`, `tikz`, `titlesec`, `balance`, `tabularx`, and `hyperref`. The committed PDF is rendered from the committed LaTeX source.

## Where it fits in the Cambridge talk

The 90-second optional Q&A bridge follows the **runtime/evidence/acceptance** chain and is not inserted into the 41:25 planned narration. Full argument and caveats are in the sidecar PDF. The talk's main chronology, fixed slide count, existing claims, and preregistered decision thresholds remain untouched.