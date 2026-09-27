# Speaker notes — Cambridge SRG · 30 minutes

Talk: **Forkable Sandboxes: The Runtime Layer for AI Software Factories**  
Speaker: **Yossi Eliaz — Incredibuild / islo.dev + HIT**  
Target: **27–28 minutes of content + 2–3 minutes slack**

The talk should feel like a story about **state**:
1. state as something science must reproduce,
2. state as something build systems want to reuse,
3. state as something agents make dangerous,
4. state as something forkable runtimes turn into a controlled search primitive.

Do not narrate every bullet. Each slide has one job.

---

## Slide 1 — Forkable Sandboxes (0:00–1:00)

Open immediately:

> “I want to make one argument today: once software agents stop only writing text and start running code, the missing abstraction is not another model. It is a machine you can fork.”

Then:

> “And the design constraint is: burn the runner, keep the proof, fork the machine — not the trust.”

Do not introduce every employer/title. The title slide already does that.

Transition:

> “Let me start with the architecture most of us accidentally build first.”

---

## Slide 2 — 100 agents. One laptop. What could possibly go wrong? (1:00–3:00)

Point to the left-side agents.

> “We call this a swarm. The operating system calls it roommates.”

Pause for the laugh.

Walk the failure modes quickly:
- shared filesystem,
- shared tests,
- shared credentials,
- shared caches,
- shared stale processes.

Then:

> “The surprising problem is not that the agents communicate. The problem is that they can share state without us knowing which conclusions are still independent.”

Punchline:

> “Parallelism without isolation is correlated chaos.”

Transition:

> “That sounds like an agent problem. I got here from somewhere else.”

---

## Slide 3 — Why I ended up here (3:00–5:00)

Do not give a biography. Tell three lessons.

Science:

> “In computational science, I learned that the experiment is not just the Python script. It is the exact inputs, machine state, versions, and provenance.”

Build systems:

> “In build systems, I learned the opposite economic lesson: recomputing the world is insane. Reuse everything you safely can.”

Agents:

> “Then the developer became a program that edits the machine itself.”

Pause.

> “So the same state I wanted to reuse for speed became the state I needed to isolate for trust.”

That sentence is the personal reason for the whole talk.

Transition:

> “That gives us a much cleaner way to divide the system.”

---

## Slide 4 — Search can be plural. Authority must be singular. (5:00–7:00)

Point left:

> “Search wants abundance. I want cheap failure.”

Point right:

> “Authority wants scarcity. I want one narrow place where the world actually changes.”

Examples:
- 100 candidate patches / 1 merge.
- 10,000 rollouts / 1 checkpoint.
- millions of simulations / 1 real robot hour.

Stage line:

> “A million compiles are search. One merge is authority.”

Do not say “humans must always approve.” The point is singular authority, which can be automated under a trusted controller.

Transition:

> “What machine primitive makes the left-hand side economically real?”

---

## Slide 5 — The primitive is a machine you can fork (7:00–10:00)

Draw the story with your finger:
S0 → forks → run → reduce → promote → burn.

Say:

> “Think Git branch, except the branch contains the filesystem, the processes, the memory, and the execution context.”

Then:

> “The key is that promotion is not another child operation. It is outside the fan-out.”

Mention Firecracker / DeltaBox / Shepherd only as context:

> “There is now strong systems work making checkpoint, rollback, and reversible agent execution first-class. My interest is the contract that sits above those mechanisms.”

Avoid latency numbers unless asked.

Transition:

> “But ‘fork the machine’ is dangerously underspecified.”

---

## Slide 6 — What actually has to fork? (10:00–13:00)

Four buckets. One sentence each.

State:
> “The child needs enough of the old world to resume exactly.”

Speed:
> “CoW means I pay mainly for divergence.”

Authority:
> “Credentials and network power are not ordinary memory bytes.”

Evidence:
> “The receipt has to outlive the disposable machine that produced it.”

Important line:

> “A filesystem snapshot without credential semantics is not a sandbox contract.”

Optional lighter line:

> “Your cache can be warm. Your trust boundary should not be fuzzy.”

Transition:

> “This becomes especially interesting when the disposable machine is not CI — it is part of training.”

---

## Slide 7 — Coding RL turns reset into a training primitive (13:00–16:00)

Start with:

> “For coding RL, the environment is not just infrastructure around the training example. The environment is part of the training example.”

Point to the episode tuple.

Explain cold path vs fork path.

Be precise:

> “I am not claiming a universal 100× here. I am saying there is a systems opportunity: prepare an authenticated start state once, then make reset a runtime operation instead of reconstructing the world for every episode.”

Critical line:

> “Reset is part of the reward contract.”

Why:
- same task from different hidden state ≠ same experiment,
- leaked previous trajectory ≠ clean episode,
- verifier modifications break reward meaning.

Transition:

> “And that immediately creates another boundary.”

---

## Slide 8 — The student cannot grade their own exam (16:00–18:30)

This is a fun, memorable slide. Slow down.

> “The student cannot grade their own exam.”

Pause.

> “If the agent can rewrite the test harness, the reward function, or the score file, it has not necessarily solved the task. It may have solved the evaluator.”

Point to RUN ≠ EVAL.

> “The searcher may be untrusted. The oracle cannot be in the same writable authority domain.”

Do not overclaim “perfectly leak-proof reward.” Say sealed/owned outside the worker’s write set.

Transition:

> “There is a similar mistake on the other side of the machine: copying credentials because we copied memory.”

---

## Slide 9 — Copy the machine, not the keys (18:30–21:00)

Start:

> “Copy-on-write is a memory optimization. It is not a security policy.”

Good share:
- immutable source,
- toolchain,
- CAS artifacts,
- read-only caches.

Remint:
- credentials,
- egress capabilities,
- verifier state.

Fun line:

> “If the secret survives the fork by accident, that is not credential management. That is inheritance law.”

Then serious line:

> “Warmth is a performance feature. Authority is a capability.”

Transition:

> “Now suppose we solved isolation perfectly. There is still one statistical trap.”

---

## Slide 10 — Four clones do not make four witnesses (21:00–23:30)

Point to the four workers.

> “Four copies of the same ancestor are four executions. They are not automatically four independent witnesses.”

Examples:
- same hidden fixture,
- same model prior,
- same poisoned cache,
- same ancestor.

Then cold liar:

> “And if one worker can claim arbitrarily high confidence, it can dominate the reducer. Isolation does not authenticate confidence.”

No derivation. The room can ask about β, lineage, precision, correlation in Q&A.

Punchline:

> “Fork makes search cheap. It does not manufacture evidence.”

Transition:

> “Once you see that, three domains collapse into the same diagram.”

---

## Slide 11 — Three factories. Same loop. (23:30–25:00)

Read across, not down.

Software:
patch → tests/evidence → merge.

RL:
trajectory → reward/verifier → checkpoint.

HIL/science:
hypothesis/sim → measured evidence → expensive physical tip.

Say:

> “Same slots, different nouns.”

Then:

> “The farther right you go, the more expensive a false positive becomes.”

Transition:

> “That suggests the API I actually want.”

---

## Slide 12 — The capability contract is only three verbs (25:00–26:30)

Do not over-explain.

Fork:
> “Make worlds cheap.”

Reduce:
> “Make evidence honest.”

Promote:
> “Spend authority once.”

Then read the law once:

> “Durable intent. Disposable execution. Singular authority. Deterministic convergence.”

Final technical thesis:

> “Search may be stochastic. Authority may not be ambient.”

Transition:

> “So I want to end with questions rather than pretend this is finished.”

---

## Slide 13 — What I want from this room (26:30–28:30)

Choose **two** of the four questions to speak aloud based on room reaction. Leave all four visible.

Default:
1. What is the right first-class machine value?
2. Where can warm state live without becoming a side channel?

If the room is more statistical:
- ask about correlation / shared ancestry.

If the room is more distributed-systems:
- ask about authority when children outlive parents.

Close exactly:

> “If you remember one thing: burn the runner, keep the proof, fork the machine — not the trust.”

Stop. Do not add a second ending.

---

## Appendix / Q&A

### “Is this just VMs?”
No. VM/microVM isolation is one mechanism. The talk’s claim is about the higher-level contract: forkable state, scoped authority, evidence lineage, reduction, and singular promotion.

### “Is this just checkpoint/restore?”
Checkpoint/restore solves state movement. It does not by itself specify:
- credential inheritance,
- oracle ownership,
- evidence semantics,
- correlation,
- promotion authority.

### “Why not containers?”
Containers can be appropriate under the right threat model. Do not make a universal “containers bad” claim. The boundary must match the untrusted workload and capability exposure.

### “Do forks give independent samples?”
No. Shared ancestry can induce correlation. That is precisely why lineage belongs in the evidence model.

### “What about your statistical-physics language?”
Use only in Q&A:
- annealing / temperature as search-schedule intuition,
- replicas as correlated branches,
- driven/open system as an analogy.

Do **not** claim Gibbs equilibrium, detailed balance, or thermodynamic laws for CI.

### “How much faster is fork reset?”
Answer:
> “That is exactly the benchmark I want to make explicit. I would compare cold build, cached container restart, snapshot restore, and snapshot fork under identical repo/task/verifier episodes. I do not want to quote a universal multiplier before that measurement.”

---

## Hard cut rule

If you are behind at minute 20:
- compress slide 9 to one sentence,
- compress slide 11 to 45 seconds,
- never cut slides 7, 8, 10, 12, or the closing question slide.

The talk works without any physics slide. Physics is depth, not dependency.
