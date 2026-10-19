# Coherence-label gradient bound

At a fixed diffusive depth, the full native gradient for the logical X and Y classification tasks is exponentially small in the number of qubits. A surviving charge statistic distinguishes the two branches of each coherent input, which bounds the interference accessible to the readout and every gate derivative.

The circuit, data source, population loss, and native coordinate convention are defined in [the common model](model.md). The complementary lower bound is proved in [density transport](density_transport.md).

## 1. Statement

Let $`n\in4\mathbb N`$, $`n\ge8`$, and $`D\ge1`$. Each layer chooses the even or odd nearest-neighbor perfect matching with equal probability and applies independent Haar gates from the full two-qubit charge-preserving group. All $`nD/2`$ gates are trainable, with six left-tangent directions

```math
\left\{I,\ Z_i,\ Z_j,\ Z_iZ_j,\ H_x,\ H_y\right\},
\qquad
H_x=\frac{X_iX_j+Y_iY_j}{2},
\qquad
H_y=\frac{X_iY_j-Y_iX_j}{2}.
```

Every generator has norm one and spectrum contained in $`\{-1,0,1\}`$. The zero identity derivative is retained in the count $`M=3nD`$. Write

```math
\mathcal G_u(U)=\sum_{e,H}\left(\partial_{e,H}L_u(U)\right)^2.
```

Each derivative varies an actual gate as $`G_e\mapsto e^{-i\theta H}G_e`$ at $`\theta=0`$.

Set $`a=n/4`$ and define

```math
f_j=\sin\left[\frac{2\pi}{n}\left(j-a-\frac12\right)\right],
\qquad
c_n=\cos(2\pi/n)>0.
```

For nuisance value $`x`$, let the positive branch be a half-filled basis state with magnetization profile $`q^{(x)}`$ and the negative branch its bitwise complement. Assume

```math
\langle f,q^{(x)}\rangle\ge\beta n
\quad\text{for every }x,
\qquad
\beta>0,
\qquad
m_*=\max\{\beta n-\pi,0\}.
```

The nuisance distribution is fixed independently of the circuit. The fixed-weight source in [the model](model.md) satisfies this condition with $`\beta=2/\pi-1/4`$.

To verify that value, the perfect wall has
$`\langle f,q^{\mathrm{wall}}\rangle=m_0=2\csc(\pi/n)\ge2n/\pi`$.
Each nonzero logical output bit flips two physical magnetizations relative to the wall and decreases this overlap by at most four. The source has exactly
$`k_{\mathrm{nuis}}=\lfloor(n/2)/8\rfloor\le n/16`$
such bits. Thus every nuisance branch satisfies

```math
\langle f,q^{(x)}\rangle
\ge m_0-4k_{\mathrm{nuis}}
\ge\left(\frac2\pi-\frac14\right)n.
```

**Theorem 1.** For $`u=X,Y`$,

```math
\mathbb E\,\mathcal G_u
\le M\min\left\{
1,\,
4\exp\left[-\frac{m_*^2c_n^{2D}}{8n}\right]
\right\}.
\qquad\text{(1)}
```

This also holds conditional on every fixed matching schedule, averaging only over the Haar gates. For fixed $`\alpha,\beta>0`$ and $`D=\lfloor\alpha n^2\rfloor`$,

```math
\mathbb E\,\mathcal G_X,\quad
\mathbb E\,\mathcal G_Y
\le \exp[-\Omega_{\alpha,\beta}(n)].
\qquad\text{(2)}
```

For the random matching ensemble, set $`r_D=D/2+\sqrt{nD}`$. A sharper finite-size bound is

```math
\mathbb E\,\mathcal G_u
\le M\min\left\{
1,\,
4\exp\left[-\frac{m_*^2c_n^{2r_D}}{8n}\right]+e^{-2n}
\right\},
\qquad u=X,Y.
\qquad\text{(3)}
```

When $`m_*=0`$, these formulas assert only $`\mathbb E\mathcal G_u\le M`$. For the concentration argument below, therefore assume $`\beta n>\pi`$.

## 2. Haar-averaged populations are a conditional exclusion process

Fix the nuisance value $`x`$ and complete matching schedule $`\sigma=(\sigma_1,\ldots,\sigma_D)`$. Average only the Haar gates.

The zero- and two-particle sectors of a two-qubit gate are one-dimensional. Haar averaging in the one-particle sector sends either basis population to the uniform mixture of $`01`$ and $`10`$. On a diagonal density matrix this is precisely a classical swap of the two occupation bits with probability $`1/2`$. Equal bits are unchanged.

Independence of the gates makes these swaps independent across the edges of a matching. The averaged density matrix stays diagonal after each layer. Its final populations are therefore the parallel symmetric exclusion process for the fixed schedule.

A deterministic occupation configuration is strongly Rayleigh: its generating polynomial is a monomial. Partial symmetrization by a transposition preserves the strongly Rayleigh property, and strongly Rayleigh measures are negatively associated. These are [Theorems 4.20 and 4.9 of Borcea, Brändén, and Liggett](https://arxiv.org/html/0707.2340v2). Every swap/no-swap operation above is such a partial symmetrization, so the conditional final population measure is negatively associated.

Neither the schedule mixture nor the nuisance mixture is assumed strongly Rayleigh. Concentration is established before removing either conditioning.

## 3. An exact identity for matching projections

Let $`P_A,P_B`$ be the real symmetric projections that average the two coordinates on each edge of the respective matching. The conditional mean magnetization is

```math
P_{\sigma_D}\cdots P_{\sigma_1}q^{(x)}.
```

Put $`k=2\pi/n`$, $`\chi=\cos(k/2)`$, and

```math
h_A=P_Af/\chi,\qquad h_B=P_Bf/\chi.
```

Averaging a sine over a matched pair gives its value at the pair midpoint multiplied by $`\chi`$. Averaging this result over the other matching gives

```math
P_Ah_A=h_A,\qquad P_Bh_B=h_B,
\qquad
P_Ah_B=c_nh_A,\qquad P_Bh_A=c_nh_B.
\qquad\text{(4)}
```

For example, the B-pair midpoints adjoining an A pair of midpoint $`j+1/2`$ are $`j-1/2`$ and $`j+3/2`$. Their sine average is $`\cos(k)`$ times the sine at $`j+1/2`$, proving the cross relation.

Let $`s(\sigma)`$ count changes between consecutive matchings. Pulling the projections backward through the inner product proves, for any real profile $`q`$,

```math
\langle f,P_{\sigma_D}\cdots P_{\sigma_1}q\rangle
=c_n^{s(\sigma)}
\langle P_{\sigma_1}f,q\rangle,
\qquad D\ge1.
\qquad\text{(5)}
```

On one matched edge the contribution to $`\|P_Af-f\|_1`$ is the absolute difference of its two original sine values, at most $`2\sin(\pi/n)`$. Thus

```math
\|P_Af-f\|_1\le n\sin(\pi/n)\le\pi,
\qquad
\|P_Bf-f\|_1\le\pi.
\qquad\text{(6)}
```

Since $`\|q^{(x)}\|_\infty=1`$, the conditional mean of the signed charge statistic satisfies

```math
\mu_{\sigma,x}
:=\mathbb E_{\sigma,x}\sum_jf_jZ_j
\ge(\beta n-\pi)c_n^{s(\sigma)}
\ge(\beta n-\pi)c_n^D.
\qquad\text{(7)}
```

Complementing an input complements every configuration of the swap process. The complementary branch therefore has mean exactly $`-\mu_{\sigma,x}`$.

## 4. Weighted concentration with explicit constants

Let $`N_j=(1-Z_j)/2`$ be the final classical occupation variables. Define

```math
w_j=\frac{1+f_j}{2},
\qquad
T=\sum_jw_jN_j.
```

The weights lie in $`[0,1]`$. Fixed half filling and $`\sum_jf_j=0`$ give the pointwise identity

```math
T=\frac n4-\frac14\sum_jf_jZ_j.
\qquad\text{(8)}
```

The two branch means of $`T`$ are consequently $`n/4\mp\mu_{\sigma,x}/4`$.

Negative association implies, for every real $`t`$,

```math
\mathbb E e^{t(T-\mathbb ET)}
\le
\prod_j
\mathbb E e^{t w_j(N_j-\mathbb EN_j)}.
\qquad\text{(9)}
```

For positive $`t`$, the factors are nonnegative increasing functions on disjoint coordinates. For negative $`t`$, they are nonnegative decreasing functions. The two-function inequality also holds for decreasing functions by changing both signs, and induction applies because their products stay nonnegative and decreasing.

For one Bernoulli variable put

```math
K_j(t)=\log\mathbb E e^{t w_j(N_j-\mathbb EN_j)}.
```

Under exponential tilting,
$`K_j''(t)=w_j^2p_t(1-p_t)\le w_j^2/4`$.
Together with $`K_j(0)=K_j'(0)=0`$, this gives
$`K_j(t)\le t^2w_j^2/8`$.
Combining with (9) and optimizing the exponential Markov bound proves both one-sided inequalities

```math
\Pr(T-\mathbb ET\ge v),\quad
\Pr(T-\mathbb ET\le-v)
\le
\exp\left[-\frac{2v^2}{\sum_jw_j^2}\right]
\le e^{-2v^2/n},
\qquad v\ge0.
\qquad\text{(10)}
```

The threshold $`T=n/4`$ distinguishes the branches with each conditional error at most

```math
\delta_{\sigma,x}
=\exp\left[-\frac{\mu_{\sigma,x}^2}{8n}\right].
\qquad\text{(11)}
```

The exact sum $`\sum_jw_j^2=3n/8`$ improves the denominator in (11) to $`3n`$. The theorem retains the conservative $`8n`$.

## 5. A projector inequality bounds squared interference

For one quantum circuit realization write

```math
|\alpha_x\rangle=U|z_x\rangle,\qquad
|\gamma_x\rangle=U|\bar z_x\rangle,\qquad
A_x(U)=\langle\gamma_x|Z_0|\alpha_x\rangle.
```

Let $`\Pi_T`$ be the computational-basis projector onto $`T\le n/4`$. It commutes with $`Z_0`$. Define

```math
e_{+,x}=\langle\alpha_x|(I-\Pi_T)|\alpha_x\rangle,
\qquad
e_{-,x}=\langle\gamma_x|\Pi_T|\gamma_x\rangle.
```

Splitting the matrix element into the two projector sectors and using Cauchy–Schwarz gives

```math
\begin{aligned}
|A_x|
&\le
\sqrt{(1-e_{+,x})e_{-,x}}
+\sqrt{e_{+,x}(1-e_{-,x})}\\
&\le\sqrt{e_{+,x}}+\sqrt{e_{-,x}},\\
|A_x|^2&\le2(e_{+,x}+e_{-,x}).
\end{aligned}
\qquad\text{(12)}
```

The Haar averages of these errors are exactly the two classical population errors in (11). Hence

```math
\mathbb E_G[|A_x(U)|^2\mid\sigma,x]
\le4\delta_{\sigma,x}.
\qquad\text{(13)}
```

This bounds the second moment of an actual off-diagonal quantum matrix element; a zero mean has not been substituted for a small second moment.

Let $`\omega_x`$ be the nuisance probabilities and
$`\overline A=\sum_x\omega_x A_x`$.
Convexity gives
$`|\overline A|^2\le\sum_x\omega_x|A_x|^2`$.
Using the uniform mean gap and $`|\overline A|\le1`$ therefore yields

```math
\mathbb E_G[|\overline A(U)|^2\mid\sigma]
\le
\min\left\{
1,\,
4\exp\left[-\frac{m_*^2c_n^{2s(\sigma)}}{8n}\right]
\right\}.
\qquad\text{(14)}
```

The inequality is applied to the population amplitude in the upper-bound direction. No property of the nuisance-averaged classical measure is required.

## 6. Parseval and Haar invariance control every native derivative

For the phase conventions in [the model](model.md), the binary classification losses are exactly

```math
L_X=\frac12-\frac12\mathrm{Re}\overline A,
\qquad
L_Y=\frac12-\frac12\mathrm{Im}\overline A.
\qquad\text{(15)}
```

Fix all base gates and vary one as $`e^{-i\theta H}G_e`$. The angle enters through a single conjugation. The generator's eigenvalue differences belong to $`\{-2,-1,0,1,2\}`$, so

```math
\overline A(\theta)=\sum_{r=-2}^{2}a_r e^{ir\theta}.
```

Parseval gives

```math
\frac1{2\pi}\int_0^{2\pi}|\overline A'(\theta)|^2\,d\theta
=\sum_{r=-2}^{2}r^2|a_r|^2
\le4\sum_{r=-2}^{2}|a_r|^2
=\frac4{2\pi}\int_0^{2\pi}|\overline A(\theta)|^2\,d\theta.
\qquad\text{(16)}
```

The factor $`1/2`$ in (15) consequently gives, for $`u=X,Y`$,

```math
\frac1{2\pi}\int_0^{2\pi}
\left(\frac{dL_u(\theta)}{d\theta}\right)^2\,d\theta
\le
\frac1{2\pi}\int_0^{2\pi}|\overline A(\theta)|^2\,d\theta.
\qquad\text{(17)}
```

Now average over the selected Haar gate. For any fixed angle,
$`e^{-i\theta H}G_e`$ is again Haar and independent of the other gates. Its derivative in the same left direction is the derivative in (17). Both angle-averaged sides therefore transfer to the original circuit at $`\theta=0`$:

```math
\mathbb E_G[(\partial_{e,H}L_u)^2\mid\sigma]
\le
\mathbb E_G[|\overline A(U)|^2\mid\sigma].
\qquad\text{(18)}
```

The auxiliary angle belongs only to the proof. The circuit has no additional gate or specially randomized angle.

Summing (18) over the $`M`$ coordinates proves

```math
\mathbb E_G[\mathcal G_u\mid\sigma]
\le M\min\left\{
1,\,
4\exp\left[-\frac{m_*^2c_n^{2s(\sigma)}}{8n}\right]
\right\}.
\qquad\text{(19)}
```

No independence between gradient coordinates is used. Since $`s(\sigma)\le D`$, this proves (1). Haar invariance also makes the mean of each derivative zero: the Haar-averaged loss is constant under that left multiplication. The energy is therefore a sum of coordinate variances.

For fixed $`D=\lfloor\alpha n^2\rfloor`$,

```math
m_*=\beta n+O(1),
\qquad
c_n^D=\exp[-2\pi^2\alpha+o(1)].
```

The exponent in (1) is a positive constant times $`n`$. Absorbing $`M=O(n^3)`$ proves (2).

## 7. Matching statistics and the logarithmic window

### Exact perfect-wall identity

For $`q^{\mathrm{wall}}=\mathrm{sign}(f)`$,

```math
\langle f,q^{\mathrm{wall}}\rangle=m_0=2\csc(\pi/n).
```

For completeness, the positive half of the sine profile sums to
$`\csc(\pi/n)`$: multiply its terms by $`2\sin(\pi/n)`$
and use
$`2\sin(\pi/n)\sin[(2j-1)\pi/n]=\cos[2(j-1)\pi/n]-\cos(2j\pi/n)`$.
The sum telescopes from $`\cos 0`$ to $`\cos\pi`$. The negative half contributes the same absolute sum.

The two interfaces are separated by the even number $`n/2`$. One matching, $`Q_0`$, avoids both and fixes the wall. Consequently

```math
\langle P_{Q_0}f,q^{\mathrm{wall}}\rangle=m_0,
\qquad
\langle P_{\ne Q_0}f,q^{\mathrm{wall}}\rangle=c_nm_0.
```

The second equality follows from (4) and $`P_{Q_0}q^{\mathrm{wall}}=q^{\mathrm{wall}}`$. The exact mean is

```math
\mu_\sigma=m_0c_n^{\nu(\sigma)},
\qquad
\nu(\sigma)=\mathbf1_{\{\sigma_1\ne Q_0\}}+s(\sigma).
\qquad\text{(20)}
```

For general profiles, $`s(\sigma)\le\nu(\sigma)`$, so $`m_*c_n^{\nu(\sigma)}`$ remains a valid lower bound without asserting equality.

### Exact binomial law

Encode the independent fair matching choices by bits $`B_1,\ldots,B_D`$, with zero denoting $`Q_0`$. The map

```math
(B_1,\ldots,B_D)
\longmapsto
(B_1,\ B_2\mathbin{\oplus}B_1,\ \ldots,\ B_D\mathbin{\oplus}B_{D-1})
```

is a bijection of the Boolean cube. Its output bits are independent and fair, and their sum is $`\nu`$. Thus

```math
\nu\sim\mathrm{Binomial}(D,1/2),
\qquad
\Pr\left(\nu>D/2+\sqrt{nD}\right)\le e^{-2n}.
\qquad\text{(21)}
```

The tail follows from the scalar moment-generating-function argument applied to independent bits. On the good event use the mean $`m_*c_n^{r_D}`$. On the exceptional event use $`|\overline A|^2\le1`$. Combining with (18) proves (3). If $`r_D>D`$, the bad event is empty and the larger real exponent remains valid.

An exact binomial average with $`\nu`$ gives another finite-size bound. For the perfect wall, replace $`m_*`$ throughout this refinement by $`m_0`$.

### Logarithmic-depth corollary

Fix $`\epsilon\in(0,1)`$ and suppose

```math
1\le D\le\frac{(1-\epsilon)n^2\log n}{2\pi^2}.
\qquad\text{(22)}
```

Using

```math
\log c_n=-2\pi^2/n^2+O(n^{-4}),
\qquad
\frac{\sqrt{nD}}{n^2}
=O\left(\sqrt{\frac{\log n}{n}}\right)
```

gives the uniform lower estimate

```math
m_*c_n^{r_D}
=\Omega_{\beta,\epsilon}\left(n^{(1+\epsilon)/2}\right).
```

The exponent in (3) is at least a positive constant times $`n^\epsilon`$. Its polynomial coordinate count and exceptional-event term can be absorbed, so

```math
\mathbb E\mathcal G_X,\quad\mathbb E\mathcal G_Y
\le\exp[-\Omega_{\beta,\epsilon}(n^\epsilon)].
\qquad\text{(23)}
```

The [density logarithmic-depth corollary](density_transport.md#7-logarithmic-depth-corollaries) supplies the simultaneous polynomial lower bound when its suffix condition holds.

## 8. Scope

The result concerns the specified population misclassification loss at Haar initialization and the specified native coordinate metric. It does not establish the same bound for every loss, every reparameterization, or a subsequent adaptive training trajectory.

Markov's inequality gives $`\Pr(\mathcal G_u\ge h)\le\mathbb E\mathcal G_u/h`$ for $`h>0`$. The coherence result therefore also controls typical full gradients, with adjusted thresholds and exponents. The density lower has a different logical strength: its ensemble second moment does not by itself establish typical successful training.

The finite concentration constants can be small at large fixed $`\alpha`$. This asymptotic theorem does not claim sharp small-system estimates. The logarithmic window is a sufficient range for the proof, not a demonstrated sharp transition. An uninformative bound at greater depth proves neither gradient revival nor a cutoff.

## Primary source used in the proof

Julius Borcea, Petter Brändén, and Thomas M. Liggett, **Negative dependence and the geometry of polynomials**, *Journal of the American Mathematical Society* **22**, 521–567 (2009), [arXiv:0707.2340v2](https://arxiv.org/html/0707.2340v2). Theorem 4.20 supplies preservation under partial symmetrization; Theorem 4.9 supplies negative association. The proof above specifies their application to the conditional circuit populations.

