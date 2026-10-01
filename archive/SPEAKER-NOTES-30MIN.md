# Speaker notes — Cambridge SRG · 30 minutes

Talk: **Forkable Sandboxes: The Runtime Layer for AI Software Factories**  
Speaker: **Yossi Eliaz — Incredibuild / islo.dev + HIT**  
Target: **27–28 minutes of content + 2–3 minutes slack**

The talk should feel like a story about **state and cheap futures**:
1. state as something science must reproduce,
2. state as something build systems want to reuse,
3. state as something agents make dangerous,
4. world models as one way to make futures cheap,
5. forkable runtimes as the systems dual: make executable interaction cheap enough to branch directly.

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

## Slide 5 — There are two ways to make futures cheap (6:30–9:30)

Point left:

> “Dreamer-style systems learn a world because interacting with the world can be slow, unsafe, or scarce. They buy cheap imagination by accepting approximation.”

Mention Contrastive World Models precisely:

> “Bonnie Li’s Contrastive World Models makes the representation selective: do not waste the latent reconstructing nuisance pixels; preserve what predicts the future.”

Point right:

> “But software gives systems people another lever. The world is executable. We can attack the interaction cost itself.”

Main line:

> “World models make imagination cheap. Forkable sandboxes make interaction cheap.”

Then the careful inversion:

> “I am not saying a fork always beats a model. I am saying there is a crossover. For the part of the world that is executable and cheap to reset, why predict the transition if I can run it?”

Transition:

> “That turns a snapshot into a planning primitive.”

---

## Slide 6 — For code, the best world model is often the world (9:30–12:00)

Trace S0 → patch A/B/C/N → execute tests → evidence → promote.

> “A learned model asks: what would happen if I did A instead of B? A fork lets me perform both interventions from the same parent state.”

Use the exact phrase:

> “These are executable counterfactuals: same past, different intervention, actual software transition inside the boundary I captured.”

Claim fence aloud:

> “Not philosophical magic and not zero uncertainty: clocks, external services, hardware and nondeterminism still matter. The narrower claim is no learned transition-model error for the state I actually execute.”

Then:

> “For code, the best world model is often the world.”

Transition:

> “But that only works if we are precise about what the world contains.”

---

## Slide 7 — A fork should copy state, not authority (12:00–14:30)

Four buckets; one sentence each.

Copy:
> “Enough concrete state to continue the experiment.”

Share carefully:
> “Heat is useful — toolchains, CAS, immutable caches — but sharing itself is a policy.”

Remint:
> “Credentials and network identity are capabilities, not ordinary memory bytes.”

Keep outside:
> “The ruler and the promotion key do not live in the student’s backpack.”

Punchline:

> “Copy the machine, not the keys.”

Optional CWM bridge:

> “This is the filtering dual: CWM asks what the representation should forget; the sandbox contract asks what state and authority the child should never inherit. Same shape of question, different layer.”

Transition:

> “This becomes especially concrete when the disposable machine is part of training.”

---

## Slide 8 — Coding RL turns reset into a training primitive (14:30–17:15)

> “For coding RL, the environment is part of the training example.”

Point to the tuple.

> “Same task, different hidden starting state is not the same experiment.”

Cold path versus fork path.

> “I am not putting a universal speedup number on this. The systems opportunity is to prepare an authenticated state once and make reset a runtime operation.”

Critical line:

> “Reset is part of the reward contract.”

Transition:

> “And reward creates the next boundary.”

---

## Slide 9 — The student cannot grade their own exam (17:15–19:15)

Say slowly:

> “The student cannot grade their own exam.”

Pause.

> “If the agent can rewrite the test harness or reward script, it may have solved the evaluator rather than the task.”

Point to RUN ≠ EVAL.

> “The searcher can be untrusted. The oracle cannot be in the same writable authority domain.”

Transition:

> “Perfect isolation still does not give us independent evidence.”

---

## Slide 10 — Four clones do not make four witnesses (19:15–21:30)

> “Four copies of one ancestor are four executions. They are not automatically four independent witnesses.”

Shared model, prompt, artifact, hidden bad fixture, ancestor.

Cold liar:

> “If a worker can mint its own confidence, it can dominate a reducer. Isolation does not authenticate confidence.”

Punchline:

> “Fork makes search cheap. It does not manufacture evidence.”

Transition:

> “Once you see that, several domains collapse into one runtime shape.”

---

## Slide 11 — Three factories. Same loop. (21:30–23:00)

Software: patch → tests/evidence → merge.  
RL: trajectory → verifier/reward → checkpoint.  
HIL/science: hypothesis/sim → evidence → expensive physical tip.

> “Same slots, different nouns. The farther right you go, the more expensive a false positive becomes.”

Transition:

> “So the API I want is embarrassingly small.”

---

## Slide 12 — The capability contract is only three verbs (23:00–25:00)

Fork:
> “Make worlds cheap.”

Reduce:
> “Make evidence honest.”

Promote:
> “Spend authority once.”

Read the law once:

> “Durable intent. Disposable execution. Singular authority. Deterministic convergence.”

Then:

> “Search may be stochastic. Authority may not be ambient.”

Transition:

> “I want to end with the systems questions this opens, not pretend the problem is finished.”

---

## Slide 13 — What I want from this room (25:00–27:30)

Speak two or three depending on the room.

Default questions:

1. **Executable state:** what must the first-class machine value actually include?
2. **Model vs world crossover:** at what fork/reset cost is executable interaction cheaper than learned imagination for a given horizon?
3. **Correlation:** how should shared ancestry change evidence reduction?
4. **Authority:** how does a child inherit state without inheriting the power to grade/promote itself?

Close exactly:

> “If you remember one thing: burn the runner, keep the proof, fork the machine — not the trust.”

Stop.

---

## Appendix / Q&A

## World-model Q&A

### “Are you saying world models are unnecessary for code?”

No.

> “I am drawing the crossover. World models are useful when interaction remains expensive or unavailable, and for proposing/prioritizing long-horizon futures. Forks are attractive when the environment is executable, high-fidelity, and cheap to reset. A good system can use both: model to choose branches, forks to ground them.”

### “Is a snapshot the latent state?”

Not literally.

> “A world model learns a compact, deliberately lossy predictive latent. A snapshot is explicit and usually overcomplete. The connection is the sufficiency question: what state must survive for the future to continue correctly?”

### “Does a fork remove sim-to-real?”

Only for the software dynamics actually executed inside the boundary.

> “External services, time, hardware, randomness, production state and incomplete tests can all sit outside it. My precise claim is no learned transition-model error for the transition we execute.”

### “How does Contrastive World Models connect to sandbox filtering?”

> “CWM asks what the representation should forget so nuisance pixels do not dominate. A sandbox asks what state and authority a child should never inherit. It is a useful duality, not the same theorem.”

---

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
- compress slide 11 to 35 seconds,
- compress slide 12 to the three verbs + one law,
- never cut slides 5, 6, 8, 9, 10, or the closing question slide.

The talk works without any physics slide. Physics is depth, not dependency.
