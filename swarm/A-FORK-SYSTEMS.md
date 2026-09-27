# Researcher A — Fork / Systems (CoW, snapshot, side-channels)
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** DeltaBox · Crab · Shepherd · Firecracker NSDI’20 · Xu–Kaffes · OpenRath · forkd/Mitos/Tensorlake landscape  
**Fence:** Cite peer systems as *related*, not owned. Vendor/eng latencies = speaker-note only. Align with `PAPERS-AND-SOURCES.md` claim fence + `PARALLEL-WORLDS-STATPHYS.md` (fork = parallel world; CoW siblings ≠ independent evidence).

---

## 1. Top-8 systems claims (Cambridge routing)

| # | System | Peer URL | One-line claim | Cite on slide? | Speaker-note only |
|---|---|---|---|---|---|
| 1 | **Firecracker** — Agache et al., NSDI’20 | https://www.usenix.org/conference/nsdi20/presentation/agache | Canonical microVM isolation + snapshot pedigree; MAP_PRIVATE CoW memory load is the industry fork substrate every agent sandbox cites. | **MAIN** pedigree | Do not invent “we invented VMs”; restore latency is kernel/cgroup-sensitive (docs: prefer cgroups v2). |
| 2 | **DeltaBox** — Dong, Du, Xia, Chen et al. | https://arxiv.org/abs/2605.22781 | Change-based coupled FS+process C/R on Firecracker: **~10.83 ms** ckpt work (hidden under LLM wait) / **~1.86 ms** fast-path restore; SWE-bench MCTS + RL fan-out. | **MAIN** (pick vs Crab) | “How-fast / what-to-diff” twin. Table 1 baselines (E2B, FC-Diff, Docker commit) are *their* measurements — quote as comparative, not yours. |
| 3 | **Crab** — Wu, Chang, Cao, Gao, Wang (HKUST) | https://arxiv.org/abs/2604.28138 | Semantics-aware C/R: eBPF net-change skips **≤87%** of turns; turn-aligned, LLM-wait overlap; **100%** recovery correctness vs 8–13% chat-only; ≤**1.9%** overhead vs fault-free. | **MAIN** (pick vs DeltaBox) | “What/when to checkpoint” twin — complementary to DeltaBox’s OS primitives (both papers say so). |
| 4 | **Shepherd** — Yu, Chong, Manning, Shi et al. | https://arxiv.org/abs/2605.10913 | Agent+env as reversible Git-like effect trace; `scope.fork()` **134–143 ms**, ~**5×** faster than docker commit; Tree-GRPO + supervisor + CRO. | **MAIN** meta-agent | Not a ms-OS paper — programmable *fork/revert/merge* API for meta-agents. Lean mechanizes effect fragments, **not** Docker/sandbox correctness. |
| 5 | **Xu–Kaffes** — Toward Systems Foundations for Agentic Exploration | https://arxiv.org/abs/2510.05556 | Names the open agenda: **fork semantics**, **external side-effects**, **native CoW fork** (µs, not seconds). Generic CRIU/Docker/AWS-VM fail interactive exploration. | BACKUP→MAIN if “foundations” slide | Frame talk as *answering* this agenda. Their Table 1 = diagnostic, not production APIs. |
| 6 | **OpenRath** — Wen, Wang, Xu | https://arxiv.org/abs/2606.19409 | **Session** = first-class branchable/inspectable/replayable runtime value (placement + lineage + tool evidence). PyTorch-like `forward(session)→session`. | BACKUP | Complements Shepherd on *what object flows*; claims scoped to deterministic packets, not leaderboard latency. |
| 7 | **Catalyzer / REAP / FaaSnap** (serverless ancestry) | Catalyzer ASPLOS’20 · REAP arXiv:2101.09355 · FaaSnap EuroSys’22 | `sfork` / userfaultfd prefetch / concurrent paging — ancestors of agent restore economics. | Pedigree footnote | Serverless unit = *invocation*, not in-trajectory backtrack (DeltaBox §7). |
| 8 | **Landscape: forkd / Mitos / Tensorlake** | forkd GitHub · mitos-run · docs.tensorlake.ai | Eng/product: warm-parent CoW fan-out; Tensorlake `FILESYSTEM` vs `MEMORY` snapshot types; clone ≈ memory ckpt + create. | **BACKUP name-once** | **High claim-risk.** Demo numbers (forkd ~100 children/~100 ms; BRANCH ~150 ms) ≠ peer benchmarks. Never put on slide as “our numbers.” |

**Deck rule (≤5 total cites):** Firecracker + (DeltaBox **xor** Crab) + Shepherd + Boltzmann MapReduce (2607.09689) + (SWE-bench **or** Rebound→Remedy). OpenRath / Xu–Kaffes / landscape = verbal Q&A.

---

## 2. Contrast: DeltaBox vs Crab vs Shepherd — WHAT / WHEN

| Axis | **DeltaBox** (2605.22781) | **Crab** (2604.28138) | **Shepherd** (2605.10913) |
|---|---|---|---|
| **Primary question** | How to make *full* coupled C/R millisecond-cheap? | *Whether / what* to checkpoint per turn? | What *API object* lets a meta-agent fork/revert/rewrite execution? |
| **WHAT snapshotted** | Atomic **(FS, process mem)** = `DeltaState`. DeltaFS: freeze overlay upper → new CoW upper (+ XFS reflink). DeltaCR: CRIU image **and** warm **template process** (`fork()`). | **Adaptive granularity:** skip / FS-only (ZFS) / process-only (CRIU) / full — from eBPF+soft-dirty **net-change** since last ckpt. Manifest \(C_i=(P_j,F_k)\). | **Typed effect stream** + **scope** (sandbox handles, providers, tools, cursor). Fork = atomic CoW of FS+processes+bindings. Intent≠outcome events. |
| **WHEN** | Every MCTS / search node: `deltaCheckpoint` concurrent with LLM wait; `deltaRestore` on backtrack (critical path). RL: `fork_n` from one warm template. | **Turn boundaries** only (Coordinator proxies agent↔LLM). Skip if no recovery-relevant net change (≤87%). Gate LLM response until ckpt durable. | **Meta-agent policy:** before risky write; at chosen RL fork turn \(t\); on CRO edit’s first affected commit; supervisor inject/handoff/discard. |
| **Restore semantics** | Kill active agent → overlay stack switch → template `fork()` (fast) or CRIU lazy-pages (slow). Resume at instruction after ckpt. | ZFS rollback ± CRIU load to published manifest. Agent-in-sandbox: **fast-forward** cached turns if process older than FS. | `checkout` commit → byte-identical agent+env; `discard` leaves parent untouched; replay suffix under new handler. |
| **CoW sharing** | Yes: pages shared template↔child; FS via overlay+reflink. Async-warm pre-pays CoW faults off critical path. | ZFS block CoW for FS; process dumps typically **not** live-shared across siblings (restore reconstitutes). | Overlay deltas share prefix by content hash; K branches pay divergent suffixes. |
| **Peer latency (quote as theirs)** | ckpt **10.83 ms** local / agent-perceived **0** under LLM; restore **1.86 ms** fast / **9.29 ms** slow. Fan-out p50 **0.57→5.47 ms** for N=1→64 kernel forks (Table 3). | Exposed ckpt delay median **0** (hidden in LLM wait); p95 **0.44%** task time @64 density. FS ckpt ~20–100 ms; process ~700–1000 ms. E2E ≤**1.9%** over no-fault. | Fork **134–143 ms**, revert **140–147 ms** across 42 MB–5.8 GB images (~5× docker commit ~658–725 ms). |
| **Isolation wall** | Firecracker microVM + custom guest 6.8 kernel (DeltaFS module). Multi-agent per VM possible (process-level C/R). | Host-side over **runc + CRIU + ZFS** (container density). Transparent — no agent rewrite. | Device-layer over Docker OverlayFS / E2B / Modal / Daytona; ~95% KV-cache hit on forked LLM prefixes. |
| **Side-effect honesty** | **NPD** keeps LLM sockets out of forkable address space. Explicit: *“does not currently support network I/O rollback.”* | Spot migrate / speculative fork / TreeRL case studies; external APIs still outside C/R. | Reversibility tiers: reversible / compensable / **irreversible** (model calls, email) — record-only. |
| **Talk framing** | Closest systems twin to “fork is the API” at OS speed. | Complements: sparsity + scheduling under co-location. | Academic twin of Controllable fork + promote + Tree-RL. |

**One spoken line:** “DeltaBox makes every checkpoint cheap; Crab makes most checkpoints unnecessary; Shepherd makes the checkpoint a value a meta-agent can hold.”

---

## 3. Peer-published numbers vs engineering blogs

| Source class | Examples | Stage rule |
|---|---|---|
| **Peer / venue (low risk)** | Firecracker NSDI’20; DeltaBox 2605.22781 Tables 1–4; Crab 2604.28138 Figs 12–18; Shepherd 2605.10913 Table 3; Xu–Kaffes 2510.05556 Table 1 (diagnostic); Catalyzer/REAP/FaaSnap | On-slide OK when attributed. Prefer “authors report…” |
| **Strong arXiv, med risk** | OpenRath 2606.19409 (scoped packets, not ms claims); SandboxEscapeBench 2603.02277 (escape threat → microVM wall) | Cite for semantics / threat model, not latency contests. |
| **Engineering / vendor (high risk)** | forkd README (~100 kids/~100 ms; BRANCH ~150 ms / live ~56 ms p50); Mitos CRDs; Tensorlake docs (`FILESYSTEM` vs `MEMORY`, `tl sbx clone`); E2B “~4 s/GiB” pause; CubeSandbox vendor p95; Daytona marketing | **Speaker-note / hallway only.** Name once as landscape. Never equalize with peer tables. |
| **Yossi artifacts** | islo.dev; zozo123 field manual; boltzmann-mapreduce | Own numbers only from *your* artifact tables. |

**Xu–Kaffes diagnostic (peer, seconds-scale):** CRIU 2 GiB ≈ 1.445 s; Docker 2 GiB disk ≈ 6.9 s; AWS-VM hundreds of seconds — motivates native fork, not “use Docker commit for MCTS.”

---

## 4. Snapshot types taxonomy (for SRG diagram)

| Type | Captures | Restore | Who |
|---|---|---|---|
| **FS-only** | Files / overlay / ZFS | Cold process restart or replay | Crab FS-only; Tensorlake `FILESYSTEM`; Git stash foil |
| **Process / memory** | Address space (+ optionally paired FS) | Resume mid-execution | CRIU; DeltaCR; Crab process; Tensorlake `MEMORY` |
| **Full VM** | Guest RAM + devices (± separate block snap) | MicroVM resume | Firecracker snapshot; E2B pause; FC-Diff+dm |
| **Change-based / delta** | Inter-ckpt diffs only | Layer switch + template fork | **DeltaBox** DeltaFS+DeltaCR |
| **Semantics-selective** | Net-change subset at turn boundary | Manifest compose | **Crab** |
| **Effect-trace / Session** | Typed events + lineage + placement | Checkout / replay / merge | **Shepherd** commits; **OpenRath** Session |
| **Warm-parent CoW fan-out** | Parent mem image `mmap(MAP_PRIVATE)` | N children share until dirty | **forkd / Mitos / Tensorlake clone** (eng) |

---

## 5. Side-channels & credential-on-fork gaps (honest open problems)

1. **Warm shared pages as covert channels.** CoW / KSM / MAP_PRIVATE density ↔ confidentiality understudied in agent papers (security community separate). Density claims ≠ isolation claims.
2. **Credential / identity refresh.** Peer literature thin. Product surfaces (islo gateway, mitos handshake) mention fresh entropy; **no peer lease model** for WIRE after CoW. forkd DESIGN: relies on **vmgenid** CRNG reseed + fresh TSC offset; still must isolate MAC/IP via per-child netns — template inheritance breaks without it.
3. **External side-effects (Xu–Kaffes).** Sockets, cloud APIs, DB sessions: restoring invalidates remote peer state. DeltaBox NPD = local workaround for LLM I/O, not general fork-aware services. Shepherd marks irreversible effects; does not make them reversible.
4. **Network I/O rollback.** DeltaBox: unsupported. Crab speculative/spot: checkpoint host state, not remote. Open problem for WIRE door.
5. **Execution independence ≠ evidence independence.** Fast CoW siblings share model/prompt/repo/ancestor → ρ>0 (B’s Eq. 1). Systems optimize *execution* independence; reduce must not treat N as i.i.d. (see Challenges → B).

---

## 6. Landscape sketch (BACKUP, one slide max / verbal)

```
Firecracker (NSDI'20) ── pedigree wall
        │
   ┌────┴────┬────────────┬──────────────┐
   │         │            │              │
DeltaBox   Crab      Shepherd/OpenRath   Eng: forkd·Mitos·Tensorlake
(how-fast) (what/when) (API object)      (product CoW fan-out)
   │         │            │              │
   └──── coupled FS+mem ──┴── Session/Trace ──┘
                    │
            Xu–Kaffes open agenda
         (semantics · side-effects · native fork)
```

Tensorlake API note (docs, not peer): `checkpoint(FILESYSTEM|MEMORY)`; `clone` = memory ckpt + create; MEMORY bakes CPU/RAM into snapshot. Useful for parallel-worlds diagram; **not** a latency cite.

---

## 7. Challenges to B / C / E (and F)

### → B (Reduce / StatPhys)
- **No peer ρ measurement under CoW.** DeltaBox/Crab/Shepherd publish *latency* and *correctness*, not pairwise correlation of sibling estimates sharing a warm parent. Until an overlap model exists, reduce should treat `same snapshot root ∈ ℒ` as **unresolved ρ** and **abstain from narrowing Σ_g** (or inflate variance), not pretend N i.i.d.
- **Lineage is logged, not calibrated.** Shepherd commits / OpenRath Session / DeltaBox snapshot index tree give you \(ℒ_k\) — they do **not** give \(\hat\rho\). Your paper owns the reduce; we own emitting honest lineage + placement tags in \(m_k\).
- **Ask:** What minimal systems telemetry (shared-page dirty fraction? prompt-hash? gold-file digest?) would let you upgrade from “abstain” to a conservative \(\rho\) prior without claiming Gibbs nature?

### → C (Oracle / Escape)
- **Oracle must leave the forked body.** Rebound→Remedy / SpecBench: agents rewrite evaluator tests *inside* the env. Coupled C/R that restores FS+mem will cheerfully restore a *tampered* oracle if the scorer lives in-sandbox.
- **Credential-on-fork is a C∩A gap.** After CoW, inherited tokens/sockets are a WIRE hazard. Demand: controller-issued **short leases** + forced re-handshake on fork; vmgenid-class entropy is necessary but not sufficient for API keys.
- **Escape wall ≠ evidence wall.** SandboxEscapeBench motivates Firecracker-class ESCAPE; it does not stop a child from minting forged \((J_k,n_k)\) into the reduce. Bind oracle digests **outside** DeltaState/Session mutability.

### → E (Credentials / WIRE)
- **Fork copies memory; authority must remint.** Ambient keys/cookies/TLS tickets inside a warm parent become N× blast radius. Demand: opaque lease handles in guest; secrets only in broker *outside* DeltaState/Session. Align with your \(L=(\mathit{id},\mathit{principal},\mathit{scope},B,\mathit{TTL},\mathcal{L},e,\sigma)\) + `secretInheritance: reissue`.
- **Scrub classification (A’s answer to your →A).** Heat OK to share: language runtime, pip/conda layers, compile caches, model weights. Secret-forbidden: env credential pages, SDK token caches, cookie jars, SSH agents, TLS session tickets, memfd-backed secret stores. **Default posture until measured:** treat entire guest credential surface as dirty → drop sockets + scrub + remint before child runnable. No peer paper yet bounds scrub≪ms fork (DeltaBox 1.86 ms / Shepherd ~140 ms) — that cost is *your* missing measurement paper, not ours to invent.
- **vmgenid ≠ WIRE.** forkd DESIGN correctly reseeds CRNG/TSC on restore; that does **not** revoke inherited API keys. Compose: Firecracker wall + remint + controller-only promote/oracle leases.
- **Self-fork side channel.** In-guest `Fork()` that inherits secrets bypasses audit — require broker materialization even for agent-initiated BRANCH (ties to Shepherd scope.fork + your audit ledger).

### → F (Warm CoW side-channels) — cross-check
- Structural CoW / page-cache / KSM channels are F’s beat; A supplies mechanism taxonomy only. Do not disable density rhetoric without F’s placement policy (templates vs live tenant pages).

---

## 8. Slide / speaker checklist

**On slide:** Firecracker pedigree · DeltaBox *or* Crab ms/sparsity · Shepherd fork-as-value · (optional) Xu–Kaffes three gaps.  
**Spoken:** “Parallel world with shared past; promote is world-selection.”  
**Never:** forkd/E2B/Daytona numbers as peer; “we invented snapshot”; Gibbs-ensemble claim; HIL as systems result.

---

*Researcher A deep pass 2026-09-27 IDT. Primary: arXiv abs/HTML for 2605.22781, 2604.28138, 2605.10913, 2510.05556, 2606.19409 + Firecracker snapshot docs + forkd DESIGN.md (eng only).*
