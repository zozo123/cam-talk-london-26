# Presenter guide: Forkable Sandboxes

**Contracts for state, evidence, and authority.** Cambridge SRG, 15 October 2026.

Generated from canonical source. 45 main slides; no appendix. Planned duration **40:35**; 3800 spoken words. Cues are a plan, not a measured rehearsal. Q&A detail is retained separately from the spoken script.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:45 | 0:00–0:45 | 84 | 112 |
| 2 | The branching mechanism must preserve the state the continuation needs. | 0:45 | 0:45–1:30 | 83 | 111 |
| 3 | Existing runtimes reuse state for cloning, evaluation, and recovery. | 0:45 | 1:30–2:15 | 81 | 108 |
| 4 | A backup request reduced p99.9 latency from 1,800 ms to 74 ms. | 0:45 | 2:15–3:00 | 83 | 111 |
| 5 | 250 attempts raised SWE-bench Lite coverage from 15.9% to 56%. | 0:45 | 3:00–3:45 | 84 | 112 |
| 6 | We built evidence accounting; the integrated forked factory remains proposed. | 0:45 | 3:45–4:30 | 83 | 111 |
| 7 | The factory ran one hosted model through separate stages and checks. | 0:55 | 4:30–5:25 | 84 | 92 |
| 8 | The uv installer failed at two redirect hosts missing from the policy. | 0:55 | 5:25–6:20 | 84 | 92 |
| 9 | The approved plan limited the allowlist update to six files. | 0:55 | 6:20–7:15 | 87 | 95 |
| 10 | Two repairs and two reviews used 59% of recorded stage time. | 0:55 | 7:15–8:10 | 82 | 89 |
| 11 | The repair agent diagnosed different owners for the lease and active cell. | 0:55 | 8:10–9:05 | 87 | 95 |
| 12 | The suite had no failures, but the adoption path lacked a direct test. | 0:55 | 9:05–10:00 | 89 | 97 |
| 13 | The second repair changed code while the requested test remained absent. | 0:55 | 10:00–10:55 | 88 | 96 |
| 14 | Delivery was refused three times, and cleanup lost the patch. | 0:55 | 10:55–11:50 | 87 | 95 |
| 15 | The records included skipped checks, mislabeled approvals, and missing inputs. | 0:55 | 11:50–12:45 | 86 | 94 |
| 16 | The observed gaps define obligations that future branches must preserve. | 0:55 | 12:45–13:40 | 86 | 94 |
| 17 | Worktrees, checkpoints, and replay preserve different kinds of state. | 0:55 | 13:40–14:35 | 83 | 91 |
| 18 | Published latency figures measure different operations. | 0:55 | 14:35–15:30 | 77 | 84 |
| 19 | Restore fidelity needs checks of the state the API claims to preserve. | 0:55 | 15:30–16:25 | 83 | 91 |
| 20 | Each child needs private writable state and host-controlled authority. | 0:55 | 16:25–17:20 | 81 | 88 |
| 21 | Restoring local state does not undo completed external actions. | 0:55 | 17:20–18:15 | 80 | 87 |
| 22 | Forking saves resources when avoided preparation exceeds reuse overhead. | 0:55 | 18:15–19:10 | 82 | 89 |
| 23 | The API traces measured creation and restore--run--capture separately. | 0:55 | 19:10–20:05 | 79 | 86 |
| 24 | The factory has a publication gate, but its fork store is missing. | 0:55 | 20:05–21:00 | 82 | 89 |
| 25 | A replacement restore must invalidate the old worker epoch. | 0:55 | 21:00–21:55 | 88 | 96 |
| 26 | Selection, composition, and pooling require different evidence. | 0:50 | 21:55–22:45 | 81 | 97 |
| 27 | The Chamo project rejected a numerically unresolved cross-check. | 0:50 | 22:45–23:35 | 86 | 103 |
| 28 | Source identities must be recorded before counting separate evidence. | 0:50 | 23:35–24:25 | 84 | 101 |
| 29 | Checkpoint-started success is conditional on reaching that checkpoint. | 0:50 | 24:25–25:15 | 81 | 97 |
| 30 | Repair tests and generalization tests support different claims. | 0:50 | 25:15–26:05 | 82 | 98 |
| 31 | A check can run correctly and still miss the required behavior. | 0:50 | 26:05–26:55 | 76 | 91 |
| 32 | Distinct execution IDs do not make copied evidence new. | 0:50 | 26:55–27:45 | 81 | 97 |
| 33 | At correlation 0.1, 100 measurements have the mean precision of about nine. | 0:50 | 27:45–28:35 | 84 | 101 |
| 34 | Zero pairwise correlation does not fix the all-wrong probability. | 0:50 | 28:35–29:25 | 77 | 92 |
| 35 | Shared conditions can reduce uncertainty in a paired comparison. | 0:50 | 29:25–30:15 | 87 | 104 |
| 36 | Passing every pair does not establish that the full composition passes. | 0:50 | 30:15–31:05 | 79 | 95 |
| 37 | The reducer rejects declared duplicates and retains lineage. | 0:50 | 31:05–31:55 | 81 | 97 |
| 38 | Information pooling outperformed equal averaging on synthetic logistic shards. | 0:50 | 31:55–32:45 | 80 | 96 |
| 39 | Inflated reported precision pushed the synthetic pooled estimate to 17.0004. | 0:50 | 32:45–33:35 | 87 | 104 |
| 40 | The proposed gate withholds publication until the missing test passes. | 1:10 | 33:35–34:45 | 87 | 75 |
| 41 | The proposed cost experiment compares restore with a warm cached template. | 1:10 | 34:45–35:55 | 96 | 82 |
| 42 | The proposed sibling experiment measures environmental co-failure. | 1:10 | 35:55–37:05 | 90 | 77 |
| 43 | Shared families and repeated rounds require dependence-aware analysis. | 1:10 | 37:05–38:15 | 93 | 80 |
| 44 | Testing the disputed path and resampling the repair answer different questions. | 1:10 | 38:15–39:25 | 94 | 81 |
| 45 | The runtime must preserve shared history and verify the result before publication. | 1:10 | 39:25–40:35 | 101 | 87 |

## Script and Q&A detail

### 01. Forkable Sandboxes

*0:45; starts 0:00*

Suppose we reach a running application state and reproduce a failure. We would like several continuations from that point. A fork might preserve the relevant state while giving each continuation private changes. We first need to identify what must survive and which authority must remain unique. Our factory records expose obligations around testing, review, and delivery. They do not yet demonstrate a useful live fork. We will connect those obligations to a runtime contract and a set of experiments. What should a child inherit?

**Q&A detail**

The title figure is a proposed lifecycle. A motivating future workload is a running application at a reproduced failure, with relevant process memory and local state. It has not been exercised in the factory case study. The observed serial repair establishes source files and feedback, not a demonstrated need for live fork. Select a worktree, warm image, disk snapshot, or verified process/VM checkpoint according to the required state. Disclosure and affiliations match the supplied Cambridge deck.

### 02. The branching mechanism must preserve the state the continuation needs.

*0:45; starts 0:45*

We choose the branching mechanism from the next action's state requirements. Source alternatives may need only worktrees. Prepared files can come from a warm image or a disk snapshot. If useful process memory must survive, we need a verified process or VM checkpoint. Our serial factory establishes files and feedback, without showing that live processes must survive. The hosted model remains outside the guest. We should compare mechanisms that supply the same declared state. Existing runtimes already support several versions of this operation.

**Q&A detail**

A fork supplies several continuations from one captured parent with private writable state. Git worktrees preserve source views. Process checkpoints may preserve memory and processes. VM snapshots preserve their declared state surfaces. Filesystem snapshots do not establish memory capture. The hypothetical running-application workload differs from the actual serial repair. Remote model sessions, model randomness, and already performed external effects require separate handling. Neither setup time nor a checkpoint API name establishes whole-prefix reuse or fidelity.

### 03. Existing runtimes reuse state for cloning, evaluation, and recovery.

*0:45; starts 1:30*

SnowFlock exposed VM fork in 2009, on top of Xen. Kimi's AgentENV supports checkpointing, resumption, and sandbox branches for reward evaluation. Its report counts fifty-one million sandboxes across training and evaluation. DeepSeek's DSec retains environments and replays cached command results when a training task resumes. These operations preserve different surfaces and serve different purposes. A sandbox branch does not establish independent judgments. We ask what contract an agent workflow needs around these mechanisms. First consider why an additional execution can help.

**Q&A detail**

SnowFlock: Lagar-Cavilla et al., Rapid Virtual Machine Cloning for Cloud Computing, EuroSys 2009, built on Xen. Kimi K3 reports 51,219,741 sandboxes across 1,505,678 images in training and evaluation, up to 98% of sandbox lifetime during model waits, and checkpoint/resume times as low as 133/49 ms. These are attributed infrastructure figures, not our measurements. Forking is offered for reward judging without side effects. DSec retains sandboxes when training tasks are preempted and replays cached command results on resumption. DeepSeek-V4, arXiv:2606.19348, 5.2.5.

### 04. A backup request reduced p99.9 latency from 1,800 ms to 74 ms.

*0:45; starts 2:15*

Dean and Barroso measured a thousand-key BigTable read. If the request had not completed after ten milliseconds, the client sent a backup to another server and accepted the first response. The 99.9th-percentile latency fell from eighteen hundred milliseconds to seventy-four, with two percent more requests. The backup can escape a delay specific to one server. Shared causes of delay limit that gain. For code generation, an alternative execution may produce a different candidate. We then have to recognize which candidate solves the task.

**Q&A detail**

Dean and Barroso report the 99.9th-percentile latency of a 1,000-key BigTable read, using a hedged request after 10 ms and accepting the first response: 1,800 ms to 74 ms, with 2% more requests. Their assumption is that the cause of variability does not affect multiple replicas at once. This is a published request-hedging result, not a fork benchmark or agent-correctness measurement. The second request can escape server-specific delay without changing the requested operation.

### 05. 250 attempts raised SWE-bench Lite coverage from 15.9% to 56%.

*0:45; starts 3:00*

Brown and colleagues sampled DeepSeek-Coder-V2-Instruct on SWE-bench Lite. One sample solved about sixteen percent of issues. At 250 samples, at least one candidate solved fifty-six percent. That measures coverage of the collection. A production verifier must still recognize the useful candidate. Stroebl and colleagues show that false acceptance costs can make a small sampling budget preferable under their conditions. Our factory also had tests and reviews. Before connecting it to branching, we should separate what we observed, what we built, and what remains proposed.

**Q&A detail**

Brown et al., Large Language Monkeys, arXiv:2407.21787: DeepSeek-Coder-V2-Instruct on SWE-bench Lite improves pass-at-least-once coverage from 15.9% at one sample to 56% at 250, a 40.1 percentage-point increase. This does not report production selection accuracy. Stroebl, Kapoor and Narayanan, The Limits of Inference Scaling Through Resampling, arXiv:2411.17501: when false-positive acceptance carries negative utility, the optimum is often fewer than ten attempts under their modeled conditions. This is not a universal branch-count recommendation. Neither paper measures our sandbox-fork effect.

### 06. We built evidence accounting; the integrated forked factory remains proposed.

*0:45; starts 3:45*

We observed two complete factory work orders and measured several sandbox API paths. We built duplicate-evidence rejection and lineage transport in a numerical reducer. A separate factory gate binds approval to an artifact digest. The integrated fork lifecycle and dependence-aware uncertainty remain proposed. Neither case-study run forked, so those records establish no fork speedup or sibling-dependence effect. They identify obligations that branching must preserve. We will first follow the serial factory, then specify the state, evidence, and authority a future child would need.

**Q&A detail**

SELFHOST-2 and SELFHOST-3 ran through Airflow's Docker Sandbox backend with hosted model access through Databricks. Neither forked; the workgraph recorded serial fallback. The numerical reducer rejects repeated declared evidence IDs and carries lineage. It does not consume lineage to calibrate uncertainty or abstain on unknown dependence. A separate artifact-digest gate was exercised in the factory. Snapshot API measurements are restore/run/capture workflows with unverified memory semantics. The integrated fork store, external evaluator, and restore authority protocol remain proposed.

### 07. The factory ran one hosted model through separate stages and checks.

*0:55; starts 4:30*

We ran a software factory against its own repository. The agent produced specifications, plans, edits, repairs, and reviews. The harness executed the test contract, and the controller checked delivery. Docker Sandboxes supplied the work cell through Airflow's toolset. One model served through Databricks performed every agent role. The harness answered the approval gates. The cell was unmanaged, and execution stayed serial because fork was unavailable. These actors make different claims. The work order began with an installer failure observed on a different sandbox platform.

**Q&A detail**

The factory proposed changes to its own repository. Agent stages generated specifications, plans, edits, repairs, and reviews. The harness ran the tests; the controller enforced artifact delivery. Both work orders used Docker Sandboxes through toolset:SbxCommaPolicyBackend, not islo. The cells were unmanaged, so sandbox authority leases were unused. This differs from dispatch-coordination leases exercised by a concurrency test later. Approvals recorded mode human and actor admin although the harness answered. The workgraph recorded serial_fallback_missing_fork. Sources: docs/factory/SELFHOST-2 stage, approval, and workgraph records in github.com/zozo123/ariflow-swfactory.

### 08. The uv installer failed at two redirect hosts missing from the policy.

*0:55; starts 5:25*

We observed the installer failure on islo. The uv script at astral dot sh redirects to releases dot astral dot sh and can fall back to GitHub release assets. The six-host policy omitted both destinations. The request returned 403 and uv remained unavailable. We then used Docker Sandboxes to execute the work order that corrected the declarations. Allowing a shared release hostname grants more than one installer, so artifact-level access remains a separate design question. First, we recorded the requested change and its scope.

**Q&A detail**

The source work order records curl error 22, HTTP 403, and absent uv after islo use --init minimal ran the setup script. The initial six-host policy omitted releases.astral.sh and release-assets.githubusercontent.com, the uv installer's redirect and release-asset fallback destinations. The factory fix was executed using Docker Sandboxes, not islo. Hostname permissions can allow other assets on the same host; a proxy resolving pinned artifact digests is a proposed refinement and was not built in this run. Sources: docs/factory/SELFHOST-2/intent.md, plan.json, and docs/selfhost.md.

### 09. The approved plan limited the allowlist update to six files.

*0:55; starts 6:20*

We approved six files before editing. Two implement the allowlist, one contains regression tests, one is a deployment script, and two are documentation. Acceptance required both redirect hosts throughout those declarations. The tests checked agreement using repository files rather than network calls, and the full suite also had to pass. Dispatch ownership was outside this plan. That makes scope expansion observable instead of a retrospective judgment. The intended change was small, but its execution encountered a failing test. Here is the time and cost of that workflow.

**Q&A detail**

Declared files: src/swfactory/doctor.py, deploy/islo/bootstrap.sh, tests/test_doctor.py, deploy/islo/deploy.sh, docs/islo.md, docs/selfhost.md. The plan pinned the eight-host tuple, checked gateway command shape, parsed the shell ALLOW_HOSTS array, checked agreement with the Python tuple, and checked prose declarations. Missing or empty parses had to fail loudly. Tests read repository files and imported doctor; no network, subprocess, islo, or curl. The full suite was also required. Dispatch logic in src/swfactory/backend/service.py was not in the approved file list. Sources: docs/factory/SELFHOST-2/plan.json.

### 10. Two repairs and two reviews used 59% of recorded stage time.

*0:55; starts 7:15*

We recorded forty-three minutes and forty-four seconds of elapsed time and ten dollars thirty-three of model cost. The stage records sum to forty-two minutes and thirty-eight seconds. Two repair sessions and two reviews consumed twenty-five minutes, fifty-nine percent of stage time, and seventy-five percent of cost. These durations include tool activity. Initial sandbox setup took twenty seconds. That is not a measurement of the whole reusable prefix. The dominant work here followed a failed test, which sent the repair into dispatch ownership.

**Q&A detail**

Recorded stage sum: 2,557.517 s, rounded to 42:38. Timestamp wall time: 2,624 s, or 43:44, from 11:39:56 to 12:23:40. About 66 s lies outside those stage totals. The first row includes intent, specification, and plan. Timings are agent-session durations including tool activity, not pure inference time. Two repairs plus two reviews sum to about 25.2 min and \7.75. Setup is 20.3 s: a 100-fold speedup saves about 20.1 s, roughly 0.8% of recorded stages. Initial setup is not the whole reusable prefix and does not establish or rule out another reached-state workload's benefit. Sources: metrics.json and agent/stages.jsonl.

### 11. The repair agent diagnosed different owners for the lease and active cell.

*0:55; starts 8:10*

We reached a concurrency test that reported zero runs from four replicas. The first repair diagnosed a split between cell activation and dispatch ownership. With the zero-duration dispatch lease, the final claimant could hold the valid token while another attempt had activated the cell. The activation winner lost its lease; the token holder encountered CellBusy. This is the agent's recorded explanation, not an independently validated diagnosis. The proposed repair allowed adoption of an active cell owned by the same work order. That introduced a specific behavioral obligation.

**Q&A detail**

The repair record explains that replicas can all claim an intent when its dispatch lease has zero duration; only the final claimant keeps a valid token. One attempt can win cell activation, then fail while recording the epoch with DispatchLeaseLost. The token holder encounters CellBusy. The proposed source fix inspects the active cell and adopts it when the owner is another attempt of the same work order. This records the agent's explanation, not an independently reproduced causal diagnosis. The test's dispatch lease is distinct from the sandbox authority lease disabled by the unmanaged cell.

### 12. The suite had no failures, but the adoption path lacked a direct test.

*0:55; starts 9:05*

We received a suite report with nineteen hundred seventy-two cases, including skips, and zero failures. That result did not supply the direct deterministic test requested for the new adoption behavior. Existing tests exercised the helper through a crash path and refused a foreign owner through the busy path. The missing obligation was their specific condition: CellBusy followed by same-owner adoption. We need to force that path and assert one dispatch. The harness ran the suite, but the repair itself had no shell. The next review accepted the remaining gap.

**Q&A detail**

Existing tests exercise adoption through a crash path and refusal of a foreign owner through a busy path. They do not deterministically cover the conjunction CellBusy plus same-work-order adoption. Review 1 requested deterministic tests as a blocker; review 2 approved and rated the missing direct test minor. The suite may encounter the path through a favorable race interleaving, which is not a deterministic branch test. The harness ran the suite after repairs; the repair agents had no shell. Do not say every reported case passed: 1,972 includes skips and zero failures. Sources: agent/review.1.json, fix.5.json, review.2.json and stage records.

### 13. The second repair changed code while the requested test remained absent.

*0:55; starts 10:00*

We can follow the unresolved obligation through three decisions. Review asked for deterministic tests as a blocker. The second repair reported protected tests and refactored an existing recovery path onto the helper. Review then approved and treated the missing direct test as minor. The edit log contains fifteen allowed edits and no blocked test-edit attempt. Scope checking and test protection were separate controls. We propose explicit scope amendments and a check for the required behavior. Approval also leaves a different question: can delivery preserve or recover the candidate?

**Q&A detail**

All 15 logged edits were allowed; six were made by repair agents. The agent reported that tests were protected, but the log does not show a blocked edit attempt and the test hook never fired. Scope checks applied to planned work nodes; repairs followed a non-node path without the same scope check. The out-of-plan backend/service.py change remained major while review could approve. A proposed amendment would explicitly authorize new source scope and require the requested behavioral test. The co-authored OffRisk work is only an annotation/enforcement analogy: Bioinformatics Advances 3:vbad138 (2023), not evidence about this repair policy.

### 14. Delivery was refused three times, and cleanup lost the patch.

*0:55; starts 10:55*

We observed a separate delivery failure after an approved review. The suite reported nineteen hundred eighty-one cases and no failures. Delivery found an unreviewed file, refused three times, and teardown removed the workspace. The file was our harness's review archive. The run took about twenty-six minutes, cost three dollars forty-three, and produced no pull request. Refusing publication and preserving the candidate are separate responsibilities. We propose durable export before cleanup. Preservation also depends on records that accurately state what ran, who approved, and which inputs were used.

**Q&A detail**

SELFHOST-3 recorded about 26 minutes wall time and 853.8 s of stage time, \3.43, 1,981 reported cases with no failures, and approved review. Delivery refused three times because files lay outside the reviewed commit stream. The unexpected file was a review-diff archive mirrored into the workspace. Teardown removed the patch, and no pull request resulted. The supplied deck does not specify the original requested change; this is a delivery/recovery incident, not a full second task reconstruction. Export before cleanup is proposed, not merged. Preserve or snapshot state during long human waits without granting publication authority. Related recovery mechanisms: Planarian, Crab, DSec.

### 15. The records included skipped checks, mislabeled approvals, and missing inputs.

*0:55; starts 11:50*

We found records that overstated or incompletely identified their events. A CI job succeeded with its real evaluation skipped. An approval named a human although the harness answered. The adapter digest identified a local shim whose source was not recoverable from the repository. A trusted recorder still needs accurate event semantics and retrievable inputs. We distinguish an audit from replay against recorded responses and from a fresh run with new model calls. Those records now give us specific obligations for the runtime around any future branch.

**Q&A detail**

The evals-islo Actions job passed in about three seconds while its real evaluation step was skipped because a key was absent. Approvals recorded mode human and actor admin although the harness answered. A local adapter shim outside Git had a recorded digest but no recoverable source in the repository. Another setup attempt failed while parsing stdout contaminated by status text. Typed states are executed, skipped, and failed; actors are human, harness, and service. Authenticity alone does not establish semantic accuracy. Audit inspects records; replay requires retrievable adapter bytes and recorded external responses; fresh hosted-model calls create a fresh run. Related: PASS, CamFlow, in-toto, rr, DSec, and ENCODE pipelines.

### 16. The observed gaps define obligations that future branches must preserve.

*0:55; starts 12:45*

We can now connect each observation to a required mechanism. A new behavior needs a concrete test obligation. Records need the actual execution status and actor. Candidates need durable export on every exit. For future branches, we also need an identified parent, private changes, and fresh authority. We could freeze the pre-repair files and feedback for alternatives, but this case does not show that live process memory must survive. The branching lifecycle remains proposed. We next compare the mechanisms that preserve each kind of required state.

**Q&A detail**

Before the first repair, we could identify the input tree, dependencies, and failed-test receipt for proposed alternative continuations. No actual fork occurred. The case does not establish that useful process memory must survive, so worktrees or warm environments remain alternatives. The hypothetical live-application failure is a future workload, not factory evidence. New scope needs authorization and a behavioral obligation; missing coverage needs a targeted artifact-bound test; inaccurate receipts need typed event semantics; recovery needs export before teardown; replay needs retrievable inputs. For proposed branching, declare the captured surface, sharing policy, external observations, child identity, and authority. The numerical reducer does not detect the missing test by itself.

### 17. Worktrees, checkpoints, and replay preserve different kinds of state.

*0:55; starts 13:40*

The first design choice is the state surface. Worktrees preserve files. Process checkpoints preserve supported process state. Virtual machine snapshots preserve their declared memory and device state. Replay preserves recorded observations. Each gives a continuation something different. If we edit loaded application code, we may need a reload or restart, which can destroy the state we hoped to reuse. We should first identify what the continuation consumes, then choose a mechanism and a faithful baseline. That distinction also explains the published latency figures.

**Q&A detail**

Worktrees parallelize edits without preserving live processes. gVisor supplies a userspace-kernel sandbox with its own supported save/restore semantics. Replay can reuse a response without reexecuting a remote service. Network, time, randomness and remote model sessions need declared semantics. The factory case establishes files, dependencies and failed-test feedback, not a necessary live process. An unchanged simulator or application at a reproduced failure is a possible useful live-state workload, not an observed property of the allowlist repair.

### 18. Published latency figures measure different operations.

*0:55; starts 14:35*

These published numbers locate mechanisms. DeltaBox reports checkpoint time; Kimi reports minimum checkpoint and resume times; Shepherd reports fork time. SnowFlock forks across hosts, while Firecracker measures boot to application code. They have different endpoints, workloads and accounting conventions. We therefore cannot rank them using this table. For our runtime, the useful comparison must reach equivalent usable state and include the costs the workflow pays. Before timing a live fork, we must observe the state that survives.

**Q&A detail**

All values retain their source endpoints. The mechanism lineage includes Xen, live migration, Potemkin, SnowFlock, Catalyzer, Nephele and MITOSIS; agent checkpointing includes DeltaBox and Shepherd; Crab and Planarian address recovery. Recovery is not interchangeable with branching. Kimi reports checkpoint/resume minima, not typical latency. Workload and timing conventions differ; this table cannot rank platforms. The survey is bounded to the systems examined.

### 19. Restore fidelity needs checks of the state the API claims to preserve.

*0:55; starts 15:30*

A process keeps a random nonce only in RAM. We capture, restore three children, and ask whether the process is alive with the same nonce. That is a necessary probe of the memory path, not full fidelity certification. We then compare the declared deterministic behavior between direct and restored execution. Private writes, clocks, identities, randomness and sockets need checks appropriate to the workload. The probe is preregistered and unrun. Our current measurements therefore establish restore fan-out; they do not establish a memory fork.

**Q&A detail**

The RAM nonce is a necessary probe, not a complete fidelity proof. Check private writes, process identity, clocks, random state and sockets as relevant. A snapshot name does not establish memory semantics. Hosted-model weights, KV state and sampling are outside the guest. A failed nonce probe requires reporting the actual filesystem/restore semantics. A successful probe still requires useful captured state and declared semantic tests.

### 20. Each child needs private writable state and host-controlled authority.

*0:55; starts 16:25*

A child needs private writable state, while an immutable cache can be shared within a declared trust domain. It also needs authority assigned outside the copied guest state. A guest generation string and a bearer token can both be cloned. The host must authenticate and authorize the child, with an epoch, expiry and budget. The publishing credential stays with the controller, bound to a specific artifact decision. Kernel isolation is valuable, but it addresses a different boundary from permission to act.

**Q&A detail**

A microVM can contain a still-valid bearer token. Guest-supplied generation strings are copied and cannot authenticate a clone. The host must authenticate and authorize each child separately. VMGenID can reseed the kernel; userspace RNG treatment is application-dependent. Refresh network identity, clock and socket semantics. Immutable caches still need a trust and leakage policy. Egress policy is distinct from withholding publication credentials. Controller-held publication is exercised; fresh clone authority remains proposed.

### 21. Restoring local state does not undo completed external actions.

*0:55; starts 17:20*

Restoration brings back local state. It cannot unsend a model request, recover its cost, or reverse a remote tool action that already happened. Some outputs can be staged until verification; other effects need a journal, idempotency or reconciliation when the outcome is uncertain. Earlier recovery systems show ways to delay output, but a general effect buffer is still proposed here. We also export the patch and evidence before every teardown. This gives the runtime obligations beyond merely creating a child.

**Q&A detail**

Speculator, external synchrony and Remus supply precedents for delaying output. DSec can replay cached command results on resumption. A general effect buffer is proposed here. An uncertain remote action cannot be blindly retried. Export on refusal is motivated by SELFHOST-3. The factory exercised one controller-mediated publication path; it did not intercept every external effect.

### 22. Forking saves resources when avoided preparation exceeds reuse overhead.

*0:55; starts 18:15*

The resource condition compares preparation avoided with reuse overhead. Eight children and thirty resource-seconds of preparation avoid two hundred ten, while capture, restore and divergence add thirty-four. With a warm cache, preparation can fall to two and the same reuse path loses twenty. These are illustrative calculations. Ordinary continuation work cancels; elapsed time depends on the critical path and contention. In our file-edit case, worktrees could also provide parallelism. The twenty-second setup measurement is not a measurement of the full reusable prefix.

**Q&A detail**

This is an additive resource-cost model, not measured elapsed time. Ordinary continuation work common to both alternatives cancels; D is incremental divergence overhead, including copy-on-write. P must be the reusable preparation, not merely sandbox setup. In SELFHOST-2 the three edit tasks sum to 342.579 seconds, versus ideal unchanged-duration critical path 176.689 seconds: a 165.890-second saving, about 6.5 percent of stage time, before fork/merge/verification. Worktrees may support that schedule. Jitsu and LightVM illustrate cheap fresh-start alternatives.

### 23. The API traces measured creation and restore--run--capture separately.

*0:55; starts 19:10*

The traces show what actually executed. Daytona and Tensorlake created sandboxes, at requested concurrency eight. The islo path restored a named snapshot, ran a command and captured at concurrency twelve. It completed two hundred fifty-five of two hundred fifty-six operations, with median six point eight seven seconds. Per-operation teardown is outside the reported percentiles, and memory capture remains unverified. Different operations explain why this is not a ranking. The controlled experiment must isolate whether reuse beats a warm alternative.

**Q&A detail**

Daytona and Tensorlake requested concurrency eight. islo used a named 141 MB snapshot at concurrency twelve. Teardown is excluded from per-operation percentiles. The islo result is a client API round trip including restore, command execution and capture; memory preservation is unverified. These are exercised paths, not isolated mechanism latencies or a provider ranking.

### 24. The factory has a publication gate, but its fork store is missing.

*0:55; starts 20:05*

Here is the complete lifecycle, with the evidence boundary highlighted. Our scheduler, journal, work cell and artifact-digest gate have been exercised on the serial path. The numerical reducer was built separately. A lease broker exists but was unused in these work orders. The fork store is missing and the external evaluator is proposed. The contract joins these pieces; it does not claim that the integrated system already runs. Each returned candidate needs selection or composition, exact-artifact verification and current authority before publication.

**Q&A detail**

Calls checkpoint, fork, evaluate, select, reduce and promote express different decisions. Named snapshots are exercised, numerical deduplication is built and the digest gate is exercised; integrated fork, external evaluator, calibrated dependence and epoch-fenced publication are proposed. Eight obligations: identified immutable parent; fresh child authority; no guest publishing token; input/evidence/feedback records; duplicate rejection plus retained shared factors; deterministic composition and conflict retention; exact-composition verification; durable export on every exit. Selection/composition of patches is separate from common-target numerical reduction.

### 25. A replacement restore must invalidate the old worker epoch.

*0:55; starts 21:00*

Suppose a logical worker is replaced after a failure. The controller advances its epoch. A delayed publication from the old instance must be rejected, even if its local state still looks valid. Evidence and approval must also identify the frozen artifact being published. A concurrent fork is different: it gets a new worker identity, and the parent may continue. We have a TLA plus design, not a recorded model-checker result. Now that we have defined the execution and authority boundaries, we can interpret what comes back from branches.

**Q&A detail**

The controller checks authenticated identity, current epoch, artifact, scope and budget. Replacement and concurrent fork are distinct: replacing logical worker w invalidates its old epoch; a new child identity need not revoke a continuing parent. Intended model covers clone, lease expiry, delayed approvals and uncertain effects. No TLC run or implementation trace check is recorded. State restoration and authority renewal are coupled protocol events.

### 26. Selection, composition, and pooling require different evidence.

*0:50; starts 21:55*

There are three different uses of branching. We may choose among different patches, compose compatible patches, or pool measurements of one target quantity. The evidence required by each decision differs. A numerical score for a patch is not automatically an information estimate, and the reducer does not select patches. Our implemented reducer occupies the measurement lane under stated assumptions. The work with Ori Chamo offers a scientific example of the distinction between a proposed candidate, a screen and an admissible claim.

**Q&A detail**

Candidate selection needs a separately evaluated selector and cost/error model. Common-parameter pooling cannot combine different artifacts simply because each returns a number. Composition can create higher-order interactions. Fresh evaluation for generalization is different from a deterministic regression check, which can still establish its asserted behavior.

### 27. The Chamo project rejected a numerically unresolved cross-check.

*0:50; starts 22:45*

With Ori Chamo, we studied an atlas built from one hundred thirty-five thousand source orbits. The preliminary manuscript reports twenty-six selected difficult links crossed by bidirectional continuation, connecting apparent projected branches within a sampled component. Candidates pass through numerical screens, high-precision checks and independent reproduction before a claim is frozen. One independent RK4 cross-check was numerically unresolved, so we rejected it as evidence. The project retains open completeness obligations. The lesson for our runtime is concrete: a plausible candidate and an admissible claim occupy different states.

**Q&A detail**

Ori Chamo is the coauthor affiliated with Incredibuild. The source catalog is Li, Li and Liao unequal-mass planar periodic orbits. Extra-Trees/active learning proposes computations; deterministic shooting/Floquet screening is not final verification. The twenty-six selected connections comprise five bottleneck, twenty chart-discontinuity and one near-projected long-range connection. They are bidirectionally continued in the preliminary manuscript. Independent mpmath RK4 64/128-step self-test was numerically unresolved; its output was rejected as evidence, without invalidating every other result. Representative high-precision checks and a bounded sampled-component claim are distinct from global completeness. The project illustrates evidence admission, not sandbox-fork performance or agent dependence.

### 28. Source identities must be recorded before counting separate evidence.

*0:50; starts 23:35*

Across our coauthored studies, the visible identifier was sometimes finer than the source of the observation. Tumor cells shared patients. Mining addresses could be linked to the same agent. In a runtime, executions can share a test case or return the same observation. The recurring step is to identify the unit and record its relationships before counting it. These domain examples do not estimate fork correlation. They motivate the manifest, while the next question concerns the population from which a checkpoint observation is drawn.

**Q&A detail**

The coauthored Bitcoin study linked most early mining to sixty-four agents; malignant-cell clustering depended on patient identity. These required domain-specific inference, not a generic lineage algorithm. They do not measure fork outcomes. Proposed runtime manifest: candidate digest, parent snapshot, input tree, execution ID, observation IDs, prompt/model version, seed policy, case/fixture IDs and feedback IDs. Built lineage transport does not estimate effects or hidden shared blind spots. Additional perception/physical-network and ENCODE examples remain methodological context in REFERENCES.md.

### 29. Checkpoint-started success is conditional on reaching that checkpoint.

*0:50; starts 24:25*

If a workflow reaches a checkpoint half the time and then succeeds with probability point eight, the corresponding end-to-end success probability is point four. Starting directly from the checkpoint observes point eight. That is a conditional question. It does not estimate how often we reach that state or establish every earlier choice. Go-Explore makes returning to reached states explicit. For our evaluation, we need to name both the checkpoint population and the task-start population, and retain which feedback shaped the candidate.

**Q&A detail**

Illustrative probabilities, not measured. A viable reached state contains information about the prefix; continuation success alone does not estimate how often it is reached or validate every earlier decision. Go-Explore explicitly separates return-to-state and exploration. A success rate at a selected checkpoint differs from a task-start success rate.

### 30. Repair tests and generalization tests support different claims.

*0:50; starts 25:15*

The repair sequence exposes failed tests and review feedback to the candidate. That is useful development. A regression check can still establish the deterministic behavior it actually asserts on that artifact. Claims about generalization or selection performance require a suitable evaluation beyond the development feedback. Adaptive-analysis work explains why reuse changes the interpretation. In our case, one hosted model performed the roles, but we did not estimate their dependence. The next slide separates three questions that a single green receipt cannot answer.

**Q&A detail**

One hosted model performed all agent roles, without an agent-dependence estimate. Public diagnostics versus hidden held-out verifiers address different purposes. METR RE-Bench 30.4 percent versus HCAST .7 percent was not a controlled scorer-visibility comparison; scorer visibility was a leading hypothesis. ImpossibleBench shows read-only tests do not prevent special-casing. None establishes fork-induced judgment dependence. A regression test used during repair remains valid evidence of the behavior actually asserted on its exact artifact.

### 31. A check can run correctly and still miss the required behavior.

*0:50; starts 26:05*

Apply three questions to the same-owner adoption candidate. First, did a check execute on this exact artifact? Second, did it deliberately exercise the new path and assert one dispatch? Third, what broader claim does the collection of outcomes support? Artifact binding addresses the first; a targeted test the second; a suitable sampling design the third. The observed gap belongs to coverage. Rejecting duplicate evidence is useful, but it cannot discover an assertion that was never written.

**Q&A detail**

The adoption-path gap is behavioral coverage, not proof of a bad patch or correlation. Identity checks and external recording address integrity; they do not establish semantic adequacy or calibration. Authentication of a recorder and trust in the behavior asserted are separate. Passing the targeted test does not prove generalization, and a confidence interval does not replace the targeted test.

### 32. Distinct execution IDs do not make copied evidence new.

*0:50; starts 26:55*

We distinguish copied evidence from related new observations. If two workers return observation e one, the built reducer rejects the declared duplicate. If they return different observations from one parent, it retains the relationship but does not correct dependence. Four runs of one hundred cases produce four hundred outcomes grouped under one hundred case identities. Fresh randomness can produce a new outcome; it does not create a new case. This is why execution, observation, case and candidate identifiers need separate roles.

**Q&A detail**

A copied receipt remains the same observation. A genuinely fresh stochastic outcome can obtain a new observation ID but retains the case, candidate and ancestry cluster. Deterministic reruns supply execution checks, not new test cases. Four runs of one hundred cases do not establish four hundred independent cases. Distinct worker declarations do not authenticate underlying evidence.

### 33. At correlation 0.1, 100 measurements have the mean precision of about nine.

*0:50; starts 27:45*

For a mean, we can show exactly how an assumed dependence affects precision. With equal marginal variances and common correlation point one, one hundred measurements have the variance-equivalent precision of about nine independent measurements. The variance stops shrinking toward zero because of the shared component. This is a calculation under stated assumptions. It is not a probability that the answer is correct, and shared bias remains. Published judge panels provide context, not a measurement of fork effects. Candidate search requires a different joint quantity.

**Q&A detail**

For N=9, effective counts are 9 at rho=0, 5 at rho=.1, 1.8 at rho=.5. Kohli 2026 preprint estimates nine frontier judges from seven families at Kish effective count 2.18, CI 2.07--2.31; 9.1 percent of 319 unanimous MNLI decisions were wrong. Kim ICML 2025 reports conditional agreement on wrong answers, 60 percent versus 33 percent by chance, not rho. Neither measures forks. Independent slow-request illustration: 1-.99^100 is about .634. A hypothetical .1 failure rate gives .9^29 about .047 probability of twenty-nine greens. Amdahl has analogous algebra, not the same causal quantity. Poolkeh models a different pooling operation, 295,951 tests for about nine million people; it was not a laboratory pooling experiment.

### 34. Zero pairwise correlation does not fix the all-wrong probability.

*0:50; starts 28:35*

Here are three exact joint distributions. Each candidate is wrong half the time and every pair has zero correlation. Yet the probability that all three are wrong is zero, one eighth or one quarter. A selector cannot return a correct member when all members are wrong, and must still recognize one when it exists. The effective-size formula for a mean therefore cannot answer the search-coverage question. We need the joint failure behavior, not only a pairwise statistic.

**Q&A detail**

One denotes an error. All three distributions have error probability one half for each candidate and zero pairwise correlation. Their all-wrong probabilities differ. A selector returning one member succeeds at most one minus the all-wrong rate and must recognize a correct member. The variance-equivalent effective count for a mean cannot substitute for this joint distribution. The enumeration is exact; the Chen preprint is cited only for the selector ceiling.

### 35. Shared conditions can reduce uncertainty in a paired comparison.

*0:50; starts 29:25*

Sharing can be useful when our quantity is a difference. Compare A and B under matched conditions: positive shared variation can reduce the variance of A minus B. That is the reason for paired comparisons and common random numbers. The relevant randomness must actually be controlled; cloning a guest seed does not control a hosted model. An ancestry tree is also incomplete, because fixtures, tests, retrieval and feedback can link executions. The runtime should retain these relationships and let the evaluation question determine how to use them.

**Q&A detail**

An execution tree misses retrieval, evaluator, prompt, fixture and feedback relationships. Correlation is not uniformly harmful: positive covariance can help matched differences, while it raises mean variance. Common random numbers require control of the actual randomness consumed. A cloned guest PRNG does not control remote model sampling. Compare equivalent cases and record assignment and exclusion rules.

### 36. Passing every pair does not establish that the full composition passes.

*0:50; starts 30:15*

Three patches each enable one worker. Every single patch and every pair fits within capacity two. The full composition does not. With eight candidates there are twenty-eight pairs but two hundred fifty-six subsets, so pair checks can miss higher-order interactions. Publication concerns the actual artifact we selected, not an assortment of individually green parts. We must rebuild and test that composition and bind the receipt to its digest. Statistical reduction of measurement summaries does not solve this artifact problem.

**Q&A detail**

For fixed objective U, Gamma_ij=U(i,j)-U(i)-U(j)+U(empty). With U=1 for pass, the example gives zero pair interactions and a failing triple. Numerical reduction does not solve patch composition. The biological context is synthetic lethality: Gilad et al. screened knockouts lethal with an SRC-3 inhibitor; this is an analogy, not runtime data. Deterministic composition must preserve conflicts and resulting bytes before verification.

### 37. The reducer rejects declared duplicates and retains lineage.

*0:50; starts 31:05*

This is the implemented boundary. A result records its estimate, reported information, sample count, evidence identifiers and lineage. The reference reducer combines numerical summaries and rejects an exact repeated declared evidence identifier. Different identifiers with a shared parent can merge; the lineage travels with the result, but it does not adjust covariance. Calibration, independence and a common target remain assumptions of the caller. This is useful enforceable behavior with a precise scope. The next slide shows numerical checks of that scope.

**Q&A detail**

The Gaussian/Wald reference reducer adds natural-parameter summaries associatively under an independence/common-target model and retains a disagreement statistic. Declared exact duplicate evidence IDs are rejected by default. Lineage is transported but not consumed for covariance. Worker declarations are not authenticated manifests. Conservative refusal when dependence is unknown, trusted evidence identity and controller-derived information remain proposed. Cochran 1954 supplies inverse-variance-estimation context.

### 38. Information pooling outperformed equal averaging on synthetic logistic shards.

*0:50; starts 31:55*

On five synthetic logistic shards, information pooling was closer to the centralized maximum-likelihood estimate than equal averaging. The mean gaps were point zero zero eight three and point one seven seven over eight fixed seeds; the whiskers are standard deviations. Sample-size weighting was not compared. A separate four-worker islo trace exercised snapshot-to-reducer integration with a small numerical gap. These checks establish execution of the record and algebra under their assumptions. They do not demonstrate improved agent accuracy or dependence correction.

**Q&A detail**

Five shard sizes are 60,120,400,2000,5000. Mean norm gap to centralized MLE over eight fixed seeds is .0083 plus/minus .0042 for information pooling and .177 plus/minus .090 for equal averaging. These are SD, not confidence intervals. Sample-size weighting was not compared. Separate four-worker islo integration trace from a 141 MB snapshot pooled synthetic mean4.9422 versus full-sample4.9450, gap .0028, in6.70s client restore--run--capture. This tests aggregation and an exercised integration path, not agent accuracy or dependence correction.

### 39. Inflated reported precision pushed the synthetic pooled estimate to 17.0004.

*0:50; starts 32:45*

A worker can report a real sample count and still inflate the strength of its evidence. In this synthetic stress case, a two-thousand-point shard returns a distant estimate and fiftyfold reported precision. Unprotected pooling moves to seventeen. A heuristic returns about four point nine six, without a Byzantine guarantee. Sample count alone does not detect the attack. Information needs trusted recomputation under the numerical model, while agent scores need their own validated error model. We now have enough structure to state the experiments and the acceptance policy.

**Q&A detail**

The 2000-point shard returns a distant estimate and reports fiftyfold information per point. Unprotected pooling yields17.0004, stress heuristic4.9566. Sample count alone cannot detect this claim. The heuristic illustrates one stress case, not a Byzantine guarantee. Trusted recomputation under the numerical model can validate information; agent scores need a separately validated error model. These extensions are proposed. An external recorder alone does not establish statistical calibration.

### 40. The proposed gate withholds publication until the missing test passes.

*1:10; starts 33:35*

We can turn the case into a precise acceptance policy. The candidate added a same-owner adoption path. Before publication, we freeze that candidate, deliberately force the path, and assert that one dispatch occurs. The receipt must name the artifact we actually tested. If we combine candidates, we test that exact combination again. The controller then checks current authority and approval for that digest. A refusal retains the patch and its receipts. This resolves a concrete missing obligation; it does not yet establish how well an ensemble generalizes.

**Q&A detail**

Scope authorization, an executed receipt, behavioral coverage, exact-composition verification, artifact-bound approval and current controller authority are separate obligations. A valid digest proves identity, not correctness. A passing regression path supports that behavior; it does not establish held-out accuracy or ensemble confidence. The gate is proposed; the built digest gate and numerical reducer do not supply all these checks. Durable export prevents the second incident's teardown loss.

### 41. The proposed cost experiment compares restore with a warm cached template.

*1:10; starts 34:45*

The first experiment asks which execution mechanism we should choose. We compare restore after setup and a warm test with a cached template that already has dependencies. For three, six and twelve children, we interleave twenty batches per arm and measure the time until the last child produces its first test result. There are no model calls. We establish capture semantics first and expose failures and capture cost. A win informs the backend choice for this workload. To claim a benefit from live memory, we also need useful running state and an equivalent warm reconstruction baseline.

**Q&A detail**

Current protocol: gain is median cached makespan minus median restore makespan, with 10,000 within-arm bootstrap resamples. Supports H1 if the 95% lower confidence bound exceeds 10 seconds at every N; rejects if the Bonferroni 98.3% upper bound is below 10 seconds at any N. Gate 0 restores a RAM-only nonce in three children; this is a necessary probe, not full fidelity certification. Current protocol excludes failed restores from timing but counts them as failures; any amended failure or capture-amortization rule must be dated before collection. Resource cost and batch latency are different endpoints. A timing gain does not prove that process memory was needed: children must consume useful captured running state and the warm alternative must reconstruct equivalent usable state.

### 42. The proposed sibling experiment measures environmental co-failure.

*1:10; starts 35:55*

The second experiment asks whether captured ancestry changes environmental failure patterns. Twelve independently prepared families each supply three siblings. We compare them with three restores from other families, matched by host and start slot, over at least three hundred race-test rounds. We record failure classes as well as binary outcomes. Before collecting data, we must identify a varying parent-state feature that is preserved and actually consumed. If the test rebuilds the relevant state, it removes the treatment. This is an environmental experiment; the hosted model remains outside the guest snapshot.

**Q&A detail**

Both arms restore; strangers can still share host, scheduling, fixtures or other causes. The planned race test is tests/test_dispatch_strand.py::test_two_replicas_pumping_the_same_outbox_dispatch_once. Its fresh backend construction may discard relevant restored state, so the causal treatment must be verified before collection. Guest RNG state does not control the hosted model's RNG. The overlapping family assignments and repeated rounds invalidate an automatic independent-pair analysis. This experiment does not establish judge correlation, reducer calibration, accepted-patch quality or a general effect of forked agents.

### 43. Shared families and repeated rounds require dependence-aware analysis.

*1:10; starts 37:05*

The comparison design determines the analysis. In the recorded protocol, families recur in several comparisons and the same cells run many rounds. We cannot treat twelve differences as independent by default. Before collection, we need independent blocks or a model that handles these links and time dependence. The example shows why baseline dependence also matters: nine measurements at correlation point one carry five independent measurements' variance-equivalent precision. Raising correlation to point fifteen gives about four point one. These are illustrative calculations, not outcomes. We retain the original preregistration and identify the amendment explicitly.

**Q&A detail**

The current protocol reuses families i+1, i+2 and i+3 modulo twelve. Its independent sign-flip rule and twelve-pair t interval require exchangeability or independent experimental units that are not supplied automatically by that design. A proposed amendment should independently assign family blocks, or specify and justify an analysis of overlap and temporal dependence. The effective count N/[1+(N-1)rho] is variance-equivalent under equal variances and common pairwise correlation. The value 6.4 for nine measurements and rho=.05 assumes zero baseline correlation; it does not follow from an excess .05 over a .10 baseline. Amendments must be public and dated before collection; no outcome is reported here.

### 44. Testing the disputed path and resampling the repair answer different questions.

*1:10; starts 38:15*

We finish the experiments by returning to the disputed repair. The earliest useful check is a deterministic test that forces same-owner CellBusy adoption and asserts one dispatch on the frozen artifact. It may pass or fail; either outcome resolves the missing coverage. Separately, we can resample the repair nine times and describe scope edits, distinct diffs and test claims. That measures repeatability under the stated model setup. The exact original input tree is unavailable, so the public substitute needs qualification. These procedures answer different questions, and neither alone establishes a benefit from guest forking.

**Q&A detail**

The recorded Phase C prediction is at least five of nine repeats of the out-of-plan service.py edit. Original in-cell input b77afa9 is not recoverable; the public substitute c07bc4a is justified by delivered commit order, not a verified tree-hash comparison. This limits replication. Holding the hosted endpoint and prompt fixed does not move its weights, KV state or sampler into a guest snapshot. Resampling cannot establish a causal effect of guest fork on model outputs. Scope authorization and coverage remain separate checks even if all nine repairs differ. Accepted-result gains require a defined workload population, selection policy and equal-cost comparison.

### 45. The runtime must preserve shared history and verify the result before publication.

*1:10; starts 39:25*

Return to the running failure in the opening. We want to reuse state that actually helps a continuation, preserve what each result used, and verify the artifact before publication. We have recorded factory incidents, exercised execution paths, and built duplicate and artifact-identity checks. The integrated forked workflow remains proposed. Two research problems remain: using shared-history metadata to justify uncertainty or refusal, and renewing authority safely after restore. The next decisive result is useful reached state that survives capture and beats an equivalent warm reconstruction. Fork supplies an execution option; the contract determines what the continuation established and what it may publish.

**Q&A detail**

Two research questions: can an ancestry/fixtures/feedback manifest support a calibrated dependence model or a justified refusal of a precision claim? Can restore renew authority and reject stale publication across failure and uncertain external effects? The decisive live-state systems result needs useful reached state that survives capture, remains valid in private continuations, and is cheaper to restore than to reconstruct with a warm alternative. Code edits may require reload or restart. The built reducer handles common-target numerical measurements under declared assumptions; it does not choose or validate patches. Completed incidents do not measure fork-induced correlation. Keep the evidence ledger, exported bytes, exact-artifact verification and current authority distinct.
