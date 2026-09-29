# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from `talk.tex` by `tools/presenter_guide.py`. 28 main slides, 13 backups. Planned talk: **37:45**, 3770 spoken words, 100 wpm average, peak 108 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:45 | 0:00-0:45 | 80 | 107 |
| 2 | Blocker. One more repair. Approve. | 1:50 | 0:45-2:35 | 189 | 103 |
| 3 | One factory, seven places the runtime bit | 1:10 | 2:35-3:45 | 123 | 105 |
| 4 | A factory needs a wall, a fork and a count | 1:30 | 3:45-5:15 | 154 | 103 |
| 5 | Allowlists name hosts; the web redirects | 1:15 | 5:15-6:30 | 133 | 106 |
| 6 | Filesystem state: what a snapshot shares | 1:25 | 6:30-7:55 | 133 | 94 |
| 7 | Locking the tests was not enough | 1:40 | 7:55-9:35 | 178 | 107 |
| 8 | The agent never pushes; its token still copies | 1:35 | 9:35-11:10 | 169 | 107 |
| 9 | Teardown must not destroy the experiment | 1:15 | 11:10-12:25 | 128 | 102 |
| 10 | A green check is not proof the check ran | 1:15 | 12:25-13:40 | 135 | 108 |
| 11 | What the run pins, and what it cannot | 1:10 | 13:40-14:50 | 126 | 108 |
| 12 | Parallel-safe steps, and nothing to fork them | 1:05 | 14:50-15:55 | 103 | 95 |
| 13 | Fork is old, and much of it ran on Xen | 1:40 | 15:55-17:35 | 154 | 92 |
| 14 | Fork copies memory, secrets and identity | 1:35 | 17:35-19:10 | 146 | 92 |
| 15 | Hold effects until an authority releases them | 1:05 | 19:10-20:15 | 115 | 106 |
| 16 | When fork pays, and where it loses | 1:55 | 20:15-22:10 | 188 | 98 |
| 17 | Two axes: what a child can reach, and name | 1:05 | 22:10-23:15 | 117 | 108 |
| 18 | Machines fork; authority stays outside | 1:45 | 23:15-25:00 | 182 | 104 |
| 19 | The second review was not a second witness | 1:05 | 25:00-26:05 | 116 | 107 |
| 20 | Execution multiplicity is not evidence multiplicity | 1:25 | 26:05-27:30 | 123 | 87 |
| 21 | The runtime holds some of the cluster labels | 1:30 | 27:30-29:00 | 149 | 99 |
| 22 | Fork is also how you run the control | 0:55 | 29:00-29:55 | 77 | 84 |
| 23 | Every worker returns a receipt, not a score | 1:45 | 29:55-31:40 | 165 | 94 |
| 24 | Isolation does not authenticate precision | 1:10 | 31:40-32:50 | 114 | 98 |
| 25 | The test that could prove me wrong | 2:00 | 32:50-34:50 | 182 | 91 |
| 26 | The same work order, run as it should be | 1:05 | 34:50-35:55 | 112 | 103 |
| 27 | Open problems where this room is ahead of me | 1:20 | 35:55-37:15 | 138 | 104 |
| 28 | Fork the machine, not the trust. | 0:30 | 37:15-37:45 | 41 | 82 |

## Script

### 01. Forkable Sandboxes

*0:45, starts at 0:00*

Thank you for having me. I work on distributed builds at Incredibuild, I teach at HIT, and I build an agent sandbox platform called islo. I'll disclose that once and then only talk about components. In build systems I learned that recomputing the world is insane. So the state I wanted to reuse for speed became the state I had to isolate for trust. This talk is about that runtime layer, and about one run that shows why it matters.

### 02. Blocker. One more repair. Approve.

*1:50, starts at 0:45*

Let me start with a real run. On the 27th of September my software factory worked on its own code. The work order was small: fix the sandbox's network allowlist. Along the way a four-thread race test failed, and the loop sent a repair agent. That agent had no shell, and it said so: it could not run the tests. It read the code, decided the bug was in the race logic, and rewrote it, in a file no plan listed. Review one said: blocker, untested and unverified. So the loop tried again. The tests were locked, so it could not add one. It restructured the code, said plainly it had not run the suite, and argued the change was already covered. Review two downgraded "untested" to minor, and approved. All four steps ran on the same model. The harness had run the suite once after the first repair, and it was green. One green run of a race test. Forty-three minutes, ten dollars. I reverted that file by hand. Nothing was pushed and nothing was denied. Every agent told the truth. The gate still approved an untested change.

### 03. One factory, seven places the runtime bit

*1:10, starts at 2:35*

Here is the factory as a pipeline, with the seven topics from the abstract pinned where each one bit. I will take them roughly in the order they bit, across two runs on the 27th and a CI job the next day, and save fast cloning for last, because that is where the fork comes in. Every evidence slide carries a tag: measured in my own run records, built and tested, proposed, or other people's work. And here is the scope, said once so I do not hedge every slide. The two runs used Docker's sandbox, not my platform. Two observations that day come from islo. My harness answered the approval gates, not a person. Leases were built but off. And nothing forked.

### 04. A factory needs a wall, a fork and a count

*1:30, starts at 3:45*

That run needs three things from its runtime. A wall: control over what a cell can reach, change and report. A fork: alternatives from a state we already paid to reach. And a count: knowing what those alternatives actually found. To be fair to the sandbox, some of what went wrong is plain policy. Scope-check the repair loop, make an out-of-plan edit a blocker, use a different reviewer, and give the repair a way to run tests. No runtime needed for those. The rest needs the runtime, and one question needs a count: what is one green run of a race test worth? What I claim is a worker and reducer contract, real traces, and a hypothesis you can reject. What I do not claim is a new estimator, a speed ranking, a factory that forks today, or a dependence model from lineage. The one line to remember: execution multiplicity is not evidence multiplicity.

### 05. Allowlists name hosts; the web redirects

*1:15, starts at 5:15*

The wall first. Surface one, networking. The work order itself was a network bug, seen on islo that morning. The sandbox allowlist named astral dot sh. But astral dot sh answers with a redirect to another host that was not on the list, and the installer's fallback goes to GitHub's release-asset host, also not on the list. So curl returned 403, uv never installed, and the tests could never pass. The list lived in five places, and they had drifted. The fix added both hosts. Be honest about what that does: the second host admits every release asset on GitHub. The lesson is granularity. A list of names is the wrong unit when the web is a graph of redirects. The build-system answer is to fetch by content digest, through a caching proxy.

### 06. Filesystem state: what a snapshot shares

*1:25, starts at 6:30*

Surface two, filesystem state. A snapshot captures a boundary, not the universe, so each kind of state needs a policy. Files and build outputs are pinned by content digest; OBuilder, from this building's ecosystem, snapshots every build step on ZFS or btrfs. The workspace disk is shared copy-on-write, as overlay layers in day10, as DeltaBox's layered filesystem, and as DeepSeek's chained snapshots. Guest memory is mapped from the image and faulted in on first touch, so the real cost of a restore is the working set, not the copy; REAP made cold starts almost four times faster just by prefetching it. Agent history stays outside the VM. Randomness is reseeded or coupled on purpose, and external services are mediated; both come back later. So measure time to useful work, not time to resume.

### 07. Locking the tests was not enough

*1:40, starts at 7:55*

Surface three, build and test. We did the standard thing. The tests directory was write-protected by a hook, and the agent was told so. It never tried to edit a test, so the hook never fired. It did not matter. Planned steps are scope-checked against the files they declare; repairs are not, so the repair loop could touch any file. The repair changed the code under test, not the test. An out-of-plan edit counts as major, not as a blocker, and the writer and both reviewers were one model. Two of those are policy fixes, not runtime fixes, and I will say so. This is not special to my factory. METR saw o3 reward-hack in about thirty percent of RE-Bench runs and under one percent of HCAST runs, and suggests the visible scorer on RE-Bench is why. ImpossibleBench shows read-only tests stop test edits but not special-casing. And the Kimi K3 report names the fixes: isolate agents from verifiers, keep hidden verifiers, limit submission budgets. Run, evaluate and promote are three permissions, and each grader gets a budget.

### 08. The agent never pushes; its token still copies

*1:35, starts at 9:35*

Surface four, networking and credentials. The orchestrator holds the GitHub token and delivers only after the gate. The agent never pushes. The work cell has no GitHub token and deny-by-default egress. In islo's design the model credential is injected by an egress gateway, so it never sits in the cell, and Docker's sandbox documents the same idea: a host-side proxy injects the header and the raw credential never enters the VM. But be precise, because this room will be. What the cell holds is a placeholder, and a placeholder is still a bearer string in guest memory. Fork the VM and you copy it. Forked children are bit-identical, so nothing inside them tells them apart. And the model endpoint itself carries arbitrary bytes out. So the next step, which is proposed, is that the gateway keys each request on identity the host assigns, a per-clone tap device or a vsock ID, and a restore bumps a generation and voids the parent's lease. Capabilities and macaroons are the right vocabulary.

### 09. Teardown must not destroy the experiment

*1:15, starts at 11:10*

Surface five, recovery. A second work order the same day went well, then badly. Build and test passed first time. Review approved. Then delivery was refused three times: the workspace had a file outside the reviewed commits. That file was my own harness's review archive, mirrored into the workspace. So the gate was right to refuse. What happened next was wrong: teardown destroyed the cell, and the approved candidate with it. Twenty-six minutes, three dollars forty, nothing delivered. The fix is not exotic. The artifact has to leave the cell before the cell dies; a patch file on the host would have been enough. A crash, a refusal or a long human wait should destroy a worker, never the experiment. For a day-long human gate: snapshot, destroy, restore.

### 10. A green check is not proof the check ran

*1:15, starts at 12:25*

Surface six, observability. Three receipts, all mine. First, a CI job that evaluates the islo lane reported success in three seconds, because the key was unset and every real step was skipped. Second, my approvals file records the gates as mode human, actor admin. It was my harness answering. Third, my own islo command line printed its status messages on the same standard output as the program it ran, and an earlier attempt that day died trying to parse them. All three are my own receipts, and each was wrong. I would rather tell you than have you find them. So every check needs a receipt that says it actually ran, on a channel the child cannot write. This room knows that problem as provenance, from PASS and CamFlow; the supply-chain world calls it in-toto.

### 11. What the run pins, and what it cannot

*1:10, starts at 13:40*

Surface seven, reproducibility. The run record pins the input commit and the lockfile, digests of the policy, the inputs and the sandbox adapter, and the output of every agent step. It does not pin the hosted model, which has no sampling seed I control; the external hosts and their redirects; the clock; or the source of my sandbox adapter, which is a local shim that is not in the repository yet. So the honest target is replay, not rerun: log every model response, every external fetch through that caching proxy, and every clock read, and re-execute the rest against the log. That is rr's rule, and DeepSeek logs every sandbox command for the same reason. Today a scientist could audit this run. Nobody could rerun it.

### 12. Parallel-safe steps, and nothing to fork them

*1:05, starts at 14:50*

Last on the wall, fast cloning. The plan had three steps. The tests step was safe to run in parallel with the other two, and the executor asked its sandbox provider for a fork. None offered one, so it ran them in series and wrote down why: serial fallback, missing fork. Had tests run in a fork, the critical path would have been about three minutes shorter, out of forty-three. And these steps touch disjoint files, so two worktrees would have done. So speed is not why we fork. A fork matters when the reached state is expensive, and when we want alternatives.

### 13. Fork is old, and much of it ran on Xen

*1:40, starts at 15:55*

Now the fork. Fork is old, and much of it was built on Xen, in this building. Potemkin flash-cloned honeypot VMs with copy-on-write memory in 2005. SnowFlock forked Xen VMs across hosts in 2009, in six to eight hundred milliseconds, and its very first example is our pattern: run trusted code, fork, and give the child the untrusted work. Catalyzer forked running sandboxes; Nephele brought fork to unikernel VMs on Xen. This year DeltaBox checkpoints agent sandboxes in about eleven milliseconds, and Shepherd forks them in about 140. Moonshot's Kimi K3 report counts fifty-one million sandboxes across training and evaluation, and its microVM runtime offers fork, in their words, for reward judging without side effects. By fork I mean forking a whole machine, not the POSIX fork call, which Baumann and colleagues argued we should retire. The mechanism is old. The caller is new: a program that searches, reads git history and games tests.

### 14. Fork copies memory, secrets and identity

*1:35, starts at 17:35*

Fork copies memory, so it copies everything in memory. Five things follow the child that must not. Random state: siblings share random streams. VMGenID reseeds the kernel generator, but Firecracker's own documentation says there is no generic solution for userspace. Tokens: eight forks of a VM holding a token are eight live tokens, which is why the secret should never be in the guest, and why AWS proposed wiping memory on suspend. The clock resumes at snapshot time. Network identity: every clone has the same IP and MAC, so each needs its own namespace and NAT; in 2005 Potemkin already spent 142 of its 521 milliseconds configuring IP. And nobody clones an open TCP connection. CRIU can hand an open connection to one restored copy, not to eight, and gVisor resets it. A runtime for search has to make all five part of the fork contract.

### 15. Hold effects until an authority releases them

*1:05, starts at 19:10*

External effects. A restore cannot unsend an email or un-push a branch, and the answers here are old too. Speculator and external synchrony ran ahead speculatively and held output until it was safe. Remus held network output until the checkpoint committed. This year Zheng and colleagues state the agent version: an execution edit cannot undo a tool request already sent. In my factory the rule is structural: children hold no credential that can publish, and the orchestrator delivers once, after the gate. In these runs it delivered to a local git remote. The one exception is the model API: every child uses it, and it is metered and logged, not held. Output commit, made structural.

### 16. When fork pays, and where it loses

*1:55, starts at 20:15*

When does fork pay? Without a fork you prepare N times. With a fork you prepare once, capture once, and pay a restore and divergence per child. The inequality is just that. Fork loses in three places. With one child. When the state is only files and your build cache is good, which is the lesson I learned at Incredibuild. And when a minimal image boots faster than you can restore: the Jitsu argument from this room, and LightVM's from NEC Labs. Now my number, carefully. From a named 141-megabyte islo snapshot, one restore, run and capture through the public API takes 6.87 seconds at the median, at concurrency twelve, and 255 of 256 succeeded. I have not yet shown that snapshot includes memory, so call it restore fan-out, not fork. The mechanisms are far faster: Kimi reports checkpoints as fast as 133 milliseconds, DeltaBox about eleven. And Kimi reports that a sandbox spends up to 98 percent of its life waiting on the model. So fork does not pay in seconds. It pays for state you cannot rebuild cheaply, and for a grader the child cannot touch.

### 17. Two axes: what a child can reach, and name

*1:05, starts at 22:10*

Isolation has two axes, and this building built both. One is kernel surface: a container shares one kernel, gVisor puts a kernel in user space, and a microVM or a unikernel stands on hardware virtualisation. The other is authority: an ordinary process can name whatever its user can; under Capsicum or on CHERI it can use only what it is handed. Work cells run arbitrary builds, so they get a microVM. Their authority should be handed over explicitly, never ambient. Kimi reports kernel panics in its early container runtimes, and Firecracker's production guide says to disable simultaneous multithreading and same-page merging, because both are side channels. We call it a swarm. The operating system calls it roommates.

### 18. Machines fork; authority stays outside

*1:45, starts at 23:15*

Here is the architecture with honest labels. Solid boxes are built and ran: an Airflow scheduler with a durable journal and a run lock, the work cells, and a gate that binds an approval to the exact artifact hash. Dashed gold is built or designed but not exercised: a lease broker that ties each credential to an attempt, a cell and an epoch, and an evaluator outside the cell. Dashed red is missing: the fork store. I wrote the fork contract before I had the fork. It has eight conditions: a content-addressed parent; a lease and budget per branch; no publishing credentials; recorded parent and evidence identities; never count siblings that reuse evidence as independent agreement; merge deterministically; verify the merge; and tear down every child. Promotion is epoch-fenced, which is Chubby's sequencer and Kleppmann's fencing token, and there is a TLA+ design model of it, not yet checked against real traces. I can model-check promotion. I cannot model-check what a child will write. That is why the count is statistics, and condition five is where the rest of this talk goes.

### 19. The second review was not a second witness

*1:05, starts at 25:00*

Now the count. Go back to that run. Repair two was written against review one's verdict, and graded by the same model. The candidate adapted to its grader, which is the adaptive-data-analysis problem Dwork and colleagues named: a reused holdout stops being a holdout. So review two was one independent look at best, not a second witness. And the thing the factory asked for makes a second problem. Fork the repair loop nine times from the same parent, and suppose all nine go green. That is not nine witnesses either. Same parent, same model, same prompt, same flaky test. So the runtime has to record both: what feedback each candidate saw, and what its siblings share.

### 20. Execution multiplicity is not evidence multiplicity

*1:25, starts at 26:05*

Here is the arithmetic. If N runs have the same variance and a common pairwise correlation rho, the variance of their average has a floor at rho times sigma squared. More runs approach the floor; they never go below it. The same thing as an effective sample size: a hundred forks at a correlation of point one are worth about nine independent witnesses. At point five, two. And the correlation is not hypothetical. Kim and colleagues studied more than 350 language models; on one leaderboard, when two models are both wrong, they give the same wrong answer sixty percent of the time. So execution multiplicity is not evidence multiplicity. Nine clones are not nine witnesses, and past the floor, more forks buy nothing.

### 21. The runtime holds some of the cluster labels

*1:30, starts at 27:30*

I want to be precise about what is new, because it is not the statistics. Correlated evidence has a sixty-year literature: Kish's design effect, cluster-robust variance, meta-analysis of dependent effect sizes, and in databases, provenance as annotations on derived results. All of them need the same input: cluster labels. The runtime holds some of those labels and nobody else does: which runs share a parent, a seed, a test, a fixture. Today it throws them away and returns a score. But lineage cannot label everything. It cannot label a shared model's blind spots, which is exactly what Kim and colleagues measured. And parent, model and test are crossed factors, not nested ones, so a handful of snapshot families is too few clusters for any interval. So: the runtime must hand over the labels it has. Turning them into a dependence model is still open, and my paper says so.

### 22. Fork is also how you run the control

*0:55, starts at 29:00*

Dependence is not always the enemy. To compare two candidates, give them the same random draw, and the nuisance variation cancels in the difference. That is common random numbers, old in simulation. To corroborate a claim you want the opposite: vary the randomness and the failure modes. A fork decides which one you get, by whether it copies the random state or reseeds it. So the seed policy belongs in the fork API, as an explicit choice.

### 23. Every worker returns a receipt, not a score

*1:45, starts at 29:55*

That is my contribution. Every worker returns a receipt, not a score: an estimate, its information, the sample size, the identities of the evidence it used, its fork lineage, and metadata. Here is exactly what is built. The numeric summaries merge in any tree order, so it fits MapReduce-style reduction. If two workers declare the same evidence, the merge stops instead of counting it twice. And lineage travels with the result, although nothing consumes it yet. Here is what is proposed: an admission step that keeps one execution per evidence identity, so a retry is never double-counted, and a reducer that abstains when dependence is unknown instead of reporting the narrow interval independence would imply. For a pass probability you do not even need the Gaussian machinery; counts add exactly. The Gaussian path is for workers that report estimates. The estimator is Cochran's inverse-variance weighting. The contract is what was missing. One trace runs it end to end, from a named snapshot through four workers.

### 24. Isolation does not authenticate precision

*1:10, starts at 31:40*

One more trap. Isolation bounds what a child can do. It does not bound what a child can claim. In a synthetic check from the paper, one worker reports a distant estimate from a two-thousand-point shard, and inflates its reported precision a further fifty times. Unprotected pooling moves to seventeen. A simple stress heuristic brings it back to about five, and that heuristic is not a Byzantine guarantee. Measuring the sample size alone would not help, because the forgery is in the information per point. The fix is architectural: precision has to come from evidence the controller holds, by re-running or re-scoring on held-out data. Precision is an input the child should not control.

### 25. The test that could prove me wrong

*2:00, starts at 32:50*

Everything so far is one run and a synthetic check. Whether it generalises is an experiment, so here is the test that could prove me wrong, written down before any run. Phase A is cost, with no model calls: a cold cell with no cache, a cached template, and a restore, at one to twelve children, timed on the server where it can be. If restore does not beat a good cached template, fork buys nothing for this factory, and I will say so. Phase B is coupling, also with no model calls. Eighteen siblings from six snapshots, against eighteen strangers run at the same times. Each runs the flaky race test thirty times. If siblings fail together no more than strangers do, shared ancestry did not couple the evidence here. Phase C re-samples the repair loop nine times from its recorded input, and simply counts how often it makes the same out-of-plan edit. That one is descriptive. The results, held or failed, will be in the repository. A result where the build cache wins is a good result for this room.

### 26. The same work order, run as it should be

*1:05, starts at 34:50*

So here is the same work order, run the way the runtime should run it. Fork after the plan is approved, each child with its own lease and budget. The repair loop's scope is enforced, so the out-of-plan edit is denied instead of being reported as major. The evaluator lives outside the cells and uses a different model. The reducer reports an effective number of witnesses from lineage, or abstains. The artifact leaves the cell before teardown, and promotion is fenced by an epoch, so a stale worker cannot commit. Review two would not count as a second witness. Search can race. Promotion must not. This is a design, not a run.

### 27. Open problems where this room is ahead of me

*1:20, starts at 35:55*

I will end with open problems, where I think this room is ahead of me. One: estimate the dependence from lineage. Given fork trees and evidence manifests, what can we say about rho without running everything twice? Two: leases that fork. A child's capability should be re-minted on restore, revocable, and never ambient. Three: warm state and side channels. Sharing warm pages is performance, and it is also a channel, so we should pack forks by trust and not only by utilisation. Four: evidence commit. We know how to hold network output; how do we hold effects on remote services and on people? Five: when does a content-addressed build beat a live fork? Six: a human gate can take a day; the machine should not wait alive for it. I would especially like help with the first two.

### 28. Fork the machine, not the trust.

*0:30, starts at 37:15*

Fork the machine, not the trust. State without secrets. Graders the children cannot write. Receipts that outlive the cell. Evidence counted, not executions. And authority committed once. Burn the cell; keep the receipt. Thank you. I am happy to take questions.

## Backup slides

### B1. Paper Table 2: exercised API paths, not a provider ranking

Bring this up only if asked about speed. The operations differ: two rows are sandbox creation, the islo row is restore plus run plus capture. They are not comparable as latencies, and none of them is a mechanism latency.

### B2. Agent checkpoint and fork, 2026

None of these systems treats sibling outputs as correlated evidence; they optimise checkpoint latency or safety. Planarian, from Imperial, spans local and remote state and rolls remote state back with compensating actions.

### B3. Arp2/3 shapes network dynamics

This is a result from mechanochemical simulations of branched actomyosin networks. At high Arp2/3 concentration the network stalls; at low concentration it contracts; at an intermediate concentration, loosely connected clusters can collapse suddenly under motor activity. My graph-theoretic work studies how local connectivity relates to global morphology, while the avalanche study uses network science and machine learning to forecast collective rearrangements. Stockmayer's random-branching polymer theory is a formal precedent for asking when local branching yields system-scale connectivity, under its own idealized assumptions. A related question for agent systems is whether communication links connect otherwise separate lineages and reduce effective diversity; its threshold must be derived for the actual dependency model. These biological and polymer results motivate that question, but do not predict software behavior.

### B4. Reset changes the learning problem

Reusing a difficult-to-reach state can make exploration productive, as return-and-explore methods illustrate. But a policy trained primarily from favorable intermediate checkpoints has seen a different starting-state distribution. We cannot silently substitute its performance for task-start performance. Depending on the algorithm, distribution correction, curriculum design, or explicit reporting may be necessary. Snapshot ancestry records where experience came from. The final evaluation should still test the deployment question we claim to answer.

### B5. Three graphs describe the computation

Ancestry records where execution state came from, often as a tree or DAG. Communication adds edges that need not follow ancestry; these edges can introduce dependencies among later decisions. Composition concerns sets of artifacts and may need hyperedges for three-way or higher-order effects. The outline around the three candidates denotes a possible higher-order interaction, not a measured one. Keeping these structures separate avoids calling every relationship a fork. It also clarifies which metadata the controller must retain.

### B6. What does a message contribute?

The XOR example is exact and deliberately small. Either bit alone leaves H uniformly random; together they determine H. After receiving A, B contributes one bit of conditional information. This is information synergy, not the finite-difference score interaction between two software patches. In practical search we rarely know the joint distribution well enough to compute mutual information directly. Treat it as a precise way to ask what a message could add, not a ready-made universal routing score. Here, think of H as which candidate the evidence would favor under the declared objective, and E_k as a branch report. The next slide makes that distinction concrete. Useful decision information also depends on costs and available actions.

### B7. How eight changes work together

Gamma is a second finite difference of a declared scalar objective. It measures non-additivity such as synergy, conflict, or saturation, and may itself require repeated measurements. It is not mutual information or quantum interference. Define an application order or canonical composition procedure; if the patches do not compose, record a failure rather than inventing a score. Eight candidates have 28 unordered pairs, while all subsets number 256 including the empty set. Pairwise screening can guide an economical search but cannot certify every higher-order interaction.

### B8. What the reducer experiments establish

The logistic check uses five IID shards with sample sizes 60, 120, 400, 2000, and 5000. Across eight fixed seeds the information-weighted estimate is closer to the centralized maximum-likelihood estimate than equal coefficient averaging. This specific check does not establish universal efficiency or superiority to other distributed estimators. The forged-precision example motivates trustworthy information estimates, not a claim of Byzantine robustness. These are reported results from the paper; they are not new agent-task benchmark measurements.

### B9. Ablations that explain the outcome

These ablations distinguish mechanisms. A fast fork with a worse search policy may lose. A communicating system may win only because it spends more model calls. Sharing can help discovery while increasing evidence dependence. Evaluate communication with an equal full resource budget and record the induced selection history. For composition, include deliberately interacting changes rather than only independent patches. Use uncertainty across tasks and seeds and reserve fresh validation for selected results.

### B10. Evaluation under adaptive search

Access control prevents direct tampering. It does not prevent a candidate generator from adapting to repeated pass/fail or score feedback. The final reported score may then be optimistic even when every individual evaluation was computed correctly. A fresh held-out evaluation or a statistically justified adaptive procedure addresses a different failure mode from sandbox isolation. If final-validation feedback is fed back into further selection, it has become development feedback and the protocol must account for that.

### B11. The fork contract, before the fork

The full contract, quoted from the repository. Condition five is the bridge to the count; condition eight is the SELFHOST-3 lesson.

### B12. References: systems

Systems references. Every figure on a main slide is traceable to one of these or to a named run file.

### B13. References: evidence and evaluation

Evidence and evaluation references.
