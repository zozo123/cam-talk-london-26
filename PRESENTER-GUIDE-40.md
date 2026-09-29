# Presenter guide: AI (SW) Factories*

**Forkable Sandboxes as a Runtime for Automated Search and Development**

Yossi Eliaz · Associate Professor, Holon Institute of Technology (HIT) · Principal Engineer, Incredibuild / islo.dev

Cambridge SRG · 15 October 2026 · 15:00–16:00 BST · FW11 + Microsoft Teams

Canonical source: `talk.tex`. The PDF contains exactly 40 slides. All slide notes below come from that source. Timing cues total **44:45** and are a pacing plan, not a measured live rehearsal.

## The story

Preserve a useful computational state, explore alternatives, and turn results into justified decisions. Follow the eight-candidate example through runtime semantics, search, evidence, communication, and joint validation. Biology motivates attention to branching structure. The paper with Ori illustrates a discriminating scientific check. Evidence-aware MapReduce supplies the direct CS artifact.

## Run of show

| Slides | Segment | Duration | Cumulative |
|---|---|---|---|
| 1–5 | Problem and hypothesis | 4:30 | 4:30 |
| 6–15 | State and runtime | 10:25 | 14:55 |
| 16–22 | Search and learning | 7:55 | 22:50 |
| 23–32 | Evidence and composition | 13:05 | 35:55 |
| 33–40 | Implementation and agenda | 8:50 | 44:45 |

## Opening

“Imagine eight candidate changes. Each passes when tested from the same prepared parent. Which result should we keep, how much have we learned, and which changes can we combine? A fork helps us create those trials. The rest of the talk asks what makes their results useful.”

## Pacing when discussion starts early

Keep the opening puzzle, the continuation contract, the break-even model, the two RL loops, the three graphs, evidence reduction assumptions, composition, the measured trace, and the falsifiable benchmark. Give slides 6, 12, 13, 17, 21, and 34 a brief explanation if time is tight. Keep the physics anecdote to approximately 90 seconds. Finish by returning to the eight candidates.

## Questions to be ready for

- **Why not a build cache?** It may win. Compare against cached restart and identify which reached state cannot be reconstructed as cheaply from immutable artifacts.
- **Does a fork create independence?** It creates a separate continuation. Statistical dependence comes from the data, randomness, model, interventions, selection, and communication.
- **Can shared randomness help?** Yes, for a paired difference when the coupling preserves the intended marginals and induces helpful covariance. Independent corroboration answers a different question.
- **What if eight patches all pass?** Test the selected composition as a new artifact. Pairwise screening does not rule out higher-order interactions.
- **What is actually implemented?** The reference evidence reducer and reported snapshot-to-worker integration path. The complete runtime, routing policy, and promotion protocol are proposals.
- **What is the new performance result?** This seminar reports no new controlled speedup. The 6.70 s trace is a total client-observed worker-round-trip duration without an equivalent cold baseline.
- **How far does the physics analogy go?** The paper tests connectivity behind a projected split. It does not establish quantum interference, independent universes, or sandbox acceleration.
- **Can the evidence record solve adaptive dependence?** No. It preserves information needed to investigate the problem. A calibrated general reducer for adaptive, correlated branches remains open.

## Slide notes

### 01. AI (SW) Factories*

**Cue: 0:45 · planned clock 0:00–0:45**

We increasingly ask AI systems to develop artifacts through repeated interaction: code, models, experiments, and scientific explanations. My question is what the runtime must expose to make that process economical and accountable. I use factory with an asterisk: an atelier in which proposals are explored, compared, and refined. The argument joins three subjects: operating-system state, algorithms for allocating computation, and the evidence needed to accept a result. The biological and physical examples will each make one of those distinctions concrete.

### 02. Eight candidates pass. What can we accept?

**Cue: 1:00 · planned clock 0:45–1:45**

Imagine eight patches to one parser. All pass the available tests when applied separately to the same parent. Which one should we keep? Are eight passes eight independent confirmations? Can we merge all eight? These are three different questions. A snapshot makes it convenient to generate the trials, but does not settle any of them. Keep this example in mind: we will return to it after defining the runtime, the search policy, and the evidence contract. The eight outcomes are a thought experiment, not measurements.

### 03. Where the pattern matters

**Cue: 0:50 · planned clock 1:45–2:35**

These are application settings, not claims of deployed systems or completed benchmarks on the named projects. Biology includes analysis pipelines and simulations, whose state is computational, while wet-lab validation remains external. Scientific computing adds numerical error and model validity. Post-training adds a policy-update loop. Large open-source maintenance adds compatibility, regression risk, and human review. What unites them is a repeated experimental structure with potentially reusable preparation.

### 04. Development as iterative search

**Cue: 0:50 · planned clock 2:35–3:25**

Development here includes improving an artifact or a method, not only writing executable code. A scientific hypothesis may be ranked by evidence without being proved. A specification may be checked for consistency. A runtime executes the computational part of that work. It does not turn every domain judgment into a Boolean verifier. This distinction lets us discuss software, research, and post-training together while keeping their claims honest.

### 05. The systems hypothesis

**Cue: 1:05 · planned clock 3:25–4:30**

This is a falsifiable systems hypothesis. It can fail when setup is cheap, divergence is expensive, or verification dominates. The present implementation supports a narrower contribution: structured evidence reduction and an exercised snapshot-to-worker path. It does not yet establish a controlled end-to-end speedup. The proposed benchmark must count capture, restore, inference, failed trials, verification, memory, and communication under the same task and quality contract.

### 06. Environment, sandbox, snapshot, fork

**Cue: 1:00 · planned clock 4:30–5:30**

A sandbox is an active controlled execution boundary, while a snapshot is a representation of captured state. An environment is an interaction contract and may span multiple machines or the physical world. A VM can contain an environment, but the VM alone does not specify a task, reward, or termination rule. I use fork broadly for a supported branch of execution; I am not claiming every implementation is POSIX fork or that every resource can be copied.

### 07. What belongs to the state?

**Cue: 1:00 · planned clock 5:30–6:30**

This is a conceptual state decomposition, not a promise that one snapshot format captures all components. A VM snapshot may preserve process memory yet leave the agent's remote conversation history outside it. A copied random generator creates a coupling until streams diverge or are explicitly reseeded. External service state needs a declared policy: freeze a fixture, replay responses, recreate the service, or accept an uncontrolled dependency. The manifest makes those choices auditable.

### 08. A continuation contract

**Cue: 1:15 · planned clock 6:30–7:45**

This is a proposed observational contract. The law symbol denotes the distribution of observations under the declared continuation, not equality of every machine bit. For deterministic tests we may require exact agreement; stochastic simulations need a justified distributional criterion. Finite tests check specified observations and cannot certify every possible policy or event. Restoration fidelity, candidate quality, and scientific validity are separate axes. We establish the first before attributing an outcome to a changed candidate.

### 09. Simulation and the external world

**Cue: 1:00 · planned clock 7:45–8:45**

A branch in a simulation is a controlled computational alternative conditional on a model. A learned model may predict cheaply but brings approximation error. Neither makes the real world checkpointable. Likewise, restoring an API client does not undo an email, a database write, or a robot movement. External effects require transactions, mocks, compensation where possible, or separate authorization. The scientific question is whether the model and measurement justify the conclusion outside the captured boundary.

### 10. One running software experiment

**Cue: 0:50 · planned clock 8:45–9:35**

This is a proposed experiment, not a measured parser benchmark. Each candidate changes one implementation relative to the same identified parent. Correctness is a constraint and throughput is an objective, so a fast incorrect parser cannot win. The public development corpus and final validation material have distinct roles. Preserve the baseline and all candidate identities. Later we will ask whether two patches that pass alone still pass when composed.

### 11. The branch lifecycle

**Cue: 0:55 · planned clock 9:35–10:30**

A common shortcut in this story is to patch a file and assume a restored process now runs the new implementation. It does not. The candidate has to rebuild, reload, restart, or otherwise change the executing program. Reuse repository preparation and expensive fixtures only where the intervention leaves them valid. Content-addressed build artifacts can be shared with explicit scope and provenance. This lifecycle is also why restore latency alone is a poor measure of useful search cost.

### 12. Mechanisms for branching

**Cue: 1:00 · planned clock 10:30–11:30**

These are mechanism classes, not a performance ranking. A container image is a recipe for reconstruction rather than a live checkpoint. Process checkpointing depends on which kernel and device resources it can represent. A VM snapshot extends the boundary but still needs supported device semantics and a policy for external identity. Firecracker is a relevant microVM isolation reference, not evidence that every snapshot operation or workload has equal guarantees. A benchmark must compare equivalent required behavior.

### 13. Copy-on-write moves cost to divergence

**Cue: 0:55 · planned clock 11:30–12:25**

Copy-on-write changes when copying is paid. It can make the branch operation cheap while shifting overhead into execution. Large write sets and memory contention can erase the benefit. Sharing a prepared object also creates dependencies: its content and authorization matter. The cartoon shows eligible memory pages only; disk, devices, distributed state, and application caches may use different mechanisms.

### 14. When does branching pay?

**Cue: 1:20 · planned clock 12:25–13:45**

This additive resource model assumes both paths do the same candidate work and evaluation. Cold execution repeats P each time; branching pays it once, plus capture and per-child restore and divergence overhead. Subtracting the expressions gives the break-even inequality. The graph uses declared hypothetical units, not benchmark data. Wall-clock latency additionally depends on scheduling and parallelism. Model calls belong in W, and all unsuccessful branches and checks count. If the paths differ in candidate work, add that difference explicitly.

### 15. A runtime architecture for experiments

**Cue: 1:10 · planned clock 13:45–14:55**

This is the proposed architecture. Separate data movement from permission to accept a result. The controller owns task identity and scheduling. Workers can produce candidate artifacts and observations, while evaluation code and admission records have separate write permissions. An append-only campaign log records failures and retries. Expiring capabilities and fencing prevent an old worker from committing into a later campaign. The architecture is an interface proposal; the later trace demonstrates only a subset of this complete contract.

### 16. Stochastic improvement

**Cue: 1:00 · planned clock 14:55–15:55**

Stochastic hill climbing is the simplest policy to place above the runtime. It proposes a candidate, evaluates it, and accepts according to a rule. With noisy scores, one positive difference is weak evidence. Repeated paired comparisons or independent confirmation may be needed. Other policies can temporarily accept worse states or maintain multiple incumbents. A checkpoint does not implement an optimizer or guarantee convergence; it lowers the cost of some operations the optimizer may request.

### 17. Population search and diversity

**Cue: 1:10 · planned clock 15:55–17:05**

Genetic search operates on representations of candidates. A code crossover is a proposal for a new program; it does not merge live machines safely or inherit proof of correctness. MAP-Elites supplies a useful perspective on diversity: retain strong candidates in different behavior regions. The schematic archive has no measured values. In maintenance, behavioral dimensions might expose different compatibility or resource tradeoffs, but their choice is part of the search design and needs validation.

### 18. Branching in biological networks

**Cue: 1:15 · planned clock 17:05–18:20**

My biological work motivates asking how local connections determine global structure. The biological result and the computational proposal must remain separate. Arp2/3-mediated branching is a physical mechanism in actin networks, not an optimizer and not a software checkpoint. For our design problem, the useful analogy is controlled growth under limited resources: branch placement, interactions, pruning, and network structure matter. Flory–Stockmayer-style connectivity arguments are another bounded inspiration; their idealized bonding assumptions do not establish a critical threshold for agent success. Transition: in learning systems we can specify the growth and selection rules explicitly.

### 19. Reinforcement learning has two loops

**Cue: 1:05 · planned clock 18:20–19:25**

The inner loop is interaction: observe, act, transition, receive feedback. The outer loop uses trajectories to change policy parameters. Post-training can place a language model inside this structure, with tools and a verifier-derived reward. A fork provides a way to start or continue an episode from supported state. It does not turn branch selection into reinforcement learning by itself. Keep inference cost, environment cost, evaluation cost, and optimizer cost distinct when assessing an infrastructure benefit.

### 20. Reset changes the learning problem

**Cue: 1:05 · planned clock 19:25–20:30**

Reusing a difficult-to-reach state can make exploration productive, as return-and-explore methods illustrate. But a policy trained primarily from favorable intermediate checkpoints has seen a different starting-state distribution. We cannot silently substitute its performance for task-start performance. Depending on the algorithm, distribution correction, curriculum design, or explicit reporting may be necessary. Snapshot ancestry records where experience came from. The final evaluation should still test the deployment question we claim to answer.

### 21. Automated research chooses experiments

**Cue: 1:05 · planned clock 20:30–21:35**

Automated research includes choosing what to measure, not merely searching parameters under a fixed score. POET is a relevant example of jointly generating environments and optimizing agents, with transfer between problems. The extension here is a systems question: how do task identity and evidence remain meaningful when the search changes its own experiments? Exploratory measurements can guide future trials, but final validation needs an explicit criterion. Scores from different objective versions are not automatically comparable.

### 22. Which computation is worth buying?

**Cue: 1:15 · planned clock 21:35–22:50**

This is a metareasoning problem. Computation has a cost and changes what we know or which actions are available. An ideal controller values a computation by the expected improvement in its eventual decision, accounting for budget and dependencies. That value is generally unknown and difficult to estimate; it is not a new implemented scheduler in this artifact. A simple policy might compare predictive uncertainty, diversity, expected gain, and cost. The physics example next shows why a targeted check can be more useful than many similar trials.

### 23. Apparent branches, verified connections

**Cue: 1:30 · planned clock 22:50–24:20**

Two apparent branches in an invariant projection were interpreted as separate sets. Our continuation study tests the underlying solutions rather than treating the picture as decisive. The paper reports successful bidirectional continuation on 26 selected difficult links and independent checks of a long-range connection. The claim concerns the sampled catalog, not the global topology of all periodic orbits. For this talk the lesson is methodological: retain the state and path, then choose a check that discriminates between interpretations. This study does not measure sandbox performance or demonstrate autonomous discovery. The schematics explain that question and are not numerical figures from the study.

### 24. Repeated runs can share an error

**Cue: 1:20 · planned clock 24:20–25:40**

Expand the variance of the average into K variance terms and K(K-1) covariance terms to obtain this expression. Here all variables have marginal variance sigma squared and all distinct pairs have correlation rho. With positive rho the variance approaches a floor. This is an illustrative model, not a fitted dependence law for sandbox workers. Lineage reveals possible dependencies but cannot infer their strength. Also, variance is not bias: a shared misspecified model can be confidently wrong even if numerical noise is small.

### 25. Shared randomness can improve a comparison

**Cue: 1:15 · planned clock 25:40–26:55**

Dependence can be designed for a purpose. To compare two simulation methods, use paired random inputs so that nuisance variation cancels. The variance identity is exact; improvement over independent runs requires positive covariance and appropriate marginal sampling. Common random numbers do not always help. This is a different question from independently corroborating a scientific claim. The runtime should expose whether it preserves RNG state, reseeds, or assigns coupled streams, so the experimenter can choose rather than inherit an accidental statistical design.

### 26. Three graphs describe the computation

**Cue: 1:20 · planned clock 26:55–28:15**

Ancestry records where execution state came from, often as a tree or DAG. Communication adds edges that need not follow ancestry; these edges can introduce dependencies among later decisions. Composition concerns sets of artifacts and may need hyperedges for three-way or higher-order effects. The outline around the three candidates denotes a possible higher-order interaction, not a measured one. Keeping these structures separate avoids calling every relationship a fork. It also clarifies which metadata the controller must retain.

### 27. What does a message contribute?

**Cue: 1:25 · planned clock 28:15–29:40**

The XOR example is exact and deliberately small. Either bit alone leaves H uniformly random; together they determine H. After receiving A, B contributes one bit of conditional information. This is information synergy, not the finite-difference score interaction between two software patches. In practical search we rarely know the joint distribution well enough to compute mutual information directly. Treat it as a precise way to ask what a message could add, not a ready-made universal routing score. Useful decision information also depends on costs and available actions.

### 28. An evidence record

**Cue: 1:00 · planned clock 29:40–30:40**

This is the record shape used in the evidence-aware reduction work. Fisher information here is distinct from the Shannon quantity on the previous slide. Bind data and artifacts to trusted identities where possible. Additional evaluation and selection context belongs in metadata. The interface makes questions about provenance possible; it cannot prove a worker's reported precision is calibrated or its data are unbiased. A production system needs trusted capture and validation mechanisms beyond a schema.

### 29. Evidence-aware reduction

**Cue: 1:30 · planned clock 30:40–32:10**

These are standard precision-weighted formulas for a common target, not a new universal estimator for heterogeneous agent outputs. Exact arithmetic permits associative summary merging; floating-point implementations need tolerance checks. The reference reducer validates records and rejects repeated nonempty evidence IDs. Disjoint IDs do not prove independent errors. The asymptotic scope fixes dimension and worker count while local sample sizes grow. A general treatment of correlated, adaptively selected branches remains open; ancestry metadata is an input to that problem rather than its solution.

### 30. How eight changes work together

**Cue: 1:20 · planned clock 32:10–33:30**

Gamma is a second finite difference of a declared scalar objective. It measures non-additivity such as synergy, conflict, or saturation, and may itself require repeated measurements. It is not mutual information or quantum interference. Define an application order or canonical composition procedure; if the patches do not compose, record a failure rather than inventing a score. Eight candidates have 28 unordered pairs, while all subsets number 256 including the empty set. Pairwise screening can guide an economical search but cannot certify every higher-order interaction.

### 31. Evaluation under adaptive search

**Cue: 1:15 · planned clock 33:30–34:45**

Access control prevents direct tampering. It does not prevent a candidate generator from adapting to repeated pass/fail or score feedback. The final reported score may then be optimistic even when every individual evaluation was computed correctly. A fresh held-out evaluation or a statistically justified adaptive procedure addresses a different failure mode from sandbox isolation. If final-validation feedback is fed back into further selection, it has become development feedback and the protocol must account for that.

### 32. The atelier as an institution

**Cue: 1:10 · planned clock 34:45–35:55**

The institution analogy has operational content: who may propose, what evidence is shared, who evaluates, and who can commit. Optimistic concurrency control offers a useful pattern of speculative work followed by validation and commitment. Our validation includes semantic tests and scientific judgments beyond database conflict checks. Promotion needs an artifact identity, an objective identity, and a fence against stale authority. The result is a workshop that can explore in parallel while maintaining an explicit record of what was accepted and why.

### 33. The implemented execution path

**Cue: 1:10 · planned clock 35:55–37:05**

The reported four-worker trace has no per-phase timing or equivalent cold-reconstruction baseline. The diagram is an operation sequence, not a proportional time chart. In particular 6.70 seconds is the total client-observed duration of concurrent restore-run-capture worker round trips, not a per-worker restore latency. The small difference between pooled and full-sample means belongs to this seed-pinned example. Keep the scope at integration, then ask what experiment could establish a useful cost improvement.

### 34. What the reducer experiments establish

**Cue: 1:20 · planned clock 37:05–38:25**

The logistic check uses five IID shards with sample sizes 60, 120, 400, 2000, and 5000. Across eight fixed seeds the information-weighted estimate is closer to the centralized maximum-likelihood estimate than equal coefficient averaging. This specific check does not establish universal efficiency or superiority to other distributed estimators. The forged-precision example motivates trustworthy information estimates, not a claim of Byzantine robustness. These are reported results from the paper; they are not new agent-task benchmark measurements.

### 35. A maintenance campaign end to end

**Cue: 1:00 · planned clock 38:25–39:25**

This is a proposed application, not a claim that Airflow currently implements this fork protocol. The concrete challenge is retry behavior when external work may already have happened. A fixture or controlled external service must make the test interpretable. We can compare several candidate implementations from the same prepared system and test their composition. The final artifact is still reviewed under the project's maintenance process. Similar patterns can motivate Spark, OpenClaw, or kernel work, but each has different device and integration boundaries.

### 36. A test that could reject the hypothesis

**Cue: 1:15 · planned clock 39:25–40:40**

This comparison has not yet been run. First establish that each path satisfies the same continuation and evaluation requirements. Then repeat over tasks and random seeds with controlled resource limits. Count setup, storage, model inference, retries, verification, and failed candidates. Report both total resources and elapsed time because parallelism trades one for the other. A path that is cheaper but changes the starting-state distribution or weakens validation is answering a different question. A result in which caching wins is scientifically useful.

### 37. Ablations that explain the outcome

**Cue: 1:05 · planned clock 40:40–41:45**

These ablations distinguish mechanisms. A fast fork with a worse search policy may lose. A communicating system may win only because it spends more model calls. Sharing can help discovery while increasing evidence dependence. Evaluate communication with an equal full resource budget and record the induced selection history. For composition, include deliberately interacting changes rather than only independent patches. Use uncertainty across tasks and seeds and reserve fresh validation for selected results.

### 38. Research questions at the runtime boundary

**Cue: 1:10 · planned clock 41:45–42:55**

These are connected research directions rather than three claims of solved problems. Checkpoint placement is a decision about future work reuse and the distribution of experience. Message routing is a decision about what information reaches a selector and what dependencies it creates. Task evolution expands the search space and can invalidate simple score comparisons. The theoretical challenge is to reason about these decisions together; the systems challenge is to expose sufficient state, cost, and provenance to support that reasoning.

### 39. Revisiting the eight candidates

**Cue: 1:00 · planned clock 42:55–43:55**

We can now answer the opening questions. Select a candidate only relative to a declared objective and adequate assessment. Treat repeated tests with their dependencies, rather than counting workers. Compose promising changes in a new controlled experiment and validate the resulting artifact. Sometimes the correct next step is another measurement, and sometimes the budget runs out with unresolved alternatives. A useful runtime should support those outcomes rather than force every campaign to report one winner.

### 40. What should a runtime expose to a learning system?

**Cue: 0:50 · planned clock 43:55–44:45**

The runtime abstraction I want us to study is a supported continuation together with the evidence and authority needed to use it. Search and learning decide which alternatives to explore. Experimental design decides what to hold fixed and what to vary. Statistical and domain-specific validation determine what the results justify. Forkable sandboxes can connect these layers when the state boundary is explicit. The research question I leave with the room is which computation would most improve the next decision, and what the runtime must reveal to answer it.
