# From barren plateaus to label-dependent gradients

A quantum classifier receives a labeled state, applies a trainable circuit,
and predicts a binary label by measuring one qubit. This project asks how
the physical information carrying the label affects the entire gradient at
random initialization. The comparison holds the circuit ensemble, readout,
encoder, charge sector, and average input state fixed. Changing the label
from a density branch to a relative phase changes the gradient scaling.

The single educational anchor is **Martín Larocca et al., Barren Plateaus
in Variational Quantum Computing**, *Nature Reviews Physics* **7**, 174–189
(2025), [published article](https://doi.org/10.1038/s42254-025-00813-9).
All section numbers in this route refer to **arXiv:2405.00781v2**, revised
8 May 2025. Its [accessible text](https://arxiv.org/html/2405.00781v2) is
headed *A Review of Barren Plateaus in Variational Quantum Computing*;
the [version record](https://arxiv.org/abs/2405.00781v2) identifies the
published article. The source is linked rather than reproduced here.

The review provides the framework for circuit, data, measurement, and loss
concentration. This bridge develops the connections specific to conserved
transport and supervised labels. The [30-milestone map](MILESTONES.md)
organizes the understanding targets; the [scientific model](../science/model.md)
owns the exact assumptions and theorem statements. Read the source alongside
the relevant part of the project, without making the whole review a
prerequisite.

## Reading route

- [Targeted source readings](#1-targeted-source-readings)
- [Notation and assumptions](#2-notation-and-assumptions)
- [A complete dual-rail example](#3-a-complete-dual-rail-example)
- [The common data source and population loss](#4-the-common-data-source-and-population-loss)
- [Conserved transport and conditional concentration](#5-conserved-transport-and-conditional-concentration)
- [From branch information to every phase derivative](#6-from-branch-information-to-every-phase-derivative)
- [The signed density response](#7-the-signed-density-response)
- [The complete separation and task-axis geometry](#8-the-complete-separation-and-task-axis-geometry)
- [Exact decoding and measurement resources](#9-exact-decoding-and-measurement-resources)
- [Evidence and scientific synthesis](#10-evidence-and-scientific-synthesis)

## 1. Targeted source readings

Section references below use the fixed arXiv version. Their role is context;
the last column points to the project arguments that establish the result.

| Source sections | Reading focus | Connection supplied here |
|---|---|---|
| [II.1–II.2](https://arxiv.org/html/2405.00781v2) | Variational framework and its components | [Measured prediction and balanced population error](#4-the-common-data-source-and-population-loss) |
| [III.1 and III.3](https://arxiv.org/html/2405.00781v2) | Probabilistic concentration and variance methods | [Conditional populations, squared interference, and all native derivatives](#5-conserved-transport-and-conditional-concentration) |
| [IV.1–IV.3](https://arxiv.org/html/2405.00781v2) | Dimension, expressiveness, input states, and measurements | [Label contrast at a common average state](#4-the-common-data-source-and-population-loss) |
| [VI.1–VI.2](https://arxiv.org/html/2405.00781v2) | Shallow circuits and small dynamical algebras | [The half-filled interacting model and its finite-depth mechanism](#2-notation-and-assumptions) |
| [IX](https://arxiv.org/html/2405.00781v2) | Questions beyond barren plateaus | [Initialization, exact decoding, and the strength of the evidence](#9-exact-decoding-and-measurement-resources) |

The review's group-variance formula in IV.2 uses a group 2-design and module
conditions. Its U(1) example in VI.2 concerns Hamming weight that does not
grow with system size. Neither supplies this project's half-filled,
finite-depth theorem. The transport, population-loss, and conditional
concentration arguments are provided in the linked scientific pages.

## 2. Notation and assumptions

An expectation value describes the average of a measurement outcome. A
supervised loss also uses the supplied label. Keeping those two objects
separate explains why an identical average input state can accompany
different learning gradients.

| Framework object | Project notation | Meaning in this project |
|---|---|---|
| Input state | $`\rho_{u,+},\rho_{u,-}`$ | States conditioned on the two labels for a unit logical axis $`u`$ |
| Prediction expectation, of the form $`\ell_{\boldsymbol\theta}(\rho,O)`$ in the review | $`f_{u,y,x}`$ | Mean physical $`Z_0`$ outcome for one labeled example |
| Supervised objective | $`L_u`$ | Expected error of the sampled binary prediction |
| Labeled input contrast | $`\Delta_u=\rho_{u,+}-\rho_{u,-}`$ | A traceless Hermitian operator; it is not a density state |
| Unlabeled input state | $`\rho_{\mathrm{mix}}`$ | Common average of the two balanced classes |
| Initialized circuit | $`U`$, with matching depth $`D`$ | $`nD/2`$ independently sampled local conserving gates |
| One parameter derivative | $`g_{e,H}=\partial_{e,H}L_u`$ | Vary an actual gate as $`G_e\mapsto e^{-i\theta H}G_e`$ at zero angle |
| Full gradient energy | $`\mathcal G_u=\sum_{e,H}g_{e,H}^2`$ | Sum in the specified native tangent basis, with $`M=3nD`$ coordinates |
| Sampling counts | $`N_{\mathrm{nuis}}`$ and $`N_{\mathrm{shot}}`$ | Number of possible nuisance strings and number of physical trials, respectively |

The theorem uses a periodic ring with $`n\in4\mathbb N`$, $`n\ge8`$,
at total excitation number $`Q=n/2`$. A layer independently chooses the
even or odd perfect matching with equal probability. Each edge receives
a Haar gate from $`U(1)\times U(2)\times U(1)`$, acting on its zero-,
one-, and two-excitation blocks. The separate scalar phases permit
interactions; the circuit is not restricted to free-particle dynamics.

The half-filled sector has dimension $`\binom n{n/2}`$, which is
exponential. Conservation therefore does not place all dynamics in a
polynomial-dimensional state space. The proof instead isolates an averaged
one-body sector and a conditional classical population process. A simple
description of those averages is not a simulation of an individual
interacting quantum circuit.

The six norm-one native generators on edge $`(i,j)`$ are

```math
\left\{I,\ Z_i,\ Z_j,\ Z_iZ_j,
\frac{X_iX_j+Y_iY_j}{2},
\frac{X_iY_j-Y_iX_j}{2}\right\}.
```

They span the local Lie algebra. The identity direction gives zero
derivative and remains in the count $`M=3nD`$. A fixed Hilbert–Schmidt
normalization changes the energy by constant factors; an arbitrary
size-dependent reparameterization can change its scaling. The
[native-coordinate account](../science/loss_and_geometry.md#4-native-tangent-coordinates-and-their-normalization)
specifies the metric throughout.

## 3. A complete dual-rail example

Two physical qubits can carry a logical qubit while keeping one excitation:

```math
|0_L\rangle=|01\rangle,\qquad |1_L\rangle=|10\rangle,
\qquad |\pm_L\rangle=\frac{|01\rangle\pm|10\rangle}{\sqrt2}.
```

For the density task, label these first two basis states by $`+1`$ and
$`-1`$. For the phase task, use $`|+_L\rangle`$ and $`|-_L\rangle`$.
Both balanced tasks have average state

```math
\frac{|01\rangle\langle01|+|10\rangle\langle10|}{2}
=\frac{|+_L\rangle\langle+_L|+|-_L\rangle\langle-_L|}{2}.
```

On this logical space, measuring physical $`Z_0`$ is measuring logical
$`Z_L`$. Without a circuit it reads the density label perfectly and gives
either outcome with equal probability for each phase label. The average
state alone does not encode the correlation between the measurement and
the supplied label.

Now use the allowed hopping generator

```math
H_y=\frac{X_0Y_1-Y_0X_1}{2}=-Y_L,
\qquad U(\theta)=e^{-i\theta H_y}.
```

The equality with $`-Y_L`$ holds on the dual-rail subspace, with the basis
ordered as $`(|01\rangle,|10\rangle)`$. Conjugating the readout gives

```math
U(\theta)^\dagger Z_0U(\theta)
=\cos(2\theta)Z_L+\sin(2\theta)X_L.
```

For the balanced measured-error loss this means

```math
L_Z(\theta)=\frac{1-\cos(2\theta)}2,
\qquad
L_X(\theta)=\frac{1-\sin(2\theta)}2.
```

| Circuit angle | Density error | Phase error |
|---|---|---|
| $`\theta=0`$ | $`0`$ | $`1/2`$ |
| $`\theta=\pi/4`$ | $`1/2`$ | $`0`$ |

At zero angle the phase prediction has no label advantage, yet
$`L_X'(0)=-1`$. A small prediction signal at a point does not establish a
small derivative there. At the same point the density derivative is zero
because the density task is already solved. This example exposes why the
large-system result must control the initialized gradient distribution,
not merely evaluate a readout or find a good classifier.

This is a two-qubit explanatory calculation. It illustrates the local gate,
label, and measurement conventions, and carries no diffusive or
large-system separation claim. The transport theorem begins at $`n\ge8`$;
its exact decoder is developed in
[data encoding](../science/data_encoding.md#7-exact-decoder-and-matching-skeleton-expressivity).

## 4. The common data source and population loss

### A source with many nuisance values

The full construction uses $`m=n/2`$ dual rails. The first carries the
control label; the others carry a sampled nuisance string. A sequential
logical CNOT chain $`F`$ spreads the control bit across the rails, and a
fixed wire permutation $`\Pi`$ aligns the resulting physical strings with
a density wall. The encoder is $`E=\Pi F`$. For each nuisance value $`x`$,

```math
E|0_L,x\rangle=|z_x\rangle,\qquad
E|1_L,x\rangle=|\bar z_x\rangle.
```

The bar denotes complementing every physical bit. Both branches remain
half filled. A control superposition becomes a coherent superposition of
these two macroscopic branches by linearity.

The nuisance distribution is specified by choosing exactly
$`k=\lfloor m/8\rfloor`$ ones among the noncontrol *output* logical bits.
Adjacent XORs give the corresponding input nuisance string. Thus

```math
N_{\mathrm{nuis}}=\binom{m-1}{k},\qquad
\tau=\frac1{N_{\mathrm{nuis}}}\sum_x|x\rangle\langle x|.
```

The number of possible strings grows exponentially for large $`n`$, but
one example is sampled and prepared using polynomial resources. There is
no enumerated database in the state-preparation procedure. The
[native construction](../science/data_encoding.md#6-native-implementation-and-preparation-resources)
implements the logical operations with physical conserving gates.

For a unit Bloch vector $`u`$, the class states and their contrast are

```math
\rho_{u,\pm}=E\left[\frac{I\pm u\cdot\sigma}{2}\otimes\tau\right]E^\dagger,
\qquad
\Delta_u=E[(u\cdot\sigma)\otimes\tau]E^\dagger.
```

Each class has rank $`N_{\mathrm{nuis}}`$, and the two class supports are
orthogonal. Their common unlabeled state is

```math
\rho_{\mathrm{mix}}=E\left[\frac I2\otimes\tau\right]E^\dagger.
```

The label-conditioned contrasts $`\Delta_Z,\Delta_X,\Delta_Y`$ differ.
The different tasks supply different pure-state decompositions of the same
average operator. Equality of the average gives identical unlabeled
single-copy measurement statistics; it does not make the supervised tasks
identical.

### Which quantity is averaged and squared

Let $`y\in\{-1,+1\}`$ be the supplied label and let $`r`$ be the sign
actually observed in the physical $`Z_0`$ measurement. The error of one
prediction and its population expectation are

```math
\ell(y,r)=\frac{1-yr}{2},\qquad
L_u(U)=\frac12-\frac14\mathrm{Tr}[Z_0U\Delta_uU^\dagger].
```

The circuit $`U`$ is held fixed while labels, nuisance values, and outcomes
are averaged. The gradient of this population loss is then formed and
squared. Finally, the theorem averages that square over circuit
initialization. These are distinct stages of averaging.

For example, two equally likely examples with derivatives $`h`$ and
$`-h`$ have population derivative zero, while the average of their squared
derivatives is $`h^2`$. A lower bound on the latter would not lower-bound
the squared population derivative. The density proof maintains a signed
population contrast before taking its square. The phase proof uses
convexity in the upper-bound direction, where averaging squared quantities
is legitimate.

There is a second distinction between this measured error and a squared
loss on a prediction mean. With
$`f_{u,y,x}=\mathbb E[r\mid u,y,x,U]`$,

```math
J_{\mathrm{MSE},u}
=\frac12\mathbb E_{y,x}(f_{u,y,x}-y)^2
=2L_u-\frac12+\frac12\mathbb E_{y,x}f_{u,y,x}^2.
```

The last term can contribute derivatives unrelated to the phase-label
margin. A squared error on the sampled binary outcome instead obeys
$`(r-y)^2/4=\ell(y,r)`$ exactly. The
[loss account](../science/loss_and_geometry.md#3-mean-squared-error-is-a-different-functional)
keeps these objectives distinct.

## 5. Conserved transport and conditional concentration

### The local average and the slow spatial mode

On an edge $`(i,j)`$, the one-particle part of a Haar gate has no preferred
basis direction. Its averaged density response obeys

```math
\mathbb E_G[G^\dagger Z_iG]
=\mathbb E_G[G^\dagger Z_jG]
=\frac{Z_i+Z_j}{2}.
```

Let $`P_A,P_B`$ average coordinates over the corresponding matched pairs.
Averaging the fair choice of matching gives the one-body transfer matrix

```math
P=\frac{P_A+P_B}{2},\qquad
(Pv)_j=\frac12v_j+\frac14v_{j-1}+\frac14v_{j+1}.
```

A Fourier profile with spatial frequency $`2\pi k/n`$ is multiplied by
$`\lambda_k=\cos^2(\pi k/n)`$ in one averaged layer. The uniform mode
records total charge; its spatial difference is zero. The first nonuniform
mode has $`1-\lambda_1=\Theta(n^{-2})`$, so a depth of order $`n^2`$
changes its amplitude by a finite factor. This explains the diffusive
scale relevant to the learning comparison.

The density proof uses $`P^t`$ when averaging complete prefix or suffix
layers. For concentration, the full matching schedule must first be held
fixed. Its mean evolution is
$`P_{\sigma_D}\cdots P_{\sigma_1}`$. Replacing this conditional product
by $`P^D`$ inside a concentration claim would erase a required conditioning.

### What the classical process describes

Fix both the nuisance input and matching schedule. Haar-averaging the
populations of a basis-state branch is equivalent to swapping the two
occupation bits of each edge with probability one half. This is a
parallel exclusion process: bits move, and their total number remains
fixed. The averaged populations describe the quantum ensemble; individual
circuits still evolve coherently.

A deterministic occupation configuration is strongly Rayleigh, and each
swap/no-swap step is a partial symmetrization. The imported
[Borcea–Brändén–Liggett results](../science/coherence_bound.md#primary-source-used-in-the-proof)
give preservation under these steps and negative association of the final
occupation variables. Those research theorems supply a proof ingredient,
not an additional educational anchor.

Negative association controls products of monotone functions on disjoint
sets of occupation variables. It is enough for the exponential-moment
bound used here, without assuming the bits are independent. It is applied
to each conditioned population measure. No closure under arbitrary
mixtures of schedules or nuisance values is assumed.

### An extensive mean gap

Set $`a=n/4`$ and use the aligned harmonic

```math
f_j=\sin\left[\frac{2\pi}{n}\left(j-a-\frac12\right)\right],
\qquad S_f=\sum_j f_jZ_j.
```

Every positive input branch of the fixed-weight source has harmonic
overlap at least $`\beta n`$, where $`\beta=2/\pi-1/4>0`$.
The matching projections preserve this overlap up to a factor determined
by the number of switches between matchings. In particular, for fixed
schedule and input, the mean $`\mu`$ of $`S_f`$ obeys

```math
\mu\ge(\beta n-\pi)c_n^D,
\qquad c_n=\cos(2\pi/n),
```

when $`\beta n>\pi`$. The complementary branch has mean $`-\mu`$.
At fixed diffusive depth $`D=\lfloor\alpha n^2\rfloor`$,
$`c_n^D=\exp[-2\pi^2\alpha+o(1)]`$, so the gap remains proportional
to $`n`$ with an $`\alpha`$-dependent constant.

To use the negative-association estimate with nonnegative weights, define

```math
w_j=\frac{1+f_j}{2},\qquad
T=\sum_jw_jN_j=\frac n4-\frac14S_f.
```

Here $`N_j=(I-Z_j)/2`$, fixed half filling is used, and
$`0\le w_j\le1`$. The two means of $`T`$ lie on opposite sides of
$`n/4`$. The exponential-moment estimate makes each wrong-side
probability at most $`\exp[-\mu^2/(8n)]`$. A mean separation of order
$`n`$ consequently yields an exponentially small error, with every
conditioning still in place. The
[concentration proof](../science/coherence_bound.md#4-weighted-concentration-with-explicit-constants)
derives the constants explicitly.

## 6. From branch information to every phase derivative

### The commuting projector supplies the quantum step

Write the two evolved branches for one nuisance value as
$`|\alpha_x\rangle=U|z_x\rangle`$ and
$`|\gamma_x\rangle=U|\bar z_x\rangle`$. The phase task depends on
their interference in the readout:

```math
A_x=\langle\gamma_x|Z_0|\alpha_x\rangle.
```

Let $`\Pi_T`$ project onto computational strings with $`T\le n/4`$.
Both $`\Pi_T`$ and $`Z_0`$ are diagonal, so they commute. Denote the
wrong-side probabilities of the two quantum branches by

```math
e_{+,x}=\langle\alpha_x|(I-\Pi_T)|\alpha_x\rangle,
\qquad
e_{-,x}=\langle\gamma_x|\Pi_T|\gamma_x\rangle.
```

Splitting the amplitude into the two projector sectors and applying
Cauchy–Schwarz gives

```math
|A_x|\le\sqrt{e_{+,x}}+\sqrt{e_{-,x}},
\qquad |A_x|^2\le2(e_{+,x}+e_{-,x}).
```

The Haar averages of these errors are precisely the conditioned classical
errors bounded above. This converts a population statement into a bound
on the squared magnitude of an actual quantum interference amplitude.
Commutation is essential: an observable that connects the two projector
sectors need not obey this argument. The statistic $`T`$ is an analytical
device and adds no measurement to the classifier.

The population amplitude is $`\bar A=\sum_xp_xA_x`$. Convexity gives
$`|\bar A|^2\le\sum_xp_x|A_x|^2`$, allowing the nuisance average
after the conditional bound. With
$`m_*=\max\{\beta n-\pi,0\}`$,

```math
\mathbb E_G[|\bar A|^2\mid\sigma]
\le\min\left\{1,
4\exp\left[-\frac{m_*^2c_n^{2D}}{8n}\right]\right\}.
```

The estimate controls a second moment. Haar symmetry can also make a
first moment zero, but zero mean alone permits large positive and negative
fluctuations. For instance, a uniformly sampled $`\cos\theta`$ has zero
mean and second moment $`1/2`$.

### Why small interference also controls the derivatives

The exact phase losses are

```math
L_X=\frac12-\frac12\mathrm{Re}\bar A,
\qquad
L_Y=\frac12-\frac12\mathrm{Im}\bar A.
```

Vary one actual gate in one native direction. Because the generator's
spectrum is contained in $`\{-1,0,1\}`$, its eigenvalue differences
lie between minus two and two. The perturbed amplitude therefore has
only five possible Fourier frequencies:

```math
\bar A(\theta)=\sum_{r=-2}^{2}a_re^{ir\theta},\qquad
\frac1{2\pi}\int_0^{2\pi}|\bar A'(\theta)|^2\,d\theta
\le\frac4{2\pi}\int_0^{2\pi}|\bar A(\theta)|^2\,d\theta.
```

This is an integrated derivative bound, not a pointwise assertion that
every small function value has a small slope. The two-qubit example above
shows why that distinction matters. Haar left invariance makes
$`e^{-i\theta H}G_e`$ have the same distribution as $`G_e`$ for each
angle. It transfers the integrated bound to the derivative at zero
angle averaged over the original gate ensemble. The loss factor
$`1/2`$ cancels the factor four after squaring, giving

```math
\mathbb E_G[(\partial_{e,H}L_u)^2\mid\sigma]
\le\mathbb E_G[|\bar A|^2\mid\sigma],\qquad u=X,Y.
```

Summing over all $`M=3nD`$ directions yields the full-gradient upper
bound. The coordinates may be correlated; linearity of expectation and
the sum of squares require no independence. The auxiliary angle is a
proof tool attached to an existing gate, with no additional circuit layer.
The [complete argument](../science/coherence_bound.md#6-parseval-and-haar-invariance-control-every-native-derivative)
also shows that each derivative has zero ensemble mean, so the summed
second moments are a sum of coordinate variances.

## 7. The signed density response

The density argument needs a lower bound and therefore handles averaging
differently. Let $`\bar q`$ be the positive class's *population*
magnetization profile, already averaged over nuisance. Write
$`p=k/(m-1)`$ and $`\eta=1-2p`$. Away from the two control-rail sites,
$`\bar q`$ is $`\eta`$ times the perfect wall; the control sites have
the full wall magnitude. At the wall edge $`(a,a+1)`$,

```math
\Delta q_0=\bar q_a-\bar q_{a+1}\le-2\eta.
```

The sign remains in the mean before a square is formed. The nuisance
source therefore does not cancel the chosen population response.

Average the classifier's suffix of $`s=D-1`$ layers. The backward-evolved
readout has one-body coefficient vector $`b=P^se_0`$, with edge
difference $`\Delta b_s=b_a-b_{a+1}`$. The first Fourier mode gives

```math
\Delta b_s\ge\frac4{n^2}\lambda_1^s,
\qquad \lambda_1=\cos^2(\pi/n),\qquad
s\ge\left\lceil\frac{n^2}{\pi^2}\right\rceil.
```

The depth condition suppresses higher-mode cancellations and lets the
remote readout couple to the wall edge. Total charge by itself would
have no edge difference. The useful response comes from the spatially
varying conserved mode.

When the first layer contains that edge, vary its actual Haar gate along
the hopping direction. Conditional on its one-particle Haar block and the
edge being present, the mean population-loss derivative over the remaining
circuit randomness is
$`-\Delta q_0\Delta b_s n_y/2`$, where $`n_y`$ is one coordinate of a
uniform unit Bloch vector. Its second moment is $`1/3`$. Conditional
Jensen and the probability one half that the edge is present give

```math
\mathbb E g_*^2
\ge\frac{(\Delta q_0)^2(\Delta b_s)^2}{24}
\ge\frac{8\eta^2}{3n^4}\lambda_1^{2(D-1)}.
```

Here $`g_*=0`$ when the chosen edge is absent. The full gradient contains
this nonnegative square, which proves its lower bound. At fixed
diffusive depth above the threshold,
$`\lambda_1^{2(D-1)}=\exp[-2\pi^2\alpha+o(1)]`$, leaving the
polynomial factor $`n^{-4}`$.

For more general profiles with positive harmonic overlap, a long enough
prefix first selects a common sign in the population profile. Summing
the resulting nonnegative coordinate energies over many internal layers
recovers a polynomial floor. That broader result has an additional
profile-dependent depth requirement; the explicit fixed-weight source
uses the sharper first-layer argument above. Both versions are proved in
[density transport](../science/density_transport.md).

## 8. The complete separation and task-axis geometry

For the specified source, $`n\in4\mathbb N`$, and sufficiently large
$`n`$, fix $`\alpha>1/\pi^2`$ and
$`D=\lfloor\alpha n^2\rfloor`$. The two arguments establish

```math
\mathbb E\mathcal G_Z=\Omega_\alpha(n^{-4}),\qquad
\mathbb E\mathcal G_X,\ \mathbb E\mathcal G_Y
\le\exp[-\Omega_\alpha(n)].
```

The expectations refer to the same initialization law and the same
native metric. The phase upper also holds for every fixed matching schedule,
with expectation over the Haar gates alone. The density lower
uses the random matching ensemble. These quantifiers are part of the
[finite theorem](../science/model.md#theorem-1-finite-full-gradient-bounds).

For arbitrary logical label axes, form the ensemble matrix

```math
K_{ab}=\mathbb E[\nabla L_a\cdot\nabla L_b],
\qquad a,b\in\{X,Y,Z\}.
```

An onsite phase on the physical image of the control rail implements a
logical rotation about $`Z`$, independently of nuisance. Absorbing this
phase on the right of the corresponding first-layer Haar gate preserves
both the ensemble and the fixed left-tangent directions. Consequently,

```math
K=\mathrm{diag}(\kappa_\perp,\kappa_\perp,\kappa_Z),\qquad
\mathbb E\mathcal G_u
=\kappa_Zu_z^2+\kappa_\perp(u_x^2+u_y^2).
```

This is axial symmetry of an ensemble covariance. It does not assert
equal phase gradients in each realized circuit. The matrix compares
three population-gradient vectors; it is not a Hessian, Fisher matrix,
or per-example neural tangent kernel. Its
[derivation](../science/loss_and_geometry.md#5-mean-zero-derivatives-and-exact-axial-covariance)
connects the discrete tasks into one logical-axis statement.

An upper moment bound $`\mathbb E\mathcal G_X\le B`$ gives
$`\Pr(\mathcal G_X\ge t)\le B/t`$ by Markov's inequality. Thus the
phase result also controls typical full gradients with appropriate
thresholds. A lower moment can be supported by a small fraction of
initializations; the density theorem alone does not give a
constant-probability convergence guarantee. The
[probability analysis](../science/loss_and_geometry.md#6-high-probability-consequence-for-transverse-gradients)
states the actual consequences on both sides.

Counting switches in the fair matching sequence sharpens the phase
estimate. Together with the density bound it gives, for fixed
$`0<\epsilon<1`$,

```math
\left\lceil\frac{n^2}{\pi^2}\right\rceil+1
\le D\le\frac{(1-\epsilon)n^2\log n}{2\pi^2},
```

the estimates give

```math
\mathbb E\mathcal G_Z=\Omega(n^{-5+\epsilon}),\qquad
\mathbb E\mathcal G_X,\ \mathbb E\mathcal G_Y
\le e^{-\Omega(n^\epsilon)}.
```

This logarithmic extension is a validity window for the estimates.
An upper bound becoming uninformative beyond its window establishes
neither a sharp transition nor a revival of the gradient. The
[matching-count proof](../science/coherence_bound.md#7-matching-statistics-and-the-logarithmic-window)
and [density corollary](../science/density_transport.md#7-logarithmic-depth-corollaries)
give the precise domains.

## 9. Exact decoding and measurement resources

### A good classifier exists in the same native architecture

Applying $`E^\dagger`$ recovers the logical control and nuisance input.
A final logical rotation $`R_u`$ turns the chosen control basis into the
physical $`Z_0`$ basis. Thus $`R_uE^\dagger`$ classifies every nuisance
value exactly, without learning or identifying that value first.

Preparation and decoding use $`n`$ qubits, no ancilla, $`O(n)`$ matching
depth, and $`O(n^2)`$ nearest-neighbor conserving gates. Loading the
initial half-filled reference state is charged separately from its
subsequent conserving evolution. Classical nuisance sampling is
polynomial and requires no QRAM.

The explicit decoder specifies a word of $`L=O(n)`$ matching parities.
In a random skeleton, wait for each required parity and put identity
gates on unused edges or layers. The next required parity matches with
probability one half, conditional on the past. For $`D\ge4L`$, the
decoder fails to fit with probability at most

```math
\Pr[\mathrm{Bin}(D,1/2)\lt L]\le e^{-D/16}.
```

This concerns an allowed gate assignment on the sampled architecture.
It is different from drawing that assignment from Haar measure or
finding it by gradient descent. An expressible exact decoder and a
small initialized phase gradient are compatible statements.

### Derivatives are measurable with the stated coordinates

The native spectrum bounds used in the proof also give a derivative
estimator. If $`F(\theta)`$ denotes either the prediction expectation or
the operational loss with one gate varied, then

```math
F'(\theta)=F(\theta+\pi/4)-F(\theta-\pi/4)
+\frac{1-\sqrt2}{2}
\left[F(\theta+\pi/2)-F(\theta-\pi/2)\right].
```

The two frequencies one and two are both possible for a hopping
generator. For a diagonal generator with spectrum $`\{-1,+1\}`$,
only nonzero frequency magnitude two appears and the first difference
suffices. All
shifted gates stay in the allowed conserving group.

One can sample a shift, a label, and a nuisance value, run the shifted
circuit, and use its single binary outcome to estimate a population
derivative. No sum over the exponentially many possible inputs is
required. For the independent-shot procedure in
[loss and geometry](../science/loss_and_geometry.md#9-a-bounded-shot-estimator-and-its-resource-scope),
the sufficient budgets are

| Accuracy goal, at failure probability at most $`\delta`$ | Sufficient total shots |
|---|---|
| One derivative, additive error $`\eta`$ | $`O(\eta^{-2}\log(1/\delta))`$ |
| All $`M`$ coordinates, error at most $`\eta`$ in each | $`O(M\eta^{-2}\log(M/\delta))`$ |
| Whole vector, Euclidean error $`\varepsilon`$ | $`O(M^2\varepsilon^{-2}\log(M/\delta))`$ |

Each shot uses $`nD/2+O(n^2)`$ native gates including preparation, which
is $`\Theta(n^3)`$ at diffusive depth. Exponentially fine precision makes
these displayed sufficient budgets exponential. A gradient upper bound
does not turn that estimator's budget into an optimal lower bound on
every measurement or learning strategy. The explicit efficient decoder
also fixes the interpretation of the source: this result separates
initialized gradient responses, without asserting a hard classification
problem or quantum advantage.

## 10. Evidence and scientific synthesis

The [finite-size account](../science/finite_size.md) evaluates the actual
analytic estimates. Their constants are conservative and can give a
weak finite-size certificate even where the asymptotic statement is
valid. Depth, system size, and the prefactors should be read together;
the result supplies no device-scale performance forecast.

The [verification route](../verification/README.md) checks matching
identities, Fourier estimates, native generators, projector bounds,
derivative formulas, and the explicit encoder and decoder on finite
instances. These checks support their tested assertions. The
asymptotic scaling follows from the analytical arguments and their
imported probability theorems. The [related-work account](../references/RELATED_WORK.md)
separates those ingredients from the project's combined statement.

The complete story joins three facts. First, the label remains present
in the structured input and is recoverable by a common efficient
decoder. Second, at diffusive initialization, conserved spatial
information continues to distinguish the complementary branches and
bounds their interference in the fixed readout. Third, that same
transport supports a signed population-density derivative while every
native phase derivative has a small second moment. The shared average
state therefore does not determine the learning response: the labeled
decomposition and its relation to conserved transport matter.

Continue through the [30 milestones](MILESTONES.md) for the project-wide
understanding route, or use the [model](../science/model.md),
[phase proof](../science/coherence_bound.md), and
[density proof](../science/density_transport.md) for the exact statements.
