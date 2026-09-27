# Outline analogies — Cambridge SRG · cam-talk-london-26

**Claim fence:** analogy **illuminates**, does not prove. Prefer deep learning (DL) where natural. Physics = schedule/algebra lens. **No Gibbs-of-nature.** No “agent forks *are* ensembles of magnets.”

**Domains:** SW eng · CS theory · biology · physics · **deep learning** (preferred).

**Legend:** primary analogy first; DL preference noted when used.

---

## Act 0 — Hook

| Beat | Domain | Primary analogy |
|---|---|---|
| Missing OS layer → forkable machine | **SW eng** | `fork(2)` / process clone: Docker made *apps* portable; forkable sandboxes make *agent trajectories* portable — same portability leap, different object. |

**Stage one-liner:** “Not another model — an OS primitive you already trust for processes.”

---

## Act I — Execution contract (six surfaces)

| Surface | Domain | Primary analogy |
|---|---|---|
| **Filesystem state** | **DL** | **Checkpointing ≈ S₀ snapshot** — workspace as `model.ckpt`: named, restore-identical, the object you fork from. |
| **Networking + credentials** | **SW eng** | Object-capability / lease remint on spawn — no ambient `getenv` keys; child gets a *new* wire, not a CoW’d secret. |
| **Reproducibility** | **DL** | Frozen weights + fixed seed: named snapshot → bit-identical restore (same contract as reload-from-ckpt before a run). |
| **Fast cloning** | **DL** | **Ensemble ≈ fork fan-out** — CoW siblings are cheap ensemble members over a shared past, not a rebuild-from-Dockerfile. |
| **Build / test / rollout** | **DL** | **MoE ≈ fork experts** — warm factory *beside* the fork routes specialist workers; the tip stays one gated path. |
| **Recovery + observability** | **SW eng** | WAL / receipts outlive the process — crash ≠ authority; evidence survives the machine the way a commit log survives a pod. |

**Act I trade-off (spoken, not a surface):** isolation ladder ≈ choosing a wall that untrusted shells cannot walk through — denser runtimes are not stronger evidence.

---

## Act II — Three factories

| Factory | Domain | Primary analogy |
|---|---|---|
| **Software factory** | **DL** | **Batch ≈ siblings** — parallel Cells / patches as a minibatch of proposals over shared `S₀`; sibling reuse ≠ confirmation (correlated batch). |
| **RL post-training** | **DL** | **RLHF reward model ≈ oracle outside policy** — scorer sealed outside the writable child; soft temp = Epoch policy, not worker-owned β. |
| **HIL** | **biology** | Phenotype screen: a million genotype / sim forks ≠ one organism-assay (robot) hour — scarcity ladder, same loop. |

**Loop mnemonic (spoken):** snapshot → fork N → search → reduce → promote → burn ≈ ckpt → ensemble → train → distill/pool → early-stop tip → **dropout** the runners.

---

## Act II½ — Two slides

| Slide | Domain | Primary analogy |
|---|---|---|
| **A — Fork ≠ independence** | **DL** | **DDP ≠ evidence independence** — data-parallel replicas share init/weights ⇒ variance floor; all-reduce without lineage forges cold \(n\). Distillation-style reduce needs \((\hat\theta,J,n,\mathcal{E},\mathcal{L})\), not a naked scalar. |
| **B — Anneal + driven sink** | **DL** | **LR schedule ≈ anneal \(T\)** — Epoch digest holds the schedule id; cool gates → \(T\to0\) promote; **early stopping ≈ promote gate**. Promote = absorbing tip under drive, not equilibrium. |

**Fence reminder:** SA / MH / SGD cousins = *schedule language*. Do not say the factory equilibrates.

---

## Act III — Open problems

| Problem | Domain | Primary analogy |
|---|---|---|
| **Fork ≠ independence** | **DL** | Same as II½ A: correlated ensemble under shared root — default abstain; DDP-style sync is not i.i.d. evidence. |
| **WIRE leases** | **SW eng** | Capability remint / short-lived tokens on fork — ambient credentials are the CVE; lit thin → research ask. |
| **Warm CoW channels** | **physics** | Heat / timing side channel — warm pages as unintended bus; pack-by-trust so density ≠ covert channel. |
| **Sealed oracle** | **DL** | Reward-model / judge **outside** the policy’s write set (RLHF / Rebound foil) — digest owned by controller. |
| **Path-integral CI** | **DL** | **Distillation ≈ reduce** — many teacher trajectories → one student tip; merge consumes \((\hat\theta,\Delta,\mathrm{abstain})\), not a green badge. |
| **Promote-once API** | **DL** | **Early stopping ≈ promote gate** — one absorbing tip; compute vs tip; workers never own the stop bit. |
| **World-diff / β-as-Epoch** | **CS theory** | Git conflict = evidence; world-diff is that for machines. Epoch bump on digest change = hyperparam / schedule change — no worker thermostat. |
| **Name the contribution** | **SW eng** | *Fork, Reduce, Promote* as a **capability contract** (POSIX-shaped API surface), not “already shipped everywhere.” |

---

## Close

| Beat | Domain | Primary analogy |
|---|---|---|
| Mantra + three SRG questions | **DL** | **Dropout ≈ burn runners** — kill unused paths; keep the proof (surviving tip / receipts). Fork the *machine*, not the *trust* (trust = sealed oracle + promote bit). |

**Mantra (unchanged):** Burn the runner. Keep the proof. Fork the machine, not the trust.

---

## Cheat sheet — preferred DL map

| DL knob | Factory / contract slot |
|---|---|
| Checkpointing | S₀ snapshot / FS restore |
| Ensemble | Fork fan-out |
| Batch / siblings | Parallel Cells over shared root |
| MoE | Fork experts / warm factory-beside |
| RLHF reward model | Oracle outside policy |
| Distillation | Reduce (structured, not naked scalar) |
| DDP | **≠** evidence independence |
| LR schedule | Anneal \(T\) / Epoch policy |
| Early stopping | Promote gate |
| BN / sync barrier | Reduce barrier before tip |
| Dropout | Burn runners |

---

## Twelve best (stage-ready)

1. **Checkpointing ≈ S₀** — FS as restore-identical object.  
2. **Ensemble ≈ fork fan-out** — CoW siblings, shared past.  
3. **Batch ≈ siblings** — software-factory Cells; reuse ≠ confirmation.  
4. **MoE ≈ fork experts** — warm factory beside the fork.  
5. **RLHF reward model ≈ oracle outside policy** — sealed scorer.  
6. **DDP ≠ evidence independence** — variance floor under shared root.  
7. **Distillation ≈ reduce** — path-integral CI / abstain.  
8. **LR schedule ≈ anneal \(T\)** — Epoch digest owns the cool-down.  
9. **Early stopping ≈ promote gate** — one absorbing tip.  
10. **Dropout ≈ burn runners** — Close mantra.  
11. **Capability remint ≈ WIRE leases** — no ambient keys after CoW.  
12. **Phenotype screen ≈ HIL tip** — million sims ≠ one robot hour.

---

*Analogies · 2026-09-27 (IDT) · illuminates ≠ proves · aligns CLAIM-FENCE + OUTLINE.*
