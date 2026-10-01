# Researcher L — Algorithms & frameworks for fork / split / merge / reduce
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Classical + modern split/merge patterns → what Tensorlake-class products enable vs what frameworks still owe (Z, leases, sealed oracle)  
**Fence:** Capability contract ≠ inventory. No “Airflow already does N-way fork-merge.” No vendor latency. Git merge ≠ world-diff coverage of GPU/mem/net. Align G / B / J / K.

---

## 1. Lineage map (one diagram worth of words)

```
MapReduce (Dean/Ghemawat) ──► Dryad DAG ──► Spark RDD lineage
        │                         │              │
        │                    CIEL dynamic        │
        │                         │              │
        └────────────► Ray (tasks + actors) ◄────┘
                            │
              fork-join · work-stealing · futures
                            │
         Evidence-Aware MapReduce (2607.09689)  ← THIS talk’s reduce
                            │
         Tree search / MCTS / Tree-GRPO (Shepherd)
                            │
         Airflow DAG as *authority spine* (not the fork fabric)
```

**Spoken:** “Map made workers. We finally have machines you can fork. The missing piece is still an honest reduce — and a promote that isn’t a CRDT.”

---

## 2. Pattern catalog (each: algo → talk mapping → stage)

| Pattern | Classic home | Talk mapping | Stage |
|---|---|---|---|
| **MapReduce** | Dean/Ghemawat OSDI’04 | `fork N` = map; pool = reduce; burn = dispose intermediates | **MAIN** mental model |
| **Evidence-Aware MapReduce** | [2607.09689](https://arxiv.org/abs/2607.09689) | \(r_k=(\hat\theta,J,n,\mathcal{E},\mathcal{L},m)\); β≡n; cold liar; `abstain` | **MAIN** |
| **Fork-join** | Cilk / OpenMP / java.util.concurrent | Parent waits on structured children; join ≠ promote tip | speaker-note |
| **Work-stealing** | Blumofe/Leiserson Cilk | Idle workers steal tasks — scheduler density, not evidence independence | speaker-note |
| **Futures / promises** | Multilisp / modern async | Handle to unfinished world; must not smuggle authority credentials | speaker-note |
| **BSP / barrier sync** | Valiant BSP; Spark stages | Barrier = “all maps done” — foil to **abstain-on-correlation** (don’t wait for fake N) | speaker-note |
| **CRDTs** | Shapiro et al. | Convergent *data* merge without coordination — **contrast** promote-once (authority is scarce, not convergent) | speaker-note (contrast) |
| **Git merge / 3-way** | Git | Textual lineage + conflict markers; cousin of world-diff — **does not** cover mem/GPU/net/creds | speaker-note |
| **World-diff** | Talk agenda (G/A) | CoW divergence of full machine state; conflict = evidence | Q&A / Act III |
| **Spark RDD lineage** | Zaharia NSDI’12 | Recompute from narrow/wide deps — snapshot lineage cousin | speaker-note |
| **Ray DAG + actors** | Moritz OSDI’18 | Dynamic graphs + stateful actors; RL sim+train | speaker-note |
| **Airflow DAG** | Apache Airflow | **Authority spine**: gates, retries, human tip — not MicroVM CoW | speaker-note (swfactory) |
| **Tree search / MCTS** | Kocsis/Szepesvári UCT; Coulom | Expand = fork; backup = reduce along path | speaker-note |
| **Tree-GRPO** | Shepherd 2605.10913 | Branching RL on effect traces | **MAIN** (via Shepherd) |
| **Divide-and-conquer** | Classical algorithms | Recursive fork; still needs ρ-honest reduce at combine | speaker-note |
| **Barrier sync vs abstain-on-correlation** | BSP vs B’s contract | Barrier assumes interchangeable workers; shared snapshot root ⇒ **abstain**, don’t barrier-narrow Σ_g | **MAIN** (with B) |

### CRDTs vs promote-once (say once, carefully)

| CRDT intuition | Promote-once (this talk) |
|---|---|
| Concurrent updates eventually converge | One scarce tip per Epoch |
| Conflict-free by design | Conflict = **evidence** for the gate |
| Anyone may write (within type) | Workers must **not** hold tip credentials |
| Great for collaborative docs | Wrong algebra for merge-to-main / wet-lab / paper claim |

### Git merge vs world-diff

| Git | World-diff (owed) |
|---|---|
| Blobs/trees/lines | FS + mem + processes + device bindings |
| 3-way text merge | Divergence sketches / overlay stacks |
| Conflict markers in files | Conflict as structured evidence for reduce |
| `main` move = social+CI | `Promote.tip` with sealed oracle + leases |

---

## 3. Frameworks: what they give vs what they omit

| Framework | Gives | Omits (talk gap) |
|---|---|---|
| **Hadoop/MapReduce** | Map/reduce scheduling, shuffle | MicroVM body; evidence-weighted reduce; WIRE |
| **Spark** | RDD lineage, stages, fault recompute | Agent in-trajectory fork; sealed oracle |
| **Dryad/CIEL** | General/dynamic DAGs | CoW machine fork; promote fence |
| **Ray** | Tasks+actors, RL loops | Trustworthy Z after correlated rollouts; credential remint |
| **Airflow / Temporal / Prefect** | Authority spine, retries, human gates | Native N-way MicroVM fork (capability ≠ inventory) |
| **Tensorlake Orchestrate / `@function`** | Durable function fan-out, sandbox bodies | Evidence-aware reduce; objective digest epochs; tip leases |
| **Shepherd API** | Typed fork/revert/merge for meta-agents | Peer ρ; WIRE model |
| **Kubernetes Jobs** | Scale-out pods | Warm MEMORY clone semantics; Search≠Authority |

---

## 4. Practical patterns Tensorlake-class products enable

Sources: docs.tensorlake.ai snapshots / applications; CEO suspend-vs-snapshot blog — **patterns**, not benchmarks.

| Pattern | How (product shape) | Factory slot |
|---|---|---|
| **Golden base → fan-out** | MEMORY snapshot / `copy -n K` after setup | Map phase; RL rollouts; CI matrix |
| **Idle without lose-state** | Suspend named sandbox; resume same ID | Human-in-loop coding agent |
| **Tool isolation** | Ephemeral sandbox or `@function` per tool | Sandbox-as-tool |
| **Agent computer** | Long-lived MicroVM + tl fs/git mounts | Agent-inside |
| **Artifact promote (data)** | `tl git snapshot` → CAS promote to branch | *Data* tip — not factory `Promote.tip` |
| **Durable map steps** | `@function` checkpoints for replay | Crash recovery in map |

---

## 5. What frameworks still owe (Z, leases, sealed oracle)

| Owed primitive | Why products/frameworks don’t finish it | Owner in swarm |
|---|---|---|
| **Trustworthy Z / reduce** | Fan-out returns K scalars; shared MEMORY root ⇒ ρ>0; need \(r_k\), abstain, cold-liar clip | B + 2607.09689 |
| **`Objective.digest` epochs** | Changing metric mid-flight must hard-bump Epoch — not soft anneal | G ↔ B ↔ D |
| **Sealed oracle** | Grader in writable child ⇒ Rebound; need controller digests + \(a_k\) | C |
| **WIRE leases** | MEMORY clone copies secrets; need remint+broker | E |
| **Promote-once tip kinds** | Git CAS ≠ paper/wet/robot tip; two-phase `Promote.compute` / `Promote.tip` | G ↔ D |
| **Abstain-on-correlation** | Barrier sync lies when siblings share snapshot root | B + A lineage tags |
| **World-diff protocol** | Git doesn’t merge GPU/mem/net; conflict=evidence API missing | G / Act III |
| **Pack-by-trust** | Work-stealing schedulers optimize fill, not side channels | F |

**One line:** “Tensorlake-class makes the measure samplable. Frameworks still owe the partition function, the lease, and the sealed energy function.”

---

## 6. Divide-and-conquer / tree algorithms ↔ sandboxes

| Algo move | Sandbox move | Reduce honesty |
|---|---|---|
| Split problem | `fork` / MEMORY clone | Children correlated if shared root |
| Conquer | Run agent/rollout in child | Oracle outside body |
| Combine | Reduce / Tree backup | Weighted by n,J — abstain if ρ unresolved |
| Root decision | Promote once | Singular tip; burn runners |

MCTS: select→expand(**fork**)→simulate→backup(**reduce**). Tree-GRPO: same spine with learned policy over Shepherd traces.

---

## 7. Challenges → J / B / G / K

- **→ J:** Which Orchestrate/`@function` patterns should we demo verbally without implying sealed oracle ships?  
- **→ B:** Is “barrier then average” the anti-pattern slide under abstain-on-correlation?  
- **→ G:** Name Airflow as authority spine on the wire diagram — fork fabric ⊥ tip spine.  
- **→ K:** Dean/Ghemawat + Ray + Kirkpatrick are enough spoken lineage; keep CRDT contrast to one breath.

---

## 8. Slide / speaker checklist

**On slide:** Map → fork-join worlds → evidence-aware reduce → promote once.  
**Spoken:** CRDT≠promote; Git≠world-diff; barrier≠abstain.  
**Never:** “Spark already solves agent fork”; vendor ms; Everett.

---

*Researcher L · 2026-09-27 IDT.*
