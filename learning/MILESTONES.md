# Quantum Learning Anisotropy: 30 understanding milestones

This map follows the project's scientific argument from local quantum operations to a controlled separation between density-label and phase-label gradients. It records common understanding targets, their dependencies, and their authoritative sources. Detailed constructions and proofs remain in `science/`.

The single educational anchor is **Larocca et al., _Barren Plateaus in Variational Quantum Computing_, [arXiv:2405.00781v2][larocca]**. All review section numbers below refer to that version. The [Larocca bridge](LAROCCA_BRIDGE.md) relates its notation and assumptions to this project. Review pointers supply context; the conserving-circuit diffusion identities, conditional concentration argument, native encoder, and exact task-gradient bounds are supplied by the linked project sources. The probability results imported by those proofs retain their primary-source attribution there.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background joins states, measured losses, local derivatives, conservation, randomness, and operator alignment into one model contract. The longer narrative is needed because the contribution connects an explicit data construction to two different mechanisms: a signed density response and a concentration bound on phase-sensitive interference. It then joins those mechanisms through the complete gradient geometry, depth dependence, and resource account.

| Phase | Milestones | Local-to-global progression |
|---|---|---|
| Background/preliminaries | [M01](#m01-quantum-states-and-a-local-readout)–[M04](#m04-charge-conservation-and-an-extensive-quantum-sector) | Local states, measured loss, gate derivatives, and charge |
| Background/preliminaries | [M05](#m05-matching-layers-locality-and-physical-circuit-resources)–[M08](#m08-concentration-full-gradient-scope-and-probability-strength) | Spatial circuits, operator evolution, and probability |
| Background/preliminaries | [M09](#m09-expressivity-haar-randomness-and-design-assumptions)–[M12](#m12-synthesis-of-the-model-contract) | Expressivity, label alignment, diffusion, and the complete model |
| Narrative/innovation | [M13](#m13-a-native-conserving-encoder)–[M16](#m16-an-exact-decoder-inside-the-same-architecture) | Common source, uniform contrast, and exact decoding |
| Narrative/innovation | [M17](#m17-conditional-classical-populations-from-quantum-gates)–[M20](#m20-branch-distinguishability-bounds-squared-quantum-interference) | Conditional populations, concentration, and quantum interference |
| Narrative/innovation | [M21](#m21-from-interference-to-a-derivative-at-the-actual-haar-gate)–[M24](#m24-fourier-filtering-and-the-polynomial-density-floor) | Full phase-gradient upper and signed density lower |
| Narrative/innovation | [M25](#m25-exact-logical-axis-covariance)–[M27](#m27-finite-constants-and-the-meaning-of-verification) | Axis geometry, depth windows, and quantitative evidence |
| Narrative/innovation | [M28](#m28-loss-choice-and-label-independent-gradients)–[M30](#m30-synthesis-of-hydrodynamic-label-axis-selection) | Loss, resources, and synthesis of the scientific statement |

## Phase I: Background/preliminaries

### M01: Quantum states and a local readout

**Phase:** Background/preliminaries.

**Central question:** What information does one physical measurement of a quantum state produce?

**Understanding target:** Distinguish a pure state, a statistical mixture, an observable, its expectation, and one sampled outcome. Relate the two outcomes of physical $`Z_0`$ to their probabilities, and distinguish a relative phase from a change in computational-basis populations.

**Dependencies and story role:** Entry point. These local objects supply the meaning of every later input, class state, interference amplitude, and measured prediction.

**Conceptual connection:** The project compares information accessible through a specified observable, so global state differences and locally visible prediction differences must be kept distinct from the outset.

**Source pointers:** Anchor context: [§II.2][larocca]. Project: [physical prediction and error](../science/loss_and_geometry.md#1-expected-error-of-the-physical-prediction), [effective logical observable](../science/loss_and_geometry.md#2-effective-logical-observable).

### M02: From a measured prediction to a supervised population loss

**Phase:** Background/preliminaries.

**Central question:** Which mathematical quantity represents classification error for this experiment?

**Understanding target:** Connect the binary error $`(1-yr)/2`$ to the expected population loss. Identify the balanced class difference as the label-bearing input operator, and explain why an unlabeled average state does not determine that difference. Distinguish averaging over nuisance examples from averaging over measurement shots.

**Dependencies and story role:** Depends on M01. It specifies the object whose gradient matters before introducing circuit optimization or concentration.

**Conceptual connection:** Linearity in the labeled margin permits the high-rank class mixtures to enter the proof exactly and makes signed population averaging essential.

**Source pointers:** Anchor context: [§§II.1–II.2][larocca]. Project: [operational loss](../science/model.md#3-operational-loss), [expected error](../science/loss_and_geometry.md#1-expected-error-of-the-physical-prediction).

### M03: Local gate variations and a specified gradient metric

**Phase:** Background/preliminaries.

**Central question:** What does changing one trainable gate mean, and how is the size of that change normalized?

**Understanding target:** Interpret the curve $`e^{-i\theta H}G`$ as a left variation of an actual gate. Distinguish one coordinate derivative from the complete gradient energy, and distinguish operator-norm-one generators from Hilbert–Schmidt-normalized generators. Recognize why a size-dependent rescaling can alter a gradient claim.

**Dependencies and story role:** Depends on M01–M02. It fixes the local differential objects later summed over the entire initialized circuit.

**Conceptual connection:** A comparison of task gradients is meaningful only after the available gate directions and their normalization are held fixed.

**Source pointers:** Anchor context: [§§II.2 and III.3][larocca]. Project: [fixed tangent convention](../science/model.md#fixed-local-tangent-convention), [native coordinates and normalization](../science/loss_and_geometry.md#4-native-tangent-coordinates-and-their-normalization).

### M04: Charge conservation and an extensive quantum sector

**Phase:** Background/preliminaries.

**Central question:** What does particle-number conservation restrict, and what freedom remains?

**Understanding target:** Relate the occupation operator $`N_j=(I-Z_j)/2`$ to total charge. Explain the zero-, one-, and two-excitation blocks of an allowed local gate, including its interacting phases. Distinguish the half-filled sector's exponential dimension from the much smaller number of one-body charge observables.

**Dependencies and story role:** Depends on M01 and M03. It identifies the physical restriction behind the local gate basis without assuming that symmetry makes the whole model small or classically simulable.

**Conceptual connection:** Conserved structure can protect selected responses inside an exponentially large sector; a symmetry restriction alone is not a small-dynamical-Lie-algebra conclusion.

**Source pointers:** Anchor context: [§§IV.1–IV.2 and VI.2][larocca]. Project: [circuit and conserved charge](../science/model.md#1-circuit-and-conserved-charge), [transport interpretation](../science/density_transport.md#8-interpretation-and-limitations).

### M05: Matching layers, locality, and physical circuit resources

**Phase:** Background/preliminaries.

**Central question:** How do nearest-neighbor geometry and layer count constrain a classifier?

**Understanding target:** Describe the two perfect matchings of the ring and the difference between parallel depth and total gate count. Relate a local gate's influence on a distant readout to its causal reach. Keep input preparation separate from classifier depth, while including both in the full resource account.

**Dependencies and story role:** Depends on M03–M04. It turns the local conserving gate model into a spatial circuit and identifies the depth scales used later.

**Conceptual connection:** The project's diffusive regime is much deeper than the linear-depth native decoder; its phase suppression cannot be explained solely by a permanently disconnected readout cone.

**Source pointers:** Anchor context: [§§II.2 and VI.1][larocca]. Project: [ring architecture](../science/model.md#1-circuit-and-conserved-charge), [suffix locality condition](../science/density_transport.md#4-a-suffix-fourier-bound-with-explicit-constants), [per-example resources](../science/data_encoding.md#8-per-example-resource-account).

### M06: Forward states and backward observables

**Phase:** Background/preliminaries.

**Central question:** Why can the same prediction be described by evolving either the input or the readout?

**Understanding target:** Interpret $`\mathrm{Tr}[U\rho U^\dagger O]=\mathrm{Tr}[\rho U^\dagger OU]`$ as two accounts of one experiment. Explain the roles of a prefix, a selected gate, and a suffix. Identify how forward input structure and a backward local observable can both determine a derivative.

**Dependencies and story role:** Depends on M02–M05. It introduces the operator viewpoint that links circuit locality to the conditional density-response calculation.

**Conceptual connection:** The density floor depends on two spatial differences meeting at one gate, while the coherence upper depends on an off-diagonal matrix element of the same readout.

**Source pointers:** Anchor context: [§§IV.1 and IV.3][larocca]. Project: [one-body transfer and backward readout](../science/density_transport.md#2-the-one-body-transfer-matrix), [effective logical observable](../science/loss_and_geometry.md#2-effective-logical-observable).

### M07: Initialization ensembles, conditional means, and second moments

**Phase:** Background/preliminaries.

**Central question:** Which randomness is averaged in a gradient statement?

**Understanding target:** Distinguish random initial gates, random matching choices, nuisance sampling, and quantum measurement outcomes. Explain why the initialized circuit stays fixed during repeated evaluations. Relate a conditional mean to a second-moment lower bound through Jensen, and recognize that a vanishing mean does not imply a small second moment.

**Dependencies and story role:** Depends on M02–M06. It provides the probability bookkeeping required by both proof mechanisms.

**Conceptual connection:** The density proof exploits a nonzero conditional signed response; the phase proof must control an actual squared interference amplitude. Those are different uses of averaging.

**Source pointers:** Anchor context: [§§III.1 and III.3][larocca]. Project: [what is differentiated](../science/interpretation.md#2-what-is-being-differentiated), [conditional Haar-gate response](../science/density_transport.md#3-exact-conditional-response-of-an-actual-haar-gate), [squared interference](../science/coherence_bound.md#5-a-projector-inequality-bounds-squared-interference).

### M08: Concentration, full-gradient scope, and probability strength

**Phase:** Background/preliminaries.

**Central question:** What distinguishes an exponentially small gradient moment from a useful optimization guarantee?

**Understanding target:** Distinguish one-coordinate concentration, simultaneous full-gradient suppression, and a lower bound on an ensemble moment. Explain how an upper second-moment bound gives a high-probability statement and why the corresponding density lower bound need not imply a constant fraction of useful initializations.

**Dependencies and story role:** Depends on M03 and M07. It fixes the quantifiers used to interpret the final separation.

**Conceptual connection:** The two sides of the theorem have different probability strength even though both are expressed using squared native gradient norms.

**Source pointers:** Anchor context: [§§III.1 and IX][larocca]. Project: [high-probability transverse consequence](../science/loss_and_geometry.md#6-high-probability-consequence-for-transverse-gradients), [density-moment implications](../science/loss_and_geometry.md#7-what-the-density-moment-does-and-does-not-establish).

### M09: Expressivity, Haar randomness, and design assumptions

**Phase:** Background/preliminaries.

**Central question:** How does the ability to represent a state or classifier differ from the distribution produced by random initialization?

**Understanding target:** Distinguish the allowed family of gate assignments, the initialized circuit ensemble, and agreement with a global Haar distribution through specified moments. Identify why independent local Haar gates do not immediately make the entire finite-depth circuit a sector-Haar sample or a design.

**Dependencies and story role:** Depends on M04–M08. It separates an architecture's possible solutions from claims about the statistics of a randomly chosen solution candidate.

**Conceptual connection:** The exact decoder and the phase-gradient plateau can coexist, and a whole-moment design estimate cannot replace the task-specific overlap calculation.

**Source pointers:** Anchor context: [§§III.3, IV.2, and VI.2][larocca]. Project: [expressivity and probability](../science/interpretation.md#5-what-probability-and-expressivity-add), [physical scope and design distinction](../science/interpretation.md#6-scope-of-the-physical-statement).

### M10: State, observable, and label alignment

**Phase:** Background/preliminaries.

**Central question:** Why can equal Hilbert-space size and equal average input state coexist with different supervised responses?

**Understanding target:** Relate a prediction to an operator overlap and identify the labeled contrast as an additional piece of structure. Distinguish input entropy, readout locality, and label orientation. Understand why none of those scalar descriptions alone fixes the task's complete gradient response.

**Dependencies and story role:** Depends on M02, M06, and M09. It assembles the state, circuit, observable, and task into the comparison that motivates the construction.

**Conceptual connection:** The project changes a logical label axis while holding the physical readout and unlabeled average fixed, isolating a supervised distinction that a mean-state-only description loses.

**Source pointers:** Anchor context: [§§IV.1–IV.3][larocca]. Project: [controlled comparison](../science/interpretation.md#1-the-controlled-comparison), [logical observable and margin](../science/loss_and_geometry.md#2-effective-logical-observable).

### M11: Conserved modes and diffusive time scales

**Phase:** Background/preliminaries.

**Central question:** How can local charge equalization retain a macroscopic spatial memory for a long time?

**Understanding target:** Interpret a stochastic transfer matrix, its constant mode, and its nonuniform Fourier modes. Relate the exact eigenvalues $`\lambda_k=\cos^2(\pi k/n)`$ to the $`n^2`$ relaxation scale of the longest spatial mode. Distinguish this closed averaged one-body calculation from simulation of the full interacting circuit.

**Dependencies and story role:** Depends on M04–M07. It supplies the transport language that both project proofs require.

**Conceptual connection:** Total charge by itself has no spatial derivative; the useful label response comes from a nonuniform conserved-density mode that overlaps with the input and readout.

**Source pointers:** Anchor context for local stochastic variance methods: [§III.3][larocca]. Project-specific transport: [one-body transfer matrix](../science/density_transport.md#2-the-one-body-transfer-matrix), [meaning of the conserved mode](../science/density_transport.md#8-interpretation-and-limitations).

### M12: Synthesis of the model contract

**Phase:** Background/preliminaries.

**Central question:** Which objects and conditions must be held together to state the project's comparison precisely?

**Understanding target:** Assemble the half-filled ring, interacting conserving gates, fair matching schedule, fixed native tangent metric, labeled source, single-site prediction, and population error into one model. Distinguish the randomness used in the theorem from the operations used to prepare and measure an example. State the controlled question without replacing it by a convergence or quantum-advantage claim.

**Dependencies and story role:** Integrates M01–M11. This closes the background phase by connecting its local physical and statistical objects into the complete setting for both proofs.

**Conceptual connection:** A valid anisotropy result must compare the same architecture and measurement under different labeled decompositions, with explicit depth and resource conventions.

**Source pointers:** Anchor context: [§§II.1–II.2, III.1, and IX][larocca]. Project: [model, data, and operational loss](../science/model.md#1-circuit-and-conserved-charge), [main theorem domains](../science/model.md#4-full-gradient-separation), [scope](../science/model.md#6-scope-of-the-conclusions).

## Phase II: Narrative/innovation

### M13: A native conserving encoder

**Phase:** Narrative/innovation.

**Central question:** How can a logical control qubit be spread into complementary physical branches using only allowed local gates?

**Understanding target:** Explain the dual-rail encoding, the boundary-phase implementation of logical CZ, the resulting CNOT chain, and the fixed wire permutation. Track why changing the control complements every encoded physical bit while preserving total charge. Account for linear depth, quadratic gate count, and the absence of ancillas.

**Dependencies and story role:** Depends on M03–M05 and M12. The narrative begins with a concrete local construction whose output supports both label tasks.

**Conceptual connection:** The data source is a specified physical circuit with a shared preparation cost, rather than an uncharged state-loading assumption.

**Source pointers:** Anchor context for input and ansatz design: [§II.2][larocca]. Project construction: [dual rails](../science/data_encoding.md#1-dual-rail-logical-qubits), [fixed encoder](../science/data_encoding.md#2-one-fixed-encoder), [native implementation](../science/data_encoding.md#6-native-implementation-and-preparation-resources).

### M14: Extensive nuisance variation with one common average state

**Phase:** Narrative/innovation.

**Central question:** How does the construction become one high-rank classification source rather than one specially selected branch pair?

**Understanding target:** Relate the fixed weight of the output nuisance bits to the sampled input nuisance string. Explain why the source has $`\binom{m-1}{\lfloor m/8\rfloor}`$ nuisance values yet admits polynomial classical sampling. Identify the orthogonal class supports and the common average $`E[(I/2)\otimes\tau]E^\dagger`$ for every logical axis.

**Dependencies and story role:** Depends on M02, M10, and M13. It turns the encoder into a population data distribution with extensive nuisance entropy.

**Conceptual connection:** Different labeled decompositions have the same fresh single-copy unlabeled statistics. This equality does not identify stronger access models involving repeated copies of a fixed sampled pure example.

**Source pointers:** Anchor context: [§§II.2 and IV.3][larocca]. Project: [nuisance sampler](../science/data_encoding.md#3-fixed-weight-nuisance-source), [class states and common average](../science/data_encoding.md#4-label-conditioned-states-and-the-common-average), [access distinction](../science/interpretation.md#1-the-controlled-comparison).

### M15: Macroscopic harmonic contrast survives nuisance averaging

**Phase:** Narrative/innovation.

**Central question:** Which feature of all those nuisance examples supplies a uniform transport signal?

**Understanding target:** Identify the aligned sine profile and explain why each flipped logical output bit can reduce its overlap by at most four. Relate the fixed-weight restriction to a positive overlap proportional to $`n`$. Separately identify the signed mean population profile and its nonzero wall contrast.

**Dependencies and story role:** Depends on M11 and M13–M14. It supplies the common input structure needed by the concentration upper bound and the density lower bound.

**Conceptual connection:** A per-branch macroscopic overlap controls phase observability, while a signed population contrast prevents cancellation of the density response. The two hypotheses play different roles.

**Source pointers:** Anchor context for input/readout structure: [§IV.3][larocca]. Project: [surviving profile](../science/data_encoding.md#5-the-surviving-density-profile), [uniform overlap hypothesis](../science/coherence_bound.md#1-statement), [initial signed contrast](../science/density_transport.md#5-the-fixed-weight-population-has-an-initial-signed-contrast).

### M16: An exact decoder inside the same architecture

**Phase:** Narrative/innovation.

**Central question:** Is a perfect phase classifier actually expressible with the allowed resources and sampled matching skeleton?

**Understanding target:** Explain how the inverse encoder and a control-basis rotation decode every nuisance value without knowing it. Relate a prescribed linear-depth decoder word to its greedy embedding in the random matching sequence. Distinguish the high-probability existence of an allowed gate assignment from its discovery by local optimization.

**Dependencies and story role:** Depends on M05, M09, and M13–M14. It establishes that the later phase-gradient upper bound is compatible with an efficiently representable exact target.

**Conceptual connection:** Expressivity is a property of the gate family; Haar-initialization geometry concerns the sampled assignments within that family. The known decoder also fixes the computational-hardness scope.

**Source pointers:** Anchor context: [§§IV.2 and IX][larocca]. Project: [decoder and matching embedding](../science/data_encoding.md#7-exact-decoder-and-matching-skeleton-expressivity), [resources](../science/data_encoding.md#8-per-example-resource-account), [expressivity interpretation](../science/interpretation.md#5-what-probability-and-expressivity-add).

### M17: Conditional classical populations from quantum gates

**Phase:** Narrative/innovation.

**Central question:** Which part of the interacting quantum evolution becomes a classical exclusion process after averaging?

**Understanding target:** Explain how a conserving Haar gate averages one-particle populations into a fair swap/no-swap update. Hold both the nuisance value and matching schedule fixed while composing those updates. Distinguish this conditional population law from the one-body matrix obtained after also averaging the matching choice.

**Dependencies and story role:** Depends on M04, M07, M11, and M15. It begins the phase proof with the correctly conditioned classical probability object.

**Conceptual connection:** The closed averaged population dynamics permits a concentration argument without making the unaveraged circuit or its complete quantum gradient classically simulable.

**Source pointers:** Anchor context for local-group stochastic methods: [§III.3][larocca]. Project: [conditional exclusion process](../science/coherence_bound.md#2-haar-averaged-populations-are-a-conditional-exclusion-process), [matching-averaged one-body matrix](../science/density_transport.md#2-the-one-body-transfer-matrix).

### M18: Matching projections retain a common harmonic statistic

**Phase:** Narrative/innovation.

**Central question:** Can one fixed charge statistic distinguish the branches for every matching schedule?

**Understanding target:** Relate the two matching projections through their action on the first harmonic. Explain why a matching change contributes a factor $`c_n=\cos(2\pi/n)`$, while a repeat contributes no extra contraction. Identify the bounded first-projection mismatch and the resulting conditional mean separation at diffusive depth.

**Dependencies and story role:** Depends on M11, M15, and M17. It supplies a schedule-uniform surviving statistic before any probability tail estimate is applied.

**Conceptual connection:** The bound concerns the overlap of this particular data profile and statistic. It does not substitute a global unitary-design mixing time for that overlap calculation.

**Source pointers:** Anchor context for analytical variance methods: [§III.3][larocca]. Project-specific identity: [matching projections](../science/coherence_bound.md#3-an-exact-identity-for-matching-projections), [perfect-wall refinement](../science/coherence_bound.md#exact-perfect-wall-identity).

### M19: Negative dependence yields an exponential branch-error bound

**Phase:** Narrative/innovation.

**Central question:** Why is a macroscopic difference of means enough here to distinguish the branches with exponentially small error?

**Understanding target:** Identify the imported preservation of the strongly Rayleigh property and its implication of negative association. Explain the fixed-charge conversion to nonnegative statistic weights and the role of a moment-generating-function bound. Keep the concentration argument conditional on the individual branch and schedule; arbitrary mixtures are not assigned the same dependence property.

**Dependencies and story role:** Depends on M07 and M17–M18. It converts the surviving mean separation into auxiliary branch-discrimination errors needed by the quantum interference argument. The charge discriminator is a proof device, not an extra classifier measurement.

**Conceptual connection:** The exponent follows from an extensive mean gap and controlled fluctuations, not from a bare statement that two expectations differ.

**Source pointers:** Anchor context: [§§III.1 and III.3][larocca]. Project and its attributed probability input: [conditional exclusion process](../science/coherence_bound.md#2-haar-averaged-populations-are-a-conditional-exclusion-process), [weighted concentration](../science/coherence_bound.md#4-weighted-concentration-with-explicit-constants).

### M20: Branch distinguishability bounds squared quantum interference

**Phase:** Narrative/innovation.

**Central question:** How does a classical charge discriminator constrain the quantum relative-phase signal in the readout?

**Understanding target:** Explain the role of a projector that commutes with $`Z_0`$. Follow the conceptual split of the off-diagonal amplitude into its two projector sectors and identify why the branch errors bound its squared magnitude. Distinguish this second-moment statement from cancellation of an averaged complex amplitude.

**Dependencies and story role:** Depends on M01, M06–M07, and M19. It is the central passage from population transport to the actual phase-sensitive quantum observable.

**Conceptual connection:** Surviving information about which macroscopic branch is present restricts the interference accessible to this readout. The statement is observable-specific and preserves the global quantum information.

**Source pointers:** Anchor context for operator alignment: [§§IV.1 and IV.3][larocca]. Project inequality: [projector bound on squared interference](../science/coherence_bound.md#5-a-projector-inequality-bounds-squared-interference), [physical mechanism](../science/interpretation.md#4-why-transport-helps-one-task-and-restricts-the-other).

### M21: From interference to a derivative at the actual Haar gate

**Phase:** Narrative/innovation.

**Central question:** Why does a small interference moment control each native derivative at the same initialized circuit?

**Understanding target:** Relate the generator spectrum to the frequency set $`\{-2,-1,0,1,2\}`$ of one gate variation. Explain how Parseval bounds an angle-averaged derivative square and how Haar left invariance transfers that average to the original gate. Recognize that the proof introduces an auxiliary angle, not an additional physical gate or independently initialized model.

**Dependencies and story role:** Depends on M03, M07, and M20. It converts the quantum-observable bound into the coordinatewise gradient upper bound.

**Conceptual connection:** The fixed local tangent convention is what allows one common physical initialization to support every derivative estimate.

**Source pointers:** Anchor context for analytical gradient methods: [§III.3][larocca]. Project: [Parseval and Haar transfer](../science/coherence_bound.md#6-parseval-and-haar-invariance-control-every-native-derivative), [native coordinates](../science/loss_and_geometry.md#4-native-tangent-coordinates-and-their-normalization).

### M22: The complete phase gradient and its high-probability suppression

**Phase:** Narrative/innovation.

**Central question:** What changes when the bound includes every local tangent of every gate?

**Understanding target:** Explain why summing $`M=3nD`$ coordinate bounds preserves exponential suppression at diffusive depth. Identify the zero coordinate means and the distinction between variance sums and correlated gradient entries. Relate the full-energy upper bound to simultaneous small transverse-axis gradients. Use M20's amplitude bound separately to explain near-random initialized classification error.

**Dependencies and story role:** Depends on M08 and M20–M21. It completes the phase side of the main theorem with its correct circuit-wide and probabilistic quantifiers.

**Conceptual connection:** The argument establishes initialization blindness to the phase label even though M16 supplies an exact classifier elsewhere in the same allowed architecture.

**Source pointers:** Anchor context: [§III.1][larocca]. Project: [full phase theorem](../science/coherence_bound.md#1-statement), [sum over native derivatives](../science/coherence_bound.md#6-parseval-and-haar-invariance-control-every-native-derivative), [high-probability consequences](../science/loss_and_geometry.md#6-high-probability-consequence-for-transverse-gradients).

### M23: A signed density response at one actual gate

**Phase:** Narrative/innovation.

**Central question:** How does the conserved profile produce a nonzero supervised derivative without averaging away the labels?

**Understanding target:** Identify the forward input difference and backward readout difference at a selected hopping gate. Explain the Haar one-particle Bloch orientation, the balanced-loss factor, and the probability that the chosen wall edge is present. Form the signed nuisance-averaged profile before applying conditional Jensen.

**Dependencies and story role:** Depends on M06–M07, M11, and M15. It starts the complementary lower-bound proof from an exact conditional response of the same circuit model.

**Conceptual connection:** An actual population-loss lower bound requires a protected signed response. A collection of large per-example squared derivatives could cancel after the examples are combined.

**Source pointers:** Anchor context: [§§III.3 and IV.3][larocca]. Project: [conditional Haar-gate response](../science/density_transport.md#3-exact-conditional-response-of-an-actual-haar-gate), [fixed-weight signed contrast](../science/density_transport.md#5-the-fixed-weight-population-has-an-initial-signed-contrast).

### M24: Fourier filtering and the polynomial density floor

**Phase:** Narrative/innovation.

**Central question:** When does the transported local readout retain enough overlap to certify a polynomial density-gradient moment?

**Understanding target:** Explain how the first Fourier pair survives while higher modes become a bounded remainder. Identify the suffix-depth threshold and why it cannot be omitted for a distant gate. Combine the resulting readout difference with M23 to obtain the fixed-weight floor; recognize how a longer prefix produces a common sign for more general profiles and allows distinct layer energies to be summed.

**Dependencies and story role:** Depends on M05, M11, and M23. It completes the density side and identifies which additional assumptions support its broader-profile extension.

**Conceptual connection:** A spatially uniform conserved charge gives no derivative. The lower bound comes from the matched nonuniform mode, with input and readout overlaps both present.

**Source pointers:** Anchor context for structured state/readout overlap: [§IV.3][larocca]. Project: [suffix Fourier bound](../science/density_transport.md#4-a-suffix-fourier-bound-with-explicit-constants), [fixed-weight lower bound](../science/density_transport.md#5-the-fixed-weight-population-has-an-initial-signed-contrast), [general profiles and internal layers](../science/density_transport.md#6-general-profiles-and-a-sum-over-internal-layers).

### M25: Exact logical-axis covariance

**Phase:** Narrative/innovation.

**Central question:** How do the density and phase bounds combine into a geometric statement for every logical label axis?

**Understanding target:** Define the three-axis population-gradient covariance. Explain why an input phase on the encoded control rail implements the same logical Z rotation for every nuisance value, and why right absorption preserves all fixed left-tangent coordinates. Relate this symmetry to equal transverse responses, zero cross terms, and the axis dependence $`\kappa_\perp(u_x^2+u_y^2)+\kappa_Zu_z^2`$.

**Dependencies and story role:** Depends on M03, M10, M14, M22, and M24. It joins both proof mechanisms into the central task-space anisotropy.

**Conceptual connection:** This is an averaged Gram matrix of population-loss gradients. Its interpretation does not automatically extend to a per-example neural tangent kernel, Hessian, Fisher matrix, or optimizer condition number.

**Source pointers:** Anchor context: [§§IV.1–IV.3][larocca]. Project: [exact covariance and Haar absorption](../science/loss_and_geometry.md#5-mean-zero-derivatives-and-exact-axial-covariance), [anisotropy interpretation](../science/interpretation.md#3-the-anisotropy-at-initialization).

### M26: Matching switches and the logarithmic depth window

**Phase:** Narrative/innovation.

**Central question:** How does the random matching word extend the controlled separation beyond a fixed diffusive depth?

**Understanding target:** Distinguish the number of consecutive matching changes from the initial-mismatch-plus-switch count $`\nu`$. Explain why the latter is exactly binomial for the perfect-wall reference and bounds the general-profile contraction. Connect its concentration to the simultaneous polynomial density floor and stretched-exponential phase upper in the stated $`n^2\log n`$ window.

**Dependencies and story role:** Depends on M07, M18, and M22–M24. It adds controlled depth dependence to the joined theorem.

**Conceptual connection:** A sufficient range for two inequalities is not a sharp dynamical crossover. The switch statistic used for transport also has a different role from the decoder's matching-word embedding in M16.

**Source pointers:** Anchor context for concentration methods: [§§III.1 and III.3][larocca]. Project: [matching statistics and logarithmic window](../science/coherence_bound.md#7-matching-statistics-and-the-logarithmic-window), [density depth corollaries](../science/density_transport.md#7-logarithmic-depth-corollaries).

### M27: Finite constants and the meaning of verification

**Phase:** Narrative/innovation.

**Central question:** What do explicit finite-size bounds and small-system checks establish about the asymptotic result?

**Understanding target:** Distinguish a lower bound, an upper bound, a measured energy, and an inferred onset. Explain why a valid exponential asymptotic estimate can remain quantitatively weak at modest sizes. Separate exact finite algebra checks, scalar bound evaluation, and native encoder verification from the analytical proof and imported probability theorem; the encoder's $`n=4`$ check does not change the transport hypothesis $`n\ge8`$.

**Dependencies and story role:** Depends on M13, M22–M26. It identifies the strength of the evidence and the practical meaning of the theorem's constants.

**Conceptual connection:** Numerical agreement supports the checked components, while the asymptotic scaling and universal quantifiers rest on the proofs. The finite bound table describes neither training performance nor the location of a transition.

**Source pointers:** Anchor context: [§III.3][larocca]. Project: [finite-size quantities](../science/finite_size.md#1-quantities-being-evaluated), [loose constants](../science/finite_size.md#3-why-a-valid-asymptotic-theorem-can-have-loose-constants), [verification scope](../verification/README.md#what-is-checked), [proof obligations](../verification/README.md#what-remains-a-proof-obligation).

### M28: Loss choice and label-independent gradients

**Phase:** Narrative/innovation.

**Central question:** Would the same full-gradient conclusion follow after replacing operational classification error by mean-squared error?

**Understanding target:** Distinguish normalized squared error of a sampled binary outcome from squared error of its predicted mean. Identify the extra squared-prediction term in the latter and the possible unlabeled-bias contribution to its derivative. Explain why a calibration gradient is not automatically a response to the phase label.

**Dependencies and story role:** Depends on M02, M10, and M22–M25. It makes the loss hypothesis explicit after the complete task-gradient result is available.

**Conceptual connection:** The theorem's useful supervised margin and an optimizer's chosen objective need not have the same full gradient. Changing the functional requires a separate analysis even when the underlying circuit and data source remain fixed.

**Source pointers:** Anchor context: [§§II.2 and IV.3][larocca]. Project: [mean-squared error distinction](../science/loss_and_geometry.md#3-mean-squared-error-is-a-different-functional), [loss interpretation](../science/interpretation.md#2-what-is-being-differentiated).

### M29: Measurement budgets and the scope of trainability

**Phase:** Narrative/innovation.

**Central question:** What resources suffice to estimate these gradients, and what learning claims do those budgets support?

**Understanding target:** Relate the two native frequencies to the valid four-setting shift rule and its bounded labeled-shot estimator. Distinguish componentwise accuracy from full-vector accuracy, and include the encoder plus classifier gate cost per shot. Separate a sufficient independent-shot budget from an optimal sampling lower bound, and a density ensemble-moment floor from typical successful training.

**Dependencies and story role:** Depends on M03, M08, M13, M16, and M21–M28. It connects the mathematical gradient geometry to its actual measurement procedure and known exact target.

**Conceptual connection:** Small initialized phase gradients, a known efficient decoder, and polynomial costs at inverse-polynomial additive precision are compatible statements. They do not establish a lower bound against every learner, collective measurement, or informed choice of parameters.

**Source pointers:** Anchor context: [§§II.2, III.1, and IX][larocca]. Project: [parameter-shift identity](../science/loss_and_geometry.md#8-parameter-shift-identity-for-the-actual-coordinates), [shot budgets](../science/loss_and_geometry.md#9-a-bounded-shot-estimator-and-its-resource-scope), [density probability limits](../science/loss_and_geometry.md#7-what-the-density-moment-does-and-does-not-establish), [per-example gate count](../science/data_encoding.md#8-per-example-resource-account).

### M30: Synthesis of hydrodynamic label-axis selection

**Phase:** Narrative/innovation.

**Central question:** What does the full construction establish about which information produces a gradient in an expressive quantum classifier?

**Understanding target:** Connect the common high-rank source and efficient decoder to both proof paths: conserved transport preserves a signed density response, while conditional concentration and a commuting projector restrict phase-sensitive interference; Parseval and Haar invariance make the latter a complete native-gradient bound. State the resulting axis covariance and separation at their proved depth scales, retaining the loss, metric, probability, and resource boundaries.

**Dependencies and story role:** Integrates M13–M29 using the model contract in M12. This closes the narrative phase with the whole contribution, rather than an additional isolated technical topic.

**Conceptual connection:** The result concerns task-dependent initialization geometry inside one large interacting sector. It sharpens the need for data, readout, and label alignment without claiming that all coherence decays, that density gradients ensure convergence, or that the structured source is quantum-hard. Its exact finite-depth statement and imported ingredients remain separately attributable.

**Source pointers:** Anchor context: [§§IV.1–IV.3 and IX][larocca]. Project synthesis: [main results](../science/model.md#4-full-gradient-separation), [physical mechanism](../science/interpretation.md#4-why-transport-helps-one-task-and-restricts-the-other), [scope](../science/interpretation.md#6-scope-of-the-physical-statement), [literature boundary](../references/RELATED_WORK.md#literature-boundary).

[larocca]: https://arxiv.org/html/2405.00781v2
