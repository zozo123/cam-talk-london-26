# Q&A: Forkable Sandboxes

For the **57-frame, six-act canonical deck**, without appendix or overlays. Questions refer to claims and artifacts, not old slide numbers. [Full sources](REFERENCES.md) and [precise bounds](CLAIM-FENCE.md).

## What changes in self-driving computation?

The workflow chooses its next execution from observed results. A user supplies a goal and constraints; the controller proposes executable alternatives, runs them, checks outcomes and chooses what to try or accept next. Each alternative still runs ordinary instructions on conventional Von Neumann hardware. The proposal concerns orchestration, search and acceptance evidence; it does not introduce a new ISA or replace the processor.

## What is the contribution in the software example?

Slides 27–32 explain one proposed execution/evidence/acceptance contract: reuse the useful starting state, try private alternatives, return changes with the checks that ran and their shared-input history, then validate and preserve the exact chosen output. Forking, fan-out/fan-in, testing, provenance and review are established techniques. The proposed contribution is their connected interface and its decision requirements. This is a research design rather than a demonstrated speedup or a priority claim over all prior systems. The observed factory run was serial. Costs, installer hosts, ownership diagnosis and delivery chronology remain in Q&A; the visible diagrams explain the general flows.

## What does the cinema analogy mean technically?

Playing a prescribed sequence corresponds to ordinary program execution. Saving a reached computation and trying private continuations corresponds to the runtime's declared snapshot or fork semantics. The agent can alter the next action, execute the alternative and decide what to keep or discard from evidence. Restoring declared computer state cannot undo a completed remote invocation, incurred cost or published action. Publication needs a current controller decision.

## What does the Python API comparison establish?

Both sketches try the same three edits against equivalent prepared input state, the same test and the same selector. The loop prepares each environment; the API prepares once, captures the required state and makes three private children. Its checkpoint/fork/execute/evaluate/select signatures are a proposed interface, not an implemented SDK. Evaluate returns an artifact and its evidence; select uses the same decision rule, without becoming an infallible verifier or numerical reducer. Ordinary Python can implement the pattern through process forks, worktrees or warm caches. The slide claims explicit reuse and isolation, without asserting concurrency or measured speedup. Changed code may need reload or restart. Forkability and adaptive control remain separate.

## What connects the six research themes?

The overview has six dated milestones in chronological reading order: early systems/security, biological/genomic research, the 2019 cancer-drug paper, NRGene, Mobileye and current compute work. Verify dates against the speaker’s career website; distinguish overlapping work periods from publication dates. The 2010–2016 period includes multiple systems employers, not six years at Twistlock alone. Headings explain the work in undergraduate language, with names underneath. The driving slide uses an official, credited Mobileye Manhattan photo from June 2021, with a concrete pedestrian/braking loop and failing-test/code-edit loop. The photo is illustrative, not attributed to a particular contribution by the speaker. The personal Mobileye role is perception of road junctions; local physical self-organization, researcher-led CRISPR design and proposed computer control remain different mechanisms.

## What did the biophysics simulation measure?

The PRE multilinker study extended Cytosim and compared linker valencies 2–7. Reported low/high motor-content comparisons used 600 seconds of simulated physical time and statistics from 30 random starts. Higher valency promoted bundles and larger clusters in those studied conditions. Filaments were graph nodes and protein connections were edges. That is a physical morphology finding, not a measurement of fork-induced correlation or execution speed.

## What exactly improved in the chromosome computation?

For the chromosome-1 A/B eigenvector at 500-bp resolution, POSSUMM took 2.5 minutes and 23 GB RAM. The dense approach's greater-than-4.6-TB requirement was a memory projection, not a measured dense run. Sparse matrix-vector products avoid materializing the dense correlation matrix. A separate first-four-components genome-wide endpoint took 39 minutes and 77.65 GB. The 33-billion input figure is quality-filtered contacts, derived from more than 42 billion paired-end read pairs. These endpoints must remain distinct. [Harris et al.](https://www.nature.com/articles/s41467-023-38429-1).

## What do the Tokio timings establish?

The speaker's external issue #8200 demonstration reports approximate compile times of 46 seconds fresh, 13 with a restored artifact cache and 3 hot. Separate full-test timings are about 75 and43 seconds; after touching source, the compared endpoints are about 38 and13. These are different operations. The report provides a practical warm-cache alternative, without a controlled raw protocol, a memory-fork result or a maintainer adoption claim. [Primary issue](https://github.com/tokio-rs/tokio/issues/8200).

## What do ENCODE's provenance records establish?

The pipeline collection processed more than 14,000 datasets, at least 40,000 FASTQ files, and approximately 20 assay types. WDL specifies workflows; Cromwell runs them; Docker supplies task environments; CAPER manages execution and I/O; CROO organizes outputs. Portal analysis/file objects preserve source files, versions, metrics and relationships. This makes analysis traceable. Biological correctness, authenticated receipts and calibrated uncertainty need their own checks. [Hitz et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC10371165/).

## What did CRISPR-IL add beyond a fixed genomic pipeline?

NRGene's GoGenome linked researcher-run editing experiments to the next design through processing and model updates. It reported >20 TB sequencing data and sub-second GOLD feature lookup, not end-to-end cycle latency. [Source](https://aws.amazon.com/blogs/storage/a-gene-editing-prediction-engine-with-iterative-learning-cycles-built-on-aws/) and [bounds](CLAIM-FENCE.md#motivation-and-personal-research-themes). Noam Barkai is distinct from OffRisk's Gil Ad Barkai.

## What does the immunotherapy theme establish?

It identifies a proposed response-guided research direction. The supplied cancer-genomics work and SI-12 drug-combination assays are relevant methodological background, not evidence of an autonomous immunotherapy system, a clinical treatment-selection policy or a clinical outcome. The theme makes no measured performance claim.

## Does a digest recover the original source?

A digest identifies bytes; reproducing the computation also requires those bytes or a retrievable immutable object. The adapter shim's source remained outside Git and was unavailable after the run. The unavailable original input b77afa9 likewise cannot be replaced by a claimed hash identity alone. These source-object gaps are distinct from SELFHOST-3, where teardown removed an approved candidate patch after delivery refusal. Preserve input manifests, source and adapter objects, candidate artifacts, evidence and decision receipts before every exit. A refusal may correctly prevent publication while still requiring durable export.

## Which identities should a result carry?

Keep candidate artifact digest, execution ID, observation ID, underlying case/data ID, and lineage separate. A fresh execution may reuse the same case or data. Four runs of 100 cases can produce 400 outcomes in 100 case clusters. The reducer rejects declared repeated evidence IDs; independently assigning different labels does not prove disjoint observations or independent noise. The interface must define what each ID identifies and bind it to accessible source objects.

## What value do the execution and sampling examples show?

Dean and Barroso report a 1,000-key BigTable read with a backup after 10 ms: p99.9 latency fell from 1,800 ms to 74 ms with 2% extra requests. Brown et al. report SWE-bench Lite coverage rising from 15.9% for one sample to 56% for 250 DeepSeek-Coder-V2-Instruct samples. These are different opportunities: escaping a slow execution and generating a correct candidate. Coverage means at least one candidate solves the issue; selecting it still requires a reliable check. Setup details and verifier limits belong here and in slide comments rather than repeated opening qualifications.

## Which existing runtimes support state reuse?

SnowFlock exposes VM_fork(N) for remote VM clones; CRIU checkpoints supported process state; Firecracker snapshots microVM state. Kimi K3 AgentENV describes pause, fork for reached-state reward judging, and recovery; its reported scale is 51,219,741 sandboxes across 1,505,678 images. It forks the sandbox for judging, rather than the judge. DeepSeek DSec retains a sandbox when the training task is preempted and replays cached command results on resumption. These attributed mechanisms inform the runtime design; their endpoints and state semantics remain distinct. Full references and figures are in the bibliography and claim fence.

## What did you actually run?

Two factory examples on Airflow through Docker Sandboxes, with hosted models through Databricks. The harness answered approval gates. Sandbox authority leases were not exercised and nothing forked; dispatch coordination leases are distinct. SELFHOST-2 public records establish the incident; SELFHOST-3 raw records are unpublished. Separate islo API measurements concern restore-run-capture, with memory capture unverified.

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

Yes. The synthetic generating target is μ = 5.0. A 2,000-point injected shard was centered at 17.0 with SD 0.02 and then inflated its reported per-observation information a further 50 times. Unprotected pooling returned 17.0004; the stress heuristic returned 4.9566. [Primary demo](https://github.com/zozo123/boltzmann-mapreduce/blob/main/demo.py#L151-L165). The 4.9450 full-sample mean belongs to a separate snapshot integration experiment. The heuristic is not Byzantine protection; counting n alone does not validate information per observation, independence or calibration. Controller-derived validation remains proposed.

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

The in-cell pre-repair input b77afa9 is unavailable. The proposed public substitute is c07bc4a. The protocol proposes a public substitute based on commit order, without a confirmed tree-hash comparison. Verify equivalence before a reproduction claim, or identify the substitute and narrow the experiment. Audit logs and fresh hosted-model reruns are not deterministic replay.

## What do 29 green race runs establish?

Under a hypothetical independent 10% branch-occurrence probability, missing it 29 times has probability 0.9^29 = 0.047. That rate was not measured, and independence is not established. A deterministic test that forces the required branch is a stronger way to resolve this obligation.

## What authority survives a clone?

Tokens copied into guest memory remain copied authority unless revoked. The proposed broker authenticates and authorizes each child and checks current permission at publication. Replacing a logical worker advances its epoch; concurrently forking a new child does not automatically revoke the parent. Host identity alone is not a capability or permission. Publishing credentials stay outside; model requests already leave and incur cost.

## Are receipts trustworthy because they are external?

External placement helps integrity, not semantic correctness. Our records included skipped CI marked successful and an approval gate answered by the harness but recorded as human. This does not mean the harness performed the human review. Typed execution/skip/approval status, exact artifact binding, and independent verification are all needed. Provenance from the guest can aid audit without being a trusted verdict.

## What does Chamo add to this seminar?

Ori Chamo and Yossi Eliaz's preliminary result connects the apparent projected branches through all 26 selected bidirectional continuation links in a 135,445-orbit source catalog. Shooting restores periodicity; Floquet calculations assess stability; representative transitions have independent 60-digit checks. Extra-Trees proposes warm starts, rather than establishing the connections. A separate unresolved RK4 cross-check was rejected. The supported claim concerns the sampled component, not global completeness or agent-fork performance.

## What did the genomics screen establish?

The screen ranked candidate perturbations, then separate siRNA and drug-combination assays tested their effects. Six of eight tested combinations improved killing in MCF-7 cells. Technical repeats (≥4 per viability point) and independent experiments (≥2 per plot) are different replication units. This is an in-vitro finding. The 2022 Matters Arising questions expression of several hits, so replication does not settle on-target validity. It supplies a proposal-to-assay workflow, not evidence about computational forks.

## What did autoresearch improve, and how?

One published session edited `train.py`, trained each candidate under a five-minute budget, measured validation bits per byte and kept or reset the change. It reports 126 attempts: 23 kept, 102 discarded, one crash; 0.997900 → 0.969686, a calculated 2.83% relative decrease. Startup/compilation lie outside that budget. The score is hardware/setup-specific and repeatedly consulted during search; it is not a held-out general capability measure.

## What are AlphaEvolve's two efficiency numbers?

Scheduling heuristics recovered 0.7% of fleet compute on average. A separate tiling heuristic sped up the relevant matrix-multiplication kernels by 23%, reducing overall Gemini training time by 1%. These are distinct deployments and denominators. Automated evaluators screen candidate programs before production use; the report does not attribute these gains to sandbox forks.

## What is AFL++ reusing?

Fuzzing repeatedly tests a target with mutated inputs. Coverage feedback keeps inputs reaching new paths for further mutation; crashes require investigation and deduplication. A deferred forkserver clones initialized state; persistent mode runs many inputs in a child while its harness resets mutable state. Typical 10–20× gains and roughly 1,000 iterations before restart come from persistent-mode documentation. The repeat loop avoids a process fork for every input. Correct reset preserves test fidelity; a crash alone does not establish an exploitable vulnerability.

## Are CyberGym's 22 zero-days a benchmark success rate?

No. The historical benchmark has 1,507 patched vulnerabilities in 188 projects; a successful input crashes the vulnerable version and not the patched version. A separate latest-code campaign uses 431 projects and 1,748 entry executables. OpenHands/GPT-5 triggers 56 crashes, with 22 unique zero-days confirmed manually. Those counts distinguish generated crash evidence from a verified vulnerability; they do not share the historical benchmark's denominator.

## Is promotion model-checked?

No. A TLA+ design specifies artifact/evidence/approval alignment and current authority, but no TLC run or implementation trace check is recorded. The gate's digest binding is built; epoch fencing remains proposed.

## Final 57 slide revision checks

Original slides 1–57 map to the final deck in DECK-REVIEW.md. Verify 57 canonical frames, no overlays/appendix, 41:25 cue total, and every frame's Q&A. ENCODE immediately precedes CRISPR-IL; the factory immediately precedes the VM/microVM/container/sandbox/cgroups table. The physics footer omits the authorship comment. The two Python examples use the same edits/checks and mark the API as proposed. The create trace retains operation, concurrency, completion and percentile endpoints. The warm comparison holds H/R/D/N fixed and changes only P. Its axis is resource-seconds. The reducer labels abstention as an acceptance design. The applied merge table says collection has not started; protocol confidence-bound rejection rules remain in Q&A. Preserve the original protocol hash and inspect all rendered pages for clipping and overlap before release.


## What changed in the current startup landscape?

ComputeSDK’s 2 October 2026 Burst TTI raw results rank Isorun first: median 72.77 ms, p95 78.29 ms, 100/100 success at concurrency 100. Miosa is 163.35/187.8 ms and Archil 237.77/250.34 ms. Time to interactive includes creation and the first successful command, measured by the client. The older Table 2 trace is create-only at requested concurrency eight, median 3.44 s and p95 9.00 s. This is a dated landscape update, not a controlled longitudinal speedup. Source JSON and commit are preserved in evidence/ and REFERENCES.md.

## Are intersection, mutual information and precision the same thing?

No. Set union counts distinct declared observations, and intersection identifies shared items. Shannon mutual information describes dependence between random variables; the entropy identity concerns uncertainty, not Fisher precision. Information about a target obeys I(theta;X,Y) = I(theta;X) + I(theta;Y | X): the second term is what Y adds after X. Pairwise overlap alone does not supply a joint model or estimate weighting.

## How can aggregation improve signal-to-noise when errors are shared?

For unbiased estimates of one scalar target with known positive-definite error covariance Sigma, generalized least-squares weights are Sigma-inverse times the all-ones vector, normalized to sum to one. The resulting estimate is the weighted sum and its variance is the reciprocal of 1-transpose Sigma-inverse 1. The matrix describes noise sizes and shared errors; it must be externally justified. This is a proposed extension beyond the built independent-summary reducer. Shared bias is not removed. Under the equal-noise/common-correlation illustration, 100 estimates at correlation 0.1 yield the mean variance of 9.17 independent estimates. Noise falls to about 0.33 of one estimate, giving about 3.03 times its SNR for a fixed signal; independence would give 0.10 noise and 10 times SNR.

Slide 8 count audit: six drugs across four breast-cancer cell models plus four extra drugs in E0771 gives ten candidates in that model. Its 45 unordered pairs are theoretical possibilities at one chosen dose per drug, not a completed combination screen. Verify the simplified three-step flow: test ten individual drugs, compare cell killing with the PD-L1 rise, then choose and test abemaciclib + SI-2 for 72 hours. Researcher-directed describes follow-up selection, not manual pipetting. The six-plus-four scope and single-drug induction range remain in Q&A. Parallel computational forks remain an analogy.

Slide 9 Roadbook audit: preserve the credited Manhattan photograph and personal junction-perception role. Verify the speaker-supplied 300M Mobileye-equipped-car assumption, anonymized data transmission, same-road alignment, aggregation and return of the updated map. The photo must remain unchanged and its caption must identify an autonomous test vehicle (AV), and the visible slide must omit the service acronym. The 34 billion 2025 road-miles / 365-day year yields ~1,080 road-miles/second as an annual average, not signals/second or an every-second upload guarantee. Use HD. The 2025 mapping total is a separately dated reported metric for a narrower contributing fleet. Do not derive current per-car or signal-upload rates from the 300M assumption.

## How does the biology search connect from computer to laboratory?

CRISPR-IL uses researcher-led experiments to update editing predictions. OffRisk is a separate computational annotation example before focused lab follow-up: 118 predicted matches include 117 possible off-targets; four unintended sites receive high-coding priority after excluding the intended target from five such labels. That is not measured safety. The 2019 Scientific Reports study compared ten drugs in E0771, giving 45 theoretical pairs at fixed doses, and reported a selected SI-2 combination. The 2021 Communications Biology study first ran a pooled cell screen with >120,000 guides covering 19,050 genes. Six guides target each gene. Three conditions, each with three biological replicate arms, give nine pooled arms. DRACO requires at least four of six guides to agree in direction before ranking by the strongest retained effect. The sequencing analysis nominates approximately 100 candidate genes. A derived nominal count of 19,050 x 6 x 3 x 3 = 1,028,700 gene-targeting guide/condition/replicate combinations per later sampling time describes the layout, not independent experiments or exact unique library constructs. Eight drug-target candidates plus five other genes led to 13 genetic checks (10 increased sensitivity) and eight drug combinations (six improved killing). The approximately 190-fold narrowing is calculated from 19,050/~100. These are connected search principles across separate studies, not one merged experiment or a purely computational whole-genome screen.

## What do the CyberGym counts mean?

431 projects supplied 1,748 runnable fuzzing targets. OpenHands/GPT-5 generated and executed inputs against current code; sanitizers reported 56 crashes. Reproduction, deduplication and analysis established 22 distinct previously unknown vulnerabilities. A project can supply several executables, and several crashes can identify one bug. No input-count or fork-count denominator is supplied by those values. The reduction is not a clean 22/56 acceptance rate.

## Which fan-in strategies are covered?

The visible strategy menu maps partition-and-gather to union, alternative selection to argmax over eligible candidates, compatible code composition to a partial merge function, measurement pooling to a normalized weighted mean, and common-finding comparison to intersection. Union and difference concern item identity; intersection concerns overlap. Agreement alone does not verify truth, and clean textual merging does not verify behavior. Q&A also retains first-valid replicas for tail latency, voting with calibrated errors, paired comparisons with common randomness and adaptive branching/pruning. The output meaning determines the check.

## How is the 300 million Mobileye car count used?

On 4 October 2026 the speaker instructed the deck to assume 300 million Mobileye-equipped cars sensing roads and sending anonymized data, based on firsthand Mobileye experience. The visible slide attributes the count to the speaker. The public release supports the data flow and the separately dated 34-billion-road-mile 2025 mapping total for a narrower contributor population. It does not verify the assumed 300M fleet or establish its per-car upload rate. 34,000,000,000 / 31,536,000 = 1,078.13 road-miles/second, rounded to 1,080 as an annual average. No larger current figure is invented.


## How do max pooling, argmax, averages and ReLU fit fan-in?

Max pooling returns the largest value. Argmax returns the candidate or index that produced the largest score, so a selected code artifact retains its identity. Ordinary averaging uses equal weights; weighted pooling requires the same target and justified uncertainty, including shared errors. Code merge constructs a new artifact and requires a check of that combined version. ReLU clips negative values and is a transformation, not a fan-in reduction. Its placement matters: ReLU(-1) and ReLU(1) average to 0.5, while ReLU of their mean is 0. Union and intersection operate on identified items, with duplicates counted once. Agreement can still reflect shared error.

## Why can one orbit family look like two groups?

Li, Li and Liao (2021) described one catalog family; Stancevic and colleagues (2023) saw two branches in a corrected period/angular-momentum projection. Chamo and Eliaz follow actual solutions through changing masses and numerical correction, connecting the tested branches in the sampled component. A many-dimensional family can fold when projected onto two observables. The new stability slide separately simplifies the paper's +1 crossing and opposite-Krein Hamiltonian–Hopf collision, each independently reproduced at 60 digits. These are representative linear planar transitions, not global connectivity or nonlinear stability proofs.


The simplified orbit-stability visual uses growing versus bounded responses to a tiny nudge, with parameter-change arrows between the examples. Its technical +1 and Hamiltonian–Hopf mechanisms remain in Q&A. Stable here means the disturbance stays bounded in the linear planar model, not that the orbit attracts nearby trajectories.
