# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from `talk.tex` by `tools/presenter_guide.py`. 33 main slides, 20 backups. Planned talk: **43:20**, 4253 spoken words, 98 wpm average, peak 108 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:20 | 0:00-0:20 | 32 | 96 |
| 2 | Hedging needs independent slowdowns | 1:15 | 0:20-1:35 | 117 | 94 |
| 3 | Forks find answers. Checks decide which. | 1:15 | 1:35-2:50 | 112 | 90 |
| 4 | Numbers every agent runtime should know | 1:20 | 2:50-4:10 | 118 | 88 |
| 5 | Where 43 minutes went | 1:00 | 4:10-5:10 | 86 | 86 |
| 6 | Blocker. One more repair. Approve. | 1:30 | 5:10-6:40 | 153 | 102 |
| 7 | One factory, seven places the runtime bit | 0:55 | 6:40-7:35 | 93 | 101 |
| 8 | A factory needs a wall, a fork and a count | 1:05 | 7:35-8:40 | 114 | 105 |
| 9 | Allowlists name hosts; the web redirects | 1:20 | 8:40-10:00 | 140 | 105 |
| 10 | Keys stay outside; a fork copies the inside | 1:10 | 10:00-11:10 | 120 | 103 |
| 11 | Filesystem state: what a snapshot shares | 0:55 | 11:10-12:05 | 91 | 99 |
| 12 | Locking the tests was not enough | 1:15 | 12:05-13:20 | 129 | 103 |
| 13 | Teardown must not destroy the experiment | 1:15 | 13:20-14:35 | 135 | 108 |
| 14 | A green check is not proof the check ran | 1:20 | 14:35-15:55 | 144 | 108 |
| 15 | What the run pins, and what it cannot | 1:30 | 15:55-17:25 | 154 | 103 |
| 16 | Parallel-safe steps, and nothing to fork them | 1:15 | 17:25-18:40 | 126 | 101 |
| 17 | The shape of an agent sandbox, drawn in 2009 | 1:20 | 18:40-20:00 | 120 | 90 |
| 18 | Fork copies memory, secrets and identity | 1:35 | 20:00-21:35 | 146 | 92 |
| 19 | What each kind of fork copies | 1:35 | 21:35-23:10 | 145 | 92 |
| 20 | Hold effects until an authority releases them | 1:05 | 23:10-24:15 | 115 | 106 |
| 21 | When fork pays, and where it loses | 1:30 | 24:15-25:45 | 136 | 91 |
| 22 | Isolation has two axes: kernel and authority | 1:25 | 25:45-27:10 | 152 | 107 |
| 23 | The interface the runtime owes the factory | 1:40 | 27:10-28:50 | 160 | 96 |
| 24 | The second review was not a second witness | 1:35 | 28:50-30:25 | 163 | 103 |
| 25 | More forks are not more witnesses | 1:55 | 30:25-32:20 | 172 | 90 |
| 26 | The runtime holds some of the cluster labels | 1:35 | 32:20-33:55 | 154 | 97 |
| 27 | Every worker returns a receipt, not a score | 1:45 | 33:55-35:40 | 167 | 95 |
| 28 | A sandbox bounds actions, not claims | 1:10 | 35:40-36:50 | 114 | 98 |
| 29 | Test 1: does restore beat a warm cache? | 1:30 | 36:50-38:20 | 143 | 95 |
| 30 | Test 2: do siblings fail together? | 1:30 | 38:20-39:50 | 140 | 93 |
| 31 | The same work order, run as it should be | 1:25 | 39:50-41:15 | 150 | 106 |
| 32 | Open problems where this room is ahead of me | 1:00 | 41:15-42:15 | 102 | 102 |
| 33 | Hedging works when failures are independent. | 1:05 | 42:15-43:20 | 110 | 102 |

## Script

### 01. Forkable Sandboxes

*0:20, starts at 0:00*

Thank you for having me. I work on distributed builds at Incredibuild, and I build an agent sandbox platform called islo. I will say that once and then talk only about components.

### 02. Hedging needs independent slowdowns

*1:15, starts at 0:20*

In 2013 Jeff Dean and Luiz Barroso described a trick that is now widely used. Send a request to a second replica, and keep whichever answer comes first. In one Google benchmark it cut the 99.9th-percentile latency from 1,800 milliseconds to 74, for two percent more requests. And they said why it works: the slowness is often not in the request. It is interference, and the replicas do not share it. AI agents now play the same trick for correctness. Run the attempt several times; keep the one that passes. But a wrong answer often is in the request: the same prompt, the same model, the same starting state, the same flaky test. The copies share it.

### 03. Forks find answers. Checks decide which.

*1:15, starts at 1:35*

So does hedging for correctness work? Partly, and the numbers are striking. Sample a coding model two hundred and fifty times and it solves fifty-six percent of SWE-bench Lite instead of sixteen. Forks find answers. But only when something can tell which answer is right. Without an automatic check, voting and reward models plateau. And a check that says yes to wrong answers caps the whole thing: when a wrong answer costs more than no answer, Stroebl and colleagues find the best number of tries is often under ten. So hedging for correctness is only as good as the check you hedge on. This talk is about the runtime underneath that check.

### 04. Numbers every agent runtime should know

*1:20, starts at 2:50*

Jeff Dean gave us numbers everyone should know. Here is the list I wish someone had handed me for agent runtimes. Checkpoint a sandbox: eleven milliseconds. Fork one: about a hundred and forty. SnowFlock forked Xen VMs across hosts in 2009 in under a second. One work order in my factory: forty-three minutes and ten dollars. One frontier lab created fifty-one million sandboxes for a single model, and its sandboxes spend up to ninety-eight percent of their lives waiting on the model. The primitives take milliseconds. Through a public API, seconds. The work takes minutes. Every row has a source, except the last: how correlated two forks' verdicts are. That row decides what every other row is worth.

### 05. Where 43 minutes went

*1:00, starts at 4:10*

Now my own numbers. This is one work order in my open-source software factory, on the 27th of September. Forty-three minutes. Setting up the sandbox took twenty seconds: under one percent. Build and test took almost half, review the other half, and both are agents and checks. Make sandbox setup a hundred times faster and this run gets eight tenths of a percent faster. Amdahl sends his regards. The minutes are in the agents and the checks. And, as it turns out, so is the risk.

### 06. Blocker. One more repair. Approve.

*1:30, starts at 5:10*

Here is what happened inside that run. The work order was small: fix the sandbox allowlist. A four-thread race test failed, and the loop sent a repair agent. That agent had no shell, and it said so: it could not run the tests. It rewrote code outside the plan. Review one said: blocker, untested and unverified. The tests were locked, so the second repair restructured the code and argued it was covered. Review two downgraded "untested" to minor, and approved. One model did all four steps. A committee of one. The suite passed after each repair, nineteen hundred and seventy-two tests. But the new branch had no test of its own. Both repairs said they had not run the tests. The gate approved anyway. I reverted it by hand. Now suppose the loop had forked that repair nine times, and all nine came back green. How many witnesses is that? Hold that question.

### 07. One factory, seven places the runtime bit

*0:55, starts at 6:40*

The talk you signed up for promised seven topics. Here they are, pinned on the factory pipeline where each one bit, numbered in the order I will take them, across two runs on the 27th and a CI job the next day. Every evidence slide carries a tag: measured in my own records, built and tested, proposed, or other people's work. And the scope, said once: the runs used Docker's sandbox, not my platform. Two observations come from islo. My harness answered the approval gates, not a person. Leases were off. Nothing forked.

### 08. A factory needs a wall, a fork and a count

*1:05, starts at 7:35*

So the runtime owes the factory three things. A wall: control over what a cell can reach, change and report. A fork: alternatives from a state we already paid for. And a count: knowing what those alternatives actually found. What I claim: a receipt contract, which is built; two real runs, which are measured; and two hypotheses, one about cost and one about coupling, which I will show you how to reject. What I do not claim: a new estimator, a speedup, a ranking of vendors, or a factory that forks today. The one sentence to take home: forks multiply executions, not evidence. And the runtime is where you can see what forks share.

### 09. Allowlists name hosts; the web redirects

*1:20, starts at 8:40*

The wall first. Surface one is networking and credentials; start with the network. The work order itself was a network bug, seen on islo that morning. The sandbox allowlist named astral dot sh. But astral dot sh answers with a redirect to another host that was not on the list, and the installer's fallback goes to GitHub's release-asset host, also not on the list. So curl returned 403, uv never installed, and the tests could never pass. The list lived in five places, and they had drifted. The fix added both hosts. Be honest about what that does: the second host admits every release asset on GitHub. The lesson is granularity. A list of names is the wrong unit when the web is a graph of redirects. The build-system answer is to fetch by content digest, through a caching proxy.

### 10. Keys stay outside; a fork copies the inside

*1:10, starts at 10:00*

Same surface, the credential half. The orchestrator holds the GitHub token and delivers only after the gate. The agent never pushes. The cell has no GitHub token and deny-by-default egress. The model credential is injected by an egress gateway, as Docker's sandbox also documents: the raw credential never enters the VM. But the cell still holds a placeholder, and a placeholder is a bearer string in guest memory. Fork the VM and you copy it; forked children are bit-identical. And the model endpoint carries arbitrary bytes out. The proposed next step: the gateway keys each request on identity the host assigns, a per-clone tap or vsock ID, and a restore voids the parent's lease. Capabilities and macaroons are the vocabulary.

### 11. Filesystem state: what a snapshot shares

*0:55, starts at 11:10*

Surface two, filesystem state. A snapshot captures a boundary, not the universe, so each kind of state needs a policy. Files and build outputs are pinned by content digest; OBuilder snapshots every build step on ZFS or btrfs. The workspace disk is shared copy-on-write: as overlay layers in day10, as DeltaBox's layered filesystem, and as DeepSeek's chained snapshots. Agent history stays outside the VM. Randomness and external services come back later in the talk. Memory is the part a filesystem cannot share, and I will come to it with the fork.

### 12. Locking the tests was not enough

*1:15, starts at 12:05*

Surface three, build and test. The tests directory was write-protected, and the agent was told. It never tried to edit a test, so the hook never fired. It did not matter. Planned steps are scope-checked; repairs are not. The repair changed the code under test. An out-of-plan edit counts as major, not a blocker, and writer and reviewers were one model. Two of those are policy fixes, not runtime. Published work agrees. METR saw o3 reward-hack in about thirty percent of RE-Bench runs and under one percent of HCAST, and suggests the visible scorer may be why. ImpossibleBench shows read-only tests stop test edits, not special-casing. Kimi K3 names the fix: isolate agents from verifiers, and keep the verifiers hidden. Run, evaluate and promote are three permissions, not one.

### 13. Teardown must not destroy the experiment

*1:15, starts at 13:20*

Surface four, recovery. A second work order the same day went well, then badly. Build and test passed first time. Review approved. Then delivery was refused three times: the workspace had a file outside the reviewed commits. That file was my own harness's review archive, mirrored into the workspace. The gate was protecting the repository from me. So it was right to refuse. What happened next was wrong: teardown destroyed the cell, and the approved candidate with it. Twenty-six minutes, three dollars forty, nothing delivered. The fix is not exotic. The artifact has to leave the cell before the cell dies; a patch file on the host would have been enough. A crash, a refusal or a long human wait should destroy a worker, never the experiment. For a day-long human gate: snapshot, destroy, restore.

### 14. A green check is not proof the check ran

*1:20, starts at 14:35*

Surface five, observability. Three receipts, all mine. First, a CI job that evaluates the islo lane reported success in three seconds, because the key was unset and every real step was skipped. My fastest CI job ever, because it did nothing. Second, my approvals file records the gates as mode human, actor admin. It was my harness answering. Third, my own islo command line printed its status messages on the same standard output as the program it ran, and an earlier attempt that day died trying to parse them. All three are my own receipts, and each was wrong. I would rather tell you than have you find them. So every check needs a receipt that says it actually ran, on a channel the child cannot write. This room knows that problem as provenance, from PASS and CamFlow; the supply-chain world calls it in-toto.

### 15. What the run pins, and what it cannot

*1:30, starts at 15:55*

Surface six, reproducibility. The run record pins the input commit and the lockfile, digests of the policy, the inputs and the sandbox adapter, and the output of every agent step. It does not pin the hosted model, which has no seed I control; external hosts and their redirects; the clock; or my sandbox adapter's source, a local shim not yet in git. So the honest target is replay, not rerun: log every model response, every external fetch through that caching proxy, and every clock read, and re-execute the rest against the log. That is rr's rule, and DeepSeek's. Genomics set the audit bar years ago: in the ENCODE pipelines I worked on, every data file is captured in the portal with the software versions, parameters and reference genome that produced it. This run is close; the gaps are the hosted model and my adapter's source. So you can audit it. You cannot rerun it.

### 16. Parallel-safe steps, and nothing to fork them

*1:15, starts at 17:25*

Last on the wall, surface seven, fast cloning. The plan had three steps. The tests step was safe to run in parallel with the other two, and the executor asked its sandbox provider for a fork. None offered one, so it ran them in series and wrote down why: serial fallback, missing fork. Had tests run in a fork, the critical path would have been about three minutes shorter, out of forty-three. And these steps touch disjoint files, so two worktrees would have done. So speed is not why we fork. We fork when the reached state is expensive, and when we want alternatives. That is the wall. Seven surfaces, one rule: whatever you must trust lives outside the cell. Now let us copy the cell.

### 17. The shape of an agent sandbox, drawn in 2009

*1:20, starts at 18:40*

These are two of the four patterns in Figure 1 of SnowFlock, EuroSys 2009. It forked Xen virtual machines, and Xen came from this lab. Pattern (a) is called sandboxing. Run trusted code, fork, give the child the untrusted code, and the parent waits. That is the shape of an agent sandbox, drawn seventeen years ago. Pattern (b) is parallel computation: each child works on data indexed by its own fork ID, so the ID picks its slice. Now fork an agent's repair nine times. Same state, same tests. Nine children, one slice. The rest of the lineage is in the backup. The mechanism is old. The caller is new: a program that searches, reads git history and games tests.

### 18. Fork copies memory, secrets and identity

*1:35, starts at 20:00*

Fork copies memory, so it copies everything in memory. Five things follow the child that must not. Random state: siblings share random streams. VMGenID reseeds the kernel generator, but Firecracker's own documentation says there is no generic solution for userspace. Tokens: eight forks of a VM holding a token are eight live tokens, which is why the secret should never be in the guest, and why AWS proposed wiping memory on suspend. The clock resumes at snapshot time. Network identity: every clone has the same IP and MAC, so each needs its own namespace and NAT; in 2005 Potemkin already spent 142 of its 521 milliseconds configuring IP. And nobody clones an open TCP connection. CRIU can hand an open connection to one restored copy, not to eight, and gVisor resets it. A runtime for search has to make all five part of the fork contract.

### 19. What each kind of fork copies

*1:35, starts at 21:35*

What does a fork actually copy? Children share memory until they write, so the total is the shared part plus each child's private pages. Four mechanisms, four answers. A worktree or an overlay layer keeps files only, and costs the bytes each child writes. A container checkpoint with CRIU keeps processes and memory, but an open TCP connection needs its original IP, so at most one restored copy can keep it. A microVM snapshot keeps guest memory and device state, with disks handled separately, and the real cost is the pages each child touches after restore; REAP showed that is where cold starts go. Record and replay keeps a log instead of a state. One caution. A restore that returns OK is not fidelity: before a child counts, compare restored and direct runs on the outputs you declared. Cheap at fork; you pay at divergence.

### 20. Hold effects until an authority releases them

*1:05, starts at 23:10*

External effects. A restore cannot unsend an email or un-push a branch, and the answers here are old too. Speculator and external synchrony ran ahead speculatively and held output until it was safe. Remus held network output until the checkpoint committed. This year Zheng and colleagues state the agent version: an execution edit cannot undo a tool request already sent. In my factory the rule is structural: children hold no credential that can publish, and the orchestrator delivers once, after the gate. In these runs it delivered to a local git remote. The one exception is the model API: every child uses it, and it is metered and logged, not held. Output commit, made structural.

### 21. When fork pays, and where it loses

*1:30, starts at 24:15*

When does fork pay? Without a fork you prepare N times. With a fork you prepare once, capture once, and pay a restore and divergence per child. Work and evaluation, including every model call, appear on both sides and cancel. And a restored process does not run your patch: each child still rebuilds. So fork loses with one child, when the state is only files and your build cache is good, which is the Incredibuild lesson, and when a minimal image boots faster than you can restore: the Jitsu argument from this room, and LightVM's from NEC Labs. My own number is an API round trip, 6.87 seconds, and until I show the snapshot holds memory, it is restore fan-out, not fork. Fork does not pay in seconds. It pays for state you cannot rebuild cheaply.

### 22. Isolation has two axes: kernel and authority

*1:25, starts at 25:45*

Isolation has two axes, and this building built both. One is kernel surface: a container shares one kernel, gVisor puts a kernel in user space, and a microVM or a unikernel stands on hardware virtualisation. The other is authority: an ordinary process can name whatever its user can; under Capsicum or on CHERI it can use only what it is handed. Work cells run arbitrary builds, so they get a microVM, and their authority is handed over explicitly. Then there is warm state, which is where build systems live. A build cache is performance and also a channel, so share it within one trust domain; share dependency images by digest, so a poisoned base is caught; and never share scratch. Kimi reports kernel panics in its early container runtimes, and Firecracker's production guide says to disable simultaneous multithreading and same-page merging. We call it a swarm. The operating system calls it roommates.

### 23. The interface the runtime owes the factory

*1:40, starts at 27:10*

If this is a runtime layer, here is the interface it owes the factory. Checkpoint a cell into a snapshot; islo has named snapshots today, as disk images. Fork a snapshot with a lease, an explicit seed policy, copy or reseed, and an egress policy. Evaluate an artifact outside the child, and get back a receipt. Select one candidate on a fresh test: that is choosing, and it is not pooling. Reduce receipts into an estimate and an effective number of witnesses, or abstain; the merge and the evidence check are built, abstention is proposed. And promote once: the gate that binds approval to the artifact hash is built, and the epoch fence, which is Chubby's sequencer and Kleppmann's fencing token, is proposed. There is a TLA+ design model of promotion with explicit invariants, not yet checked against real traces. Promotion is small enough to model-check. What a child will write is not. That is why the count is statistics.

### 24. The second review was not a second witness

*1:35, starts at 28:50*

Now the count, and the question I asked you to hold. Go back to that run. Repair two was written against review one's verdict, and graded by the same model. The candidate adapted to its grader, which is the adaptive-data-analysis problem Dwork and colleagues named: a reused holdout stops being a holdout. So review two was one independent look at best. Now the nine forks. There are two different questions hiding there. Nine forks that write nine different patches is choosing, and choosing needs a fresh test. Nine re-runs of one patch is confirming, and it is capped by what the runs share. How many greens would confirming need? Review two itself says the race reaches the new code only when the interleaving happens to lose an activation. If that happens one run in ten, you need twenty-nine independent green runs before the chance of missing it drops below five percent. Independent is the hard word. Nine green forks are not nine witnesses.

### 25. More forks are not more witnesses

*1:55, starts at 30:25*

Here is the arithmetic, and the one number to remember from it: a hundred forks can be worth nine witnesses. If N runs have the same variance and a common pairwise correlation rho, the variance of their average has a floor at rho times sigma squared. More runs approach the floor; they never go below it. As an effective sample size: at a correlation of point one, a hundred forks are worth about nine witnesses; at point five, two. In evidence terms: four re-runs of a hundred tests are four hundred executions but a hundred evidence identities, and until rho is measured they count as a hundred. Pool within a candidate, compare across candidates. And the correlation is not hypothetical. Kim and colleagues found that on one leaderboard, two models that are both wrong give the same wrong answer sixty percent of the time. A shared blind spot is bias, not variance: no number of re-runs averages it away. Forks multiply executions, not evidence. If you remember one sentence, remember that one.

### 26. The runtime holds some of the cluster labels

*1:35, starts at 32:20*

What is new is not the statistics. Correlated evidence has a sixty-year literature: Kish's design effect, cluster-robust variance, dependent effect sizes, provenance as annotations. All of it needs cluster labels. The runtime holds some of those labels and nobody else does: which runs share a parent, a seed, a test, a fixture, and, through the egress gateway, which model they called. My co-authors and I have had to uncover structure like this from outside twice: address linking tied most early bitcoin to sixty-four agents, and malignant cells cluster by patient rather than by cell type. A fork runtime does not have to recover anything. It writes the labels. It cannot label a shared model's blind spots, and parent, model and test are crossed factors, so you need multiway clustering, and a wild-cluster bootstrap when clusters are few. Others must recover cluster labels. A fork runtime can write them. The dependence model is still open.

### 27. Every worker returns a receipt, not a score

*1:45, starts at 33:55*

That is my contribution. Every worker returns a receipt, not a score: an estimate, its information, the sample size, the identities of the evidence it used, its fork lineage, and metadata. Here is exactly what is built. The numeric summaries merge in any tree order, so it fits MapReduce-style reduction. If two workers declare the same evidence, the merge stops instead of counting it twice. And lineage travels with the result, although nothing consumes it yet. Here is what is proposed: one execution per evidence identity, so a retry is never double-counted, and a reducer that abstains when dependence is unknown instead of reporting the narrow interval independence would imply. For a pass probability the counts simply add, but m siblings inflate the variance by one plus m minus one times rho, which is exactly the design effect. The estimator is Cochran's inverse-variance weighting. The contract is what was missing. A separate four-worker trace runs it end to end from a named snapshot, with no cold baseline.

### 28. A sandbox bounds actions, not claims

*1:10, starts at 35:40*

One more trap. Isolation bounds what a child can do. It does not bound what a child can claim. In a synthetic check from the paper, one worker reports a distant estimate from a two-thousand-point shard, and inflates its reported precision a further fifty times. Unprotected pooling moves to seventeen. A simple stress heuristic brings it back to about five, and that heuristic is not a Byzantine guarantee. Measuring the sample size alone would not help, because the forgery is in the information per point. The fix is architectural: precision has to come from evidence the controller holds, by re-running or re-scoring on held-out data. Precision is an input the child should not control.

### 29. Test 1: does restore beat a warm cache?

*1:30, starts at 36:50*

Everything so far is one run and a synthetic check. Whether it generalises is an experiment, so here are two tests that could prove me wrong, written down before any run. Test one is cost. First a gate: put a random value in RAM, snapshot, restore three children, and see whether it survives; if not, everything I report is restore fan-out, not fork. Then fidelity: deterministic tests must give identical outputs restored and direct. Then the comparison that matters: a cached template against a restore, twenty interleaved repetitions at each size, timed on the server to the first test result. If the whole interval for the gain sits below ten seconds at any size, the warm cache wins here, and I will say so; anything in between is inconclusive. A result where the build cache wins is a good result for this room.

### 30. Test 2: do siblings fail together?

*1:30, starts at 38:20*

Test two is coupling. Twelve snapshot families of three siblings, each paired with three strangers restored from other families, in the same slot on the same host, so the only difference is shared ancestry. Each triple runs the race test in lockstep rounds, at least three hundred, and the statistic is how correlated the three outcome sequences are, siblings minus strangers, tested by flipping signs across the twelve pairs. Above point zero five with p below point zero five, the thesis holds here. Confidently below point zero five, it does not. Why do I expect coupling? Part of my PhD was on actomyosin networks, where how filaments link and branch reshapes the whole network's connectivity, and branched networks show rare, sudden avalanches. A motivation, not a prediction. Last, the loop: re-sample the repair nine times and count the out-of-plan edits.

### 31. The same work order, run as it should be

*1:25, starts at 39:50*

So here is the same work order, run the way the runtime should run it. Fork after the plan is approved, three children here because that is the sandbox cap I run at, each with its own lease and budget. The repair loop's scope is enforced, so the out-of-plan edit is denied instead of being reported as major. The evaluator lives outside the cells, uses another model family and hidden tests the repair loop never saw, and scores the frozen candidate once, so the holdout stays a holdout. The reducer clusters receipts by lineage and reports the number of runs, a bound on the effective number of witnesses from the coupling test, or abstains. The artifact leaves the cell before teardown, and promotion is fenced by an epoch. Review two would not count as a second witness. Search can race. Promotion must not. This is a design, not a run.

### 32. Open problems where this room is ahead of me

*1:00, starts at 41:15*

I will end with open problems, where I think this room is ahead of me. Six are on the slide. I will talk about two, because I want help with them. One: estimate dependence from lineage. Given fork trees and evidence manifests, what can we say about rho without running everything twice? Two: leases that fork. A child's capability should be re-minted on restore, revocable, and never ambient. The other four are on the slide for questions: side channels in warm state; holding effects on remote services and people; when a content-addressed build beats a live fork; and a day-long human gate.

### 33. Hedging works when failures are independent.

*1:05, starts at 42:15*

Hedging works when failures are independent. The runtime's job is to know when they are not. Remember the blank row in the table: how correlated two forks' verdicts are. No system I surveyed reports it. Test two is how I plan to fill it in. In 2009 the parent's last line was wait. Ours has to be count: reduce the receipts by lineage, or abstain. My bet: agents will soon fork far more often than people commit. Then the runtime that matters is the one that can tell you what a thousand green checks are worth. Fork the machine, not the trust. Thank you. I am happy to take questions.

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

### B11. TLA+ promotion invariants

Use this if someone asks why promotion is not also statistics. The invariants are written for TLC under the README's stated assumptions; no TLC run is recorded here yet, and the next step is checking that real control-kernel traces are admitted by the model.

### B12. Machines fork; authority stays outside

Here is the architecture with honest labels. Solid boxes are built and ran: an Airflow scheduler with a durable journal and a run lock, the work cells, and a gate that binds an approval to the exact artifact hash. Dashed gold is built or designed but not exercised: a lease broker that ties each credential to an attempt, a cell and an epoch, and an evaluator outside the cell. Dashed red is missing: the fork store. I wrote the fork contract before I had the fork. It has eight conditions: a content-addressed parent; a lease and budget per branch; no publishing credentials; recorded parent and evidence identities; never count siblings that reuse evidence as independent agreement; merge deterministically; verify the merge; and tear down every child. Condition five is where the rest of this talk goes.

### B13. Fork is old, and much of it was built on Xen

Now the fork. Fork is old, and much of it was built on Xen, in this building. Live migration, from here in 2005, already moved a running VM's memory by pre-copying dirty pages, with sixty milliseconds of downtime for a game server. Potemkin flash-cloned honeypot VMs with copy-on-write memory. SnowFlock forked Xen VMs across hosts in 2009, in six to eight hundred milliseconds, and its very first example is our pattern: run trusted code, fork, and give the child the untrusted work. Catalyzer forked running gVisor sandboxes; Nephele brought fork to unikernel VMs on Xen. This year DeltaBox checkpoints agent sandboxes in about eleven milliseconds, and Shepherd forks them in about 140. And Moonshot's Kimi K3 report offers fork, in their words, for reward judging without side effects. By fork I mean forking a whole machine, not the POSIX fork call, which Baumann and colleagues argued we should retire. The mechanism is old. The caller is new: a program that searches, reads git history and games tests.

### B14. Fork is also how you run the control

Dependence is not always the enemy. To compare two candidates, give them the same random draw, and the nuisance variation cancels in the difference. That is common random numbers, old in simulation. To corroborate a claim you want the opposite: vary the randomness and the failure modes. A fork decides which one you get, by whether it copies the random state or reseeds it. So the seed policy belongs in the fork API, as an explicit choice.

### B15. Research record: biophysics

PhD work at the University of Houston and Rice: graph theory of actomyosin network shape, Arp2/3 branching and avalanches, protein folding and calcium binding. This is the motivation for Test 2, not evidence for it.

### B16. Research record: genomics

Genome architecture, bioinformatics and cancer genomics at Baylor, NRGene, HIT and Harvard. ENCODE sets the reproducibility bar on slide 15; per-patient clustering is a cluster-label story.

### B17. Research record: preprints, systems and talks

Preprints, systems work and talks. The three-body e-print is on an AI-assisted server and is not peer reviewed; say so if asked.

### B18. References: systems

Systems references. Every figure on a main slide is traceable to these, to the slide's own source line, or to a named run file.

### B19. References: evidence and evaluation

Evidence and evaluation references.

### B20. References: own work and documentation

The speaker's own and co-authored work cited on main slides, and the documentation behind slides 10, 11, 18, 19 and 22.
