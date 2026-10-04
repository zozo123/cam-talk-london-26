# Two-sentence slide takeaways

Takeaways for the [57-slide Cambridge seminar](dist/forkable-sandboxes-cambridge.pdf), in the final deck order. Each title links to its slide source.

## 01. [Forkable sandboxes let computers explore executable alternatives.](acts/1-introduction/01-title.tex)

The proposed system saves useful execution state, runs private alternatives, and returns each candidate with the evidence needed to evaluate it. Reuse can lower the cost of exploration, but the controller still needs a clear rule for choosing, combining, and accepting results before continuing.

## 02. [My work led from securing software and modeling cells to self-driving compute.](acts/1-introduction/02-research-path.tex)

The speaker’s work connects software security, biological modeling, drug experiments, gene-editing predictions, and road perception to a question about reusable computation. These projects use different mechanisms, but they repeatedly show why observations must inform the next action and why a proposed action needs a meaningful check.

## 03. [Twistlock learned container behavior and enforced the resulting model.](acts/1-introduction/02-container-security.tex)

Twistlock learned expected processes, file access, network activity and system calls for each container image, then could alert on or block deviations. Its vendor-reported learning plateau of roughly one hour illustrates a feedback loop in which recorded execution shapes a policy for later actions.

## 04. [Graph measures link protein binding to actomyosin self-organization.](acts/1-introduction/03-physics-origin.tex)

In the reported simulations, representing filaments as nodes and protein links as edges showed that more binding sites promoted bundles and larger clusters. Graph measures made physical self-organization measurable across 600-second runs and 30 random starts, connecting local binding rules to larger structures.

## 05. [POSSUMM computed 500-bp chromosome compartments with 23 GB of RAM.](acts/1-introduction/04-genome-algorithms.tex)

POSSUMM extracted chromosome 1’s active/inactive compartment pattern at 500-base-pair resolution in 2.5 minutes using 23 GB of RAM, avoiding an explicitly dense correlation matrix. Sparse computation made this analysis practical compared with a projected dense requirement above 4.6 TB, illustrating that a better representation can matter as much as more hardware.

## 06. [ENCODE recorded how each result came from its input data.](acts/1-introduction/05-encode-pipelines.tex)

ENCODE’s uniform analysis pipelines processed more than 14,000 datasets while connecting outputs to their input files, software versions, and quality checks. Those records let others inspect and repeat the computation, although knowing a result’s origin does not by itself establish that the biological conclusion is correct.

## 07. [Computer predictions guide gene-editing experiments, then learn from them.](acts/1-introduction/05-crispr-design.tex)

CRISPR-IL used measured gene-editing outcomes to update predictions, while the separate OffRisk example annotated 118 predicted DNA matches and flagged four unintended sites for higher priority. Computer screening can focus researcher-run experiments, but an annotation or prediction still needs laboratory follow-up to establish what actually happens.

## 08. [Researchers chose a drug pair to test.](acts/1-introduction/05-immune-response.tex)

Researchers compared ten drugs in mouse breast-cancer cells and selected abemaciclib plus SI-2, which preserved cell killing while reducing the PD-L1 rise. Ten drugs allow 45 two-drug pairs at one dose each, but only selected follow-ups were tested, illustrating a researcher-directed search rather than an exhaustive combination screen.

## 09. [300 million cars build Mobileye's Roadbook.](acts/1-introduction/06-self-driving-systems.tex)

At the speaker-reported scale of 300 million equipped cars, Mobileye’s Roadbook aligns anonymized observations of the same roads and sends the combined map back to vehicles. The separately reported 2025 mapping total of 34 billion road-miles averages about 1,080 road-miles per second, describing aggregate driven distance rather than each car’s upload rate.

## 10. [Forkable computation lets us try different futures from the same state.](acts/1-introduction/02-executable-search.tex)

The proposed execution model saves a reached state, tries different next actions and advances with a continuation whose result passes the required checks. Sharing the starting point lets us compare alternative futures while keeping each trial’s writable changes private and its completed external effects explicitly recorded.

## 11. [The forkable API prepares once and runs alternatives in private children.](acts/1-introduction/02-control-comparison.tex)

The proposed API evaluates the same three edits and checks as the example Python loop, while making one preparation and three private continuations explicit. Its value depends on what the captured state preserves and what each result proves, since ordinary Python can also implement reuse and the sketch establishes no measured speedup.

## 12. [Caching lets repeated experiments reuse their expensive build work.](acts/1-introduction/07-build-reuse.tex)

The author-reported Tokio demo took about 46 seconds for a fresh compile, 13 seconds after restoring saved build files and three seconds when those files were already available. A hot cache is therefore a strong alternative to restoration, so a reuse claim should compare against the preparation the next trial actually needs.

## 13. [An agent changes the environment that executes its next experiment.](acts/1-introduction/08-agent-execution.tex)

In the recorded software factory, an agent edited files and ran tools in a sandbox, using test and review feedback to decide its next action. The environment becomes part of the experiment because one accepted change affects later runs, and this serial record motivates a proposed design with private alternative continuations.

## 14. [A sandbox is a policy boundary; VMs and containers are implementation choices.](acts/1-introduction/08-runtime-layers.tex)

A VM supplies a guest kernel, a Linux container isolates processes sharing a kernel, and a sandbox defines which accesses and actions execution may perform. Choosing a backend therefore requires checking its isolation, resource limits, and permitted effects separately, rather than assuming that one label answers all three questions.

## 15. [A fork creates private continuations from one captured execution state.](acts/1-introduction/10-fork-definition.tex)

A fork creates multiple continuations from captured state, gives each private writable changes, and returns its artifact and observations. The backend must specify whether it preserves files, processes, or memory, while remote effects and permission to publish require separate handling outside the child’s private state.

## 16. [Different fields use the same pattern: explore alternatives, then check the results.](acts/2-case-study/00-examples-overview.tex)

Security, AI, genomics, physics, and software repair all explore changed trials and gather their results, although their execution mechanisms and available checks differ. The useful common questions are what setup can be shared, what each trial changes, and which rule turns the returned results into an accepted output.

## 17. [AFL++ finds bugs by changing inputs and reusing the initialized program.](acts/2-case-study/01-fuzzing-state.tex)

AFL++ mutates inputs, keeps those that reveal new code paths, and records crashes while a persistent child reuses initialized program state across many inputs. Correctly resetting mutable state between inputs, and periodically replacing the child, is essential because a faster testing loop is useful only when earlier inputs do not contaminate later ones.

## 18. [AFL++ reports 10–20 times faster execution in persistent mode.](acts/2-case-study/02-fuzzing-speed.tex)

AFL++ documentation reports typical 10–20-fold speedups for persistent mode, which spreads process-creation cost across many inputs executed by one child. The gain depends on the target and a correct state reset, so greater throughput creates more testing opportunities without guaranteeing independent observations or validated vulnerabilities.

## 19. [250 samples raised SWE-bench Lite coverage from 15.9% to 56%.](acts/2-case-study/03-sampling-coverage.tex)

In the published SWE-bench Lite experiment, increasing DeepSeek-Coder-V2-Instruct sampling from one attempt to 250 raised the fraction of tasks with at least one correct patch from 15.9% to 56%. More attempts can uncover useful candidates, but that coverage gain becomes useful in practice only if the selection process recognizes an acceptable patch.

## 20. [Autoresearch kept 23 experiments and lowered validation bits per byte.](acts/2-case-study/04-autoresearch.tex)

In one reported sequential session, Autoresearch kept 23 of 126 attempts and lowered validation bits per byte by 2.8% while holding the evaluator fixed. Recording the candidate, executed evaluation and keep-or-revert decision makes improvement traceable, while a separate held-out check is still needed to test whether repeated selection generalizes.

## 21. [AlphaEvolve recovered 0.7% of Google's worldwide compute.](acts/2-case-study/05-alphaevolve.tex)

AlphaEvolve combined proposed program edits, automated validity and performance checks, and evolutionary selection to discover a deployed scheduling rule that reportedly recovered 0.7% of Google's worldwide compute on average. The practical value comes from selecting evaluated algorithms; this result measures the discovered rule, rather than the benefit of sandbox forking.

## 22. [Over 120,000 CRISPR guides helped rank about 100 candidate genes.](acts/2-case-study/06-genomics-screen.tex)

A pooled laboratory screen used over 120,000 CRISPR guides, with six guides per target gene and nine treatment-and-repeat arms, to help rank about 100 candidates from 19,050 genes. The roughly 190-fold narrowing counts genes, while agreement among multiple guides supports prioritization for focused validation rather than treating every guide or analysis as independent evidence.

## 23. [Focused tests found promising gene targets and drug combinations.](acts/2-case-study/07-genomics-assay.tex)

Focused laboratory tests in MCF-7 breast-cancer cells found that 10 of 13 genetic targets increased sensitivity to SI-12, while six of eight separately tested drug combinations improved killing. Genetic tests and drug combinations answer different questions, so their outcomes need separate assays and denominators when assessing how well the shortlist translated into results.

## 24. [With Chamo, we connected two apparent branches of one orbit family.](acts/2-case-study/08-three-body-question.tex)

Following repeating three-body orbits as their masses changed connected representative endpoints that appeared separated in a simpler period-versus-angular-momentum plot. This reconciles the two views within the sampled orbit family and illustrates why an apparent split in a projection needs a check in the underlying solution space.

## 25. [All 26 selected connections survived checks in both directions.](acts/2-case-study/09-three-body-verification.tex)

All 26 selected connections, covering five broad gaps, twenty chart jumps and one distant pair, were reproduced in both directions within one sampled solution component. Numerical correction and validation support those connections, while successful checks of selected links leave exploration of the whole solution space open.

## 26. [An orbit can gain or lose stability.](acts/2-case-study/09-three-body-stability.tex)

Changing the masses within one orbit family can turn growing disturbances into small bounded oscillations, or make small disturbances grow, and independent 60-digit calculations reproduced one example of each change. Connectivity and stability answer different questions: connected orbits can respond differently to small disturbances within their orbital plane.

## 27. [Software agents improve code through a feedback loop.](acts/2-case-study/10-installer-task.tex)

In the recorded serial factory repair, an agent proposed changes, the harness ran tests, and review feedback sent the work back for repair before acceptance. This makes software improvement a feedback loop whose next step depends on executed checks, although an approved review alone does not settle every promised behavior.

## 28. [Forking tests different ideas from the same prepared state.](acts/2-case-study/11-workflow-time.tex)

The proposed fan-out creates private trials that inherit the same code and dependencies, then explore different edits without overwriting one another. Reusing their common preparation can save work, but the recorded factory run was serial, so a controlled comparison must establish any parallel benefit after fork, contention, merge and checking costs.

## 29. [Fan-in checks the version we choose or combine.](acts/2-case-study/12-review-cost.tex)

Fan-in collects each proposed change with its test records, then either selects an alternative or combines compatible changes into a final version. A combination can introduce interactions absent from the separate trials, so acceptance needs checks tied to the exact version retained rather than a collection of unrelated passing results.

## 30. [Our proposal connects state reuse with evidence about returned results.](acts/2-case-study/13-dispatch-race.tex)

The proposed interface returns changed files, records of executed checks and shared inputs so a coordinator can judge each trial with its evidence attached. The contribution connects established forking, testing and review tools so the coordinator can assess the exact output and trace which information the trials reused.

## 31. [A useful test checks the behavior that the change promises.](acts/2-case-study/14-adoption-obligation.tex)

Review approved a retry-related repair even though the direct test forcing its new path and checking for one job start was still missing. Many tests with zero failures can leave the changed behavior unresolved, so the acceptance check must deliberately exercise the specific condition and outcome the repair promises.

## 32. [Accepted work must survive the experiment.](acts/2-case-study/15-durable-delivery.tex)

A separate factory run lost an approved patch when delivery was refused and cleanup deleted its temporary workspace. Save the exact result and its test records, confirm that the saved copy is retrievable, and only then clean up; preserving work and authorizing its publication remain separate decisions.

## 33. [AI testing produced 56 crashes and 22 confirmed new vulnerabilities.](acts/2-case-study/16-security-discovery.tex)

CyberGym's latest-code campaign examined 431 projects with 1,748 runnable targets, producing 56 crashes and ultimately confirming 22 distinct previously unknown vulnerabilities after reproduction, deduplication and investigation. A crash is a lead, and these counts describe different objects, so the drop from crashes to bugs is not a simple success rate.

## 34. [A forkable runtime must preserve state, gather evidence and control acceptance.](acts/3-design/00-three-jobs.tex)

The proposed system has three responsibilities: preserve the state a private trial needs, record what it ran and learned, and decide which checked output may continue or be published. Treating execution, evidence and acceptance together prevents cheap trials from being mistaken for useful information or an authorized final result.

## 35. [The next action determines which state a continuation needs.](acts/3-design/01-state-choice.tex)

Source edits need files and build inputs, live computation needs supported memory and runtime state, and reused observations need recorded executions or responses. Choose the cheapest mechanism that faithfully supplies the next action's required state, and verify its declared properties instead of assuming a worktree, checkpoint and replay log preserve the same things.

## 36. [Our paper recorded 256 sandbox creates with a 3.44-second median.](acts/3-design/04-create-trace.tex)

The recorded default-environment creation path completed all 256 requests at a requested concurrency of eight, with a 3.44-second median and a 9.00-second p95. These client API round trips measure creation and exclude teardown, so a comparison needs the same operation, usable state and timing endpoint.

## 37. [Isorun led the October 2 sandbox startup benchmark at a 73 ms median.](acts/3-design/04-current-startup.tex)

ComputeSDK's October 2, 2026 test timed sandbox creation through the first successful command under 100 concurrent requests per provider, with Isorun leading at a 73 ms median. Cheap starts raise the bar for reuse, but this dated benchmark measures a different endpoint and protocol from our earlier creation trace, so dividing their timings would not give a controlled speedup.

## 38. [Reusing state pays off when it avoids more setup than it adds.](acts/3-design/05-resource-rule.tex)

Preparing once avoids the setup repeated by the remaining trials, and reuse pays off when this saving exceeds capture, child startup and private-change costs. The comparison should use the preparation a faithful alternative would actually repeat, with total resource consumption kept distinct from elapsed time.

## 39. [Restoring wins against cold setup but loses against this warm cache.](acts/3-design/06-warm-alternative.tex)

In the eight-run illustration, 34 resource-seconds of reuse overhead saves 176 against cold preparation but spends 20 more than the warm-cache alternative. Reuse therefore needs a comparison with the cheapest way to reconstruct equivalent usable state, and these additive resource costs must not be mistaken for measured elapsed time.

## 40. [Restoring a sandbox does not undo an API call or its bill.](acts/3-design/07-external-effects.tex)

Restoring a checkpoint rewinds local sandbox state, while a completed hosted-model request and its charge remain real events at the remote service. Record external outcomes outside the restored state and reconcile uncertain actions before retrying, using idempotency when supported to avoid repeating an effect unintentionally.

## 41. [Workers propose patches; the controller holds the key to publish them.](acts/3-design/08-controller-authority.tex)

The factory exercised a separation in which workers returned candidate patches and check records, while a controller held the publication credential and checked the approved bytes. Keeping that key outside copied worker state makes publication a separate decision, although identifying approved code does not itself establish that its behavior was adequately tested.

## 42. [Once a worker is replaced, it can no longer publish results.](acts/3-design/10-restore-epochs.tex)

The proposed protocol rejects a replaced worker’s delayed result when its permission version differs from the controller’s current record, such as version one arriving after version two starts. This check controls publication rather than scheduling, and placing it outside restored worker state prevents an old snapshot from reviving revoked permission.

## 43. [Combining branch results should add information while accounting for overlap.](acts/4-analysis/00-evidence-boundary.tex)

Fan-in turns returned branch outputs into a decision by checking chosen or merged artifacts, or by pooling measurements of one quantity with their reliability and overlap accounted for. Private execution alone does not make evidence independent, so the return path must ask what each result adds beyond the information already collected.

## 44. [Choosing a result, merging code and pooling measurements are different operations.](acts/4-analysis/01-result-decisions.tex)

Selecting a model, composing code edits and pooling estimates produce different outputs: one candidate, a newly combined artifact or an estimate of a shared target. Evaluate the selected candidate, test the merged version or justify the pooled uncertainty according to that output, because a numeric score alone does not make candidates suitable for averaging.

## 45. [Code changes that pass in pairs can fail when all three are merged.](acts/4-analysis/02-exact-composition.tex)

In the capacity example, each change starts a one-gigabyte worker, so every pair fits on a two-gigabyte server while the three-change combination does not. Successful individual and pair tests leave larger interactions untested, making the exact merged version the artifact that needs verification before publication.

## 46. [Combining results should keep shared observations once.](acts/4-analysis/03-information-overlap.tex)

If A contains a, b, and c while B contains b, c, and d, their union has four distinct observations, their intersection has two shared ones, and B adds only d. These set operations remove identity duplicates, while statistical dependence between different observations still needs a model of shared errors.

## 47. [The result type determines the fan-in operator.](acts/4-analysis/04-fan-strategies.tex)

Gather items with union, select an eligible candidate with argmax, combine compatible edits with merge, average same-target measurements with normalized weights, and find common items with intersection. Max returns a score rather than its candidate, and ReLU clips negative values rather than combining branches, so each operator needs checks suited to its output’s meaning.

## 48. [Our reducer catches duplicate observation IDs and keeps their source history.](acts/4-analysis/06-reducer-identity.tex)

The implemented reference reducer rejects repeated declared observation IDs, combines distinct numerical summaries under its independent, common-target model, and retains their source history. Different IDs can still share errors, so using that history to calibrate covariance-aware weights remains a proposed extension rather than a property supplied by deduplication alone.

## 49. [For estimates of one quantity, covariance guides the pooling weights.](acts/4-analysis/07-covariance-pooling.tex)

For unbiased estimates of one target with a known positive-definite error covariance, inverse-covariance weights give the smallest-variance linear estimate with weights summing to one. This proposed reducer extension accounts for shared noise through calibrated relationships between errors, while a shared systematic bias still requires its own check.

## 50. [A worker that exaggerates its precision can dominate a weighted average.](acts/4-analysis/08-precision-stress.tex)

In the synthetic stress case, one worker inflated its reported information per point fiftyfold, pulling ordinary pooling to 17.0004 while the demo’s heuristic returned 4.9566 near the true value of five. The example shows why weighting needs trusted precision estimates, while one successful heuristic test supplies no general guarantee against dishonest workers.

## 51. [With shared errors, 100 estimates can reduce noise like about nine independent ones.](acts/4-analysis/09-mean-precision.tex)

For 100 equal-noise estimates with every pair of errors correlated at 0.1, the mean has the variance of 9.17 independent estimates and a signal-to-noise gain of about three rather than ten. This variance-equivalent count describes precision under that model, explaining why repeated estimates with shared errors cannot be counted as 100 independent witnesses.

## 52. [If 50 of 100 tasks reach a checkpoint and 40 finish, overall success is 40%.](acts/4-analysis/12-checkpoint-population.tex)

In the illustrative population, 40 successful completions among 50 checkpoint arrivals gives an 80% continuation rate, while the same 40 completions among 100 starting tasks gives 40% overall success. Reporting both rates separates how useful a reached state is from how often the full process manages to reach it.

## 53. [A check record must say what ran, who ran it and which files it checked.](acts/5-evaluation/01-receipt-semantics.tex)

The factory audit found a green CI job that skipped evaluation, a human-approval label supplied by automation, and a recorded code hash whose helper source was unavailable. A useful receipt must preserve the actual event, actor, checked artifact, and retrievable files, because a success label or fingerprint alone cannot support replay or verification.

## 54. [The code we publish must be the same code that passed the required check.](acts/5-evaluation/02-publication-obligation.tex)

The proposed behavioral gate freezes a candidate, runs its required test on those exact files, and lets the controller publish the same version only after that check passes. If the files change, the previous result no longer covers them, and a code hash binds identity without substituting for the promised behavior’s test.

## 55. [Each use case needs a merge rule and a check matched to its output.](acts/5-evaluation/03-two-tests.tex)

Model designs need selection and evaluation, code edits need tests of the merged version, measurements need overlap and noise accounting, and drug or orbit candidates need assays or numerical checks. The planned restore-versus-warm and sibling-versus-other-family comparisons have not begun, leaving the proposed reuse and dependence claims as questions for controlled experiments.

## 56. [Self-driving compute tries alternatives, combines what they teach us and continues.](acts/6-conclusion/01-final-contract.tex)

The proposed system reuses useful state, runs alternative trials, gathers their contributions, checks the resulting output, and continues under the controller’s acceptance decision. Making trials cheap is only part of the task: the return path must retain shared evidence once, verify the exact artifact, and preserve current publication authority.

## 57. [Cheaper trials help when their results add useful evidence.](acts/6-conclusion/02-numeric-takeaways.tex)

The recap gives three separate examples: reported Tokio compilation fell from 46 to 13 seconds, published candidate coverage rose from 15.9% to 56%, and a correlation model gave 100 estimates the mean precision of 9.17 independent ones. The design goal is to spend less on repeated setup while turning additional trials into useful information the controller can verify and use.
