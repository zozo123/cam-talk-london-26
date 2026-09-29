# Claim boundaries for the Cambridge SRG seminar

This file applies to the canonical `talk.tex`: 27 main slides plus backups.

Each evidence slide carries one tag:

- **MEASURED**: in the speaker's own run records.
- **BUILT**: implemented and unit-tested, or a synthetic check.
- **PROPOSED**: a design that has not been run.
- **PUBLISHED**: other people's work.

The caveats are said once, on slide 3.

## Measured: runs SELFHOST-2 and SELFHOST-3, 27 Sep 2026

Source: `zozo123/ariflow-swfactory`, `.factory/evidence/`.

**Setup of both runs**
- Both ran on Docker's sandbox (`toolset:SbxCommaPolicyBackend`), not on islo.
- The harness answered the intent and plan gates. `approvals.json` records them as `"mode": "human"`, actor `admin`.
- Leases were not exercised (`cell.json` `managed: false`).
- Nothing forked. The work graph recorded `serial_fallback_missing_fork`.

**SELFHOST-2**
- Repair 1 (`agent/fix.4.json`) had no shell tool and did not run the tests. It changed `src/swfactory/backend/service.py`, which is outside the plan.
- Review 1 returned `request_changes` with a blocker. Repair 2 (`fix.5.json`) could not edit `tests/` (hook-protected) and refactored.
- Review 2 returned `approve`, with the out-of-plan file still reported as "major".
- All four steps used the same hosted model.
- Final head: 1,972 tests, 0 failed. `cycle_s` 2557.5 (about 43 min). Total $10.33.
- The speaker reverted the out-of-plan change by hand in PR #2351. **#2348–#2351 are open, not merged.**

**SELFHOST-3**
- 1,981 tests passed first time, and review approved.
- Delivery was refused three times with "files outside the reviewed commit stream". The stray file was the harness's own review-diff archive.
- Teardown followed, and no PR was produced. Cost $3.43, cycle 853.8 s.

**Other measured facts**
- Repairs are recorded without a scope check: `work_stage.py`, the non-node branch.
- The CI job `evals-islo` in Actions run 36423283572 passed in 3 s with its real step skipped.
- The allowlist appears in five places (`demo/selfhost-2.md`).

## Built

- The evidence-aware reduction contract and reference reducer: Eliaz, arXiv:2607.09689.
  - **Title:** the arXiv listing says "Evidence-Aware MapReduce for Forkable Compute". The v4 PDF's first line says "Evidence-Aware Reduction". Slides cite the paper by ID.
- The trace:
  - a named 141 MB snapshot and 4 concurrent restore–run–capture round trips, 6.70 s in total, measured by the client;
  - pooled mean 4.9422 vs full-sample 4.9450.
- Paper Table 2: islo p50 6.87 s, p95 9.04 s, 255 of 256 succeeded at concurrency 12. These are API round trips, not a mechanism latency or a vendor ranking.
- The forged-precision result (17.0004 vs 4.9566) is a **synthetic** check. The heuristic is not a Byzantine guarantee.
- The logistic check was not compared with sample-size weighting.

## Proposed

- The gateway authenticates the child, re-minted on restore.
- A scope check in the repair loop.
- An evaluator outside the cell.
- Epoch-fenced promotion.
- A controller-measured n.
- Replay logs.
- The redesigned SELFHOST-2 on slide 25.
- The whole protocol in `PREREGISTRATION.md`. No result from it is claimed until it runs.

## Published

- Every system on slides 12–16 and in the backups is cited to its paper or docs.
- DeltaBox: slide 12 quotes the abstract figures (14 ms / 5 ms), and slide 15 quotes the evaluation figures (10.83 ms / 1.86 ms).
- Kimi K3 quotes are from §5.3.2 of its technical report.

## Statistical scope

- The variance floor assumes equal variances and a common pairwise correlation.
- Lineage names the shared factors; it does not estimate their strength.
- Precision pooling requires one common parameter, calibrated information and independent evidence.
- On slide 22, θ is one candidate's quantity. Choosing among candidates is a separate selection problem.

## Do not say

- That any self-authored PR was merged.
- That a person answered the gates.
- That the runs used islo.
- That the factory forks today.
- That fork is faster than a good build cache.

Also, do not name the hosted model provider or endpoint on stage.
