# Researcher O — Labs map: DeepSeek · OpenAI · Anthropic
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Public positions / products on agent sandboxes, code execution, computer use, isolation — primary URLs only  
**Fence:** **No rumor.** Product blogs / eng posts = **BACKUP verbal**. Docs + OSS repos = citeable. Do not invent Firecracker claims where the lab did not write them. Magentic = **Microsoft**, not Anthropic (note below).  
**Spoken line:** “All three ship walls and harnesses; none yet owes the fork+reduce+authority contract Cambridge is asking for.”

---

## 0. Thesis (one breath)

OpenAI productizes **harness ⊥ compute** (Codex / Agents API / Agents SDK sandboxes; Computer Use as BYO desktop). Anthropic productizes **OS-enforced FS+net confinement** (Claude Code sandbox + cloud web sandbox) and **computer use** with VM/container guidance + constitutional *training* values. DeepSeek splits **open weights (you isolate)** vs **hosted API (tenant/rate isolation)** and ships an open **DeepSeek Harness** whose own docs mark worker-thread code-runtime as **containment, not a security boundary**. Map each onto the isolation ladder **Monty → Docker → MicroVM → computer**. Cambridge debt: **fork fabric · reduce/abstain · sealed authority** remain unpaid across all three.

---

## 1. Isolation ladder (shared vocabulary)

Align with **N** (`N-SANDBOX-LAYERS-MONTY.md`): talk ladder **Monty → Docker → MicroVM → computer**. Field-manual ns/bwrap sits *between* Monty and Docker (shared kernel, not language-level).

| Rung | Meaning for this note | Typical mechanisms |
|---|---|---|
| **Monty** | Language-level / interpreter isolate (capability-from-nothing CodeMode) | Pydantic Monty; DeepSeek worker-thread `codeRuntime`; Code Interpreter kernel |
| **(+ ns/bwrap)** | Same-host OS confine — *not* a separate Monty product name | Seatbelt / bubblewrap / Landlock (Claude Code Bash; dsh `ctx.sandbox`) |
| **Docker** | Shared-kernel container / hosted Linux workspace | Docker; Claude Code on the web; OpenAI `openai_hosted` / Responses container |
| **MicroVM** | Hardware-isolated guest (Firecracker-class) | Firecracker / Cloud Hypervisor / partner microVM images |
| **computer** | Full GUI desktop / browser the agent drives | screenshots + mouse/keyboard / Playwright / PyAutoGUI |

**Rule:** a product may *sit on* a higher rung without *shipping* the talk’s fork CoW / reduce / promote bits. Monty ≠ EscapeBench wall (N/C).

---

## 2. OpenAI — Codex / Code Interpreter / Computer Use / Agents sandboxes

### 2.1 Products (public)

| Product | What it is | Ladder rung | Primary |
|---|---|---|---|
| **Code Interpreter** (Responses / Assistants lineage) | Model writes & runs Python in a **sandboxed** environment; files in/out | **Docker-class** hosted workspace (OpenAI-managed; internals not claimed as Firecracker on this page) | [Code Interpreter](https://developers.openai.com/api/docs/guides/tools-code-interpreter) |
| **Responses API + shell tool + hosted container** | Model proposes shell; platform runs in isolated FS + optional SQLite; egress proxy + domain-scoped secret injection | **Docker-class** (BACKUP eng: container workspace) | [Equip Responses API](https://openai.com/index/equip-responses-api-computer-environment/) **BACKUP** · [Computer use guide](https://developers.openai.com/api/docs/guides/tools-computer-use) |
| **Agents API** | OpenAI-hosted **Codex harness**; env = `none` \| `openai_hosted` \| `self_hosted` | Hosted sandbox = Docker-class product surface; self-hosted = bring-your-wall | [Architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture) · [openai_hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted) · [Agents API intro](https://openai.com/index/introducing-the-agents-api/) **BACKUP** |
| **Agents SDK SandboxAgent** | Harness in app; compute via clients: Unix-local, Docker, Blaxel, Cloudflare, Daytona, **E2B**, Modal, Runloop, Vercel | **Monty** (UnixLocal) → **Docker** → partner (**often MicroVM**, e.g. E2B/Firecracker in partner docs) | [Sandbox Agents](https://developers.openai.com/api/docs/guides/agents/sandboxes) · [SDK evolution](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) **BACKUP** · [JS clients](https://openai.github.io/openai-agents-js/guides/sandbox-agents/clients/) |
| **Computer Use** | Model drives browser/desktop via **code execution** (recommended) or structured `computer` actions; **you** provide the environment | **computer** (isolation = whatever you wrap it in) | [Computer use](https://developers.openai.com/api/docs/guides/tools-computer-use) · [CUA + Daytona cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/computer_use_with_daytona/computer_use_with_daytona) |
| **Firecracker mention (partner path)** | DigitalOcean M.A.R.S. starts a **Firecracker microVM** with `codex-agentapi` for Agents API self-hosted | Explicit **MicroVM** on partner path | [DigitalOcean provider](https://developers.openai.com/api/docs/guides/agents-api/environments/providers/digitalocean) |

### 2.2 Position (claim-fenced)

- **Harness ⊥ compute** is the public architecture: Codex/Agents harness owns the loop; sandbox owns files/shell; app owns function tools / lifecycle ([Architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture)).
- Hosted sandbox: packages, setup commands, network `enabled|disabled|restricted`, vault secrets for egress — **product isolation**, not a published fork CoW API ([openai_hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted)).
- **Do not** say “OpenAI runs everything on Firecracker” on stage — primary Firecracker string found on the **DigitalOcean** Agents API provider page; treat other MicroVM claims as partner/eng unless OpenAI names them.

### 2.3 Cambridge debt (OpenAI)

| Owes | Why |
|---|---|
| **Fork** | Hosted/self-hosted sandboxes are session workspaces — no public N-way warm CoW sibling fabric with lineage tags for ρ |
| **Reduce** | Multi-agent SDK has handoffs; no inverse-information / abstain-on-shared-root contract |
| **Authority** | Vault/egress proxies keep secrets out of the model — good WIRE *hints* — but promote/oracle digests are not first-class outside the sandbox |

---

## 3. Anthropic — Computer Use / Claude Code sandboxes / Magentic? / constitution

### 3.1 Products (public)

| Product | What it is | Ladder rung | Primary |
|---|---|---|---|
| **Computer use tool** | Client toolset: screenshot / mouse / keyboard; **your** app runs calls; security guidance = dedicated **VM or container**, domain allowlist, human confirm for consequential acts | **computer** (+ recommend Docker/VM wrap) | [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) · [Announce Oct 2024](https://www.anthropic.com/news/3-5-models-and-computer-use) **BACKUP** |
| **Claude Code Bash sandbox** | OS-level **filesystem + network** isolation for Bash (and children); Linux **bubblewrap**, macOS **Seatbelt**; open-sourced `@anthropic-ai/sandbox-runtime` research preview | **ns/bwrap** (shared-kernel; between Monty and Docker) — *not* a microVM by default | [Sandboxing eng post](https://www.anthropic.com/engineering/claude-code-sandboxing) **BACKUP** · [Docs](https://code.claude.com/docs/en/sandboxing) |
| **Claude Code on the web** | Each session in an **isolated cloud sandbox**; git via scoped credential + proxy (secrets stay outside) | **Docker-class** cloud isolate | Same eng post **BACKUP** |
| **Constitutional AI / Claude’s constitution** | Training-time principles (helpful/honest/harmless) via AI feedback — **policy sandbox**, not runtime isolate | Off-ladder (values) | [Claude’s constitution](https://www.anthropic.com/research/claudes-constitution) · [update pointer](https://www.anthropic.com/news/claude-new-constitution) if cited |
| **Magentic?** | **Not Anthropic.** **Magentic-One** = Microsoft Research / AutoGen multi-agent (WebSurfer, FileSurfer, Coder, ComputerTerminal) | N/A for Anthropic column | [MSR Magentic-One](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/) |

### 3.2 Position (claim-fenced)

- Explicit thesis: **both** FS and network isolation required — either alone fails under prompt injection ([eng post](https://www.anthropic.com/engineering/claude-code-sandboxing)).
- Docs are unusually honest about **limits**: default proxy does not inspect TLS; Unix sockets / broad write paths can escalate; Linux nested `enableWeakerNestedSandbox` weakens isolation ([sandboxing docs](https://code.claude.com/docs/en/sandboxing)).
- Computer use: classifiers on screenshots for injection; still requires human-in-loop for many consequential actions ([computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)).
- Constitution ≠ EscapeBench wall — keep training values off the isolation slide except as “policy layer beside the wall.”

### 3.3 Cambridge debt (Anthropic)

| Owes | Why |
|---|---|
| **Fork** | Sandbox = boundaries for *one* agent session; no public warm-parent CoW fan-out of coding worlds |
| **Reduce** | Permission/approval UX ≠ statistical reduce; no ρ-abstain |
| **Authority** | Git proxy + credential mask/inject are strong **WIRE cousins**; sealed *eval/oracle* digests and Promote.tip kinds still missing from the public coding agent contract |

---

## 4. DeepSeek — code/API sandbox · coding deployment · open weights vs hosted

### 4.1 Split: weights vs hosted

| Mode | What ships | Isolation story | Primary |
|---|---|---|---|
| **Open weights** | DeepSeek-V3 / later MoE checkpoints on GitHub + Hugging Face; run via vLLM/SGLang/etc. | **You** choose Monty/Docker/MicroVM — lab publishes model, not a managed agent microVM | [DeepSeek-V3 README](https://github.com/deepseek-ai/DeepSeek-V3) · [HF deepseek-ai](https://huggingface.co/deepseek-ai) |
| **Hosted API** | OpenAI/Anthropic-compatible API; agent integrations list Claude Code, Codex, OpenCode, etc. as *clients* | **Account concurrency** + optional `user_id` content-safety isolation — **not** a code-execution sandbox product | [Rate Limit & Isolation](https://api-docs.deepseek.com/quick_start/rate_limit) · [API docs](https://api-docs.deepseek.com/) · [Harness preview note on docs](https://api-docs.deepseek.com/) |
| **DeepSeek Harness (dsh)** | Open pluginized agent harness (developer preview) | Separate seams: `ctx.sandbox` (process) vs `ctx.codeRuntime` (program) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) · [Harness docs site](https://deepseek-harness.github.io/deepseek-harness/) |

### 4.2 Harness isolation (primary, claim-fenced)

| Seam | Mechanism | Ladder | Security claim in primary text |
|---|---|---|---|
| **`ctx.sandbox` / dsh-sandbox-local** | Linux **bwrap / Landlock**, macOS **Seatbelt**, Windows ACL restricted-token; modes `read-only` / `workspace-write` / `danger-full-access` (file effects) | **ns/bwrap** | Same-world subprocess confine. Docs: **containers / microVMs / remote are sibling seams**, not `ctx.sandbox` providers ([sandbox subsystem](https://deepseek-harness.github.io/deepseek-harness/en/reference/subsystems/sandbox); agent note [2026-07-06-sandbox](https://cdn.jsdelivr.net/gh/deepseek-ai/deepseek-harness@master/.agents/notes/implemented/feature/2026-07-06-sandbox.md)) |
| **`ctx.codeRuntime` / worker-thread** | Fresh Node worker per program; empty env; heap/time caps; hard terminate | **Monty** | Official posture: **containment, not a security boundary**; programs can reach Node APIs / spawn processes that survive `terminate()` ([code-runtime note](https://cdn.jsdelivr.net/gh/deepseek-ai/deepseek-harness@master/.agents/notes/implemented/feature/2026-06-15-ptc.md) · learn page [deepseekdocs code-runtime](https://deepseekdocs.com/en/docs/learn/core/code-runtime) as community mirror — prefer GitHub note if contested) |
| **Container-class backends** | Descriptors include `'container'`; community/plugin container providers exist | **Docker** (when composed) | Need multi-tenant hard boundary ⇒ container-class backend for **both** code and bash (same notes) |

**No public DeepSeek first-party Computer Use product** found under primary lab URLs (as of this note). Coding agents using DeepSeek as backend inherit *that agent’s* sandbox (Claude Code / Codex / OpenCode configs on [api-docs](https://api-docs.deepseek.com/)).

### 4.3 Cambridge debt (DeepSeek)

| Owes | Why |
|---|---|
| **Fork** | Open weights + harness compose local confine; no lab-shipped MicroVM fork fabric |
| **Reduce** | Harness approvals/escalation ≠ reduce; open weights make *deployer* responsible for evidence independence |
| **Authority** | Credentials subsystem exists in harness tree; no public sealed-oracle / Promote.tip contract. Hosted API `user_id` ≠ Search≠Authority |

---

## 5. Cross-lab ladder map (one slide)

| Lab | Monty | Docker | MicroVM | computer |
|---|---|---|---|---|
| **OpenAI** | Code Interpreter kernel ≈ **Monty**; SDK `UnixLocal` = local process workspace | Hosted container / `openai_hosted` / Docker client; Responses shell workspace | Partner: DigitalOcean **Firecracker** + `codex-agentapi`; E2B-class SDK clients | Computer Use (BYO desktop/browser) |
| **Anthropic** | (policy/training only) — Bash sandbox is **ns/bwrap**, not Monty CodeMode | Claude Code **on the web** cloud sandbox; CU reference **Docker** desktop | *Not* the default public story for Claude Code local | Computer use toolset (VM/container recommended) |
| **DeepSeek** | Worker-thread `codeRuntime` ≈ **Monty**; `ctx.sandbox` = **ns/bwrap** | Optional/container backends & plugins; else **self-host** | **Deployer chooses** (open weights); not a DeepSeek hosted FC product in primary docs | No first-party CU product found |

---

## 6. Who still owes fork + reduce + authority (Cambridge angle)

Spoken closer for Act I / Q&A:

1. **Isolation wall ≠ fork fabric.** OpenAI and Anthropic sell *safe rooms*; DeepSeek/Harness documents *seams*. None publish warm-parent CoW N-siblings with lineage for B’s ρ-abstain (A/J/M agenda).
2. **Harness ≠ reduce.** Agents SDK / Claude Code / dsh own tool loops and approvals. Inverse-information merge, cold-liar resistance, and `verdict=abstain` are still **B/G**.
3. **Egress proxy ≠ authority.** OpenAI vault injection, Anthropic git/credential proxy, DeepSeek harness credentials are **WIRE cousins (E)** — they do not mint sealed oracles or Promote.tip (C/D/G).
4. **Open weights shift the debt to the deployer** — DeepSeek’s honest worker-thread disclaimer is a gift for the talk: **containment ≠ EscapeBench wall**; escalate outer wall yourself (C/M).
5. **Magentic-One is Microsoft** — if a slide conflates it with Anthropic computer use, fix before stage.

| Lab | Closest to Cambridge | Still unpaid |
|---|---|---|
| OpenAI | Harness⊥compute productization; partner Firecracker path | Fork CoW · reduce/abstain · sealed promote |
| Anthropic | Dual FS+net OS confine + credential proxy honesty | Fork fabric · reduce · oracle-outside-fork |
| DeepSeek | Open composition; explicit “not a security boundary” | Managed MicroVM story · fork/reduce/authority as lab products |

---

## 7. Challenges / ROUNDTABLE handoffs

| → | Ask |
|---|---|
| **N** | Ladder cells use N’s Monty≠EscapeBench cut; Claude Code / dsh `ctx.sandbox` = ns/bwrap, not Monty CodeMode. |
| **A** | Treat lab “sandbox” marketing as *session isolate*, not DeltaBox/Crab fork — keep peer ms for research systems only. |
| **C** | EscapeBench slide: Anthropic/OpenAI Docker-class defaults vs Firecracker minimum — partner FC (OpenAI×DO) is the honest MicroVM cite. |
| **E** | Anthropic mask/inject + OpenAI vault = closest public WIRE; DeepSeek harness credentials package = open analogue — still remint-on-fork. |
| **G** | None of the three expose `World.fork` / Epoch / `Promote.tip` — factory API remains speaker contribution. |
| **J/M** | Tensorlake/FC product landscape sits *beside* these labs; don’t let Codex/Claude Code slide erase MicroVM pedigree. |
| **K** | Prefer primary docs URLs above; eng blogs BACKUP only. |

---

## 8. Claim fence (O-specific)

| DO | DO NOT |
|---|---|
| Quote OpenAI Architecture / Anthropic sandbox docs / DeepSeek harness notes | Claim OpenAI “is Firecracker” without the DigitalOcean (or other primary) cite |
| Say Magentic-One is **Microsoft** | Attribute Magentic to Anthropic |
| Call dsh worker-thread “containment not security boundary” (their words) | Upgrade DeepSeek API rate-limit page into a code sandbox |
| Map products onto Monty→Docker→MicroVM→computer | Equate Computer Use with a sealed oracle |
| Cambridge debt slide: fork+reduce+authority | Imply labs already solved Search≠Authority |

---

## 9. URL dump (primary index)

**OpenAI**  
- https://developers.openai.com/api/docs/guides/tools-code-interpreter  
- https://developers.openai.com/api/docs/guides/tools-computer-use  
- https://developers.openai.com/api/docs/guides/agents-api/architecture  
- https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted  
- https://developers.openai.com/api/docs/guides/agents-api/environments/providers/digitalocean  
- https://developers.openai.com/api/docs/guides/agents/sandboxes  
- https://openai.com/index/introducing-the-agents-api/ *(BACKUP)*  
- https://openai.com/index/the-next-evolution-of-the-agents-sdk/ *(BACKUP)*  
- https://openai.com/index/equip-responses-api-computer-environment/ *(BACKUP)*  
- https://openai.github.io/openai-agents-js/guides/sandbox-agents/clients/  

**Anthropic**  
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool  
- https://www.anthropic.com/news/3-5-models-and-computer-use *(BACKUP)*  
- https://www.anthropic.com/engineering/claude-code-sandboxing *(BACKUP)*  
- https://code.claude.com/docs/en/sandboxing  
- https://www.anthropic.com/research/claudes-constitution  
- Magentic (Microsoft, not Anthropic): https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/  

**DeepSeek**  
- https://api-docs.deepseek.com/  
- https://api-docs.deepseek.com/quick_start/rate_limit  
- https://github.com/deepseek-ai/DeepSeek-V3  
- https://huggingface.co/deepseek-ai  
- https://github.com/deepseek-ai/deepseek-harness  
- https://deepseek-harness.github.io/deepseek-harness/  
- https://deepseek-harness.github.io/deepseek-harness/en/reference/subsystems/sandbox  
- https://cdn.jsdelivr.net/gh/deepseek-ai/deepseek-harness@master/.agents/notes/implemented/feature/2026-07-06-sandbox.md  
- https://cdn.jsdelivr.net/gh/deepseek-ai/deepseek-harness@master/.agents/notes/implemented/feature/2026-06-15-ptc.md  

---

*Researcher O · 2026-09-27 (IDT) · Cambridge SRG swarm*
