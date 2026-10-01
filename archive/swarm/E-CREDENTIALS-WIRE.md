# Researcher E — Credentials / WIRE / Identity-on-fork
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Lens:** Jeff Dean (lease economics at scale) + Rich Neiger (fault / epoch fencing) + capability security (KeyKOS · EROS · CapROS · seL4)  
**Companion reads:** `STORY-SPINE.md` Act I §2 + Act III §2 + claim fence; `PAPERS-AND-SOURCES.md` gaps §4; `UNIVERSAL-HILLCLIMB.md` authority-leak row  
**Claim fence (non-negotiable):** Literature on **credential leases across CoW forks** is thin. Product systems (islo gateway, mitos `secretInheritance: reissue`) mention fresh entropy; peer papers name external side-effects but almost never ship a lease algebra. Say: *open systems problem + research agenda.* Do **not** claim a shipped universal WIRE protocol, do not invent fake papers, do not treat env-var inheritance as a security story.

---

## 0. One-line problem (Act III #2)

**Fork copies memory. Credentials must not.**  
Ambient `export API_KEY=…` / cookie jars / SSH agents / OAuth refresh tokens that live *inside* the snapshot become N× blast radius the instant you `fork(n=K)`. The right object is a **capability lease** held as an opaque handle in the child and as secret material only in a broker / gateway **outside** the fork trust boundary.

Spoken: *“CoW clones pages. Authority must be reissued, attenuated, and revocable — KeyKOS rules, not `fork()` rules.”*

---

## 1. Why this is an open systems problem (literature honesty)

| What exists | What it actually covers | Gap for forkable sandboxes |
|---|---|---|
| Classic ocap: KeyKOS, EROS/CapROS, seL4 CDT (mint / copy / revoke) | Explicit delegation; no ambient authority; revocation trees | Designed for processes/objects, **not** agent microVM CoW + brokered cloud APIs |
| Macaroons (Birgisson et al., NDSS’14) | Bearer + attenuating caveats; hierarchical delegation | No native “on fork, reissue child” runtime contract; no CoW snapshot story |
| SPIFFE/SPIRE, workload identity | Short-lived SPIFFE IDs for VMs/pods | Identity of *workload*, not of *forked search sibling* with lineage badge |
| Xu/Zhou/Wu/Kaffes arXiv 2510.05556 | Names **external side-effects**: live sockets, auth tokens, cloud APIs break under snapshot/restore | Agenda paper — pinpoints the hole; does not propose a lease algebra |
| Agent libOS arXiv 2606.03895 | Process-like + capability boundaries for long-running agents | ESCAPE/KEY framing; not fork-time WIRE refresh |
| Shepherd / OpenRath | Lineage / session as branchable value | Track *what forked*; not *what authority the child may still wield* |
| Product: islo gateway, mitos captokens (`secretInheritance: reissue` default) | Fresh child credentials; budget/scope attenuation | Engineering practice ≠ peer lease model; cite as *existence proof of demand*, not as solved science |

**Honest SRG line:** peer literature is thin on lease models for WIRE after CoW. That thinness *is* the talk’s research gift — leave the room with an agenda, not a vendor slide.

---

## 2. Architecture proposals (capability contract, not product claim)

### 2.1 Separation invariant (Search ≠ Authority on the wire)

```
┌──────────────── controller / epoch ────────────────┐
│  lease mint · revoke · budget ledger · audit       │
│  secrets NEVER enter child memory                  │
└──────────────┬─────────────────────────────────────┘
               │ opaque handle / captoken / macaroon
               ▼
┌──────────────── forked sandbox (search body) ──────┐
│  FS + mem + processes  (CoW OK)                    │
│  WIRE = handle only; egress via brokered gateway   │
│  no ambient env keys; no parent bearer bytes       │
└────────────────────────────────────────────────────┘
```

Matches spine Act I surface #2: *brokered wire; no ambient keys in the child.*  
Matches hill-climb failure row: *authority leak = worker holds publish / merge / booking token.*

### 2.2 Lease object (proposed systems API)

A lease \(L\) is not a string secret; it is a **revocable capability record**:

\[
L = \big(\mathit{id},\; \mathit{principal},\; \mathit{scope},\; B,\; \mathit{TTL},\; \mathcal{L},\; e,\; \sigma\big)
\]

| Field | Meaning | Fork rule |
|---|---|---|
| \(\mathit{id}\) | Opaque handle the child presents | **New** id per child (never copy parent handle value) |
| \(\mathit{principal}\) | Identity of *this* sandbox / Cell | Fresh principal on fork (identity-on-fork) |
| \(\mathit{scope}\) | Allowed actions (net hosts, tools, `exec`/`files`/`fork`/…) | Child ⊆ parent (attenuation only) |
| \(B\) | Budget (calls, bytes, \$ , tokens, robot-minutes) | Child budget ≤ remaining parent budget; dual-entry ledger |
| \(\mathit{TTL}\) | Absolute / sliding expiry | Child TTL ≤ parent TTL |
| \(\mathcal{L}\) | Fork lineage badge (ties to reduce \(\mathcal{L}_k\)) | Append child edge; never erase ancestor |
| \(e\) | Epoch / generation (Neiger-style fence) | Child stamped with current epoch; stale epoch → deny |
| \(\sigma\) | Broker signature / macaroon caveat chain | Re-sealed at mint; child cannot widen |

**Invariant:** \(\mathrm{rights}(L_{\mathrm{child}}) \subseteq \mathrm{rights}(L_{\mathrm{parent}})\) and \(\mathrm{secret}(L_{\mathrm{child}}) \cap \mathrm{secret}(L_{\mathrm{parent}}) = \emptyset\).

### 2.3 Fork-time protocol (reissue, never inherit)

Default policy name (borrowed from mitos product language, elevated to agenda): **`secretInheritance: reissue`**.

1. Parent presents \(L_p\) (or controller initiates fork).  
2. Broker checks \(B_p > 0\), \(\mathit{TTL}\), epoch \(e\), revocation set.  
3. Broker **mints** \(L_c\) with fresh \(\mathit{id}\), fresh principal, attenuated \(\mathit{scope}/B/\mathit{TTL}\), lineage \(\mathcal{L}_p \| c\), same or newer epoch.  
4. Parent bearer material is **not** mapped into child pages (scrub / never-present). Snapshot restore of warm parent must run a **credential scrub + remint** pass before the child is runnable.  
5. Audit ledger records `(fork, parent, child, attenuations)` — same path as controller-initiated create (no self-fork side channel that bypasses policy).

Opt-in `inherit` is a **hazard flag** for SRG: only for non-secret handles (e.g. public read-only artifact URLs), never for promote/merge/publish.

### 2.4 Gateway as the only egress (WIRE = brokered)

- Child opens TCP only to the gateway (or uses vsock / virtio-net ACL).  
- Gateway verifies lease, deducts budget, applies host allowlist, injects real credential **ephemerally on the wire to the upstream**, never writes it back into the guest.  
- Upstream sees per-child identity (SPIFFE-like or signed `X-Sandbox-Id` + lineage) so rate limits / abuse / audit attribute to the **search sibling**, not the warm parent.  
- Promote path uses a **different** lease class held only by the controller (publish keys, merge token, robot-hour booking) — never minted into search children.

### 2.5 Identity-on-fork (KEY × WIRE)

Cell identity + epoch fencing (swfactory gift) must extend to network principal:

- Crash of sandbox 17 → sandbox 18 retry under **same epoch work item**, **new** lease principal.  
- Sibling forks are **distinct principals** even if CoW-shared pages look identical.  
- Evidence records \(r_k\) already carry \(\mathcal{L}_k\); WIRE should stamp the same lineage on egress so reduce and audit share one DAG.  
- “Children outlive parents” (spine close Q3): leases must survive parent death via **controller ownership** of the revocation tree — seL4 CDT intuition: revoke descends; orphan children do not inherit dangling parent authority.

### 2.6 Three factories, one WIRE law

| Factory | Search lease may | Must never hold |
|---|---|---|
| Software | clone repo read, run tests, call model API under budget | merge-to-main / release signing / prod deploy |
| RL post-training | rollout env step, log under shard id | checkpoint promote / reward-model write / oracle digest mint |
| HIL | sim / synthetic plant I/O | real-arm booking / human-hour schedule / wet-lab unlock |

Same attenuation algebra; different scope vocabularies.

---

## 3. Failure modes (SRG will ask)

1. **Ambient inheritance (classic).** Snapshot contains `.env`, browser profile, `SSH_AUTH_SOCK`, cloud SDK cache → N children share one key → one escape = full tree compromise.  
2. **Handle confusion.** Child A presents child B’s handle (if handles are guessable or CoW-shared in a mem region). Mitigate: high-entropy ids; handles live in broker-side map, guest holds only unguessable token; scrub shared pages that held parent token.  
3. **Budget double-spend.** Parent and children race the same \(B\) without a ledger → overspend. Need atomic deduct at gateway + per-tree remaining budget.  
4. **TTL / revoke lag.** Parent revoked; child still accepted until next check. Cascade revocation must be **checked on every governed request** (macaroon practice), not only at mint.  
5. **Epoch split-brain.** Promote under epoch \(e\); late child of epoch \(e-1\) still holds live lease → writes after authority moved. Fence: epoch in caveat; gateway denies mismatched \(e\).  
6. **Warm-cache credential bleed.** Shared compile artifact cache is fine; shared `~/.aws` is not. Warm state must be **classified**: heat OK, secrets not (ties to Act III #3 + A’s CoW pages).  
7. **Self-fork agency without audit.** Agent calls `Fork()` inside the guest and expects inherited secrets for “tree search.” Without controller materialization, this is a side channel. Design: self-fork still goes through broker remint + audit (mitos docs’ intent).  
8. **Oracle / promote confusion.** Lease that can rewrite tests or mint \((J_k,n_k)\) (Rebound-class) is an ESCAPE×WIRE failure — oracle digests and promote keys are controller-only (hand to C).  
9. **Restoration of live sockets.** Xu/Kaffes: restore invalidates TCP seq + peer-held auth. Naïve “resume TLS session” re-attaches old identity. Correct: drop sockets on fork; remint; re-handshake under child principal.  
10. **Statistical coupling via shared upstream quota.** Distinct leases still share a model-provider account → correlated throttling / poisoning. Lineage-aware rate limits are research, not solved.

---

## 4. Related-work scraps (cite carefully; no invented papers)

**Capability pedigree (verbal credit, not “we reimplemented KeyKOS”):**
- KeyKOS / EROS / CapROS — object capabilities; no ambient authority; factory/keeper patterns.  
- seL4 — segregated caps; `Mint` with subset rights; capability derivation tree; recursive revoke.  
- Macaroons (Birgisson, Politz, Erlingsson, Taly, Vrable, Lentczner — NDSS 2014) — attenuating bearer credentials; caveat chains; closest crypto cousin to fork-time reissue.

**Agent/systems papers that *touch* the hole without closing it:**
- Xu, Zhou, Wu, Kaffes — *Toward Systems Foundations for Agentic Exploration*, arXiv 2510.05556 — external side-effects + auth tokens under snapshot/restore. **Frame talk as answering this agenda for WIRE.**  
- Agent libOS, arXiv 2606.03895 — capability-controlled long-running agents (BACKUP KEY/ESCAPE).  
- Shepherd (2605.10913), OpenRath (2606.19409) — lineage/session objects; pair with leases so authority has the same DAG as evidence.  
- Rebound→Remedy (2604.01476) — why oracle/promote credentials must not live in the fork.  
- SandboxEscapeBench (2603.02277) — escape justifies microVM wall; escape + inherited creds = catastrophe.

**Product / eng existence proofs (name once, claim fence):**
- islo.dev gateway-enforced isolation (Harbor etc.); brokered egress as product pattern.  
- mitos captoken / capability budgets / `secretInheritance: reissue` — engineering articulation of remint-on-fork; **not** a peer lease paper.

**Deliberately out of scope as “solved WIRE”:** plain Docker `--env-file`, Kubernetes Secret mounts copied into every replica, long-lived cloud IAM keys in AMI snapshots.

---

## 5. Research agenda (what to leave SRG with)

### A. Lease algebra for CoW forks
Formalize mint / attenuate / revoke / epoch-fence with proofs that child rights ⊆ parent and secret disjointness survives snapshot restore. Connect to seL4 CDT + macaroon caveats; add **fork** as a first-class derivation that *always* remints.

### B. Scrub + remint cost model (Dean economics)
Measure: pages touched to purge credential material from warm parent; remint latency vs Firecracker/DeltaBox fork latency; when scrub dominates ms-class forks. Goal: WIRE tax ≪ fork tax, or fork is lying about being cheap *and* safe.

### C. Lineage-coupled identity
Bind lease principal to evidence \(\mathcal{L}_k\) so reduce, audit, and egress share one DAG. Open: does shared upstream quota induce a \(\rho\) term B’s reducer must know?

### D. Fork-aware remote services
Xu/Kaffes ask for versioned side-effects (S3-like). Agenda: which cloud APIs should accept a lineage badge and isolate branch writes? Which must stay controller-mediated forever (promote, payment, physical actuators)?

### E. Threat model + escape composition
Compose WIRE leases with C’s escape boundary: microVM wall without remint is incomplete; remint without escape wall is theater. Propose a joint “Door” map aligned with Zenity NYC talk without reusing that script.

### F. Measurement study (missing paper)
Instrument N sibling forks under (a) env inherit, (b) remint+attenuate, (c) remint+budget ledger. Report: credential fan-out count, revoke latency, double-spend attempts caught, warm-cache false sharing of secret pages. **This paper does not exist yet — that is the point.**

---

## 6. SRG-ready open questions (slide candidates)

1. **API:** Is the right WIRE primitive `lease_mint(parent, attenuate)` returning an opaque handle, or a macaroon the guest may further attenuate offline? Trade-off: offline attenuation vs gateway-enforced budget ledger.  
2. **Where do secrets live so density ≠ side channel?** Warm CoW pages vs encrypted broker store vs per-child sealed memfds — who wins under ms forks? (Hand to A.)  
3. **How do you fence authority when children outlive parents?** Controller-owned revocation tree + epoch in every caveat — is that enough when promote already fired?  
4. **Can statistical reducers trust egress-attributed evidence?** If leases are distinct but upstream identity collapses, is \(\mathcal{L}\) on the wire mandatory for B’s \(\rho\) model?

---

## 7. Act placement + spoken lines

- **Act I surface #2:** one diagram — handle in guest, secret in gateway.  
- **Act III #2:** “Credential leases across forks — capability handles, not env inheritance.” Then: literature thin → agenda A–F.  
- **Close mantra alignment:** *Burn the runner. Keep the proof. Fork the machine, not the trust.* Trust here = leases + promote keys.  
- **Do not say:** we solved WIRE; every islo path remints; macaroons are deployed in your factory; fork guarantees credential independence.

---

## 8. Handoffs

| Peer | Need from them | Offer to them |
|---|---|---|
| **A (CoW mem)** | Which shared pages can hold residual secrets after fork? Scrub cost vs CoW sharing. | Classification: heat vs secret; remint must run before child runnable. |
| **B (Reduce)** | Lineage \(\mathcal{L}\) already in \(r_k\) — stamp same on WIRE egress? | Distinct lease principals ≠ independent evidence; shared upstream may induce \(\rho\). |
| **C (Escape)** | Escape after remint still dangerous if gateway mis-bound. | Compose: microVM wall + no ambient keys + controller-only promote leases. |

---

*Researcher E pass · 2026-09-27 · agenda-first; no invented papers.*
