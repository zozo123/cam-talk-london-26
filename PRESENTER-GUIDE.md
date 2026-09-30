# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from `talk.tex` by `tools/presenter_guide.py`. 31 main slides, 13 backups. Planned talk: **42:45**, 4248 spoken words, 99 wpm average, peak 108 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:45 | 0:00-0:45 | 80 | 107 |
| 2 | Blocker. One more repair. Approve. | 2:00 | 0:45-2:45 | 206 | 103 |
| 3 | One factory, seven places the runtime bit | 1:10 | 2:45-3:55 | 121 | 104 |
| 4 | A factory needs a wall, a fork and a count | 1:30 | 3:55-5:25 | 158 | 105 |
| 5 | Allowlists name hosts; the web redirects | 1:20 | 5:25-6:45 | 140 | 105 |
| 6 | The agent never pushes; its token still copies | 1:35 | 6:45-8:20 | 169 | 107 |
| 7 | Filesystem state: what a snapshot shares | 1:00 | 8:20-9:20 | 95 | 95 |
| 8 | Locking the tests was not enough | 1:40 | 9:20-11:00 | 178 | 107 |
| 9 | Teardown must not destroy the experiment | 1:15 | 11:00-12:15 | 128 | 102 |
| 10 | A green check is not proof the check ran | 1:15 | 12:15-13:30 | 135 | 108 |
| 11 | What the run pins, and what it cannot | 1:10 | 13:30-14:40 | 126 | 108 |
| 12 | Parallel-safe steps, and nothing to fork them | 1:05 | 14:40-15:45 | 105 | 97 |
| 13 | Fork is old, and much of it was built on Xen | 1:45 | 15:45-17:30 | 167 | 95 |
| 14 | Fork copies memory, secrets and identity | 1:35 | 17:30-19:05 | 146 | 92 |
| 15 | What each kind of fork copies | 1:35 | 19:05-20:40 | 148 | 93 |
| 16 | Hold effects until an authority releases them | 1:05 | 20:40-21:45 | 115 | 106 |
| 17 | When fork pays, and where it loses | 2:00 | 21:45-23:45 | 190 | 95 |
| 18 | Two axes: what a child can reach, and name | 1:25 | 23:45-25:10 | 152 | 107 |
| 19 | Machines fork; authority stays outside | 1:20 | 25:10-26:30 | 136 | 102 |
| 20 | The interface the runtime owes the factory | 1:35 | 26:30-28:05 | 147 | 93 |
| 21 | The second review was not a second witness | 1:30 | 28:05-29:35 | 156 | 104 |
| 22 | More forks are not more witnesses | 1:35 | 29:35-31:10 | 140 | 88 |
| 23 | The runtime holds some of the cluster labels | 1:25 | 31:10-32:35 | 141 | 100 |
| 24 | Fork is also how you run the control | 0:55 | 32:35-33:30 | 77 | 84 |
| 25 | Every worker returns a receipt, not a score | 1:45 | 33:30-35:15 | 163 | 93 |
| 26 | Isolation does not authenticate precision | 1:10 | 35:15-36:25 | 114 | 98 |
| 27 | Test 1: does restore beat a warm cache? | 1:30 | 36:25-37:55 | 138 | 92 |
| 28 | Test 2: do siblings fail together? | 1:40 | 37:55-39:35 | 165 | 99 |
| 29 | The same work order, run as it should be | 1:20 | 39:35-40:55 | 139 | 104 |
| 30 | Open problems where this room is ahead of me | 1:20 | 40:55-42:15 | 138 | 104 |
| 31 | Fork the machine, not the trust. | 0:30 | 42:15-42:45 | 35 | 70 |

## Script

### 01. Forkable Sandboxes

*0:45, starts at 0:00*

Thank you for having me. I work on distributed builds at Incredibuild, I teach at HIT, and I build an agent sandbox platform called islo. I'll disclose that once and then only talk about components. In build systems I learned that recomputing the world is insane. So the state I wanted to reuse for speed became the state I had to isolate for trust. This talk is about that runtime layer, and about one run that shows why it matters.

### 02. Blocker. One more repair. Approve.

*2:00, starts at 0:45*

Let me start with a real run. On the 27th of September my software factory worked on its own code. The work order was small: fix the sandbox's network allowlist. Along the way a four-thread race test failed, and the loop sent a repair agent. That agent had no shell, and it said so: it could not run the tests. It read the code, decided the bug was in the race logic, and rewrote it, in a file no plan listed. Review one said: blocker, untested and unverified. So the loop tried again. The tests were locked, so it could not add one. It restructured the code, said plainly it had not run the suite, and argued the change was already covered. Review two downgraded "untested" to minor, and approved. All four steps ran on the same model. The suite had run once, after the first repair, and it was green. The second repair never ran under test before it was approved. I reverted that file by hand. Every agent told the truth. The gate approved a change no test had run. Now suppose the loop had forked that repair nine times, and all nine came back green. How many witnesses is that? Hold that question.

### 03. One factory, seven places the runtime bit

*1:10, starts at 2:45*

Here is the factory as a pipeline, with the seven topics from the abstract pinned where each one bit, and numbered in the order I will take them: across two runs on the 27th and a CI job the next day, saving fast cloning for last, because that is where the fork comes in. Every evidence slide carries a tag: measured in my own run records, built and tested, proposed, or other people's work. And here is the scope, said once so I do not hedge every slide. The two runs used Docker's sandbox, not my platform. Two observations that day come from islo. My harness answered the approval gates, not a person. Leases were built but off. And nothing forked.

### 04. A factory needs a wall, a fork and a count

*1:30, starts at 3:55*

That run needs three things from its runtime. A wall: control over what a cell can reach, change and report. A fork: alternatives from a state we already paid to reach. And a count: knowing what those alternatives actually found. To be fair to the sandbox, some of what went wrong is plain policy. Scope-check the repair loop, make an out-of-plan edit a blocker, use a different reviewer, and give the repair a way to run tests. No runtime needed for those. Here is what I claim, by tag. Built: a receipt contract, where reused evidence stops the merge and lineage travels with every result. Measured: two real factory runs. Proposed: two hypotheses I will test, one about cost and one about coupling. What I do not claim: a new estimator, a controlled speedup, a ranking of platforms, a factory that forks today, or a dependence model. The one line to remember: execution multiplicity is not evidence multiplicity.

### 05. Allowlists name hosts; the web redirects

*1:20, starts at 5:25*

The wall first. Surface one is networking and credentials; start with the network. The work order itself was a network bug, seen on islo that morning. The sandbox allowlist named astral dot sh. But astral dot sh answers with a redirect to another host that was not on the list, and the installer's fallback goes to GitHub's release-asset host, also not on the list. So curl returned 403, uv never installed, and the tests could never pass. The list lived in five places, and they had drifted. The fix added both hosts. Be honest about what that does: the second host admits every release asset on GitHub. The lesson is granularity. A list of names is the wrong unit when the web is a graph of redirects. The build-system answer is to fetch by content digest, through a caching proxy.

### 06. The agent never pushes; its token still copies

*1:35, starts at 6:45*

Same surface, the credential half. The orchestrator holds the GitHub token and delivers only after the gate. The agent never pushes. The work cell has no GitHub token and deny-by-default egress. In islo's design the model credential is injected by an egress gateway, so it never sits in the cell, and Docker's sandbox documents the same idea: a host-side proxy injects the header and the raw credential never enters the VM. But be precise, because this room will be. What the cell holds is a placeholder, and a placeholder is still a bearer string in guest memory. Fork the VM and you copy it. Forked children are bit-identical, so nothing inside them tells them apart. And the model endpoint itself carries arbitrary bytes out. So the next step, which is proposed, is that the gateway keys each request on identity the host assigns, a per-clone tap device or a vsock ID, and a restore bumps a generation and voids the parent's lease. Capabilities and macaroons are the right vocabulary.

### 07. Filesystem state: what a snapshot shares

*1:00, starts at 8:20*

Surface two, filesystem state. A snapshot captures a boundary, not the universe, so each kind of state needs a policy. Files and build outputs are pinned by content digest; OBuilder, from this building's ecosystem, snapshots every build step on ZFS or btrfs. The workspace disk is shared copy-on-write: as overlay layers in day10, as DeltaBox's layered filesystem, and as DeepSeek's chained snapshots. Agent history stays outside the VM. Randomness and external services come back later in the talk. Memory is the part a filesystem cannot share, and I will come to it with the fork.

### 08. Locking the tests was not enough

*1:40, starts at 9:20*

Surface three, build and test. We did the standard thing. The tests directory was write-protected by a hook, and the agent was told so. It never tried to edit a test, so the hook never fired. It did not matter. Planned steps are scope-checked against the files they declare; repairs are not, so the repair loop could touch any file. The repair changed the code under test, not the test. An out-of-plan edit counts as major, not as a blocker, and the writer and both reviewers were one model. Two of those are policy fixes, not runtime fixes, and I will say so. This is not special to my factory. METR saw o3 reward-hack in about thirty percent of RE-Bench runs and under one percent of HCAST runs, and suggests the visible scorer on RE-Bench is why. ImpossibleBench shows read-only tests stop test edits but not special-casing. And the Kimi K3 report names the fixes: isolate agents from verifiers, keep hidden verifiers, limit submission budgets. Run, evaluate and promote are three permissions, and each grader gets a budget.

### 09. Teardown must not destroy the experiment

*1:15, starts at 11:00*

Surface four, recovery. A second work order the same day went well, then badly. Build and test passed first time. Review approved. Then delivery was refused three times: the workspace had a file outside the reviewed commits. That file was my own harness's review archive, mirrored into the workspace. So the gate was right to refuse. What happened next was wrong: teardown destroyed the cell, and the approved candidate with it. Twenty-six minutes, three dollars forty, nothing delivered. The fix is not exotic. The artifact has to leave the cell before the cell dies; a patch file on the host would have been enough. A crash, a refusal or a long human wait should destroy a worker, never the experiment. For a day-long human gate: snapshot, destroy, restore.

### 10. A green check is not proof the check ran

*1:15, starts at 12:15*

Surface five, observability. Three receipts, all mine. First, a CI job that evaluates the islo lane reported success in three seconds, because the key was unset and every real step was skipped. Second, my approvals file records the gates as mode human, actor admin. It was my harness answering. Third, my own islo command line printed its status messages on the same standard output as the program it ran, and an earlier attempt that day died trying to parse them. All three are my own receipts, and each was wrong. I would rather tell you than have you find them. So every check needs a receipt that says it actually ran, on a channel the child cannot write. This room knows that problem as provenance, from PASS and CamFlow; the supply-chain world calls it in-toto.

### 11. What the run pins, and what it cannot

*1:10, starts at 13:30*

Surface six, reproducibility. The run record pins the input commit and the lockfile, digests of the policy, the inputs and the sandbox adapter, and the output of every agent step. It does not pin the hosted model, which has no sampling seed I control; the external hosts and their redirects; the clock; or the source of my sandbox adapter, which is a local shim that is not in the repository yet. So the honest target is replay, not rerun: log every model response, every external fetch through that caching proxy, and every clock read, and re-execute the rest against the log. That is rr's rule, and DeepSeek logs every sandbox command for the same reason. Today a scientist could audit this run. Nobody could rerun it.

### 12. Parallel-safe steps, and nothing to fork them

*1:05, starts at 14:40*

Last on the wall, surface seven, fast cloning. The plan had three steps. The tests step was safe to run in parallel with the other two, and the executor asked its sandbox provider for a fork. None offered one, so it ran them in series and wrote down why: serial fallback, missing fork. Had tests run in a fork, the critical path would have been about three minutes shorter, out of forty-three. And these steps touch disjoint files, so two worktrees would have done. So speed is not why we fork. A fork matters when the reached state is expensive, and when we want alternatives.

### 13. Fork is old, and much of it was built on Xen

*1:45, starts at 15:45*

Now the fork. Fork is old, and much of it was built on Xen, in this building. Live migration, from here in 2005, already moved a running VM's memory by pre-copying dirty pages, with sixty milliseconds of downtime for a game server. Potemkin flash-cloned honeypot VMs with copy-on-write memory. SnowFlock forked Xen VMs across hosts in 2009, in six to eight hundred milliseconds, and its very first example is our pattern: run trusted code, fork, and give the child the untrusted work. Catalyzer forked running gVisor sandboxes; Nephele brought fork to unikernel VMs on Xen. This year DeltaBox checkpoints agent sandboxes in about eleven milliseconds, and Shepherd forks them in about 140. And Moonshot's Kimi K3 report offers fork, in their words, for reward judging without side effects. By fork I mean forking a whole machine, not the POSIX fork call, which Baumann and colleagues argued we should retire. The mechanism is old. The caller is new: a program that searches, reads git history and games tests.

### 14. Fork copies memory, secrets and identity

*1:35, starts at 17:30*

Fork copies memory, so it copies everything in memory. Five things follow the child that must not. Random state: siblings share random streams. VMGenID reseeds the kernel generator, but Firecracker's own documentation says there is no generic solution for userspace. Tokens: eight forks of a VM holding a token are eight live tokens, which is why the secret should never be in the guest, and why AWS proposed wiping memory on suspend. The clock resumes at snapshot time. Network identity: every clone has the same IP and MAC, so each needs its own namespace and NAT; in 2005 Potemkin already spent 142 of its 521 milliseconds configuring IP. And nobody clones an open TCP connection. CRIU can hand an open connection to one restored copy, not to eight, and gVisor resets it. A runtime for search has to make all five part of the fork contract.

### 15. What each kind of fork copies

*1:35, starts at 19:05*

What does a fork actually copy? Children share memory until they write, so the total is the shared part plus each child's private pages. Four mechanisms, four answers. A worktree or an overlay layer keeps files only, and costs the bytes each child writes. A container checkpoint with CRIU keeps processes and memory, but an open TCP connection can be restored only once. A microVM snapshot keeps guest memory and device state, with disks handled separately, and the real cost is the pages each child touches after restore; REAP showed that is where cold starts go. Record and replay keeps a log instead of a state. Two cautions. A restore that returns OK is not fidelity: before a child counts, compare restored and direct runs on the outputs you declared. And I have not yet verified that islo's snapshot captures memory. Cheap at fork; you pay at divergence.

### 16. Hold effects until an authority releases them

*1:05, starts at 20:40*

External effects. A restore cannot unsend an email or un-push a branch, and the answers here are old too. Speculator and external synchrony ran ahead speculatively and held output until it was safe. Remus held network output until the checkpoint committed. This year Zheng and colleagues state the agent version: an execution edit cannot undo a tool request already sent. In my factory the rule is structural: children hold no credential that can publish, and the orchestrator delivers once, after the gate. In these runs it delivered to a local git remote. The one exception is the model API: every child uses it, and it is metered and logged, not held. Output commit, made structural.

### 17. When fork pays, and where it loses

*2:00, starts at 21:45*

When does fork pay? Without a fork you prepare N times. With a fork you prepare once, capture once, and pay a restore and divergence per child. The work and the evaluation, including every model call, appear on both sides and cancel. And a restored process does not run your patch: each child still rebuilds. Fork loses in three places. With one child. When the state is only files and your build cache is good, which is the lesson I learned at Incredibuild. And when a minimal image boots faster than you can restore: the Jitsu argument from this room, and LightVM's from NEC Labs. Now my number, carefully. From a named 141-megabyte islo snapshot, one restore, run and capture through the public API takes 6.87 seconds at the median, at concurrency twelve, and 255 of 256 succeeded. That is a latency, not a mechanism, and until I show the snapshot holds memory, it is restore fan-out, not fork. Kimi reports a sandbox spends up to 98 percent of its life waiting on the model. So fork does not pay in seconds. It pays for state you cannot rebuild cheaply.

### 18. Two axes: what a child can reach, and name

*1:25, starts at 23:45*

Isolation has two axes, and this building built both. One is kernel surface: a container shares one kernel, gVisor puts a kernel in user space, and a microVM or a unikernel stands on hardware virtualisation. The other is authority: an ordinary process can name whatever its user can; under Capsicum or on CHERI it can use only what it is handed. Work cells run arbitrary builds, so they get a microVM, and their authority is handed over explicitly. Then there is warm state, which is where build systems live. A build cache is performance and also a channel, so share it within one trust domain; share dependency images by digest, so a poisoned base is caught; and never share scratch. Kimi reports kernel panics in its early container runtimes, and Firecracker's production guide says to disable simultaneous multithreading and same-page merging. We call it a swarm. The operating system calls it roommates.

### 19. Machines fork; authority stays outside

*1:20, starts at 25:10*

Here is the architecture with honest labels. Solid boxes are built and ran: an Airflow scheduler with a durable journal and a run lock, the work cells, and a gate that binds an approval to the exact artifact hash. Dashed gold is built or designed but not exercised: a lease broker that ties each credential to an attempt, a cell and an epoch, and an evaluator outside the cell. Dashed red is missing: the fork store. I wrote the fork contract before I had the fork. It has eight conditions: a content-addressed parent; a lease and budget per branch; no publishing credentials; recorded parent and evidence identities; never count siblings that reuse evidence as independent agreement; merge deterministically; verify the merge; and tear down every child. Condition five is where the rest of this talk goes.

### 20. The interface the runtime owes the factory

*1:35, starts at 26:30*

If this is a runtime layer, here is the interface it owes the factory. Checkpoint a cell into a snapshot; islo has named snapshots today, as disk images, and memory is unverified. Fork a snapshot with a lease, an explicit seed policy, copy or reseed, and an egress policy. Evaluate an artifact outside the child, and get back a receipt. Select one candidate on a fresh test: that is choosing, and it is not pooling. Reduce receipts into an estimate and an effective number of witnesses, or abstain; the merge and the evidence check are built, abstention is proposed. And promote once, under an epoch fence, which is Chubby's sequencer and Kleppmann's fencing token. There is a TLA+ design model of promotion, not yet checked against real traces. I can model-check promotion. I cannot model-check what a child will write. That is why the count is statistics.

### 21. The second review was not a second witness

*1:30, starts at 28:05*

Now the count, and the question I asked you to hold. Go back to that run. Repair two was written against review one's verdict, and graded by the same model. The candidate adapted to its grader, which is the adaptive-data-analysis problem Dwork and colleagues named: a reused holdout stops being a holdout. So review two was one independent look at best. Now the nine forks. There are two different questions hiding there. Nine forks that write nine different patches is choosing, and choosing needs a fresh test. Nine re-runs of one patch is confirming, and it is capped by what the runs share. How many greens would confirming need? Review two itself says the race reaches the new code only when the interleaving happens to lose an activation. If that happens one run in ten, you need twenty-nine independent green runs before the chance of missing it drops below five percent. Independent is the hard word.

### 22. More forks are not more witnesses

*1:35, starts at 29:35*

Here is the arithmetic. If N runs have the same variance and a common pairwise correlation rho, the variance of their average has a floor at rho times sigma squared. More runs approach the floor; they never go below it. As an effective sample size: a hundred forks at a correlation of point one are worth about nine independent witnesses; at point five, two. In evidence terms: four re-runs of a hundred tests are a hundred pieces of evidence, not four hundred. Pool within a candidate, compare across candidates. And the correlation is not hypothetical. Kim and colleagues found that on one leaderboard, two models that are both wrong give the same wrong answer sixty percent of the time. A shared blind spot is bias, not variance: no number of re-runs averages it away. Execution multiplicity is not evidence multiplicity.

### 23. The runtime holds some of the cluster labels

*1:25, starts at 31:10*

I want to be precise about what is new, because it is not the statistics. Correlated evidence has a sixty-year literature: Kish's design effect, cluster-robust variance, meta-analysis of dependent effect sizes, and in databases, provenance as annotations on derived results. All of them need the same input: cluster labels. The runtime holds some of those labels and nobody else does: which runs share a parent, a seed, a test, a fixture. Today it throws them away and returns a score. But lineage cannot label everything. It cannot label a shared model's blind spots. And parent, model and test are crossed factors, not nested ones, so the tools are multiway clustering and, with few clusters, a wild-cluster bootstrap. So: the runtime must hand over the labels it has. Turning them into a dependence model is still open, and my paper says so.

### 24. Fork is also how you run the control

*0:55, starts at 32:35*

Dependence is not always the enemy. To compare two candidates, give them the same random draw, and the nuisance variation cancels in the difference. That is common random numbers, old in simulation. To corroborate a claim you want the opposite: vary the randomness and the failure modes. A fork decides which one you get, by whether it copies the random state or reseeds it. So the seed policy belongs in the fork API, as an explicit choice.

### 25. Every worker returns a receipt, not a score

*1:45, starts at 33:30*

That is my contribution. Every worker returns a receipt, not a score: an estimate, its information, the sample size, the identities of the evidence it used, its fork lineage, and metadata. Here is exactly what is built. The numeric summaries merge in any tree order, so it fits MapReduce-style reduction. If two workers declare the same evidence, the merge stops instead of counting it twice. And lineage travels with the result, although nothing consumes it yet. Here is what is proposed: one execution per evidence identity, so a retry is never double-counted, and a reducer that abstains when dependence is unknown instead of reporting the narrow interval independence would imply. For a pass probability the counts simply add, but m siblings inflate the variance by one plus m minus one times rho, which is exactly the design effect. The estimator is Cochran's inverse-variance weighting. The contract is what was missing. A separate four-worker trace runs it end to end from a named snapshot.

### 26. Isolation does not authenticate precision

*1:10, starts at 35:15*

One more trap. Isolation bounds what a child can do. It does not bound what a child can claim. In a synthetic check from the paper, one worker reports a distant estimate from a two-thousand-point shard, and inflates its reported precision a further fifty times. Unprotected pooling moves to seventeen. A simple stress heuristic brings it back to about five, and that heuristic is not a Byzantine guarantee. Measuring the sample size alone would not help, because the forgery is in the information per point. The fix is architectural: precision has to come from evidence the controller holds, by re-running or re-scoring on held-out data. Precision is an input the child should not control.

### 27. Test 1: does restore beat a warm cache?

*1:30, starts at 36:25*

Everything so far is one run and a synthetic check. Whether it generalises is an experiment, so here are two tests that could prove me wrong, written down before any run. Test one is cost. First a gate: put a random value in RAM, snapshot, restore three children, and see whether it survives; if not, everything I report is restore fan-out, not fork. Then fidelity: deterministic tests must give identical outputs restored and direct. Then the comparison that matters to this room: a cached template against a restore, twenty interleaved repetitions at each size, timed on the server to the first test result. If restore does not beat the cache by ten seconds, fork buys nothing for this factory, and I will say so. A result where the build cache wins is a good result for this room.

### 28. Test 2: do siblings fail together?

*1:40, starts at 37:55*

Test two is coupling. Twelve snapshot families of three siblings each, and each family paired with three strangers started in the same slot on the same host, so the only difference is shared ancestry. A pilot sets how many runs each cell gets, so every cell expects at least ten failures of the race test. Each triple runs the test in lockstep rounds, and the statistic is how correlated its three outcome sequences are: siblings minus strangers, tested by flipping signs across the twelve pairs. If siblings fail together more than strangers by more than point zero five, the thesis holds here. If the difference is confidently within point zero five of zero, shared ancestry did not couple the evidence, and I will say that. Point zero five matters because nine siblings at that correlation are worth only six and a half witnesses. Last, the loop: re-sample the repair nine times and count how often it makes the same out-of-plan edit. That one is descriptive.

### 29. The same work order, run as it should be

*1:20, starts at 39:35*

So here is the same work order, run the way the runtime should run it. Fork after the plan is approved, each child with its own lease and budget. The repair loop's scope is enforced, so the out-of-plan edit is denied instead of being reported as major. The evaluator lives outside the cells, uses another model family and hidden tests the repair loop never saw, and scores the frozen candidate once, so the holdout stays a holdout. The reducer clusters receipts by lineage and reports the number of runs, a bound on the effective number of witnesses from the coupling test, or abstains. The artifact leaves the cell before teardown, and promotion is fenced by an epoch. Review two would not count as a second witness. Search can race. Promotion must not. This is a design, not a run.

### 30. Open problems where this room is ahead of me

*1:20, starts at 40:55*

I will end with open problems, where I think this room is ahead of me. One: estimate the dependence from lineage. Given fork trees and evidence manifests, what can we say about rho without running everything twice? Two: leases that fork. A child's capability should be re-minted on restore, revocable, and never ambient. Three: warm state and side channels. Sharing warm pages is performance, and it is also a channel, so we should pack forks by trust and not only by utilisation. Four: evidence commit. We know how to hold network output; how do we hold effects on remote services and on people? Five: when does a content-addressed build beat a live fork? Six: a human gate can take a day; the machine should not wait alive for it. I would especially like help with the first two.

### 31. Fork the machine, not the trust.

*0:30, starts at 42:15*

Fork the machine, not the trust. State without secrets. Graders the children cannot write. Receipts that outlive the cell. Evidence counted, not executions. And authority committed once. Thank you. I am happy to take questions.

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

### B6. How eight changes work together

Gamma is a second finite difference of a declared scalar objective. It measures non-additivity such as synergy, conflict, or saturation, and may itself require repeated measurements. It is not mutual information or quantum interference. Define an application order or canonical composition procedure; if the patches do not compose, record a failure rather than inventing a score. Eight candidates have 28 unordered pairs, while all subsets number 256 including the empty set. Pairwise screening can guide an economical search but cannot certify every higher-order interaction.

### B7. What the reducer experiments establish

The logistic check uses five IID shards with sample sizes 60, 120, 400, 2000, and 5000. Across eight fixed seeds the information-weighted estimate is closer to the centralized maximum-likelihood estimate than equal coefficient averaging. This specific check does not establish universal efficiency or superiority to other distributed estimators. The forged-precision example motivates trustworthy information estimates, not a claim of Byzantine robustness. These are reported results from the paper; they are not new agent-task benchmark measurements.

### B8. Ablations that explain the outcome

These ablations distinguish mechanisms. A fast fork with a worse search policy may lose. A communicating system may win only because it spends more model calls. Sharing can help discovery while increasing evidence dependence. Evaluate communication with an equal full resource budget and record the induced selection history. For composition, include deliberately interacting changes rather than only independent patches. Use uncertainty across tasks and seeds and reserve fresh validation for selected results.

### B9. Evaluation under adaptive search

Access control prevents direct tampering. It does not prevent a candidate generator from adapting to repeated pass/fail or score feedback. The final reported score may then be optimistic even when every individual evaluation was computed correctly. A fresh held-out evaluation or a statistically justified adaptive procedure addresses a different failure mode from sandbox isolation. If final-validation feedback is fed back into further selection, it has become development feedback and the protocol must account for that.

### B10. The fork contract, before the fork

The full contract, quoted from the repository. Condition five is the bridge to the count; condition eight is the SELFHOST-3 lesson.

### B11. Promotion invariants in the TLA+ design model

Use this if someone asks why promotion is not also statistics. The invariants are model-checked in TLC under stated assumptions; the next step is checking that real control-kernel traces are admitted by the model.

### B12. References: systems

Systems references. Every figure on a main slide is traceable to one of these or to a named run file.

### B13. References: evidence and evaluation

Evidence and evaluation references.
