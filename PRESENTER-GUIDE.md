# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from `talk.tex` by `tools/presenter_guide.py`. 48 main slides, 10 end-matter pages. Planned talk: **44:40**, 4403 spoken words, 99 wpm average, peak 109 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:45 | 0:00-0:45 | 82 | 109 |
| 2 | Hedging: ask twice, keep the first answer | 1:10 | 0:45-1:55 | 120 | 103 |
| 3 | Forks find answers. Checks decide which. | 0:50 | 1:55-2:45 | 89 | 107 |
| 4 | Numbers every agent runtime should know | 1:10 | 2:45-3:55 | 118 | 101 |
| 5 | Where 43 minutes went | 0:45 | 3:55-4:40 | 77 | 103 |
| 6 | Blocker. One more repair. Approve. | 1:35 | 4:40-6:15 | 158 | 100 |
| 7 | How a biophysicist ended up forking sandboxes | 1:05 | 6:15-7:20 | 110 | 102 |
| 8 | One factory, seven places the runtime bit | 0:45 | 7:20-8:05 | 74 | 99 |
| 9 | A factory needs a wall, a fork and a count | 0:55 | 8:05-9:00 | 90 | 98 |
| 10 | Allowlists name hosts; the web redirects | 0:50 | 9:00-9:50 | 86 | 103 |
| 11 | Keys stay outside; a fork copies the inside | 0:50 | 9:50-10:40 | 83 | 100 |
| 12 | Filesystem state: what a snapshot shares | 0:45 | 10:40-11:25 | 74 | 99 |
| 13 | Locking the tests was not enough | 0:55 | 11:25-12:20 | 88 | 96 |
| 14 | Reward hacking is the RL name for it | 0:55 | 12:20-13:15 | 90 | 98 |
| 15 | Teardown must not destroy the experiment | 0:55 | 13:15-14:10 | 97 | 106 |
| 16 | A green check is not proof the check ran | 0:55 | 14:10-15:05 | 91 | 99 |
| 17 | What the run pins, and what it cannot | 0:55 | 15:05-16:00 | 92 | 100 |
| 18 | Parallel-safe steps, and nothing to fork them | 0:45 | 16:00-16:45 | 73 | 97 |
| 19 | The shape of an agent sandbox, drawn in 2009 | 0:55 | 16:45-17:40 | 88 | 96 |
| 20 | Fork is old, and much of it was built on Xen | 1:00 | 17:40-18:40 | 96 | 96 |
| 21 | Training runs are sandbox factories | 1:05 | 18:40-19:45 | 105 | 97 |
| 22 | Reset changes the learning problem | 0:45 | 19:45-20:30 | 71 | 95 |
| 23 | Fork copies memory, secrets and identity | 0:55 | 20:30-21:25 | 90 | 98 |
| 24 | What each kind of fork copies | 0:55 | 21:25-22:20 | 93 | 101 |
| 25 | Hold effects until an authority releases them | 0:55 | 22:20-23:15 | 93 | 101 |
| 26 | When fork pays, and where it loses | 1:10 | 23:15-24:25 | 117 | 100 |
| 27 | Isolation has two axes: kernel and authority | 0:55 | 24:25-25:20 | 90 | 98 |
| 28 | The interface the runtime owes the factory | 0:55 | 25:20-26:15 | 91 | 99 |
| 29 | Machines fork; authority stays outside | 1:00 | 26:15-27:15 | 96 | 96 |
| 30 | Promotion is small enough to model-check | 0:45 | 27:15-28:00 | 73 | 97 |
| 31 | The second review was not a second witness | 1:00 | 28:00-29:00 | 100 | 100 |
| 32 | A reused grader becomes a training set | 0:45 | 29:00-29:45 | 75 | 100 |
| 33 | One formula, three fields | 0:55 | 29:45-30:40 | 95 | 104 |
| 34 | More forks are not more witnesses | 1:45 | 30:40-32:25 | 189 | 108 |
| 35 | The runtime holds some of the cluster labels | 0:55 | 32:25-33:20 | 87 | 95 |
| 36 | Fork is also how you run the control | 0:45 | 33:20-34:05 | 74 | 99 |
| 37 | When does a swarm gel? | 0:50 | 34:05-34:55 | 76 | 91 |
| 38 | Two green patches can fail together | 0:45 | 34:55-35:40 | 73 | 97 |
| 39 | Every worker returns a receipt, not a score | 1:00 | 35:40-36:40 | 88 | 88 |
| 40 | A sandbox bounds actions, not claims | 0:55 | 36:40-37:35 | 84 | 92 |
| 41 | Test 1: does restore beat a warm cache? | 1:00 | 37:35-38:35 | 95 | 95 |
| 42 | Why I expect siblings to fail together | 0:40 | 38:35-39:15 | 65 | 98 |
| 43 | Test 2: do siblings fail together? | 1:00 | 39:15-40:15 | 94 | 94 |
| 44 | What two tests cannot separate | 0:40 | 40:15-40:55 | 61 | 92 |
| 45 | The same work order, run as it should be | 0:55 | 40:55-41:50 | 86 | 94 |
| 46 | Open problems where this room is ahead of me | 0:40 | 41:50-42:30 | 61 | 92 |
| 47 | The hedging paper already had the answer | 0:50 | 42:30-43:20 | 73 | 88 |
| 48 | Contributions | 1:20 | 43:20-44:40 | 132 | 99 |

## Script

### 01. Forkable Sandboxes

*0:45, starts at 0:00*

Thank you. I do distributed builds at Incredibuild and build Airflow Factory, an open-source software factory on Apache Airflow. Disclosure: I also build an agent sandbox platform; I do not rank vendors. In five minutes I will ask how many witnesses nine green forks are. By the end, you can work that out, and know what a fork runtime must record. You will see what I did: a receipt contract built, two factory runs measured, two tests that could prove me wrong.

### 02. Hedging: ask twice, keep the first answer

*1:10, starts at 0:45*

In 2013 Jeff Dean and Luiz Barroso published a trick called hedging. If a server is slow to answer, send the same request to a second server and use whichever replies first. In one Google benchmark the slowest requests fell from 1,800 milliseconds to 74, for two percent more requests. It works because the delay is usually the server's fault, not the request's, and two servers rarely stall at the same moment. [click] Agents now hedge too, for correctness: run the task several times and keep a run that passes. But when the flaw is in the task itself, every copy repeats it. Their paper has a second trick for exactly that case. I will hold it until the end.

### 03. Forks find answers. Checks decide which.

*0:50, starts at 1:55*

So does hedging for correctness work? Partly, and the numbers are striking. Sample a coding model two hundred and fifty times and it solves fifty-six percent of SWE-bench Lite, not sixteen. But only with a check. Without one, voting and reward models plateau. A check that says yes to wrong answers caps the gain: when a wrong answer costs more than no answer, Stroebl and colleagues find the best number of tries is often under ten. If you train models, you know this check by another name: the reward.

### 04. Numbers every agent runtime should know

*1:10, starts at 2:45*

Jeff Dean also gave us numbers everyone should know, so here is the list I wish someone had handed me for agent runtimes. Checkpoint a sandbox: eleven milliseconds. Fork one: about a hundred and forty. SnowFlock forked Xen VMs across hosts, in 2009, in under a second. Through a public API: seconds. One work order in my Airflow Factory: forty-three minutes and ten dollars. One frontier model: fifty-one million sandboxes across its training and evaluation. Every row has a source, except the one that matters most: how correlated two forks' verdicts are. That row decides what every other row is worth. My claim: the runtime sees what forks share, so it is where that blank row gets filled.

### 05. Where 43 minutes went

*0:45, starts at 3:55*

That forty-three-minute row is Airflow Factory; let me open it up. I spent two years on self-driving cars at Mobileye, where the hard part was the rare case. My analogy: a software factory is self-driving software, and the hard part is the same. Sandbox setup: twenty seconds, under one percent. A hundred times faster, and this run gets eight tenths of a percent faster. The minutes are in the agents and the checks. So is the risk.

### 06. Blocker. One more repair. Approve.

*1:35, starts at 4:40*

So here is what the agents and the checks actually did. A four-thread race test failed, and the loop sent a repair agent. It had no shell, and it rewrote code outside the plan. Review one: blocker, untested and unverified. The tests were locked, so repair two restructured the code and argued it was covered. Review two downgraded untested to minor, and approved. One model did all four steps. A committee of one. All 1,972 tests passed after each repair, but the new code had no test of its own. Both repairs said they had not run the tests. The gate approved. [click] Now suppose the loop had forked that repair nine times, and all nine came back green. How many witnesses is that? Pick a number; on Teams, type it in the chat. [wait seven seconds, silently; then read one or two numbers aloud for the recording] Keep your number; we will check it when we count.

### 07. How a biophysicist ended up forking sandboxes

*1:05, starts at 6:15*

I have met that question before; it is how a biophysicist ended up forking sandboxes. In my PhD, simulating protein filament networks: which links make parts move together? Then my co-authors and I met it in genomics: a new cell type, or the same patient again? And in Bitcoin: a decentralized network, or sixty-four agents? In agent factories: nine green forks, or one parent? And in RL training, the field's meeting, not mine: which rollouts shared a start? Four of these five fields are mine, and I have published in each. Physics and biology are vocabulary here, not evidence about forks. I keep changing fields; the question keeps following me.

### 08. One factory, seven places the runtime bit

*0:45, starts at 7:20*

The fourth meeting is the one I have logs for, so here it is in systems terms: one factory, seven places the runtime bit, in the order I take them. Every evidence slide carries a tag, analogy included. Scope, said once: two Airflow Factory runs, in Docker Sandboxes through Airflow's sandbox toolset, with models served through Databricks. Two observations come from my own sandbox platform. My harness answered the gates. Leases off. Nothing forked.

### 09. A factory needs a wall, a fork and a count

*0:55, starts at 8:05*

Those seven surfaces reduce to three things the runtime owes the factory: a wall, a fork and a count. The order of the talk: wall, fork, count, and two tests that could prove me wrong. I claim a built receipt contract, two measured runs, and two hypotheses I will show you how to reject. I do not claim an estimator, a speedup, a ranking, or a factory that forks today. Nor that physics or biology is evidence about forks. Forks multiply executions, not evidence. The runtime sees what forks share.

### 10. Allowlists name hosts; the web redirects

*0:50, starts at 9:00*

Part one, the wall: surface one is networking, and the work order itself was a network bug, seen on my own sandbox platform that morning. The allowlist named astral dot sh, which redirects to a host not on the list; the fallback, GitHub's asset host, was not on it either. Curl said 403, and uv never installed. The list lived in five places, and they had drifted: four copies too many. The fix admits every release asset on GitHub. Fetch by digest, through a caching proxy.

### 11. Keys stay outside; a fork copies the inside

*0:50, starts at 9:50*

That was the network half of surface one; the credential half is about where the keys live. The GitHub token stays with the orchestrator. The cell has deny-by-default egress, and a gateway injects the model credential. But the cell still holds a placeholder, a bearer string in guest memory, and a fork copies it bit for bit. Proposed: key each request on identity the host assigns, and let restore bump a generation that voids the parent's lease. Copy the machine, not the keys.

### 12. Filesystem state: what a snapshot shares

*0:45, starts at 10:40*

Surface two is filesystem state, and the first thing to say is that a snapshot captures a boundary, not the universe. So each kind of state gets its own policy. Build outputs are pinned by digest; OBuilder snapshots every step. The workspace disk is copy-on-write, and RL platforms already chain those snapshots: DeepSeek's DSec does. Randomness and external services come later. Memory is the part a filesystem cannot share; hold that for the fork.

### 13. Locking the tests was not enough

*0:55, starts at 11:25*

Surface three is build and test, and here the wall was a write-protected tests directory. The agent never tried: fifteen edits, all allowed; the hook never fired. It did not matter. Repairs were not scope-checked, and one edited code outside the plan. Biology, as an analogy, calls that an off-target edit. Biologists label off-target risk before they cut; my co-authors and I built a tool for it. A scope check is that label for code. The fixes are policy, not runtime. A locked directory is not a scope.

### 14. Reward hacking is the RL name for it

*0:55, starts at 12:20*

This is not my harness being unlucky: reinforcement learning has a name for it, reward hacking. METR saw o3 reward-hack in thirty percent of RE-Bench runs and under one percent of HCAST; their leading guess is the visible scorer. ImpossibleBench: read-only tests stop test edits, not special-casing. Kimi K3 hides some verifiers. And on its kernel tasks, the hacking detector penalises input caching. I work at a build-acceleration company. I felt seen. Whether a cache is engineering or cheating depends on what the grader measures. Run, evaluate, promote: three permissions.

### 15. Teardown must not destroy the experiment

*0:55, starts at 13:15*

Surface four, recovery: a second work order that same day went well, and then badly. Tests and review passed. Then delivery was refused three times, for a stray file outside the reviewed commits: my own harness's review archive. The gate was protecting the repository from me. Then teardown destroyed the cell, and the approved candidate with it: twenty-six minutes, three dollars forty-three, nothing delivered. The artifact must leave the cell before the cell dies. DeepSeek's DSec keeps the sandbox when training is preempted, and replays its log to resume. For a long human wait: snapshot, destroy, restore.

### 16. A green check is not proof the check ran

*0:55, starts at 14:10*

Surface five, observability, and here I have three receipts, all mine, all wrong. A sandbox eval CI job passed in three seconds: every real step skipped. My fastest CI job ever, because it did nothing. My approvals file says mode human; my harness answered. My sandbox CLI mixed status into standard output. So every check needs a receipt the child cannot write; this room calls it provenance. RL learned this too: reward the final state, not the self-report. Both repairs confessed they never ran the tests. The harness ran them anyway.

### 17. What the run pins, and what it cannot

*0:55, starts at 15:05*

Surface six, reproducibility: if a receipt is right, can anyone rerun it? The record pins the commit, the lockfile and the digests. Not the hosted model, external hosts, the clock, or my adapter's source. The target is replay: log every model response, fetch and clock read, and re-execute the rest. DeepSeek's sandbox logs every command for replay. Genomics set this bar in the ENCODE pipelines I worked on; the off-target tool from surface three ships as a Docker image for the same reason. You can audit this run. You cannot rerun it.

### 18. Parallel-safe steps, and nothing to fork them

*0:45, starts at 16:00*

Last on the wall, surface seven, fast cloning: the executor actually asked for a fork that day. No provider offered one, so it ran in series and wrote down why: serial fallback, missing fork. A fork would have saved three minutes of forty-three. Amdahl again. We fork to buy alternatives from expensive state, not speed. Seven surfaces, one rule: whatever you must trust lives outside the cell. Now let us copy the cell.

### 19. The shape of an agent sandbox, drawn in 2009

*0:55, starts at 16:45*

Part two: the fork. It starts with a picture this building will recognise. SnowFlock, EuroSys 2009, forked Xen machines, and Xen came from this lab. Pattern (a) is sandboxing: fork, give the child the untrusted code, and the parent waits. That is an agent sandbox, drawn seventeen years ago. Pattern (b) is parallel work: the fork ID picks each child's slice. Now fork an agent's repair nine times. Same state, same tests. Nine children, one slice. The mechanism is old. The caller is new: a program that searches.

### 20. Fork is old, and much of it was built on Xen

*1:00, starts at 17:40*

SnowFlock was one point on a line that started in this building in 2003. Xen; then live migration, sixty milliseconds of downtime. Potemkin cloned honeypots, SnowFlock forked across hosts, Catalyzer forked a gVisor sandbox in under a millisecond, best case, and MITOSIS forked remotely over RDMA. By fork I mean the whole machine, not the POSIX call Baumann and colleagues asked us to retire. The shaded band is this year, and one row is a training run. Every row is latency or safety. None counts what siblings share. That is the survey behind the blank row.

### 21. Training runs are sandbox factories

*1:05, starts at 18:40*

So who calls fork at the largest scale today? Not a software factory: a training run. Kimi K3 created fifty-one million sandboxes across training and evaluation. It pauses a sandbox while the model thinks, up to ninety-eight percent of its life. It forks one, in their words, for reward judging without side effects. It snapshots for recovery. And its trainer stops waiting once a fraction lambda of trajectories finish, to mitigate the long-tail latency. That is Dean's good enough, with a pause button. DeepSeek runs hundreds of thousands per cluster. A sandbox is an environment; a fork is a reset; a verifier is a reward.

### 22. Reset changes the learning problem

*0:45, starts at 19:45*

Once a fork is a reset, it also changes what the learner gets to see. Start at the task start and you sample one distribution; restore from a checkpoint and you sample another. Go-Explore showed that returning, then exploring, makes exploration productive. So record where each checkpoint came from and why it was chosen, and evaluate on the task you care about. A restore point is a choice of training data.

### 23. Fork copies memory, secrets and identity

*0:55, starts at 20:30*

Trainer or factory, the child inherits everything in memory, including what it should not. Random state: siblings share random streams, and for userspace there is no generic solution. Tokens: eight forks holding a token are eight live tokens, so secrets stay outside. The clock resumes at snapshot time. Clones share one IP and MAC. And nobody clones an open TCP connection. All five belong in the fork contract. An analogy, not evidence: systems people named a remote fork MITOSIS. Biologists would add that daughter cells inherit the parent's mistakes too.

### 24. What each kind of fork copies

*0:55, starts at 21:25*

So what does each kind of fork copy, and where does the bill land? Children share until they write. Kimi reports that copy-on-write memory, with page-cache tricks, lets it overcommit memory up to six and a half times. A worktree keeps files. CRIU keeps processes, but a connection survives in one copy at most. A microVM pays for the pages each child touches. A restore that returns OK is not fidelity. An analogy from physics: trajectories that share a past and split at the first write. Cheap at fork; you pay at divergence.

### 25. Hold effects until an authority releases them

*0:55, starts at 22:20*

Memory we can copy or throw away; an email already sent is another matter. Speculator, external synchrony and Remus all held output until it was safe. This year Zheng and colleagues state it in Lean: nothing undoes a request already sent. DeepSeek replays logged results, so a non-idempotent command never runs twice. Kimi forks a sandbox to judge reward for exactly this reason: no side effects. In my factory, children hold no publishing credential; the orchestrator delivers once, after the gate. The model API is the one unheld channel. Output commit, made structural.

### 26. When fork pays, and where it loses

*1:10, starts at 23:15*

Held effects make a fork safe; now, when does it pay? Fork trades N preparations for one capture, plus a restore and a divergence per child. So it loses at one child, on files-only state with a good build cache, and against a minimal image that boots faster, Jitsu from this room, LightVM from NEC Labs. If your build cache is good, fork loses. My day job is fast builds, so I am contractually obliged to tell you that. The API timings are in the end matter; they are different operations, not a ranking. With teardown, a slot on my platform averaged 11.3 seconds, and until the snapshot is shown to hold memory, that is restore fan-out.

### 27. Isolation has two axes: kernel and authority

*0:55, starts at 24:25*

Wherever the child starts, it needs a wall with two axes, and this building built both. Kernel surface: a container shares one kernel, gVisor moves it to user space, a microVM stands on a hypervisor. Authority: a process can name whatever its user can; under Capsicum or CHERI, only what it is handed. Share a build cache within one trust domain; never share scratch. Kimi saw kernel panics in early container runtimes; Firecracker says disable SMT and same-page merging. We call it a swarm. The operating system calls it roommates.

### 28. The interface the runtime owes the factory

*0:55, starts at 25:20*

Put the wall, the fork and the held effects together and you get the interface the runtime owes the factory. Six calls, with honest status. Checkpoint: my platform has named snapshots, memory unverified. Fork takes a lease, an egress policy and a seed policy, copy or reseed; hold on to that knob. Evaluate outside the child. Select one candidate on a fresh test. Reduce receipts to an estimate, or abstain: the merge is built, abstention proposed. Promote once: the hash-bound gate is built, the epoch fence proposed. Choosing is not pooling.

### 29. Machines fork; authority stays outside

*1:00, starts at 26:15*

Behind those six calls sits an architecture, and here it is with honest labels. Solid boxes are built and ran: the scheduler with its journal and run lock, the work cells, and a gate bound to the artifact's hash. [click] Dashed gold is not exercised: the lease broker is built, the outside evaluator only designed. Every architecture diagram should have a box labelled missing. [click] Mine is the fork store. I wrote the fork contract before I had the fork. Condition eight is the teardown lesson. Condition five is where the rest of this talk goes.

### 30. Promotion is small enough to model-check

*0:45, starts at 27:15*

One box must never race, the promotion gate, and it is small enough to model-check. Evidence names only the frozen candidate, approval needs that evidence, and publication needs all three in the current epoch. Six invariants, zero model-checker runs. I would rather you heard that from me. Even the hedging paper did not hedge writes: consistent updates go to quorum protocols like Paxos. A child's output cannot be model-checked. It must be counted.

### 31. The second review was not a second witness

*1:00, starts at 28:00*

Part three: the count, heading for the number you gave me. Repair two was written against review one's verdict and graded by the same model. A reused holdout stops being a holdout; Dwork named that. Two reviews by one model were, at best, one look. And your nine imagined forks? Choosing among nine patches needs a fresh test. Confirming one patch nine times is capped by what the runs share. Biologists are taught not to confuse technical replicates with independent experiments; our 2021 paper reported both. Our factories confuse them by default. Nine forks of one parent are technical replicates.

### 32. A reused grader becomes a training set

*0:45, starts at 29:00*

Machine learning has a name for a grader you keep going back to: a training set. Even a protected evaluator teaches search to overfit its feedback. So freeze the candidate and validate once. RL labs do this: Kimi K3 pairs public diagnostic verifiers with hidden held-out ones, and caps verbosity so longer answers cannot win. Our repair two argued past review one. Same failure, grader or reward model. Feedback you optimise against stops being evidence.

### 33. One formula, three fields

*0:55, starts at 29:45*

Here is a formula this room knows, in three costumes. Dean: each server slow one time in a hundred, a hundred-way fan-out, sixty-three percent of requests slow. Dorfman, 1943: a pool is clean only if every swab is. Hold that year. In 2020 my co-authors and I modelled putting many swabs in one tube: Poolkeh covered nine million people with under three hundred thousand tests. Now I put one machine in many sandboxes. Say our race loses one run in ten: twenty-nine greens before a miss drops under five percent. All three assume independent draws.

### 34. More forks are not more witnesses

*1:45, starts at 30:40*

Here is what happens to all three when the draws are not independent. Give N runs a common correlation rho, and the variance of their average has a floor at rho sigma squared. In witnesses: a hundred forks at point one are nine; at point five, two; at one, a hundred forks are one witness. And your nine green repairs? [hold up nine photocopies of one page, beside the screen, in camera] Nine sheets, one page: at rho of one, one witness. At rho of one half, still under two. Four hundred executions of a hundred tests are a hundred evidence IDs. And rho is real: on one leaderboard, two wrong models agree sixty percent of the time. That is bias, not variance. Reading rho as coupling is my interpretation. Systems people: where have you seen N over one plus N minus one times a fraction? [wait seven seconds, silently; repeat any answer aloud for the recording] [click] Statisticians call this Kish's design effect. Systems people call it Amdahl's law: rho is the serial fraction of your evidence. Amdahl sends his regards. Again. [pause] Forks multiply executions, not evidence.

### 35. The runtime holds some of the cluster labels

*0:55, starts at 32:25*

The formula is sixty years old; what it needs, and rarely gets, is cluster labels. The runtime holds some that nobody else does: parent, seed, test, fixture, and, through the egress gateway, the model. It cannot label a shared model's blind spots. My co-authors and I had to infer clusters from outside. A decentralized network, or sixty-four agents? A new cell type, or the same patient? Cancer cells cluster by patient; forks cluster by parent. Others must infer the clusters. A fork runtime can record its own.

### 36. Fork is also how you run the control

*0:45, starts at 33:20*

Correlation is not always the enemy: when you compare two candidates, you want it. Give A and B the same draw and the covariance term cancels the nuisance: common random numbers. To corroborate, vary the draw. A fork decides which you get, by copying the seed or reseeding, so the seed policy belongs in the fork API. Test two is built this way: only ancestry differs. Share randomness to compare; vary it to corroborate.

### 37. When does a swarm gel?

*0:50, starts at 34:05*

Seeds are a coupling we choose; communication between forks is one we often do not. A swarm has three graphs: ancestry, evidence flow and composition. Ancestry is a tree. Evidence flow is not: its edges can join separate lineages into one cluster, the way cross-links join polymer chains. Stockmayer asked when that makes one gel. 1943 again. Enough shared context, and a swarm becomes one witness. That is an analogy; the agent threshold must be derived.

### 38. Two green patches can fail together

*0:45, starts at 34:55*

The composition graph hides the nastiest case: two patches that are green alone and break together. Gamma measures that non-additivity. Eight candidates give twenty-eight pair tests and two hundred and fifty-six subsets, and higher-order effects survive pairwise screening. Genetics calls strongly negative gamma synthetic lethality; my co-authors and I screened the genome for it. Each knockout survivable, together lethal. Each patch green, together red. Rebuild and evaluate the composition you ship: condition seven.

### 39. Every worker returns a receipt, not a score

*1:00, starts at 35:40*

So what should a worker hand back? A receipt, not a score: estimate, information, sample size, evidence IDs, lineage and metadata. Built: summaries merge in any tree order, and a duplicate evidence ID stops the merge. Proposed: one execution per evidence ID, and abstention when dependence is unknown. A hedged request is a speculative duplicate, and DSec replays cached results rather than re-running them. Count that evidence once. Yes, the repository is called boltzmann-mapreduce. Physicists never really leave. The estimator is Cochran's. The contract is what was missing.

### 40. A sandbox bounds actions, not claims

*0:55, starts at 36:40*

A receipt can lie too, and isolation will not stop it. Two synthetic checks from the paper. Left, honest shards of unequal size: information pooling lands far closer to the full-data estimate than equal averaging, over eight seeds. Right, one worker forges its precision fifty-fold. One confident liar moves the answer from about five to seventeen. A heuristic brings it back, but that is no Byzantine guarantee. This is reward hacking, aimed at the reducer. Precision is an input the child should not control.

### 41. Test 1: does restore beat a warm cache?

*1:00, starts at 37:35*

Part four: the test. Everything so far is two runs and synthetic checks, so here are two tests that could prove me wrong, written before any run. Test one: cost. Gate zero: a random value in RAM, snapshot, restore three children. If it dies, I report restore fan-out, not fork. Fidelity: restored and direct outputs must match. A cached template against a restore, twenty interleaved reps per size. Restore wins only if the whole interval clears ten seconds at every size. A result where the build cache wins is a good result for this room.

### 42. Why I expect siblings to fail together

*0:40, starts at 38:35*

Before test two, let me declare why I expect siblings to be coupled: I have watched networks do it. My co-authors and I simulated branched actomyosin networks. High Arp2/3: they stall. Low: they contract. In between, loosely connected clusters may collapse suddenly, in avalanches; we noted they are reminiscent of the cytoquakes seen in cells. The physicists here will hold me to that analogy tag.

### 43. Test 2: do siblings fail together?

*1:00, starts at 39:15*

So test two asks it directly: do siblings from one snapshot fail together more than strangers do? Twelve families of three siblings, each paired with three strangers: same slot, same host. Technical replicates against independent experiments. The statistic is the sibling excess correlation. Above point zero five and significant: supported. Confidently below: rejected. Why point zero five? It takes nine siblings down to six point four witnesses. And the nine imagined repairs: re-sample repair one nine times. I predict at least five repeat the out-of-plan edit. When it runs, it fills the blank row.

### 44. What two tests cannot separate

*0:40, starts at 40:15*

Suppose both tests go my way: a win would still not tell us why. A fast fork with a worse search policy can still lose. A communicating system may win only because it spends more model calls. So each row varies one thing, at an equal full budget. Recall Stroebl: how many tries you pay for is part of the result.

### 45. The same work order, run as it should be

*0:55, starts at 40:55*

Put the whole talk together: the same work order, run the way the runtime should run it. Fork after the plan: three children, each with its own lease. Why three? Stroebl again: when a wrong answer costs more than none, often under ten tries. The out-of-plan edit is denied. Another model family scores hidden tests once, as K3 hides its verifiers. The reducer clusters by lineage, or abstains. The artifact leaves before teardown. Search can race. Promotion must not. This is a design, not a run.

### 46. Open problems where this room is ahead of me

*0:40, starts at 41:50*

Building it hits problems where I think this room is ahead of me. Six are on the slide. I would like help with the first two. One: estimate dependence from lineage and evidence edges, without running everything twice. Two: leases that fork. A child's capability should be re-minted on restore, revocable, and never ambient. The other four are there for questions.

### 47. The hedging paper already had the answer

*0:50, starts at 42:30*

Just one more thing. At the start I promised the hedging paper's second trick, for when the fault is in the request. Their worry is a request that exercises an untested code path, crashing thousands of servers at once. The cure is not more replicas. It is a canary: one or two leaves first. My run's new code had no test. Nine green forks would share that gap. So: a canary for correlation.

### 48. Contributions

*1:20, starts at 43:20*

Let me close where I began, with Dean's hedged request. Hedging works when failures are independent; the runtime's job is to know when they are not. Remember the blank row, how correlated two forks' verdicts are: it stays blank until test two runs. In 2009 the parent's last line was wait. Ours has to be count: reduce the receipts by lineage, or abstain. [pause; let the room read the contributions] In physics, genomics and Bitcoin, my co-authors and I had to infer the clusters; a fork runtime can record them. Forks multiply executions, not evidence. [pause] Xen came from this lab, so bringing a question about forks here has been a privilege. I would like to come back with that row filled in. [Stop. Contributions slide stays up through questions. No thank-you.]

## End matter (untimed)

### E1. Fork lineage, in full

Detail for slide 20.

### E2. Fork cost model and API timings

Detail for slide 26: the full cost model and the three API paths behind it.

### E3. The fork contract, in full

Detail for slide 29.

### E4. Pre-registered decision rules

Detail for slides 41 and 43; the protocol is PREREGISTRATION.md, tags prereg-v1 to prereg-v3.

### E5. Research record: biophysics

PhD work at the University of Houston and Rice: graph theory of actomyosin network shape (PRE 2020, linker valency), Arp2/3 branching and avalanches (PNAS 2020, JPCB 2021), protein folding and calcium binding. Used on slide 7 (the journey) and slide 42, the declared prior for Test 2. It is the motivation for Test 2, not evidence for it. Team results: my co-authors and I.

### E6. Research record: genomics

Genome architecture, bioinformatics and cancer genomics at Baylor, NRGene, HIT and Harvard. Where they appear: OffRisk on slide 13 (the off-target analogy); the 2021 CRISPR screen on slides 31, 38 and 43 (replicates, synthetic lethality); the per-patient tumour clustering (iScience) on slides 7 and 35 (cluster labels). The ENCODE pipelines, which set the replay bar on slide 17, are on the next page. Team results: my co-authors and I.

### E7. Research record: preprints, systems and talks

Preprints, systems work and talks. Where they appear: Poolkeh on slide 33 (a model, not a deployment); arXiv:2607.09689 on slides 39 and 40 (receipts, forged precision); Bitcoin on slides 7 and 35 (team result); the ENCODE pipelines on slides 7 and 17. The three-body e-print is on an AI-assisted server and is not peer reviewed; say so if asked.

### E8. References: systems

Systems references. Every figure on a story slide is traceable to these, to the slide's own source line, or to a named run file.

### E9. References: evidence and evaluation

Evidence and evaluation references.

### E10. References: own work and documentation

The speaker's own and co-authored work cited on story slides, the documentation behind slides 11, 12, 23, 24 and 27, and Go-Explore for slide 22.
