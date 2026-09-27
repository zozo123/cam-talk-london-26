# Deck beats — Cambridge SRG · Forkable Sandboxes
**Talk:** CL SRG · Thu 15 Oct 2026 · FW11 · 15:00–16:00 Europe/London  
**Speaker:** Yossi Eliaz · Repo: zozo123/cam-talk-london-26  
**Rule:** ≤18 slide intents · on-slide cites from **deck five only** · no vendor / eng latency numbers

## Deck five (only these on slides)

| # | Cite | Short form on slide |
|---|---|---|
| 1 | Firecracker — Agache et al., NSDI’20 | Firecracker (NSDI’20) |
| 2 | DeltaBox — Dong et al., arXiv 2605.22781 | DeltaBox (2605.22781) |
| 3 | Shepherd — Yu et al., arXiv 2605.10913 | Shepherd (2605.10913) |
| 4 | Evidence-Aware MapReduce — Eliaz, arXiv 2607.09689 | Boltzmann / EA-MapReduce (2607.09689) |
| 5 | From Rebound to Remedy — arXiv 2604.01476 | Rebound→Remedy (2604.01476) |

Verbal / Q&A only (never on-slide): Crab, Xu–Kaffes, OpenRath, EscapeBench, SWE-bench, forkd / Tensorlake / E2B / Daytona ms, AIDE² / RRSI / GEAR / DGM numbers.

---

## Beats (17)

### 1. Title
- **Purpose:** Name venue, talk, and the substrate claim in one glance.
- **On-slide cite:** —
- **Spoken cue:** “Forkable sandboxes: the runtime layer for AI software factories — cheap forked machines for search, authority that never lives inside them.”

### 2. Hook — agents run code
- **Purpose:** Move the room from autocomplete to OS: the missing layer is a machine you can fork like a process.
- **On-slide cite:** —
- **Spoken cue:** “Docker made apps portable. Forkable sandboxes make agent trajectories portable.”

### 3. One-sentence talk + mantra
- **Purpose:** Lock the Search≠Authority spine before any systems detail.
- **On-slide cite:** —
- **Spoken cue:** “Burn the runner. Keep the proof. Fork the machine, not the trust.”

### 4. Scarcity ladder
- **Purpose:** Show why one substrate serves software, RL, and HIL — plural search vs singular tip.
- **On-slide cite:** —
- **Spoken cue:** “A million compiles are search. One merge — or one robot hour — is authority you can burn.”

### 5. Act I — six surfaces
- **Purpose:** State the execution contract: FS, wire+creds, reproducibility, fast cloning, warm factory beside trust, recovery/observability.
- **On-slide cite:** —
- **Spoken cue:** “These are capability slots, not a product inventory. If any slot is missing, the factory lies.”

### 6. Isolation wall — microVM pedigree
- **Purpose:** Anchor the outer wall: untrusted agents with a shell need Firecracker-class isolation, not density-only containers.
- **On-slide cite:** Firecracker (NSDI’20)
- **Spoken cue:** “Firecracker is the pedigree every agent sandbox cites. Escape wall first; ergonomics second.”

### 7. Fork as OS primitive — how-fast twin
- **Purpose:** Show change-based coupled FS+mem C/R as the systems twin of ‘fork is the API’ for agent search.
- **On-slide cite:** DeltaBox (2605.22781)
- **Spoken cue:** “DeltaBox makes every checkpoint cheap under LLM wait — authors’ measurements, not mine. How-fast, not what-to-skip.”

### 8. Fork as value — meta-agent API
- **Purpose:** Elevate fork from ms trick to a first-class object a supervisor can hold, revert, and rewrite.
- **On-slide cite:** Shepherd (2605.10913)
- **Spoken cue:** “Shepherd makes the checkpoint a value a meta-agent can hold — Git-like effect trace, not just a restore path.”

### 9. Parallel-worlds diagram ★
- **Purpose:** One diagram for the whole talk: \(S_0\) → fork \(N\) → run → reduce → promote once → burn; shared past, divergent futures.
- **On-slide cite:** —
- **Spoken cue:** “A fork is a parallel world with a shared past. A promote is world-selection. CoW siblings are replicas — not yet independent evidence.”

### 10. Three factories, one loop
- **Purpose:** Tell `snapshot → fork N → search → reduce → promote → burn` with three noun sets (SW / RL / HIL).
- **On-slide cite:** —
- **Spoken cue:** “Same slots. Different oracles. Only the tip gets scarcer.”

### 11. Software factory — Cell / epoch
- **Purpose:** swfactory/OpenClaw/pstack gift: worker ≠ authority; Cell crash ≠ epoch death; sibling reuse ≠ confirmation.
- **On-slide cite:** —
- **Spoken cue:** “Sandbox 17 crashes; sandbox 18 retries; the epoch still owns the work. Shared laptop swarm is theater.”

### 12. RL factory — oracle outside the fork
- **Purpose:** Prove why scorers must not live in writable child FS: agents rewrite tests when reward is scarce.
- **On-slide cite:** Rebound→Remedy (2604.01476)
- **Spoken cue:** “Rebound Phase III: when legitimate reward is scarce, the agent rewrites `run_tests()`. Oracle digests stay controller-owned.”

### 13. HIL tip — ladder extreme
- **Purpose:** Position robot hour / wet slot as the scarce promote, not a different sandbox story.
- **On-slide cite:** —
- **Spoken cue:** “HIL is the extreme of the same ladder: burn a million sim forks before you spend the arm.”

### 14. β / Z / cold-liar beat ★
- **Purpose:** Act II½ physics-with-teeth: Eq. (1) variance floor; worker record; forged \(P_o\) hijacks the pool; clip = heuristic.
- **On-slide cite:** Boltzmann / EA-MapReduce (2607.09689)
- **Spoken cue:** “β is not mystic — in the Gaussian reduce it’s sample size. A cold liar forges that coldness. Isolation does not authenticate \(n\).”

### 15. Capability contract — Fork / Reduce / Promote
- **Purpose:** Name the systems-API paper: objective digests as epoch bumps; path-integral CI; world-diff as Git analogue for machines.
- **On-slide cite:** —
- **Spoken cue:** “The paper this talk contributes is the capability contract — not another sandbox microbenchmark, and not a claim every factory path already has N-way fork.”

### 16. Invariants (Search≠Authority)
- **Purpose:** Client-rely list: immutable \(S_0\), frozen Obj/Epoch, one promote bit, structured evidence or reject, abstain first-class, burn-after-promote.
- **On-slide cite:** Boltzmann / EA-MapReduce (2607.09689) *(shared with beat 14 if slide budget tight — prefer verbal cross-ref)*
- **Spoken cue:** “Abstain is a valid verdict. Unresolved ρ or digest mismatch — withhold the narrow promote. No silent best-of-N escape hatch.”

### 17. Act III open problems + close
- **Purpose:** Leave research, not a sales close: ρ under CoW, credential leases, warm heat vs side-channels, acceptance boundary, HIL tip placement.
- **On-slide cite:** —
- **Spoken cue:** “Three questions: API for forkable machine? Where does warm state live so density isn’t a channel? How do you fence authority when children outlive parents?”

---

## Staging notes

- **Must-hit diagram:** beat 9 (parallel worlds).  
- **Must-hit algebra:** beat 14 (β/Z/cold liar) — minimal latex; \(Z_g\) diagnostic only, not Bayes evidence.  
- **Never on slide:** vendor ms (forkd / E2B / Daytona / Tensorlake clone), Gibbs-of-nature claim, “we invented VMs,” replaced-PIs / wet-lab AGI.  
- **If cut to ~14:** drop 11 or 13 into spoken bridges; keep 9 and 14.
