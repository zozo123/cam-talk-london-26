# World models ↔ forkable sandboxes — the Cambridge bridge

This note is about **Contrastive World Models** (Bonnie Li, arXiv:2609.22175), not Meta's **Code World Model**. Both are relevant to this repo, but they are different works and should never be abbreviated ambiguously on stage.

## 1. Strongest bridge: two ways to make futures cheap

World-model systems such as Dreamer learn dynamics so an agent can train or plan through imagined experience when direct interaction is expensive, slow, scarce, or unsafe. **Contrastive World Models** changes the representation objective: instead of reconstructing every pixel, it encourages the latent state to preserve information predictive of future observations while ignoring visual nuisance factors.

Forkable sandboxes attack the complementary systems variable.

For software, the world itself is executable. A repo, dependencies, processes, tests, and tools define a transition system. If setup/reset is expensive, learned or heuristic approximations become attractive. If a warm, authenticated state can be snapshotted and forked cheaply, many futures can be evaluated by executing the software transition instead.

### Stage formulation

> **World models make imagination cheap. Forkable sandboxes make interaction cheap.**

> **For code, the best world model is often the world.**

### Important fence

Do **not** say “reality is always cheaper than its model.” The crossover is empirical and workload-dependent. Learned models can remain useful for long-horizon planning, action proposal, prioritization, inaccessible external services, physical systems, or whenever executable interaction is still costly.

The systems question becomes:

> At what reset/fork cost does executable interaction dominate learned imagination for a given planning horizon and fidelity target?

That is a strong Cambridge research question.

---

## 2. Forks as executable counterfactuals

A learned dynamics model answers an intervention approximately:

> Starting from state s, what happens if I take action a?

A forkable software runtime can answer the same kind of question by execution:

1. capture one parent state S0,
2. fork N children,
3. apply a different candidate patch/tool action in each child,
4. execute the build/tests/program transition,
5. preserve evidence,
6. reduce and promote once.

This is **branching experimental intervention on the executable environment**. It avoids learned transition-model error inside the captured boundary.

### Better wording than “true counterfactual”

Use **executable counterfactual** or **branching future**. Software execution can still contain nondeterminism, clocks, networks, hardware effects, flaky tests, or external state. The runtime must pin, capture, broker, or explicitly model those sources before branches can be compared as controlled interventions.

This bridge explains why **Fork is a planning primitive**, not only a security or CI primitive.

---

## 3. Snapshot versus latent state

Contrastive World Models asks a representation-learning question:

> What information should a compact latent z retain so future-relevant dynamics remain predictable while irrelevant visual detail is discarded?

A forkable runtime asks a systems version of the sufficiency question:

> What concrete machine/environment state must S contain so execution can continue faithfully from this point?

They are not the same object.

| Learned latent z | Executable snapshot S |
|---|---|
| compressed | usually overcomplete |
| learned | explicit/system-defined |
| deliberately lossy | lossless-ish within a chosen boundary |
| predictive representation | continuation state |
| may incur transition-model error | executes actual program dynamics |
| cheap to roll out | costs real compute/storage |

### Stage-safe line

> “A world model searches for a compact sufficient latent. A snapshot gives me an executable sufficient state — usually much less compact, but I can resume it instead of predict it.”

Do not call the snapshot *the* latent state without this qualification. External state can invalidate sufficiency.

---

## 4. The filtering dual

Contrastive World Models is motivated by nuisance information: pixel reconstruction can spend representation capacity on details irrelevant to planning. The contrastive/InfoMax objective biases the representation toward future-predictive information.

A secure forkable environment also succeeds by exclusion, but at a different layer:

- exclude ambient host state,
- exclude inherited secrets,
- exclude uncontrolled egress,
- exclude writable reward logic,
- exclude sibling contamination,
- retain only the capabilities and state required for the episode.

### Useful analogy

> **CWM asks what information the representation should forget. The sandbox contract asks what information and authority the execution world should never inherit.**

This is an analogy, **not the same theorem**. Keep it as one sentence on stage or use it in Q&A.

---

## 5. The deeper synthesis: model error versus systems error

The failure surfaces are complementary.

### Learned-world failures

- representation omits relevant state,
- transition model is wrong,
- compounding rollout error,
- distractor contamination,
- model exploitation by the policy.

### Forked-world failures

- snapshot omits external state,
- reset is not faithful,
- verifier leaks into the worker,
- credentials/authority inherit accidentally,
- nondeterminism makes comparisons noisy,
- siblings share ancestry and evidence is overcounted.

Both are versions of one question:

> **What state and information are sufficient for a future, and what errors appear when the boundary is wrong?**

That connects the world-model literature to the Cambridge systems agenda without pretending the mechanisms are identical.

---

## 6. Final thesis after adding this bridge

Before this bridge, the talk can sound like a strong sandbox/CI talk.

After it, the claim is broader:

> **Forkable sandboxes are an environment-layer primitive for learning and search systems.** When a world is executable, a fork can turn real interaction itself into a cheap planning operation. The remaining hard problems are then not only isolation and latency, but state sufficiency, reward integrity, evidence correlation, and authority.

That is the level of abstraction appropriate for Cambridge SRG.

---

## 7. Sources / nomenclature

- Danijar Hafner, Wilson Yan, Timothy Lillicrap, **Training Agents Inside of Scalable World Models (Dreamer 4)**, arXiv:2509.24527 (2025).
- Bonnie Li, **Contrastive World Models**, arXiv:2609.22175 (2026).
- Meta FAIR, **Code World Model**, September 2025 — separate work; trained on Python execution and agentic container trajectories and RL in verifiable coding/software-engineering environments.

Do not abbreviate both world-model works as “CWM” in the same paragraph without expanding the name.
