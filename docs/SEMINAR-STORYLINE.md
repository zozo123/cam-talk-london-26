# Forkable Sandboxes — connected 41-slide storyline

This outline follows the canonical `talk.tex` and its six act indexes. **41 main slides; 39:30 of timed narration; no appendix or overlays.** Each slide has one clear takeaway and a concrete visual. Detailed source scope, qualifications and follow-up questions remain in its `\qadetail` comments and the generated [presenter guide](../PRESENTER-GUIDE.md).

The spine is simple: **reuse a useful state → explore private continuations → collect observations → choose or compose → verify the exact result → authorize publication and preserve the artifact**. Different fields supply different acceptance tests. The cases establish their own results; together they motivate the runtime design.

| Act | Slides | Purpose |
|---|---:|---|
| Opportunity | 1–4 | Definition, published gains and own records |
| Cases | 5–14 | Software, genomics, physics, AI research and security |
| Design | 15–23 | State semantics, cost, effects and publication authority |
| Analysis | 24–35 | Evidence units, selection, composition and the built reducer |
| Evaluation | 36–40 | Backend choice, environmental co-failure, coverage and repeatability |
| Conclusion | 41 | Reconnect the useful results to one lifecycle |

Use the diagram before the prose. Keep three short claims on screen where possible; put the method, result and next decision in the narration. Evidence tags attach to the claim: MEASURED, BUILT, PUBLISHED or PROPOSED; illustrations state their assumptions. [Full bibliography](../REFERENCES.md), [claim boundaries](../CLAIM-FENCE.md), and [Q&A](../QA-BANK.md) carry the secondary detail.

## Act 1 — Opportunity: define the continuation and show its value

The opening takes four slides: a definition, published gains, and our own concrete record. It sets up what the rest of the seminar will explain.

### Slide 1 — Forkable sandboxes reuse execution state; each result needs verification.

**[0:45] · LIFECYCLE**

**On screen:** A reached state branches into three continuations, which return through verification and publication. Name the state, evidence and authority boundaries.

**Say:** Suppose we reproduce a failure in a running application and want several continuations from that state. We would like to preserve the useful past while giving each continuation private changes. That requires a clear account of what survives, what each result establishes, and who can publish it. We will move from software repair to genomics, physics, AI research and security, then derive the runtime and evidence rules that connect them. The goal is a checked result from a useful continuation. First, define what a sandbox fork actually supplies.

**Connection:** Define the operation before comparing its benefits.

[Slide source and full comments](../acts/1-introduction/01-title.tex)

### Slide 2 — A sandbox fork starts private continuations from one reached state.

**[1:00] · PROPOSED**

**On screen:** One captured parent → private continuations A/B/C. Choose worktrees, warm files, or a process/VM checkpoint for the state the next action consumes.

**Say:** A sandbox fork starts several continuations from one captured parent. Each continuation receives private writable state. We should choose the mechanism from the next action's requirements. Source alternatives can use worktrees. Prepared files can come from a warm image or disk snapshot. Useful process memory calls for a process or VM checkpoint with declared semantics. Hosted-model sampling stays outside the guest. SnowFlock, AgentENV, and DSec demonstrate different forms of reuse. We next compare two concrete benefits of additional executions, then examine our own workflow.

**Connection:** Show two results where additional executions created value.

[Slide source and full comments](../acts/1-introduction/02-fork-definition.tex)

### Slide 3 — Additional requests reduced latency, and additional samples raised coverage.

**[1:00] · PUBLISHED**

**On screen:** Two concrete published results: a 1,000-key BigTable read, backup after 10 ms, p99.9 latency 1,800 → 74 ms with 2% extra requests; SWE-bench Lite coverage 15.9% → 56% at 250 samples.

**Say:** Dean and Barroso sent a backup request after ten milliseconds during a thousand-key BigTable read. The 99.9th-percentile latency fell from eighteen hundred milliseconds to seventy-four, with two percent more requests. The backup could escape a server-specific delay. Brown and colleagues sampled DeepSeek-Coder-V2-Instruct on SWE-bench Lite. Coverage rose from about sixteen percent to fifty-six percent at 250 samples. Coverage means some candidate solved the issue. We still need to recognize it. Our next evidence comes from a complete factory with tests, reviews, and delivery.

**Connection:** Move from published opportunities to a complete recorded workflow.

[Slide source and full comments](../acts/1-introduction/03-published-benefits.tex)

### Slide 4 — We recorded two factory runs and implemented evidence checks.

**[1:00] · MEASURED + BUILT**

**On screen:** Two own run records: 43:44 / $10.33 and about 26 min / $3.43. Built checks: duplicate evidence IDs stop merge, lineage travels, and approval binds an artifact digest.

**Say:** We have two complete factory records. The allowlist update took forty-three minutes and forty-four seconds and cost ten dollars thirty-three. A separate delivery incident took about twenty-six minutes and cost three dollars forty-three. We also implemented duplicate-evidence rejection and lineage transport in a numerical reducer. The factory's separate gate binds approval to an artifact digest. These pieces let us trace a candidate and its supporting observations. We will follow the first work order through its task, failing test, repair, review, and publication checks.

**Connection:** Start with the concrete installer input and approved change.

[Slide source and full comments](../acts/1-introduction/04-our-records-and-checks.tex)

## Act 2 — Cases: show what was done, how, and what changed

Four software slides and six cross-domain cases provide the actual inputs, mechanisms, numerical results and acceptance decisions. Each adds a job to the shared workflow.

### Slide 5 — The installer fix added two redirect hosts across a six-file plan.

**[1:10] · MEASURED**

**On screen:** Installer redirect chain: astral.sh → releases.astral.sh → possible release-assets.githubusercontent.com fallback. Two missing destinations caused HTTP 403; the approved fix covered six files. Airflow + Docker Sandboxes + Databricks executed the work order.

**Say:** We began with the uv installer failing on islo. Its redirects reached two hosts outside a six-host allowlist, returning 403 and leaving uv unavailable. We ran the resulting work order in Docker Sandboxes through Airflow, with a hosted model served through Databricks. The plan covered six files: the Python allowlist, bootstrap, tests, deployment script, and documentation. It required the declarations to agree and the regression checks to remain hermetic. The factory then progressed through edits, harness tests, repair, review, and delivery. A failing test redirected that small task into dispatch ownership. Here is the cost of that detour.

**Connection:** Follow the detour through the recorded time and cost.

[Slide source and full comments](../acts/2-case-study/01-installer-task.tex)

### Slide 6 — Repairs and reviews consumed 59% of the recorded factory stage time.

**[1:10] · MEASURED**

**On screen:** Three-row work table: specification/plan 3:41 / $0.96; build/test 20:01 / $4.50; review 18:55 / $4.87. Two repairs and two reviews consumed 25.2 min / $7.75. Setup took 20.3 s; the calculated 100× improvement saves 20.1 s.

**Say:** We recorded forty-three minutes and forty-four seconds of elapsed time and ten dollars thirty-three of model cost. The stage records sum to forty-two minutes and thirty-eight seconds. Two repair sessions and two reviews consumed twenty-five minutes and seven dollars seventy-five. That is fifty-nine percent of stage time and seventy-five percent of model cost. These are agent-session durations, including tool activity. Initial sandbox setup took twenty seconds, eight tenths of a percent of stage time. Making it a hundred times faster would save about twenty seconds. The more substantial question is what the repair changed and what the checks established.

**Connection:** Inspect the changed behavior behind that expenditure.

[Slide source and full comments](../acts/2-case-study/02-workflow-cost.tex)

### Slide 7 — The repair added same-owner adoption without its required direct test.

**[1:05] · MEASURED**

**On screen:** The recorded diagnosis separates cell ownership from dispatch-lease ownership. The fix adopts the active cell after same-work-order `CellBusy`. Review approved without the direct test, and `service.py` changed outside the six-file plan. The suite reports 1,972 cases including skips and zero failures. Force the new path and assert one dispatch.

**Say:** The concurrency test reported zero runs from four replicas. The repair agent diagnosed one replica owning the active cell and another holding the valid dispatch lease. Its fix allowed adoption after CellBusy when the active cell belonged to the same work order. Review requested a deterministic test. The second repair refactored a helper, and review approved with that direct test still absent. The suite reported nineteen hundred seventy-two cases, including skips, and zero failures. All fifteen logged edits were allowed. We need to force the new path and assert exactly one dispatch. Next, a separate delivery incident shows why retaining the result matters.

**Connection:** Then preserve the artifact when acceptance cannot proceed.

[Slide source and full comments](../acts/2-case-study/03-adoption-test.tex)

### Slide 8 — Delivery refused three times, then cleanup erased an approved patch.

**[1:05] · MEASURED + PROPOSED**

**On screen:** Approved review → unreviewed archive → three delivery refusals → teardown loses patch. Show the separate 26-minute / $3.43 incident and three record problems: skipped evaluation marked successful, harness approval labeled human, and digest without recoverable adapter source.

**Say:** A second work order received an approved review, but delivery found our harness's own review archive outside the reviewed files. It refused three times, and teardown discarded the patch. The run took about twenty-six minutes, cost three dollars forty-three, and produced no pull request. We also found CI success with evaluation skipped, harness approval labeled human, and an adapter digest without recoverable source. These are distinct failures of recovery, record meaning, and input preservation. We propose exporting candidates and typed receipts before cleanup. The broader case set now asks how other workflows identify an observation and admit a claim.

**Connection:** Compare this proposal-to-claim distinction in genomics.

[Slide source and full comments](../acts/2-case-study/04-delivery-receipts.tex)

### Slide 9 — Six of eight drug combinations improved killing in MCF-7 cells.

**[1:00] · PUBLISHED**

**On screen:** >120,000 CRISPR guides / 19,050 genes → terrace ranking + DRACO / about 100 candidates → siRNA and drug-combination assays / MTS viability. Six of eight combinations improved killing in MCF-7. Each viability point has ≥4 technical repeats; each plot represents ≥2 experiments.

**Say:** In genomics, our goal was to find gene perturbations that make breast cancer cells more sensitive to SI-12. A genome-scale CRISPR library fed two ranking methods, which shortlisted about one hundred candidates. Separate assays then tested perturbations and drug combinations. Six of eight tested combinations improved killing in MCF-7 cells. The viability points had technical repeats, and the experiments were repeated independently. Those units answer different questions. The connection to our runtime is the separation between proposing an attractive candidate and collecting evidence about its actual effect.

**Connection:** Use physics to show how a specific numerical check settles a structural question.

[Slide source and full comments](../acts/2-case-study/05-genomics.tex)

### Slide 10 — 26 bidirectional continuations joined the projected orbit branches.

**[1:00] · MEASURED**

**On screen:** With Ori Chamo: test whether projected branches of periodic three-body orbits connect in solution space. 135,445 source orbits → 26 selected difficult links → 26 successful bidirectional continuations within one sampled component. Shooting restores periodicity; Floquet calculations assess stability; representative transitions have independent 60-digit checks. Extra-Trees proposes warm starts.

**Say:** With Ori Chamo, we asked whether two branches seen in a projected orbit diagram really belong to different solution components. We started from a catalog of one hundred thirty-five thousand unequal-mass orbits. We selected twenty-six difficult connections and used prediction followed by shooting correction, running continuation in both directions. All twenty-six connected within the sampled component. Floquet calculations then described stability, with representative transitions independently checked at sixty digits. Extra-Trees helps propose warm starts in the Atlas. The numerical checks determine which claims those proposals can support.

**Connection:** Move from numerical continuation to automated model-development experiments.

[Slide source and full comments](../acts/2-case-study/06-physics.tex)

### Slide 11 — Autoresearch kept 23 of 126 experiments and lowered its score by 2.8%.

**[1:00] · PUBLISHED**

**On screen:** Incumbent Git commit → edit `train.py` → five-minute training and `val_bpb` → keep or revert. One reported session: 126 attempts, 23 kept, 102 discarded, one crash; score 0.997900 → 0.969686, a calculated 2.8% relative reduction.

**Say:** Autoresearch gives us a very simple research loop. The agent edits training code, runs a five-minute training budget, reads validation bits per byte, and keeps or reverts the change. The evaluator stays fixed. In one reported session, 126 experiments produced twenty-three kept changes, 102 discards and one crash. The best score fell from about point nine nine eight to point nine seven zero, a relative reduction of 2.8 percent. This is sequential hill climbing through Git. The useful abstraction is an incumbent, a candidate, a fixed evaluation and a decision.

**Connection:** Scale the candidate/evaluator loop to deployed algorithm optimization.

[Slide source and full comments](../acts/2-case-study/07-autoresearch.tex)

### Slide 12 — AlphaEvolve's scheduler recovered 0.7% of Google's worldwide compute.

**[1:00] · PUBLISHED**

**On screen:** Program database → Gemini Flash/Pro proposals → validity/performance evaluators → evolutionary selection. Report two separate production endpoints: 0.7% fleet compute recovered by scheduling; 23% kernel speedup → 1% shorter Gemini training.

**Say:** AlphaEvolve makes the search population explicit. A database supplies promising programs; Gemini Flash and Pro propose edits; automated evaluators check validity and performance; evolutionary selection feeds successful programs back. DeepMind reports a scheduling heuristic that recovered point seven percent of worldwide Google compute. On a separate Gemini kernel, a twenty-three percent local speedup became a one percent training-time reduction. That distinction matters for our talk: the result should record the application-level benefit as well as the fast inner operation. The population grows through evaluated programs, not through proposals alone.

**Connection:** Now isolate state reuse itself in a mature execution tool.

[Slide source and full comments](../acts/2-case-study/08-alphaevolve.tex)

### Slide 13 — AFL++ reports 10–20× speedups from persistent process reuse.

**[1:00] · PUBLISHED**

**On screen:** Initialize target → deferred forkserver → fork once into a child. Inside that child, execute mutated inputs → collect coverage/crash → reset target state → repeat. After about 1,000 inputs, restart the child. Documentation gives typical 10–20× persistent-mode gains.

**Say:** AFL++ is a direct systems example of useful process reuse. We initialize the target, fork a child, then feed it mutated inputs. Coverage decides which inputs deserve further exploration, while crashes become candidates for investigation. Persistent mode runs about a thousand inputs in the child before restarting it. Its documentation reports typical speedups of ten to twenty times. That gain depends on correctly resetting mutable state between inputs. The forkserver saves initialization; the persistent loop avoids repeating process creation. This is where state reuse has a concrete operation, a mechanism and a reported value.

**Connection:** Follow crash generation through confirmation of a security finding.

[Slide source and full comments](../acts/2-case-study/09-fuzzing.tex)

### Slide 14 — CyberGym's GPT-5 campaign turned 56 crashes into 22 confirmed zero-days.

**[1:00] · PUBLISHED**

**On screen:** Latest-code campaign: OpenHands/GPT-5 explores 431 projects / 1,748 executables; 56 crashes → reproduction, deduplication and domain-specific validation → 22 confirmed zero-days. Separate historical benchmark: 1,507 patched vulnerabilities / 188 projects; candidate input must crash the vulnerable version and not the patched version.

**Say:** CyberGym shows why exploration needs a second decision after execution. In its latest-code campaign, OpenHands with GPT-five explored 431 OSS-Fuzz projects and 1,748 executables. It produced fifty-six crashes, which validation reduced to twenty-two confirmed zero-day vulnerabilities. Separately, its historical benchmark covers 1,507 known vulnerabilities and tests that a reproduction triggers the vulnerable version but not the patched version. Across these cases, candidates become accepted results through domain-specific checks. We can now choose what starting state an execution runtime should preserve.

**Connection:** Choose what starting state the runtime should preserve, then specify its contract.

[Slide source and full comments](../acts/2-case-study/10-security-discovery.tex)

## Act 3 — Design: make the state and publication contract explicit

Choose the state surface; verify capture; assign authority; account for external effects and cost; bind the returned artifact to the controller’s decision.

### Slide 15 — Worktrees, checkpoints, and replay preserve different kinds of state.

**[0:55] · PUBLISHED**

**On screen:** A state-to-tool table: source/build inputs → worktrees/OBuilder; process state → CRIU/gVisor; VM state → Xen/SnowFlock/Firecracker; recorded observations → rr/DSec. Match the mechanism to what the continuation consumes.

**Say:** The first design choice is the state surface. Worktrees preserve files. Process checkpoints preserve supported process state. Virtual machine snapshots preserve their declared memory and device state. Replay preserves recorded observations. Each gives a continuation something different. If we edit loaded application code, we may need a reload or restart, which can destroy the state we hoped to reuse. We should first identify what the continuation consumes, then choose a mechanism and a faithful baseline. That distinction also explains the published latency figures.

**Connection:** Keep state surfaces explicit when reading published latency numbers.

[Slide source and full comments](../acts/3-design/01-state-surfaces.tex)

### Slide 16 — DeltaBox checkpoints in 10.83 ms; SnowFlock forks remotely in 600–800 ms.

**[0:55] · PUBLISHED**

**On screen:** The timing table retains operation names: DeltaBox checkpoint 10.83 ms; Kimi minimum checkpoint/resume 133/49 ms; Shepherd fork 134–143 ms; SnowFlock remote fork 600–800 ms; Firecracker boot under 125 ms. Time delivery of equivalent usable state.

**Say:** DeltaBox reports a ten point eight three millisecond checkpoint. SnowFlock reports six hundred to eight hundred milliseconds for a remote fork across hosts. Between those endpoints, Kimi reports minimum checkpoint and resume times, Shepherd reports fork time, and Firecracker reports boot to application code. The operation labels are the useful part: each runtime pays for a different state transition. A fair comparison reaches equivalent usable state and accounts for the same workflow costs. We first choose the state our continuation needs, then measure delivery of that state. The next check asks what actually survives restoration.

**Connection:** Test which state survives our own restoration path.

[Slide source and full comments](../acts/3-design/02-published-latencies.tex)

### Slide 17 — A RAM-only 128-bit nonce tests memory restoration in three children.

**[0:55] · PROPOSED**

**On screen:** RAM-only 128-bit nonce → capture → three children → process-alive and nonce checks. Distinguish filesystem restoration, process/memory restoration, and fidelity of the declared semantic properties.

**Say:** Here is the restoration experiment. A process generates a hundred twenty-eight bit nonce and holds it only in RAM. Capture that state, restore three children, and check that each child has the live process and the same nonce. Files surviving establishes a filesystem path. The process and nonce surviving adds evidence for the memory path. Then compare the declared deterministic behavior against direct execution, with workload-specific checks for writes, clocks, randomness and sockets. Gate zero is preregistered and awaits execution. It gives us a concrete way to label the state our API actually preserves.

**Connection:** Give restored children private writes and current permissions.

[Slide source and full comments](../acts/3-design/03-restore-fidelity.tex)

### Slide 18 — Each child needs private writable state and host-controlled authority.

**[0:55] · PUBLISHED + PROPOSED**

**On screen:** Shared immutable parent/cache, private child writes, host authentication and authorization, controller-held publication credential. Copied bearer tokens require authority treatment beyond kernel isolation.

**Say:** A child needs private writable state, while an immutable cache can be shared within a declared trust domain. It also needs authority assigned outside the copied guest state. A guest generation string and a bearer token can both be cloned. The host must authenticate and authorize the child, with an epoch, expiry and budget. The publishing credential stays with the controller, bound to a specific artifact decision. Kernel isolation is valuable, but it addresses a different boundary from permission to act.

**Connection:** Extend the boundary to effects already sent outside the child.

[Slide source and full comments](../acts/3-design/04-child-authority.tex)

### Slide 19 — Restoring local state does not undo completed external actions.

**[0:55] · PUBLISHED + PROPOSED**

**On screen:** A table distinguishes model requests, remote tool actions and staged patches. Local restore cannot reverse completed external actions. Proposed journals/buffers use idempotency or reconciliation; every exit exports artifacts and receipts.

**Say:** Restoration brings back local state. It cannot unsend a model request, recover its cost, or reverse a remote tool action that already happened. Some outputs can be staged until verification; other effects need a journal, idempotency or reconciliation when the outcome is uncertain. Earlier recovery systems show ways to delay output, but a general effect buffer is still proposed here. We also export the patch and evidence before every teardown. This gives the runtime obligations beyond merely creating a child.

**Connection:** Account for the costs of creating and preserving continuations.

[Slide source and full comments](../acts/3-design/05-external-effects.tex)

### Slide 20 — Forking saves resources when avoided preparation exceeds reuse overhead.

**[0:55] · PUBLISHED**

**On screen:** Additive resource condition: `(N−1)P > H + N(R+D)`. Illustrative N=8: avoiding 210 resource-seconds while adding 34 saves 176; warm-cache preparation reduces avoided cost to 14 and loses 20. Batch elapsed time remains a separate endpoint.

**Say:** The resource condition compares preparation avoided with reuse overhead. Eight children and thirty resource-seconds of preparation avoid two hundred ten, while capture, restore and divergence add thirty-four. With a warm cache, preparation can fall to two and the same reuse path loses twenty. These are illustrative calculations. Ordinary continuation work cancels; elapsed time depends on the critical path and contention. In our file-edit case, worktrees could also provide parallelism. The twenty-second setup measurement is not a measurement of the full reusable prefix.

**Connection:** Compare that model with the API workflows actually exercised.

[Slide source and full comments](../acts/3-design/06-reuse-cost.tex)

### Slide 21 — islo completed 255/256 restore–run–capture calls, median 6.87 s.

**[0:55] · MEASURED**

**On screen:** Exercised API table: Daytona create 1,024/1,024, p50 0.20 s; Tensorlake create 256/256, p50 3.44 s; islo restore/run/capture 255/256, p50 6.87 s, p95 9.04 s. Snapshot 141 MB; islo concurrency 12; creation paths requested 8; teardown excluded.

**Say:** The islo trace completed two hundred fifty-five of two hundred fifty-six restore, run and capture calls. Its median was six point eight seven seconds, and its ninety-fifth percentile was nine point zero four seconds. The input was a named hundred forty-one megabyte snapshot, with concurrency twelve. Daytona and Tensorlake exercised creation at requested concurrency eight; their endpoints are shown separately. Teardown is outside these percentiles. Memory preservation still needs the nonce probe. These traces establish concrete API paths and costs; the next experiment asks whether that reuse path beats a faithful warm alternative.

**Connection:** Place candidates, receipts and publication into one architecture.

[Slide source and full comments](../acts/3-design/07-api-traces.tex)

### Slide 22 — The controller binds repository publication to a candidate digest.

**[0:55] · BUILT + PROPOSED**

**On screen:** Solid path: Airflow scheduler → Docker cell → candidate digest → controller gate → repository. Dashed extensions: fork store and external evaluator returning artifact-bound receipts. The controller holds the publication decision.

**Say:** The solid path is the factory architecture we exercised. Airflow schedules a Docker work cell. The cell returns a candidate identified by its digest. The controller binds approval to that artifact before repository publication. The journal records the decisions along the path. The dashed extensions place a fork store beside execution and an external evaluator beside candidate verification. Those extensions are designed rather than integrated. A numerical reducer was built separately for measurement summaries. The architectural connection is concrete: candidates and artifact-bound receipts return to the controller, which holds the publication credential and decides whether the exact candidate may proceed.

**Connection:** Add the authority rule for a worker restored after replacement.

[Slide source and full comments](../acts/3-design/08-component-status.tex)

### Slide 23 — An epoch check rejects the old instance after worker replacement.

**[0:55] · PROPOSED**

**On screen:** Worker epoch 1 → replacement advances epoch to 2 → delayed epoch-1 publication rejected. A concurrent child receives a separate worker identity. Approval names one frozen artifact; authority is checked outside restored state.

**Say:** A logical worker starts with authority at epoch one. When the controller replaces that worker, it advances the current epoch to two. A delayed publication from the old instance carries epoch one, so the controller rejects it. Approval also names the frozen artifact, and the controller checks scope, expiry and budget. A concurrent fork receives a new worker identity and its own epoch; the parent may continue with its existing authority. This epoch protocol has a TLA plus design and still needs model and implementation checks. Execution can preserve state while publication remains a current controller decision.

**Connection:** Separate the decisions we make about returned objects.

[Slide source and full comments](../acts/3-design/09-epoch-fence.tex)

## Act 4 — Analysis: match evidence to the decision

Separate selection, composition and common-target pooling. Keep observation identities, feedback and joint outcomes visible, then demonstrate the built reducer’s useful behavior and trust boundary.

### Slide 24 — Selection, composition, and pooling require different evidence.

**[0:50] · BUILT + PROPOSED**

**On screen:** Three lanes: different patches → select and validate one; compatible patches → compose and test resulting bytes; measurements of one target → reduce with calibrated information and a dependence model. The implemented reducer occupies the measurement lane.

**Say:** There are three different uses of branching. We may choose among different patches, compose compatible patches, or pool measurements of one target quantity. The evidence required by each decision differs. A numerical score for a patch is not automatically an information estimate, and the reducer does not select patches. Our implemented reducer occupies the measurement lane under stated assumptions. The scientific and security cases illustrate the same separation between candidates, executed checks and accepted claims. Next, consider what repeated checking can establish.

**Connection:** Name the population behind any continuation-success rate.

[Slide source and full comments](../acts/4-analysis/01-three-result-lanes.tex)

### Slide 25 — Checkpoint-started success is conditional on reaching that checkpoint.

**[0:50] · ILLUSTRATION / ANALOGY**

**On screen:** Task start → reached checkpoint → continuations. Illustration: 50% reaches the checkpoint, 80% succeeds given it, so end-to-end success is 40%. Retain both checkpoint and task-start populations.

**Say:** If a workflow reaches a checkpoint half the time and then succeeds with probability point eight, the corresponding end-to-end success probability is point four. Starting directly from the checkpoint observes point eight. That is a conditional question. It does not estimate how often we reach that state or establish every earlier choice. Go-Explore makes returning to reached states explicit. For our evaluation, we need to name both the checkpoint population and the task-start population, and retain which feedback shaped the candidate.

**Connection:** Retain the feedback that helped create the candidate.

[Slide source and full comments](../acts/4-analysis/04-conditional-success.tex)

### Slide 26 — Repair tests and generalization tests support different claims.

**[0:50] · MEASURED + PUBLISHED**

**On screen:** Failed test → repair → review feedback → repair again → frozen artifact. A regression receipt supports its asserted behavior; a claim about generalization or selection needs an appropriate untouched evaluation.

**Say:** The repair sequence exposes failed tests and review feedback to the candidate. That is useful development. A regression check can still establish the deterministic behavior it actually asserts on that artifact. Claims about generalization or selection performance require a suitable evaluation beyond the development feedback. Adaptive-analysis work explains why reuse changes the interpretation. In our case, one hosted model performed the roles, but we did not estimate their dependence. The next slide separates three questions that a single green receipt cannot answer.

**Connection:** Separate execution, required coverage and broader inference.

[Slide source and full comments](../acts/4-analysis/05-development-feedback.tex)

### Slide 27 — A check can run correctly and still miss the required behavior.

**[0:50] · MEASURED + PROPOSED**

**On screen:** Three questions applied to adoption: did the check execute on this digest; did it force `CellBusy` adoption and assert one dispatch; what broader claim can repeated outcomes support? Identity, coverage and statistical support require separate mechanisms.

**Say:** Apply three questions to the same-owner adoption candidate. First, did a check execute on this exact artifact? Second, did it deliberately exercise the new path and assert one dispatch? Third, what broader claim does the collection of outcomes support? Artifact binding addresses the first; a targeted test the second; a suitable sampling design the third. The observed gap belongs to coverage. Rejecting duplicate evidence is useful, but it cannot discover an assertion that was never written.

**Connection:** Record observations with their actual case and ancestry identities.

[Slide source and full comments](../acts/4-analysis/06-three-evidence-questions.tex)

### Slide 28 — Four runs of 100 cases produce 400 outcomes in 100 case clusters.

**[0:50] · ILLUSTRATION / ANALOGY**

**On screen:** 100 case identities fan out to four runs: 400 observation IDs retain 100 shared case IDs and ancestry. A fresh outcome gets its own observation ID; a copied receipt retains its original identity.

**Say:** Consider one hundred benchmark cases, each evaluated in four runs. We collect four hundred outcomes but retain one hundred case identities. A fresh stochastic evaluation gets a new observation identifier and keeps its case, candidate and ancestry labels. Those labels let us ask whether our variation comes from cases, repeated measurements or related continuations. The genomics case used the same distinction between technical repeats and independent experiments. A ledger preserves those relationships so that later analysis can use the appropriate unit. Next, we quantify one consequence of shared variation.

**Connection:** Quantify one consequence of shared variation for a mean.

[Slide source and full comments](../acts/4-analysis/07-fresh-observations.tex)

### Slide 29 — At correlation 0.1, 100 measurements have the mean precision of about nine.

**[0:50] · ILLUSTRATION / ANALOGY**

**On screen:** Under equal variances and common pairwise ρ: `Var(mean)=σ²[ρ+(1−ρ)/N]`. For N=100, ρ=0.1 gives variance-equivalent N_eff≈9.17. The quantity is precision of a mean.

**Say:** For a mean, we can show exactly how an assumed dependence affects precision. With equal marginal variances and common correlation point one, one hundred measurements have the variance-equivalent precision of about nine independent measurements. The variance stops shrinking toward zero because of the shared component. This is a calculation under stated assumptions. It is not a probability that the answer is correct, and shared bias remains. Published judge panels provide context, not a measurement of fork effects. Candidate search requires a different joint quantity.

**Connection:** Switch from mean precision to the joint event that limits search.

[Slide source and full comments](../acts/4-analysis/08-variance-equivalent-count.tex)

### Slide 30 — Zero pairwise correlation does not fix the all-wrong probability.

**[0:50] · ILLUSTRATION / ANALOGY**

**On screen:** Three exactly enumerated error distributions have 50% individual error and zero pairwise correlation, but all-wrong probabilities 0%, 12.5% and 25%. Search depends on the joint failure event and on recognizing an available correct candidate.

**Say:** Here are three exact joint distributions. Each candidate is wrong half the time and every pair has zero correlation. Yet the probability that all three are wrong is zero, one eighth or one quarter. A selector cannot return a correct member when all members are wrong, and must still recognize one when it exists. The effective-size formula for a mean therefore cannot answer the search-coverage question. We need the joint failure behavior, not only a pairwise statistic.

**Connection:** Use shared variation constructively when estimating a difference.

[Slide source and full comments](../acts/4-analysis/09-search-joint-errors.tex)

### Slide 31 — Shared conditions can reduce uncertainty in a paired comparison.

**[0:50] · PUBLISHED + PROPOSED**

**On screen:** Paired comparison on the same case: `Var(A−B)=Var(A)+Var(B)−2Cov(A,B)`. Positive shared variation can reduce uncertainty in a difference. Record ancestry, fixtures, tests and feedback; control the randomness actually consumed.

**Say:** Sharing can be useful when our quantity is a difference. Compare A and B under matched conditions: positive shared variation can reduce the variance of A minus B. That is the reason for paired comparisons and common random numbers. The relevant randomness must actually be controlled; cloning a guest seed does not control a hosted model. An ancestry tree is also incomplete, because fixtures, tests, retrieval and feedback can link executions. The runtime should retain these relationships and let the evaluation question determine how to use them.

**Connection:** Then distinguish comparing candidates from composing their artifacts.

[Slide source and full comments](../acts/4-analysis/10-paired-comparisons.tex)

### Slide 32 — Passing every pair does not establish that the full composition passes.

**[0:50] · ILLUSTRATION / ANALOGY**

**On screen:** Capacity example: each patch adds one worker; all singles and pairs fit capacity two; all three fail. Eight candidates have 28 pairs and 256 subsets. Test the exact selected composition and bind its digest.

**Say:** Three patches each enable one worker. Every single patch and every pair fits within capacity two. The full composition does not. With eight candidates there are twenty-eight pairs but two hundred fifty-six subsets, so pair checks can miss higher-order interactions. Publication concerns the actual artifact we selected, not an assortment of individually green parts. We must rebuild and test that composition and bind the receipt to its digest. Statistical reduction of measurement summaries does not solve this artifact problem.

**Connection:** Show what the implemented numerical lane enforces.

[Slide source and full comments](../acts/4-analysis/11-exact-composition.tex)

### Slide 33 — The reducer rejects a repeated evidence ID and carries lineage forward.

**[0:50] · BUILT**

**On screen:** Result record: estimate, information, n, evidence IDs, lineage, metadata. Two summaries declaring the same evidence ID cause merge to raise. Distinct summaries combine and retain lineage under the common-target model.

**Say:** The reference reducer makes one ledger rule executable. A result records its estimate, information, sample count, evidence identifiers and lineage. If two results declare the same evidence identifier, merging them raises an error. Distinct observations can merge numerically, and their lineage travels with the combined record. The algebra assumes a common target and calibrated information; carrying ancestry makes later dependence analysis possible, but does not perform it automatically. This gives us a concrete implementation to test, beginning with ordinary uneven shards and then a deliberately inflated weight.

**Connection:** Test the numerical reducer on uneven synthetic shards.

[Slide source and full comments](../acts/4-analysis/12-built-reducer.tex)

### Slide 34 — Information pooling reduced the synthetic MLE gap from 0.177 to 0.0083.

**[0:50] · MEASURED**

**On screen:** Five logistic shards, n=60,120,400,2,000,5,000. Across eight fixed seeds, mean norm gap to centralized MLE: information pooling 0.0083 ± 0.0042 versus equal averaging 0.177 ± 0.090. Whiskers are SD.

**Say:** We split a synthetic logistic-regression dataset into five uneven shards, from sixty observations to five thousand. Equal averaging gives the smallest shard the same influence as the largest. Information pooling uses each shard's estimated precision. Across eight fixed seeds, its mean distance to the centralized maximum-likelihood estimate was point zero zero eight three, compared with point one seven seven for equal averaging. The whiskers show standard deviations. This is a concrete check of the numerical reducer under a common-parameter model. The next stress case asks what happens when the reported precision is inflated.

**Connection:** Stress the assumption that reported information is trustworthy.

[Slide source and full comments](../acts/4-analysis/13-synthetic-pooling.tex)

### Slide 35 — Inflated reported precision pushed the synthetic pooled estimate to 17.0004.

**[0:50] · MEASURED**

**On screen:** Synthetic 2,000-point shard reports a distant estimate and 50× inflated information. Unprotected pooled estimate: 17.0004; stress heuristic: 4.9566. Evidence identity and justified weight are separate requirements.

**Say:** A worker can report a real sample count and still inflate the strength of its evidence. In this synthetic stress case, a two-thousand-point shard returns a distant estimate and fiftyfold reported precision. Unprotected pooling moves to seventeen. A heuristic returns about four point nine six, without a Byzantine guarantee. Sample count alone does not detect the attack. Information needs trusted recomputation under the numerical model, while agent scores need their own validated error model. We now have enough structure to state the experiments and the acceptance policy.

**Connection:** Turn the obligations into a concrete acceptance policy.

[Slide source and full comments](../acts/4-analysis/14-forged-information.tex)

## Act 5 — Evaluation: let an experiment change a runtime decision

H1 chooses a preparation backend. H2 tests environmental co-failure. A dated analysis amendment resolves linked experimental units; targeted coverage and repair resampling answer separate questions.

### Slide 36 — The publication gate requires the adoption test on the exact candidate.

**[1:10] · PROPOSED**

**On screen:** Candidate/scope → force adoption and assert one dispatch → receipt naming exact digest → current authority. An unmet obligation retains the candidate. If selected patches are composed, verification follows composition. Export on refusal.

**Say:** We can turn the case into a precise acceptance policy. The candidate added a same-owner adoption path. Before publication, we freeze that candidate, deliberately force the path, and assert that one dispatch occurs. The receipt must name the artifact we actually tested. If we combine candidates, we test that exact combination again. The controller then checks current authority and approval for that digest. A refusal retains the patch and its receipts. This resolves a concrete missing obligation; it does not yet establish how well an ensemble generalizes.

**Connection:** Let the first experiment choose the preparation mechanism.

[Slide source and full comments](../acts/5-evaluation/01-obligation-gate.tex)

### Slide 37 — 20 batches at each fan-out compare restore with a warm cached template.

**[1:10] · PROPOSED**

**On screen:** Proposed H1: warm cached template versus restore after setup and a warm test; N={3,6,12}, 20 interleaved batches per arm/N. No model calls. Endpoint: request to the last child’s first test result. Establish fidelity and report failures/capture cost.

**Say:** The first experiment asks which execution mechanism we should choose. We compare restore after setup and a warm test with a cached template that already has dependencies. For three, six and twelve children, we interleave twenty batches per arm and measure the time until the last child produces its first test result. There are no model calls. We establish capture semantics first and expose failures and capture cost. A win informs the backend choice for this workload. To claim a benefit from live memory, we also need useful running state and an equivalent warm reconstruction baseline.

**Connection:** Ask whether common captured ancestry affects environmental failures.

[Slide source and full comments](../acts/5-evaluation/02-cost-experiment.tex)

### Slide 38 — 12 snapshot families compare sibling and separately prepared co-failures.

**[1:10] · PROPOSED**

**On screen:** Proposed H2: 12 independently prepared snapshot families, three siblings each, versus restored children from separately prepared families; matched host/start slot and ≥300 lockstep race rounds. Record binary outcomes and failure classes; confirm the test consumes a captured varying feature.

**Say:** The second experiment asks whether captured ancestry changes environmental failure patterns. Twelve independently prepared families each supply three siblings. We compare them with three restores from other families, matched by host and start slot, over at least three hundred race-test rounds. We record failure classes as well as binary outcomes. Before collecting data, we must identify a varying parent-state feature that is preserved and actually consumed. If the test rebuilds the relevant state, it removes the treatment. This is an environmental experiment; the hosted model remains outside the guest snapshot.

**Connection:** Choose an analysis that respects the actual experimental units.

[Slide source and full comments](../acts/5-evaluation/03-sibling-experiment.tex)

### Slide 39 — At correlation 0.10, nine outcomes have a variance-equivalent count of five.

**[1:10] · PROPOSED**

**On screen:** Reused families link comparisons; repeated rounds may share temporal effects. The proposed amendment declares independent blocks or a justified dependence model before collection. At N=9, absolute ρ=0.10 gives N_eff=5.00; ρ=0.15 gives 4.09.

**Say:** The comparison design determines the analysis. In the recorded protocol, families recur in several comparisons and the same cells run many rounds. We cannot treat twelve differences as independent by default. Before collection, we need independent blocks or a model that handles these links and time dependence. The example shows why baseline dependence also matters: nine measurements at correlation point one carry five independent measurements' variance-equivalent precision. Raising correlation to point fifteen gives about four point one. These are illustrative calculations, not outcomes. We retain the original preregistration and identify the amendment explicitly.

**Connection:** Return to the repair with a targeted test and a separate repeatability study.

[Slide source and full comments](../acts/5-evaluation/04-dependent-analysis.tex)

### Slide 40 — One adoption test checks dispatch; nine repair samples measure repeatability.

**[1:10] · PROPOSED**

**On screen:** Two procedures: freeze digest → force same-owner `CellBusy` → assert exactly one dispatch; separately fix input/prompt/policy → nine repair samples → record scope edits and distinct diffs. One checks behavior; the other describes repeatability.

**Say:** We end the experiment plan where the software case began. Freeze the candidate, force same-owner CellBusy, and assert exactly one dispatch. That is the acceptance obligation for the new behavior. Separately, run nine repair samples from fixed inputs, prompt, policy and hosted endpoint. Record which samples edit outside the planned scope and how many distinct diffs they produce. Those samples describe repair repeatability. The public substitute input and the full protocol are retained in the notes. Together, the procedures distinguish a check on a concrete artifact from a measurement of the process that generated it.

**Connection:** Close by connecting state reuse, evidence handling and exact-result verification.

[Slide source and full comments](../acts/5-evaluation/05-test-and-resample.tex)

## Act 6 — Conclusion: return a verifiable result

The closing reconnects the concrete state, evidence and verification results to the proposed lifecycle.

### Slide 41 — Reuse the useful state, retain the evidence, and verify the exact result.

**[1:10] · LIFECYCLE**

**On screen:** Return to the full lifecycle. State: AFL++ 10–20×; evidence: synthetic MLE gap 0.177 → 0.0083; verification: CyberGym 56 crashes → 22 findings. Reuse useful state, preserve exact artifacts and evidence, and let current authority approve publication.

**Say:** The story comes back to one useful reached state and several possible continuations. AFL plus plus shows a concrete performance gain from process reuse. Our synthetic reducer shows why the strength and identity of returned measurements matter. CyberGym shows the distance between a generated crash and a confirmed finding. Software repair adds the last boundary: the exact tested artifact must survive export, and current authority must approve its publication. These are separate results supporting one design. The next systems experiment compares faithful restore with equivalent warm reconstruction. The goal is useful continuations that return inspectable evidence and a verifiable artifact.

**Connection:** The next systems experiment chooses faithful restore or equivalent warm reconstruction.

[Slide source and full comments](../acts/6-conclusion/01-final-contract.tex)

## Record and next step

`PREREGISTRATION.md` remains unchanged. H2 analysis changes are **proposed dated amendments before collection**, rather than silently revised decision rules. No unrun experiment has a reported outcome. The public pre-repair substitute still needs equivalence qualification.

The original deck’s source bibliography remains complete in `REFERENCES.md`. Older end-matter and archived slides are historical source material outside this 41-slide build. The generated presenter guide retains the detailed facts that were moved into comments, including run receipts, numerical assumptions, published endpoint definitions and domain limits.

The next useful systems result compares a faithful restore path with a warm alternative that supplies equivalent usable state. In parallel, the targeted adoption test checks the concrete disputed behavior, while a separate repair-resampling study describes the generation process. Each procedure changes a named runtime decision.
