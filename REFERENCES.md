# References and source record

The canonical seminar has **54 main frames in six acts, no appendix or overlays**. This bibliography is a repository reference, not additional deck pages. Earlier end-matter files remain in the tree as historical sources and are not part of the canonical build.

## Current primary sources

- Yossi Eliaz. **Evidence-Aware Reduction for Forkable Compute**, arXiv:2607.09689v4 (2026). [Paper](https://arxiv.org/abs/2607.09689). Earlier metadata and source files used *Evidence-Aware MapReduce for Forkable Compute*. The current v4 title governs this deck.
- [SELFHOST-2 public run records](https://github.com/zozo123/ariflow-swfactory/tree/main/docs/factory/SELFHOST-2): intent, plan, metrics, work graph, repair and review outputs. SELFHOST-3 raw records are unpublished.
- [Experiment protocol](PREREGISTRATION.md), preserved unchanged. Inference changes discussed in [CLAIM-FENCE.md](CLAIM-FENCE.md) and [QA.md](QA.md) are **proposed amendments before collection**, not changes already made to that protocol.
- Ori Chamo and Yossi Eliaz. [Continuation Geometry Resolves Apparent Branch Splitting in Unequal-Mass Three-Body Orbits](https://ai.vixra.org/pdf/2608.0069v1.pdf), ai.viXra:2608.0069 (2026), preliminary and not peer reviewed. [Three-Body Atlas code and records](https://github.com/zozo123/threebody-closing-the-open).

## Primary sources for the motivation and examples

- Eliaz, Nedelec, Morrison, Levine and Cheung. [Insights from graph theory on the morphologies of actomyosin networks with multilinkers](https://doi.org/10.1103/PhysRevE.102.062420). Physical Review E 102:062420 (2020). [Author preprint](https://arxiv.org/abs/2006.06503). Linker valencies 2–7; 600 seconds of simulated physical time and 30 random starts in the reported motor-content comparisons.
- Harris, Gu, Olshansky, Wang, Kaur, Eliaz et al. [Chromatin alternates between A and B compartments at kilobase scale for subgenic organization](https://www.nature.com/articles/s41467-023-38429-1). Nature Communications 14:3303 (2023). POSSUMM chromosome-1 endpoint: 500-bp resolution, 2.5 min, 23 GB; greater-than-4.6-TB dense memory projection.
- Hitz et al., including Eliaz. [The ENCODE uniform analysis pipelines](https://pmc.ncbi.nlm.nih.gov/articles/PMC10371165/), DOI 10.1101/2023.04.04.535623 (2023). WDL, Cromwell, Docker, CAPER, CROO, and Portal provenance.
- Noam Barkai and Yossi Eliaz. [A gene-editing prediction engine with iterative learning cycles built on AWS](https://aws.amazon.com/blogs/storage/a-gene-editing-prediction-engine-with-iterative-learning-cycles-built-on-aws/). AWS Storage Blog, 15 February 2022. NRGene CRISPR-IL / GoGenome architecture account.
- Gil Ad Barkai, Malul, Eliaz, Eyal and Veksler-Lublinsky. [OffRisk: a docker image for annotating CRISPR off-target sites in the human genome](https://pmc.ncbi.nlm.nih.gov/articles/PMC10568243/). Bioinformatics Advances 3:vbad138 (2023). [Official code](https://github.com/IsanaVekslerLublinsky/OffRisk).
- [BMR synthetic mean demo](https://github.com/zozo123/boltzmann-mapreduce/blob/main/demo.py#L90-L93) sets the true target to μ = 5.0. The [forged-precision block](https://github.com/zozo123/boltzmann-mapreduce/blob/main/demo.py#L151-L165) injects an estimate around 17.0 from 2,000 points at SD 0.02 and inflates per-observation information 50×. This is the stress-chart reference; full-sample 4.9450 belongs to a separate snapshot integration trace.

- Gilad, Eliaz et al. [A genome-scale CRISPR Cas9 dropout screen identifies synthetically lethal targets in SRC-3 inhibited cancer cells](https://doi.org/10.1038/s42003-021-01929-1). Communications Biology 4:399 (2021), Figs. 2–4 and Methods. [Full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7994904/).
- Schultz and Coelingh Bennink. [Target expression is a relevant factor in synthetic lethal screens](https://doi.org/10.1038/s42003-022-03746-6). Communications Biology 5:835 (2022), Matters Arising on the screen above.
- Karpathy. [autoresearch](https://github.com/karpathy/autoresearch), `README.md` and `program.md` (2026). [Session report, discussion #43](https://github.com/karpathy/autoresearch/discussions/43), 8 March 2026; an automated report on Karpathy's behalf, not an independently replicated study.
- Novikov et al. [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) (2025), technical report; [original report PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf).
- AFL++ project. [LLVM persistent-mode documentation](https://github.com/AFLplusplus/AFLplusplus/blob/stable/instrumentation/README.persistent_mode.md), §§1, 3–4, supplies current state-reset conditions, typical throughput gains and loop-count guidance. [Technical testing-loop documentation](https://aflplus.plus/docs/technical_details/) explains mutation, coverage feedback and input retention; its foundational AFL whitepaper is marked outdated.
- [CyberGym: Evaluating AI Agents' Cybersecurity Capabilities with Real-World Vulnerabilities at Scale](https://arxiv.org/abs/2506.02548). [ICLR 2026 conference paper](https://openreview.net/pdf/eea34d6015b8e77e38bafe756ab3d4924402b055.pdf), [Berkeley RDI campaign report](https://rdi.berkeley.edu/blog/cybergym/) and [project report](https://www.cybergym.io/cybergym/). Historical benchmark and latest-code vulnerability-discovery campaign have distinct populations.

- Eliaz. [Tokio issue #8200: external Incredibuild artifact-cache demonstration](https://github.com/tokio-rs/tokio/issues/8200), 8 June 2026. Approximate compile timings 46 s fresh, 13 s restored, and 3 s hot; an author-reported demonstration rather than a controlled benchmark or maintainer adoption.

## Systems

- Fork, snapshot, isolation
- Barham et al. Xen and the art of virtualization. SOSP 2003.
- Vrable et al. Scalability, fidelity, and containment in the Potemkin virtual honeyfarm. SOSP 2005.
- Lagar-Cavilla et al. SnowFlock. EuroSys 2009.
- Madhavapeddy et al. Jitsu. NSDI 2015.
- Manco et al. My VM is lighter (and safer) than your container. SOSP 2017.
- Baumann et al. A fork() in the road. HotOS 2019.
- Agache et al. Firecracker. NSDI 2020.
- Du et al. Catalyzer. ASPLOS 2020.
- Brooker et al. Restoring uniqueness in microVM snapshots. arXiv:2102.12892, 2021.
- Ustiugov et al. Benchmarking, analysis, and optimization of serverless function snapshots (REAP). ASPLOS 2021.
- Lupu et al. Nephele: cloning unikernel-based VMs. EuroSys 2023.
- Clark et al. Live migration of virtual machines. NSDI 2005.
- Leases and fencing
- Gray & Cheriton. Leases. SOSP 1989.
- Burrows. The Chubby lock service. OSDI 2006.
- Kleppmann. How to do distributed locking. 2016.
- Agent sandboxes, 2026
- Dong et al. DeltaBox. arXiv:2605.22781. Yu et al. Shepherd. arXiv:2605.10913. Wu et al. Crab. arXiv:2604.28138.
- Guo et al. Planarian: managing agent state with statepoints. arXiv:2609.35366. Zheng et al. arXiv:2608.22928.
- Kimi Team (Moonshot AI). Kimi K3: Open Frontier Intelligence. Tech. report, 2026, §4.1.2, §4.2.4, §4.2.6, §5.3.2. DeepSeek-AI. DeepSeek-V4 (DSec). arXiv:2606.19348.
- Wei et al. No provisioned concurrency: fast RDMA-codesigned remote fork (MITOSIS). OSDI 2023. Ao et al. FaaSnap. EuroSys 2022.
- Effects, authority, provenance
- Nightingale, Chen & Flinn. Speculative execution in a distributed file system. SOSP 2005.
- Nightingale et al. Rethink the sync. OSDI 2006.
- Cully et al. Remus. NSDI 2008.
- Watson et al. Capsicum. USENIX Security 2010.
- Watson et al. CHERI. IEEE S&P 2015.
- Birgisson et al. Macaroons. NDSS 2014.
- Muniswamy-Reddy et al. Provenance-aware storage systems. USENIX ATC 2006.
- Pasquier et al. Practical whole-system provenance capture. SoCC 2017.
- Torres-Arias et al. in-toto. USENIX Security 2019.
- O'Callahan et al. Engineering record and replay for deployability. USENIX ATC 2017.

## Evidence and evaluation

- Dependent evidence
- Dorfman. The detection of defective members of large populations. Ann. Math. Stat. 14(4):436-440, 1943.
- Cochran. The combination of estimates from different experiments. Biometrics 1954.
- Kish. Survey Sampling. Wiley, 1965.
- Amdahl. Validity of the single processor approach to achieving large scale computing capabilities. AFIPS SJCC 1967.
- Liang & Zeger. Longitudinal data analysis using generalized linear models. Biometrika 1986.
- Hedges, Tipton & Johnson. Robust variance estimation in meta-regression with dependent effect size estimates. Research Synthesis Methods 2010.
- Green, Karvounarakis & Tannen. Provenance semirings. PODS 2007.
- Cameron, Gelbach & Miller. Bootstrap-based improvements for inference with clustered errors. REStat 2008.
- Cameron, Gelbach & Miller. Robust inference with multiway clustering. JBES 2011.
- Glasserman & Yao. Some guidelines and guarantees for common random numbers. Management Science 1992.
- Stockmayer. Theory of molecular size distribution and gel formation in branched-chain polymers. J. Chem. Phys. 11:45, 1943.
- Shared errors across models
- Kim, Garg, Peng & Garg. Correlated errors in large language models. ICML 2025, PMLR 267. arXiv:2506.07962.
- Goel et al. Great models think alike and this undermines AI oversight. ICML 2025. arXiv:2502.04313.
- Evaluation under search
- Dean & Barroso. The tail at scale. CACM 2013 (hedged requests; also fan-out, good enough, canary requests, mutations).
- Dean. Designs, lessons and advice from building large distributed systems (“Numbers everyone should know”). LADIS keynote, 2009.
- Brown et al. Large Language Monkeys: scaling inference compute with repeated sampling. arXiv:2407.21787, 2024.
- Von Arx, Chan & Barnes (METR). Recent frontier models are reward hacking. 5 June 2025.
- Zhong, Raghunathan & Carlini. ImpossibleBench. arXiv:2510.20270, 2025.
- Dwork et al. The reusable holdout. Science 2015.
- Stroebl, Kapoor & Narayanan. The limits of inference scaling through resampling (v1: Inference scaling fLaws). arXiv:2411.17501, 2024.
- Russo & Zou. Controlling bias in adaptive data analysis using information theory. AISTATS 2016.
- Shared errors across models: 2026 preprints
- Jo, Garg & Raghavan. The subjectivity of monoculture. arXiv:2602.24086, preprint.
- Kohli. Nine judges, two effective votes: correlated errors undermine LLM evaluation panels. arXiv:2605.29800, preprint.
- Chen. When does combining language models help? A co-failure ceiling on routing, voting, and mixture-of-agents across 67 frontier models. arXiv:2606.27288, preprint.
- Bone, Stephany & del Rio-Chanona. Monocultural biases: correlated biases in large language models lead to unequal systemic exclusion rates in hiring. arXiv:2609.22169, preprint.

## Own work and documentation

- Speaker and co-authors
- Y. Eliaz. Evidence-Aware Reduction for Forkable Compute. arXiv:2607.09689, 2026.
- github.com/zozo123/ariflow-swfactory, runs SELFHOST-2/3, 27 Sep 2026.
- Blackburn, Huber, Eliaz et al. Cooperation among an anonymous group protected Bitcoin during failures of decentralization. arXiv:2206.02871, 2022.
- Saurty-Seerunghen, El-Habr, Eliaz et al. A unique malignant cell type per patient tumor encoded in each cancer cell transcriptome. iScience 29:115139, 2026.
- Hitz, ..., Eliaz, ..., Cherry. The ENCODE uniform analysis pipelines. bioRxiv 2023, doi:10.1101/2023.04.04.535623.
- Gilad, Eliaz et al. A genome-scale CRISPR Cas9 dropout screen identifies synthetically lethal targets in SRC-3 inhibited cancer cells. Commun. Biol. 4:399, 2021.
- Barkai, ..., Eliaz, .... OffRisk. Bioinformatics Advances 3:vbad138, 2023.
- Eliaz, Danovich & Gasic. Poolkeh. medRxiv 2020.
- Speaker's physics work
- Eliaz et al. PRE 102:062420, 2020; Liman et al. PNAS 117:10825, 2020; Li et al. JPCB 125:11591, 2021.
- Documentation
- OBuilder (github.com/ocurrent/obuilder); day10 (tunbury.org, 16 Feb 2026); Docker Sandboxes security; Firecracker snapshotting, snapshot-support and prod-host-setup docs; CRIU TCP_REPAIR; gVisor checkpoint/restore.
- RL and exploration
- Ecoffet et al. Go-Explore. Nature 2021.

## Biophysics research record

- PhD, University of Houston, with the Rice Center for Theoretical Biological Physics
- Eliaz, Nedelec, Morrison, Levine & Cheung. Insights from graph theory on the morphologies of actomyosin networks with multilinkers. Phys. Rev. E 102:062420 (2020). First author.
- Liman, ..., Eliaz, ..., Cheung. The role of the Arp2/3 complex in shaping the dynamics and structures of branched actomyosin networks. PNAS 117:10825 (2020).
- Li, Liman, Eliaz & Cheung. Forecasting avalanches in branched actomyosin networks with network science and machine learning. J. Phys. Chem. B 125:11591 (2021).
- Zegarra, ..., Eliaz, .... Impact of hydrodynamic interactions on protein folding rates depends on temperature. Phys. Rev. E 97:032402 (2018).
- Zhang, Nde, Eliaz, Jennings, Cieplak & Cheung. CaXML: Chemistry-informed machine learning explains mutual changes between protein conformations and calcium ions in calcium-binding proteins using structural and topological features. Protein Science 34:e70023 (2025).
- Thesis
- Eliaz. Physics of self-assembly in complex matter. PhD thesis, University of Houston (2020); self-published in book form as Physics of Complex (Biological) Matter (2023).

## Genomics research record

- Genome architecture and bioinformatics
- Harris, ..., Eliaz, ..., Lieberman Aiden, Rowley. Chromatin alternates between A and B compartments at kilobase scale for subgenic organization. Nat. Commun. 14:3303 (2023).
- Kaushal, ..., Eliaz, .... CTCF loss has limited effects on global genome architecture in Drosophila despite critical regulatory functions. Nat. Commun. 12:1011 (2021).
- Barkai, ..., Eliaz, .... OffRisk: a docker image for annotating CRISPR off-target sites in the human genome. Bioinformatics Advances 3:vbad138 (2023).
- Cancer genomics
- Saurty-Seerunghen, El-Habr, Eliaz, ..., Junier. A unique malignant cell type per patient tumor encoded in each cancer cell transcriptome. iScience 29:115139 (2026).
- Gilad, Eliaz, .... A genome-scale CRISPR Cas9 dropout screen identifies synthetically lethal targets in SRC-3 inhibited cancer cells. Commun. Biol. 4:399 (2021).
- Gilad, Eliaz, .... Reply to: Target expression is a relevant factor in synthetic lethal screens. Commun. Biol. 5:836 (2022).
- Gilad, Eliaz, .... Drug-induced PD-L1 expression and cell stress response in breast cancer cells can be balanced by drug combination. Sci. Rep. 9:15099 (2019).

## Preprints, systems and talks

- Preprints
- Eliaz. Evidence-Aware Reduction for Forkable Compute. arXiv:2607.09689 (2026). Sole author; code github.com/zozo123/boltzmann-mapreduce.
- Blackburn, Huber, Eliaz, ..., Lieberman Aiden. Cooperation among an anonymous group protected Bitcoin during failures of decentralization. arXiv:2206.02871 (2022).
- Eliaz, Danovich & Gasic. Poolkeh finds the optimal pooling strategy for a population-wide COVID-19 testing. medRxiv (2020). First author.
- Hitz, ..., Eliaz, ..., Cherry. The ENCODE uniform analysis pipelines. bioRxiv (2023).
- The ENCODE Project Consortium (member). The Encyclopedia of DNA Elements. bioRxiv (2026).
- Chamo & Eliaz. Continuation geometry resolves apparent branch splitting in unequal-mass three-body orbits. ai.viXra:2608.0069 (2026); not peer reviewed.
- Systems and open source
- Airflow Factory, an open-source Apache Airflow software factory: github.com/zozo123/ariflow-swfactory.
- This talk's slides and notes: github.com/zozo123/cam-talk-london-26.
- apache/airflow: sandbox toolset with Docker sbx and OpenSandbox backends (merged, 2026); two more backends (open).
- openclaw/crabbox, nushell, and sandbox PRs to Spark, Kafka Connect and mecatl (2026).
- The Sandbox Shift: a field manual for running untrusted code (2026).
- Talks, October 2026
- Cambridge SRG (this talk), 15 Oct.
- RustChinaConf, Shenzhen: Disposable Runners, Warm Cargo Factory, 17 Oct.
- Zenity AI Agent Security Summit, New York: Your Agent Escaped Without Escaping the Sandbox, 21 Oct.

## Primary documentation links

- [OBuilder](https://github.com/ocurrent/obuilder).
- [Docker Sandboxes documentation](https://docs.docker.com/ai/sandboxes/).
- [Firecracker snapshot support](https://github.com/firecracker-microvm/firecracker/blob/main/docs/snapshotting/snapshot-support.md) and [production host setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md).
- [CRIU TCP connection checkpointing](https://criu.org/TCP_connection).
- [gVisor checkpoint and restore](https://gvisor.dev/docs/user_guide/checkpoint_restore/).
- [METR: Recent frontier models are reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/).

## Legacy mentions not used as current evidence

The former Q&A also named Rebound, SandboxEscapeBench / EscapeBench, an unspecified NCSC minimum, and CoPilot-style gates without a complete verified citation. These mentions are retained here to preserve the historical source inventory; **they do not support claims in the current deck or Q&A**. No identifiers, numbers, or blanket isolation recommendations are inferred from them.

## Interpretation boundaries

Cross-model error studies are not agent-fork experiments. Conditional wrong-answer agreement is not rho. A panel effective sample size is not a fork correctness rate. Reported runtime timings measure different operations and endpoints. The speaker’s biology, physics, genomics and Bitcoin work provides concrete methodological examples, not empirical evidence about sandbox forks.

## Motivation attribution

The dated overview connects systems/security, biological and genomic work, a published cancer result, NRGene gene-editing prediction, Mobileye perception and current compute. Dates follow the career website below; overlapping work periods and publication events remain distinct. The 2022 CRISPR-IL article's Noam Barkai and the 2023 OffRisk paper's Gil Ad Barkai are different coauthors. Existing cancer papers and SI-12 assays do not document an autonomous immunotherapy system or clinical controller, and the factory records do not establish Docker security improvement. Mobileye perception is the speaker's account; publication dates do not establish a specific contribution or employment transition. Adaptive execution is software-workflow framing on conventional hardware. The second act is EXAMPLES; published findings retain their authors and workloads.

## Sources added to the final motivation and terminology

- [Twistlock 1.7 technical newsletter, January 2017](https://cdn.twistlock.com/docs/TechNews/Twistlock_Jan17_1_7.pdf), runtime defense model learning/enforcement, pp. 2–3. Vendor operational account.
- Gilad, Eliaz, Yu, Han, O'Malley and Lonard. [Drug-induced PD-L1 expression and cell stress response in breast cancer cells can be balanced by drug combination](https://doi.org/10.1038/s41598-019-51537-7). Scientific Reports 9:15099 (2019). [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6805932/); [2020 label correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC7056712/).
- [Docker Sandboxes architecture](https://docs.docker.com/ai/sandboxes/architecture/): sbx, microVM, private Docker daemon and host policy boundary.
- [Firecracker project](https://firecracker-microvm.github.io/): guest virtualization with a minimal device model.
- [Linux cgroup v2 documentation](https://docs.kernel.org/admin-guide/cgroup-v2.html): resource accounting/control, distinct from the sandbox access policy.

## Career chronology and driving photograph

- [Yossi Eliaz’s career website](https://yossieliaz.netlify.app/), retrieved 4 October 2026. Early systems roles 2010–2016; research 2016–2021; NRGene August 2020–November 2021; Mobileye December 2021–March 2024; Incredibuild December 2025–present. The cancer-combination marker is the 2019 paper already cited above.
- [Mobileye Now Testing AVs in New York City](https://www.mobileye.com/press-kit/press-kit-mobileye-new-york-city/), official press kit, 20 July 2021. Manhattan photograph taken June 2021; image credit Mobileye / Intel. Asset attribution is retained in assets/SOURCES.md.


## Current startup benchmark and aggregation explanation

- [ComputeSDK Burst TTI leaderboard](https://www.computesdk.com/benchmarks/sandboxes/burst-tti), latest dated run used here: 2 October 2026; retrieved 4 October 2026. [Immutable raw JSON](https://github.com/computesdk/benchmarks/blob/24922f27408279200074cbc8773cbda9a4aa4785/results/burst_tti/2026-10-02.json) is copied to [evidence/computesdk-burst-tti-2026-10-02.json](evidence/computesdk-burst-tti-2026-10-02.json). Isorun median 72.77 ms / p95 78.29 ms, Miosa 163.35 / 187.8 ms, Archil 237.77 / 250.34 ms; 100/100 success each, concurrency 100. Client create-to-first-successful-command endpoint. [Methodology](https://github.com/computesdk/benchmarks/blob/24922f27408279200074cbc8773cbda9a4aa4785/METHODOLOGY.md).
- Polyanskiy and Wu, [MIT 6.441 Information Theory lecture notes](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/), Chapter 2: mutual information, entropy identity and information chain rules.
- Valassi and Chierici, [Information and treatment of unknown correlations in the combination of measurements using the BLUE method](https://arxiv.org/abs/1307.4003), European Physical Journal C 74:2717 (2014), [DOI](https://doi.org/10.1140/epjc/s10052-014-2717-6). Correlation-aware best linear unbiased estimate; externally justified error model required.
- Chamo and Eliaz, [Three-Body Orbit Atlas source](https://github.com/zozo123/threebody-closing-the-open/tree/23640cd869720ce62bc7a5fee4d7269d860e7321), including paper/short/main_short.pdf: 135,445 catalogued orbits; selected checks 5 macroscopic MST cuts, 20 chart jumps and one distant pair; 26 bidirectional connections. This supports the numbered workflow, not a global completeness claim.

## Mobileye Roadbook aggregation update

- [Mobileye Stellantis announcement](https://ir.mobileye.com/news-releases/news-release-details/mobileye-supply-cloud-enhanced-adas-select-future-stellantis), 21 July 2026: >8 million REM contributing vehicles; 34 billion miles in 2025. The separate EyeQ installed-base figure is >230 million vehicles through 2025. Retrieved 4 October 2026.
- [Mobileye REM technology](https://www.mobileye.com/technology/rem/): tagged observations, alignment/aggregation along the same road, semantic map generation and distribution to vehicles. The slide uses the sourced HD Roadbook description.
- The displayed rate is an annual-average calculation: 34,000,000,000 / 31,536,000 = 1,078.1 road-miles of observations per second, rounded to 1,080. It is not a signals/second or instantaneous upload-rate measurement.
