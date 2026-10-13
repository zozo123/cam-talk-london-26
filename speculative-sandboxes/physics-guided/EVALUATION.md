# Exploratory evaluation protocol: evidence frontiers

**Status: DESIGN, NO EXECUTED EXPERIMENTS.** This is separate from, and does not change, the Cambridge `PREREGISTRATION.md` (Gate 0, H1 warm-cache economics, H2 sibling failure coupling).

## Core falsifiable thesis

Under a fixed verifier, task population, and resource budget, an evidence-frontier controller that chooses **run ahead / diversify / pair / diagnose / warm / stop** from calibrated estimates can reduce time or spend to a genuinely verified result compared with the best feasible warm-cache/worktree baseline **without relaxing accepted-artifact or issue-time effect invariants**.

## Workloads / arms

1. **Dependent sequence:** patch A -> full trusted check A -> follow-up B -> check *exact* final artifact A+B. Arms: warm sequential; warm worktree run-ahead; fixed sandbox run-ahead; cost-aware run-ahead. Record speculative B waste after rejected A and contention with verifier. This isolates whether the *sandbox backend* adds value beyond ordinary overlapping work.
2. **Root-cause search:** pinned repository defects with competing documented root-cause hypotheses. Arms: direct repair, same-family best-of-N, diverse portfolio, diagnostic-first/VOI. Exact targeted tests must be independently reviewed; agents cannot modify hidden tests or grader. Record novel hypotheses and trace the decision after failures. Include the Cambridge `CellBusy` conjunction as a candidate workload, not as an already solved demonstration.
3. **Controlled comparisons:** A and B variants with repeated noisy performance/test outcomes. Randomize order; compare paired fixed-fixture forks versus independent environments under equal budget. Estimate covariance and uncertainty from **independently created families**. Security entropy and credentials remain unique; only declared experimental fixture RNG is controlled.
4. **Negative tests:** tampered verifier identity, stale epoch, unsaved accepted bytes, checker tampering, merged artifacts not rechecked, copied secrets, observable side-effect leakage before rollback, timeout misreported as failure, and shared false-pass vulnerabilities.

## Metrics and fairness

- Primary: task-level **time to accepted exact artifact**, including setup, verification, merges, export and teardown; resource CPU/LLM seconds and dollars **per accepted task**; failed/unfinished tasks counted in denominators.
- Secondary: per-arm p50/p95 wall time; verifier queue utilization, deferred/wasted speculative compute, saved critical-path seconds, aggregate acceptance, conditional acceptance by lineage; calibration Brier/log loss and ECE on **held-out repositories and task families**.
- Validity: actual checker ID and sealed test manifest, artifact digest before and after promotion, epoch CAS outcome, all trial outcomes including censored/timeout. Hidden independent test reveals false passes; tool/network outbound effects logged at **issue time**, not at commit.
- Benchmarks: same pinned tool/model/checker versions, equal concurrency quotas, cache-temperature fairness, same hardware, randomized arm order, pre-defined inclusion criteria. Warm worktrees, restored containers and any real memory-fork mode compared only after fidelity gate. Pair within task/repo families, analyze uncertainty at family level, and publish complete cost distributions.
- Logging: record policy selection propensities (or randomized exploration arm) so selectively sampled acceptance labels are not treated as population calibration. If a complete observed-candidate propensity model is unavailable, limit claims to on-policy performance of evaluated arms.

## Criteria for refutation

- **No backend advantage:** a warm worktree gives equivalent critical-path savings at equal or lower cost.
- **No scheduling advantage:** conditional outcome predictors fail held-out calibration or diagnostic-first/adaptive policies do not beat simpler fixed choices.
- **No pairing gain:** induced covariance is zero/negative and paired comparisons do not reduce uncertainty under the actual workload.
- **No sound acceptance:** the system promotes wrong/stale bytes, bypasses actual checker, or leaks speculative external effects. Such an outcome blocks rollout regardless of performance.

**Publication claims require raw data and preregistered thresholds for confirmatory tests.** This note and its toy math do not supply those measurements.
