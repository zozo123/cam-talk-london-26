# QA bank — hard SRG questions from swarm ROUNDTABLE
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Source:** Challenges A–G in `swarm/ROUNDTABLE.md` + researcher packs  
**Use:** 2–4 sentence answers Yossi can say aloud · claim-fenced · no vendor ms

---

### Q1 — CoW siblings ≠ independent evidence (A ↔ B)
**Challenge:** DeltaBox/Shepherd make execution cheap — why isn’t \(K\) forks \(K\) i.i.d. samples?  
**Answer:** Because exchangeable correlation \(\rho>0\) floors \(\mathrm{Var}(\bar\theta)\) at \(\rho\sigma^2\) no matter how large \(K\) is — shared model, prompt, repo, or snapshot root is common-mode error. Systems optimize execution isolation; reduce must not bill CoW siblings as independent evidence. Until we have a measured overlap model, same snapshot root in lineage means unresolved \(\rho\): abstain from narrowing \(\Sigma_g\), don’t pretend Firecracker walls mint independence.

### Q2 — Abstain as first-class verdict (B ↔ G)
**Challenge:** Will the factory API let reduce refuse a narrow posterior?  
**Answer:** Yes — `verdict=abstain` is on the wire whenever shared lineage lacks a \(\rho\) model, `obj_digest` mismatches the Epoch, a cold-liar / precision-clip fires, or \(\Delta\) fails calibration. Promote hard-fails on abstain; there is no silent best-of-N escape hatch. Path-integral CI’s human-facing triple is \((\hat\theta,\Delta,\mathrm{abstain})\), not a green badge.

### Q3 — Oracle digests outside the fork (C ↔ A/B)
**Challenge:** Rebound shows agents rewrite `run_tests()` inside the env — what stops forged \((J_k,n_k)\)?  
**Answer:** Content-address the oracle *before* fork; inject tests only in EVAL; never leave held-outs in a writable overlay. The child may invoke a sealed scorer and receive a signed receipt — it must not mint precision itself. Coupled C/R that restores a tampered scorer is an oracle-contract bug, not a DeltaBox feature; escape wall ≠ evidence wall.

### Q4 — Credential remint after CoW (E ↔ A)
**Challenge:** Fork copies memory — don’t children inherit API keys and cookies?  
**Answer:** Ambient credentials inside the snapshot become \(N\times\) blast radius. Default posture: treat the entire guest credential surface as dirty — drop sockets, scrub, remint opaque leases from a broker *outside* the fork. Heat (runtimes, compile caches, model weights) may share; secrets must not. vmgenid reseeds entropy; it does not revoke an inherited cloud key.

### Q5 — Warm CoW as side-channel (F ↔ A)
**Challenge:** Does density via shared pages create a confidentiality channel?  
**Answer:** Structural CoW, host page-cache, and prefetch profiles make the shared past observable via fault timing and residency. Pack by trust tier — tenant, template digest, threat tier, wire epoch — not by NUMA fill; disable KSM and cross-tenant file maps across tenants. Firecracker’s isolation guidance is the baseline, not an optional slide knob; density claims are not isolation claims.

### Q6 — Objective digest = epoch bump (D ↔ B/G)
**Challenge:** Can a searcher “improve” the metric mid-campaign?  
**Answer:** No — mutating `Objective.digest` is an authority Epoch bump, not a child patch. Soft \(\beta\) anneal only inside a declared Epoch; metric edits require promote-authority, or you get Rebound Phase III at paper scale. Mismatched `obj_digest` is a hard reject *before* any natural-parameter merge — joint G+C+B invariant.

### Q7 — Two-phase promote (D ↔ G)
**Challenge:** Is publish-a-paper the same bit as keep-an-experiment?  
**Answer:** Name them apart. `Promote.compute` accepts harness artifacts under a frozen digest; `Promote.tip` burns a scarce tip — merge, checkpoint, robot hour, wet slot, paper claim. Runtime owns the bit and the evidence digest; humans, IRB, or clinic own tip spend. Do not smuggle claim-promote through compute-promote.

### Q8 — Capability contract vs inventory (G)
**Challenge:** Does swfactory / Airflow already do N-way fork-merge?  
**Answer:** We claim a *capability contract* — what a hill-climb runtime must expose so Search≠Authority holds — not that every Cell path already ships native N-way fork. Forkable sandboxes are the body; objective digest, reduce, and promote are the spine. Bindings differ; invariants do not.

### Q9 — \(Z_g\) misuse (B ↔ G)
**Challenge:** Is the partition function Bayesian model evidence for CI?  
**Answer:** No. \(Z_g\) and \(\Delta/2\) are diagnostics of pool volume and heterogeneity under the Gaussian product kernel — useful on the ledger, dangerous as a green-score. Prefer exposing \(\Delta\), degrees of freedom, and abstain to reviewers. Physics naming here is algebra with teeth, not a claim that sandboxes thermalize.

### Q10 — Containers vs Firecracker for agents (C)
**Challenge:** Why not stay on dense containers if EscapeBench saturates?  
**Answer:** SandboxEscapeBench shows frontier models reliably escape Docker-class misconfigs; NCSC-aligned minimum for untrusted agent bodies is a hypervisor wall. Containers remain fine as an *inner* layer with dropped caps; they are not a substitute outer wall. EscapeBench measures escape — it does not authenticate evidence into reduce.

### Q11 — HIL / robot hour as tip (D)
**Challenge:** Is Physical AI a different systems story?  
**Answer:** Same fabric, scarcer tip. Million sim forks are search; one robot hour is authority you burn once. Tip *placement* beats tip volume — CoPilot-style gates beat both full-auto flood and step-by-step paralysis. Fail day: experiment and scorekeeper share a writable machine.

### Q12 — Promote tip outside the fork fabric (A/D ↔ G)
**Challenge:** Can perfect FS+mem C/R still leak authority into workers?  
**Answer:** Pin immutable \((S_0,\mathrm{Epoch},\mathrm{obj\_digest})\) into every child; refuse tip capabilities — publish keys, wet booking, promote tokens — inside the worker even when CoW is perfect. Singular promote stays outside the fork fabric; irreversible tip I/O is record-only or capability-refused. Children may outlive parents; authority must not.

---

## Staging

- Prefer **Q1, Q3, Q4, Q8** if time is short.  
- Keep **Q9** ready if someone hears “partition function” and smells Bayes cosplay.  
- Never invent forkd/E2B/Daytona latencies in answers; quote peer tables only when forced, attributed.
