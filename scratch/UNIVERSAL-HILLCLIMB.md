# The universal hill-climb — story depth for Cambridge

Forkable sandboxes are not “better VMs.” They are the **machine that makes scientific iteration cheap** for every domain that looks like:

> propose → isolate → measure → keep or revert → promote once

That loop is **hill-climbing**. Auto-software, auto-build, auto-research, biology, simulation, RL post-training, and HIL are the *same loop* with different oracles and different scarcity at the tip.

---

## 1. What hill-climbing actually is (pstack’s discipline, generalized)

From pstack’s hillclimb playbook, stripped of Cursor furniture:

1. **Own one metric** and a stop predicate (target + floor on attempts — lucky early win can’t end the run).
2. **Freeze the harness** before changing the system. Prove sensitivity. Baseline + regression gate.
3. **Decision log** — one row per attempt: hypothesis, before, after, verdict.
4. **One change per attempt.** Measure. Keep or full revert. Never stack untested changes. Never claim a win from inspection.
5. **Fan independent hypotheses into separate worktrees / machines** — then serialize only shared state.
6. **Push past plateaus**; don’t relax the predicate to meet it.
7. **Promote** the accepted stack through a review gate.

**The systems translation:** every step that touches state needs a **forkable body**. Without fork, “revert” is a prayer; without a frozen harness, “better” is theater; without singular promote, the swarm becomes twenty control planes.

---

## 2. The universal schema

| Slot | Meaning | Must live outside the forked worker |
|---|---|---|
| **Objective** | What “uphill” means (objective digest) | Yes — changing it is an authority act |
| **State S₀** | Named snapshot / content-addressed parent | Yes — immutable parent |
| **Proposal Δ** | Patch, hyperparam, sequence, protocol, mesh | Generated in child |
| **Oracle O** | Tests, reward, binding assay, solver residual, human preference | Criteria owned by controller; may *run* in child but answers compared to controller copy |
| **Evidence E** | Metric, logs, digests, lineage | Retained with provenance |
| **Verdict** | keep / revert | Controller + gate |
| **Promote** | Merge, checkpoint, publish paper claim, book HIL slot | Singular authority |

**Law:** Search may be stochastic. The objective digest, the parent snapshot id, and the promote bit may not.

This is exactly swfactory’s Search≠Authority, liquid entropy create/destroy, and Boltzmann “fork ≠ independence.”

---

## 3. One loop, many factories

```text
        ┌──────────── objective digest (authority) ────────────┐
        ▼                                                      │
   snapshot S₀ ──fork──► child₁…N ──run──► evidence Eᵢ         │
        │                     │                                 │
        │                     ▼                                 │
        │              reduce / compare (precision, lineage)    │
        │                     │                                 │
        │              keep? ──no──► burn child, log revert     │
        │                 │yes                                  │
        │                 ▼                                     │
        └────────── promote once ──► new S₀' / release ─────────┘
                         burn runners
```

| Domain | Proposal | Oracle (examples) | Scarce tip |
|---|---|---|---|
| **Auto software** | agent patch (OpenClaw / pstack swarm) | tests, types, eval harness | merge to main |
| **Auto build / CI** | toolchain or cache policy change | build graph time, correctness digests | protected branch |
| **RL post-training** | rollout / preference sample | reward model, win-rate, KL | policy checkpoint |
| **Simulation science** | mesh, timestep, constitutive param | residual, conservation, validation suite | “publishable run” |
| **Computational biology** | sequence design, docking pose, pipeline knobs | binding score, wet-lab assay, replication | wet lab / animal / clinic |
| **HIL / Physical AI** | controller candidate from sim | sim metrics → then human + arm | robot hour |
| **Auto research** | hypothesis + experiment script | pre-registered metric + reproduction | paper / grant claim |

**Biology and sim are not special cases.** They are domains where the oracle is expensive or noisy, so you *must* burn cheap forked search before you spend the tip. That is the same scarcity ladder as “million compiles / one robot hour.”

---

## 4. Why forkable sandboxes are the runtime layer for *all* of this

Without forkable machines you get:

| Failure | Symptom |
|---|---|
| **Contaminated search** | Trial N leaves packages, files, env in the machine Trial N+1 inherits |
| **Fake independence** | Parallel agents share one FS → correlated “wins” |
| **Unrevertability** | No snapshot → can’t full-revert; hillclimb dies |
| **Authority leak** | Worker holds publish keys / wet-lab booking / merge token |
| **Harness drift** | Metric script edited inside the same sandbox as the subject |
| **Evidence theater** | Green badge without lineage; siblings cite shared gold |

Forkable sandboxes fix the *body* of the loop. They do not fix the *brain* (model) or the *judge* (objective). Cambridge talk owns the body; mentions brain/judge as interfaces.

---

## 5. Auto-research as the widest frame (still systems, not vibes)

“Auto research for biology / simulations / everything” is:

> a factory that hill-climbs claims under a frozen evaluation contract, with disposable execution and singular publication authority.

That is **factory-of-factories** in swfactory language: child generations with budgets, lineage, no inherited production credentials, explicit promote/rollback.

Claim fence for SRG:
- Yes: the *architecture* of auto-research is this loop.
- No: we have replaced Principal Investigators, or automating wet labs end-to-end, or AGI scientist demos.

Yossi’s Cambridge punch: *the systems problem of auto-research is not generating hypotheses — it’s making keep/revert and promote honest at scale.*

---

## 6. Story beats for the talk (deeper than three factories)

**Cold open:** Science has always been hill-climbing. Agents made proposals cheap. The bottleneck moved to **honest isolation and honest measurement**.

**Reveal:** The same OS primitive — forkable sandbox — underwrites:
1. software factories (your Airflow cells),
2. agent swarms (pstack/OpenClaw),
3. RL rollouts,
4. sim parameter sweeps,
5. computational biology campaigns,
6. and the cheap side of HIL.

**Tension:** Fork makes search cheap; it does not make workers independent or objectives true. Reduce + acceptance boundary + epoch fencing are the hard open problems.

**Close:** Build the lever (frozen harness). Separate before sharing state (fork). Sequence verifiable units (one Δ). Promote once. Burn the runner. Keep the proof.

---

## 7. Lines you can say aloud

- “Hill-climbing is not a coding trick. It’s the shape of every closed-loop improvement system.”
- “pstack’s discipline — one change, one measurement, keep or revert — is an OS requirement once agents fan out.”
- “OpenClaw is the searcher. The sandbox is the body. Airflow is the spine. Promotion is the brain stem — singular.”
- “Biology doesn’t need a different sandbox story. It needs a more expensive oracle and a stricter tip.”
- “Auto-research fails the day the experiment and the scorekeeper share a writable machine.”

---

## 8. What this does to the Cambridge abstract

Stay faithful to published abstract (systems challenges of forkable environments).  
Enrich Act II: not only “software factory,” but **universal hill-climb substrate** with SW / RL / sim / bio / HIL as isomorphic instances.  
Do not turn the hour into a biology keynote or an AGI-scientist pitch — one isomorphism slide is enough; depth stays on FS/net/creds/clone/recovery/reduce.
