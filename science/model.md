# Conserved transport and label-dependent gradients

## Scientific question

Can a quantum classifier retain a polynomial gradient response to one kind
of information while its whole local gradient is exponentially insensitive
to another, even when the two tasks have the same average input state?

This model answers that question through conserved-density transport. Two
complementary branches carry opposite macroscopic density profiles. At
diffusive circuit depth, a charge statistic still distinguishes the branches.
That surviving distinction bounds their interference in the local readout
and suppresses the phase-label gradient. A separate signed response of the
diffusing density gives a polynomial lower bound for the density-label loss.

The result compares actual supervised population losses in one circuit
ensemble. It includes an extensive nuisance source and a fixed efficient
encoder and decoder. A polynomial density-gradient moment is an ensemble
statement; it is not a guarantee that a training algorithm succeeds.

## Reading route

| Question | Authoritative account |
|---|---|
| Which circuit, data source, loss, and gradient are being compared? | This page |
| How can the data be prepared and perfectly classified? | [Data encoding and decoding](data_encoding.md) |
| Why does surviving density information suppress every phase derivative? | [Coherence bound](coherence_bound.md) |
| Where does the polynomial population-gradient floor come from? | [Density transport](density_transport.md) |
| What is the exact logical-axis geometry, and what changes with the loss? | [Loss and geometry](loss_and_geometry.md) |
| How should the theorem and its resource limits be interpreted? | [Physical interpretation](interpretation.md) |
| What do the explicit constants certify at finite size? | [Finite-size bounds](finite_size.md) |
| Which ingredients and related results are established literature? | [Related work](../references/RELATED_WORK.md) |
| Which finite calculations can be reproduced? | [Verification](../verification/README.md) |

## 1. Circuit and conserved charge

Let $`n\in4\mathbb N`$, $`n\ge8`$, and place the qubits on the periodic cycle
with sites $`0,\ldots,n-1`$. The total excitation number is

```math
Q=\sum_{j=0}^{n-1}N_j,\qquad N_j=\frac{I-Z_j}{2}.
```

All supplied inputs belong to the sector $`Q=n/2`$. Its dimension is
$`\binom n{n/2}`$, which is exponential in system size.

Each of $`D`$ layers independently chooses one of the two perfect matchings,

```math
A=\{(0,1),(2,3),\ldots,(n-2,n-1)\},
\qquad
B=\{(1,2),(3,4),\ldots,(n-1,0)\},
```

with probability $`1/2`$. Every matched edge receives an independent Haar
gate from the full local conserving group

```math
\mathcal U_{\mathrm{loc}}
=U(1)\times U(2)\times U(1),
```

acting on the zero-, one-, and two-excitation blocks, respectively.
The phases of the one-dimensional blocks and the full one-particle unitary
are independent. The model includes interacting diagonal phases and is
not restricted to a Gaussian or matchgate ansatz.

There are $`nD/2`$ two-qubit gates. Depth counts matching layers, including
every gate in the classifier. State preparation is a separate, explicitly
charged resource.

### Fixed local tangent convention

At a gate $`G_e`$ on edge $`e=(i,j)`$, define a derivative by the replacement

```math
G_e\longmapsto e^{-i\theta H}G_e,\qquad \theta=0,
```

where the fixed six-generator basis is

```math
\mathcal H_e=
\left\{
I,\ Z_i,\ Z_j,\ Z_iZ_j,\
\frac{X_iX_j+Y_iY_j}{2},\
\frac{X_iY_j-Y_iX_j}{2}
\right\}.
```

Every generator has operator norm one and spectrum in
$`\{-1,0,1\}`$. They span the local real Lie algebra. The identity derivative
vanishes, but is retained in the convenient total count

```math
M=3nD.
```

For a loss $`L`$, write $`g_{e,H}=\partial_{e,H}L`$ and define

```math
\mathcal G(L)=\sum_{e,H}g_{e,H}^{\,2}
=\lVert\nabla L\rVert_{\mathrm{native}}^2.
```

This is a specified tangent-coordinate energy. The hopping generators and
the diagonal generators have different Hilbert–Schmidt norms; replacing the
basis by a fixed normalized basis changes the estimates only by constants.
An arbitrary parameterization or optimizer metric is not part of the claim.

Every coordinate has zero ensemble mean by Haar left invariance. Thus
$`\mathbb E\mathcal G`$ is also the sum of its coordinate variances.
All terms refer to the same initialized circuit. No independence among
different derivative coordinates is required.

## 2. One encoded nuisance source

Write $`m=n/2`$ and use adjacent dual rails

```math
\lvert0_{\mathrm L}\rangle=\lvert01\rangle,\qquad
\lvert1_{\mathrm L}\rangle=\lvert10\rangle.
```

Each rail has exactly one excitation. Let $`F`$ be the sequential CNOT chain
from rail 1 to 2, then 2 to 3, and so forth. Set $`a=n/4`$. A fixed physical
wire permutation $`\Pi`$ maps the all-logical-zero rail state to the wall
$`z`$ whose magnetization is

```math
q_j^{\mathrm{wall}}=
\begin{cases}
+1,&a+1\le j\le a+n/2,\\
-1,&\text{otherwise},
\end{cases}
```

with cyclic indices. The common encoder is $`E=\Pi F`$.
It does not include a control Hadamard.

For input control bit $`b`$ and nuisance string $`x_2,\ldots,x_m`$, the chain
produces

```math
y_1=b,\qquad y_j=b\oplus x_2\oplus\cdots\oplus x_j.
```

Hence changing the control complements every physical bit after encoding:

```math
E\lvert0,x\rangle=\lvert z_x\rangle,\qquad
E\lvert1,x\rangle=\lvert\bar z_x\rangle.
```

For the positive-control branch, sample exactly
$`k=\lfloor m/8\rfloor`$ ones uniformly among
$`y_2,\ldots,y_m`$, keeping $`y_1=0`$, and set
$`x_j=y_j\oplus y_{j-1}`$.
Let $`\tau`$ be the resulting diagonal nuisance mixture. Define

```math
p=\frac{k}{m-1},\qquad
N_{\mathrm{nuis}}=\binom{m-1}{k}.
```

The number of nuisance values grows as $`\exp[\Theta(n)]`$.
It is sampled by ordinary polynomial classical preprocessing.
The source does not require an enumerated exponential database.

For a unit logical Bloch vector $`u=(u_x,u_y,u_z)`$, the balanced binary
classification task supplies

```math
\rho_{u,\pm}
=E\left[
\frac{I\pm(u_xX+u_yY+u_zZ)}2\otimes\tau
\right]E^\dagger
```

with labels $`\pm1`$. For each axis, the two class supports are orthogonal
and have rank $`N_{\mathrm{nuis}}`$. Every axis has exactly the same unlabeled
average state:

```math
\rho_{\mathrm{mix}}
=\frac{\rho_{u,+}+\rho_{u,-}}2
=E\left[\frac I2\otimes\tau\right]E^\dagger.
```

The supplied pure-state ensembles for different axes are different
decompositions of this density operator.

The $`Z`$ task distinguishes the complementary density branches.
For $`X`$, each nuisance value supplies
$`(\lvert z_x\rangle\pm\lvert\bar z_x\rangle)/\sqrt2`$.
The $`Y`$ task uses the corresponding relative phases $`\pm i`$.
These pure phase examples have one ebit across a nontrivial bipartition.
Their high-rank class mixture comes from nuisance entropy.

## 3. Operational loss

The classifier applies $`U`$, measures the fixed physical $`Z_0`$, and uses
that random measured sign as its prediction. Its expected error is exactly

```math
L_u(U)
=\frac12-\frac14
\mathrm{Tr}\!\left[
Z_0U(\rho_{u,+}-\rho_{u,-})U^\dagger
\right].
```

Equivalently, $`L_u=\mathbb E[(1-y\widehat y)/2]`$ where
$`y,\widehat y\in\{-1,+1\}`$.
This is the error of a stochastic measured prediction, not the discontinuous
error obtained by thresholding an estimated expectation value.

For the phase task, set

```math
\overline A(U)
=\sum_x p_x
\langle U\bar z_x\vert Z_0\vert Uz_x\rangle.
```

Then $`L_X=1/2-\mathrm{Re}\overline A/2`$.
The bounds below concern derivatives of this population loss. In particular,
the density lower bound does not replace the square of an averaged
derivative by an average of squares.

## 4. Full-gradient separation

Define the constants

```math
\lambda_1=\cos^2(\pi/n),\qquad
c_n=\cos(2\pi/n),\qquad
\beta=\frac2\pi-\frac14,\qquad
m_*=\max\{\beta n-\pi,0\}.
```

The aligned first harmonic is

```math
f_j=\sin\!\left[\frac{2\pi}{n}
\left(j-a-\frac12\right)\right].
```

Each positive branch satisfies
$`\langle f,q^{(x)}\rangle\ge\beta n`$.
The wall overlap is $`2\csc(\pi/n)`$, and each of the $`k`$ changed logical
bits reduces it by at most four.

### Theorem 1: finite full-gradient bounds

For every $`D\ge1`$, the phase-label losses obey

```math
\mathbb E\mathcal G(L_X),\
\mathbb E\mathcal G(L_Y)
\le
M\min\left\{
1,\,
4\exp\!\left[-\frac{m_*^2c_n^{2D}}{8n}\right]
\right\}.
```

This upper bound holds even conditional on any fixed matching schedule,
with the expectation then taken over the Haar gates.

If $`D-1\ge\lceil n^2/\pi^2\rceil`$, the density-label loss satisfies

```math
\mathbb E\mathcal G(L_Z)
\ge
\frac{2(1-2p)^2}{3n^2}
\sin^2(\pi/n)\lambda_1^{2(D-1)}
\ge
\frac{8(1-2p)^2}{3n^4}
\lambda_1^{2(D-1)}.
```

The density expectation includes the random schedule. It uses the hopping
coordinate at the initial wall edge when that edge is present in layer 1,
an event of probability $`1/2`$.

For any fixed $`\alpha>1/\pi^2`$, taking
$`D=\lfloor\alpha n^2\rfloor`$ therefore gives, for sufficiently large $`n`$,

```math
\mathbb E\mathcal G(L_Z)=\Omega_\alpha(n^{-4}),\qquad
\mathbb E\mathcal G(L_X),\
\mathbb E\mathcal G(L_Y)\le e^{-\Omega_\alpha(n)}.
```

The finite constants are not asserted to be optimal.
Proofs: [phase upper bound](coherence_bound.md) and
[population density lower bound](density_transport.md).

### Theorem 2: exact logical-axis covariance

Let

```math
K_{ab}
=\mathbb E[\nabla L_a\cdot\nabla L_b],
\qquad a,b\in\{X,Y,Z\}.
```

Then

```math
K=\mathrm{diag}(\kappa_\perp,\kappa_\perp,\kappa_Z),
\qquad
\mathbb E\mathcal G(L_u)
=\kappa_Zu_z^2+
\kappa_\perp(u_x^2+u_y^2).
```

An onsite phase on the encoded control rail implements the same logical
$`Z`$ rotation independently of nuisance. Right absorption into the first
Haar layer preserves the ensemble and the fixed left-tangent convention.
This is the covariance symmetry used in the proof.
See [loss and geometry](loss_and_geometry.md).

### Theorem 3: efficient exact classification

The common encoder and inverse decoder use $`n`$ physical qubits, no
ancilla, $`O(n)`$ depth, and $`O(n^2)`$ nearest-neighbor conserving gates.
After $`E^\dagger`$, a constant-cost logical basis rotation turns any chosen
axis label into the physical $`Z_0`$ outcome. The classifier works for all
nuisance values without knowing which one was supplied.

If its prescribed decoder word has $`L=O(n)`$ matching layers, a random
$`D`$-layer skeleton contains that classifier except with probability

```math
\Pr\!\left[\mathrm{Bin}(D,\tfrac12)\lt L\right]
\le e^{-D/16},
\qquad D\ge4L.
```

The statement concerns an allowed assignment of all local gates.
It does not say that gradient descent finds this assignment.
See the [native construction and embedding proof](data_encoding.md).

## 5. Corollaries and their domains

**A wider profile family.** The phase upper extends to any complementary
half-filled branches with fixed positive harmonic overlap
$`\langle f,q^{(x)}\rangle\ge\beta_0n`$.
A sufficiently long diffusive prefix gives a common-sign population density
response for arbitrary mixtures of these profiles. Summing eligible layers
then restores the $`\Omega(n^{-4})`$ energy floor above the stated
$`\beta_0`$-dependent depth threshold.
The explicit fixed-weight source needs only the simpler first-layer proof.

**A logarithmic depth window.** Put $`r_D=D/2+\sqrt{nD}`$.
The exact binomial law for matching switches gives the stronger averaged
phase upper

```math
\mathbb E\mathcal G(L_X)
\le M\min\left\{
1,\,
4\exp\!\left[-\frac{m_*^2c_n^{2r_D}}{8n}\right]+e^{-2n}
\right\}.
```

The same holds for $`Y`$. For each fixed $`0<\epsilon<1`$, in the range

```math
\left\lceil\frac{n^2}{\pi^2}\right\rceil+1
\le D\le
\frac{(1-\epsilon)n^2\log n}{2\pi^2},
```

the density floor is $`\Omega(n^{-5+\epsilon})`$ and the phase upper is
$`\exp[-\Omega(n^\epsilon)]`$.
This is a domain of the estimates, not a sharp phase transition or a
post-window gradient-revival claim.

**High-probability phase blindness.** If $`B(n,D)`$ denotes any established
upper bound on $`\mathbb E\mathcal G(L_X)`$, Markov gives

```math
\Pr[\mathcal G(L_X)\ge t]\le
\min\{1,B(n,D)/t\},\qquad t>0.
```

At fixed diffusive depth, choosing an exponential threshold yields an
exponentially small failure probability. The density expectation lower
does not imply the analogous typical-initialization statement.

## 6. Scope of the conclusions

The measured error, native local tangent convention, fixed charge, specified
random circuit law, and macroscopic branch contrast are part of the theorem.
The comparison keeps the average density operator fixed while changing its
labeled decomposition.

The known decoder establishes expressivity and explicit preparation costs.
It also makes clear that this structured data source carries no computational
hardness claim. Nuisance variation does not make an extensive phase label
robust to finite local dephasing. The gradient theorem concerns random
initialization and does not impose a lower bound on every optimizer or
learning protocol.

Other losses can have calibration gradients even when the useful phase
response is small. These distinctions, together with the interpretation of
the full-gradient normalization, are developed in
[loss and geometry](loss_and_geometry.md) and
[physical interpretation](interpretation.md).
