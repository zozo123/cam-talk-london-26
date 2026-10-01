# P — ALL SOLUTION LEVELS catalog (exhaustive)
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Isolation / capability ladder **0–10** with concrete open + vendor products (1-line role + URL when known); decision matrix threat × need-fork × oracle-seal → minimum level; claim fence  
**Aligns:** N (Monty / OS ladder) · M (beyond Firecracker) · A (fork systems) · C (EscapeBench) · O (labs) · J (Tensorlake) · G (factory API) · field manual [sandboxes-why-how-when](https://zozo123.github.io/sandboxes-why-how-when/)  
**Fence:** Levels = **thickness + capability grant**, not a bake-off. Peer ms (DeltaBox/Crab/Shepherd) attributed only. Vendor/eng ms = verbal landscape. Escape wall ≠ evidence wall ≠ WIRE. Monty/Wasm ≠ EscapeBench substitute. Firecracker = necessary pedigree, not the whole factory.  
**Spoken line:** “Pick the lowest level that holds the threat; climb when you need a real OS world, N-way fork, or EscapeBench-class outer wall.”

---

## 0. How to read this catalog

| Axis | Meaning |
|---|---|
| **Level** | Isolation / orchestration rung (0 thinnest → 10 control-plane factory) |
| **Boundary** | What separates guest from host / siblings |
| **Fork story** | Can you get N warm siblings with shared past? |
| **EscapeBench floor** | Does this rung hold hostile shell agents? (C / EscapeBench 2603.02277) |
| **Oracle / authority** | Does the rung itself seal the grader / Promote.tip? (**Almost never** — C/G/E live *outside*) |

**Compose pattern (recommended):** controller + sealed oracle + WIRE **outside** → outer wall at the right level → optional thinner inners (Monty / Docker) **inside**.

```
L0  in-process/REPL
L1  language sandbox          (Monty · denom · RestrictedPython · QuickJS …)
L2  process OS jail           (bwrap · Seatbelt · Landlock · nsjail · Anthropic srt)
L3  Wasm                      (wasmtime · WasmEdge · Monty wasm · Pyodide · Spin)
L4  containers                (Docker/runc · Podman · containerd)
L5  user-kernel / light VM    (gVisor · Kata · Nabla · Unikraft)
L6  microVM pedigree          (Firecracker · Cloud Hypervisor · crosvm · libkrun · QEMU microvm)
L7  fork/C/R fabrics          (DeltaBox · Crab · Shepherd · Tensorlake · forkd · Mitos · islo · E2B · Daytona · Modal · Northflank · Vercel Sandbox)
L8  full VM / nested          (EscapeBench outer nest · QEMU/KVM thick · Hyper-V)
L9  computer/desktop          (OpenAI / Anthropic computer use · browser agents)
L10 factory control planes    (Airflow/swfactory · Ray · Spark · OpenAI Sandbox Agents harness)
```

**Note on L7:** fork fabrics are **orthogonal** to isolation thickness — they *sit on* L4–L6 walls and add CoW / C/R / clone APIs. L7 is not “thicker than Firecracker”; it is the **fork factory** layer the talk is about.

---

## Level 0 — In-process / REPL

**Boundary:** same address space, ambient host authority.  
**Holds:** accidental typos of *trusted* helpers (barely).  
**Fails:** any adversarial / unreviewed code; credential theft; host compromise.  
**Fork:** language `fork`/`clone` ≠ isolation; siblings share process trust.  
**When:** trusted experiments, REPL demos, never EscapeBench-class agents.

| Product / project | Role | URL |
|---|---|---|
| **CPython `eval` / `exec`** | Ambient in-process evaluation — no wall | https://docs.python.org/3/library/functions.html#eval |
| **IPython / Jupyter kernel** | Interactive REPL; shares kernel process with notebook | https://ipython.org/ · https://jupyter.org/ |
| **Node `vm` / `eval`** | JS in-process context (escape-prone) | https://nodejs.org/api/vm.html |
| **OpenAI UnixLocal (Agents SDK)** | Local process workspace client — Monty-adjacent density, host trust | https://developers.openai.com/api/docs/guides/agents/sandboxes |
| **DeepSeek harness `codeRuntime` (worker-thread)** | Fresh Node worker; docs: **containment ≠ security boundary** | https://github.com/deepseek-ai/deepseek-harness |
| **safepyrun + fastaudit** | In-process allowlist via CPython audit hooks (cooperative, not EscapeBench) | https://github.com/AnswerDotAI/safepyrun |
| **sandtrap `isolation=none`** | AST-rewritten Python in-process | https://pypi.org/project/sandtrap/ |

---

## Level 1 — Language sandbox

**Boundary:** interpreter / bytecode VM with capability-from-nothing (or restricted subset); **no** separate guest kernel.  
**Holds:** unreviewed *subset* code that must not touch FS/net/env unless you grant host functions.  
**Fails:** full Linux ABI, bash, arbitrary pip wheels, EscapeBench shell agents.  
**Fork:** kB interpreter snapshots ≠ guest MEMORY CoW (N).  
**When:** CodeMode / tool orchestration / browser side-panel agents.

| Product / project | Role | URL |
|---|---|---|
| **Pydantic Monty** | Rust bytecode Python-subset VM; capability-from-nothing CodeMode | https://github.com/pydantic/monty · https://pydantic.dev/docs/monty/get-started/ · https://pydantic.dev/articles/pydantic-monty |
| **denom** | Language-level isolate named for this catalog (confirm shipping URL before stage cite) | *(URL when known — treat as L1 peer of Monty/QuickJS, not EscapeBench wall)* |
| **RestrictedPython** | Static language subset for trusted envs — **not** a secure sandbox vs adversaries | https://github.com/zopefoundation/RestrictedPython · https://restrictedpython.readthedocs.io/ |
| **QuickJS** | Embeddable JS engine; common host-bound language sandbox for tool glue | https://bellard.org/quickjs/ · https://github.com/bellard/quickjs |
| **Starlark** | Deterministic Python-like config language (Bazel / Buck2) | https://github.com/bazelbuild/starlark |
| **Lua / LuaJIT sandboxes** | Embeddable scripting with host-granted C APIs | https://www.lua.org/ |
| **OpenAI Code Interpreter kernel** | Hosted Python kernel ≈ language/workspace Monty-class product surface | https://developers.openai.com/api/docs/guides/tools-code-interpreter |
| **DeepSeek `ctx.codeRuntime`** | Worker-thread program isolate; official “not a security boundary” | https://deepseek-harness.github.io/deepseek-harness/ |

---

## Level 2 — Process OS jail (shared kernel)

**Boundary:** namespaces / cgroups / seccomp / Landlock / Seatbelt — still **shared host kernel**.  
**Holds:** semi-trusted code; accidental blast; FS+net deny-by-default for coding-agent bash.  
**Fails:** kernel CVE / misconfig → host (EscapeBench orchestration/runtime/kernel classes).  
**Fork:** process C/R possible (CRIU) but not EscapeBench outer wall.  
**When:** Claude Code local bash; DeepSeek `ctx.sandbox`; developer laptop confine.

| Product / project | Role | URL |
|---|---|---|
| **bubblewrap (`bwrap`)** | Unprivileged Linux namespace sandbox (bind mounts, netns strip) | https://github.com/containers/bubblewrap |
| **macOS Seatbelt (`sandbox-exec`)** | Apple sandbox profiles for FS/net confine | https://reverse.put.as/wp-content/uploads/2011/09/Apple-Sandbox-Guide-v1.0.pdf *(concept)* · used by Anthropic srt |
| **Landlock LSM** | Unprivileged Linux FS (and growing) access-control | https://docs.kernel.org/userspace-api/landlock.html · https://landlock.io/ |
| **nsjail** | Google process jail: namespaces + seccomp + cgroups | https://github.com/google/nsjail |
| **Anthropic sandbox-runtime (`srt`)** | Cross-platform FS+net confinement (bwrap / Seatbelt / Windows WFP) for agents & MCP | https://github.com/anthropic-experimental/sandbox-runtime · https://code.claude.com/docs/en/sandboxing |
| **seccomp-bpf / libseccomp** | Syscall allow/deny filters | https://github.com/seccomp/libseccomp |
| **Firejail** | Convenient Linux SUID sandbox (namespaces + seccomp) | https://github.com/netblue30/firejail |
| **minijail** | ChromeOS/Android-style process sandbox | https://google.github.io/minijail/ |
| **DeepSeek `ctx.sandbox` / dsh-sandbox-local** | bwrap / Landlock / Seatbelt / Windows restricted token for file effects | https://deepseek-harness.github.io/deepseek-harness/en/reference/subsystems/sandbox |
| **sandtrap `isolation=kernel`** | Subprocess + Landlock/Seatbelt/seccomp second layer | https://pypi.org/project/sandtrap/ |

---

## Level 3 — Wasm

**Boundary:** Wasm linear memory + capability imports; soft crash via Worker / trap.  
**Holds:** portable CodeMode / edge / browser isolates; WASI-scoped FS/net.  
**Fails:** full Linux toolchain / arbitrary binaries unless you reimplement ABI; not EscapeBench substitute for OS agents.  
**Fork:** instant instantiate; not guest MEM/FS CoW for MCTS.  
**When:** browser agents, edge functions, Monty-in-Wasm, WASI apps.

| Product / project | Role | URL |
|---|---|---|
| **wasmtime** | Bytecode Alliance Wasm/WASI runtime (Rust) | https://wasmtime.dev/ · https://github.com/bytecodealliance/wasmtime |
| **WasmEdge** | Cloud/edge Wasm runtime (CNCF) | https://wasmedge.org/ · https://github.com/WasmEdge/WasmEdge |
| **Monty Wasm (`@pydantic/monty/wasm`)** | Monty bytecode VM in browser Worker / Node worker_threads | https://pydantic.dev/docs/monty/get-started/ |
| **Pyodide** | CPython compiled to Wasm (browser / Node) | https://pyodide.org/ · https://github.com/pyodide/pyodide |
| **Fermyon Spin** | Wasm serverless / microservice framework on Wasmtime | https://www.fermyon.com/spin · https://github.com/spinframework/spin |
| **Wasm3 / WAMR** | Lightweight Wasm interpreters for embed | https://github.com/wasm3/wasm3 · https://github.com/bytecodealliance/wasm-micro-runtime |
| **pycage** | Real CPython as Wasm component (self-hosted E2B-class alternative) | https://github.com/samyfodil/pycage |
| **Cloudflare Workers / workerd** | V8 isolate edge (Wasm + JS) | https://developers.cloudflare.com/workers/ |
| **Extism** | Wasm plugin system across host languages | https://extism.org/ |

---

## Level 4 — Containers (shared kernel + OCI)

**Boundary:** runc/containerd namespaces + cgroups + OCI image; **shared host kernel**.  
**Holds:** portable deps; trusted-human or low-stakes packaging; **inner** layer under microVM.  
**Fails:** EscapeBench Docker-class escapes (socket, privileged, runc/kernel).  
**Fork:** `docker commit` / overlay — seconds-class; not ms CoW peer fabric.  
**When:** portable inner world; Claude Code on the web; OpenAI `openai_hosted` surfaces.

| Product / project | Role | URL |
|---|---|---|
| **Docker Engine + runc** | De-facto OCI container UX; EscapeBench foil as *sole* outer wall | https://docs.docker.com/ · https://github.com/opencontainers/runc |
| **containerd** | Industry container runtime (K8s default CRI path) | https://containerd.io/ · https://github.com/containerd/containerd |
| **Podman** | Daemonless OCI containers (rootless-friendly) | https://podman.io/ · https://github.com/containers/podman |
| **CRI-O** | K8s-oriented OCI runtime | https://cri-o.io/ |
| **Youki** | Rust OCI runtime (runc-class) | https://github.com/youki-dev/youki |
| **Buildah / skopeo** | Image build/copy without full daemon | https://buildah.io/ |
| **OpenAI Agents SDK Docker client** | Harness compute via local/remote Docker | https://openai.github.io/openai-agents-js/guides/sandbox-agents/clients/ |
| **Anthropic Claude Code on the web** | Isolated cloud sandbox (Docker-class product surface) | https://www.anthropic.com/engineering/claude-code-sandboxing |

---

## Level 5 — User-kernel / light VM

**Boundary:** userspace kernel (gVisor) or VM-per-pod / unikernel — thicker than runc, not always full Firecracker pedigree.  
**Holds:** shrinks syscall surface vs runc; Kata gives hardware VM per pod when backend is FC/CH/QEMU.  
**Fails:** gVisor alone ≠ EscapeBench *substitute* for hostile OS agents (C/N); Nabla/Unikraft = specialized ABI.  
**Fork:** process C/R / warm pools; ms CoW still usually L6+L7.  
**When:** K8s RuntimeClass isolation; denser than full QEMU; unikernel appliances.

| Product / project | Role | URL |
|---|---|---|
| **gVisor (`runsc`)** | Userspace kernel / syscall intercept — container ergonomics, no separate guest kernel | https://gvisor.dev/ · https://github.com/google/gvisor |
| **Kata Containers** | K8s RuntimeClass → QEMU / Firecracker / Cloud Hypervisor backends | https://katacontainers.io/ · https://github.com/kata-containers/kata-containers |
| **Nabla Containers** | Unikernel containers (runnc) — tiny attack surface, limited ABI | https://nabla-containers.github.io/ · https://github.com/nabla-containers/runnc |
| **Unikraft** | Modular unikernel (Linux ABI subset / many libs) | https://unikraft.org/ · https://github.com/unikraft/unikraft |
| **sysbox** | Rootless Docker-in-Docker style (system containers) | https://github.com/nestybox/sysbox |
| **agent-sandbox gVisor use-case** | K8s SIG docs for gVisor isolation | https://agent-sandbox.sigs.k8s.io/docs/use-cases/gvisor-isolation/ |

---

## Level 6 — microVM pedigree

**Boundary:** **hardware VM** + thin virtio; own guest kernel (KVM / HVF / Hyper-V).  
**Holds:** EscapeBench-class untrusted shell agents (**talk default outer wall**); density + ~100 ms boot class.  
**Fails:** rare hypervisor/device bugs; warm CoW side-channels (F); no WIRE/oracle by itself.  
**Fork:** stock snap/restore = VM-granularity; **dense warm CoW UX needs L7 on top**.  
**When:** SWE/RL/OS worlds; multi-tenant agent clouds; NCSC-aligned hypervisor minimum.

| Product / project | Role | URL |
|---|---|---|
| **Firecracker** | Canonical dense microVM (NSDI’20); AWS Lambda/Fargate pedigree | https://firecracker-microvm.github.io/ · https://www.usenix.org/conference/nsdi20/presentation/agache · https://github.com/firecracker-microvm/firecracker |
| **Cloud Hypervisor** | rust-vmm cousin; VFIO GPU, UFFD restore, live migrate | https://www.cloudhypervisor.org/ · https://github.com/cloud-hypervisor/cloud-hypervisor |
| **crosvm** | ChromeOS/Android VMM; virtio-gpu interest | https://chromium.googlesource.com/chromiumos/platform/crosvm |
| **libkrun (+ krucible)** | Embeddable VMM; KVM + **HVF (macOS)**; snapshot/fork evolving | https://github.com/containers/libkrun · https://bhatti.sh/docs/under-the-hood/engine/ |
| **QEMU `microvm` machine** | Thin QEMU device model; postcopy/UFFD migrate | https://www.qemu.org/docs/master/system/i386/microvm.html |
| **OpenVMM** | Microsoft open Rust VMM (Hyper-V / WHP / KVM lanes) | https://techcommunity.microsoft.com/blog/windowsosplatform/the-openvmm-project/4547237 |
| **AWS Nitro / Lambda SnapStart** | Hyperscale control plane + managed restore lineage (product) | AWS Lambda SnapStart docs · Firecracker open-source announce |
| **OpenAI × DigitalOcean M.A.R.S.** | Partner path: Firecracker microVM + `codex-agentapi` | https://developers.openai.com/api/docs/guides/agents-api/environments/providers/digitalocean |

---

## Level 7 — Fork / C/R fabrics

**Boundary:** control-plane + CoW/C/R **on top of** L4–L6 walls — the talk’s *fork factory*.  
**Holds:** N-way warm siblings, checkpoint/rollback, Session/trace APIs, product clone/suspend.  
**Fails:** does **not** by itself seal oracle / Promote.tip / WIRE remint (A/C/E/G debt).  
**Fork:** **this is the rung** — peer (DeltaBox/Crab/Shepherd) + eng/product landscape.  
**When:** MCTS / Tree-RL / BoN / parallel agent search; durable MicroVM worlds.

### 7a. Research / peer systems (slide-safe attributed)

| Product / project | Role | URL |
|---|---|---|
| **DeltaBox** | Change-based coupled FS+mem C/R on Firecracker (~ms ckpt/restore; MCTS/RL) | https://arxiv.org/abs/2605.22781 |
| **Crab** | Semantics-aware what/when to checkpoint (eBPF net-change skips; ≤1.9% overhead) | https://arxiv.org/abs/2604.28138 |
| **Shepherd** | Agent+env as reversible Git-like effect trace; `scope.fork()` ~134–143 ms | https://arxiv.org/abs/2605.10913 |
| **OpenRath** | Session as first-class branchable/inspectable runtime value | https://arxiv.org/abs/2606.19409 |
| **Xu–Kaffes** | Agenda paper: fork semantics, side-effects, native CoW | https://arxiv.org/abs/2510.05556 |

### 7b. Eng / product fabrics (verbal landscape — no vendor ms on slides)

| Product / project | Role | URL |
|---|---|---|
| **Tensorlake** | Durable MicroVM worlds (FC/CH); FILESYSTEM vs MEMORY snaps; clone/suspend; `@function` fan-out | https://www.tensorlake.ai/ · https://docs.tensorlake.ai/sandboxes/snapshots · https://github.com/tensorlakeai/tensorlake |
| **forkd** | Warm-parent CoW fan-out control plane on Firecracker | *(eng landscape — cite via mitos/forkd DESIGN when speaking; no slide ms)* |
| **Mitos** | CoW-aware metering + scheduling on FC husk pods | https://github.com/mitos-run/mitos · https://mitos.run/docs/metering |
| **islo.dev** | Managed sandboxes / gateway (Yossi-related; WIRE cousin) | https://islo.dev/sandboxes/ |
| **E2B** | Managed Firecracker-class code sandboxes; pause/resume | https://e2b.dev/ · https://github.com/e2b-dev/E2B |
| **Daytona** | Dev/workspace sandboxes; Agents SDK / CUA partner path | https://www.daytona.io/ |
| **Modal Sandboxes** | Fast Python/GPU serverless + sandbox API (container-class isolate) | https://modal.com/docs/guide/sandbox |
| **Northflank** | Long-lived / BYOC sandboxes with orchestration | https://northflank.com/ |
| **Vercel Sandbox** | Ephemeral microVM sandboxes on Vercel platform | https://vercel.com/docs/vercel-sandbox |
| **Deno Deploy Sandboxes** | Instant Linux microVMs + snapshot volumes | https://docs.deno.com/sandbox/ · https://deno.com/deploy/sandboxes |
| **Runloop / Blaxel / Cloudflare / Superserve** | Agents SDK partner compute clients (landscape) | OpenAI Agents SDK clients index |
| **crabbox.sh** | Provider-agnostic runner — same task across sandbox vendors | https://crabbox.sh/ |

**Number fence (A):** on-slide latencies only DeltaBox / Crab / Shepherd (attributed). forkd / Tensorlake / E2B / Daytona / islo / Modal / Northflank / Vercel = **verbal only**.

---

## Level 8 — Full VM / nested (EscapeBench)

**Boundary:** thick device model and/or **nested** container-in-VM (how EscapeBench is measured).  
**Holds:** regulated / genuinely hostile / air-gapped; nested CTF measures Docker escapes *inside* a VM.  
**Fails:** cost, boot, ops density — wrong default for thousands of agent forks.  
**Fork:** hypervisor checkpoints; not the talk’s ms CoW sweet spot.  
**When:** EscapeBench harness itself; high-assurance nests; Windows/enterprise thick VMs.

| Product / project | Role | URL |
|---|---|---|
| **SandboxEscapeBench** | Nested container-in-VM CTF measuring agent breakouts | https://arxiv.org/abs/2603.02277 · https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities |
| **AgentEscapeBench** | Broader `(model × sandbox)` matrix incl. Docker/gVisor/FC/QEMU/Wasm | https://github.com/safety-research/agent-escape-bench |
| **QEMU/KVM full machine** | Broadest device model; Windows/display/VFIO | https://www.qemu.org/ |
| **Hyper-V / WHP** | Windows hypervisor lane (OpenVMM cousin) | Microsoft Hyper-V docs |
| **VMware / VirtualBox** | Classic thick Type-2 / enterprise VMs | vendor docs |
| **Nested K8s (kind / k3s in VM)** | Orchestration nest for EscapeBench-class scenarios | https://kind.sigs.k8s.io/ |

**Stage rule:** EscapeBench **motivates** L6 outer wall for untrusted agents; L8 nest is the *measurement apparatus*, not the production fork factory.

---

## Level 9 — Computer / desktop

**Boundary:** full GUI desktop / browser the model drives (screenshots + mouse/keyboard).  
**Holds:** high-capability interactive work; human-in-the-loop typical for consequential acts.  
**Fails:** maximal ambient capability — **not** an EscapeBench outer wall by itself; isolation = whatever you wrap it in (Docker/VM).  
**Fork:** session clones rare; not N-way CoW search fabric.  
**When:** computer-use products; browser agents; Magentic-One-style multi-agent desktops (**Microsoft**, not Anthropic).

| Product / project | Role | URL |
|---|---|---|
| **OpenAI Computer Use** | Model drives browser/desktop; **you** provide the environment | https://developers.openai.com/api/docs/guides/tools-computer-use |
| **Anthropic Computer Use tool** | Screenshot/mouse/keyboard toolset; recommend VM/container wrap | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool |
| **OpenAI CUA + Daytona cookbook** | Computer use inside Daytona sandbox | https://developers.openai.com/cookbook/examples/agents_sdk/computer_use_with_daytona/computer_use_with_daytona |
| **Browser agents (Playwright / Puppeteer / Stagehand)** | Headless/headed browser automation as agent body | Playwright · Browserbase · etc. |
| **Magentic-One (Microsoft AutoGen)** | Multi-agent desktop/web/file/coder — **not Anthropic** | https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/ |
| **OpenClaw-class agent loops** | Session + tools + sandboxed body (talk inspiration, not robot OS) | *(methodology twin — see README)* |

---

## Level 10 — Factory control planes

**Boundary:** **orchestration / authority spine** — not an escape wall. Owns Epoch, objective digest, reduce, promote.  
**Holds:** Search≠Authority; path-integral CI; schedule/anneal; multi-domain hill-climb.  
**Fails:** if mistaken for isolation — Airflow does not EscapeBench-harden a Docker child.  
**Fork:** may *call* L7 fabrics; must not smuggle Promote.tip into the worker.  
**When:** swfactory Cells; Ray/Spark fan-out; OpenAI Sandbox Agents harness ⊥ compute.

| Product / project | Role | URL |
|---|---|---|
| **Apache Airflow** | DAG authority spine / lifecycle (swfactory cousin) | https://airflow.apache.org/ |
| **ariflow-swfactory / swfactory** | Cell · epoch · Search≠Authority · evidence · promote (talk methodology) | *(speaker methodology — capability contract, not “already ships N-way fork everywhere”)* |
| **Ray** | Distributed tasks+actors; MapReduce lineage cousin | https://www.ray.io/ · https://github.com/ray-project/ray |
| **Apache Spark** | RDD lineage / shuffle reduce pedigree | https://spark.apache.org/ |
| **Evidence-Aware MapReduce / Boltzmann** | Precision-weighted reduce; β≡n; abstain (2607.09689) | https://arxiv.org/abs/2607.09689 · https://github.com/zozo123/boltzmann-mapreduce |
| **OpenAI Agents API / Sandbox Agents harness** | Harness ⊥ compute; env = none \| openai_hosted \| self_hosted | https://developers.openai.com/api/docs/guides/agents-api/architecture · https://developers.openai.com/api/docs/guides/agents/sandboxes |
| **DeepSeek Harness (dsh)** | Pluginized agent harness with sandbox/codeRuntime seams | https://github.com/deepseek-ai/deepseek-harness |
| **Temporal / Cadence** | Durable workflow authority (cousin control planes) | https://temporal.io/ |
| **Kubeflow / Flyte** | ML pipeline control planes | https://www.kubeflow.org/ · https://flyte.org/ |

---

## Decision matrix — threat × need-fork × oracle-seal → **minimum level**

Read rows top-down; take the **max** of the three column minima (fail closed). Oracle-seal is almost always a **controller obligation beside** the wall — the matrix says when you must *additionally* refuse thinner walls.

### Axes

| Axis | Low | Mid | High |
|---|---|---|---|
| **Threat** | Trusted / cooperative code | Semi-trusted LLM subset / bash | EscapeBench-class shell agent / multi-tenant hostile |
| **Need-fork** | Single shot | Occasional snapshot | N-way warm CoW fan-out (MCTS/RL/BoN) |
| **Oracle-seal** | No grader / human grades offline | Soft tests in-env OK | Sealed oracle + Promote.tip must leave the fork |

### Matrix (minimum **isolation / fabric** level)

| Threat ↓ \ Need-fork → | Single shot | Snapshot / resume | N-way warm CoW |
|---|---|---|---|
| **Trusted cooperative** | **L0–L1** | L1–L2 or L4 | L7 on L4+ (eng OK) |
| **LLM CodeMode subset** (no bash) | **L1** (Monty/Wasm) | L1–L3 | L1 snapshots ≠ guest CoW → escalate **L6+L7** if real OS worlds |
| **Semi-trusted bash / deps** | **L2** or **L4** | L4 (+CRIU) | L7 on L4; prefer **L6+L7** if secrets/VPC |
| **Untrusted OS agent** (shell+FS) | **L6** outer (Docker inner OK) | L6 snap + L7 C/R | **L6 + L7** (talk default) |
| **EscapeBench / multi-tenant** | **L6** minimum; L8 nest for measurement | L6+L7 | **L6+L7** + pack-by-trust (F) |
| **Computer use / desktop** | **L9** wrapped in L4 or L6 | session save | rarely N-way — still wrap L6 if autonomous hostile |
| **Factory authority** | **L10** always *beside* wall | L10 owns Epoch | L10 calls L7; never lives in child |

### Oracle-seal overlay (additive)

| Oracle-seal need | Extra requirement (any threat/fork) |
|---|---|
| None / offline human | — |
| In-env tests acceptable | Prefer RUN≠EVAL privileges; still content-address harness |
| **Sealed oracle + Promote.tip** | Controller digests + attestation \(a_k\) **outside** guest mutability; WIRE remint on fork; **no level alone substitutes** — minimum wall still from threat row, plus C/E/G contracts |

### Quick chooser (one breath)

1. CodeMode Python subset, no host reach → **L1** (Monty) / **L3** (Wasm).  
2. Local bash confine, same laptop → **L2** (srt / bwrap / Seatbelt).  
3. Portable deps, accept shared kernel → **L4** inner.  
4. Untrusted agent with shell → **L6** outer (+ optional L4/L1 inner).  
5. Need N warm siblings → add **L7** on L6 (peer DeltaBox/Crab/Shepherd; eng Tensorlake/forkd/…).  
6. Measuring escapes → **L8** nest.  
7. GUI desktop → **L9** (wrap L4/L6).  
8. Epoch / reduce / promote → **L10** outside the CoW body.

---

## Dual sketch — OS thickness vs capability grant vs fork fabric

```
Capability grant (Monty continuum)     OS escape wall (field manual)      Fork fabric (talk)
──────────────────────────────         ─────────────────────────────      ─────────────────
tool call → L1 Monty → L4/L7 svc → L9 desktop
                 │                            │                              │
                 │ language                   │ shared kernel                │ CoW / C/R API
                 ▼                            ▼                              ▼
              L1 / L3                      L2 / L4 / L5                   L7 on L4–L6
                                              │
                                              ▼ EscapeBench floor
                                           L6 microVM  ◄── default outer wall
                                              │
                                              ▼
                                           L8 full/nested

Authority spine (always outside):  L10  + sealed oracle (C) + WIRE (E) + Reduce/abstain (B)
```

---

## Claim fence (P-specific)

| DO | DO NOT |
|---|---|
| “Levels = thickness + capability + fork fabric — compose, don’t conflate.” | Treat L7 as “thicker than Firecracker” |
| Docker OK as **inner**; microVM **outer** for EscapeBench-class agents | “Containers are fine outer walls now” |
| Monty/Wasm/denom/RestrictedPython/QuickJS = **L1 language** rung | “Monty replaces Firecracker / passes EscapeBench” |
| Quote DeltaBox/Crab/Shepherd ms **attributed** | Put E2B/Tensorlake/forkd/Daytona/Modal ms on slides as Yossi benches |
| Firecracker = **necessary but not sufficient** (M) | “Firecracker is obsolete” |
| L10 = authority spine; Search≠Authority | “Airflow/Ray already ship sealed oracle + N-way fork” |
| Oracle-seal / WIRE / Promote.tip live **outside** every level | “Thicker sandbox ⇒ Rebound-proof” |
| Magentic-One = **Microsoft** | Attribute Magentic to Anthropic |
| denom = L1 peer until URL verified | Invent denom peer latency or EscapeBench claims |

**Stage recovery:** “To be precise: the ladder picks the *wall*; the factory still owes fork fabric, sealed oracle, and promote-once outside the child.”

---

## Challenges / ROUNDTABLE handoffs

| → | Ask |
|---|---|
| **N** | Confirm L0–L6 map onto Monty continuum + field-manual ladder; L1 denom sits with Monty/QuickJS. |
| **M** | L6 roster matches next-gen VMM map; L5 gVisor/Kata/Nabla/Unikraft as contrast. |
| **A** | L7a peer vs L7b eng split preserves number fence. |
| **C** | EscapeBench → L6 minimum; L8 = measurement nest; L1/L3 off substitute list. |
| **G** | `World.fork(..., isolate_tier=L0…L10)` fail-closed enum from this catalog? |
| **O** | Lab products placed on levels without globalizing Firecracker. |
| **J** | Tensorlake = L7 practice on L6 FC/CH — not L10 promote. |
| **E** | Remint required on any L7 clone that copies credential pages. |

---

## URL dump (index)

- Field manual: https://zozo123.github.io/sandboxes-why-how-when/  
- EscapeBench: https://arxiv.org/abs/2603.02277  
- Monty: https://github.com/pydantic/monty  
- Anthropic srt: https://github.com/anthropic-experimental/sandbox-runtime  
- Firecracker NSDI’20: https://www.usenix.org/conference/nsdi20/presentation/agache  
- DeltaBox / Crab / Shepherd: arXiv 2605.22781 / 2604.28138 / 2605.10913  
- Tensorlake: https://www.tensorlake.ai/  
- Boltzmann / MapReduce: https://arxiv.org/abs/2607.09689  

---

*Researcher P · ALL SOLUTION LEVELS · 2026-09-27 (IDT) · Cambridge SRG swarm*
