# Related work and sources

This account locates the ingredients used in the finite-depth classification result. The comparison concerns the exact circuit ensemble, input states, loss, gradient coordinates, and asymptotic regime. Bibliographic records are collected in [references.bib](references.bib); preprint versions below were checked on 18 October 2026.

The result studied here compares logical density labels with logical phase labels for a common encoded qubit and nuisance distribution. The two tasks have the same unlabeled average density operator, the same half-filled ring circuit, and the same local readout. Its central quantities are the second moments of the complete specified local-tangent gradient of the balanced classification error. The [interpretation](../science/interpretation.md) explains the probabilistic and learning scope.

## Source map

| Ingredient or comparison | Primary source and exact location | Role here |
|---|---|---|
| Haar-averaged charge transport | Khemani, Vishwanath, and Huse, Section III.1.1, Eq. (15), Appendix C; Rakovszky, Pollmann, and von Keyserlingk, Section III | Established local averaging mechanism underlying the one-body transfer matrix |
| Negative dependence under exclusion updates | Borcea, Brändén, and Liggett, Theorems 4.20 and 4.9 | External probabilistic input to the coherence upper bound |
| Dataset-dependent gradient concentration | Thanasilp et al., Section III.1, Theorem 1; Section III.2, Proposition 1 | Distinguishes prediction moments from the label-weighted population gradient |
| Stochastic propagation of gradient moments | Monbroussou et al., Lemma 1; Appendix F.1–F.3, F.8 | Closely related proof technique with a different circuit and cost |
| Measurement and readout orientation | Ait Haddou, Sections II, VII–VIII | Geometric comparison; its normalized score covariance differs from the task covariance here |
| Noise-aligned coherence | Ugail and Howard, Sections 2.1–2.3, Theorems 1–2 | Fixed-state and perturbative noise setting |
| Long-lived coherence in conserving dynamics | McCulloch, Jacoby, and Gopalakrishnan, Sections II.3, III–V; Aditya et al., Sections II–IV | Prevents identifying all coherence with a fast mode |
| Late unitary-design formation | Yada, main Theorems 1–2; Supplemental Material II.1, IV.5, VI.2 | Moment-gap context; distinct from overlap with this particular task |

## Charge diffusion and operator spreading

**Vedika Khemani, Ashvin Vishwanath, and David A. Huse**, [*Operator Spreading and the Emergence of Dissipative Hydrodynamics under Unitary Evolution with Conservation Laws*](https://arxiv.org/html/1710.09835v3), Physical Review X **8**, 031057 (2018), [DOI](https://doi.org/10.1103/PhysRevX.8.031057). Key: `KhemaniVishwanathHuse2018`.

Section III.1.1, Eq. (15), derives equalization of the two local conserved amplitudes under a Haar-averaged conserving gate. Appendix C gives the microscopic calculation. The model includes an optional local qudit; the one-body averaging rule applies also to the qubit case. Sections III.1.2–III.1.3 connect charge diffusion with ballistic operator spreading and hydrodynamic tails.

The ring transfer matrix used here is an explicit specialization of this averaging mechanism to independently selected even/odd matchings. The paper supplies physical context for slow conserved components; a lower bound on a label-dependent classifier gradient still requires the input profile, the differentiated gate, and the readout overlap to be specified.

**Tibor Rakovszky, Frank Pollmann, and C. W. von Keyserlingk**, [*Diffusive Hydrodynamics of Out-of-Time-Ordered Correlators with Charge Conservation*](https://arxiv.org/html/1710.09827v3), Physical Review X **8**, 031058 (2018), [DOI](https://doi.org/10.1103/PhysRevX.8.031058). Key: `RakovszkyPollmannVonKeyserlingk2018`.

Section III derives ensemble-averaged charge diffusion in conserving random circuits; subsequent sections address out-of-time-ordered correlators and their hydrodynamic relaxation. These results establish that charge transport and scrambling have distinct structures. They do not directly determine a supervised loss gradient or the matrix element between the complementary, macroscopically inhomogeneous branches used here.

## The negative-dependence input

**Julius Borcea, Petter Brändén, and Thomas M. Liggett**, [*Negative dependence and the geometry of polynomials*](https://arxiv.org/html/0707.2340v2), Journal of the American Mathematical Society **22**(2), 521–567 (2009), [DOI](https://doi.org/10.1090/S0894-0347-08-00618-8). Key: `BorceaBrandenLiggett2009`.

Theorem 4.20 states that mixing a measure with its image under a single transposition preserves stability of the generating polynomial. Thus a deterministic configuration remains strongly Rayleigh after a sequence of independent swap/no-swap updates. Theorem 4.9 implies negative association for strongly Rayleigh measures. These are the two external theorems used for the classical population concentration bound.

The application conditions on the complete matching schedule and on each initial nuisance string. It does **not** assume that averaging over schedules or nuisance strings preserves strong Rayleigh structure. Concentration is proved conditionally and only then averaged. The conversion from branch concentration to an off-diagonal readout second moment, followed by Haar invariance and Parseval for every native tangent, is given in the repository's [coherence proof](../science/coherence_bound.md).

## Data-dependent barren plateaus

**Supanut Thanasilp, Samson Wang, Nhat A. Nghiem, Patrick J. Coles, and M. Cerezo**, [*Subtleties in the trainability of quantum machine learning models*](https://arxiv.org/html/2110.14753v1), Quantum Machine Intelligence **5**, 21 (2023), [DOI](https://doi.org/10.1007/s42484-023-00103-6). Key: `ThanasilpEtAl2023`.

Section III.1, Theorem 1, bounds a general supervised-loss derivative variance using prediction derivatives and loss-dependent factors. Section III.2, Proposition 1, invokes an earlier local two-design calculation to relate a local prediction-gradient variance to the reduced input state's distance from the maximally mixed state. The dataset-induced plateau discussion makes clear that encoding and data properties can alter trainability.

Here the object is the derivative of the **balanced population loss**, after combining examples with their labels. Class contributions can cancel even when separate prediction derivatives are appreciable. Identical unlabeled average states therefore do not force identical gradients. The construction keeps that average fixed while rotating the encoded label axis; it does not assume that a mean state determines the full distribution of pure-state examples.

**Carlos Ortiz Marrero, Mária Kieferová, and Nathan Wiebe**, [*Entanglement-Induced Barren Plateaus*](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040316), PRX Quantum **2**, 040316 (2021), [DOI](https://doi.org/10.1103/PRXQuantum.2.040316). Key: `OrtizMarreroKieferovaWiebe2021`.

Proposition 1 and Theorem 3 of the [author manuscript](https://arxiv.org/pdf/2010.15968v2) connect visible/hidden entanglement and appropriate random-state assumptions to concentration and gradient suppression. The individual transverse examples here are complementary-string cats with one ebit across every nontrivial bipartition, so their input entanglement is not a volume-law hypothesis. Subsequent circuit evolution may generate substantial entanglement; the theorem here instead uses persistent distinguishability of the two evolving branch populations.

## Hamming-weight circuits and stochastic gradient propagation

**Léo Monbroussou, Eliott Z. Mamon, Jonas Landman, Alex B. Grilo, Romain Kukla, and Elham Kashefi**, [*Trainability and Expressivity of Hamming-Weight Preserving Quantum Circuits for Machine Learning*](https://arxiv.org/html/2309.15547v4), Quantum **9**, 1745 (2025), [DOI](https://doi.org/10.22331/q-2025-05-15-1745). Key: `MonbroussouEtAl2025`.

Lemma 1 and Appendix F.1–F.3 express gradient moments through stochastic propagation of squared amplitudes for RBS/FBS circuits and a squared Euclidean state-vector cost. Theorem 3 gives a sector-dimension formula after averaging independent input and target vectors with the stated coordinate moments. The periodic-architecture claim in Theorem 2 is formalized for fixed Hamming weight in Appendix F.8, Theorem F.4, under Conjecture F.1.

This is direct precedent for using classical transfer matrices in a trainability calculation. The present model uses general interacting two-qubit conserving Haar gates, half filling with exponentially large sector dimension, a bounded local measurement, and a label-weighted classification loss. Its transverse bound concerns actual second moments of all specified gate tangents. The stochastic population process alone would not supply that conclusion without the additional matrix-element and Haar–Parseval arguments.

## Readout orientation and noise-visible coherence

**Marwan Ait Haddou**, [*Readout Orientation Controls Measurement-Accessible Quantum Tangent Geometry*](https://arxiv.org/html/2608.17085v1), arXiv:2608.17085v1 (2026), [DOI](https://doi.org/10.48550/arXiv.2608.17085). Key: `AitHaddou2026`.

Section II defines normalized tangent-score covariance after a fixed measurement and the tangent mass retained by a readout subspace. Section III separates rank, covariance spectrum, and subspace orientation. Sections VII–VIII compare fixed-rank readouts numerically, including a half-filled RZ–XY circuit with strong low-weight alignment. The paper explicitly distinguishes these diagnostics from supervised-loss gradient variances and its finite-size case study from an asymptotic hydrodynamic theorem.

Here the readout stays fixed while the label axis varies. The covariance is over derivatives of operational task losses in a specified gate metric; it is not the normalized measurement-score covariance of that work. The controlled comparison is the separation of longitudinal and transverse label response at diffusive circuit depths.

**Hassan Ugail and Newton Howard**, [*A Coherence Law for Trainability in Noisy Equivariant Quantum Neural Networks*](https://arxiv.org/html/2606.30688v1), arXiv:2606.30688v1 (2026), [DOI](https://doi.org/10.48550/arXiv.2606.30688). Key: `UgailHoward2026`.

Section 2.1 uses one localized fixed-charge input, fixed XY hopping gates, trainable on-site phase angles, and a small-box initialization prior. Theorem 1 states a positive gradient-moment lower bound at **fixed depth and charge**, subject to light-cone non-degeneracy and nonvanishing sector weight. Theorem 2 treats perturbative Markovian noise under a first-order alignment condition; the simplest scalar law additionally uses restricted isotropy.

This identifies readout-visible coherence as a relevant noise-dependent quantity. The light-cone lower-bound statement is not an ingredient of the present proof: a nonzero sector commutator alone need not produce a nonzero expectation on a chosen input. The present task comparison is noiseless, has charge proportional to system size and depth proportional to its square, and changes the encoded information being classified. Its full-tangent upper bound is not a consequence of the fixed-state light-cone or perturbative noise statements.

## Hydrodynamic coherence requires an operator-specific statement

**Ewan McCulloch, J. Alexander Jacoby, and Sarang Gopalakrishnan**, [*Long-lived local quantum coherences from hydrodynamic large deviations*](https://arxiv.org/html/2604.27074v2), arXiv:2604.27074v2 (2026), [DOI](https://doi.org/10.48550/arXiv.2604.27074). Key: `McCullochJacobyGopalakrishnan2026`.

Sections II.3 and III–IV develop the coupling of local coherence to rare hydrodynamic fluctuations; Section V gives a conserving-circuit replica construction. The local charge-changing Green's functions can exhibit long-lived behavior even without overlap with an ordinary conserved-density mode. Appendix G also discusses neutral operators and hydrodynamic cascades.

Consequently, vanishing first-moment overlap with density does not justify an exponential coherence bound. The operator here is a coherence between complementary extensive profiles **within the same total-charge sector**. Its upper bound follows from branch distinguishability and concentration, not from assigning all off-diagonal operators a common decay rate. The full unitary evolution preserves the encoded information; the statement concerns access through the chosen local readout and its local derivatives.

**Sreemayee Aditya, Emanuele Tirrito, Piotr Sierant, and Xhek Turkeshi**, [*Coherence dynamics in quantum many-body systems with conservation laws*](https://arxiv.org/html/2604.23192v1), arXiv:2604.23192v1 (2026), [DOI](https://doi.org/10.48550/arXiv.2604.23192). Key: `AdityaEtAl2026`.

Section II defines participation entropy and relative entropy of coherence. Sections III.1 and IV study global and local coherence in conserving circuits from alternating product inputs, with replica and numerical methods. Section III.1 explicitly distinguishes those inputs from atypical domain-wall configurations. Local coherence and total coherence need not relax in the same way.

These quantities differ from a selected class-difference matrix element and its parameter derivatives. The present profile family retains a prescribed macroscopic harmonic component; adding exponentially many nuisance values broadens the dataset while preserving that structural condition. It is not a statement about equilibrium-typical inputs or about every measure of coherence.

## Initialization diagnostics and late design formation

**Ankit Kulshrestha, Ricard Puig, Diego García-Martín, Lukasz Cincio, Ilya Safro, Zoë Holmes, and M. Cerezo**, [*Exponentially many initializations to avoid barren plateaus*](https://arxiv.org/html/2606.18515v1), arXiv:2606.18515v1 (2026), [DOI](https://doi.org/10.48550/arXiv.2606.18515). Key: `KulshresthaEtAl2026`.

Sections II.4 and III.1 develop an operator-level first-moment witness and its contraction/rotation description. The discussion following Theorem 2 distinguishes this witness from a guarantee for a fixed input overlap or successful training. This is relevant to interpreting a transported density component: an ensemble witness alone does not establish a typical useful gradient. Here the density lower bound is a separately derived second-moment statement, and the transverse conclusion requires an upper bound on actual second moments.

**Toshihiro Yada**, [*Optimal Scaling of Unitary Design Formation in U(1)-Symmetric Random Circuits: A Bottleneck Slower than Charge Transport*](https://arxiv.org/html/2609.39458v1), arXiv:2609.39458v1 (2026). Key: `Yada2026`.

Main Theorems 1–2 and Table 1 give moment-gap bounds controlled by a two-particle encounter rate. The random matching definition is in Section II.3; periodic lattices are covered in Supplemental Material II.1. Architecture comparison and the lower bound appear in Supplemental Material IV.5 and VI.2, respectively. In the one-dimensional parallel normalization relevant here, the fixed-order gap scales as the inverse square of system size. In other geometries it can be parametrically slower than charge transport.

A gap constrains convergence of the whole moment operator. Obtaining a particular loss-gradient bound still requires the task overlap and the norm-conversion factors. The finite-depth density/coherence separation is proved directly, without replacing those overlaps by a worst-case gap. This source supplies late-design context, not an independently derived all-coordinate late-depth theorem for this classifier.

## Literature boundary

The comparison above is limited to the specified public versions and their stated assumptions. Yada's reference list announces *Fast chaos and emergent classicality in charge-conserving random circuits* as forthcoming. No publicly accessible manuscript for that title was located in the source check, so no results are attributed to it and no speculative bibliographic record is included.
