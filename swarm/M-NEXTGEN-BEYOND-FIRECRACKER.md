# Researcher M — Next generation beyond Firecracker
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Firecracker as *necessary pedigree, not sufficient end-state* for agent fork factories; candidacy map for VMM / isolate / product lanes  
**Fence:** Firecracker = MAIN pedigree (do **not** trash). Vendor / eng ms = **BACKUP verbal only**. Peer DeltaBox/Crab/Shepherd numbers OK attributed. Align `CLAIM-FENCE.md` + A’s number fence.  
**Spoken line:** “Firecracker is necessary but not sufficient — the wall we stand on, not the whole factory.”

---

## 0. Thesis (one breath)

Firecracker (Agache et al., NSDI’20) solved **dense, fast, hardware-isolated microVMs** for serverless. Agent **fork factories** need that wall **plus**: dense warm CoW fan-out, honest memory-snapshot UX, credential remint (WIRE), GPU/Windows lanes where needed, and control-plane fork semantics (reduce/promote live *outside* the VMM). Next-gen work either **evolves on the pedigree** (DeltaBox/Crab/forkd/Mitos/Tensorlake) or **routes around** FC’s deliberately thin device model (Cloud Hypervisor, QEMU, crosvm/libkrun, gVisor+CRIU, wasm).

---

## 1. Firecracker as pedigree — what it solved

| Solved (NSDI’20 + production line) | Why agents still cite it |
|---|---|
| **Hardware isolation** (KVM + minimal virtio device set) | Escape wall vs Docker-class shared kernel (SandboxEscapeBench → microVM minimum) |
| **Density + overcommit** | Memory ballooning / sparse restore; many guests per host |
| **Fast boot + snapshot/restore** | MAP_PRIVATE / on-demand page-in (userfaultfd handlers documented upstream) |
| **Attack-surface minimalism** | ~5 virtio devices (net, block, vsock, serial, i8042); no PCI by design |
| **Production pedigree** | AWS Lambda / Fargate lineage; open Firecracker; SnapStart family stories |

**Sources:** [USENIX NSDI’20 Agache](https://www.usenix.org/conference/nsdi20/presentation/agache) · [Firecracker snapshot docs](https://github.com/firecracker-microvm/firecracker/blob/main/docs/snapshotting/snapshot-support.md) · [UFFD page-fault resume](https://github.com/firecracker-microvm/firecracker/blob/main/docs/snapshotting/handling-page-faults-on-snapshot-resume.md)

**Stage rule:** Firecracker = **MAIN pedigree cite #1**. Never “we invented microVMs.”

---

## 2. What Firecracker lacks for agent *fork factories*

Honest gaps — **insufficiency, not failure**:

| Gap | Why fork factories care | Status / evidence |
|---|---|---|
| **Dense warm fork UX** | Agent MCTS/RL wants N siblings from one warm parent in ms, CoW-shared, with FS+mem consistency | Stock FC snapshot/restore is **VM-granularity**; Diff snapshots long in preview; multi-resume of one snapshot insecure without uniqueness (docs). Peer: DeltaBox shows FC Diff baselines **hundreds of ms–1.5 s** vs process-level template fork **~ms** ([2605.22781](https://arxiv.org/abs/2605.22781) Table 2) |
| **GPU / PCIe** | Tool-use agents that need CUDA/ROCm inside the sandbox | **Deliberately omitted.** Community PCIe PoC existed; GPU/PCIe work **paused** (resources + pinned memory vs overcommit conflict). Track: [Discussion #4845](https://github.com/firecracker-microvm/firecracker/discussions/4845), [#849](https://github.com/firecracker-microvm/firecracker/issues/849) |
| **Memory snapshot UX for agents** | FILESYSTEM vs MEMORY (Tensorlake ontology); mid-flight process resume; template pools | FC gives full-guest RAM dumps; agent-relevant state is a **subset** — DeltaCR template/`fork()` is the evolution **on** the wall |
| **Credential / identity story** | Fork copies memory → N× blast radius for keys/cookies/TLS | FC gives isolation + vmgenid-class entropy hooks in some stacks; **not** a WIRE lease algebra (E’s agenda) |
| **Windows guests** | Some agent desktops / enterprise tools | Linux-first microVM; Windows → Hyper-V / OpenVMM / QEMU lanes |
| **Live migration** | Drain hosts, sticky warm pools, cross-node clone | Not FC’s design center; Cloud Hypervisor / QEMU stronger here |
| **Host share / virtio-fs ergonomics** | Mount workspace into sandbox without bloating device model | FC rejects host-share devices by minimalism; libkrun / CH / QEMU often preferred for `--mount` |
| **macOS / HVF** | Local agent sandbox on Apple Silicon | FC is Linux/KVM; libkrun / Parallels / QEMU HVF fill the gap |

**Spoken recovery:** “Necessary wall. Not the fork API, not the GPU lane, not the lease model.”

---

## 3. NEXT GEN candidates (with sources)

### 3.1 Evolution **ON** the Firecracker pedigree

| Candidate | What it adds | Sources | Slide? |
|---|---|---|---|
| **DeltaBox** (Dong et al.) | Change-based coupled **FS+mem** C/R *inside* FC guest: DeltaFS layer switch + DeltaCR template `fork()`; peer **~14 ms ckpt / ~5 ms restore** (Table 1 means); FC Diff as baseline | [arXiv:2605.22781](https://arxiv.org/abs/2605.22781) | **MAIN** (with A) |
| **Crab** (Wu et al.) | Semantics-aware *what/when* to checkpoint (eBPF net-change skips ≤87% turns); ≤1.9% overhead; complements DeltaBox’s how-fast | [arXiv:2604.28138](https://arxiv.org/abs/2604.28138) | **MAIN** xor DeltaBox |
| **forkd / Mitos** | Warm-parent CoW fan-out control plane on FC; CoW-aware metering; bin-pack by shared template; husk pod path | [mitos-run/mitos](https://github.com/mitos-run/mitos) · [metering docs](https://mitos.run/docs/metering) · [scheduling.md](https://github.com/mitos-run/mitos/blob/main/docs/scheduling.md) | BACKUP landscape |
| **Tensorlake** (Diptanu Gon Choudhury) | Product MicroVMs (FC / Cloud Hypervisor) + Lattice scheduler + versioned FS; `FILESYSTEM` vs `MEMORY` snapshots; clone/suspend | [tensorlake.ai](https://www.tensorlake.ai/) · [docs snapshots](https://docs.tensorlake.ai/sandboxes/snapshots) · [Suspend vs snapshot](https://www.tensorlake.ai/blog/suspend-vs-snapshot) · J’s note | BACKUP landscape |
| **E2B / Daytona / islo** (eng) | Managed FC sandboxes; pause/resume economics | Product docs | Verbal only |

### 3.2 VMM peers that **route around** FC thinness

| Candidate | Isolation | Fork / snapshot story | GPU / Windows / migrate | Open vs product | Sources |
|---|---|---|---|---|---|
| **Cloud Hypervisor** | KVM (+ MSHV); rust-vmm cousin of FC | Snapshot/restore; **userfaultfd demand-paged restore** (`memory_restore_mode`); sparse mem files; live migration (multi-TCP); paused migrate | **VFIO / iommufd** GPU path; no macOS | Open (LF / Intel lineage) | [CH v52 release](https://www.cloudhypervisor.org/blog/cloud-hypervisor-v52.0-released/) · [Depot CH vs QEMU](https://depot.dev/blog/differences-between-qemu-and-cloud-hypervisor) |
| **crosvm** | ChromeOS / Android virt; KVM | Snapshot efforts in Chromium virt stack; GPU virtio-gpu / Venus interest | Stronger GPU story than FC | Open (Google) | Chromium `crosvm` docs / tree |
| **QEMU (+ microvm + userfaultfd)** | Broadest device model | `migrate`/`savevm`; postcopy + **userfaultfd**; dm-snapshot FS coupling (used as CubeSandbox/CH baselines in DeltaBox) | VFIO, vGPU, Windows, display | Open | QEMU docs; DeltaBox CHV+dm baseline |
| **libkrun** (+ **krucible** fork) | Embeddable VMM; KVM + **HVF (macOS)** | Upstream: snapshot RFC in flight / HVF capture; **krucible** adds pause/snapshot/fork as first-class | virtio-gpu path evolving; macOS native | Open (+ community fork) | [libkrun #748](https://github.com/libkrun/libkrun/issues/748) · [krucible engine](https://bhatti.sh/docs/under-the-hood/engine/) |
| **Kata Containers** | K8s RuntimeClass → QEMU / FC / Cloud Hypervisor | Warm pools offset VM start; not itself a ms CoW fork API | Backend-dependent | Open | [agent-sandbox Kata](https://agent-sandbox.sigs.k8s.io/docs/use-cases/kata-containers-isolation/) · [Zylos survey](https://zylos.ai/research/2026-04-04-ai-agent-sandboxing-security-isolation/) |
| **OpenVMM** (Microsoft) | Rust VMM; Hyper-V / WHP / KVM backends; paravisor mode | Snapshot/migrate evolving with Hyper-V lineage | **Windows guest** lane; GPU via Hyper-V stack | Open (announced ~2024–25) | [OpenVMM Project](https://techcommunity.microsoft.com/blog/windowsosplatform/the-openvmm-project/4547237) |
| **Hafnium** (“HAFNION” ask) | ARM Trusted Firmware **type-1** hypervisor; static partitions | **Not** an agent fork factory — boot-time security domains, not dense CoW clone | N/A for MCTS fan-out | Open (TrustedFirmware) | [Hafnium architecture](https://hafnium.docs.trustedfirmware.org/) |
| **NVMM** | FreeBSD native VMM | Snapshot/migrate in bhyve/NVMM family; niche for agent clouds | Limited agent ecosystem | Open (FreeBSD) | FreeBSD handbook / NVMM |
| **AWS Nitro vs Firecracker / SnapStart** | Nitro = AWS silicon+hypervisor control plane; FC = open microVMM used *inside* Lambda story; SnapStart = managed snapshot restore for Java/etc. | SnapStart = **product lineage** of “restore warm state,” not a public fork API | GPU = separate Nitro/Inferentia lanes | Nitro proprietary; FC open; SnapStart product | AWS Open Source FC announce; Lambda SnapStart docs |

### 3.3 Non-VMM / thinner isolate lanes (contrast)

| Candidate | Isolation thickness | Fork story | Role in talk |
|---|---|---|---|
| **gVisor (`runsc`)** | Userspace kernel / syscall intercept — **no** separate guest kernel | CRIU-style process C/R; Modal-class GPU memory snapshots in some stacks | Contrast: denser / no KVM; EscapeBench still prefers hypervisors for untrusted agents |
| **gVisor + Triton?** | Inference serving (Triton) beside gVisor sandboxing | Not a unified public “gVisor+Triton fork fabric” — treat as **compose pattern**, not a named product | Q&A only unless primary cite found |
| **wasm / wasmtime** | Capability-first isolate; near-zero overhead | Instant instantiate; **not** full Linux ABI / arbitrary toolchains | Tool-sandbox lane, not SWE-bench OS world |
| **Youki** | Rust OCI runtime (runc-class) | Container start, not microVM fork | Inner runtime under Kata/gVisor; not the outer wall |
| **seL4 / KVM composites** | seL4 = formally verified microkernel; compose with VMs | Capability mint/revoke pedigree for **WIRE leases** (E); not dense agent CoW VMM alone | Credential / authority ontology, not fork latency |

---

## 4. Honest comparison table

Latency classes are **orders of magnitude**, not bake-off scores. Peer numbers attributed; vendor cells = qualitative.

| System | Isolation thickness | Fork/clone latency class | Memory CoW | GPU | Density | Open vs product |
|---|---|---|---|---|---|---|
| **Firecracker** | Hardware microVM (thin devices) | Boot ~100 ms class; stock snap/restore **100 ms–s**; Diff baseline in DeltaBox **~0.5–1.5 s** | Guest mem MAP_PRIVATE / UFFD on restore | **No** (paused PCIe) | Very high (design goal) | Open |
| **DeltaBox on FC** | Same wall + in-guest DeltaFS/DeltaCR | Peer **~14 ms ckpt / ~5 ms restore**; fan-out p50 **0.57→5.47 ms** N=1→64 (kernel forks) | Template `fork()` + async-warm | No (inherits FC) | High (multi-agent/process in one VM) | Research / open mechanisms |
| **Crab** | Often container (runc+CRIU+ZFS) + can sit behind FC wall | Skip-heavy; process ckpt ~700–1000 ms when needed; E2E ≤1.9% | Process dumps typically not live-shared siblings | Host-dependent | Very high (container) | Research |
| **Cloud Hypervisor** | Hardware VM (richer PCI) | Snap+UFFD demand page; migrate path | Sparse + UFFD restore | **Yes** (VFIO) | High | Open |
| **QEMU** | Full / microvm | savevm/migrate; postcopy | Yes (postcopy/UFFD) | **Yes** | Medium–high | Open |
| **libkrun / krucible** | MicroVM; HVF+KVM | Snapshot/fork in fork; cold boot ~hundreds ms class (eng) | Emerging CoW overlays | Evolving | High embed | Open (+fork) |
| **Kata** | VM per pod (backend choice) | Warm-pool claim; not ms CoW fork | Backend | Backend | K8s-native | Open |
| **gVisor** | Userspace kernel | Process C/R | Process-level | Limited / special paths | Very high | Open |
| **wasmtime** | Wasm isolate | µs–ms instantiate | N/A (linear mem) | Via host | Extreme | Open |
| **Mitos/forkd** | FC microVM + control plane | Eng: tens of ms warm CoW fan-out (verbal) | CoW-aware metering | No (FC) | Designed for pack | Open eng |
| **Tensorlake** | FC / CH MicroVM + Lattice + FS | Eng: sub-second create; clone/suspend (verbal) | MEMORY snap + FS CoW | Via CH lane possible | Product density | Product |
| **OpenVMM / Hyper-V** | Hypervisor (Windows-strong) | Hyper-V checkpoint lineage | Host-dependent | Yes (Hyper-V) | Enterprise | OpenVMM open; Hyper-V product |
| **Hafnium** | Type-1 static partitions | **Not fork-factory** | N/A | N/A | Low dynamic | Open |
| **Nitro / SnapStart** | AWS control plane + FC-class guests | Managed restore (product) | Product | Separate | Hyperscale | Mostly product |

---

## 5. Claim fence (M-specific)

| DO | DO NOT |
|---|---|
| “Firecracker is **necessary but not sufficient**.” | “Firecracker is obsolete / bad / we should abandon it.” |
| Quote **DeltaBox/Crab/Shepherd** ms attributed | Put Tensorlake / forkd / E2B / Mitos ms on slides as Yossi numbers |
| Name CH / QEMU / libkrun as **GPU / macOS / migrate** lanes | Claim FC has shipping GPU |
| Hafnium = security-partition pedigree, **not** agent fork | Spell “HAFNION” as a shipping fork VMM without checking — use **Hafnium** |
| gVisor = contrast thickness | Equate gVisor isolation with KVM microVM for EscapeBench-class threat |
| Next-gen = pedigree evolution **or** deliberate route-around | Single winner bake-off |

**Vendor ms BACKUP only.** Peer DeltaBox Table 2 / Crab ≤1.9% / Shepherd 134–143 ms OK.

---

## 6. Architecture sketch for Act I / Q&A

```
                    ┌── DeltaBox / Crab / Shepherd     (peer: how-fast / what-when / API object)
Firecracker wall ───┼── forkd / Mitos / Tensorlake     (eng: CoW fan-out + scheduler + FS)
 (NSDI'20)          └── WIRE remint + sealed oracle    (E/C — outside the VMM)
        │
        ├── route-around GPU/Windows/migrate/macOS
        │     Cloud Hypervisor · QEMU · crosvm · libkrun · OpenVMM
        │
        └── thinner isolates (contrast)
              gVisor · wasmtime · Youki(inner) · Hafnium(static TE)
```

**One spoken closer:** “We keep Firecracker’s wall. We still need a fork factory, a lease broker, and — when the agent needs a GPU or a Mac — a second VMM lane. That’s next generation: *on* the pedigree, and *beside* it.”

---

## 7. Challenges / handoffs

| → | Ask |
|---|---|
| **A** | Confirm FC Diff vs DeltaCR framing stays “baseline vs evolution,” not “FC bad.” |
| **E** | Which next-gen VMM hooks (vmgenid, vsock reset on restore, credential scrub) are portable across CH/libkrun? |
| **F** | CH `core_scheduling` + per-zone `mergeable` KSM — pack-policy cousins of Firecracker guidance? |
| **J** | Tensorlake CH backend = practice proof that product already dual-VMM’s FC insufficiency. |
| **G** | Factory API must be VMM-agnostic: `World.fork` binds Epoch/obj_digest, not “Firecracker-only.” |

---

## 8. URL dump (quick index)

- Firecracker NSDI’20: https://www.usenix.org/conference/nsdi20/presentation/agache  
- FC GPU/PCIe discussion: https://github.com/firecracker-microvm/firecracker/discussions/4845  
- DeltaBox: https://arxiv.org/abs/2605.22781  
- Crab: https://arxiv.org/abs/2604.28138  
- Shepherd: https://arxiv.org/abs/2605.10913  
- Cloud Hypervisor v52: https://www.cloudhypervisor.org/blog/cloud-hypervisor-v52.0-released/  
- CH vs QEMU microvm: https://depot.dev/blog/differences-between-qemu-and-cloud-hypervisor  
- libkrun snapshot RFC: https://github.com/libkrun/libkrun/issues/748  
- krucible: https://bhatti.sh/docs/under-the-hood/engine/  
- Mitos: https://github.com/mitos-run/mitos  
- Tensorlake: https://www.tensorlake.ai/ · https://docs.tensorlake.ai/sandboxes/snapshots  
- Kata + agent-sandbox: https://agent-sandbox.sigs.k8s.io/docs/use-cases/kata-containers-isolation/  
- gVisor isolation: https://agent-sandbox.sigs.k8s.io/docs/use-cases/gvisor-isolation/  
- OpenVMM: https://techcommunity.microsoft.com/blog/windowsosplatform/the-openvmm-project/4547237  
- Hafnium: https://hafnium.docs.trustedfirmware.org/  
- Sandbox survey (Zylos): https://zylos.ai/research/2026-04-04-ai-agent-sandboxing-security-isolation/  
- mvmctl GPU research note: https://docs.rs/crate/mvmctl/latest/source/specs/research/gpu-passthrough.md  

---

*Researcher M · 2026-09-27 (IDT) · Cambridge SRG swarm*
