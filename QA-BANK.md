# Q&A: Forkable Sandboxes

For the **41-frame, six-act canonical deck**, without appendix or overlays. Questions refer to claims and artifacts, not old slide numbers. [Full sources](REFERENCES.md) and [precise bounds](CLAIM-FENCE.md).

## What value do the opening numbers show?

Dean and Barroso report a 1,000-key BigTable read with a backup after 10 ms: p99.9 latency fell from 1,800 ms to 74 ms with 2% extra requests. Brown et al. report SWE-bench Lite coverage rising from 15.9% for one sample to 56% for 250 DeepSeek-Coder-V2-Instruct samples. These are different opportunities: escaping a slow execution and generating a correct candidate. Coverage means at least one candidate solves the issue; selecting it still requires a reliable check. Setup details and verifier limits belong here and in slide comments rather than repeated opening qualifications.

## Which existing runtimes support state reuse?

SnowFlock exposes VM_fork(N) for remote VM clones; CRIU checkpoints supported process state; Firecracker snapshots microVM state. Kimi K3 AgentENV describes pause, fork for reached-state reward judging, and recovery; its reported scale is 51,219,741 sandboxes across 1,505,678 images. It forks the sandbox for judging, rather than the judge. DeepSeek DSec retains a sandbox when the training task is preempted and replays cached command results on resumption. These attributed mechanisms inform the runtime design; their endpoints and state semantics remain distinct. Full references and figures are in the bibliography and claim fence.

## What did you actually run?

Two factory work orders on Airflow through Docker Sandboxes, with hosted models through Databricks. The harness answered approval gates. Sandbox authority leases were not exercised and nothing forked; dispatch coordination leases are distinct. SELFHOST-2 public records establish the incident; SELFHOST-3 raw records are unpublished. Separate islo API measurements concern restore-run-capture, with memory capture unverified.

## Why call this forkable if the factory did not fork?

The talk proposes an execution contract and tests its prerequisites. Files may need only worktrees or a warm template. Process/RAM reuse requires a semantic probe and a workload that benefits from valid captured state. A running application at a reproduced failure is hypothetical here. Restore fan-out must not be renamed memory fork without evidence.

## Why not use a build cache or restart?

Those are credible alternatives. A fork must preserve useful state and compete on preparation, capture, restore, divergence and validation cost. Changed code may require reload or restart. The recorded file-level schedule could use worktrees; its 165.890-second saving is computed from serial timings and excludes overhead.

## What was the concrete testing failure?

A two-host installer task encountered an unrelated four-replica dispatch race. Repair added same-owner adoption on CellBusy outside the plan. Existing tests could cover helper behavior without deterministically forcing that new combination. Review approved with the direct test still absent. The harness suite reported 1,972 including skips and zero failures; an agent's statement that it could not run tests does not mean the harness did not run them.

## Where did the time and money go?

SELFHOST-2 timestamps give 43:44; recorded stages total 42:37.517. The two repairs and two reviews took 25.235 session minutes and $7.74846: 59.201% of stage time and 75.025% of $10.327824. These include tool activity. Initial setup was 20.3 seconds; making it 100 times faster saves about 20 seconds.

## Did the publication gate fail?

In the separate work order, it correctly refused an unreviewed file—the harness's diff archive. Recovery then lost the approved patch during teardown. Preservation/export and publication are separate decisions; export does not bypass approval.

## Does immutable testing prevent gaming or guarantee coverage?

No. It prevents some test edits, but source can optimize against exposed feedback or lack the needed test. Use development feedback, freeze a candidate, then validate its required behavior on reserved or directly targeted checks. Our incident establishes an unresolved obligation, not deliberate reward hacking or a failure frequency.

## What is built today?

Associative numeric merge; rejection of declared duplicate evidence IDs; lineage carriage; an artifact-digest approval gate. Lineage is not consumed to calibrate dependence. Unknown-dependence abstention, independently calibrated information, external evaluator, clone authority and epoch fencing remain proposed. The factory fork store is not demonstrated.

## Is the reducer just deduplication?

Its evidence check is precisely declared-reuse deduplication. That useful mechanism is distinct from measuring dependence between different observations. Pool only measurements of one common target; select candidates separately and verify the exact composition delivered. A fresh execution ID cannot make reused data statistically fresh.

## Can a worker forge precision?

Yes. A synthetic shard inflated its information 50 times and dominated unprotected pooling. The heuristic is not Byzantine protection; counting n alone does not validate information per observation, independence or calibration. Controller-derived validation remains proposed.

## Does N_eff measure correctness or pass@N?

No. N/[1+(N-1)rho] is variance-equivalent sample size for an average under equal variances and common pairwise correlation. It does not remove shared bias or determine all-fail probability. At N = 100 and rho = 0.1 it is 9.17. Selection also needs a verifier capable of identifying a correct candidate.

## Do cross-model error studies measure fork dependence?

No. Kim's 60% is conditional same-wrong-answer agreement, not rho. Kohli's nine-judge effective sample size is a task-specific panel result. Those studies motivate asking the question; they supply neither a floor nor a calibrated prediction for shared-snapshot agent continuations. Difficulty-adjusted baselines also change estimates of excess agreement.

## Why record lineage if it does not estimate rho?

Parent, fixture, test, seed policy and feedback exposure are shared factors known during execution. Records preserve them for analysis. They are not enough to determine strength, hidden model blind spots, or an appropriate crossed-factor model. The contribution is retaining usable provenance, not a new estimator.

## What do H1 and H2 decide?

H1 compares restore and a warm cached template for preparation makespan; it helps choose an execution backend. H2 compares environmental race-test co-failure of siblings and restored strangers; it may justify ancestry modeling for that workload. Neither measures agent judgment correctness. A targeted adoption test resolves coverage; nine repair resamples describe repeatability.

## Is H2's original analysis valid with reused families?

It has an unresolved design problem. Families recur across matched comparisons, so twelve pair differences are not automatically independent. Lockstep rounds may also be temporally dependent. A valid randomization/exchangeability argument and uncertainty method are needed. **The correction is a proposed dated amendment before collection. PREREGISTRATION.md is unchanged; no data collection or result is claimed.**

## Why not substitute Delta rho into the sample-size formula?

Because Delta rho is excess over strangers. The formula requires absolute rho. An excess of 0.05 yields 6.43 for nine measurements only when the absolute sibling rho is 0.05; strangers at 0.10 and siblings at 0.15 yield 4.09. The original thresholds must retain their history when amended.

## Can you reproduce the pre-repair state?

The in-cell input commit is unavailable. The protocol proposes a public substitute based on commit order, without a confirmed tree-hash comparison. Verify equivalence before a reproduction claim, or identify the substitute and narrow the experiment. Audit logs and fresh hosted-model reruns are not deterministic replay.

## What do 29 green race runs establish?

Under a hypothetical independent 10% branch-occurrence probability, missing it 29 times has probability 0.9^29 = 0.047. That rate was not measured, and independence is not established. A deterministic test that forces the required branch is a stronger way to resolve this obligation.

## What authority survives a clone?

Tokens copied into guest memory remain copied authority unless revoked. The proposed broker authenticates and authorizes each child, changes generation on restore and checks current permission at publication. Host identity alone is not a capability or permission. Publishing credentials stay outside; model requests already leave and incur cost.

## Are receipts trustworthy because they are external?

External placement helps integrity, not semantic correctness. Our records included skipped CI marked successful and harness approval recorded as human. Typed execution/skip/approval status, exact artifact binding, and independent verification are all needed. Provenance from the guest can aid audit without being a trusted verdict.

## What does Chamo add to this seminar?

Ori Chamo and Yossi Eliaz's preliminary result connects the apparent projected branches through all 26 selected bidirectional continuation links in a 135,445-orbit source catalog. Shooting restores periodicity; Floquet calculations assess stability; representative transitions have independent 60-digit checks. Extra-Trees proposes warm starts, rather than establishing the connections. A separate unresolved RK4 cross-check was rejected. The supported claim concerns the sampled component, not global completeness or agent-fork performance.

## What did the genomics screen establish?

The screen ranked candidate perturbations, then separate siRNA and drug-combination assays tested their effects. Six of eight tested combinations improved killing in MCF-7 cells. Technical repeats (≥4 per viability point) and independent experiments (≥2 per plot) are different replication units. This is an in-vitro finding. The 2022 Matters Arising questions expression of several hits, so replication does not settle on-target validity. It supplies a proposal-to-assay workflow, not evidence about computational forks.

## What did autoresearch improve, and how?

One published session edited `train.py`, trained each candidate under a five-minute budget, measured validation bits per byte and kept or reset the change. It reports 126 attempts: 23 kept, 102 discarded, one crash; 0.997900 → 0.969686, a calculated 2.83% relative decrease. Startup/compilation lie outside that budget. The score is hardware/setup-specific and repeatedly consulted during search; it is not a held-out general capability measure.

## What are AlphaEvolve's two efficiency numbers?

Scheduling heuristics recovered 0.7% of fleet compute on average. A separate tiling heuristic sped up the relevant matrix-multiplication kernels by 23%, reducing overall Gemini training time by 1%. These are distinct deployments and denominators. Automated evaluators screen candidate programs before production use; the report does not attribute these gains to sandbox forks.

## What is AFL++ reusing?

An initialized forkserver supplies children; persistent mode runs many inputs inside a child and resets target state between inputs. Documentation gives typical 10–20× speed gains and 1,000 iterations as a starting point before restart. State reset is a fidelity requirement. Incomplete cleanup can affect later inputs and distort results.

## Are CyberGym's 22 zero-days a benchmark success rate?

No. The historical benchmark has 1,507 patched vulnerabilities in 188 projects; a successful input crashes the vulnerable version and not the patched version. A separate latest-code campaign uses 431 projects and 1,748 entry executables. OpenHands/GPT-5 triggers 56 crashes, with 22 unique zero-days confirmed manually. Those counts distinguish generated crash evidence from a verified vulnerability; they do not share the historical benchmark's denominator.

## Is promotion model-checked?

No. A TLA+ design specifies artifact/evidence/approval alignment and current authority, but no TLC run or implementation trace check is recorded. The gate's digest binding is built; epoch fencing remains proposed.
