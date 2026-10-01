# Researcher J — Tensorlake as next-level fork fabric (practice lens)
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Tensorlake product primitives as *engineering ontology* for parallel worlds — not a vendor bake-off  
**Fence:** Eng/product = **BACKUP / verbal landscape** only. No Tensorlake / E2B / Daytona / forkd / islo ms as Yossi benchmarks. Physics = interpretation. No Everett-as-physics-proof. Align `CLAIM-FENCE.md` + `PARALLEL-WORLDS-STATPHYS.md` + A’s number fence.

---

## 1. Why Tensorlake is on the practice chart

Peer systems (DeltaBox / Crab / Shepherd / Firecracker) answer *how-fast / what-to-diff / API object*.  
Tensorlake answers a different SRG question: **what does a shipped fork fabric look like when worlds are MicroVMs with durable FS, memory snapshots, suspend/resume, clone fan-out, and an application layer (`@function`) on top?**

For this talk, Tensorlake is the **durable configuration space** in the parallel-worlds diagram (see `scratch/PARALLEL-WORLDS-STATPHYS.md` §5): cheap worlds + Git/FS field + function fan-out. It does **not** ship the talk’s trustworthy reduce / sealed oracle / promote-once fence — that gap *is* the research ask.

**Stage rule:** name once as landscape (with forkd / Mitos / crucible / E2B / Daytona / islo). Never put vendor SQLite / cold-start / Harbor timing tables on slides as “our numbers.”

---

## 2. People (public sources only — names + sources; no gossip)

| Person | Public role | Sources (prefer primary) |
|---|---|---|
| **Diptanu Gon Choudhury** | Founder & CEO / Co-founder, Tensorlake | Bylines “CEO / Co-founder” on [tensorlake.ai/blog](https://www.tensorlake.ai/blog) (e.g. [Suspend vs snapshot](https://www.tensorlake.ai/blog/suspend-vs-snapshot), Harbor posts); [LinkedIn](https://www.linkedin.com/in/diptanu) (“Founder and CEO @ Tensorlake”); California SoS filing for Tensorlake, Inc. lists him CEO (bizprofile / bizfileonline extracts) |
| *(background, optional speaker-note)* | Early HashiCorp engineer; co-led open-source **Nomad**; prior cluster-scheduler / ML infra work (Netflix Titus, Facebook FBLearner — self-described on LinkedIn) | [linkedin.com/in/diptanu](https://www.linkedin.com/in/diptanu); MotherDuck author blurb ([motherduck.com/authors/diptanu-gon-choudhury](https://motherduck.com/authors/diptanu-gon-choudhury/)) |

**Do not invent titles.** LinkedIn company “Key Executives” lists (advisor / founding DS) are noisy — omit unless a primary Tensorlake page confirms. No funding gossip, no personal biography on stage.

**Spoken (optional, ≤1 breath):** “Diptanu Gon Choudhury — Tensorlake founder/CEO; Nomad-era scheduler pedigree — *speaker note*, not a slide claim.”

---

## 3. Product primitives ≡ talk ontology

Sources: [tensorlake.ai](https://www.tensorlake.ai/), [docs — snapshots](https://docs.tensorlake.ai/sandboxes/snapshots), [docs — sandboxes FAQ](https://docs.tensorlake.ai/faqs/sandboxes-faq), [Suspend vs snapshot](https://www.tensorlake.ai/blog/suspend-vs-snapshot), [Applications overview](https://docs.tensorlake.ai/applications/overview).

| Primitive | What it captures | Talk mapping | Slide? |
|---|---|---|---|
| **MicroVM sandbox** (Firecracker / CloudHypervisor) | Hardware-isolated guest: own kernel, FS, processes | ESCAPE wall pedigree (Firecracker NSDI’20); body for searchers | MAIN as *class*; Tensorlake by name = BACKUP |
| **`filesystem` snapshot** | FS only → cold boot restore; resources may change | FS-only branch in A’s taxonomy; “stash the tree, restart the process” | Speaker-note / diagram footnote |
| **`memory` snapshot** | FS + VM memory + running processes → warm restore | Full parallel world (shared past, live mid-flight state) | **MAIN** ontology (not ms) |
| **`tl sbx copy` / clone** | Fan-out warm copies from running/suspended source | `worlds = sandbox.fork(n=K)` | MAIN concept / BACKUP product name |
| **Suspend / resume** | Pause same sandbox ID; meter stops; wake in place | Single-lineage idle (not branch); compute vs storage split | Speaker-note |
| **Versioned FS + hosted Git** (`tl fs` / `tl git`) | Mountable durable dirs; snapshot → promote via CAS | World artifacts as first-class; promote pointer ≠ worker minting tip | Speaker-note (ties G promote) |
| **`@application` / `@function`** | Durable serverless fan-out; each call isolated; checkpoints | Agent-inside vs tool-as-sandbox; map phase of MapReduce | Speaker-note pattern |
| **Orchestrate layer** | Endpoints, retries, queues, observability on sandboxes | Control plane *beside* bodies — still not sealed oracle | Q&A |

### FILESYSTEM vs MEMORY (say carefully)

From docs (paraphrase, attributed):

- **`filesystem`:** captures filesystem; restore = cold boot. Good for golden trees / dependency pins when process tree need not resume.
- **`memory`:** captures filesystem + memory + running processes; restore = warm start; image/resources/entrypoint frozen from snapshot.
- **Clone / copy:** memory-class fan-out — build base once, N identical warm worlds.

**Spoken line:** “Filesystem snapshot saves the tree. Memory snapshot saves the *world* — processes mid-flight. Clone is fan-out of that world. None of that is a trustworthy reduce.”

### Suspend ≠ snapshot (CEO blog, Apr 2026)

| | Suspend | Snapshot |
|---|---|---|
| Identity | Same sandbox ID | New sandbox per restore |
| Artifact | In place | Durable object |
| Fan-out | No branching | N restores |
| Cost shape | No compute while paused | Storage per artifact |

Use suspend for one ongoing agent between idle turns; snapshot/clone for RL/CI fan-out and golden environments.

---

## 4. Agent-inside vs sandbox-as-tool

Two patterns Tensorlake (and peers) make explicit — both belong in Act I/II:

| Pattern | Shape | When | Fence |
|---|---|---|---|
| **Agent-inside** | Long-lived named sandbox = the agent’s computer (SSH/IDE/PTY); suspend between human turns | Coding agents, multi-day sessions | Still needs WIRE remint (E); session ≠ authority |
| **Sandbox-as-tool** | Ephemeral MicroVM per tool call / `@function`; harness stays outside | Untrusted code, tool isolation, map fan-out | Tool score ≠ promote; sealed oracle still outside |

**Compose:** harness can live *in* a durable sandbox while each dangerous tool lands in a fresh child — Search≠Authority still applies to the *tip*.

---

## 5. Gap vs trustworthy reduce / authority fence

Tensorlake-class products **enable** the left column. The talk’s contract still **owes** the right:

| Enabled (practice) | Still owed (research / capability contract) |
|---|---|
| Cheap MicroVM worlds, MEMORY clone fan-out | **Evidence-aware reduce** (2607.09689): \(r_k\), \(\beta\equiv n\), abstain on shared root ρ |
| Durable FS / Git promote pointers | **`Objective.digest` epoch bumps**; promote-once outside CoW body (G) |
| `@function` map + durable checkpoints | **Sealed oracle / attestation \(a_k\)** — child cannot mint \((n,J)\) (C) |
| Suspend / resume economics | **WIRE leases** — fork copies memory; credentials must remint (E) |
| Harbor / eval integrations | **Held-outs never in writable overlay**; RUN≠EVAL |
| Observability traces | **Path-integral CI** — merge consumes \((\hat\theta,\Delta,\mathrm{abstain})\), not a green badge |

**One breath for SRG:** “Tensorlake and friends make worlds cheap. The open problem is making the partition function trustworthy — and keeping promote outside the fork.”

---

## 6. Landscape compare (BACKUP verbal — no latency contest)

```
Firecracker (NSDI'20) ── pedigree wall
        │
   peer: DeltaBox · Crab · Shepherd/OpenRath
        │
   eng/product CoW fan-out (name once, hallway):
        ├── Tensorlake   — MEMORY/FS snap, copy, suspend, tl fs/git, @function
        ├── forkd        — warm-parent CoW / BRANCH (eng README)
        ├── Mitos        — CRD-shaped fork fabric
        ├── crucible     — eng propagator class
        ├── E2B          — pause/snapshot class peer product
        ├── Daytona      — sandbox DX / lifecycle
        └── islo         — Yossi artifact; gateway / WIRE-shaped surface
```

| Axis | Tensorlake (docs/blog) | Typical peer contrast (verbal) |
|---|---|---|
| Isolation | Firecracker / CloudHypervisor MicroVM | Containers share kernel (weaker ESCAPE) |
| Snapshot split | Explicit `filesystem` vs `memory` | Some vendors: “snapshot” = FS-only |
| Suspend vs snapshot | Distinct ops (same as E2B class) | Some collapse pause into snapshot |
| Fan-out | `copy` / restore-many from MEMORY | forkd BRANCH; Mitos CRDs; eng only |
| Artifacts | Versioned FS + hosted Git promote | Git worktrees = source-only isolation |
| Orchestration | `@function` / Orchestrate | Airflow/Ray/Spark = different layer (see L) |

**Never on slide:** vendor SQLite benches, Harbor wall-clock, “84 ms cold start,” forkd ~100 kids/~100 ms — those are *their* marketing or eng notes, not Cambridge peer tables.

---

## 7. Challenges → B / C / G / A / E

### → B (Reduce)
Product clone gives you \(K\) warm siblings from one MEMORY root — **same snapshot root ∈ ℒ ⇒ unresolved ρ**. Will reduce default `verdict=abstain` until overlap tags ship, even when the product happily returns \(K\) green tool scores?

### → C (Oracle)
`@function` durability checkpoints outputs for replay — useful for crash recovery, dangerous if the *grader* lives inside a durable child. Confirm sealed oracle digests stay outside MEMORY restore mutability.

### → G (Factory API)
`tl git promote` / CAS branch move is a *data* promote. Name explicitly that factory `Promote.tip` (merge / checkpoint / paper / wet) is a **different bit** — Git CAS ≠ Search≠Authority tip lease.

### → A / E
MEMORY clone copies credential pages with the world. Demand remint+scrub before child runnable; Tensorlake isolation wall ≠ WIRE lease model.

---

## 8. Slide / speaker checklist

| | |
|---|---|
| **On slide** | Parallel-worlds diagram; Firecracker pedigree; MEMORY vs FS as *ontology* (optional footnote) |
| **Spoken once** | “Tensorlake-class: snapshot, clone, suspend, function fan-out” |
| **Never** | Vendor ms as ours; Everett; Gibbs-of-CoW; “Tensorlake solves reduce” |

---

*Researcher J · 2026-09-27 IDT. Sources: tensorlake.ai + docs.tensorlake.ai + CEO blog bylines + LinkedIn primary for Diptanu only.*
