# Density transport and a population-gradient lower bound

The conserved one-body sector provides a polynomial lower bound on the native gradient energy of the density-label population loss. For the fixed-weight nuisance source, one first-layer hopping direction is enough. For a broader class of profiles, a diffusive prefix selects a uniformly signed Fourier component, and contributions from many layers can be summed.

Definitions of the all-Haar circuit, fixed data encoder, six native generators, and loss are in [the common model](model.md). The complementary [coherence bound](coherence_bound.md) applies to every native direction in the same circuit.

## 1. Main density bound

Let $`n\in4\mathbb N`$, $`n\ge8`$, and $`a=n/4`$. Define

```math
\lambda_k=\cos^2(\pi k/n),\qquad
\lambda=\lambda_1,\qquad
S=\left\lceil\frac{n^2}{\pi^2}\right\rceil.
```

For the fixed-weight nuisance source, put

```math
m=n/2,\qquad
k_{\mathrm{nuis}}=\lfloor m/8\rfloor,\qquad
p=\frac{k_{\mathrm{nuis}}}{m-1},\qquad
\eta=1-2p.
```

Here $`p`$ is the marginal probability that any noncontrol logical output bit is one. It is not the class prior, which is $`1/2`$. Since $`m\ge4`$, the conservative bound $`p\le1/6`$ implies $`\eta\ge2/3`$.

**Theorem 1.** If $`D-1\ge S`$, the actual population loss satisfies

```math
\mathbb E\,\mathcal G_Z
\ge
\frac{2\eta^2}{3n^2}\sin^2(\pi/n)\lambda^{2(D-1)}
\ge
\frac{8\eta^2}{3n^4}\lambda^{2(D-1)}.
\tag{1}
```

The expectation includes both the fair matching schedule and all Haar gates. The gradient energy is the sum over the $`M=3nD`$ directions in
$`\{I,Z_i,Z_j,Z_iZ_j,H_x,H_y\}`$, with the convention in [the model](model.md). The proof uses the hopping direction of an actual gate in the first layer; no gate is inserted into the circuit.

Consequently, for fixed $`\alpha>1/\pi^2`$ and $`D=\lfloor\alpha n^2\rfloor`$,

```math
\mathbb E\,\mathcal G_Z=\Omega_\alpha(n^{-4}).
\tag{2}
```

The floor concerns the square of the derivative of the population loss. An average of per-example squared gradients is not substituted for that quantity.

## 2. The one-body transfer matrix

On one edge $`(i,j)`$, averaging a full charge-preserving Haar gate gives

```math
\mathbb E_G[G^\dagger Z_iG]
=\mathbb E_G[G^\dagger Z_jG]
=\frac{Z_i+Z_j}{2}.
\tag{3}
```

In the one-particle block the traceless part of either local Z averages to zero. In the zero- and two-particle blocks both sides of (3) have the same scalar value. Operators on other sites are unchanged.

Let $`P_A,P_B`$ average the coordinates on the edges of the two perfect matchings. Averaging the independent fair matching choice in one physical layer gives

```math
P=\frac12(P_A+P_B)
=I-\frac14L_{C_n},
\qquad
(Pv)_j=\frac12v_j+\frac14v_{j-1}+\frac14v_{j+1}.
\tag{4}
```

The Fourier modes $`e^{2\pi i k j/n}`$ have eigenvalues
$`\lambda_k=\cos^2(\pi k/n)`$.

This averaged matrix is appropriate for the density calculation, where independent complete layers are averaged before the conditional derivative is squared. It differs from the fixed-schedule product $`P_{\sigma_D}\cdots P_{\sigma_1}`$ used in the conditional concentration proof for [coherence labels](coherence_bound.md#3-an-exact-identity-for-matching-projections).

Let $`\rho_+`$ be the diagonal positive-class input mixture and $`\rho_-`$ its complemented mixture. Write

```math
\bar q_j=\operatorname{Tr}(Z_j\rho_+),
\qquad
\operatorname{Tr}(Z_j\rho_-)=-\bar q_j.
```

After $`t`$ averaged prefix layers the positive profile is $`P^t\bar q`$. Averaging a suffix of $`s`$ layers sends the readout to

```math
\sum_j b_jZ_j,\qquad b=P^se_0.
\tag{5}
```

## 3. Exact conditional response of an actual Haar gate

Fix a layer $`\ell`$ and the physical edge $`e=(a,a+1)`$. It belongs to that layer's chosen matching with probability $`1/2`$. On this event, select its actual Haar gate $`G`$ and the native hopping direction

```math
H_x=\frac{X_aX_{a+1}+Y_aY_{a+1}}2.
```

Set $`t=\ell-1`$, $`s=D-\ell`$, and

```math
\Delta q_t=(P^t\bar q)_a-(P^t\bar q)_{a+1},
\qquad
\Delta b_s=(P^se_0)_a-(P^se_0)_{a+1}.
```

All other gates in layer $`\ell`$ act on disjoint edges. They may be placed before the selected gate and cannot alter its reduced input state. The independent prefix and suffix layers retain their distributions after conditioning on the matching at layer $`\ell`$.

Use the ordered one-particle basis $`(|01\rangle,|10\rangle)`$, in which $`H_x=\sigma_x`$. The averaged input block has the form

```math
\rho_{+,1}=\frac12(wI+d\sigma_z),
\qquad
d=\Delta q_t/2.
```

Write the selected Haar block as $`G_1`$ and define

```math
G_1\sigma_zG_1^\dagger
=n_x\sigma_x+n_y\sigma_y+n_z\sigma_z.
```

The suffix observable on this block is $`\Delta b_s\sigma_z`$; its charge-dependent scalar part contributes no derivative. Since
$`i[\sigma_x,\sigma_z]=2\sigma_y`$, the conditional positive-class prediction derivative is $`\Delta q_t\Delta b_s n_y`$. The negative-class derivative is its negative. The balanced classification loss therefore has the exact conditional response

```math
\mathbb E\left[
\partial_{\ell,e,H_x}L_Z
\mid G,\ e\text{ present}
\right]
=-\frac12\Delta q_t\Delta b_s n_y.
\tag{6}
```

This equation uses the mean labeled profile $`\bar q`$ before any square is taken.

Haar conjugation makes $`(n_x,n_y,n_z)`$ uniform on the unit sphere. Rotational invariance and $`n_x^2+n_y^2+n_z^2=1`$ give $`\mathbb En_y^2=1/3`$. Conditional Jensen and the probability of the edge being present yield

```math
\mathbb E\,g_\ell^2
\ge\frac{(\Delta q_t)^2(\Delta b_s)^2}{24},
\tag{7}
```

where $`g_\ell`$ is the selected derivative when the edge is present and is defined to be zero otherwise. The factor $`1/24`$ consists of the squared loss factor $`1/4`$, the Haar Bloch factor $`1/3`$, and the matching probability $`1/2`$.

The full gradient energy contains this square and all other nonnegative coordinate squares. No independence between coordinates is needed.

## 4. A suffix Fourier bound with explicit constants

The readout difference has the exact Fourier representation

```math
\Delta b_s
=\frac1n\sum_{k=0}^{n-1}\lambda_k^s
\left[
\cos(2\pi ka/n)
-\cos(2\pi k(a+1)/n)
\right].
\tag{8}
```

The constant mode cancels. The $`k=1,n-1`$ pair contributes

```math
\frac4n\sin(\pi/n)\cos(\pi/n)\lambda^s,
\tag{9}
```

because $`a=n/4`$. The $`k=n/2`$ mode is zero when $`s\ge1`$.

For $`2\le k<n/2`$,

```math
\left(\frac{\lambda_k}{\lambda}\right)^s
\le
\exp\left[-\frac{\pi^2s}{n^2}(k^2-1)\right],
\qquad
\sin(\pi k/n)\le k\sin(\pi/n).
\tag{10}
```

For the first inequality, integrate $`\tan x\ge x`$ between $`\pi/n`$ and $`\pi k/n`$ in the difference of two logarithms of cosines. For the second, use $`|\sin(kx)|\le k|\sin x|`$.

A higher Fourier pair in (8) has absolute coefficient at most
$`(4/n)\sin(\pi k/n)`$. Therefore, for $`s\ge S`$, the entire higher-mode remainder satisfies

```math
|R_s|
\le
\frac4n\sin(\pi/n)\lambda^s
\sum_{k=2}^{\infty}k e^{-(k^2-1)}.
\tag{11}
```

The scalar sum can be bounded without a numerical approximation. Since
$`k^2-1\ge3(k-1)`$ for $`k\ge2`$, and $`r=e^{-3}<1/20`$,

```math
\sum_{k=2}^{\infty}k e^{-(k^2-1)}
\le
\sum_{j=1}^{\infty}(j+1)r^j
=\frac{r(2-r)}{(1-r)^2}
<
\frac{39}{361}
<
\frac18.
\tag{12}
```

Combining (9), (11), and (12), and using
$`\cos(\pi/n)\ge\cos(\pi/8)>5/8`$, proves

```math
\Delta b_s
\ge
\frac2n\sin(\pi/n)\lambda^s
\ge
\frac4{n^2}\lambda^s,
\qquad s\ge S.
\tag{13}
```

The last inequality uses $`\sin(\pi/n)\ge2/n`$. The lower-depth condition is material: the selected edge and readout are macroscopically separated, and sufficiently short suffixes can give exactly zero response.

## 5. The fixed-weight population has an initial signed contrast

For the source in [the model](model.md), the logical output bit on the control rail is fixed to zero in the positive class. Every other logical output bit has the same marginal occupation probability $`p=k_{\mathrm{nuis}}/(m-1)`$, even though the bits are dependent.

After the fixed wire permutation, the mean positive physical profile is the perfect-wall profile on the two control-rail sites and $`\eta`$ times that wall profile on every other site. At the wall boundary,
$`q^{\mathrm{wall}}_a=-1`$ and $`q^{\mathrm{wall}}_{a+1}=+1`$. It follows that

```math
\Delta q_0=\bar q_a-\bar q_{a+1}
\le-2\eta,
\qquad
|\Delta q_0|\ge2\eta.
\tag{14}
```

The bound is valid regardless of where the fixed permutation places the control rail. A control site has magnetization magnitude one and a noncontrol site magnitude $`\eta`$; their signs at this edge are opposite.

Choose the first layer, so $`t=0`$ and $`s=D-1`$. Equations (7), (13), and (14) give

```math
\begin{aligned}
\mathbb E\,\mathcal G_Z
&\ge \frac{\eta^2}{6}(\Delta b_{D-1})^2\\
&\ge
\frac{2\eta^2}{3n^2}\sin^2(\pi/n)\lambda^{2(D-1)}\\
&\ge
\frac{8\eta^2}{3n^4}\lambda^{2(D-1)}.
\end{aligned}
```

This proves Theorem 1 for the actual population loss. For the perfect wall without nuisance, set $`p=0`$ and $`\eta=1`$.

At fixed diffusive depth,
$`\lambda^{2(D-1)}=\exp[-2\pi^2\alpha+o(1)]`$.
Together with the uniform positive lower bound on $`\eta`$, this proves (2).

## 6. General profiles and a sum over internal layers

The first-layer argument uses a special property of the fixed-weight source: its mean profile already has a signed contrast at the selected edge. A broader profile class can be treated after a sufficiently long prefix.

Let $`q^{(x)}`$ be any complementary half-filled basis-state family with a fixed nuisance distribution and

```math
\langle f,q^{(x)}\rangle\ge\beta n,
\qquad
f_j=\sin\left[\frac{2\pi}{n}\left(j-a-\frac12\right)\right],
\qquad
0<\beta\le1.
```

Its mean profile obeys $`\|\bar q\|_\infty\le1`$ and
$`\langle f,\bar q\rangle\ge\beta n`$. Define

```math
\tau_\beta=1+\log(1/\beta),
\qquad
T_\beta=\left\lceil\frac{\tau_\beta n^2}{\pi^2}\right\rceil.
```

### Prefix filtering gives a common sign

For $`t\ge1`$, put
$`f_j^{(k)}=\sin[2\pi k(j-a-1/2)/n]`$.
Pairing opposite Fourier modes gives the exact edge-difference expansion

```math
\Delta q_t
=-\frac4n
\sum_{k=1}^{n/2-1}
\sin(\pi k/n)\lambda_k^t
\langle f^{(k)},\bar q\rangle.
\tag{15}
```

The leading term is

```math
-\frac4n\sin(\pi/n)\lambda^t\langle f,\bar q\rangle
\le-4\beta\sin(\pi/n)\lambda^t.
\tag{16}
```

The cosine quadrature does not enter this particular edge difference. Since
$`|\langle f^{(k)},\bar q\rangle|\le n`$, (10) bounds the remainder by

```math
|R_t|
\le4\sin(\pi/n)\lambda^t
\sum_{k=2}^{\infty}
k\exp\left[-\frac{\pi^2t}{n^2}(k^2-1)\right].
\tag{17}
```

When $`t\ge T_\beta`$, the scalar sum satisfies

```math
\begin{aligned}
\sum_{k=2}^{\infty}k e^{-\tau_\beta(k^2-1)}
&=
\sum_{k=2}^{\infty}k e^{-(k^2-1)}\beta^{k^2-1}\\
&\le
\beta^3\sum_{k=2}^{\infty}k e^{-(k^2-1)}
<
\frac{\beta^3}{8}
\le\frac{\beta}{2}.
\end{aligned}
\tag{18}
```

Combining (16)–(18) proves the uniformly signed estimate

```math
\Delta q_t
\le
-2\beta\sin(\pi/n)\lambda^t,
\qquad t\ge T_\beta.
\tag{19}
```

The mean labeled profile was formed before filtering and before squaring. Thus the protected conditional responses cannot cancel when the nuisance examples are averaged.

### Distinct layers contribute nonnegative energies

For a layer with $`t=\ell-1\ge T_\beta`$ and $`s=D-\ell\ge S`$, insert (13) and (19) into (7). Since $`s+t=D-1`$,

```math
\begin{aligned}
\mathbb E\,g_\ell^2
&\ge
\frac{2\beta^2}{3n^2}\sin^4(\pi/n)\lambda^{2(D-1)}\\
&\ge
\frac{32\beta^2}{3n^6}\lambda^{2(D-1)}.
\end{aligned}
\tag{20}
```

Exactly

```math
J=\max\{0,D-T_\beta-S\}
```

layers meet the two conditions. Their selected directions are distinct coordinates of the full gradient. Summing their squares proves

```math
\mathbb E\,\mathcal G_Z
\ge
J\,\frac{32\beta^2}{3n^6}\lambda^{2(D-1)}.
\tag{21}
```

For fixed
$`\alpha>(\tau_\beta+1)/\pi^2`$
and $`D=\lfloor\alpha n^2\rfloor`$,
one has $`J=\Theta(n^2)`$, giving

```math
\mathbb E\,\mathcal G_Z
=\Omega_{\alpha,\beta}(n^{-4}).
\tag{22}
```

The same profile condition supplies the [uniform coherence upper bound](coherence_bound.md#1-statement). Thus the comparison extends to any fixed nuisance distribution in this profile class. The fixed-weight family has the stronger first-layer result and needs only $`\alpha>1/\pi^2`$.

## 7. Logarithmic-depth corollaries

Fix $`\epsilon\in(0,1)`$. If

```math
S+1\le D\le
\frac{(1-\epsilon)n^2\log n}{2\pi^2},
\tag{23}
```

then
$`\log\lambda=-\pi^2/n^2+O(n^{-4})`$
gives

```math
\lambda^{2(D-1)}
=\Omega_\epsilon(n^{-1+\epsilon}).
\tag{24}
```

For the fixed-weight nuisance source, Theorem 1 therefore implies

```math
\mathbb E\,\mathcal G_Z
=\Omega_\epsilon(n^{-5+\epsilon}).
\tag{25}
```

In the same window, [the matching-count refinement of the coherence bound](coherence_bound.md#7-matching-statistics-and-the-logarithmic-window) gives

```math
\mathbb E\,\mathcal G_X,\quad
\mathbb E\,\mathcal G_Y
\le\exp[-\Omega_\epsilon(n^\epsilon)].
\tag{26}
```

For the broader profile class, (21) and (24) instead give the explicit bound

```math
\mathbb E\,\mathcal G_Z
\ge
C_{\beta,\epsilon}\,J\,n^{-7+\epsilon}
```

for a positive constant and sufficiently large $`n`$. In particular, if
$`D\ge T_\beta+S+\gamma n^2`$
for some fixed $`\gamma>0`$, the density floor is again
$`\Omega_{\beta,\epsilon,\gamma}(n^{-5+\epsilon})`$.
At the upper endpoint of (23), $`J=\Theta(n^2\log n)`$ gives the additional factor $`\log n`$. The extra prefix condition is required for this general-profile statement.

These are sufficient ranges for the proved estimates. They do not locate a sharp transition at the logarithmic depth scale.

## 8. Interpretation and limitations

The invariant total-charge mode has no spatial derivative and gives no response by itself. The lower bound comes from a nonuniform conserved-density mode that overlaps both the labeled input profile and the local readout after transport. Equation (6) converts the product of those two spatial differences into a native training derivative.

The result is an ensemble second-moment floor in a fixed coordinate metric. It does not prove that a constant fraction of initializations has a useful gradient, that an optimizer converges, or that the classifier has a computational advantage. The population misclassification loss is essential to the calculation; a different loss can contain additional label-independent derivatives.

The one-body calculation does not assert classical simulation of the full interacting circuit. General local charge-preserving Haar gates include diagonal interaction phases, and only the particular averaged sector in (3) is closed under this transfer matrix.

Conserved one-body modes are part of the operator-hydrodynamic framework developed, for example, by [Khemani, Vishwanath, and Huse, Physical Review X 8, 031057 (2018)](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.031057). The exact layer normalization, response identity, and finite-size Fourier estimates needed for the bounds above have been derived explicitly here.

