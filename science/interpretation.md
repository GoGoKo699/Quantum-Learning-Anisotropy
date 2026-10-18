# Physical and learning interpretation

The result isolates how the **information carried by the label** changes the initialization gradient of a charge-conserving classifier. At depth proportional to the square of the ring size, density labels have an inverse-polynomial gradient second-moment lower bound, while phase labels have an exponentially small upper bound for the complete specified local-tangent gradient. The circuit, local readout, data-preparation encoder, and unlabeled average state are shared.

The [circuit model](model.md), [data construction](data_encoding.md), [density proof](density_transport.md), and [coherence proof](coherence_bound.md) give the definitions and finite-size constants. The [loss and geometry account](loss_and_geometry.md) derives the operational loss, covariance, and measurement statements. This page explains what those statements imply and where their assumptions enter.

## 1. The controlled comparison

There are $`m=n/2`$ logical qubits in dual-rail encoding. Each rail pair contains one physical excitation, so all examples lie in the same half-filled sector. A fixed conserving encoder $`E`$ maps a control qubit and a classical nuisance register to the physical ring. For a logical axis $`u`$ and a balanced label $`y\in\{+1,-1\}`$,

```math
\rho_{u,y}
=E\left[|u,y\rangle\langle u,y|\otimes\tau\right]E^\dagger.
```

The nuisance distribution has exponentially many possible values. Each axis has orthogonal class supports, and a common inverse encoder followed by the appropriate control-basis rotation perfectly decodes every nuisance value. The data are available through an explicit physical preparation circuit of linear depth and quadratic gate count; no quantum random-access memory is assumed.

All axes have exactly the same average state:

```math
\frac{\rho_{u,+}+\rho_{u,-}}2
=E\left[\frac{I_{\mathrm{control}}}{2}\otimes\tau\right]E^\dagger
=\rho_{\mathrm{mix}}.
```

For density labels, a pure example is one of two complementary computational-basis strings. For phase labels, it is their equal superposition with relative phase $`+1`$, $`-1`$, $`+i`$, or $`-i`$. The tasks use different decompositions of the same mixed state; they are not a relabeling of one identical list of pure states. Equality of the mean state implies equality of unlabeled single-copy measurement statistics, not equality of every possible data-access protocol involving repeated copies of a fixed example.

This comparison controls a limitation of diagnostics based only on the mean input state. A supervised derivative also depends on the class difference $`\rho_{u,+}-\rho_{u,-}`$. Earlier work established that the dataset and encoding can affect gradient concentration; the precise distinction between prediction derivatives and a population-loss derivative is essential here. See [Thanasilp et al., Sections III.1–III.2](https://arxiv.org/html/2110.14753v1) and the [source comparison](../references/RELATED_WORK.md).

## 2. What is being differentiated

One shot of the classifier measures physical $`Z_0`$ and uses the resulting sign as its predicted label. The expected error of that prediction is

```math
L_u(U)=\frac12-\frac14\mathrm{Tr}\!\left[
Z_0U(\rho_{u,+}-\rho_{u,-})U^\dagger\right].
```

The initialized circuit is held fixed across examples and shots. Averaging over Haar gates describes an ensemble of initializations; it does not prescribe fresh random gates on every evaluation.

Each actual two-qubit gate has six fixed local tangent directions spanning the conserving Lie algebra. They include the two hopping generators as well as diagonal phase directions. A coordinate replaces that gate by $`e^{-i\theta H}G`$ and differentiates at $`\theta=0`$. The gradient energy sums the squares of these derivatives over all gates. Including the zero identity derivative gives $`M=3nD`$ coordinates for $`D`$ physical layers.

This is a specified native metric on gate variations. Its polynomial-versus-exponential conclusion survives the constant-factor conversion to a Hilbert–Schmidt-orthonormal local basis. Arbitrary size-dependent rescaling of the parameters would change a gradient norm and is outside the comparison.

The definition of the loss also matters. Balanced labels remove the unlabeled readout bias from the operational error. Mean-squared error of **prediction means** contains an additional squared-prediction term, so its full gradient can include a calibration response even when the useful phase margin has a tiny gradient. Conversely, squared error of the binary measured outcome, divided by four, equals the one-shot classification error exactly. The [loss derivation](loss_and_geometry.md) keeps these two uses of squared error separate. A majority-vote or thresholded-mean classifier likewise needs its own risk analysis.

## 3. The anisotropy at initialization

For the explicit fixed-weight nuisance source, at $`D=\lfloor\alpha n^2\rfloor`$ with fixed $`\alpha>1/\pi^2`$, the proved bounds give

```math
\mathbb E\|\nabla_{\mathrm{nat}}L_Z\|^2
\ge C_\alpha n^{-4},
\qquad
\mathbb E\|\nabla_{\mathrm{nat}}L_X\|^2,
\ \mathbb E\|\nabla_{\mathrm{nat}}L_Y\|^2
\le e^{-c_\alpha n}
```

for positive constants and sufficiently large $`n`$. The finite-size bounds retain their explicit dependence on depth, harmonic contrast, and the number of coordinates. Their constants can be conservative; the asymptotic statement does not assert a large numerical gradient at modest system sizes.

Define the task-gradient covariance by

```math
K_{ab}=\mathbb E\!\left[
\nabla_{\mathrm{nat}}L_a\cdot\nabla_{\mathrm{nat}}L_b\right],
\qquad a,b\in\{X,Y,Z\}.
```

An on-site input phase implements an arbitrary logical rotation about the control's density axis, independently of nuisance. Absorbing that phase into the first Haar layer preserves the circuit distribution and the left-tangent convention. Consequently,

```math
K=\mathrm{diag}(\kappa_\perp,\kappa_\perp,\kappa_Z),
\qquad
\mathbb E\|\nabla_{\mathrm{nat}}L_u\|^2
=\kappa_Zu_z^2+\kappa_\perp(u_x^2+u_y^2).
```

The controlled separation is thus between orthogonal ways of encoding label information in the same logical qubit. This covariance is neither a neural tangent kernel indexed by individual examples nor a Fisher matrix, Hessian, or optimizer condition number. The comparison with measurement-score geometry is developed in [Ait Haddou, Sections II and VII–VIII](https://arxiv.org/html/2608.17085v1); that work holds the measurement fixed while changing the retained readout subspace, whereas this construction holds the local readout fixed and changes the task.

## 4. Why transport helps one task and restricts the other

The positive computational branches have a macroscopic component along a fundamental sinusoidal charge profile. Complementation reverses its sign. A conserving Haar gate equalizes the two averaged local occupations it acts on. Repeating these updates transports that profile diffusively. This one-body mechanism is established in [Khemani, Vishwanath, and Huse, Section III.1.1](https://arxiv.org/html/1710.09835v3) and [Rakovszky, Pollmann, and von Keyserlingk, Section III](https://arxiv.org/html/1710.09827v3).

For the density task, the spatial profile overlaps with the backward-transported local readout. Conditioning on a first-layer hopping gate leaves a nonzero label-dependent derivative. Squaring this conditional mean, then averaging its Haar orientation and the matching choice, yields the density second-moment lower bound. This calculation uses the signed population profile before squaring; an unsigned average of example-wise gradient variances would not establish it.

The phase task asks for interference between the two branches. At diffusive depth their macroscopic charge statistics are still distinguishable with exponentially small error. A projector onto the sign of the sinusoidal charge statistic commutes with $`Z_0`$. Splitting the off-diagonal readout matrix element with that projector bounds it by the branches' concentration errors.

The classical concentration statement is conditional. For each fixed matching schedule and input string, the averaged populations form a sequence of independent swap/no-swap updates. [Borcea, Brändén, and Liggett, Theorems 4.20 and 4.9](https://arxiv.org/html/0707.2340v2) provide stability under those updates and the resulting negative association. Averaging over schedules and nuisance values happens after this bound; no closure under arbitrary mixtures is assumed.

This controls the actual squared interference amplitude. Its conversion to a gradient bound requires another step: along each native tangent, the amplitude has Fourier frequencies of magnitude at most two. Parseval bounds the averaged derivative energy, and Haar invariance identifies that average with the derivative at the initialized gate. Applying this argument to every coordinate bounds the full gradient without assuming coordinate independence. A zero averaged coherence alone would not suffice.

## 5. What probability and expressivity add

An upper bound on the transverse gradient energy gives a high-probability statement by Markov's inequality. If $`B_{n,D}`$ denotes the finite transverse upper bound, then

```math
\Pr\!\left[\|\nabla L_X\|>\sqrt{B_{n,D}/\delta}\right]
\le\delta,
\qquad 0<\delta<1.
```

At fixed diffusive depth, one can choose both the gradient threshold and failure probability exponentially small. The same holds for $`Y`$. By contrast, a density second-moment lower bound alone does not show that a constant fraction of initializations have useful density gradients. It does not establish optimizer convergence, generalization, or a successful training trajectory. Operator-level initialization witnesses have related limitations; see [Kulshrestha et al., Sections II.4 and III.1](https://arxiv.org/html/2606.18515v1).

The exact decoder establishes representability within the allowed conserving gates. A typical sufficiently long even/odd matching schedule can accommodate its linear-depth native implementation by setting unused gates to identity. Thus the phase plateau is compatible with an efficiently representable perfect classifier. The construction does not say that random initialization lies near that decoder, or that local descent reaches it. Directly using the known inverse encoder is already an efficient solution for these data.

## 6. Scope of the physical statement

Each pure phase example contains one ebit across every nontrivial spatial bipartition. This input property differs from a volume-law entanglement assumption; see [Ortiz Marrero, Kieferová, and Wiebe](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040316). The extensive relative phase nevertheless remains sensitive to local dephasing. The noiseless bounds supply no noise tolerance or quantum computational advantage.

The suppression concerns access to a particular encoded coherence through a local readout and its local derivatives. Unitary evolution preserves the encoded information globally. Other coherence observables can have long hydrodynamic tails, including local operators without a simple conserved-density overlap. The mechanisms in [McCulloch, Jacoby, and Gopalakrishnan, Sections II.3 and III–V](https://arxiv.org/html/2604.27074v2), and the coherence measures of [Aditya et al., Sections II–IV](https://arxiv.org/html/2604.23192v1), therefore do not support a blanket statement that non-density information decays rapidly. The profile and branch-concentration assumptions are doing specific work here.

The proof extends beyond one domain wall to families with a uniformly positive macroscopic harmonic component. The explicit nuisance family satisfies this condition while preserving a common efficient decoder. It remains a structured, far-from-equilibrium source. A larger number of examples does not make it an equilibrium-typical source or a source of unknown computational difficulty.

Finally, charge relaxation, task-gradient suppression, and formation of an approximate unitary design are separate quantities. [Yada's moment-gap bounds](https://arxiv.org/html/2609.39458v1) describe late convergence of the full moment operator and distinguish transport from encounter-controlled relaxation across geometries. Applying such a bound to a classifier requires its own task-overlap and norm estimates. The direct finite-depth theorem does not use a global gap as a substitute for those estimates, and the depth where a displayed upper bound becomes uninformative is not a proved transition or recovery of trainability.
