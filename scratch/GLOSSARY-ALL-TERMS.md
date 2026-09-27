# Glossary — all terms (swarm A–M + physics)
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Purpose:** One mega note so deck, Q&A, and papers share vocabulary.  
**Fence:** Physics terms = *interpretation with teeth* (algebra + schedule), not Gibbs-of-nature. Vendor ms verbal only.

Alphabetized within sections. Cross-refs: `swarm/A`…`M`, `CLAIM-FENCE.md`, `PARALLEL-WORLDS-STATPHYS.md`.

---

## A. Systems / fork fabric

| Term | Meaning (talk sense) | Home |
|---|---|---|
| **Async-warm** | Background thread that pre-faults / privatizes CoW pages after template `fork()` so the agent’s first writes don’t stall on the critical path | A, DeltaBox |
| **BRANCH / clone / copy** | Fan-out of a warm world into N siblings; product names vary (`tl sbx copy`, forkd `Fork`, Shepherd `scope.fork`) | A, J |
| **Burn / burn-after-promote** | Dispose runner sandboxes after authority decision; keep receipts / evidence, not machines | G, B, CLAIM-FENCE |
| **Checkpoint (ckpt)** | Capture state so rollback/restore is possible; may be FS-only, process/mem, full-VM, delta, or semantics-selective | A |
| **Cold start** | Boot / restore with no warm template resident | A, landscape |
| **CoW (copy-on-write)** | Share pages/blocks until a writer forces a private copy; density substrate *and* side-channel surface | A, F |
| **Crab** | Semantics-aware C/R: eBPF net-change decides whether/what to checkpoint per turn | A · 2604.28138 |
| **CRIU** | Checkpoint/Restore In Userspace — process memory dumps; lazy-pages via userfaultfd | A, DeltaCR |
| **DeltaBox** | Change-based coupled FS+mem C/R sandbox on Firecracker (DeltaFS + DeltaCR) | A · 2605.22781 |
| **DeltaCR** | Process half of DeltaBox: incremental dump + frozen **template** + `fork()` restore | A |
| **DeltaFS** | Filesystem half: hot overlay layer switch + CoW uppers (often XFS reflink) | A |
| **DeltaState** | Atomic (filesystem, process memory) pair treated as one transactional checkpoint | A |
| **Diff snapshot (Firecracker)** | Snapshot of pages dirtied since prior snap; peer baselines show merge cost on restore | A, M |
| **Effect trace / Session** | Shepherd commits / OpenRath Session — branchable execution object (not just bytes) | A |
| **Escape wall** | Outer isolation that stops host compromise (microVM/KVM preferred for untrusted agents) | C, M |
| **Evidence wall** | Binding that child-reported scores cannot mint authority (sealed oracle / attestation) | C |
| **Fan-out** | Launch N parallel children from one warm parent (RL / BoN / MCTS siblings) | A, B |
| **Firecracker** | Lightweight KVM microVMM (NSDI’20); pedigree isolation wall for many agent sandboxes | A, M |
| **Fork (systems)** | Create a child world sharing a past; may mean OS `fork()`, VM restore-clone, or API `World.fork` | A, G |
| **forkd** | Per-node daemon owning Firecracker VMs + gRPC Fork/heartbeat (Mitos stack) | A, M |
| **Full-VM snapshot** | Guest RAM + devices (± block) captured by VMM | A, M |
| **FS-only snapshot** | Files/tree only; process usually cold-restarts (Tensorlake `FILESYSTEM`) | A, J |
| **Inference-masked checkpoint** | Hide ckpt cost under LLM RTT (DeltaBox NPD keeps sockets out of frozen agent) | A |
| **Irreversible effect** | Side effect that C/R cannot undo (email, paid API, wet tip) — record-only | A, D |
| **Kata Containers** | K8s RuntimeClass wrapping each pod in a lightweight VM (QEMU/FC/CH backends) | M |
| **KSM** | Kernel Samepage Merging — cross-guest page merge; density vs confidentiality | F |
| **Lattice** | Tensorlake’s dynamic cluster scheduler (product name) | J, M |
| **libkrun / krucible** | Embeddable VMM (KVM+HVF); krucible fork adds snapshot/fork | M |
| **Lineage \(\mathcal{L}\)** | Snapshot/template/ancestry tags emitted with worker evidence | A, B, F |
| **Live migration** | Move a running VM across hosts with short downtime | M (CH/QEMU) |
| **MAP_PRIVATE** | mmap flag: private CoW mapping over a shared snapshot file | A, F |
| **Memory snapshot** | FS + guest/process memory + mid-flight processes (Tensorlake `MEMORY`) | A, J |
| **microVM** | Minimal-device hardware-virtualized guest (Firecracker class) | A, M |
| **Mitos** | Open control plane for forkable Firecracker sandboxes (CRDs, forkd, CoW metering) | M |
| **NPD (Network Proxy Daemon)** | Sidecar that owns LLM sockets so agent templates stay fork-safe | A (DeltaBox) |
| **OpenRath Session** | First-class branchable/inspectable runtime value | A · 2606.19409 |
| **Overlay / upper / lower** | Union-FS layering; checkpoint often freezes upper → new CoW upper | A |
| **Pack key** | Placement tuple for co-residency policy, e.g. `(tenant, template_digest, threat_tier, wire_epoch)` | F |
| **Reflink** | Filesystem extent sharing (XFS/Btrfs) so CoW doesn’t full-copy files | A |
| **Restore / rollback** | Return to a prior checkpoint (agent view: rollback; mechanism: restore) | A |
| **SandboxEscapeBench** | Benchmark showing frontier models escape Docker-class misconfigs → motivates microVM wall | C · 2603.02277 |
| **Shepherd** | Agent+env as Git-like effect trace; programmable fork/revert/merge | A · 2605.10913 |
| **Side-channel (warm CoW)** | Observability of shared past via fault timing / residency / write-set sketches | F |
| **Snapshot taxonomy** | FS-only · process/mem · full-VM · delta · semantics-selective · effect-trace · warm-parent CoW | A |
| **Suspend vs snapshot** | Suspend = same ID pause; snapshot = durable artifact, often forkable | J |
| **Template (process)** | Frozen SIGSTOP’d process used as `fork()` donor for fast restore | A |
| **Template (VM / warm pool)** | Pre-booted or snapshotted base claimed by new sandboxes | A, M |
| **Tensorlake** | Product MicroVM sandboxes + versioned FS + MEMORY/FILESYSTEM snaps + clone | J, M |
| **userfaultfd (UFFD)** | Kernel API for userspace handling of page faults — lazy snapshot populate | A, M |
| **VFIO / iommufd** | Device passthrough (GPU) into a VM; usually **breaks** cheap snapshot/migrate | M |
| **vmgenid** | Virtual machine generation id — reseeds guest CRNG after clone/restore | A, E |
| **Warm parent / warm pool** | Resident snapshot or live VM that children clone from | A, F |
| **World** | One sandbox configuration + mid-flight state; fork creates parallel worlds | G, PARALLEL-WORLDS |
| **Xu–Kaffes agenda** | Open systems foundations: fork semantics, external side-effects, native CoW fork | A · 2510.05556 |

---

## B. Reduce / statistical physics (algebra)

| Term | Meaning | Home |
|---|---|---|
| **Abstain** | First-class Reduce verdict when ρ unresolved / cold-liar / Δ fails — **do not** narrow \(\Sigma_g\) | B, G |
| **β (beta) / \(\beta_k=n_k\)** | Inverse-temperature *naming*: sample size / information weight of worker \(k\) — colder shouts louder | B · 2607.09689 |
| **Cold liar** | Worker forging high precision \(P_o\) / \(n\) without real samples — hijacks inverse-information pool | B |
| **Cochran \(Q\) / residual \(\Delta\)** | Heterogeneity of worker estimates after pooling; \(\Delta\sim\chi^2\) intuition in Gaussian case | B |
| **Evidence-Aware MapReduce** | Paper framing (2607.09689): map = fork workers; reduce = precision-weighted pool with evidence IDs | B |
| **Exchangeable correlation \(\rho\)** | Shared-root siblings are not i.i.d.; \(\mathrm{Var}(\bar\theta)\) floors at \(\rho\sigma^2\) | B Eq. 1 |
| **Gibbs / Wald kernel \(g_k\)** | \(g_k=\exp\{-\beta_k E_k\}\) — product-pool building block (naming, not thermalization claim) | B |
| **MapReduce (classic)** | Map embarrassingly parallel tasks; reduce aggregates — foil that ignores evidence/authority | B, G |
| **Natural parameters \((P,q,c,N)\)** | Associative merge state for Gaussian/Wald pool | B |
| **Partition \(Z\) / \(Z_g\)** | Normalizer of pooled kernels; **diagnostic** (volume + \(\Delta/2\)), **not** Bayes evidence / CI green | B |
| **Path integral (operational)** | \(Z\approx\int\mathcal{D}[\mathrm{path}]\,e^{-\beta E(\mathrm{path})}\) — fan-out of trajectories under a protocol | B, I, PARALLEL-WORLDS |
| **Precision \(P_k=n_k J_k\)** | How loud a worker may influence the pool | B |
| **Promote (physics clothes)** | \(T\to0\) authority selection; free-energy *language* only | B, H |
| **Reduce** | Merge structured worker records into pooled estimate / verdict (possibly abstain) | B, G |
| **Replica** | CoW sibling — correlated unless evidence proves otherwise | B |
| **Self-consistency** | Majority / agreement foil; upgraded by evidence-aware contract | B |
| **Worker record \(r_k\)** | \((\hat\theta_k,J_k,n_k,\mathcal{E}_k,\mathcal{L}_k,m_k)\) — systems API of a child | B |
| **\(\mathcal{E}_k\)** | Evidence IDs (duplicate-ID reject; Proof-of-Use cousin) | B |
| **\(\hat\theta_k\)** | Child’s estimate / claim | B |
| **\(J_k\)** | Per-observation information / precision shape | B |
| **\(m_k\)** | Execution metadata (placement, retry, speculative tag) | B |
| **\(n_k\)** | Literal sample count (= \(\beta_k\)) | B |

---

## C. Oracle / RL / escape

| Term | Meaning | Home |
|---|---|---|
| **Attestation \(a_k\)** | Controller bit / sealed receipt that oracle digests and scores are authentic | C, B |
| **EVAL vs RUN** | Privileges: evaluation injects tests; run must not rewrite grader | C |
| **GRPO / PPO** | RL algorithms; Rebound shows reward hacking under GRPO when tests are mutable | C |
| **Held-out / SpecBench \(\Delta\)** | Val−heldout composition gap — **not** Cochran residual \(\Delta\) (don’t overload the name) | C |
| **LEGO-RL** | Stage-wise defenses: withhold tests, hide history, egress fence | C |
| **Oracle (sealed)** | Controller-owned scorer / tests; content-addressed **before** fork; never writable by searcher | C |
| **obj_digest / Objective.digest** | Hash of the frozen eval contract; mutation = **Epoch bump** | C, G, D |
| **ProRL Agent** | Rollout-as-a-service framing | C |
| **Rebound → Remedy** | Agents rewrite `run_tests()` under RL pressure; Remedy = systems binding | C · 2604.01476 |
| **Reward hack** | Optimize the proxy (visible tests) not the intent; School of Reward Hacks caution | C |
| **Search ≠ Authority** | Workers produce evidence; controllers own criteria / promote | C, G, NYC bridge |
| **SpecBench** | Frontier agents saturate visible validation while held-out gap grows | C · 2605.21384 |
| **Tree-GRPO** | Tree-structured RL on forked traces (Shepherd context) | A, C, H |

---

## D. Auto-research / HIL / promote tips

| Term | Meaning | Home |
|---|---|---|
| **AIDE² / RRSI / DGM / GEAR** | Harness / search-policy RSI papers — hill-climb *under* frozen eval | D |
| **AI Scientist / AutoResearchClaw** | Paper/HITL tip sociology — separate promote bit from harness RSI | D |
| **Auto-research** | Factory-of-factories under frozen eval + singular publication authority | D, G |
| **HIL** | Human/robot-in-loop; robot-hour as scarce tip | D |
| **Harness RSI** | Self-improve the searcher/harness, not the claim criterion | D |
| **Promote.compute vs Promote.tip** | Two-phase: accept artifacts under Epoch vs burn scarce tip (merge/robot/wet/paper) | D, G |
| **Scarce tip** | Merge token, robot hour, wet slot, paper/grant claim — burn once | D |
| **Universal hillclimb** | `propose → isolate → measure → keep/revert → promote` isomorphism | D, UNIVERSAL-HILLCLIMB |
| **Wet lab / clinic tip** | Irreversible physical authority spend | D |

---

## E. Credentials / WIRE / leases

| Term | Meaning | Home |
|---|---|---|
| **Blast radius** | Fork copies memory → secrets multiply across siblings | E |
| **Broker / gateway** | Holds real secrets; children see opaque handles only | E |
| **Capability (KeyKOS / seL4)** | Mint + revoke rights; pedigree for lease thinking | E, M |
| **Lease \(L\)** | Proposed \((id, principal, scope, B, TTL, \mathcal{L}, e, \sigma)\) | E |
| **Remint / reissue** | Default `secretInheritance: reissue` — fresh id, rights ⊆ parent, secret-disjoint | E |
| **Scrub** | Clear credential pages before child runnable (heat OK vs secret forbidden) | E, A |
| **WIRE** | Wire-time identity & rights for ephemeral explorers — leases, not ambient env keys | E |
| **WIRE epoch \(e\)** | Generation for cascade revoke on governed requests | E |

---

## F. Warm CoW / packing / channels

| Term | Meaning | Home |
|---|---|---|
| **CAS heat** | Content-addressed shared artifacts (safe to share across same pack) | F |
| **Co-residency** | Which sandboxes share a host / SMT / page cache | F |
| **Pack policy** | Place by trust pack key, not blind NUMA fill | F |
| **Prefetch profile / REAP / FaaSnap** | Serverless ancestors of restore-path warming — don’t inherit secret-trained profiles cross-tenant | F, A |
| **Structural CoW** | Honest shared pages via MAP_PRIVATE — not KSM cross-tenant | F |
| **Threat tier** | Policy input → KSM off, SMT pin, no shared exe maps, etc. | F |

---

## G. Factory API / capability contract

| Term | Meaning | Home |
|---|---|---|
| **Capability contract** | Named invariants (Search≠Authority, immutable S0, one promote bit/Epoch, structured evidence, burn-after-promote) — not inventory of every DAG tool | G |
| **Epoch** | Generation of frozen Objective / schedule / rights; digest mutation bumps Epoch | G, H |
| **Factory API** | `Fork, Reduce, Promote` (+ leases) as first-class operations | G |
| **Fork, Reduce, Promote** | Talk’s systems-API paper framing | G |
| **Immutable \(S_0\)** | Shared past / golden snapshot root pinned into children | G, A |
| **Path-integral CI** | Merge consumes **reduced measure**, not a green badge | G |
| **Promote sink** | Singular authority bit; absorbing boundary (I) | G, I, D |
| **World-diff** | Machine-state analogue of Git conflict = evidence | G |
| **swfactory / Cell** | Example thermostat + fence dual (Cell/epoch) | G, H |

---

## H. Annealing / MCMC / SGD (schedule dual)

| Term | Meaning | Home |
|---|---|---|
| **Anneal schedule** | Hot explore → cool reduce → \(T\to0\) promote → burn | H, B |
| **Detailed balance (honesty)** | Frozen energy \(E\) / Obj for an Epoch — **not** proof the factory equilibrated | H, I |
| **Exploration budget** | Authority-owned search allowance on Obj | H, G |
| **Langevin / Langevin-SGD** | Noisy gradient dynamics cousin of temperature schedules | H, I |
| **Metropolis–Hastings (MH)** | Propose in child; accept/keep or reject/revert under controller energy | H |
| **Simulated annealing (SA)** | Temperature schedule over proposals | H |
| **Temperature \(T\)** | Factory exploration knob (≠ reduce \(\beta\equiv n\)) — **two named knobs** | H, B |
| **Thermostat** | Who may set \(T\) / schedule — must be Epoch/authority, never worker | H |

---

## I. Non-equilibrium / Hamiltonian ontology

| Term | Meaning | Home |
|---|---|---|
| **Absorbing boundary** | Promote removes measure from the search swarm | I |
| **Driven system** | Continuous proposals, budgets, measurements — not closed | I |
| **Entropy production** | Irreversibility record (lineage + burns + tip spends) | I |
| **Fluctuation theorems** | Q&A-only; **refuse** second-law-for-CI / Jarzynski-on-stage | I |
| **Hamiltonian \(H(q,p)\)** | **Proposal generator** for isolated searcher — not the factory’s full dynamics | I |
| **NESS** | Non-equilibrium steady state — steady swarm at fixed Epoch \(T\) with continuous fork/burn | I |
| **Protocol \(\lambda(t)\)** | Finite-rate driven anneal / budget schedule (not quasi-static equilibrium) | I, H |
| **TUR (intuition)** | Thermodynamic uncertainty — precision costs dissipation; bridge to β≡n / cold-liar **as interpretation** | I |

---

## J / M. Practice landscape & next-gen VMM

| Term | Meaning | Home |
|---|---|---|
| **Cloud Hypervisor (CH)** | Rust VMM; VFIO GPU; UFFD restore; live migration — route-around FC thinness | M |
| **crosvm** | ChromeOS VMM; GPU-friendlier peer | M |
| **Diptanu (Gon Choudhury)** | Tensorlake founder/CEO; Nomad-era scheduler pedigree (speaker-note) | J |
| **gVisor** | Userspace kernel isolate — contrast thickness vs microVM | M |
| **Hafnium** | ARM TF type-1 static partition hypervisor — **not** agent fork factory (“HAFNION” ask) | M |
| **Hyper-V / OpenVMM** | Windows-strong VMM lane; OpenVMM = open Rust VMM | M |
| **Necessary but not sufficient** | Firecracker wall required; still need fork UX, WIRE, GPU lanes | M |
| **Nitro / SnapStart** | AWS control-plane / managed restore lineage related to FC story | M |
| **NVMM** | FreeBSD VMM family | M |
| **QEMU** | Full-device VMM; Windows/GPU/display unifier; postcopy UFFD | M |
| **wasm / wasmtime** | Capability isolate lane — not full OS world | M |
| **Youki** | Rust OCI runtime — inner container layer, not outer wall | M |

---

## K. Books / theory practice (pointer)

See `swarm/K-BOOKS-THEORY-PRACTICE.md` — top books/papers marked MAIN / speaker-note / do-not-cite. Prefer Feynman path-integral pedagogy over Everett on stage.

---

## L. Algos / frameworks split-merge (pointer)

See `swarm/L-ALGOS-FRAMEWORKS-SPLIT-MERGE.md` — MapReduce→Ray lineage; CRDT≠promote; Git≠world-diff; Airflow = authority spine not fork fabric; BSP barrier ≠ abstain-on-ρ.

| Term | Meaning | Home |
|---|---|---|
| **Airflow / tip spine** | Orchestration of scarce authority — not N-way CoW fork | L, G |
| **BSP barrier** | Bulk-sync then average — anti-pattern under unresolved ρ | L, B |
| **CRDT** | Convergent data merge ≠ singular Promote.tip | L |
| **Ray / CIEL / Spark lineage** | Task/actor / lineage ancestors of evidence-aware reduce | L |
| **Split-merge** | Fan-out then merge — owes Z/abstain/oracle/WIRE still | L |

---

## L–Z quick symbols

| Symbol / short | Gloss |
|---|---|
| **\(S_0\)** | Immutable shared past / golden root |
| **Epoch** | Frozen Obj + schedule generation |
| **\(\rho\)** | Sibling correlation under shared root |
| **\(\Sigma_g\)** | Pooled posterior covariance — don’t shrink on abstain |
| **\(\Delta\)** | Pool residual / Cochran Q (≠ SpecBench gap) |
| **\(Z_g\)** | Partition diagnostic |
| **\(\beta\)** | \(=n\) in Gaussian reduce |
| **\(T\)** | Exploration temperature (factory) |
| **WIRE** | Lease remint fabric |
| **MH / SA / SGD** | Schedule cousins |
| **NESS** | Driven steady swarm |
| **H** | Proposal Hamiltonian (metaphor) |
| **pack key** | Co-residency trust tuple |
| **Tree-GRPO** | Tree RL on forks |
| **world-diff** | State conflict as evidence |

---

## Forbidden conflations (glossary fence)

| Don’t confuse | With |
|---|---|
| Fork speed | Evidence independence |
| Firecracker pedigree | End of next-gen story |
| \(\beta\equiv n\) | Factory exploration \(T\) |
| \(Z_g\) | Bayesian model evidence |
| Cochran \(\Delta\) | SpecBench val−heldout \(\Delta\) |
| Escape wall | Evidence / oracle wall |
| vmgenid | API-key revoke / WIRE |
| Suspend | Snapshot / fork |
| Hafnium | Dense CoW microVM fork factory |
| Gibbs naming | Agents thermalize like magnets |

---

*Mega glossary · 2026-09-27 (IDT) · covers swarm A–M + physics companions*
