# Claim boundaries for the Cambridge SRG seminar

This file applies to the canonical `talk.tex`: 50 story slides (no backup slides) plus untimed end matter (detail pages, research record, references).

Each evidence slide carries one or more tags:

- **MEASURED**: in the speaker's own run records.
- **BUILT**: implemented and unit-tested, or a synthetic check.
- **PROPOSED**: a design that has not been run.
- **PUBLISHED**: other people's work.

The scope caveats are said on slides 6 and 7.

## Measured: runs SELFHOST-2 and SELFHOST-3, 27 Sep 2026

**Sources**
- SELFHOST-2: PR #2351 of `zozo123/ariflow-swfactory`, `docs/factory/SELFHOST-2/`.
- SELFHOST-3: local run records. They are not published; the slide says "redacted copy on request".

**Setup of both runs**
- Both ran on Docker's sandbox (`toolset:SbxCommaPolicyBackend`), not on islo.
- The harness answered the intent and plan gates. `approvals.json` records them as `"mode": "human"`, actor `admin`.
- Leases were not exercised (`cell.json` `managed: false`).
- Nothing forked. The work graph recorded `serial_fallback_missing_fork`. The 176.7 s "with a fork" figure is a computed critical path.

**Observed on islo on 27 Sep (islo CLI 0.53.1)**
- The 403 that became the SELFHOST-2 work order (`intent.md`).
- The stdout mix that killed an earlier SELFHOST-2 attempt at setup (PR #2348).

**SELFHOST-2**
- Repair 1 (`agent/fix.4.json`) had no shell tool and did not run the tests. It changed `src/swfactory/backend/service.py`, which is outside the plan.
- Review 1 returned `request_changes` with a blocker. Repair 2 (`fix.5.json`) could not edit `tests/` (hook-protected) and refactored.
- Review 2 returned `approve`. The out-of-plan file stayed "major", and "untested" was downgraded to minor.
- The harness ran the full suite after each repair (`stages.py` re-runs tests after a review fix): 1,972 tests including skips, 0 failures.
- The new CellBusy-adoption branch "lands with no test in the diff" (review 2). Its only coverage is the race, which reaches it "only when the interleaving happens to lose an activation".
- The test hook never fired: 15 edits, all allowed.
- All four steps used the same hosted model.
- `cycle_s` 2557.5 (about 43 min). Total $10.33.
- The speaker reverted the out-of-plan change by hand in PR #2351. **#2348–#2351 are open, not merged.**

**SELFHOST-3**
- 1,981 tests passed first time, and review approved.
- Delivery was refused three times with "files outside the reviewed commit stream". The stray file was the harness's own review-diff archive.
- Teardown followed, and no PR was produced. Cost $3.43. Wall clock was about 26 min; stage time was 853.8 s.

**Other measured facts**
- Repairs are recorded without a scope check: `work_stage.py`, the non-node branch.
- The CI job `evals-islo` in Actions run 36423283572 passed in 3 s with its real step skipped.
- The allowlist appears in five places (`demo/selfhost-2.md`).

## Built

- The evidence-aware reduction contract and reference reducer: Eliaz, arXiv:2607.09689.
  - **Title:** the arXiv listing says "Evidence-Aware MapReduce for Forkable Compute". The v4 PDF's first line says "Evidence-Aware Reduction". Slides cite the paper by ID.
- **Built:**
  - an associative merge of numeric summaries;
  - a repeated evidence ID stops the merge (it raises);
  - lineage travels with the result, but nothing consumes it yet.
- **Proposed:**
  - one execution per evidence ID, so a retry is never counted twice;
  - abstention when dependence is unknown;
  - a controller-derived precision.
- **Measured** (paper):
  - the trace: a named 141 MB islo snapshot and 4 concurrent restore–run–capture round trips, 6.70 s in total, measured by the client; pooled mean 4.9422 vs full-sample 4.9450;
  - Table 2: islo p50 6.87 s, p95 9.04 s, 255 of 256 succeeded at concurrency 12, with per-op teardown excluded from the percentiles.
  - These are API round trips, not a mechanism latency or a vendor ranking.
  - Whether the snapshot includes memory is **unverified**, so the talk says "restore fan-out".
- The forged-precision result (17.0004 vs 4.9566) is a **synthetic** check. The forgery is in the information per point, so measuring n alone does not stop it. The heuristic is not a Byzantine guarantee.
- The logistic check was not compared with sample-size weighting.

## Proposed

- The gateway authenticates the child, re-minted on restore.
- A scope check in the repair loop.
- An evaluator outside the cell.
- Epoch-fenced promotion.
- A controller-measured n.
- Replay logs.
- The redesigned SELFHOST-2 on slide 54.
- The runtime interface on slide 33, except `checkpoint` (islo named snapshots exist), `reduce` (merge and evidence check built) and `promote` (sha256-bound gate built; the epoch fence is proposed).
- The TLA+ promotion model (formal/authority) is a design model; no TLC run or trace check is recorded.
- The whole protocol in `PREREGISTRATION.md`. No result from it is claimed until it runs.

## Published

- Dean & Barroso, CACM 2013: hedged request after 10 ms; 99.9th-percentile latency for 1,000 BigTable keys from 1,800 ms to 74 ms with 2% more requests; "the source of latency is often not inherent in the particular request".
- Brown et al., arXiv:2407.21787: SWE-bench Lite 15.9% (1 sample) to 56% (250 samples); majority voting and reward models plateau without automatic verifiers.
- Stroebl, Kapoor & Narayanan, arXiv:2411.17501 (current title *The Limits of Inference Scaling Through Resampling*; v1 was *Inference Scaling fLaws*): imperfect verifiers cap repeated-sampling gains; when false positives have negative utility, the best number of attempts is often under 10. Say the condition.
- Slide 2's independence condition is Dean & Barroso's own: the techniques work only when the cause of variability does not hit several replicas at once. It is about latency, not failure; the close generalises it. Correlated wrong answers: Kim et al., ICML 2025.
- Slide 25 lists published runtime operations with their endpoints. It is not a ranking. The run figures (slide 10) come from a run record (SELFHOST-2 metrics.json), not a paper.
- Slide 10 stage times are of the 2,557.5 s cycle (metrics.json): intent, specification and plan 3:41, build and test 20:01, review 18:55. Setup is 20.3 s (operations.jsonl).
- Blackburn et al., arXiv:2206.02871 (Eliaz 3rd of 9): most bitcoin from 3 Jan 2009 to 9 Feb 2011 was mined by 64 agents (address linking >99% sensitivity and specificity). Used as a motivating example of dependence uncovered from outside, not as evidence about forks. Say "my co-authors and I", not "I".
- Saurty-Seerunghen et al., iScience 2026 (Eliaz 3rd of 7): malignant cells cluster by patient tumour, non-malignant cells by cell type. The patient was known metadata; this is dependence structure, not a recovered hidden label.
- Eliaz et al. PRE 2020 is about linker valency (multilinkers), not branching. Liman et al. PNAS 2020 and Li et al. JPCB 2021 are about Arp2/3 branching and avalanches. None says branching sets global connectivity or that whole networks collapse together. The PhD also covered Hi-C loops and protein-folding hydrodynamics.
- Hitz et al. 2023 (ENCODE pipelines): data files, reference genome versions, software versions and parameters are captured in the ENCODE Portal.

- Every system named on a story slide is cited on that slide's source line, and the three References end-matter pages collect them with the documentation used.
- Live migration (Clark et al., NSDI'05): 60 ms downtime for a Quake 3 server. Nephele (Lupu et al., EuroSys'23): no figure quoted.
- DeltaBox: the slides use the evaluation checkpoint figure (10.83 ms on slide 25). The abstract's 14 ms / 5 ms are not used.
- Kimi K3 (Moonshot AI), §5.3.2:
  - checkpoint and resume are "as low as" 133 ms and 49 ms;
  - 51.2M sandboxes counts all K3 runtimes, across training and evaluation;
  - fork is offered "for reward judging without side effects".
- METR (Von Arx, Chan & Barnes): 30.4% on RE-Bench vs 0.7% on HCAST. Scorer visibility is METR's leading guess (difficulty and scaffolding also differ), not a controlled variable.
- Kim, Garg, Peng & Garg, ICML 2025 (PMLR 267), arXiv:2506.07962: on HELM (71 models, MMLU, four options), when two models both miss a question they pick the same wrong answer 60% of the time on average, against 33% by chance, and 97.5% of pairs are above chance; on the HuggingFace leaderboard (349 models) it is 42% against 13%. More accurate models share more errors, even across providers and architectures. These are different models, not forks or repeated runs of one model, and the 60% is a conditional agreement rate, not a correlation ρ.
- Kohli, arXiv:2605.29800 (2026 preprint): 9 frontier judges from 7 model families carry about 2.2 independent votes (Kish n_eff 2.18, 95% CI 2.07–2.31), with a ceiling of about 2.6 however many judges are added; the panel never beat the best single judge beyond noise; when all 9 agreed they were still wrong 9.1% of the time.
- Chen, arXiv:2606.27288 (2026 preprint): any vote, router or best-of-N that returns one member's answer is capped at 1 − β, where β is the rate at which all members are wrong together; average pairwise correlation cannot identify β. Quote only this ceiling: the paper's other numbers are internally inconsistent.
- Jo, Garg & Raghavan, arXiv:2602.24086 (2026 preprint; Garg is Kim et al.'s senior author): much of the "excess" agreement shrinks once the baseline accounts for question difficulty, and the measured monoculture depends on the baseline and on which models are compared. That errors are shared stands; how much is beyond difficulty is contested. For counting witnesses, total shared failure is what matters.
- Goel et al., ICML 2025, arXiv:2502.04313: AI judges favour models similar to themselves, beyond accuracy. No number quoted.
- Bone, Stephany & del Rio-Chanona, arXiv:2609.22169 (2026 preprint): post-training makes models from different vendors agree more; near-unanimous hiring exclusion rises from 5.6% (base models) to 17.3% (post-trained). The arXiv PDF header says COLM 2026; cite it as a preprint until the proceedings are out.
- None of these measures forks of one agent from a shared snapshot, or multi-step agent runs. That gap is what Test 2 measures.
- LightVM is NEC Labs work, not SRG work.

Added with the one-story restructure:

- Kimi K3 §5.3.2: 51,219,741 sandboxes "across" (not "over") 1,505,678 images; memory overcommit "up to 6.5×" in real workloads, from copy-on-write memory plus page-cache optimisations together. It does not measure the shared part alone.
- Kimi K3 §4.1.2: partial rollout at a fraction λ; verbosity control. §4.2.4: the hacking-detection quote (CUDA graph replay, input caching, precision reduction). §4.2.6: evaluation of final environment state "rather than the agent's self-reported completion"; public diagnostic verifiers paired with hidden held-out ones.
- Kimi forks a sandbox, not the judge: fork is "useful for reward judging without side effects".
- DeepSeek-V4 §5.2.5 (DSec): hundreds of thousands of concurrent sandboxes per cluster; when a training task is preempted the sandbox is retained, and on resumption DSec replays cached results. The sandbox itself is not preempted.
- Dean & Barroso: each server's 99th percentile is 1 s, so one request in 100 is slow on each server; a 100-way fan-out makes 63% of requests slow. Not "one slow server". Canary requests (one or two leaf servers first); mutations go to quorum algorithms such as Paxos.
- Dorfman, Ann. Math. Stat. 14:436 (1943): group testing.
- Poolkeh (Eliaz, Danovich & Gasic, medRxiv 2020): a SIR-D model plus a nested pooling strategy, a model only, no laboratory pooling. Israel, ~9M people, 295,951 tests, s1 = 92, s2 = 10, 30-fold fewer. Say "my co-authors and I modelled", never "I pooled".
- OffRisk (Barkai, Malul, Eliaz et al., Bioinformatics Advances 3:vbad138, 2023; Eliaz 3rd of 5): a Docker image that annotates CRISPR off-target sites and labels their risk. Used as an analogy for a scope check.
- Gilad, Eliaz et al., Commun. Biol. 4:399 (2021), Methods: at least four technical replicates per viability point, at least two independent experiments per plot.
- Li et al., JPCB 2021: loosely connected clusters "may collapse suddenly when driven by motors". Liman et al., PNAS 2020: avalanches "reminiscent of" experimental cytoquakes. Neither defines a cytoquake as a failure.
- Stockmayer (J. Chem. Phys. 11:45, 1943): gelation, an analogy only, under idealised assumptions.
- Amdahl: 100 cores with 10% serial give 9.2×; reading ρ as a serial fraction is the speaker's interpretation.
- The 1-in-10 race loss rate behind "29 greens" is illustrative, not measured.

## Statistical scope

- The variance floor assumes equal variances and a common pairwise correlation.
- Lineage names the shared factors; it does not estimate their strength.
- Precision pooling requires one common parameter, calibrated information and independent evidence.
- On slides 47 and 48, θ is one candidate's quantity. Choosing among candidates is a separate selection problem.
- Lineage labels shared parents, seeds, tests and fixtures. It cannot label a shared model's blind spots.

## Do not say

- That any self-authored PR was merged.
- That a person answered the gates.
- That the runs used islo.
- That the factory forks today.
- That fork is faster than a good build cache.
- That the speaker's PhD was only on branched networks, or that the papers show whole networks collapsing together.
- "I recovered" for the Bitcoin or iScience results: they are team results.
- That nine forks were run or came back green: the nine candidates on slide 37 and the nine repair samples on slide 53 are hypothetical or proposed.
- That Poolkeh pooled real samples: it is a model.
- That clusters or networks "collapse together": say "may collapse suddenly".
- That Kimi forks its reward judge: it forks a sandbox for judging.
- That Kim et al. measured forks or repeated runs of one model.
- That 60% is a correlation ρ.
- That the follow-up preprints are peer reviewed.
- That SELFHOST-2 or SELFHOST-3 ran on the speaker's own sandbox platform (they ran in Docker Sandboxes through Airflow's sandbox toolset).

Models were served through Databricks; that may be named. Name no model vendor or endpoint.

The slides do not name the speaker's sandbox platform (speaker's choice); the disclosure stays in generic form.

Do not say:
- that repair 2 was never tested (the suite ran after it);
- that promotion is model-checked;
- that the built reducer abstains;
- that any islo snapshot is a memory fork before Gate 0 is resolved;
- that nothing escaped. Say "nothing was pushed and nothing was denied".
