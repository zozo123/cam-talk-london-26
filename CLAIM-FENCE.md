# Claim boundaries for the Cambridge SRG seminar

This file applies to the canonical `talk.tex`: **41 main frames in six acts, no appendix and no overlays**. Historical end-matter is preserved as bibliography in `REFERENCES.md`, outside the deck.

Each evidence slide carries one or more tags:

- **MEASURED**: in the speaker's own run records.
- **BUILT**: implemented and unit-tested, or a synthetic check.
- **PROPOSED**: a design that has not been run.
- **PUBLISHED**: published source results, including co-authored studies.

Scope boundaries attach to the relevant claims and are summarized here; this document uses titles and artifacts instead of fragile slide numbers.

## Measured: runs SELFHOST-2 and SELFHOST-3, 27 Sep 2026

**Sources**
- SELFHOST-2: PR #2351 of `zozo123/ariflow-swfactory`, `docs/factory/SELFHOST-2/`.
- SELFHOST-3: local run records. They are not published; the slide says "redacted copy on request".

**Setup of both runs**
- Both ran on Docker's sandbox (`toolset:SbxCommaPolicyBackend`), not on islo.
- The harness answered the intent and plan gates. `approvals.json` records them as `"mode": "human"`, actor `admin`.
- Sandbox authority leases were not exercised (`cell.json` `managed: false`); dispatch coordination leases are a separate mechanism.
- Nothing forked. The work graph recorded `serial_fallback_missing_fork`. The 176.7 s "with a fork" figure is a computed critical path.

**Observed on islo on 27 Sep (islo CLI 0.53.1)**
- The 403 that became the SELFHOST-2 work order (`intent.md`).
- The stdout mix that killed an earlier SELFHOST-2 attempt at setup (PR #2348).

**SELFHOST-2**
- Repair 1 (`agent/fix.4.json`) had no shell tool and did not run the tests. It changed `src/swfactory/backend/service.py`, which is outside the plan.
- Review 1 returned `request_changes` with a blocker. Repair 2 (`fix.5.json`) reported that `tests/` were protected and refactored. No blocked edit attempt is recorded; the hook never fired.
- Review 2 returned `approve`. The out-of-plan file stayed "major", and "untested" was downgraded to minor.
- The harness ran the full suite after each repair (`stages.py` re-runs tests after a review fix): 1,972 tests including skips, 0 failures.
- The new CellBusy-adoption branch "lands with no test in the diff" (review 2). Its only coverage is the race, which reaches it "only when the interleaving happens to lose an activation".
- The test hook never fired: 15 edits, all allowed.
- All four steps used the same hosted model.
- Recorded stages total **2,557.517 s (42:37.517)**; timestamps give **43:44 wall time**. Total **$10.327824**.
- Two repair and two review sessions total **1,514.087 s (25.235 min)** and **$7.74846**: **59.201%** of recorded stage time and **75.025%** of run cost. Session durations include agent/tool activity, not pure inference.
- Initial setup was **20.3 s**, about **0.794%** of stage time. A 100-fold improvement would save about 20.1 s.
- Serial edit nodes total **342.579 s**; computed critical path **176.689 s**; difference **165.890 s**, excluding fork, merge, contention, and verification overhead. Worktrees could support the file-level schedule.
- The speaker reverted the out-of-plan change by hand in PR #2351. No merge is claimed.

**SELFHOST-3**
- The second work order reported suite count **1,981**, zero failures, and review approval. Raw records are unpublished; do not upgrade a reported suite count into a confirmed all-passed count.
- Delivery was refused three times with "files outside the reviewed commit stream". The stray file was the harness's own review-diff archive.
- Teardown followed, and no PR was produced. Cost $3.43. Wall clock was about 26 min; stage time was 853.8 s.

**Other measured facts**
- Repairs are recorded without a scope check: `work_stage.py`, the non-node branch.
- The CI job `evals-islo` in Actions run 36423283572 passed in 3 s with its real step skipped.
- The allowlist appears in five places (`demo/selfhost-2.md`).

## Built

- The evidence-aware reduction contract and reference reducer: Eliaz, arXiv:2607.09689.
  - **Current v4 title:** *Evidence-Aware Reduction for Forkable Compute*. Earlier metadata used *Evidence-Aware MapReduce for Forkable Compute*; cite arXiv:2607.09689v4 for the current title.
- **Built:**
  - an associative merge of numeric summaries;
  - a repeated evidence ID stops the merge (it raises);
  - lineage travels with the result, but nothing consumes it yet.
- **Proposed:**
  - evidence identities tied to underlying observations, so declared reuse is never counted twice;
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
- The redesigned SELFHOST-2.
- The runtime interface, except `checkpoint` (islo named snapshots exist), `reduce` (merge and evidence check built) and `promote` (sha256-bound gate built; the epoch fence is proposed).
- The TLA+ promotion model (formal/authority) is a design model; no TLC run or trace check is recorded.
- The whole protocol in `PREREGISTRATION.md`. No result from it is claimed until it runs.

## Published

- Dean & Barroso, CACM 2013: hedged request after 10 ms; 99.9th-percentile latency for 1,000 BigTable keys from 1,800 ms to 74 ms with 2% more requests; "the source of latency is often not inherent in the particular request".
- Brown et al., arXiv:2407.21787: SWE-bench Lite 15.9% (1 sample) to 56% (250 samples); majority voting and reward models plateau without automatic verifiers.
- Stroebl, Kapoor & Narayanan, arXiv:2411.17501 (current title *The Limits of Inference Scaling Through Resampling*; v1 was *Inference Scaling fLaws*): imperfect verifiers cap repeated-sampling gains; when false positives have negative utility, the best number of attempts is often under 10. Say the condition.
- The hedged-request example's independence condition is Dean & Barroso's own: the techniques work only when the cause of variability does not hit several replicas at once. It is about latency, not failure; the close generalises it. Correlated wrong answers: Kim et al., ICML 2025.
- The relevant frame lists published runtime operations with their endpoints. It is not a ranking. The run figures  come from a run record (SELFHOST-2 metrics.json), not a paper.
- The relevant frame stage times are of the 2,557.5 s cycle (metrics.json): intent, specification and plan 3:41, build and test 20:01, review 18:55. Setup is 20.3 s (operations.jsonl).
- Blackburn et al., arXiv:2206.02871 (Eliaz 3rd of 9): most bitcoin from 3 Jan 2009 to 9 Feb 2011 was mined by 64 agents (address linking >99% sensitivity and specificity). Used as a motivating example of dependence uncovered from outside, not as evidence about forks. Say "my co-authors and I", not "I".
- Saurty-Seerunghen et al., iScience 2026 (Eliaz 3rd of 7): malignant cells cluster by patient tumour, non-malignant cells by cell type. The patient was known metadata; this is dependence structure, not a recovered hidden label.
- Eliaz et al. PRE 2020 is about linker valency (multilinkers), not branching. Liman et al. PNAS 2020 and Li et al. JPCB 2021 are about Arp2/3 branching and avalanches. None says branching sets global connectivity or that whole networks collapse together. The PhD also covered Hi-C loops and protein-folding hydrodynamics.
- Hitz et al. 2023 (ENCODE pipelines): data files, reference genome versions, software versions and parameters are captured in the ENCODE Portal.

- Every system named on a story slide is cited on that slide's source line, and `REFERENCES.md` preserves the full bibliography and documentation.
- Live migration (Clark et al., NSDI'05): 60 ms downtime for a Quake 3 server. Nephele (Lupu et al., EuroSys'23): no figure quoted.
- DeltaBox: the slides use the evaluation checkpoint figure (10.83 ms). The abstract's 14 ms / 5 ms are not used.
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
- None of these measures forks of one agent from a shared snapshot or multi-step agent runs. H2 measures environmental race-test co-failure, not dependence between agent judgments. Repair resampling is descriptive.
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
- Precision pooling requires one common target quantity, calibrated information and an appropriate dependence model. Selecting different patches or verifying a composition is separate.
- On the relevant frames, θ is one candidate's quantity. Choosing among candidates is a separate selection problem.
- Lineage labels shared parents, seeds, tests and fixtures. It cannot label a shared model's blind spots.

## Do not say

- That any self-authored PR was merged.
- That a person answered the gates.
- That the runs used islo.
- That the factory forks today.
- That fork is faster than a good build cache.
- That the speaker's PhD was only on branched networks, or that the papers show whole networks collapsing together.
- "I recovered" for the Bitcoin or iScience results: they are team results.
- That nine forks were run or came back green: the nine candidates and the nine repair samples are hypothetical or proposed.
- That Poolkeh pooled real samples: it is a model.
- That clusters or networks "collapse together": say "may collapse suddenly".
- That Kimi forks its reward judge: it forks a sandbox for judging.
- That Kim et al. measured forks or repeated runs of one model.
- That 60% is a correlation ρ, or that average pairwise correlation determines all-fail probability.
- That the follow-up preprints are peer reviewed.
- That SELFHOST-2 or SELFHOST-3 ran on the speaker's own sandbox platform (they ran in Docker Sandboxes through Airflow's sandbox toolset).

Models were served through Databricks; that may be named. Name no model vendor or endpoint.

The API slide explicitly names islo. The factory work orders ran on Docker Sandboxes; the disclosure states the speaker works for a sandbox company.

Do not say:
- that repair 2 was never tested (the suite ran after it);
- that promotion is model-checked;
- that the built reducer abstains;
- that any islo snapshot is a memory fork before Gate 0 is resolved;
- that nothing escaped. Say "nothing was pushed and nothing was denied".


## Current story and execution boundary

A fork is useful when captured state remains valid for the proposed continuations and capture/restore/divergence costs compete with rebuilding. The factory demonstrates file/dependency/feedback state, not a necessary valuable live-state workload. A running application at a reproduced failure is a **hypothetical future workload**. Source changes may require reload or restart. Hosted-model state and sampling are not captured by a guest snapshot.

The proposed child pipeline is return candidate, select, verify exact artifact and required behavior, check current authority, then publish or retain/export. The host must **authenticate and authorize** the child; identity alone is not permission. Artifact-digest approval is built; clone identity generation, revocable authorization, epoch fences and external evaluator remain proposed. Preserve recoverable artifacts before teardown.

## Chamo / Three-Body Atlas

Ori Chamo is the coauthor affiliated with Incredibuild. The preliminary ai.viXra:2608.0069 work analyzes **135,445** source periodic orbits. **26 selected difficult bidirectional continuation links** connect the projected branches within one sampled component. Independent 60-digit calculations check representative stability transitions; this is not a global completeness proof. The Atlas workflow separates candidate, screening, high-precision verification, independent reproduction and frozen claim; an unresolved independent numerical cross-check was rejected. It illustrates evidence admission, not agent-fork performance or dependence. [Preprint](https://ai.vixra.org/pdf/2608.0069v1.pdf), [records](https://github.com/zozo123/threebody-closing-the-open).

## Genomics, AI and security cases

- **Genomics:** Gilad, Eliaz et al. (2021) used >120,000 sgRNAs targeting 19,050 genes, shortlisted about 100 candidates and reported improved killing for six of eight tested SI-12 combinations in MCF-7 cells. The ≥4 technical replicates per viability point and ≥2 independent experiments per plot are distinct from the screen's three biological replicate arms. These are in-vitro results. The 2022 Matters Arising questions several hits' target expression; repetition alone does not establish on-target biological validity. A computational fork of analysis variants is a proposed use, not an experiment in this paper.
- **Autoresearch:** the published session report lists 126 attempts: 23 kept, 102 discarded, one crash. Validation bits per byte fell from 0.997900 to 0.969686 (2.83% relative decrease, calculated). The five-minute training budget excludes startup/compilation. This is one reported session on its hardware and validation setup, not a controlled fork experiment or a general model-capability gain.
- **AlphaEvolve:** the technical report attributes 0.7% average fleet compute recovery to deployed scheduling heuristics. A separate kernel-tiling optimization reports 23% kernel speedup and 1% lower overall Gemini training time. Keep the two deployments and denominators separate; none is our measured result or a sandbox-fork speedup.
- **AFL++:** official persistent-mode documentation describes typical 10–20× speed gains from many inputs in one child. A 1,000-input loop is a recommended starting point before process restart, not a universal fixed setting. Critical state must reset between inputs. This is process execution reuse, not a guarantee of independent test outcomes.
- **CyberGym:** the benchmark comprises 1,507 historical patched vulnerabilities across 188 projects; its differential check requires crashing the vulnerable version and not the patched version. The separate latest-code campaign covers 431 projects and 1,748 entry executables; OpenHands/GPT-5 produces 56 crashes, from which the authors manually confirm 22 unique zero-days. Crashes, benchmark successes and confirmed vulnerabilities are different units. The campaign is not a 22/1,507 benchmark success rate or a sandbox-fork experiment.

## Experiments and proposed amendments before collection

**`PREREGISTRATION.md` remains unchanged.** No result is claimed. Any design or analysis change below must be a dated amendment before collection, retaining the original protocol and its history.

- **H1:** compare reached-state restore with a warm cached template at N = 3, 6, 12, twenty repetitions per arm/N; batch makespan is primary. Capture accounting and total resource cost must not be confused with wall-clock makespan.
- **H2:** compare environmental race-test co-failure among siblings and restored strangers. Reused snapshot families make pair differences dependent; temporal dependence across rounds also needs explicit treatment. The original sign-flip and t-interval analysis cannot be called exact or validated without a justified independence/exchangeability structure. An amendment is **proposed**, not implemented here.
- A correlation excess of 0.05 is not absolute rho. Nine measurements give 6.43 variance-equivalent observations at absolute rho = 0.05; if strangers are 0.10 and siblings 0.15, siblings give 4.09. Only absolute rho belongs in that variance illustration.
- The public pre-repair substitute is not confirmed equivalent to the unavailable in-cell state by a tree-hash comparison. Verify it or explicitly narrow reproduction claims before collection.
- **Targeted coverage test:** force CellBusy plus same-owner adoption and foreign-owner refusal. This resolves a behavioral obligation; it is not a fork-speedup or fork-correctness experiment.
- **Nine repair resamples:** same prompt, policy and hosted endpoint; record out-of-plan edit count and diff diversity. Descriptive repeatability is not a correlation estimate. No guest reseeding controls hosted-model sampling.

The variance-equivalent sample size formula assumes equal variances and common pairwise correlation. It describes precision of a mean, not a literal independent-witness count, shared bias, search accuracy, selection success, or all-fail probability. Distinct evidence IDs and different model families do not establish independence.
