# IDEATION-FULL-STORY — Cambridge SRG canonical ideation hub

**Status:** working research/story document for the Cambridge Systems Research Group seminar.  
**Purpose:** single ideation hub consolidating the strongest ideas from the current repo + the latest discussion thread before the canonical \`talk.tex\` / \`academic/*.tex\` rewrite.  
**Important:** this file is the story/decision document. The current TeX remains the delivered artifact until explicitly rewritten and rebuilt.

Cross-links worth keeping:
- \`scratch/FLOW-GATES-PAPERS.md\` — paper-tagged gates and venue mapping.
- \`scratch/AGGRESSIVE-SPINE.md\` — aggressive systems-only stage map.
- \`scratch/PAPER-STAGE-MAP.md\` — paper → slide → claim fence.
- \`CLAIM-FENCE.md\` — hard do / do-not-say boundaries.
- \`swarm/A-FORK-SYSTEMS.md\` — fork substrate.
- \`swarm/B-REDUCE-STATPHYS.md\` — reduce / correlation / stat-phys lens.
- \`swarm/C-ORACLE-RL-ESCAPE.md\` — sealed oracle / reward integrity.
- \`swarm/G-FACTORY-API.md\` — Fork/Reduce/Promote contract.
- \`swarm/H-ANNEALING-MCMC-SGD.md\`, \`swarm/I-NONEQUILIBRIUM-HAMILTONIAN.md\` — physics fences.
- \`swarm/ROUNDTABLE.md\` — cross-researcher synthesis.

---

# 1. The talk in one sentence

> **How does a possible future become admissible evidence, and how does admissible evidence become authoritative state?**

The talk is not fundamentally about “faster VMs,” RL tutorials, or a product category.

It is about three transformations:

\[
\boxed{\text{Possibility}}
\;\longrightarrow\;
\boxed{\text{Evidence}}
\;\longrightarrow\;
\boxed{\text{Authority}}
\]

- **Fork** creates alternative executable futures.
- **Reduce** determines what those alternatives actually teach us.
- **Promote** changes authoritative state.

This is the core conceptual spine.

---

# 2. Why this is bigger than coding

Do not frame code as the special case.

The relevant object is any **stateful executable environment** in which an agent can take actions and inspect resulting state:

- repository + IDE + compiler + tests,
- browser / desktop / computer-use environment,
- CAD / SolidWorks / mechanical design,
- Photoshop / Blender / graphics applications,
- game engines,
- scientific simulators,
- databases,
- EDA tools,
- operating systems,
- robot simulators,
- eventually physical experiments behind much more expensive oracles.

A useful formal world is:

\[
\mathcal W=(S,A,\Phi,O,C)
\]

where:
- \(S\) = state,
- \(A\) = actions / interventions,
- \(\Phi\) = actual transition dynamics,
- \(O\) = observables,
- \(C\) = capabilities / external side effects.

The key move:

> **An executable application is an environment.**

Once that is accepted, snapshot/fork semantics become experiment semantics.

---

# 3. The first scientific fork: predict or execute?

There are two fundamentally different ways to obtain a possible future.

### Learned / simulated transition

\[
\hat{s}_{t+1}\sim\hat P(s_{t+1}\mid s_t,a_t)
\]

A world model says:

> “I predict what would happen.”

### Executed transition

\[
s_{t+1}=\Phi(s_t,a_t,\xi)
\]

An executable world says:

> “Restore the state, apply the intervention, and observe what actually happens within the captured boundary.”

The decision is not “world models good/bad” or “forks replace models.”

It is a cost/fidelity boundary:
- use learned models when interaction is expensive, unsafe, unavailable, or impossible to reset;
- use executable branching when the relevant world is computational, state can be captured, reset is cheap enough, and actual dynamics matter more than learned approximation;
- hybrid systems are often strongest:

\[
\boxed{\text{model proposes branches; executable worlds ground them}}
\]

No RL-101 slide is needed. No taxonomy table just to teach model-free/model-based/world-model RL.

---

# 4. The executable-counterfactual object

Let \(S_0\) be a declared starting state and let \(\Delta_i\) be an intervention.

\[
\tau_i=\Phi(S_0,\Delta_i,\xi_i)
\]

A forked system attempts to create:

\[
S_0
\rightarrow
\{\Delta_1,\ldots,\Delta_N\}
\rightarrow
\{\tau_1,\ldots,\tau_N\}
\]

Examples of \(\Delta_i\):
- code patch,
- CAD operation,
- browser action sequence,
- game action,
- simulation parameter,
- graphics edit,
- policy action.

The phrase to keep:

> **Executable counterfactuals:** hold the declared past fixed, vary the intervention, observe the actual trajectory.

Claim fence: “counterfactual” here is an experimental systems term; do not claim a perfectly controlled causal intervention unless clocks, I/O, randomness and external state are actually pinned/brokered.

---

# 5. Missing gate that should be explicit: is the captured boundary sufficient?

A snapshot never captures “the universe.”

It captures a boundary \(B\):

\[
B \subset \text{all causally relevant state}
\]

The executed transition is faithful only within that declared boundary.

A VM may restore FS + memory + processes perfectly and still miss:
- GitHub / Stripe / S3,
- DNS,
- another DB,
- an LLM endpoint,
- GPU/accelerator state,
- physical sensors/actuators,
- human actions.

So the real question before “reproducible \(S_0\)?” is:

> **Is the captured executable boundary sufficient for the claim we are evaluating?**

This is the strongest bridge to world models:
- world models ask what latent state \(z_t\) is sufficient for prediction;
- forkable systems ask what executable state \(S_t\) is sufficient for faithful continuation.

Same sufficiency question; different representation.

---

# 6. Full canonical decision tree

\`\`\`text
START
  |
  v
◆ Is there a stateful world?
  FS · memory · processes · devices · network · credentials · external state
  |
  +-- no --> ordinary stateless compute may suffice
  |
  +-- yes
        |
        v
◆ Can the relevant transition be obtained directly?
  executable Φ(s,a) or only predicted by P_hat(s'|s,a)?
  |
  +-- no --> LEARN / SIMULATE
  |          world model / surrogate / external simulator
  |          (Q&A branch, not EXECUTE spine)
  |
  +-- yes --> EXECUTE SPINE
              |
              v
◆ Is the captured executable boundary sufficient for the claim?
  |
  +-- no --> expand the boundary / broker external state / use stronger oracle
  |
  +-- yes
        |
        v
◆ Can we name a reproducible S0?
  same declared starting state modulo explicit nondeterminism fence
  |
  +-- no --> build capture / replay / restore semantics
  |
  +-- yes
        |
        v
◆ Is branching economic enough to become a search primitive?
  |
  +-- no --> cold rebuild / serial execution / learned surrogate
  |
  +-- yes
        |
        v
■ FORK N
  shared declared past; divergent Δ1...ΔN
  |
  v
◆ Are sibling comparisons controlled?
  clocks · RNG · I/O · external APIs · mutable fixtures · model endpoints
  |
  +-- no --> pin / stub / broker / declare out-of-boundary
  |
  +-- yes
        |
        v
◆ Did speculative execution leak irreversible side effects?
  merge · charge · send · publish · production update · real robot action
  |
  +-- yes --> search/authority boundary already broken
  |
  +-- no
        |
        v
◆ Can the actor alter the ruler?
  objective · verifier · hidden tests · reward policy · promotion capability
  |
  +-- yes --> ■ SEAL ORACLE
  |            RUN != EVAL
  |            controller owns objective/verifier digest
  |
  +-- no
        |
        v
■ EXECUTE N TRAJECTORIES
  tau_i = Φ(S0, Δ_i, xi_i)
  each child emits structured evidence
        |
        v
◆ What dependence did the fork preserve?
  shared model · prompt · parent · cache · fixture · oracle · data · ancestry
        |
        +--> dependence bounded / modelled --> compute effective information
        |
        +--> dependence unresolved ---------> conservative reduce or ABSTAIN
        |
        v
◆ Is each worker record valid?
  same epoch?
  same objective digest?
  unique evidence IDs?
  plausible precision?
  lineage present?
  disagreement explainable?
        |
        +-- no --> REJECT / ABSTAIN
        |
        +-- yes
              |
              v
■ REDUCE
  infer over structured evidence, not majority vote
  output candidate + uncertainty + disagreement + lineage + abstain status
              |
              v
◆ Does current evidence resolve the decision?
  |
  +-- no --> sample more / stronger oracle / model / physical measurement / abstain
  |
  +-- yes
        |
        v
◆ Would acting on the result change authoritative state?
  |
  +-- no --> remain speculative / archive candidate
  |
  +-- yes
        |
        v
■ PROMOTION GATE
  current epoch?
  immutable parent identity?
  objective/verifier still current?
  evidence integrity?
  dependency policy satisfied?
  required approval?
        |
        v
◆ Is this still the current epoch?
  |
  +-- no --> evidence may remain archival, but is stale for authority
  |
  +-- yes
        |
        v
■ PROMOTE
  singular linearization point
  authoritative state changes S0 -> S1
        |
        v
■ PRESERVE RECEIPT / DISPOSE RUNNERS
        |
        v
REPEAT
\`\`\`

The decision tree is the private design document. The stage version should be visually compressed.

---

# 7. Fork semantics are experimental semantics

The important question is not merely “can I restore a machine?”

It is:

> **What does “same past” mean operationally?**

A reproducible experimental parent may need:
- filesystem state,
- memory/process state,
- dependencies/toolchain,
- clock/time policy,
- randomness policy,
- network policy,
- capability identity,
- external service broker state,
- device state,
- verifier/objective identity.

This is why Firecracker, DeltaBox, Crab and Shepherd are the **chassis**:
- Firecracker: hardware-isolated microVM pedigree;
- DeltaBox: fast/change-based checkpoint/restore;
- Crab: semantics-aware checkpointing;
- Shepherd: reversible effect-trace / branchable runtime value.

Their work makes reversible fan-out credible.

It does **not** answer what N correlated executions mean as evidence.

That is the hand-off point to the talk’s payload.

---

# 8. Security reframed academically: experimental authority must live outside the subject

Avoid the cute line “copy the machine, not the keys” as load-bearing argument.

The proper invariant is:

\[
\boxed{\text{RUN}\neq\text{EVAL}\neq\text{PROMOTE}}
\]

The child may:
- execute actions,
- mutate its local world,
- emit observations and artifacts.

The child must not silently own:
- the objective definition,
- the hidden verifier,
- the authoritative reward policy,
- the promotion capability.

The controller owns the ruler.

This is the systems interpretation of evaluator integrity / reward-hacking work such as Rebound→Remedy.

---

# 9. Speculation must be reversible; authority is deliberately committed

Move the reversibility question earlier than Reduce.

The real failure is not “can I roll back after reduction?”

It is:

> **Did speculative search leak irreversible side effects before the authority gate?**

Examples:
- sending email,
- merging,
- updating production,
- charging money,
- booking scarce hardware,
- publishing a claim.

Invariant:

\[
\boxed{\text{speculation is reversible; authority is deliberately committed}}
\]

Operational irreversibility is not a thermodynamic claim.

---

# 10. The core payload: execution independence is not evidence independence

This should be the mid-talk reveal.

Even perfect execution isolation does not make N siblings N independent witnesses.

In an exchangeable approximation with pairwise correlation \(\rho\):

\[
\operatorname{Var}(\bar X)
=
\frac{\sigma^2}{N}
\left[1+(N-1)\rho\right]
\]

and an intuitive effective sample size is:

\[
N_{\mathrm{eff}}
=
\frac{N}{1+(N-1)\rho}
\]

Examples:
- \(N=100,\rho=0.1\Rightarrow N_{\mathrm{eff}}\approx9.17\)
- \(N=100,\rho=0.5\Rightarrow N_{\mathrm{eff}}\approx1.98\)

Stage line:

> **100 isolated machines can still contain only a handful of independent witnesses.**

Why siblings correlate:
- same model,
- same prompt,
- same parent snapshot,
- same poisoned cache,
- same hidden bad fixture,
- same evaluator defect,
- same training/data ancestry.

This is the cleanest place to distinguish:
- **execution isolation**,
- **statistical/evidential independence**,
- **authority**.

They are different properties.

---

# 11. The worker must return an argument, not a scalar

Never reduce from only:

\`\`\`text
score = 0.94
\`\`\`

A useful worker record is structurally like:

\[
r_i=
(
\hat\theta_i,\,
P_i,\,
E_i,\,
\mathcal L_i,\,
M_i,\,
e_i
)
\]

where:
- \(\hat\theta_i\) = estimate/result,
- \(P_i\) = precision / uncertainty object,
- \(E_i\) = evidence IDs,
- \(\mathcal L_i\) = lineage,
- \(M_i\) = method,
- \(e_i\) = experiment epoch.

The exact tuple can evolve; the principle must not:

> **A worker returns evidence with provenance, not a naked confidence score.**

This is where Evidence-Aware MapReduce / 2607.09689 belongs.

---

# 12. Reduce is inference, not voting

Define:

\[
R=\operatorname{Reduce}(r_1,\ldots,r_N)
\]

A reducer should be able to output:
- candidate/result,
- uncertainty,
- disagreement,
- effective information,
- lineage summary,
- reason codes,
- **abstain**.

Valid terminal outcomes:

\[
\{\text{accept},\text{reject},\text{abstain}\}
\]

Abstention is required when:
- lineage overlap is unresolved,
- objective digest changed,
- evidence is missing,
- claimed precision is implausible,
- measurements disagree beyond the model,
- evidence IDs overlap unexpectedly.

This is the talk’s transition from “parallel execution” to “scientific evidence.”

---

# 13. Reduce != Promote

This deserves a dedicated slide.

A reducer may produce overwhelming support for candidate \(x\), yet promotion may still be forbidden because:
- human approval is required,
- the release window is closed,
- the epoch is stale,
- the objective changed,
- a physical assay is still missing,
- the robot is unavailable,
- policy/regulatory conditions are unmet.

So:

\[
\boxed{\text{Inference}\neq\text{Authority}}
\]

equivalently:

\[
\boxed{\text{Reduce}\neq\text{Promote}}
\]

“Search can be plural; authority must be singular” should be the **consequence** of this argument, not an early slogan.

---

# 14. Promotion semantics

Let an epoch be:

\[
e=(S_e,O_e,V_e,\Pi_e)
\]

where:
- \(S_e\) = trusted parent,
- \(O_e\) = objective digest,
- \(V_e\) = verifier identity,
- \(\Pi_e\) = search/evaluation policy.

Then:

\[
\operatorname{Promote}(x,e)
\]

is a control-plane state transition that may succeed only if:
- \(e=e_{\mathrm{current}}\),
- evidence is valid for \(e\),
- authority checks still pass,
- the relevant tip has not already been spent.

Mutating objective/verifier/trusted parent creates:

\[
e\rightarrow e+1
\]

Old evidence may remain useful as history but is stale for authority under the new epoch.

Promotion is a **linearization point** / singular authority transition.

---

# 15. The physics lens — precise, late, and fenced

Physics should not be decorative and should not appear as giant HOT/COOL/T→0 boxes.

Only introduce it after the ensemble and reducer are defined.

We have trajectories \(\{\tau_i\}\) and possibly weights \(p_i\).

A useful observable is normalized ensemble entropy:

\[
h
=
\frac{-\sum_i p_i\log p_i}{\log N}
\]

Broad support:
\[
h\approx1
\]

Concentrated support:
\[
h\downarrow
\]

A weighting family may look like:

\[
p_i(\beta)
=
\frac{e^{-\beta L_i}}{\sum_j e^{-\beta L_j}}
\]

if the chosen statistical model actually justifies that form.

Proper language:
- ensemble concentration,
- crossover,
- correlated replicas,
- observables,
- driven/open system,
- dissipative reject/burn,
- absorbing authority event.

Do **not** claim:
- detailed balance for the factory,
- equilibrium thermodynamics,
- Gibbs ensemble “of nature,”
- promotion is a free-energy minimum,
- \(T\to0\) literally equals Promote,
- a phase transition unless a sharp large-system order-parameter transition is actually demonstrated.

Academic phrasing:

> **For a finite factory, call it concentration/crossover. Reserve “phase transition” for a demonstrated sharp large-system transition.**

Critical separation:

\[
\boxed{\text{epistemic concentration does not grant permission to commit}}
\]

or verbally:

> **Even zero epistemic entropy would not create authority.**

Promotion is operational, not thermodynamic.

---

# 16. A clean physics/system dictionary

| Physics/statistics lens | Runtime object |
|---|---|
| initial/boundary condition | declared parent \(S_0\) |
| trajectory/path | child execution \(\tau_i\) |
| ensemble | forked candidate futures |
| observable | tests / reward / measurement |
| correlation | shared ancestry / shared defect |
| information/precision | evidence weight |
| entropy | diversity of plausible futures |
| driven dynamics | proposal/search loop |
| dissipation | verification / rejection / runner disposal |
| absorbing event | authoritative promotion |

Fence: this is a mathematical lens, not an identity claim.

---

# 17. The chassis vs the payload

### Cousin chassis: makes alternative executions possible

- **Firecracker (NSDI’20)** — isolation/snapshot pedigree.
- **DeltaBox (2605.22781)** — fast change-based checkpoint/restore.
- **Crab (2604.28138)** — semantics-aware checkpointing.
- **Shepherd (2605.10913)** — reversible effect-trace / fork as runtime value.
- **Xu–Kaffes (2510.05556)** — names the systems-foundations gap.
- **SWE-bench (ICLR’24)** — executable isolated evaluation pedigree.
- **Rebound→Remedy (2604.01476)** — evaluator-tampering / reward-integrity foil.

These establish:

\[
\boxed{\text{credible alternative execution}}
\]

### Payload: what those alternatives mean

The talk’s distinctive questions are:

1. What is the information value of correlated forks?
2. What must a worker return?
3. When must a reducer abstain?
4. When does reduced evidence justify action?
5. How is authoritative promotion serialized?

This is the clean contribution territory for:
- Evidence-Aware MapReduce / 2607.09689,
- the Fork/Reduce/Promote capability contract.

Do not imply invention of microVM fork itself.

---

# 18. Paper shapes this story naturally supports

1. **Evidence-Aware MapReduce for Forkable Compute: Separating Execution Fan-Out from Independent Evidence**
   - NSDI / EuroSys / ATC shape.
   - Gates: dependence → discriminate → reduce → promotion preconditions.

2. **Fork, Reduce, Promote: A Capability Contract for Cross-Domain Hill-Climb Runtimes**
   - NSDI / EuroSys; HotOS/workshop first.
   - Names runtime objects/invariants.

3. **Pricing Shared Ancestry: Correlation Floors for CoW-Sibling Ensembles**
   - NSDI / IMC / EuroSys.
   - Direct empirical follow-on to the \(\rho\) problem.

4. **Sealed Oracles for Forkable Agents: RUN!=EVAL as a Systems Invariant**
   - EuroSys / ACSAC / NDSS intersection.
   - Evaluator integrity + capability boundary.

5. **When to Fork vs When to Dream: Executable Interaction vs Learned Imagination**
   - later crossover-cost study;
   - EuroSys if systems-decision framing, NeurIPS/ICML if learning/benchmark framing.

---

# 19. The stage story: five questions, not 38 disconnected slides

## Act I — Can we run the future?

Open with:

\[
\hat P(s'|s,a)
\quad\text{vs}\quad
s'=\Phi(s,a)
\]

Question:
> When should an intelligent system predict a future, and when should it execute one?

Then establish executable applications as environments.

## Act II — Can we make the futures comparable?

Introduce:
- sufficient boundary,
- \(S_0\),
- snapshot semantics,
- fork economics,
- controlled divergence,
- external-state brokerage.

Line:
> **Fork semantics are experimental semantics: they define what “holding the past fixed” means.**

## Act III — Did N executions produce N pieces of evidence?

Mid-talk reveal:
> **Execution independence does not imply evidence independence.**

Show correlation/effective-information argument.

This is where the talk stops being “a sandbox talk.”

## Act IV — When does evidence justify a state transition?

Introduce:
- worker record,
- lineage,
- precision,
- duplicate/overlap handling,
- cold liar,
- disagreement,
- abstain,
- evidence-aware reduce.

## Act V — Who is allowed to make the future real?

Only now introduce Promote:
- frozen epoch,
- controller authority,
- Reduce != Promote,
- linearization point,
- burn/dispose speculative runners,
- accepted state becomes the next \(S_0\).

---

# 20. Proposed 34-slide core + 4 appendix

This is a candidate **full academic** structure, not yet a TeX rewrite.

## Act I — Scientific object
1. Forkable Sandboxes — title.
2. The question: predict a future or execute it?
3. Agents changed the systems problem.
4. An application is an environment.
5. Formal world: \(\mathcal W=(S,A,\Phi,O,C)\).

## Act II — Prediction vs intervention
6. Two ways to obtain the future: \(\hat P\) vs \(\Phi\).
7. Decision surface: cost / fidelity / availability / reset.
8. Hybrid: model proposes, executable world grounds.
9. Snapshot vs latent: the sufficiency question.
10. Executable counterfactuals from \(S_0\).

## Act III — Fork semantics
11. Is the captured boundary sufficient?
12. What state actually matters?
13. Where does the world boundary end?
14. Cold reconstruction vs state continuation.
15. Firecracker / DeltaBox / Crab / Shepherd: chassis.
16. Fork semantics are experimental semantics.

## Act IV — Isolation is not enough
17. Experimental subject vs authority: RUN != EVAL != PROMOTE.
18. Capability topology / sealed oracle.
19. Irreversible side effects before the gate.
20. Evidence must outlive execution.
21. Execution independence != evidence independence.
22. Shared ancestry / \(N_{\mathrm{eff}}\).

## Act V — From trajectories to evidence
23. Fork / Reduce / Promote — now reveal the abstraction.
24. Worker record schema.
25. Reduce is inference, not voting.
26. Abstention is first-class.
27. Ensemble concentration / evidence geometry.

## Act VI — From evidence to history
28. Reduce != Promote.
29. Epoch \(e=(S_e,O_e,V_e,\Pi_e)\).
30. Promotion as linearization point.
31. Driven open system — precise physics lens, no cosplay.

## Act VII — Generality + research agenda
32. Same decision tree, different worlds: code / CAD / browser / game / sim / science.
33. Open research questions.
34. Conclusion: Fork creates alternatives; Reduce makes evidence; Promote changes authoritative state.

### Appendix
35. Minimal API.
36. Correlation math / effective information.
37. Hybrid world-model + executable-fork architecture.
38. Sources + claim fences.

---

# 21. What to remove / demote from the current canonical TeX

The current full deck contains useful raw material but still reflects an earlier story.

### Cut from the main path
- “Reinforcement learning, in one slide.”
- model-free/model-based/world-model taxonomy table.
- “Coding is unusually attractive for RL.”
- coding-only framing of executable counterfactuals.
- giant motivational “cheap/plural → scarce/singular” slide early in the talk.
- “copy the machine, not the keys.”
- generic physics table “start hot / cool / T→0.”
- biology/HIL examples before the abstraction is established.
- large glossary slides unless a term is actually needed at first use.
- “benchmark not slogan” slide unless it contains concrete peer numbers/results.

### Keep, but move / sharpen
- snapshot-vs-latent sufficiency → early conceptual bridge.
- RUN != EVAL → strong central systems invariant.
- “four clones do not make four witnesses” → strengthen with dependence math.
- evidence-aware reduce + abstain → central payload.
- epochs/fencing → promotion semantics.
- Firecracker/DeltaBox/Crab/Shepherd → mechanism chassis, attributed.
- world models → short branch / appendix / Q&A unless needed for the opening question.
- physics → late lens only after ensemble semantics are defined.

---

# 22. Visual language for the rebuild

Avoid:
- giant HOT / COOL / T→0 boxes,
- four-color cartoon process strips,
- “RL 101” loops,
- slogan cards,
- simplistic “keys vs machine” metaphors,
- tables whose only job is pedagogy for basic concepts.

Prefer:
- one mathematical object per slide,
- one causal/system diagram per slide,
- decision gates,
- provenance/lineage edges,
- state boundaries,
- actual equations when they carry the argument,
- small, precise paper citations,
- sparse diagrams with semantic arrows.

The deck should look like a systems seminar / workshop paper being explained, not a product keynote.

---

# 23. One stage diagram for the whole thesis

The full private decision tree is too large for one slide.

The public compressed diagram should be:

\`\`\`text
               POSSIBLE FUTURES
                     |
                    S0
                 /   |   \
               Δ1   Δ2   ΔN
                |    |    |
               τ1   τ2   τN
                \    |    /
                 \   |   /
                  evidence
                     |
            lineage / dependence
                     |
                     v
                   REDUCE
              /       |       \
           reject   abstain   candidate
                               |
                               | current epoch?
                               | authority?
                               v
                           PROMOTE
                               |
                               v
                              S1
                               |
                             repeat
\`\`\`

Bottom line:

\[
\underbrace{\text{Fork}}_{\text{create alternatives}}
\quad
\underbrace{\text{Reduce}}_{\text{learn from alternatives}}
\quad
\underbrace{\text{Promote}}_{\text{change authoritative state}}
\]

---

# 24. The spoken story

A concise version worth preserving verbatim in notes:

> We already know how to make machines we can copy. The interesting question starts after the copy.
>
> If I fork the same state one hundred times, I can create one hundred possible futures. But I have not created one hundred independent facts.
>
> So a runtime for intelligent systems needs more than isolation. It needs semantics for how alternative executions become evidence.
>
> And evidence still is not authority. A reducer can tell us what the trajectories support; it cannot decide by itself which state becomes production, a checkpoint, a physical action, or a scientific claim.
>
> That gives us three separate operations.
>
> Fork creates alternatives.
>
> Reduce turns their outcomes into defensible evidence.
>
> Promote changes authoritative state.
>
> The research problem is to make those three operations compose without confusing parallelism with independence, measurement with truth, or confidence with permission.

That is the talk.

Everything else exists to make those claims technically unavoidable.

---

# 25. Open research questions to end on

1. **Snapshot sufficiency:** what is the minimal executable state needed for faithful continuation?
2. **Shared ancestry:** how should a system measure/model correlation among CoW siblings?
3. **Capability identity:** which credentials/capabilities may be copied, attenuated, or reminted across a fork?
4. **Evidence reduction:** how should heterogeneous structured evidence be pooled while preserving lineage and abstention?
5. **Promotion semantics:** how do we guarantee exactly-once scarce authority under racing searchers?
6. **External effects:** how do we virtualize/broker services that lie outside the snapshot boundary?
7. **Hybrid planning:** where is the empirical crossover between learned imagination and executable branching?
8. **Physical tips:** how should cheap computational epochs compose with scarce real-world oracles (robot, wet-lab, human)?
9. **Selection bias:** how does best-of-N / adaptive search alter the evidential status of the winning candidate?
10. **World diff:** what is the right merge/conflict semantics for machine state beyond files (memory, devices, network, credentials)?

---

# 26. Repo consolidation target

The final repository should eventually be understandable from a small active surface:

\`\`\`text
talk.tex
academic/
README.md
SPEAKER-NOTES.md
CLAIMS.md
Makefile
.github/workflows/
dist/forkable-sandboxes.pdf
scratch/IDEATION-FULL-STORY.md
\`\`\`

All older parallel deck descriptions / 30-minute cuts / duplicated ideation docs can be archived after the new canonical TeX lands.

For now, keep this file as the single ideation hub and retain the source research docs until the rewrite is complete.

---

# 27. Hard claim fences

Say:
- executable branching removes learned-transition error only inside the captured executable boundary;
- execution isolation != evidence independence;
- structured evidence + lineage are required for defensible reduction;
- abstention is a correct reducer outcome;
- Reduce != Promote;
- promotion is a control-plane authority transition;
- physics is a lens on ensembles/concentration/correlation, not a literal equilibrium claim.

Do not say:
- every fork is a causal counterfactual;
- snapshots capture all relevant state;
- N forks are N independent samples;
- promotion = \(T\to0\);
- the factory obeys detailed balance;
- CI literally thermalizes;
- vendor latency numbers are ours;
- this runtime already ships the full contract everywhere;
- world models are obsolete;
- code is the only useful environment.

---

# 28. Final intellectual shape

The talk should leave the room with exactly three levels:

### 1. Can I create alternatives?
**Fork** — systems / execution problem.

### 2. What did the alternatives teach me?
**Reduce** — statistics / evidence / science problem.

### 3. Which result is allowed to change the world?
**Promote** — distributed systems / security / authority problem.

The key insight is that these are **different problems**.

Fast snapshots solve only the first.

A swarm solves none of the other two automatically.

That is the research program.
