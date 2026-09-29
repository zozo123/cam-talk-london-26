# Presenter guide: AI (SW) Factories*

**Forkable Sandboxes as a Runtime for Automated Search and Development**

Yossi Eliaz · Associate Professor, Holon Institute of Technology (HIT) · Principal Engineer, Incredibuild / islo.dev

Cambridge SRG · 15 October 2026 · 15:00–16:00 BST · FW11 + Microsoft Teams

Canonical source: `talk.tex`. The PDF contains exactly 40 slides. All slide notes below come from that source. Timing cues total **44:55** and are a pacing plan, not a measured live rehearsal.

## The story

As model agency grows, coordination becomes a systems problem. Motivate this with cumulative scientific and engineering progress: later work inherits foundations, methods, artifacts, and criticism. Newton, Einstein, Turing, and Shannon are distinct milestones, not a fabricated collaboration chain. Move from this coordination need to the fields represented in Yossi's biology, genomics, software-engineering, and post-training work; pose the eight-agent puzzle; then use Arp2/3 branching to motivate why shared ancestry, branch structure, and interaction matter. The core runtime question is how parallel proposals become reviewable, cumulative work: preserve a supported state, explore alternatives, evaluate evidence, and govern integration.

## Run of show

| Slides | Segment | Duration | Cumulative |
|---|---|---|---|
| 1–6 | Motivation, fields, puzzle, and physical branching | 5:20 | 5:20 |
| 7–16 | State and runtime | 10:25 | 15:45 |
| 17–22 | Search and learning | 7:15 | 23:00 |
| 23–32 | Evidence and composition | 13:05 | 36:05 |
| 33–40 | Implementation and agenda | 8:50 | 44:55 |

## Opening

“As models gain agency, they can use tools, run experiments, and change artifacts. The next challenge is coordination. Human knowledge has advanced cumulatively: researchers inherit foundations, methods, data, and criticism, then test and extend them. Newton, Einstein, Turing, and Shannon illustrate distinct intellectual foundations, not one collaboration chain. My work touches this coordination problem in physical biology, genomics, software engineering, and model development, though each field judges results differently. Imagine eight agents proposing changes to one project: every patch passes alone. Which should we keep, what have we learned, and can we combine them? Arp2/3 gives us a physical example of local branching changing a network. A computational fork is a different mechanism, but it raises a related systems question: how can we preserve a common starting point, explore alternatives, exchange evidence, and coordinate what follows?”

## Pacing when discussion starts early

Keep the opening puzzle, the continuation contract, the break-even model, the two RL loops, the three graphs, evidence reduction assumptions, composition, the measured trace, and the falsifiable benchmark. Give slides 6, 12, 13, 17, 21, and 34 a brief explanation if time is tight. Keep the Arp2/3 result and Ori anecdote concise; distinguish biological branching from computational forking. Finish by returning to the eight candidates.

## Questions to be ready for

- **Why not a build cache?** It may win. Compare against cached restart and identify which reached state cannot be reconstructed as cheaply from immutable artifacts.
- **Does a fork create independence?** It creates a separate continuation. Statistical dependence comes from the data, randomness, model, interventions, selection, and communication.
- **Can shared randomness help?** Yes, for a paired difference when the coupling preserves the intended marginals and induces helpful covariance. Independent corroboration answers a different question.
- **What if eight patches all pass?** Test the selected composition as a new artifact. Pairwise screening does not rule out higher-order interactions.
- **What is actually implemented?** The reference evidence reducer and reported snapshot-to-worker integration path. The complete runtime, routing policy, and promotion protocol are proposals.
- **What is the new performance result?** This seminar reports no new controlled speedup. The 6.70 s trace is a total client-observed worker-round-trip duration without an equivalent cold baseline.
- **How far do the physical examples go?** Arp2/3 motivates attention to branch structure and interaction; the Ori paper motivates targeted numerical checks. Neither establishes that biology predicts runtime behavior or that the sandbox is faster.
- **Can the evidence record solve adaptive dependence?** No. It preserves information needed to investigate the problem. A calibrated general reducer for adaptive, correlated branches remains open.

## Slide notes

### 01. AI (SW) Factories*

**Cue: 0:45 · planned clock 0:00–0:45**

Introduce the title and central motivation: capable models increasingly act through tools and sequences of decisions. When many processes or agents can propose, run, and revise work, coordinating state, evidence, and commitment becomes a systems question. The atelier asterisk frames the factory as a workshop for exploration and refinement.

### 02. As model agency grows, coordination becomes a systems problem

**Cue: 0:50 · planned clock 0:45–1:35**

Models increasingly plan, use tools, run experiments, and revise artifacts. With several agents acting at once, ask what each inherited, changed, and learned, and who may commit the result. Present coordination as a research motivation, not a claim that every multi-agent system needs one architecture.

### 03. Coordination lets parallel work compound

**Cue: 0:50 · planned clock 1:35–2:25**

The point is not that Newton, Einstein, Turing, and Shannon formed one team or one direct sequence. They mark distinct foundations. Scientific and engineering progress becomes cumulative because later people inherit formal ideas, methods, instruments, data, and criticism, then test and extend them. The same is true of software: code, tests, benchmarks, and maintenance knowledge are shared foundations. These examples motivate cumulative knowledge; they do not claim that swarms reproduce scientific communities or replace human judgment. With capable agents, parallel proposals are only a start. To compound work, a system must bring complementary expertise to bear, make evidence and provenance inspectable, manage dependencies, and review the synthesis. This motivates the fields I work across and the concrete puzzle next.

### 04. One runtime question across several fields

**Cue: 0:50 · planned clock 2:25–3:15**

Connect physical biology, genomics, software and engineering, and RL to prior work and distinct validation standards. Arp2/3 and actomyosin work motivate attention to local branch structure and collective dynamics. ENCODE, POSSUMM, and OffRisk show the importance of data, reference versions, pipelines, and quality evidence. Spark, Airflow, and the Linux kernel are motivating maintenance workloads, not benchmarks in this talk. Make clear that no claim is being made that these systems already use the proposed runtime.

### 05. Eight agents, eight candidates

**Cue: 1:00 · planned clock 3:15–4:15**

Eight agents propose patches from the same prepared parent; each candidate passes the available tests in isolation. Passing alone does not decide which is best, how much independent evidence exists, or whether the changes work together. This is a thought experiment that the talk will revisit.

### 06. Branches in biology; forks in software

**Cue: 1:05 · planned clock 4:15–5:20**

Arp2/3 nucleates a daughter actin filament from a mother filament, changing network connectivity. Interactions shape behavior at larger scales. A computational fork instead restores a supported state into separate executions, applies a declared candidate and random-stream policy, and records each result's lineage. The analogy is shared history and branching structure; a physical filament is not a copied machine state, and biological thresholds do not predict software performance.

### 07. Environment, sandbox, snapshot, fork

**Cue: 1:00 · planned clock 5:20–6:20**

A sandbox is an active controlled execution boundary, while a snapshot is a representation of captured state. An environment is an interaction contract and may span multiple machines or the physical world. A VM can contain an environment, but the VM alone does not specify a task, reward, or termination rule. I use fork broadly for a supported branch of execution; I am not claiming every implementation is POSIX fork or that every resource can be copied.

### 08. What belongs to the state?

**Cue: 1:00 · planned clock 6:20–7:20**

This is a conceptual state decomposition, not a promise that one snapshot format captures all components. A VM snapshot may preserve process memory yet leave the agent's remote conversation history outside it. A copied random generator creates a coupling until streams diverge or are explicitly reseeded. External service state needs a declared policy: freeze a fixture, replay responses, recreate the service, or accept an uncontrolled dependency. The manifest makes those choices auditable.

### 09. A continuation contract

**Cue: 1:15 · planned clock 7:20–8:35**

This is a proposed observational contract. The law symbol denotes the distribution of observations under the declared continuation, not equality of every machine bit. For deterministic tests we may require exact agreement; stochastic simulations need a justified distributional criterion. Finite tests check specified observations and cannot certify every possible policy or event. Restoration fidelity, candidate quality, and scientific validity are separate axes. We establish the first before attributing an outcome to a changed candidate.

### 10. Simulation and the external world

**Cue: 1:00 · planned clock 8:35–9:35**

A branch in a simulation is a controlled computational alternative conditional on a model. A learned model may predict cheaply but brings approximation error. Neither makes the real world checkpointable. Likewise, restoring an API client does not undo an email, a database write, or a robot movement. External effects require transactions, mocks, compensation where possible, or separate authorization. The scientific question is whether the model and measurement justify the conclusion outside the captured boundary.

### 11. One running software experiment

**Cue: 0:50 · planned clock 9:35–10:25**

This is a proposed experiment, not a measured parser benchmark. Each candidate changes one implementation relative to the same identified parent. Correctness is a constraint and throughput is an objective, so a fast incorrect parser cannot win. The public development corpus and final validation material have distinct roles. Preserve the baseline and all candidate identities. Later we will ask whether two patches that pass alone still pass when composed.

### 12. The branch lifecycle

**Cue: 0:55 · planned clock 10:25–11:20**

A common shortcut in this story is to patch a file and assume a restored process now runs the new implementation. It does not. The candidate has to rebuild, reload, restart, or otherwise change the executing program. Reuse repository preparation and expensive fixtures only where the intervention leaves them valid. Content-addressed build artifacts can be shared with explicit scope and provenance. This lifecycle is also why restore latency alone is a poor measure of useful search cost.

### 13. Mechanisms for branching

**Cue: 1:00 · planned clock 11:20–12:20**

These are mechanism classes, not a performance ranking. A container image is a recipe for reconstruction rather than a live checkpoint. Process checkpointing depends on which kernel and device resources it can represent. A VM snapshot extends the boundary but still needs supported device semantics and a policy for external identity. Firecracker is a relevant microVM isolation reference, not evidence that every snapshot operation or workload has equal guarantees. A benchmark must compare equivalent required behavior.

### 14. Copy-on-write moves cost to divergence

**Cue: 0:55 · planned clock 12:20–13:15**

Copy-on-write changes when copying is paid. It can make the branch operation cheap while shifting overhead into execution. Large write sets and memory contention can erase the benefit. Sharing a prepared object also creates dependencies: its content and authorization matter. The cartoon shows eligible memory pages only; disk, devices, distributed state, and application caches may use different mechanisms.

### 15. When does branching pay?

**Cue: 1:20 · planned clock 13:15–14:35**

This additive resource model assumes both paths do the same candidate work and evaluation. Cold execution repeats P each time; branching pays it once, plus capture and per-child restore and divergence overhead. Subtracting the expressions gives the break-even inequality. The graph uses declared hypothetical units, not benchmark data. Wall-clock latency additionally depends on scheduling and parallelism. Model calls belong in W, and all unsuccessful branches and checks count. If the paths differ in candidate work, add that difference explicitly.

### 16. A runtime architecture for experiments

**Cue: 1:10 · planned clock 14:35–15:45**

This is the proposed architecture. Separate data movement from permission to accept a result. The controller owns task identity and scheduling. Workers can produce candidate artifacts and observations, while evaluation code and admission records have separate write permissions. An append-only campaign log records failures and retries. Expiring capabilities and fencing prevent an old worker from committing into a later campaign. The architecture is an interface proposal; the later trace demonstrates only a subset of this complete contract.

### 17. Search needs both improvement and diversity

**Cue: 1:30 · planned clock 15:45–17:15**

Put two search ideas together. Stochastic improvement proposes a candidate, evaluates it, and accepts or rejects under an explicit rule. With noisy scores, one positive difference is weak evidence; keep failures and uncertainty, and sometimes confirm promising results. Population search keeps more than one incumbent: mutation explores nearby candidates, crossover proposes a new artifact, and a MAP-Elites-style archive preserves useful behavioral diversity. The drawing is schematic. A code crossover does not merge live machines or inherit correctness. Every recombination is a new candidate that needs evaluation. The runtime supports branching, restoration, and evidence lineage; it does not choose the objective, acceptance rule, or guarantee convergence.

### 18. Arp2/3 shapes network dynamics

**Cue: 1:15**

In the cited actomyosin simulations, high Arp2/3 concentration is associated with stalling, low concentration with contraction, and an intermediate regime with loosely connected clusters that can collapse in motor-driven avalanches. Relate this to Yossi's graph-theoretic morphology work. The runtime design lesson is limited: branch count alone does not characterize system behavior; connectivity and interaction matter. Stockmayer's polymer theory motivates asking whether communication can connect candidate lineages, but any threshold must be derived for the actual dependency model. Do not claim that software search follows actomyosin physics.

### 19. Reinforcement learning has two loops

**Cue: 1:05 · planned clock 18:30–19:35**

The inner loop is interaction: observe, act, transition, receive feedback. The outer loop uses trajectories to change policy parameters. Post-training can place a language model inside this structure, with tools and a verifier-derived reward. A fork provides a way to start or continue an episode from supported state. It does not turn branch selection into reinforcement learning by itself. Keep inference cost, environment cost, evaluation cost, and optimizer cost distinct when assessing an infrastructure benefit.

### 20. Reset changes the learning problem

**Cue: 1:05 · planned clock 19:35–20:40**

Reusing a difficult-to-reach state can make exploration productive, as return-and-explore methods illustrate. But a policy trained primarily from favorable intermediate checkpoints has seen a different starting-state distribution. We cannot silently substitute its performance for task-start performance. Depending on the algorithm, distribution correction, curriculum design, or explicit reporting may be necessary. Snapshot ancestry records where experience came from. The final evaluation should still test the deployment question we claim to answer.

### 21. Automated research chooses experiments

**Cue: 1:05 · planned clock 20:40–21:45**

Automated research includes choosing what to measure, not merely searching parameters under a fixed score. POET is a relevant example of jointly generating environments and optimizing agents, with transfer between problems. The extension here is a systems question: how do task identity and evidence remain meaningful when the search changes its own experiments? Exploratory measurements can guide future trials, but final validation needs an explicit criterion. Scores from different objective versions are not automatically comparable.

### 22. Which computation is worth buying?

**Cue: 1:15 · planned clock 21:45–23:00**

This is a metareasoning problem. Computation has a cost and changes what we know or which actions are available. An ideal controller values a computation by the expected improvement in its eventual decision, accounting for budget and dependencies. That value is generally unknown and difficult to estimate; it is not a new implemented scheduler in this artifact. A simple policy might compare predictive uncertainty, diversity, expected gain, and cost. The physics example next shows why a targeted check can be more useful than many similar trials.

### 23. Apparent branches, verified connections

**Cue: 1:30 · planned clock 23:00–24:30**

Two apparent branches in an invariant projection were interpreted as separate sets. Our continuation study tests the underlying solutions rather than treating the picture as decisive. The paper reports successful bidirectional continuation on 26 selected difficult links and independent checks of a long-range connection. The claim concerns the sampled catalog, not the global topology of all periodic orbits. For this talk the lesson is methodological: retain the state and path, then choose a check that discriminates between interpretations. This study does not measure sandbox performance or demonstrate autonomous discovery. The schematics explain that question and are not numerical figures from the study.

### 24. Repeated runs can share an error

**Cue: 1:20 · planned clock 24:30–25:50**

Expand the variance of the average into K variance terms and K(K-1) covariance terms to obtain this expression. Here all variables have marginal variance sigma squared and all distinct pairs have correlation rho. With positive rho the variance approaches a floor. This is an illustrative model, not a fitted dependence law for sandbox workers. Lineage reveals possible dependencies but cannot infer their strength. Also, variance is not bias: a shared misspecified model can be confidently wrong even if numerical noise is small.

### 25. Shared randomness can improve a comparison

**Cue: 1:15 · planned clock 25:50–27:05**

Dependence can be designed for a purpose. To compare two simulation methods, use paired random inputs so that nuisance variation cancels. The variance identity is exact; improvement over independent runs requires positive covariance and appropriate marginal sampling. Common random numbers do not always help. This is a different question from independently corroborating a scientific claim. The runtime should expose whether it preserves RNG state, reseeds, or assigns coupled streams, so the experimenter can choose rather than inherit an accidental statistical design.

### 26. Three graphs describe the computation

**Cue: 1:20 · planned clock 27:05–28:25**

Ancestry records where execution state came from, often as a tree or DAG. Communication adds edges that need not follow ancestry; these edges can introduce dependencies among later decisions. Composition concerns sets of artifacts and may need hyperedges for three-way or higher-order effects. The outline around the three candidates denotes a possible higher-order interaction, not a measured one. Keeping these structures separate avoids calling every relationship a fork. It also clarifies which metadata the controller must retain.

### 27. What does a message contribute?

**Cue: 1:25 · planned clock 28:25–29:50**

The XOR example is exact and deliberately small. Either bit alone leaves H uniformly random; together they determine H. After receiving A, B contributes one bit of conditional information. This is information synergy, not the finite-difference score interaction between two software patches. In practical search we rarely know the joint distribution well enough to compute mutual information directly. Treat it as a precise way to ask what a message could add, not a ready-made universal routing score. Useful decision information also depends on costs and available actions.

### 28. Compare across candidates; pool only within one

**Cue: 1:00**

Use the matrix to separate the three operations. Across a row, retain compatible measurements about one candidate-specific target; down a column, compare candidates under a common evaluation block. The receipt records estimate, information, sample count, evidence identity, lineage, and metadata. Shared evaluation inputs may call for paired comparisons. A combined patch is a new candidate and needs a new evaluation.

### 29. Evidence-aware reduction

**Cue: 1:30**

The precision-weighted formula applies to compatible evidence about one fixed candidate-specific target under stated Gaussian or local Wald assumptions. Pool within one candidate, then compare candidates under the objective. The reducer rejects known duplicate evidence identifiers; disjoint identifiers do not prove independence. The broader case of correlated, adaptively selected branches remains open.

### 30. How eight changes work together

**Cue: 1:20 · planned clock 32:20–33:40**

Gamma is a second finite difference of a declared scalar objective. It measures non-additivity such as synergy, conflict, or saturation, and may itself require repeated measurements. It is not mutual information or quantum interference. Define an application order or canonical composition procedure; if the patches do not compose, record a failure rather than inventing a score. Eight candidates have 28 unordered pairs, while all subsets number 256 including the empty set. Pairwise screening can guide an economical search but cannot certify every higher-order interaction.

### 31. Evaluation under adaptive search

**Cue: 1:15 · planned clock 33:40–34:55**

Access control prevents direct tampering. It does not prevent a candidate generator from adapting to repeated pass/fail or score feedback. The final reported score may then be optimistic even when every individual evaluation was computed correctly. A fresh held-out evaluation or a statistically justified adaptive procedure addresses a different failure mode from sandbox isolation. If final-validation feedback is fed back into further selection, it has become development feedback and the protocol must account for that.

### 32. The atelier as an institution

**Cue: 1:10 · planned clock 34:55–36:05**

The institution analogy has operational content: who may propose, what evidence is shared, who evaluates, and who can commit. Optimistic concurrency control offers a useful pattern of speculative work followed by validation and commitment. Our validation includes semantic tests and scientific judgments beyond database conflict checks. Promotion needs an artifact identity, an objective identity, and a fence against stale authority. The result is a workshop that can explore in parallel while maintaining an explicit record of what was accepted and why.

### 33. The implemented execution path

**Cue: 1:10 · planned clock 36:05–37:15**

The reported four-worker trace has no per-phase timing or equivalent cold-reconstruction baseline. The diagram is an operation sequence, not a proportional time chart. In particular 6.70 seconds is the total client-observed duration of concurrent restore-run-capture worker round trips, not a per-worker restore latency. The small difference between pooled and full-sample means belongs to this seed-pinned example. Keep the scope at integration, then ask what experiment could establish a useful cost improvement.

### 34. What the reducer experiments establish

**Cue: 1:20 · planned clock 37:15–38:35**

The logistic check uses five IID shards with sample sizes 60, 120, 400, 2000, and 5000. Across eight fixed seeds the information-weighted estimate is closer to the centralized maximum-likelihood estimate than equal coefficient averaging. This specific check does not establish universal efficiency or superiority to other distributed estimators. The forged-precision example motivates trustworthy information estimates, not a claim of Byzantine robustness. These are reported results from the paper; they are not new agent-task benchmark measurements.

### 35. A maintenance campaign end to end

**Cue: 1:00 · planned clock 38:35–39:35**

This is a proposed application, not a claim that Airflow currently implements this fork protocol. The concrete challenge is retry behavior when external work may already have happened. A fixture or controlled external service must make the test interpretable. We can compare several candidate implementations from the same prepared system and test their composition. The final artifact is still reviewed under the project's maintenance process. Similar patterns can motivate Spark, OpenClaw, or kernel work, but each has different device and integration boundaries.

### 36. A test that could reject the hypothesis

**Cue: 1:15 · planned clock 39:35–40:50**

This comparison has not yet been run. First establish that each path satisfies the same continuation and evaluation requirements. Then repeat over tasks and random seeds with controlled resource limits. Count setup, storage, model inference, retries, verification, and failed candidates. Report both total resources and elapsed time because parallelism trades one for the other. A path that is cheaper but changes the starting-state distribution or weakens validation is answering a different question. A result in which caching wins is scientifically useful.

### 37. Ablations that explain the outcome

**Cue: 1:05 · planned clock 40:50–41:55**

These ablations distinguish mechanisms. A fast fork with a worse search policy may lose. A communicating system may win only because it spends more model calls. Sharing can help discovery while increasing evidence dependence. Evaluate communication with an equal full resource budget and record the induced selection history. For composition, include deliberately interacting changes rather than only independent patches. Use uncertainty across tasks and seeds and reserve fresh validation for selected results.

### 38. Research questions at the runtime boundary

**Cue: 1:10 · planned clock 41:55–43:05**

These are connected research directions rather than three claims of solved problems. Checkpoint placement is a decision about future work reuse and the distribution of experience. Message routing is a decision about what information reaches a selector and what dependencies it creates. Task evolution expands the search space and can invalidate simple score comparisons. The theoretical challenge is to reason about these decisions together; the systems challenge is to expose sufficient state, cost, and provenance to support that reasoning.

### 39. Revisiting the eight candidates

**Cue: 1:00 · planned clock 43:05–44:05**

We can now answer the opening questions. Select a candidate only relative to a declared objective and adequate assessment. Treat repeated tests with their dependencies, rather than counting workers. Compose promising changes in a new controlled experiment and validate the resulting artifact. Sometimes the correct next step is another measurement, and sometimes the budget runs out with unresolved alternatives. A useful runtime should support those outcomes rather than force every campaign to report one winner.

### 40. What should a runtime expose to a learning system?

**Cue: 0:50 · planned clock 44:05–44:55**

The runtime abstraction I want us to study is a supported continuation together with the evidence and authority needed to use it. Search and learning decide which alternatives to explore. Experimental design decides what to hold fixed and what to vary. Statistical and domain-specific validation determine what the results justify. Forkable sandboxes can connect these layers when the state boundary is explicit. The research question I leave with the room is which computation would most improve the next decision, and what the runtime must reveal to answer it.
