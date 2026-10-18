# Operational loss and task-gradient geometry

The classifier, initialized gate distribution, and native left-tangent basis are fixed in [the circuit model](model.md). The states and nuisance source are defined in [data encoding](data_encoding.md). This document identifies the supervised loss controlled by the gradient bounds and states the resulting geometry and measurement resources.

## 1. Expected error of the physical prediction

For a fixed logical axis $`u`$, draw the label $`y\in\{+1,-1\}`$ uniformly and the nuisance value $`x`$ from its specified distribution. Apply the fixed initialized classifier $`U`$ to the corresponding input and measure physical $`Z_0`$. The observed sign $`r\in\{+1,-1\}`$ is the prediction.

The one-shot error is

```math
\ell(y,r)=\mathbf 1\{r\ne y\}=\frac{1-yr}{2}.
```

Its population expectation is

```math
L_u(U)
=\frac12-\frac14\operatorname{Tr}\!\left[
 Z_0U(\rho_{u,+}-\rho_{u,-})U^\dagger\right].
```

The initialized circuit is held fixed across data draws and repeated shots. Random initialization is an outer ensemble used by the theorem.

This loss is the expected error of the sampled measurement outcome. A rule that thresholds an estimated expectation value, or takes a majority vote over several predictions, defines a different classifier and requires a separate loss analysis.

## 2. Effective logical observable

Restrict $`E^\dagger U^\dagger Z_0UE`$ to the dual-rail logical subspace and average its nuisance blocks:

```math
O_{\mathrm{eff}}(U)
=\sum_xp_x\langle x|E^\dagger U^\dagger Z_0UE|x\rangle
=a_0I+a_xX+a_yY+a_zZ.
```

This is a Hermitian control-qubit observable with norm at most one. Its coefficients are real and obey $`|a_0|+|a|\le1`$. The two class expectations are

```math
f_{u,\pm}=a_0\pm u\cdot a,
```

so the exact supervised loss reduces to

```math
L_u=\frac12-\frac12u\cdot a.
```

The unlabeled readout bias $`a_0`$ cancels because the priors are balanced. The label axis remains in the margin $`u\cdot a`$ even though every task has the same unlabeled density operator.

For the transverse axes, use the fixed orientation

```math
A_x(U)=\langle U\bar z_x|Z_0|Uz_x\rangle,
\qquad
\bar A(U)=\sum_xp_xA_x(U)=a_x+i a_y.
```

Then

```math
L_X=\frac12-\frac12\operatorname{Re}\bar A,
\qquad
L_Y=\frac12-\frac12\operatorname{Im}\bar A.
```

These are population-loss identities. In particular, the density gradient must be obtained from the signed population contrast before squaring; an average of per-example gradient variances does not provide a lower bound for it.

## 3. Mean-squared error is a different functional

Let $`f_{u,y,x}`$ denote the expected physical readout for one pure training example. Consider the common half-squared-error objective on these prediction means,

```math
J_{\mathrm{MSE},u}
=\frac12\mathbb E_{y,x}\left[(f_{u,y,x}-y)^2\right].
```

Expanding the square gives

```math
J_{\mathrm{MSE},u}
=2L_u-\frac12+\frac12\mathbb E_{y,x}[f_{u,y,x}^2],
```

and hence

```math
\nabla J_{\mathrm{MSE},u}
=2\nabla L_u+
  \mathbb E_{y,x}[f_{u,y,x}\nabla f_{u,y,x}].
```

The extra term is not bounded by the transverse population-margin theorem. For example, write the per-nuisance effective observable as $`b_{0,x}I+b_{X,x}X+b_{Y,x}Y+b_{Z,x}Z`$. For the $`X`$ task,

```math
J_{\mathrm{MSE},X}
=\frac12\mathbb E_x\left[b_{0,x}^2+(b_{X,x}-1)^2\right].
```

Gradients of the unlabeled bias $`b_{0,x}`$ can contribute independently of the small phase margin. A squared loss formed from the class-averaged means also has an additional squared-prediction term, although it uses a different average.

There is a separate elementary identity for the measured outcome itself:

```math
\frac{(r-y)^2}{4}=\ell(y,r),
\qquad r,y\in\{-1,+1\}.
```

Thus the normalized squared error of a sampled binary outcome equals the operational error exactly. Squaring its expectation instead produces the different objective above. Other nonlinear losses likewise require their own gradient analysis.

## 4. Native tangent coordinates and their normalization

For each actual gate $`G`$ and each generator $`H`$ in the fixed six-element basis, define the coordinate derivative by

```math
G(\theta)=e^{-i\theta H}G,
\qquad
\partial_{G,H}L_u
=\left.\frac{d}{d\theta}L_u(U_{G,H}(\theta))\right|_{\theta=0}.
```

Every coordinate is evaluated at the same initialized circuit. There are $`M=3nD`$ coordinates when the zero identity derivative is retained. The native gradient energy is

```math
\|\nabla_{\mathrm{nat}}L_u\|^2
=\sum_{G,H}(\partial_{G,H}L_u)^2.
```

The basis is

```math
\left\{I,Z_i,Z_j,Z_iZ_j,
\frac{X_iX_j+Y_iY_j}{2},
\frac{X_iY_j-Y_iX_j}{2}\right\}.
```

Its generators have operator norm one, but their two-qubit Hilbert-Schmidt norms differ: the four diagonal generators have norm two, and the two hopping generators have norm $`\sqrt2`$. They are mutually Hilbert-Schmidt orthogonal. For the product metric obtained by normalizing each local basis to be Hilbert-Schmidt orthonormal, every loss satisfies

```math
\frac14\|\nabla_{\mathrm{nat}}L_u\|^2
\le\|\nabla_{\mathrm{HS}}L_u\|^2
\le\frac12\|\nabla_{\mathrm{nat}}L_u\|^2.
```

The polynomial-versus-exponential scaling therefore survives that fixed normalization change. No invariance under arbitrary size-dependent parameter rescaling or an arbitrary optimizer metric is asserted.

Each coordinate obeys $`|\partial_{G,H}L_u|\le1`$. Indeed, the differentiated observable has norm at most $`2\|H\|\|Z_0\|=2`$, while $`\|\rho_{u,+}-\rho_{u,-}\|_1\le2`$ and the loss carries a factor $`1/4`$. In particular, the full energy is at most $`M`$.

## 5. Mean-zero derivatives and exact axial covariance

For every fixed $`\theta`$, the product $`e^{-i\theta H}G`$ is Haar distributed whenever $`G`$ is Haar. The averaged loss is therefore independent of $`\theta`$, giving

```math
\mathbb E[\partial_{G,H}L_u]=0.
```

This also holds conditional on a fixed matching schedule. The derivative bounds justify differentiating the finite-dimensional ensemble average. Consequently the coordinate second moments in the theorem are coordinate variances.

Define the three-axis population-gradient covariance

```math
K_{ab}
=\mathbb E\left[
 \nabla_{\mathrm{nat}}L_a\cdot\nabla_{\mathrm{nat}}L_b\right],
\qquad a,b\in\{X,Y,Z\}.
```

It is a real symmetric positive-semidefinite matrix. The linear loss identity implies

```math
\nabla L_u=u_x\nabla L_X+u_y\nabla L_Y+u_z\nabla L_Z,
\qquad
\mathbb E\|\nabla L_u\|^2=u^TKu.
```

To establish the exact axial symmetry, use the physical image $`j_c=\pi(0)`$ of the first rail's left site. Its occupation on the encoded computational branches is the control bit $`b`$, independently of nuisance. Thus the input phase

```math
D_{j_c}(\phi)=e^{i\phi N_{j_c}},
\qquad N_j=(I-Z_j)/2,
```

acts on the encoded data subspace as

```math
D_{j_c}(\phi)E
=e^{i\phi/2}E
 \left[e^{-i\phi Z_{\mathrm{control}}/2}\otimes I_{\mathrm{nuisance}}\right].
```

Absorb this physical phase into the right side of the first-layer Haar gate containing $`j_c`$. Right multiplication preserves the circuit distribution. It also preserves the fixed left-tangent convention: at that gate the perturbed product is $`e^{-i\theta H}GD_{j_c}(\phi)`$, with the same $`H`$. For every coordinate, the resulting differentiated circuit is the original differentiated circuit followed by the same input phase.

All loss gradients therefore rotate together under arbitrary logical rotations in the $`XY`$ plane. It follows that

```math
K=\begin{pmatrix}
\kappa_\perp&0&0\\
0&\kappa_\perp&0\\
0&0&\kappa_Z
\end{pmatrix},
```

and

```math
\mathbb E\|\nabla_{\mathrm{nat}}L_u\|^2
=\kappa_\perp(u_x^2+u_y^2)+\kappa_Zu_z^2.
```

This matrix compares three population-loss gradient vectors at initialization. A per-example neural tangent kernel, Hessian, Fisher matrix, and optimizer condition number are different objects. No training-time evolution of this matrix is established here.

## 6. High-probability consequence for transverse gradients

For the explicit fixed-weight source, define

```math
c_n=\cos(2\pi/n),
\qquad
m_*=[\beta n-\pi]_+,
\qquad
\varepsilon_{n,D}
=\min\left\{1,4\exp\!\left[-\frac{m_*^2c_n^{2D}}{8n}\right]\right\},
\qquad
B_{n,D}=M\varepsilon_{n,D}.
```

The coherence theorem gives

```math
\mathbb E\|\nabla L_X\|^2\le B_{n,D},
\qquad
\mathbb E\|\nabla L_Y\|^2\le B_{n,D}.
```

Markov's inequality yields, for every $`\delta\in(0,1)`$,

```math
\Pr\!\left(\|\nabla L_X\|>\sqrt{B_{n,D}/\delta}\right)
\le\delta.
```

There is also a simultaneous statement for every transverse logical axis. Since

```math
\sup_{u_z=0,\,\|u\|=1}\|\nabla L_u\|^2
\le\|\nabla L_X\|^2+\|\nabla L_Y\|^2,
```

one has

```math
\Pr\!\left(
\sup_{u_z=0,\,\|u\|=1}\|\nabla L_u\|
>\sqrt{2B_{n,D}/\delta}\right)\le\delta.
```

Every native component is bounded by its full gradient norm on the same event. This conclusion requires no independence among coordinates or task axes.

At $`D=\lfloor\alpha n^2\rfloor`$ for fixed $`\alpha>0`$, the bound has $`B_{n,D}\le e^{-\gamma n}`$ for some constant $`\gamma>0`$ and all sufficiently large $`n`$. Taking $`\delta=e^{-\gamma n/2}`$ gives a full transverse gradient of order $`e^{-\gamma n/4}`$ outside an event of probability $`e^{-\gamma n/2}`$, with a constant factor for the simultaneous-axis version.

The same amplitude argument controls the initialized classification advantage:

```math
\sup_{u_z=0,\,\|u\|=1}|L_u-1/2|^2
=\frac{|\bar A|^2}{4},
\qquad
\mathbb E|\bar A|^2\le\varepsilon_{n,D}.
```

Therefore the transverse classifier is close to error $`1/2`$ at most random initializations, in addition to having a small local gradient. These are initialization statements; they impose no restriction on a parameter assignment chosen by the exact decoder construction.

## 7. What the density moment does and does not establish

For $`s=D-1\ge\lceil n^2/\pi^2\rceil`$, the first-layer wall coordinate gives

```math
\mathbb E\|\nabla L_Z\|^2
\ge b_{n,D}
:=\frac83(1-2p)^2n^{-4}\lambda_1^{2(D-1)},
\qquad
\lambda_1=\cos^2(\pi/n).
```

At fixed diffusive depth above the stated threshold, $`b_{n,D}=\Omega(n^{-4})`$. The bound is for the actual population loss and follows from the nonzero signed mean profile of the fixed-weight source.

A positive ensemble moment alone permits a small set of initializations to supply the moment. For the specific first-layer wall hopping derivative, define $`g_*=0`$ when the sampled first matching omits that edge. Then $`|g_*|\le1`$ and $`\mathbb E g_*^2\ge b_{n,D}`$. The elementary bounded-variable estimate gives

```math
\Pr\!\left(|g_*|\ge\sqrt{b_{n,D}/2}\right)
\ge\frac{b_{n,D}}{2-b_{n,D}}.
```

This supplies an inverse-polynomial lower bound on a fraction of initialized slopes in the diffusive regime. It does not give constant-probability trainability, a useful slope for every coordinate, alignment with a path to the decoder, or a convergence rate.

Together with the coherence result, the established comparison is an exponential anisotropy of population-gradient energy and a high-probability transverse suppression. The longitudinal side remains an ensemble-moment lower bound.

## 8. Parameter-shift identity for the actual coordinates

The spectra of all native generators lie in $`\{-1,0,1\}`$. Holding all other gates fixed, either the output expectation or the operational loss has a Fourier expansion

```math
F(\theta)=\sum_{r=-2}^{2}F_re^{ir\theta}.
```

For this full frequency set, the exact derivative rule is

```math
F'(\theta)
=F(\theta+\pi/4)-F(\theta-\pi/4)
+\frac{1-\sqrt2}{2}
 \left[F(\theta+\pi/2)-F(\theta-\pi/2)\right].
```

For frequencies $`r=1,2`$, the coefficients solve

```math
2\sin(r\pi/4)+(1-\sqrt2)\sin(r\pi/2)=r,
```

which proves the identity mode by mode. A hopping generator can produce both frequencies, so its generic response requires this four-setting rule. For the diagonal generators with spectrum $`\{-1,+1\}`$, only frequencies $`0,\pm2`$ occur and the first difference alone is sufficient. The identity direction requires no measurements.

Every shifted circuit uses the same initialized gates and data source, with only the selected gate changed to $`e^{-i\theta H}G`$. The product remains an allowed charge-conserving two-qubit gate and can be implemented as one native block; executing the perturbation separately instead adds one local block per shot.

## 9. A bounded-shot estimator and its resource scope

For the generic four-setting rule, let its signed weights be

```math
(w_1,w_2,w_3,w_4)=(1,-1,c,-c),
\qquad
c=\frac{1-\sqrt2}{2},
\qquad
S=\sum_{j=1}^4|w_j|=1+\sqrt2.
```

The shifts are $`(\pi/4,-\pi/4,\pi/2,-\pi/2)`$. An unbiased estimator of one population-loss derivative can be obtained directly from labeled shots:

1. Sample setting $`j`$ with probability $`|w_j|/S`$.
2. Independently draw a label and nuisance value from the training source, prepare the example, and run the shifted circuit.
3. Measure $`r\in\{-1,+1\}`$ and return

```math
X=-\frac S2\operatorname{sgn}(w_j)yr.
```

Since $`\sum_jw_j=0`$,

```math
\mathbb E X
=\sum_jw_jL_u(\theta+s_j)
=\partial_{G,H}L_u.
```

The variable $`X`$ lies in $`[-S/2,S/2]`$. For the empirical mean of $`N_{\mathrm{shot}}`$ independent draws, Hoeffding's inequality gives

```math
\Pr\!\left(|\widehat{\partial L_u}-\partial L_u|>\eta\right)
\le2\exp\!\left[-\frac{2N_{\mathrm{shot}}\eta^2}{S^2}\right].
```

Thus a sufficient shot count is

```math
N_{\mathrm{shot}}
\ge\left\lceil\frac{S^2}{2\eta^2}\log\frac2\delta\right\rceil.
```

This estimates the population derivative without enumerating its exponentially many nuisance values. The only state source required is the efficient sampler and encoder already specified.

To estimate all $`M`$ components to componentwise error at most $`\eta`$ with joint confidence $`1-\delta`$, separate coordinate estimates give the sufficient total budget

```math
N_{\mathrm{all}}
=O\!\left(M\eta^{-2}\log\frac{M}{\delta}\right).
```

For a full-vector Euclidean error guarantee $`\epsilon`$, taking $`\eta=\epsilon/\sqrt M`$ instead gives

```math
N_{\mathrm{all}}
=O\!\left(M^2\epsilon^{-2}\log\frac{M}{\delta}\right).
```

Each shot uses $`n`$ physical qubits, one local readout, and $`nD/2+O(n^2)`$ native two-qubit gates including preparation. At $`D=\Theta(n^2)`$ this is $`\Theta(n^3)`$ gates per shot. Multiplying that cost by the stated shot budget gives the total native gate cost of this coordinatewise measurement procedure.

These are sufficient budgets for a specified independent-shot estimator, not optimality claims. Inverse-polynomial additive precision has polynomial resource cost. Requesting exponentially fine precision makes these displayed budgets exponential; the gradient upper bound alone is not a minimax sampling lower bound and does not exclude collective measurements, a different accessible observable, prior knowledge of the encoder, or a different learning strategy. In particular, the known exact decoder remains available as an efficient structured classifier.
