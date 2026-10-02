# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from `talk.tex` by `tools/presenter_guide.py`. 50 main slides, 10 end-matter pages. Planned talk: **44:35**, 4432 spoken words, 99 wpm average, peak 110 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:45 | 0:00-0:45 | 58 | 77 |
| 2 | Hedged requests reduce tail latency | 1:10 | 0:45-1:55 | 118 | 101 |
| 3 | Repeated sampling needs an automatic check | 0:45 | 1:55-2:40 | 82 | 109 |
| 4 | Latency and scale of agent runtimes | 1:10 | 2:40-3:50 | 119 | 102 |
| 5 | Where 43 minutes went | 0:50 | 3:50-4:40 | 82 | 98 |
| 6 | A review gate approved untested code | 1:35 | 4:40-6:15 | 157 | 99 |
| 7 | One question across six fields | 1:05 | 6:15-7:20 | 113 | 104 |
| 8 | Seven runtime demands in one pipeline | 0:45 | 7:20-8:05 | 71 | 95 |
| 9 | Intelligence as choice and action | 0:45 | 8:05-8:50 | 76 | 101 |
| 10 | The loop needs a wall, a fork and a count | 0:50 | 8:50-9:40 | 83 | 100 |
| 11 | Allowlists fail when hosts redirect | 0:40 | 9:40-10:20 | 71 | 106 |
| 12 | Forks copy cell memory, so keys stay outside | 0:45 | 10:20-11:05 | 75 | 100 |
| 13 | Filesystem state shared by a snapshot | 0:45 | 11:05-11:50 | 69 | 92 |
| 14 | Write-protected tests did not limit edits | 0:55 | 11:50-12:45 | 92 | 100 |
| 15 | Reinforcement learning calls it reward hacking | 0:45 | 12:45-13:30 | 74 | 99 |
| 16 | Teardown destroyed the approved patch | 0:45 | 13:30-14:15 | 75 | 100 |
| 17 | Three of our check records were wrong | 0:50 | 14:15-15:05 | 78 | 94 |
| 18 | What the run pins, and what it cannot | 0:45 | 15:05-15:50 | 69 | 92 |
| 19 | The parallel-safe steps had no fork available | 0:35 | 15:50-16:25 | 53 | 91 |
| 20 | Six findings from two experiments | 0:45 | 16:25-17:10 | 66 | 88 |
| 21 | SnowFlock described agent sandboxing in 2009 | 0:55 | 17:10-18:05 | 88 | 96 |
| 22 | Fork systems since 2003, many built on Xen | 0:55 | 18:05-19:00 | 89 | 97 |
| 23 | Training runs create sandboxes at large scale | 1:00 | 19:00-20:00 | 108 | 108 |
| 24 | Reset changes the learning problem | 0:45 | 20:00-20:45 | 67 | 89 |
| 25 | Fork copies memory, secrets and identity | 0:55 | 20:45-21:40 | 78 | 85 |
| 26 | What each kind of fork copies | 0:55 | 21:40-22:35 | 86 | 94 |
| 27 | Hold effects until an authority releases them | 0:55 | 22:35-23:30 | 88 | 96 |
| 28 | When fork pays, and where it loses | 1:10 | 23:30-24:40 | 113 | 97 |
| 29 | Isolation has two axes, kernel and authority | 0:55 | 24:40-25:35 | 86 | 94 |
| 30 | The interface the runtime owes the loop | 0:55 | 25:35-26:30 | 86 | 94 |
| 31 | Work cells fork and the gate holds authority | 0:55 | 26:30-27:25 | 89 | 97 |
| 32 | Promotion is small enough to model-check | 0:45 | 27:25-28:10 | 72 | 96 |
| 33 | The second review was not independent | 1:05 | 28:10-29:15 | 113 | 104 |
| 34 | A reused grader becomes a training set | 0:45 | 29:15-30:00 | 82 | 109 |
| 35 | One formula, three fields | 0:55 | 30:00-30:55 | 97 | 106 |
| 36 | Extra forks add few witnesses | 1:50 | 30:55-32:45 | 199 | 109 |
| 37 | The runtime holds some of the cluster labels | 0:50 | 32:45-33:35 | 86 | 103 |
| 38 | A fork can supply the control run | 0:45 | 33:35-34:20 | 71 | 95 |
| 39 | When a swarm gels | 0:50 | 34:20-35:10 | 78 | 94 |
| 40 | Two passing patches can fail together | 0:45 | 35:10-35:55 | 81 | 108 |
| 41 | Workers return a receipt of evidence and origin | 0:55 | 35:55-36:50 | 98 | 107 |
| 42 | A sandbox cannot verify a claim | 0:55 | 36:50-37:45 | 98 | 107 |
| 43 | Test 1: restore versus a warm cache | 1:00 | 37:45-38:45 | 108 | 108 |
| 44 | Why siblings may fail together | 0:35 | 38:45-39:20 | 55 | 94 |
| 45 | Test 2: sibling failure coupling | 1:05 | 39:20-40:25 | 107 | 99 |
| 46 | What two tests cannot separate | 0:40 | 40:25-41:05 | 65 | 98 |
| 47 | The same work order, run as designed | 0:50 | 41:05-41:55 | 92 | 110 |
| 48 | Six open problems for the prototype | 0:35 | 41:55-42:30 | 58 | 99 |
| 49 | Canary requests from the hedging paper | 0:50 | 42:30-43:20 | 84 | 101 |
| 50 | Contributions | 1:15 | 43:20-44:35 | 129 | 103 |

## Script

### 01. Forkable Sandboxes

*0:45, starts at 0:00*

A fork is a new sandbox started from a snapshot of a running one. In five minutes we ask how many independent observations nine passing forks provide. By the end we will be able to answer it. We built a receipt contract, ran two experiments with a self-evolving loop, and defined two tests that could falsify our claim.

### 02. Hedged requests reduce tail latency

*1:10, starts at 0:45*

In 2013 Jeff Dean and Luiz Barroso published a technique called hedging. The client sends a request to one server, and if no answer arrives within 10 milliseconds it sends a copy to a second server and uses the first answer. In one benchmark, the slowest requests fell from 1,800 milliseconds to 74, for two percent more requests. The delay usually originates in the server rather than in the request. Two servers rarely stall together. [click] Agents now hedge for correctness by running the task several times and keeping a run that passes. When the flaw is in the task itself, every copy repeats it. Their paper describes a second technique for that case, presented at the end.

### 03. Repeated sampling needs an automatic check

*0:45, starts at 1:55*

Hedging for correctness works in part. Brown and colleagues sampled a coding model 250 times and it solved 56 percent of SWE-bench Lite, against 16 percent for one sample. This gain requires an automatic check. Without a check, voting and reward models stop improving. A check that accepts wrong answers caps the gain. When wrong answers cost more than none, Stroebl and colleagues find the best number of tries is often under ten. In model training, this check is called the reward.

### 04. Latency and scale of agent runtimes

*1:10, starts at 2:40*

Jeff Dean also gave us numbers everyone should know. This table gives them for agent runtimes. Checkpointing a sandbox, saving its state, takes eleven milliseconds. Forking one takes about a hundred and forty milliseconds. SnowFlock forked Xen VMs across hosts in 2009 in under a second. Through a public API it takes seconds. One work order in our experiments takes forty-three minutes and costs ten dollars. One frontier model used fifty-one million sandboxes across training and evaluation. The row without a source is how correlated two forks' verdicts are. That value decides how much independent evidence the other rows buy. Our claim is that the runtime sees what forks share, so it is where this value can be measured.

### 05. Where 43 minutes went

*0:50, starts at 3:50*

The forty-three-minute row is one work order of a self-evolving loop, an agent system that proposes, tests and merges changes to its own code. The analogy comes from two years on self-driving cars at Mobileye, where the rare case was hardest. The loop is self-driving software with the same hard part. Setup takes twenty seconds, under one percent. A hundredfold faster setup would make this run 0.8 percent faster. The minutes are in the agents and the checks. So is the risk.

### 06. A review gate approved untested code

*1:35, starts at 4:40*

Here is what the agents and the checks did. A race test on four threads failed, and the loop sent a repair agent. It had no shell, and it rewrote code outside the plan. Review one blocked the change as untested and unverified. The tests were locked, so repair two restructured the code and argued it was covered. Review two downgraded untested to minor and approved. One model did all four steps. All 1,972 tests passed after each repair. The new code had no test of its own. Both repairs said they had not run the tests. The gate approved. [click] Suppose the loop had forked repair one nine times and all nine passed. We ask how many independent observations that provides. Pick a number and type it in the Teams chat. [wait seven seconds, silently; then read one or two numbers aloud for the recording] Keep your number, and we will check it when we count.

### 07. One question across six fields

*1:05, starts at 6:15*

We have met that question before, in six fields. It explains why a biological physicist forks sandboxes. In a PhD on protein filament networks, it was which links make parts move together. In genomics with co-authors, it was a new cell type or the same patient again. In Bitcoin, it was a decentralized network or sixty-four agents. At Mobileye, on self-driving perception, it was a million frames or one rare case. In agent loops, it is nine green forks or one parent. In reinforcement learning, it is which rollouts, or practice runs, shared a start. Five of these six fields are ours. Physics and biology give vocabulary here and no evidence about forks.

### 08. Seven runtime demands in one pipeline

*0:45, starts at 7:20*

We have logs for the experiments, and the seven places the runtime mattered. Every evidence slide carries a tag for its kind, analogy included. The scope is two experiments with the loop in Docker Sandboxes through Airflow's sandbox toolset, with models served through Databricks. Two observations come from our own sandbox platform. Our harness answered the gates with no human involved, permission leases were switched off, and no run used forking.

### 09. Intelligence as choice and action

*0:45, starts at 8:05*

We define one word. Intelligence comes from Latin intellegere, joining inter, between, and legere, to choose or to read, meaning choosing between. Since the twenty-ninth of September, US agencies must say Super Intelligence, but we will say intelligence. Our ladder is an analogy from self-driving cars to self-driving computers to self-driving intelligence, an agent in a loop. The loop reads, chooses between forks, acts inside a wall, and checks with a count that decides what counts.

### 10. The loop needs a wall, a fork and a count

*0:50, starts at 8:50*

The loop and the seven places reduce to a wall, a fork and a count, which the runtime owes the loop. Then come two tests that could prove us wrong. We claim a built receipt contract, two measured runs, and two rejectable hypotheses. We do not claim an estimator, a speedup, a ranking, a loop that forks today, or physics and biology as evidence about forks. N forks give N executions, but fewer than N independent observations. The runtime sees what forks share.

### 11. Allowlists fail when hosts redirect

*0:40, starts at 9:40*

Part one, the wall, starts with networking. The work order was a network bug seen on our sandbox platform that morning. The allowlist named astral dot sh, which redirects off the list. Curl got a 403 and uv never installed. The list lived in five drifted places, four copies too many. The fix admits every release asset on GitHub. We propose fetching by digest, the file's hash, through a caching proxy.

### 12. Forks copy cell memory, so keys stay outside

*0:45, starts at 10:20*

The GitHub token stays outside, with the orchestrator. The cell, the agent's sandbox, blocks outbound traffic, called egress, by default. A gateway injects the model credential. The cell still holds a placeholder token in memory, and a fork copies it exactly. We propose keying each request on an identity that the host assigns. Restore increments a generation number, voiding the parent's lease, its timed permission. Credentials must never reside in memory that a fork copies.

### 13. Filesystem state shared by a snapshot

*0:45, starts at 11:05*

Surface two is filesystem state. A snapshot, a saved copy of the sandbox, captures only the state inside that boundary. Each kind of state therefore needs its own policy. Build outputs are pinned by digest, and OBuilder snapshots every step. The workspace disk is copy-on-write, and DeepSeek's DSec already chains such snapshots. Randomness and external services come later. A filesystem snapshot cannot share memory, which the forking section addresses.

### 14. Write-protected tests did not limit edits

*0:55, starts at 11:50*

Surface three is build and test. Here the wall was a write-protected tests directory. The hook never fired, and all fifteen edits were allowed. The protection had no effect. Repairs were not scope-checked, and one edited code outside the plan. In biology, this is an off-target edit. Biologists label that risk before they cut, and we built a tool for it with our co-authors. A scope check serves the same function for code. The proposed scope check and blocker change policy and leave the runtime unchanged. A write-protected directory defines no scope.

### 15. Reinforcement learning calls it reward hacking

*0:45, starts at 12:45*

Others report the same failure. Reinforcement learning calls this behavior reward hacking. METR reports o3 reward-hacked in thirty percent of RE-Bench runs and under one percent of HCAST. Their leading hypothesis is the visible scorer. ImpossibleBench reports read-only tests prevent test edits but not special-casing. Kimi K3 hides some verifiers. On kernel tasks, its hacking detector penalises input caching. Input caching is also core to build acceleration. Running, evaluating and promoting are three permissions.

### 16. Teardown destroyed the approved patch

*0:45, starts at 13:30*

Surface four is recovery. A second work order that day passed tests and review, then failed. Delivery was refused three times because of a stray file, our harness's own review archive. Teardown then destroyed the sandbox and the approved patch. The run took twenty-six minutes, cost three dollars forty-three and delivered nothing. The artifact should leave the sandbox before it is destroyed. During a long human wait, the sandbox should be snapshotted, destroyed and restored.

### 17. Three of our check records were wrong

*0:50, starts at 14:15*

Surface five is observability. Three of our own receipts were wrong. A sandbox evaluation CI job passed in three seconds because every real step was skipped. Our approvals file records mode human, although our harness gave the answer. Our sandbox CLI mixed status into its output. So every check needs a receipt, a record of what ran, that the sandbox cannot write. The literature calls such a record provenance. Kimi K3 grounds reward in the final environment state.

### 18. What the run pins, and what it cannot

*0:45, starts at 15:05*

Surface six is reproducibility. Reproducibility asks whether anyone can rerun the run. The record pins the commit, the lockfile and the digests. It does not pin the hosted model, external hosts, the clock, or our adapter's source. We propose replay, which logs every model response, fetch and clock read and re-executes the rest. Genomics set this standard in the ENCODE pipelines. This run can be audited but not rerun.

### 19. The parallel-safe steps had no fork available

*0:35, starts at 15:50*

The seventh and last surface is fast cloning. The executor requested a fork in this run. No provider offered one, so the executor ran in series and recorded the reason as serial fallback, missing fork. A fork would have saved three minutes of forty-three. We propose forking to obtain alternatives from expensive state.

### 20. Six findings from two experiments

*0:45, starts at 16:25*

The runs gave six findings. Sandbox setup took under one percent of work order time. A locked test folder did not limit the repair. Passing checks can test nothing. One model in all four steps gives one review. Teardown can destroy an approved result. No provider offered a fork. Across the seven surfaces, trusted components should run outside the sandbox. Next we consider copying the sandbox.

### 21. SnowFlock described agent sandboxing in 2009

*0:55, starts at 17:10*

Part two covers the fork. SnowFlock (EuroSys 2009) forked Xen virtual machines, and Xen was built in this laboratory. Pattern (a) is sandboxing, where the parent forks a child to run untrusted code and waits. This is an agent sandbox, described seventeen years ago. Pattern (b) is parallel work, and the fork ID selects each child's slice. Forking an agent's repair nine times gives nine children. They share the same state and tests and one slice. The mechanism is old, and the caller is a program that searches.

### 22. Fork systems since 2003, many built on Xen

*0:55, starts at 18:05*

SnowFlock continued a line begun here in 2003. Xen led to live migration with sixty milliseconds of downtime. Potemkin cloned honeypots. SnowFlock forked across hosts. Catalyzer forked a gVisor sandbox in under one millisecond, best case. MITOSIS forked over remote direct memory access. Fork here means the whole machine, unlike the POSIX call Baumann and colleagues proposed to retire. The shaded band marks this year and one row is a training run. Each system targets speed or safety. None counts what sibling forks share, which is the blank row.

### 23. Training runs create sandboxes at large scale

*1:00, starts at 19:00*

The largest reported use of fork is model training. Kimi K3 created fifty-one million sandboxes for training and evaluation. It pauses a sandbox while the model thinks, up to ninety-eight percent of its life. It forks one, in their words, for reward judging without side effects. It snapshots for recovery. Its trainer stops waiting once a fraction lambda of trajectories, meaning attempts, finishes, to mitigate the long-tail latency. This matches Dean and Barroso's good-enough approach of not waiting for stragglers. DeepSeek-V4 runs hundreds of thousands of sandboxes per cluster. In training, a sandbox serves as the environment, a fork as a reset, and a verifier as the reward.

### 24. Reset changes the learning problem

*0:45, starts at 20:00*

Once a fork is a reset, it changes what the learner sees. Starting at the task start samples one distribution. Restoring from a checkpoint samples another. Ecoffet and colleagues showed that returning to a state before exploring makes exploration productive. We propose recording where each checkpoint came from and why. We also propose evaluating on the intended task distribution. Each restore point selects the learner's training data.

### 25. Fork copies memory, secrets and identity

*0:55, starts at 20:45*

The child inherits all of memory, including what it should not. Siblings share random streams, and above the kernel there is no generic solution. Eight forks holding a token are eight live tokens, so secrets stay outside the VM. The clock resumes at snapshot time. Clones share one IP and MAC address. No one can clone an open TCP connection. All five belong in the fork contract. As an analogy, systems researchers named a remote fork mechanism MITOSIS.

### 26. What each kind of fork copies

*0:55, starts at 21:40*

Each fork type copies different state and costs differently. Children share memory until they write. Kimi reports copy-on-write memory with page-cache optimisations allows up to 6.5 times overcommit. A worktree keeps files. CRIU keeps processes, but a connection survives in one copy at most. A microVM pays for the pages each child touches. A restore that returns OK is not a faithful copy. As an analogy from physics, paths share a past and split at first write. Fork is cheap, and the cost appears at divergence.

### 27. Hold effects until an authority releases them

*0:55, starts at 22:35*

Memory can be copied or discarded, but a sent email cannot. Speculator, external synchrony and Remus all held output until it was safe. Zheng and colleagues stated in Lean that no edit undoes a sent request. DeepSeek replays logged results, so a command unsafe to repeat never runs twice. Kimi forks to judge reward because judging produces no side effects. In the prototype, children hold no publishing credential. The orchestrator delivers once, after the gate. The model API is the one unheld channel. Output commit is structural here.

### 28. When fork pays, and where it loses

*1:10, starts at 23:30*

A safe fork pays when it trades N preparations for one capture, plus a restore and a divergence per child. It loses in three cases. The first is one child. The second is files-only state with a good build cache. The third is a faster-booting minimal image, as in Jitsu from Cambridge and LightVM from NEC Labs. Fork loses when the build cache is good and pays for state that cannot be rebuilt. The end matter lists API timings for different operations with no ranking. With teardown, a slot on the sandbox platform averaged 11.3 seconds. Until the snapshot is shown to hold memory, the platform's fork is restore fan-out from one snapshot.

### 29. Isolation has two axes, kernel and authority

*0:55, starts at 24:40*

The child needs isolation along two axes, and this laboratory built systems for both. A container shares one kernel, gVisor moves it to user space, and a microVM stands on a hypervisor. An ordinary process can name whatever its user can name. Under Capsicum or CHERI, it can use only what it is handed. A build cache may be shared within one trust domain, meaning code trusted equally. Never share scratch. Kimi saw kernel panics in early container runtimes. Firecracker says disable SMT and same-page merging.

### 30. The interface the runtime owes the loop

*0:55, starts at 25:35*

Together, these give the interface the runtime owes the loop. The six calls carry a stated status. Checkpoint uses named snapshots with memory unverified. Fork takes a lease, an egress policy and a seed policy, copy or reseed. Evaluate outside the child. Select one candidate on a fresh test. Reduce combines receipts into an estimate or abstains, with merge built and abstention proposed. Promote runs once, with the hash-bound gate built and the epoch fence, which blocks stale runs, proposed. Select and reduce are separate calls.

### 31. Work cells fork and the gate holds authority

*0:55, starts at 26:30*

The six calls rest on an architecture labelled by status. Solid boxes are the scheduler with its journal and run lock, the work cells, and a gate bound to the artifact's hash, and all of them were built and ran. [click] Dashed gold marks the lease broker, built but unexercised, and the evaluator, only designed. [click] The diagram marks the fork store as missing. We wrote the fork contract before the fork store existed. Condition eight came from our second run. The rest of this talk concerns condition five.

### 32. Promotion is small enough to model-check

*0:45, starts at 27:25*

The promotion gate must never race. It is small enough for a tool to model-check by trying every ordering. Evidence names only the frozen candidate. Approval needs that evidence. Publication needs all three in the current epoch. Six rules must always hold, and no model-checker run exists yet. Dean and Barroso report that consistent updates use quorum protocols such as Paxos. A child's output cannot be model-checked. It must instead be counted.

### 33. The second review was not independent

*1:05, starts at 28:10*

Part three is the count. Nine agent copies say the fix works. Belief depends on how independent they were. Nine strangers giving the same directions are probably right. Nine people reading the same wrong map hold one opinion. Our reviews shared one map. Repair two answered review one's verdict, and the same model graded it. The two reviews give at best one look. Choosing among nine patches needs a fresh test. Best-of-nine cannot beat one minus the chance all nine fail together, so record each fork's pass or fail. Confirming one patch is capped by what the runs share. Biologists call those runs technical replicates. Nine forks of one parent are technical replicates.

### 34. A reused grader becomes a training set

*0:45, starts at 29:15*

Machine learning calls a grader you keep returning to a training set. Even a protected grader can teach the search to overfit its feedback. So we freeze the candidate and validate once. Reinforcement-learning labs do this. Kimi K3 gives feedback from public verifiers and scores with hidden ones. It caps answer length, so longer answers cannot win. Our repair two argued past review one. A grader or a reward model fails the same way. Feedback that is optimised against stops being evidence.

### 35. One formula, three fields

*0:55, starts at 30:00*

One formula appears in three fields. Dean and Barroso report each server is slow one time in a hundred. Fan out to a hundred servers and sixty-three percent of requests are slow. In 1943 Dorfman noted a pool is clean only if every swab is. In 2020 we modelled Poolkeh, pooling many swabs per tube for nine million people with under three hundred thousand tests. Now we run one patch in many sandboxes. Suppose our race breaks one run in ten. It takes twenty-nine greens before a miss drops under five percent. All three assume independent draws.

### 36. Extra forks add few witnesses

*1:50, starts at 30:55*

But forks share starting code, model, prompt and tests. If the mistake comes from something shared, all nine make it. How much they share is one number, the correlation rho. A hundred forks sharing a little, rho point one, give about nine independent witnesses. A lot, point five, gives about two. Identical means one. Take nine green repairs. [hold up nine photocopies of one page, beside the screen, in camera] Nine sheets of one page give one witness. Their average's variance never drops below rho sigma squared. Two different models that both miss a question pick the same wrong answer sixty percent of the time, where chance would give a third. This is not rho but shows rho is nonzero. Nine frontier judges give about two independent votes. Reading rho as coupling and this result as bias is our interpretation. Systems people may recognise N over one plus N minus one times a fraction. [wait seven seconds, silently, repeat any answer aloud for the recording] [click] Statisticians call this Kish's design effect. Systems people call it Amdahl's law, with rho as the serial fraction of your evidence. [pause] N forks give N executions, but fewer than N independent observations.

### 37. The runtime holds some of the cluster labels

*0:50, starts at 32:45*

The formula dates from 1965. It needs cluster labels, meaning records of shared sources, that analysts rarely get. Only the runtime knows which copies share a parent, seed or test. Its egress gateway also sees which model each copy calls. It records this lineage with every result. It cannot see blind spots that different models share. We inferred clusters from outside, in bitcoin and tumours. Malignant cells cluster by patient tumour. Forks cluster by parent. Others must infer the clusters. A fork runtime can record them.

### 38. A fork can supply the control run

*0:45, starts at 33:35*

Positive correlation lowers the variance of the difference between two candidates. Giving A and B the same draw cancels shared noise, a technique called common random numbers. To corroborate, each copy needs a different draw, so a fork copies the seed or reseeds. The seed policy therefore belongs in the fork API. Test two uses this design, so only ancestry differs. Sharing the draw supports comparison and varying it supports corroboration.

### 39. When a swarm gels

*0:50, starts at 34:20*

Seeds couple copies by choice, but exchanged information often couples them unintentionally. A swarm has three graphs, ancestry, evidence flow and composition, and only ancestry (who forked from whom) forms a tree of lineages. Evidence edges can join separate lineages into one cluster, as cross-links join polymer chains. Stockmayer asked in 1943 when such links make one gel. With enough shared context, a swarm becomes one witness. This is an analogy, so the agent threshold must be derived.

### 40. Two passing patches can fail together

*0:45, starts at 35:10*

Composition hides a severe case in which two patches pass alone but fail together. Gamma measures how far the pair differs from the sum of its parts. Eight candidates give twenty-eight pair tests and two hundred and fifty-six subsets. Effects among three or more can pass every pair test. Genetics calls strongly negative gamma synthetic lethality, and we screened the genome for it. Each knockout is survivable alone but lethal together. The shipped composition must be rebuilt and evaluated (condition seven).

### 41. Workers return a receipt of evidence and origin

*0:55, starts at 35:55*

A worker should return a receipt. The receipt contains the result, the evidence it used and its origin. The built part merges summaries in any order and stops when evidence is used twice. We propose that each evidence ID corresponds to one execution. If the runtime cannot determine how much the copies share, it should abstain. A hedged request is a speculative duplicate of an earlier request. DeepSeek's DSec replays cached results instead of re-running them. Such evidence should be counted once. The estimator is Cochran's. The proposed contract specifies how the inputs to that estimator are counted.

### 42. A sandbox cannot verify a claim

*0:55, starts at 36:50*

A receipt can also be false, and isolation cannot prevent it. A copy can claim more certainty than it has. We show two synthetic checks from our preprint. The left panel shows honest shards of unequal size. Information pooling gives a distance of 0.0083 against 0.177 for the equal average. In the right panel, one worker inflates its precision fifty-fold. That worker moves the pooled estimate from about five to seventeen. A heuristic restores it to about five but gives no Byzantine guarantee. The controller should therefore set each child's precision, and children should not report their own.

### 43. Test 1: restore versus a warm cache

*1:00, starts at 37:45*

Part four presents the test, after two runs and synthetic checks. Two tests could refute our claim, and both were written before any run. Test one measures cost, and gate zero snapshots a random RAM value and restores three children. If the value is lost, memory was not restored, so the operation is restore fan-out and not a fork. Fidelity requires matching restored and direct outputs, and a cached template is compared with a restore over twenty alternating runs per size. Restore counts as better only if the whole interval exceeds ten seconds at every size. A result in which the build cache wins is a valid outcome.

### 44. Why siblings may fail together

*0:35, starts at 38:45*

Before test two, we state why siblings are expected to fail together. We simulated branched actomyosin networks and observed this behaviour. At high Arp2/3 levels the networks stall, and at low levels they contract. In between, loose clusters may collapse suddenly, in avalanches. We described the avalanches as an analogy to cytoquakes observed in cells.

### 45. Test 2: sibling failure coupling

*1:05, starts at 39:20*

Test two asks whether siblings sharing a snapshot fail together more than strangers from other snapshots. Twelve families of three siblings each pair with three strangers on the same slot and host. The statistic is delta rho, the extra correlation among siblings. The hypothesis is supported above point zero five and significant, and rejected if delta rho is confidently below it. We chose point zero five because that excess reduces nine siblings to six point four independent witnesses. For the nine imagined repairs, we resample repair one nine times and predict at least five repeats of the out-of-plan edit. When it runs, it fills the blank row.

### 46. What two tests cannot separate

*0:40, starts at 40:25*

Suppose both tests support the hypothesis. A positive result would still not explain its cause. A fast fork with a worse search policy can still lose. Forks that share notes may win only because they spend more model calls. Each row therefore changes one factor at an equal full budget. Stroebl and colleagues report that the number of paid tries is part of the result.

### 47. The same work order, run as designed

*0:50, starts at 41:05*

This design, which has not been run, shows the work order as the system should run it. The system forks after the plan into three children, each with its own lease. Stroebl reports that when a wrong answer costs more than none, the best number of tries is often under ten. The out-of-plan edit is denied. Another model family scores hidden tests once, as K3 hides its verifiers. The reducer groups results by lineage or abstains, and the artifact is exported before teardown. Search may run in parallel, but promotion may not.

### 48. Six open problems for the prototype

*0:35, starts at 41:55*

Building the prototype raises six open problems, and we would like help with the first two. Problem one is to estimate dependence from lineage and evidence edges without running everything twice. Problem two concerns leases that fork. On restore, a child's capability should be newly issued, revocable, and never ambient. The other four problems are available for questions.

### 49. Canary requests from the hedging paper

*0:50, starts at 42:30*

Next is the hedging paper's second technique, for faults in the request. The authors describe a request reaching an untested code path and crashing thousands of servers at once. They propose a canary request sent to one or two leaf servers first. The new code in our first run had no test, so nine passing forks would share that gap. Kohli reports that nine frontier judges who all agreed were still wrong 9.1 percent of the time. We therefore propose a canary for correlation.

### 50. Contributions

*1:15, starts at 43:20*

Hedging works when failures are independent. The runtime must detect when they are not. Recent work counts independent witnesses for models and judges. We know of no such count for forks of one agent. That is the blank row, which stays blank until test two runs. In 2009 the parent ended with a wait call. Ours must count by grouping the receipts by lineage, or abstain. [pause; let them read] In physics, genomics and Bitcoin, we had to infer the clusters. A fork runtime can record them. N forks give N executions, but fewer than N independent observations. [pause] Xen came from this laboratory, and bringing a question about forks here has been a privilege. We plan to report the completed row later. [Stop. Slide stays up through questions.]

## End matter (untimed)

### E1. Fork lineage, in full

Detail for slide 22.

### E2. Fork cost model and API timings

Detail for slide 28: the full cost model and the three API paths behind it.

### E3. The fork contract, in full

Detail for slide 31.

### E4. Pre-registered decision rules

Detail for slides 43 and 45; the protocol is PREREGISTRATION.md, tags prereg-v1 to prereg-v3.

### E5. Research record: biophysics

PhD work at the University of Houston and Rice: graph theory of actomyosin network shape (PRE 2020, linker valency), Arp2/3 branching and avalanches (PNAS 2020, JPCB 2021), protein folding and calcium binding. Used on slide 7 (the journey) and slide 44, the declared prior for Test 2. It is the motivation for Test 2, not evidence for it. Team results: my co-authors and I.

### E6. Research record: genomics

Genome architecture, bioinformatics and cancer genomics at Baylor, NRGene, HIT and Harvard. Where they appear: OffRisk on slide 14 (the off-target analogy); the 2021 CRISPR screen on slides 33, 40 and 45 (replicates, synthetic lethality); the per-patient tumour clustering (iScience) on slides 7 and 37 (cluster labels). The ENCODE pipelines, which set the replay bar on slide 18, are on the next page. Team results: my co-authors and I.

### E7. Research record: preprints, systems and talks

Preprints, systems work and talks. Where they appear: Poolkeh on slide 35 (a model, not a deployment); arXiv:2607.09689 on slides 41 and 42 (receipts, forged precision); Bitcoin on slides 7 and 37 (team result); the ENCODE pipelines on slides 7 and 18. The three-body e-print is on an AI-assisted server and is not peer reviewed; say so if asked.

### E8. References: systems

Systems references. Every figure on a story slide is traceable to these, to the slide's own source line, or to a named run file.

### E9. References: evidence and evaluation

Evidence and evaluation references. The shared-errors papers compare different models, not forks of one agent, and the 2026 arXiv items are preprints.

### E10. References: own work and documentation

The speaker's own and co-authored work cited on story slides, the documentation behind slides 12, 13, 25, 26 and 29, and Go-Explore for slide 24.
