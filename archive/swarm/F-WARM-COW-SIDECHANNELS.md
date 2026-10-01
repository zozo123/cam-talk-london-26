# Researcher F — Warm cache / CoW side-channels / density vs isolation
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Owner framing:** Yossi Eliaz · security+systems lens (Spectre-class intuition for agent sandboxes)  
**Owns PAPERS gap §7.5:** *Warm shared pages as side channels — density vs confidentiality under CoW mem sharing is understudied in agent papers (security community separate).*  
**Companion reads:** `PAPERS-AND-SOURCES.md` §A + gap #5, `STORY-SPINE.md` Act I #5 / Act III #3 / SRG Q2, `PARALLEL-WORLDS-STATPHYS.md` (interference ≈ fake independence)  
**Claim fence (non-negotiable):** pedigree cites (Firecracker / Catalyzer / REAP / FaaSnap) explain *mechanics*, not *your* latency. **Never** present vendor, forkd, DeltaBox, E2B, or islo restore numbers as Yossi benchmarks. Demo economics ≠ measured claim. Say: *warmth is a placement decision; the research question is where heat may live without becoming a channel.*

---

## 1. One-slide thesis (what SRG should hear)

| Density win | Confidentiality cost | Systems move |
|---|---|---|
| Structural CoW from one snapshot root (MAP_PRIVATE over shared mem file) | Sibling *timing* of first-write / major→minor fault reveals overlap & working set | Share **templates**, not **tenants’ live pages**; tag lineage \(\mathcal{L}\) |
| Host page-cache hit on warmed rootfs / artifact blobs | Cross-sandbox Flush+Reload / Prime+Probe cousins via shared files | Content-addressed **factory outside trust**; children get digests or FUSE leases, not RW mounts of the same cache dir |
| KSM / cross-VM page merging | Classic dedup timing + Rowhammer-locate | **Disable KSM** on multi-tenant agent hosts (Firecracker guidance); prefer structural CoW within a *trust domain* |
| Working-set prefetch (REAP / FaaSnap pedigree) | Prefetch / userfaultfd / page-walker patterns leak across co-scheduled guests | Prefetch profiles are **per-template**, never trained on secrets; isolate SMT / disable shared prefetch where threat requires |
| Warm parent → N children in ~ms class | Shared L1/L2/L3, BTB, PHT, MDS — Firecracker wall ≠ µarch wall | Density **tiers** by threat: same-tenant swarm ≠ cross-customer packing |

**Spoken line:** *“CoW makes parallel worlds cheap by sharing the past. Side channels ask whether that shared past is also a shared *wire*.”*

**Mantra alignment:** *Burn the runner. Keep the proof. Fork the machine, not the trust — and do not fork the cache into the trust domain.*

---

## 2. Spectre-class intuition for agent sandboxes

Agent sandboxes inherit the serverless threat surface, then add agent-specific amplifiers:

1. **Hostile code is the product.** Coding agents (SandboxEscapeBench-class) *try* to leave the box; assume a child that can time faults, probe `/proc`, and shape its working set.
2. **Warmth is intentional.** Unlike cold FaaS, agent factories *want* shared compile caches, warmed interpreters, prefetched snapshot pages — so the “optimization” *is* the channel substrate.
3. **Siblings are co-scheduled by design.** Fan-out `fork(n=K)` packs correlated guests on one host; µarch contention is not an accident, it is the density plan.
4. **Evidence channels ≠ covert channels — until they are.** B’s reduce agenda cares about statistical \(\rho\) from shared model/prompt/repo. F cares about *information* \(\rho\): can sandbox \(i\) learn bits about sandbox \(j\)’s secret patch, token, or held-out test via memory/timing?

**Separation of concerns for the talk:**

| Layer | Question | Owner |
|---|---|---|
| Evidence correlation | Do CoW siblings mint independent *estimates*? | B (Reduce) + A (overlap model) |
| Confidentiality channel | Do CoW siblings mint *information leakage*? | **F** + E (ESCAPE wall policy) |
| Structural escape | Can the child leave the VM / rewrite the oracle? | C / E (SandboxEscapeBench, Rebound) |

Do not collapse “fork ≠ independence” (stat) with “shared page ≠ private” (sec). Same mechanism, different harm.

---

## 3. Taxonomy: warm shared pages as side channels

### 3.1 Structural CoW (snapshot restore) — *intended* sharing

Firecracker snapshot restore maps guest memory with `MAP_PRIVATE` over a shared memory file: pages fault in on demand; writes allocate private anonymous copies (CoW). Pedigree: Firecracker snapshot docs; Catalyzer `sfork` / checkpoint-image boot; REAP working-set prefetch via userfaultfd / access bits; FaaSnap concurrent / hierarchical paging.

**Channel intuitions (not a PoC checklist):**

- **Fault-timing oracle.** Time-to-touch distinguishes: already-resident shared page vs major fault from disk vs CoW break on first write. A sibling that shares the same backing file learns whether another guest has already warmed (or dirtied) a region — a coarse working-set radar.
- **Prefetch profile leakage.** REAP/FaaSnap-style prefetch sets encode “what this function touches.” If a prefetch blob is built from a secret-dependent run (private repo, customer code, held-out tests) and later applied to another tenant’s restore, the *profile itself* is a side channel — even before any cache attack.
- **Dirty-bit / mincore cousins.** Diff-snapshot and `mincore`-style residency queries (host or poorly isolated guest tooling) expose which pages left the shared template — a write-set sketch of the agent’s patch.

**Non-claim:** these are *classes* security literature already knows how to weaponize under shared memory / dedup / cache; agent papers almost never measure them. Cite existence of the *gap*, not a new CVE.

### 3.2 Accidental / opportunistic sharing — *dangerous* density

| Mechanism | Density story | Confidentiality story |
|---|---|---|
| **KSM** (kernel same-page merging) | Merge identical pages across VMs | Write-latency tells “is this page shared with someone?” — classic cross-VM dedup channel; Firecracker production guidance: **disable** |
| **Host page cache on shared rootfs / layer blobs** | One warmed `node_modules` / Cargo registry / JVM serves many guests | Shared file → Flush+Reload / Prime+Probe family if guests can map the same host pages executable/readable |
| **SMT / shared L1–L3 / shared BTB–PHT** | Pack more vCPUs per core | Spectre-PHT / BTB / MDS remain relevant *across* Firecracker guests (see microarchitectural studies of Firecracker); VMM boundary ≠ speculation boundary |
| **GPU / accelerator warm contexts** | Keep weights / CUDA contexts hot | Residual activations, timing, and memory residency across “forked” inference workers — understudied for agent tool use |

### 3.3 Agent-specific amplifiers (why this is not just “serverless again”)

- **Compile / artifact heat is high-entropy and secret-adjacent.** Build caches encode dependency graphs, feature flags, and sometimes tokens in env-derived paths. Sharing `~/.cache/go-build` across trust domains is a channel *and* a credential footgun.
- **Oracle / gold files in the warm image.** If the snapshot that children CoW-fork already contains tests, rubrics, or preference labels, every child shares that past — Rebound-class agents can rewrite *and* side-channel siblings racing the same suite.
- **Long-lived warm parents.** forkd-class “warm parent → many children” (pedigree / demo only) maximizes structural sharing — and maximizes the window where one compromised child probes the shared past.

---

## 4. Density vs confidentiality under CoW memory

### 4.1 The trade-off SRG will recognize

```
cold unique boot  ──────────────────────────────  max isolation, min density
        │
        ▼
structural CoW from template (same trust domain)
        │  ← sweet spot for *single-tenant agent swarm*
        ▼
structural CoW + host page-cache for public artifacts
        │  ← OK if artifacts are content-addressed & non-secret
        ▼
KSM / cross-tenant merge / SMT packing
        │  ← density max; confidentiality research debt
        ▼
shared RW cache mounts across tenants
              ← do not ship
```

**Rule of thumb for the talk:** *Density is allowed to share **immutable, content-addressed, non-secret** bytes. Confidentiality forbids sharing **residency, write-sets, and µarch state** across trust domains.*

### 4.2 Trust-domain packing (systems API sketch)

Define a packing key the orchestrator already almost has:

\[
\mathrm{pack}(s) = \big(\mathrm{tenant},\; \mathrm{template\_digest},\; \mathrm{threat\_tier},\; \mathrm{wire\_epoch}\big)
\]

- Same \(\mathrm{tenant}\) + same \(\mathrm{template\_digest}\) → structural CoW + shared page-cache **allowed**.
- Differing \(\mathrm{tenant}\) → **no** KSM, **no** shared executable mappings, prefer separate hosts or at least no SMT siblings; treat as ESCAPE policy (hand to E).
- Differing \(\mathrm{wire\_epoch}\) (credential lease refresh) → must not resurrect pages that could hold prior secrets (scrub / refuse template reuse that baked env).

This is the security twin of B’s lineage \(\mathcal{L}\): B uses \(\mathcal{L}\) to abstain on \(\rho\); F uses packing keys to abstain on co-residency.

### 4.3 What “independence” means at three layers

| Layer | Independence means | Failure mode if shared warmth ignored |
|---|---|---|
| Execution | Child can mutate FS/mem without breaking siblings’ *correctness* | CoW works — this is the happy path |
| Evidence (B) | Estimates uncorrelated given \(\mathcal{L}\) | Variance floor; cold liar still pools |
| Confidentiality (F) | Child learns nothing about sibling secrets via timing/residency/µarch | Covert channel / cross-tenant leak / prompt-cache radar |

Act III slide should name all three. Research debt is almost entirely in rows 2–3.

---

## 5. Share compile / artifact heat without sharing trust

STORY-SPINE Act I #5: *the warm factory sits beside the fork, not inside trust.* Operationalize that as an architecture, not a slogan.

### 5.1 Three places heat can live

| Locus | What is warm | Trust implication | Verdict |
|---|---|---|---|
| **A. Inside the snapshot** | Interpreter, pre-imported modules, warmed JIT, vendored toolchain | Every child CoW-inherits it; write-set reveals use; secrets must never be baked | **Template heat only** — public, reproducible, digest-pinned |
| **B. Host page-cache / CAS blob store** | Content-addressed build artifacts (`sha256 → bytes`) | Guests receive *copies* or verified read-through by digest; no shared RW cache dir | **Preferred for compile factories** (Cargo/npm/bazel remote) |
| **C. Sibling-visible CoW / KSM / shared mount** | Whatever another agent just compiled | Channel + poison | **Forbidden across trust domains** |

### 5.2 Factory-beside-fork contract (slide-ready)

```
[ CAS / build factory ]  --digest-->  [ controller ]
        ^                                |
        | lease(digest, epoch)           v
        |                         [ snapshot S0 : template only ]
        |                                |
        |                          fork(n=K) CoW
        |                           /  |  \
        +-- fetch(digest) -------> c1  c2  cK   (private copies / FUSE)
                                         |
                                      burn runners
                                         |
                                   evidence digests out
```

Invariants:

1. **No ambient cache mount.** Children do not inherit `~/.cache` from a warm parent that other tenants also use.
2. **Digest in, bytes out.** Fetch is authorized by controller lease (`WIRE` epoch); artifact identity is content hash, not path.
3. **Template ≠ workspace.** Snapshot \(S_0\) holds toolchain + empty workspace skeleton; customer code and secrets enter after fork under FOLDER/WIRE policy.
4. **Prefetch profiles are template-scoped.** REAP/FaaSnap-class working sets are built from public template boots, never from secret-dependent agent runs, then attached to \(S_0\) by digest.
5. **Burn returns heat to the factory, not to siblings.** On teardown, private CoW pages die; CAS retains only promoted digests the controller accepts.

### 5.3 Software-factory example (OpenClaw / swfactory / RustChina cousin)

- **Share:** prebuilt `sysroot`, sccache/CAS objects keyed by hash, warmed `rustc` *binary pages* inside a *per-tenant* template.
- **Do not share:** target/` directories across Cells, env files, token-bearing `config.toml`, test oracles, sibling incremental state.
- **Density knob:** many Cells from one tenant template via structural CoW; separate tenants → separate template digests even if toolchain version matches (optional: share *read-only CAS*, never mem-merge).

### 5.4 What not to say on stage

- Do not quote Catalyzer “sub-ms,” REAP/FaaSnap restore curves, forkd “~100 children / ~100 ms,” DeltaBox “~11 ms / ~2 ms,” or islo marketing numbers as *your* result.
- Pedigree one-liner only: *“Snapshot+CoW+prefetch is the serverless lineage Firecracker → Catalyzer → REAP → FaaSnap; agent forks reuse that lineage. Our question is the security packing policy those papers left open.”*

---

## 6. Pedigree map (backup slide / speaker notes)

| System | Year | Warmth mechanic (one line) | Relevance to F |
|---|---|---|---|
| **Firecracker** (NSDI’20) | 2020 | MicroVM + snapshot; MAP_PRIVATE CoW mem; explicit guidance: disable SMT/KSM, avoid sharing files | Isolation *intent* + honest µarch caveats |
| **Catalyzer** (ASPLOS’20) | 2020 | `sfork` / checkpoint-image; minimize critical-path restore | Ancestor of “warm parent” thinking |
| **REAP** (ASPLOS’21) | 2021 | Working-set prefetch (userfaultfd / access bits) | Prefetch set = sensitive profile if secret-derived |
| **FaaSnap** (EuroSys’22) | 2022 | Concurrent / hierarchical paging over Firecracker snapshots | Density via smarter paging; still host-shared backing |
| **DeltaBox / Crab / Shepherd / forkd** | 2025–26 | Agent-era CoW C/R & branch | Execution twins; **not** confidentiality analyses — gap #5 |

Agent literature optimizes *how fast* and *when* to snapshot. Security literature knows dedup/cache/Spectre. **The join is the Cambridge open problem.**

---

## 7. Open problems to leave SRG (Act III fuel)

1. **Overlap model for pages ↔ \(\rho\).** A’s lineage \(\mathcal{L}\) should eventually carry a page-overlap or template-digest feature so B can abstain; F needs the same feature for *co-residency policy*, not only for variance.
2. **Channel budget API.** Orchestrators expose vCPU/mem; they do not expose “max shared-page fraction with tenant X” or “SMT sibling forbidden.” What is the least API that makes density *negotiable* with confidentiality?
3. **Prefetch provenance.** Treat working-set profiles as first-class artifacts with digests and trust labels — like SBOMs for warmth.
4. **Factory attestation.** Prove the CAS object a child fetched matches the controller’s lease — close the TOCTOU between “warm hit” and “poisoned blob.”
5. **Measurement gap.** No public agent-sandbox suite reports cross-sibling fault-timing or cache-timing under CoW fan-out. A SandboxEscapeBench *cousin* for side channels would make gap #5 empirical.

---

## 8. Cross-researcher handoffs

| Peer | Need from them | Offer from F |
|---|---|---|
| **A (Fork / CoW)** | Precise restore model: shared file vs private copy; whether dirty tracking / userfaultfd is exposed; template digest in \(\mathcal{L}\) | Packing key + “structural CoW OK / KSM never” policy; fault-timing as reason \(\mathcal{L}\) must record template root |
| **B (Reduce / StatPhys)** | Keep evidence-\(\rho\) distinct from channel-\(\rho\) | Shared warmth is a *common-mode* source — same snapshot root should raise both flags |
| **C (Oracle)** | Oracle bytes never baked into warm \(S_0\) | Prefetch/oracle profiles must not be trained inside the fork |
| **E (Escape / isolation walls)** | Threat-tier → host policy (SMT, KSM, file sharing, tenant pinning) | Density ladder above; Firecracker guidance as baseline ESCAPE checklist for warm pools |

---

## 9. Spoken scraps (optional)

- “Docker shared the filesystem and called it density. CoW shares the past and calls it fork. Side channels ask who else can feel that past.”
- “Warmth belongs in a content-addressed factory. Trust belongs in a lease. The sandbox gets a copy, not a peer.”
- “If your packing policy is ‘fill the NUMA node,’ your confidentiality policy is already ‘hope.’”

---

*Researcher F pass · 2026-09-27 (Asia/Jerusalem) · owns PAPERS gap #5 · claim fence: pedigree ≠ Yossi latency.*
