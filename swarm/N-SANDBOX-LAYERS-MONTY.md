# Researcher N — Sandbox isolation ladder + Pydantic Monty
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Classic isolation ladder (field-manual + EscapeBench) mapped onto Pydantic Monty’s language-level continuum; when Wasm/Docker suffice vs when a forkable microVM is required  
**Fence:** Monty = **language-level** sandbox (capability-from-nothing), **not** an EscapeBench substitute for untrusted OS agents. Field-manual ladder + EscapeBench motivate the **microVM outer wall**. Peer EscapeBench cites OK; Monty start-latency table from Pydantic article = **attributed, not Yossi ms**. Align `CLAIM-FENCE.md` + C’s escape wall ≠ evidence wall.  
**Spoken line:** “Start from nothing when the job is CodeMode Python; climb to a forkable microVM when the job is an untrusted OS agent — Monty is a rung, not the wall.”

---

## 0. Thesis (one breath)

Two ladders, one decision: **(1)** Yossi’s field-manual OS ladder (subprocess → namespaces → container → gVisor → microVM → full VM) answers *how thick is the escape wall*; **(2)** Pydantic Monty’s continuum (tool-call → Monty CodeMode → container sandbox services → coding agents → computer/desktop use) answers *how much ambient capability you grant the model*. EscapeBench says Docker-class shared-kernel walls fail against frontier agents — so **forkable microVM is the talk’s default outer wall** for untrusted OS bodies. Monty (and Wasm) win when the threat is *unreviewed Python that must not touch the host*, not *an agent with a shell inside a Linux guest*.

---

## 1. Classic ladder (field manual) — threat model per rung

Source of truth for the OS ladder: [The Sandbox Shift — sandboxes-why-how-when](https://zozo123.github.io/sandboxes-why-how-when/) (Yossi field manual) · repo [zozo123/sandboxes-why-how-when](https://github.com/zozo123/sandboxes-why-how-when).

| # | Rung | Boundary | Threat it holds | Threat it **fails** | Latency / density class |
|---|---|---|---|---|---|
| 0 | **No sandbox / `eval`** | Same process, ambient authority | None | Any adversarial / unreviewed code | µs; densest |
| 1 | **subprocess + limits** | Same kernel, same user; timeout/`ulimit` | Accidental hang / OOM of *trusted* helper | Escape, FS/net exfil, credential theft | ms; very dense |
| 2 | **namespaces · cgroups · seccomp** (nsjail, bubblewrap, Landlock) | Kernel fencing, still **shared kernel** | Semi-trusted code; accidental blast | Kernel CVE / misconfig → host | ms; dense |
| 3 | **container** (runc / containerd / Docker) | Shared kernel + OCI packaging | Trusted-human-authored workloads; portable deps | **SandboxEscapeBench** class: Docker socket, privileged, runc/kernel escapes | ~100 ms–s boot; dense |
| 4 | **gVisor** (`runsc`) | Userspace kernel / syscall intercept | Shrinks syscall attack surface vs runc | Still no separate guest kernel; not EscapeBench *substitute* for hostile OS agents | container ergonomics; dense |
| 5 | **microVM · Firecracker** (Kata/CH cousins) | **Hardware VM** + thin virtio; own guest kernel | Untrusted model-authored agents with shell/FS/tool use | Rare hypervisor/device bugs; side-channels under warm CoW (F) | ~100 ms boot class; thousands/host — **agent sweet spot** |
| 6 | **full VM · air-gapped** | Thick device model / offline | Genuinely hostile / regulated / no egress | Cost, boot, ops | slow / sparse |

**Mantra from the manual:** pick the *lowest* rung that holds the threat model; microVMs broke “VM-grade ⇒ slow.” Docker won DX, not isolation thickness — sandboxes win the same way (API + boot), **on top of** the right wall.

**Placement 2×2 (manual):** untrusted code × nothing-to-steal → public ephemeral box; untrusted × private data → inside VPC, scoped creds, deny-by-default egress. Talk’s fork factory usually sits in the second cell with a **microVM outer wall**.

---

## 2. EscapeBench angle — why the ladder has a hard floor for agents

| Bench | What it measures | Talk implication |
|---|---|---|
| **SandboxEscapeBench** (Oxford / AISI · [arXiv:2603.02277](https://arxiv.org/abs/2603.02277) · [AISI blog](https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities)) | Nested **container-in-VM** CTF: can frontier agents escape Docker/K8s via misconfig, runtime, kernel | Public scenarios saturating under newer models on **orchestration / runtime / kernel** classes → **NCSC-aligned hypervisor minimum** for untrusted agent bodies (C) |
| **AgentEscapeBench** ([safety-research/agent-escape-bench](https://github.com/safety-research/agent-escape-bench)) | Broader `(model × sandbox)` matrix: Docker, gVisor, Landlock, bwrap, nsjail, Firecracker, QEMU, Chromium, V8, Wasm… | Confirms ladder *families*; Firecracker/QEMU are the hardware walls; Wasm family exists but is a different ABI |

**Stage rule (with C):** EscapeBench measures **escape wall** failure of containers. It does **not** certify Monty, Wasm, or gVisor as drop-in replacements when the agent needs a real Linux toolchain. Docker remains fine as an *inner* layer (dropped caps) under a microVM outer wall — never as the sole outer wall for EscapeBench-class threat.

**Escape wall ≠ evidence wall:** even a perfect Firecracker still needs sealed oracles / attestation \(a_k\) (C) and WIRE remint (E). Isolation stops host compromise; it does not stop Rebound rewriting `run_tests()` *inside* the guest.

---

## 3. Pydantic Monty — what it is (and is not)

**Monty** = minimal secure Python interpreter written in Rust for AI-authored code ([docs](https://pydantic.dev/docs/monty/get-started/) · [security model](https://pydantic.dev/docs/monty/concepts/security/) · [Colvin article](https://pydantic.dev/articles/pydantic-monty) · [github.com/pydantic/monty](https://github.com/pydantic/monty)).

| Property | Fact | Fence |
|---|---|---|
| Isolation kind | **Language-level** bytecode VM (Ruff parser → Monty bytecode); **no** container, seccomp, or VM in open Monty | “Secure” ≠ EscapeBench wall |
| Ambient authority | **None** by default — no FS, env, net, spawn unless you opt-in mounts / host functions / `os=` | Capability-from-nothing (allowlist), opposite of “start full then lock down” |
| Crash isolation | Python / native JS: every session in `monty` **worker subprocess** (empty env); Wasm: browser `Worker` / Node worker_threads; Rust in-process crate = language sandbox **without** crash isolation | Subprocess ≠ microVM |
| Host reach | Only via (1) host functions, (2) `ClassInstance`/`ClassType` wrappers, (3) mounts + `os=` — all host-side, full host authority | **You** are the escape hatch if callbacks are sloppy |
| Fit | CodeMode / tool orchestration in a Python subset; µs–ms start; kB snapshots | **Poor** fit for pandas/notebooks/full CPython / bash / arbitrary toolchains |
| Full Monty (commercial) | WebSocket pool of Monty workers **plus** optional reverse-proxy to **real CPython in container/VM** | Remote CPython inherits **deployment** isolation, not Monty’s language guarantees |

**Continuum (Colvin article — left → right capability):**

```
tool calling  →  Monty (CodeMode)  →  sandbox services (E2B/Modal/…)  →  coding agents  →  full computer/desktop use
   more control ◄──────────────────────────────────────────────────────────────────────────► more capability
```

Monty sits *just right of tool calling*: the model writes Python that can loop/gather/transform, but every external effect is a host function you authored. That is **orthogonal** to the OS ladder — it is a *capability continuum*, not a thicker escape wall.

**Attributed latency table (Pydantic article — not Yossi benches):** Monty ~0.004 ms class · Docker ~195 ms · sandbox services ~1 s+ · Pyodide ~2.8 s. Quote as *their* numbers if spoken; never as Cambridge results.

---

## 4. Monty isolation tiers (REPL → process → Wasm → Docker → VM → computer)

Map Monty’s *deployment* modes onto the classic ladder. “Tier” here = where the interpreter / worker runs, not Monty’s language claim.

| Monty / continuum tier | Where code runs | Crash / escape claim | Maps to classic rung | When enough |
|---|---|---|---|---|
| **In-process REPL** (Rust `monty` crate embed; Wasm-without-Worker degrade) | Caller process | Language sandbox holds; **no** crash isolation; abort = your process | Below rung 1 | Trusted experiments only |
| **Worker subprocess** (`monty subprocess` / `monty-pool`; default Python & `@pydantic/monty`) | Sibling OS process, empty env, protobuf wire treated untrusted | Crash kills worker only; still **shared kernel** with host app | Rung 1 (+ language wall) | Untrusted *Monty-subset* Python beside your agent process |
| **Wasm + Worker** (`@pydantic/monty/wasm` in browser Worker; Node worker_threads) | Isolate / thread; hard terminate on trap | Language + soft crash fence; JS-engine / process OOM can still hurt host | Wasm family (AgentEscapeBench) ≈ thin isolate | Browser / edge CodeMode; no full Linux ABI |
| **Docker / container around Monty or Full-Monty CPython proxy** | OCI guest, shared host kernel | Packaging + some blast radius; EscapeBench applies to the *container* | Rung 3 | Need deps / bash / real FS **and** accept shared-kernel risk, or put container *inside* microVM |
| **microVM / Full Monty “full sandbox” VM** | Guest kernel (FC / CH / Kata…) | Hardware escape wall; Monty language guarantees **do not transfer** to remote CPython — deployment owns isolation | Rung 5 | Untrusted OS agent, RL eval body, SWE-bench world, any shell |
| **Coding agent / computer·desktop use** | Terminal + browser + mouse/keyboard | Maximal capability; control largely delegated; human-in-the-loop typical | Beyond ladder (workbench with keys) | Interactive high-capability; **not** autonomous EscapeBench-class outer wall by itself |

**Important Monty doc caveat:** `AsyncMontyWebsocket` / remote workers may speak to **real CPython with no sandbox** — isolation becomes “whatever container/VM you deployed.” Do not cite Monty’s security page for that path.

---

## 5. Decision table — Wasm / Docker enough vs forkable microVM required

| Workload | Author | Needs full Linux / bash / pip / GPU? | Secrets / VPC data? | Recommended outer | Monty role |
|---|---|---|---|---|---|
| Tool orchestration / CodeMode glue | LLM Python subset | No | Host functions only | **Monty worker** (± Wasm in browser) | **Primary sandbox** |
| Deterministic transforms, gather, typed stubs | LLM | No | None ambient | Monty | Primary |
| Notebook / pandas / arbitrary PyPI | LLM or human | **Yes** | Often | Container **or** microVM (threat-dependent) | Poor fit — use CPython guest |
| SWE-bench / coding agent with shell | Untrusted agent | **Yes** | Repo + maybe creds | **Forkable microVM** (FC/CH) + WIRE remint | Optional *inner* CodeMode tool, not outer wall |
| RL / eval rollouts at density | Untrusted bodies | Usually yes | Oracle digests outside | **microVM** + sealed oracle (C) | CodeMode scorer glue only if subset fits |
| Multi-tenant agent cloud | Hostile-capable | Yes | Tenant isolation | microVM + pack-by-trust (F) | Not a substitute |
| Browser side-panel agent | LLM | No native ABI | Page-scoped | **Wasm Monty Worker** | Primary |
| “Computer use” desktop | LLM + human | Desktop | Everything | Product policy + human; not EscapeBench wall alone | N/A |

### When **Wasm / Monty / Docker** are enough

- Threat = *unreviewed Python that must not open sockets/files* — capability-from-nothing holds.
- No need for real CPython ecosystem, bash, compilers, or arbitrary binaries.
- Crash isolation via worker/Wasm is acceptable; shared kernel with the **host app** is acceptable (Monty is not defending against a guest root).
- Docker enough when: human-trusted or low-stakes packaging, **or** Docker is the *inner* layer under a VM.

### When a **forkable microVM is required**

- Threat = EscapeBench-class: agent with **shell + FS write** motivated to leave the box.
- Need reproducible **full OS worlds** (SWE / RL / multi-tool) that Monty’s subset cannot express.
- Need **N-way warm CoW fork** (DeltaBox/Crab/forkd/Tensorlake) — Monty snapshots are kB interpreter state, **not** guest MEM/FS CoW siblings for MCTS/BoN.
- Multi-tenant or secret-bearing VPC workloads where a kernel CVE is unacceptable.
- Talk’s default for “untrusted agent body” (C + field manual sweet spot).

**One-liner for slides:** *Monty/Wasm = start-from-nothing CodeMode. Docker = portable inner world. Forkable microVM = EscapeBench outer wall + factory fan-out.*

---

## 6. Dual-ladder sketch (stage / Q&A)

```
Capability continuum (Monty article)          Escape / OS ladder (field manual)
───────────────────────────────               ────────────────────────────────
tool call ─► Monty ─► sandbox svc ─► agent ─► desktop
                │                         │
                │ language wall           │ shared kernel
                ▼                         ▼
         worker / Wasm               container / gVisor
                                          │
                                          ▼  EscapeBench floor
                                     microVM (Firecracker…)  ◄── talk default outer wall
                                          │
                                          ▼
                                     full VM / air-gap

Compose pattern (recommended):
  [controller + sealed oracle + WIRE]  outside
       └── microVM guest (forkable)
              ├── optional Docker/inner tools
              └── optional Monty CodeMode *as a tool* (not the wall)
```

---

## 7. Claim fence (N-specific)

| DO | DO NOT |
|---|---|
| “Monty is a **language-level** sandbox — capability from nothing.” | “Monty replaces Firecracker / passes EscapeBench.” |
| Cite field-manual ladder + EscapeBench for **outer wall** choice | Equate Wasm or gVisor with KVM microVM for hostile OS agents |
| “Docker OK as **inner** layer; microVM as **outer** for untrusted agents.” | “Containers are fine outer walls now that models are smarter.” |
| Monty start-left / grant-right continuum as **CodeMode** story | Claim Monty supports full stdlib / third-party wheels |
| Full Monty remote CPython = **deployment** isolation | Transfer Monty security-page guarantees across Websocket→CPython |
| Forkable microVM when you need OS worlds + CoW fan-out | Claim Monty kB snapshots = warm guest MEM forks |
| Escape wall ≠ evidence wall (with C) | “Thicker sandbox ⇒ Rebound-proof” |

**Vendor / eng ms:** Monty article table = attributed verbal OK. forkd/Tensorlake/E2B = verbal landscape (A/M fence). Peer EscapeBench / DeltaBox / Crab / Shepherd = attributed.

---

## 8. Challenges / handoffs

| → | Ask |
|---|---|
| **C** | Confirm EscapeBench floor wording: Docker inner OK, microVM outer mandatory for shell agents; Monty not on the EscapeBench substitute list. |
| **A** | Monty interpreter snapshots ≠ DeltaState / MEMORY snaps — keep snapshot taxonomy clean so N doesn’t smuggle “fork” language onto CodeMode pause/resume. |
| **E** | Host-function callbacks run with **host** authority — WIRE must treat Monty external_lookup as a credential surface (validate args; no ambient keys in worker env already empty, but host process still holds secrets). |
| **G** | Should `World.fork` expose a `isolate_tier` enum (`monty|wasm|container|microvm|…`) so the capability contract names the rung, fail-closed like h5i? |
| **M** | Agree: Monty/Wasm sit in M’s “thinner isolates (contrast)” bucket; Full Monty CPython-in-VM is a *compose* with FC/CH, not a VMM competitor. |
| **J** | Product CodeMode-inside-MicroVM = practice proof of compose pattern without vendor bake-off. |

---

## 9. Glossary pointer

Short terms live in `scratch/GLOSSARY-ALL-TERMS.md` § **N. Isolation ladder / Monty**. Deep biblio stays here + K.

---

## 10. URL dump

- Field manual: https://zozo123.github.io/sandboxes-why-how-when/  
- Field manual source: https://github.com/zozo123/sandboxes-why-how-when  
- Monty get-started: https://pydantic.dev/docs/monty/get-started/  
- Monty security model: https://pydantic.dev/docs/monty/concepts/security/  
- Monty article (continuum + latency table): https://pydantic.dev/articles/pydantic-monty  
- Full Monty commercial server: https://pydantic.dev/docs/monty/commercial-support/server/  
- Pool / remote CPython caveat: https://pydantic.dev/docs/monty/limitations/pool-architecture/  
- pydantic/monty: https://github.com/pydantic/monty  
- SandboxEscapeBench: https://arxiv.org/abs/2603.02277  
- AISI EscapeBench blog: https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities  
- AgentEscapeBench: https://github.com/safety-research/agent-escape-bench  
- h5i tier ladder (cousin policy model): https://h5i.dev/blog/sandboxing-ai-agents-h5i/  

---

*Researcher N · 2026-09-27 (IDT) · Cambridge SRG swarm*
