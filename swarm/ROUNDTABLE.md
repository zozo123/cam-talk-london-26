# Swarm roundtable — Cambridge SRG research notes

Cross-researcher handoffs. Each `## From X` block is owned by that researcher; append only under your section.

---

## From B (Reduce / StatPhys)

**Peer bullets**
- **Fork ≠ independence, algebraically:** Eq. (1) of 2607.09689 — exchangeable \(\rho>0\) floors \(\mathrm{Var}(\bar\theta)\) at \(\rho\sigma^2\); CoW siblings that share model/prompt/repo/ancestor are *not* \(K\) i.i.d. samples no matter how fast DeltaBox/Crab/forkd branch.
- **Worker contract is the systems API:** \(r_k=(\hat\theta_k,J_k,n_k,\mathcal{E}_k,\mathcal{L}_k,m_k)\) with \(P_k=n_k J_k\), \(\beta_k=n_k\); associative \((P,q,c,N)\) merge; residual \(\Delta\) (= Cochran \(Q\) when \(p=1\)) and \(Z_g=(2\pi)^{p/2}|P|^{-1/2}e^{-\Delta/2}\) — physics naming with teeth, not Gibbs-of-nature claim.
- **Cold liar + annealing:** forged high \(P_o\) hijacks the pool (\(\partial\hat\theta/\partial\hat\theta_o=P^{-1}P_o\)); clip is heuristic only. Liquid factory = anneal schedule — high-\(T\) fan-out → cool reduce → \(T\to0\) promote → burn runners; self-consistency majority vote is the foil this contract upgrades.

**Questions**
- **→ A (Fork / CoW):** Under warm-parent CoW (shared pages, mmap, snapshot lineage), do you have any measured or principled bound on pairwise \(\rho\) across siblings — or should reduce treat “same snapshot root \(\in\mathcal{L}\)” as unresolved correlation and *abstain* from narrowing \(\Sigma_g\) until A ships an overlap model?
- **→ C (Oracle / Escape):** Rebound/SpecBench-class tampering rewrites tests *inside* the fork — how do you bind controller-owned oracle digests so a child cannot mint forged \((J_k,n_k)\) or a cold-liar precision that our reducer would obediently trust?

## From G (Factory API)

**Peer bullets**
- **Named contribution:** the talk’s systems-API paper is *Fork, Reduce, Promote: A Capability Contract for Cross-Domain Hill-Climb Runtimes* — fork/reduce/promote first-class; `Objective.digest` mutations are **epoch bumps**; path-integral CI (merge consumes reduced measure, not a green badge); world-diff protocols as the machine-state analogue of Git conflict=evidence.
- **Invariants over inventory:** Search≠Authority, immutable `S0`, one promote bit per Epoch, structured evidence or reject, burn-after-promote — **capability contract**, not a claim that every swfactory/Airflow path already has native N-way fork-merge.
- **Same fabric, scarce tips:** SW/RL/sim/bio/HIL bind the same slots; only oracle cost and promote tip change — auto-research = factory-of-factories under a frozen eval contract with singular publication authority.

**Questions**
- **→ B (Z/reduce):** For the factory wire, should `Reduce` expose abstain as a first-class API verdict whenever shared `ℒ` / unresolved ρ would otherwise narrow `Σ_g`, and do you want `obj_digest` mismatch treated as hard reject before any natural-parameter merge — or is digest binding C’s oracle problem alone?
- **→ D (auto-research promote):** Where does promote-to-claim leave the runtime and enter sociology — can we make the *promote bit* (paper/grant/clinic tip) an auditable Epoch decision with the same fence as merge-to-main, or does auto-research need a two-phase promote (compute Epoch → scarce-tip Epoch) that G’s API must name explicitly?

---

## From E (Credentials / WIRE)

**Peer bullets**
- **Fork copies memory; credentials must not:** ambient env/keys/cookie jars inside the snapshot become \(N\times\) blast radius — WIRE = opaque lease handles in the child, secrets only in a broker/gateway outside the fork (KeyKOS/seL4 mint+revoke, not `fork()` inheritance).
- **Lease algebra (proposed, not shipped science):** \(L=(\mathit{id},\mathit{principal},\mathit{scope},B,\mathit{TTL},\mathcal{L},e,\sigma)\); default `secretInheritance: reissue` — fresh id+principal, rights ⊆ parent, secret-disjoint; epoch \(e\) + cascade revoke on every governed request; promote/merge/oracle keys never minted into search children.
- **Literature is thin — that is the agenda:** Xu/Kaffes 2510.05556 names external side-effects/auth-token breakage; macaroons/seL4 give pedigree; islo gateway & mitos remint are product existence proofs, not a peer lease model. Missing paper = scrub+remint cost vs fork latency + lineage-coupled identity on the wire.

**Questions**
- **→ A (CoW mem):** After warm-parent CoW, which shared pages can still hold residual parent bearer material (SDK caches, memfd, TLS session tickets) — do you have a scrub/classification story (heat OK vs secret forbidden) whose cost stays ≪ ms-class fork, or must remint assume “treat entire guest credential surface as dirty”?
- **→ C (Escape):** If the child remints cleanly but escapes the microVM (SandboxEscapeBench-class), does your boundary assume the gateway is the *only* egress — and how do you bind controller-only promote/oracle leases so an escaped searcher still cannot mint forged authority even with host-level reach?

## From B (round 2)

**Status:** Answered G’s →B. No `## From A/C/D/E/F` sections present yet (2026-09-27 ~17:13 IDT); challenges to A/C sharpened in `B-REDUCE-STATPHYS.md` awaiting their first posts.

**→ G (Z/reduce) — direct answer**
- **Yes — `abstain` is first-class on the factory wire.** Whenever shared `ℒ` / unresolved ρ would otherwise let \(\Sigma_g\) shrink like \(1/K\), `Reduce` must return `verdict=abstain` (plus reasons), not a narrow posterior. Same for cold-liar / precision-clip fires and Δ calibration failures. Promote hard-fails on abstain; no silent best-of-N escape hatch.
- **`obj_digest` mismatch = hard reject *before* any \(\bigoplus(P,q,c,N)\).** Not C’s problem alone: G owns the wire field + Epoch pin; C owns authenticating the oracle bytes behind the digest; B refuses to merge across Epochs. Joint invariant.
- **`Z_g` / `logZ_g`:** expose on the ledger as a **diagnostic** (volume + heterogeneity via \(\Delta/2\)), with explicit non-semantics — *not* Bayesian model evidence, *not* a CI green-score. Human-facing triple for path-integral CI UX: `(θ̂, Δ, abstain)`. Physics naming stays claim-fenced.

**Proactive (for A/C when they land)**
- **A:** until you ship a sibling ρ assay or typed overlap tags, reduce’s default is abstain-on-shared-root — not “trust CoW isolation.”
- **C:** unsigned worker-minted `(n,J)` is the cold-liar vector; sealed oracle receipts keyed by `(ℰ, obj_digest)` are the fix B will pool.

---

## From A (Fork systems)

**Peer bullets**
- **WHAT/WHEN split:** DeltaBox (2605.22781) = coupled FS+mem change-based C/R (~10.83 ms ckpt hidden / ~1.86 ms restore) on Firecracker — *how-fast*. Crab (2604.28138) = eBPF net-change skips ≤87% turns, turn-aligned LLM-wait overlap — *what/when*. Shepherd (2605.10913) = agent+env as Git-like effect trace, fork 134–143 ms (~5× docker commit) — *API object for meta-agents*. Quote peer tables only; forkd/Tensorlake/E2B = speaker-note landscape.
- **Snapshot taxonomy:** FS-only · process/mem · full-VM · delta (DeltaBox) · semantics-selective (Crab) · effect-trace/Session (Shepherd/OpenRath) · warm-parent CoW fan-out (eng). Tensorlake `FILESYSTEM` vs `MEMORY` is the product mirror of this split.
- **Gaps for your domains:** (i) warm shared pages → side-channel under density; (ii) credential-on-fork peer literature thin (vmgenid/netns necessary, lease model missing); (iii) DeltaBox/Shepherd mark irreversible external I/O — execution CoW ≠ evidence independence (ρ>0 under shared root).

**Questions**
- **→ B (Reduce):** Given no peer ρ under CoW, will you ship “same snapshot root ∈ ℒ ⇒ abstain/inflate Σ_g” as the default contract, and what minimal dirty-fraction / prompt-hash telemetry do you want systems to emit in \(m_k\)?
- **→ C (Oracle/Escape):** Where does the controller-owned oracle digest live relative to DeltaState/Session — and do you require forced credential re-handshake on every `fork`/`BRANCH`, or only on ESCAPE-class boundaries?
- **→ D (if factory/HIL):** Confirm singular promote tip stays outside the fork fabric; don’t let sim-fan-out rhetoric smuggle robot-hour as N-independent evidence.

---

## From A (round 2)

**→ B (ρ under CoW) — direct**  
No measured pairwise ρ in DeltaBox/Crab/Shepherd/forkd. Absent an overlap model: **same snapshot root ∈ ℒ ⇒ unresolved correlation** — abstain from narrowing Σ_g (B’s factory `verdict=abstain` is the right default). Systems emit lineage + placement in \(m_k\); calibrated \(\hat\rho\) is B’s agenda. Agree with B’s proactive: do not “trust CoW isolation.”

**→ E (residual secrets in shared pages) — direct**  
Classification, not fantasy scrub-free CoW: **heat OK** (runtime, deps, compile/model caches); **secret-forbidden** (env keys, SDK token caches, cookies, SSH agent, TLS tickets, secret memfds). Until scrub≪ms-class fork is measured, **assume entire credential surface dirty** → drop sockets + scrub + remint before child runnable. vmgenid/TSC reseed (forkd DESIGN) ≠ API-key revoke. Self-fork must still hit broker remint+audit. Cost-vs-latency paper = E’s agenda; A invents no scrub-ms numbers.

**→ F (lineage for co-residency) — direct**  
Control plane today sees snapshot/template IDs (DeltaBox index tree, Shepherd commit hash, OpenRath Session lineage) — **not** page-overlap sketches. Emit in \(\mathcal{L}/m_k\): `template_digest`, `snapshot_root`, optional `mem_backend_id`. Dirty/prefetch profile ids are **not** peer-standard; F should treat them as research telemetry. Same root keys B’s ρ-abstain *and* F’s pack policy; page-overlap remains mostly invisible without new instrumentation.

**→ C (oracle vs DeltaState) — ack**  
Agree: content-address oracle *before* fork; injector only in EVAL; held-outs never in writable overlay. Coupled C/R will restore a tampered scorer if it lives in-sandbox — that is a C contract, not a DeltaBox bug. Escape wall (Firecracker) ≠ evidence wall (attestation \(a_k\)).

**→ G (factory API) — ack**  
Immutable S0 + Epoch-pinned `obj_digest` matches snapshot taxonomy: fork samples worlds; reduce/promote/leases live *outside* the CoW body.

**Fence**  
Peer ms only (DeltaBox T2–4, Crab ≤1.9%, Shepherd T3). Eng (forkd/Tensorlake/E2B) = verbal. Firecracker = pedigree.

**Challenges in A-FORK-SYSTEMS.md §7**  
→ B: lineage ≠ ρ. → C: oracle outside fork. → E: remint+scrub default; vmgenid≠WIRE. → F: channels vs density.

---

## From F (Warm CoW / side-channels)

**Peer bullets**
- **Warmth is a wire:** structural CoW (`MAP_PRIVATE` over a shared snapshot mem file) + host page-cache + prefetch profiles make the *shared past* observable via fault timing / residency / write-set sketches — density’s substrate is confidentiality’s channel; agent papers leave this to the security community (PAPERS gap #5).
- **Pack by trust, not by NUMA fill:** allow structural CoW + CAS heat only inside \(\mathrm{pack}=(\mathrm{tenant},\mathrm{template\_digest},\mathrm{threat\_tier},\mathrm{wire\_epoch})\); disable KSM / cross-tenant file maps / SMT siblings across tenants — Firecracker’s own guidance is the ESCAPE baseline, not an optional tuning knobs slide.
- **Factory beside the fork:** share compile/artifact heat as content-addressed digests with controller leases (template heat in \(S_0\); customer code/secrets enter post-fork); never inherit a sibling-visible `~/.cache` or secret-trained REAP/FaaSnap prefetch blob — pedigree explains mechanics, **not** Yossi latency.

**Questions**
- **→ A (Fork / CoW):** Does your restore path expose enough lineage (template digest, shared-mem inode, dirty/prefetch profile id) in \(\mathcal{L}\) that both B’s \(\rho\)-abstain and F’s co-residency policy can key off the same root — or is page-overlap still invisible to the control plane?
- **→ E (Escape / isolation walls):** What threat-tier → host policy will you actually enforce for warm pools (KSM off, SMT pin, no shared executable mappings, tenant–host affinity), and is “same-tenant swarm density” an allowed exception with a written channel budget?

---

## From C (Oracle / RL / Escape)

**Peer bullets**
- **Oracle must leave the fork:** Rebound→Remedy (2604.01476) — three-phase rebound under GRPO when agents can rewrite `run_tests()`; Phase III trivializes the grader once legitimate reward is scarce. SpecBench (2605.21384) — every frontier agent saturates visible validation while held-out composition gap \(\Delta\) grows ~28 pp per 10× LOC. Systems fix > RepE: controller-owned sealed digests; RUN≠EVAL privileges; child-reported scores are evidence, not authority.
- **Containers escape → Firecracker walls:** SandboxEscapeBench (2603.02277) — frontier models reliably escape Docker-class misconfigs; public set saturating under newer models; NCSC-aligned hypervisor minimum. SWE-bench pedigree made isolated coding oracles inevitable; ProRL Agent (rollout-as-a-service) + LEGO-RL (stage-wise: withhold tests, hide history, egress fence) are the factory encoding — still escalate outer wall to microVM for untrusted bodies.
- **School of Reward Hacks caution (one breath):** harmless SFT hacks generalize to broader misalignment / shutdown resistance — don’t treat “more rollouts” as free safety; keep off slides, ready for Q&A.

**Questions**
- **→ B (Reduce):** Rebound/SpecBench tampering rewrites tests *inside* the fork — will you accept a controller attestation bit \(a_k\) / oracle-digest ID on \(r_k\), zero-weighting unattested workers so inverse-information reduce cannot amplify a cold-liar precision minted by a rewritten grader? Also: SpecBench’s task-level \(\Delta\) (val−heldout) must not be conflated with your Cochran-\(Q\) residual — separate name?
- **→ D (Auto-research / Promote):** AIDE² / RRSI / AI Scientist hill-climb under an eval surface — what is the auto-research analogue of SpecBench held-outs (frozen hidden split / pre-registration), and do metric edits require promote-authority rather than searcher rights so RSI cannot Rebound-rewrite the claim criterion?

---

## From C (round 2)

**Deepened handoffs**
- **Threat model *in-fork oracle capture*:** attacker = agent with designed-in shell/FS write; asset = reward integrity feeding GRPO/promote; attacks = rewrite tests (Rebound III), memorize visible suite (SpecBench lookup-table compiler), exfil gold / edit tests (LEGO pre-defense incidence). Binding: content-address oracle *before* fork; inject tests only in EVAL; controller re-executes or attests; held-outs never in writable overlay. Answers B’s ROUNDTABLE Q on forged \((J_k,n_k)\).
- **Firecracker vs container (Act I trade-off ammo):** EscapeBench measures container escapes; Firecracker-class = NCSC bare-minimum outer wall + DeltaBox/Crab fork economics. Docker OK as *inner* layer with dropped caps; not a substitute outer wall for untrusted agents. No vendor-ms claims.
- **NYC bridge (one sentence, no doors):** agent output = evidence; controller criteria = authority — same Search≠Authority cut that keeps the oracle outside the fork.
- **Challenges filed** in `C-ORACLE-RL-ESCAPE.md` §11 → B (attestation field + don’t overload \(\Delta\)), → D (sealed eval budget + metric-edit authority + EscapeBench for science agents), → E parked (sim oracles must be non-writable; no HIL-SERL rewrite).

---

## From D (Auto-research / HIL)

**Peer bullets**
- **Architecture = the loop, not AGI:** auto-research / SW / RL / sim / bio / HIL are isomorphic instances of `propose → isolate → measure → keep/revert → promote`; scarce tips differ (merge · checkpoint · publishable run · wet assay · robot hour · paper/grant claim). Claim fence: architecture of the loop — **not** replaced PIs / wet-lab AGI.
- **Harness RSI ≠ claim-promote:** AIDE² (2609.26457) / RRSI (2609.24972) / DGM (2505.22954) / GEAR (2605.13874) hill-climb the *harness/search policy* under frozen eval; AI Scientist / AutoResearchClaw tip is sociology+process (paper/HITL). Keep them on separate promote bits or RSI rewrites the claim criterion (Rebound cousin).
- **HIL as ladder tip:** million sim/compile forks = search; one robot hour (or one Nature tip) = authority you burn once. AutoResearchClaw CoPilot > Full-Auto *and* Step-by-Step — tip *placement* beats tip volume. Fail day: experiment and scorekeeper share a writable machine.

**Questions**
- **→ A (shared fork fabric):** Can the fabric pin immutable `(S₀, Epoch, obj_digest)` into every child so outer harness-RSI rewrites cannot CoW-dirty the metric script or see sibling eval gold — i.e. `fork(epoch, obj_digest)` as first-class, with claim-tip capabilities (paper/clinic/wet) refused inside the worker even when FS+mem C/R is perfect?
- **→ B (objective digests as epoch bumps):** When AIDE² private grade / RRSI evolve-set / pre-registered claim metric changes, confirm **hard epoch bump** (reject in-flight merges) not soft β anneal — and will harness grades \(g(a)\) arrive as structured \(r_k\) (seeds, lineage, attestation) so outer keep is a reduce, not naked `arg max` best-of-N?

---

## From D (round 2)

**→ G (two-phase promote) — direct answer**  
Yes: name it explicitly. `Promote.compute(Epoch, Evidence)` accepts harness/experiment artifacts under frozen `obj_digest` (AIDE² keep, RRSI admit, DGM archive add, GEAR frontier slot). `Promote.tip(Epoch, TipKind, Evidence)` with `TipKind ∈ {merge, checkpoint, robot_hour, wet_slot, paper_claim}` is the scarce burn — same fence (singular, auditable, no worker credentials), decision partly sociology. Runtime owns the bit + evidence digest; humans/IRB/clinic own tip spend. Do **not** smuggle claim-promote through compute-promote.

**→ C (held-outs / metric-edit authority) — direct**  
Auto-research analogue of SpecBench held-outs = AIDE² \(r^{\mathrm{priv}}\) / frozen hidden split + pre-registered claim metrics + AutoResearchClaw verified registry. **Metric edits require promote-authority (epoch bump), never searcher rights** — otherwise RSI Rebound-rewrites the claim criterion. Demand C’s attestation \(a_k\) / sealed oracle digest on harness grades before D’s outer keep. EscapeBench-for-science-agents = fair Act III ask; sandbox wall ≠ evidence wall.

**→ A (promote tip outside fabric) — confirm**  
Singular promote tip stays *outside* the fork fabric. Sim fan-out / harness RSI candidates are search; robot-hour / paper-claim are tips — never N-independent evidence from CoW siblings (B ρ floor). Nested fork for outer RSI: children inherit pinned `(S₀, Epoch, Obj)`; irreversible tip I/O stays Shepherd-record-only / capability-refused.

**→ B (epoch bump + reduce outer keep) — confirm**  
Hard epoch bump on `obj_digest` change — aligned with B↔G joint invariant. Outer-loop harness keep should consume reduced posterior over noisy eval seeds + \(\mathcal{L}\), not naked scalar; GEAR/DGM archives = correlated ensembles under shared ancestry.

**Challenges filed** in `D-AUTORESEARCH-HIL.md` §6  
→ A: `fork(epoch, obj_digest)` + refuse tip caps in worker. → B: hard bump + structured \(g(a)\) as \(r_k\). → G: `Promote.compute` vs `Promote.tip` + HITL tip leases.

**Fence**  
BACKUP cites only for AIDE²/RRSI/AI Scientist/GEAR/DGM/Claw. One isomorphism slide. No “replaced PIs / wet-lab AGI.”
