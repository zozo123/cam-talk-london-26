# Cambridge SRG story spine — Forkable Sandboxes

**Slot:** CL Systems Research Group · Thu 15 Oct 2026 · FW11 · 15:00–16:00  
**Repo:** zozo123/cam-talk-london-26 (empty — scaffold from this)  
**Locked spine:** systems contract, told through three factories that share one machine primitive.

---

## The one-sentence talk

Coding agents, RL post-training, and hardware-in-the-loop all need the same thing: **cheap forked machines for search, and a separate authority that never lives inside those machines.**

Forkable sandboxes are that machine. Everything else is orchestration.

---

## Three inspirations → one law

| Source | What it contributes | What it is *not* in this talk |
|---|---|---|
| **pstack** | Fearless parallelism: many agents, multi-model swarm, verification before trust | Not a Cursor plugin demo; not “how to prompt” |
| **OpenClaw** | The agent *loop* (tools, sessions, sandboxed body) | Not a robotics OS; agents engineer software, they don’t drive motors |
| **ariflow-swfactory** | Control plane: Cell, epoch, Search≠Authority, Airflow lifecycle, evidence, promotion | Not a product pitch; methodology as systems contract |

**Shared law (from liquid-methodology):**  
*Durable intent. Disposable execution. Singular authority. Deterministic convergence.*  
Create entropy where exploration pays; destroy entropy before promotion.

---

## The scarcity ladder (why one substrate serves three workloads)

```
cheap & plural                          scarce & singular
─────────────────────────────────────────────────────────
agent samples / patches                 merge to main
RL rollouts / policy candidates         checkpoint promote
sim / synthetic HIL                     real arm / human hour
forked sandbox                          controller acceptance
     SEARCH  ─────────────────────────►  AUTHORITY
```

A million compiles (or rollouts) are search.  
One robot hour (or one merge) is authority you can burn.

Forkable sandboxes make the left column economically real.  
They must not become the right column.

---

## Act structure (45 min + 15 Q&A)

### Act 0 — Hook (3 min)
Autocomplete wrote code. Agents *run* code.  
The missing OS layer isn’t another model — it’s a machine you can **fork like a process**.

Line: *Docker made apps portable. Forkable sandboxes make agent trajectories portable.*

### Act I — The execution contract (12 min)
Six surfaces the substrate must expose (matches published abstract):

1. **Filesystem state** — workspace as snapshotable object  
2. **Networking + credentials** — brokered wire; no ambient keys in the child  
3. **Reproducibility** — named snapshot → identical restore  
4. **Fast cloning** — CoW microVM economics (~ms–hundreds ms), not rebuild-from-dockerfile  
5. **Build / test / rollout execution** — the warm factory sits *beside* the fork, not inside trust  
6. **Recovery + observability** — crash ≠ authority; receipts outlive the machine  

Trade-off slide SRG will love: container vs gVisor vs Firecracker-class microVM — isolation thickness vs fork latency vs density.

### Act II — Three factories, one primitive (15 min)

Tell the same loop three times with different nouns:

```
snapshot → fork N → run searchers → reduce evidence → promote once → burn runners
```

| Factory | Searchers | Reduce | Promote | Burn |
|---|---|---|---|---|
| **Software** (OpenClaw + swfactory) | agent patches in Cells | tests + evidence digests | human/Airflow gate → main | sandboxes |
| **RL post-training** | rollouts / preference samples | reward / preference model / uncertainty-aware pool | checkpoint / policy release | rollout envs |
| **HIL** | sim / synthetic / teleop proposals | graded evidence L0–Ln | human + scarce hardware slot | trial cells |

**pstack’s gift to the story:** fearless parallelism only works when each arm gets its *own* verifiable machine. Shared laptop = correlated failure + poisoned state. Swarm without fork is theater.

**OpenClaw’s gift:** the agent is the searcher; the sandbox is the body. Without fork+rollback, exploration contaminates the next trial.

**swfactory’s gift:** Cell identity + epoch fencing. Sandbox 17 crashes; Sandbox 18 retries; epoch still owns the work. Worker ≠ authority. Sibling forks reusing the same evidence are not independent confirmation.

**Boltzmann MapReduce (optional Act II½, 3–4 min):** fork makes workers cheap; it does **not** make them independent. Reduce must carry precision, sample size, provenance — or a “cold liar” hijacks the pool. Open systems problem, not a solved product claim.

### Act III — Open systems problems (8 min)
Leave the room with research, not a sales close:

1. **Fork ≠ independence** — shared weights, prompts, caches, gold files  
2. **Credential leases across forks** — capability handles, not env inheritance  
3. **Warm cache vs isolation** — how to share compile/artifact heat without sharing trust  
4. **Acceptance boundary** — agent output = evidence; controller criteria = authority (NYC cousin, one sentence)  
5. **HIL as the extreme** — when the “promote” step costs a robot hour, the substrate’s job is to burn search *before* the scarce slot  

### Close (2 min)
Mantra: **Burn the runner. Keep the proof. Fork the machine, not the trust.**

Three questions for SRG:
1. What is the right API for “forkable machine” (FS, net, GPU, display)?  
2. Where should warm state live so density doesn’t become a side channel?  
3. How do you fence authority when children outlive parents?

---

## Claim fence (hard)

**Say:** substrate for agentic software + RL-style fan-out; HIL as scarcity metaphor / upstream CI tax.  
**Don’t say:** we accelerate GPU RL training; OpenClaw drives actuators; we rewrote HIL-SERL; IB is a robot OS; fork guarantees statistical independence; every swfactory path already has native fork-merge.

Cite liquid-methodology honestly: forkable sandboxes are a **capability contract**, not a claim that default executor already launches N candidate sandboxes per issue.

---

## Differentiation vs your other October talks

| Talk | Room | One idea they keep |
|---|---|---|
| **Cambridge SRG Oct 15** | Systems | Forkable machine as runtime layer; Search≠Authority |
| **RustChinaConf Oct 17** | Rust/CI | Million compiles / one robot hour; warm Cargo factory |
| **Zenity NYC Oct 21** | Security | Four doors; acceptance boundary; Door 4 |

Same universe. Different punchline. No reused 15-minute script.

---

## Next build steps for empty repo

1. README with slot + abstract + this spine  
2. `STORY.md` (this file)  
3. Timed outline + speaker notes  
4. One architecture diagram (snapshot→fork→reduce→promote)  
5. Optional: recorded fork demo (islo/crabbox), not live dependency  
