# Encoded data source and exact decoding

The data source uses the half-filled ring and gate set in [the circuit model](model.md). A fixed charge-conserving encoder supplies every label axis and every nuisance configuration. Its inverse gives an exact classifier with polynomial native resources.

## 1. Dual-rail logical qubits

Let $`n\in4\mathbb N`$, $`n\ge8`$, and $`m=n/2`$. Logical rail $`r\in\{1,\ldots,m\}`$ occupies physical sites $`(2r-2,2r-1)`$, with

```math
|0_L\rangle=|01\rangle,
\qquad
|1_L\rangle=|10\rangle.
```

Each rail contains exactly one excitation, so the entire logical space lies in the physical charge sector $`Q=m`$. Logical kets appearing below are understood to be embedded in this dual-rail subspace.

The reference input is $`|0_L\rangle^{\otimes m}=|01\rangle^{\otimes m}`$. If preparation begins from a vacuum reset, loading this reference state requires $`m`$ excitations. Both the density and phase sources use the same loading step. Every subsequent encoder, decoder, and classifier gate conserves charge.

Any logical one-qubit unitary $`R`$ is an allowed two-qubit gate:

```math
U_R
=|00\rangle\langle00|+|11\rangle\langle11|
 +\sum_{b,b'=0}^1R_{bb'}|b_L\rangle\langle b'_L|.
```

Thus choosing the control state and preparing a nuisance product input require at most one parallel layer of logical one-qubit gates, using $`O(n)`$ gates.

## 2. One fixed encoder

Write the input logical bits as $`(b,x_2,\ldots,x_m)`$. Apply the sequential CNOT chain

```math
F=\mathrm{CNOT}_{m-1\to m}\cdots
  \mathrm{CNOT}_{2\to3}\mathrm{CNOT}_{1\to2},
```

where the rightmost gate acts first. The output logical bits are

```math
y_1=b,
\qquad
y_r=b\oplus x_2\oplus\cdots\oplus x_r.
```

In particular, changing $`b`$ complements every logical output bit.

Set $`a=n/4`$. Define the reference physical wall $`z`$ by its magnetization profile

```math
q_j=\langle z|Z_j|z\rangle
=\begin{cases}
 +1,&a+1\le j\le a+n/2,\\
 -1,&\text{otherwise},
\end{cases}
\qquad 0\le j<n.
```

Its computational bit at site $`j`$ is $`(1-q_j)/2`$. Choose a fixed wire permutation $`\Pi`$ that maps the alternating string $`|01\rangle^{\otimes m}`$ to $`|z\rangle`$. One deterministic choice matches source zero bits, in increasing site order, to zero-bit positions of $`z`$ in increasing order, and does the same for source one bits. If the associated site permutation is $`\pi`$, a source bit at $`j`$ moves to $`\pi(j)`$.

The encoder is

```math
E=\Pi F.
```

It contains no control Hadamard: the initial logical control state determines the task axis. For every nuisance string $`x=(x_2,\ldots,x_m)`$, define $`z_x`$ by

```math
E|0_L,x\rangle=|z_x\rangle.
```

The complementary-control identity is exact:

```math
E|1_L,x\rangle=|\bar z_x\rangle,
```

where $`\bar z_x`$ is the bitwise complement of $`z_x`$. Both branches have $`n/2`$ excitations. Consequently,

```math
E\left[(\alpha|0_L\rangle+\beta|1_L\rangle)\otimes|x\rangle\right]
=\alpha|z_x\rangle+\beta|\bar z_x\rangle.
```

The same physical encoder therefore supplies density labels, relative-phase labels, and arbitrary logical Bloch axes.

## 3. Fixed-weight nuisance source

Use the following explicit distribution, independently of the control label and axis:

1. Set $`y_1=0`$ and $`k=\lfloor m/8\rfloor`$.
2. Choose a uniform $`k`$-element subset of $`\{2,\ldots,m\}`$ and set precisely those $`y_r`$ to one.
3. Compute $`x_r=y_r\oplus y_{r-1}`$ for $`r=2,\ldots,m`$.
4. Prepare the corresponding dual-rail nuisance product state $`|x\rangle`$.

The map between the selected $`y`$ strings and nuisance $`x`$ strings is bijective. Denote its image by $`\mathcal X_k`$. The number of nuisance values and their mixture are

```math
N=|\mathcal X_k|=\binom{m-1}{k},
\qquad
\tau=\frac1N\sum_{x\in\mathcal X_k}|x\rangle\langle x|.
```

Here $`\log N=\Theta(n)`$ asymptotically. Uniform subset sampling and adjacent XORs require polynomial classical work. Each quantum example is generated directly from a sampled product input; no coherent database access or QRAM is required.

The fixed-weight constraint concerns the output bits $`y_2,\ldots,y_m`$. The input nuisance string $`x`$ generally has a different Hamming weight.

## 4. Label-conditioned states and the common average

For a unit Bloch vector $`u\in\mathbb R^3`$, let $`|u,+\rangle`$ and $`|u,-\rangle`$ be the eigenstates of $`u\cdot\sigma`$ with eigenvalues $`+1`$ and $`-1`$. The two labels occur with equal probability, and their physical states are

```math
\rho_{u,\pm}
=E\left[|u,\pm\rangle\langle u,\pm|\otimes\tau\right]E^\dagger.
```

Their supports are orthogonal. Each class state has rank $`N`$ with nonzero eigenvalues $`1/N`$. For every axis,

```math
\frac{\rho_{u,+}+\rho_{u,-}}2
=\rho_{\mathrm{mix}}
=E\left[\frac{I_{\mathrm{control}}}{2}\otimes\tau\right]E^\dagger.
```

Thus the average state is exactly identical, with rank $`2N`$. The axes use different pure-state decompositions of this same average. They do not merely relabel an unchanged list of pure examples.

The principal axes give the following pure examples for each sampled nuisance value:

| Axis | Positive example | Negative example |
|---|---|---|
| $`Z`$ | $`\lvert z_x\rangle`$ | $`\lvert\bar z_x\rangle`$ |
| $`X`$ | $`(\lvert z_x\rangle+\lvert\bar z_x\rangle)/\sqrt2`$ | $`(\lvert z_x\rangle-\lvert\bar z_x\rangle)/\sqrt2`$ |
| $`Y`$ | $`(\lvert z_x\rangle+i\lvert\bar z_x\rangle)/\sqrt2`$ | $`(\lvert z_x\rangle-i\lvert\bar z_x\rangle)/\sqrt2`$ |

Each pure $`X`$ or $`Y`$ example has Schmidt rank two and one ebit across every nonempty proper physical bipartition. The two signs have identical reduced states on every proper subsystem before the classifier acts. The label is a relative phase between macroscopic branches; the exact decoder below collects that phase into one rail.

## 5. The surviving density profile

Define the fixed first-harmonic weights

```math
f_j=\sin\!\left[\frac{2\pi}{n}\left(j-a-\frac12\right)\right],
\qquad
m_0=\sum_jf_jq_j=2\csc(\pi/n).
```

Relative to the all-zero logical output, each changed $`y_r`$ flips two physical $`Z`$ signs after the permutation. Its contribution can decrease the weighted overlap by at most four. Every positive nuisance branch therefore obeys

```math
\langle f,q_x\rangle\ge m_0-4k
\ge\left(\frac2\pi-\frac14\right)n
=\beta n,
\qquad
\beta=\frac2\pi-\frac14>0.
```

This uniform overlap is the hypothesis used by the coherence-gradient concentration argument.

The population density calculation also has a direct mean-profile formula. Put $`p=k/(m-1)`$. Each noncontrol output rail is flipped with probability $`p`$, whereas the first rail has $`y_1=0`$ for the positive class. Hence

```math
\bar q_j=\frac1N\sum_x(q_x)_j
=\begin{cases}
q_j,&j\in\{\pi(0),\pi(1)\},\\
(1-2p)q_j,&\text{otherwise}.
\end{cases}
```

At an original wall edge $`e=(a,a+1)`$,

```math
|\bar q_a-\bar q_{a+1}|\ge2(1-2p).
```

This bound acts on the signed population contrast before squaring. It is the input needed for the population-density gradient lower bound; averaging separate squared-gradient bounds would not supply it.

## 6. Native implementation and preparation resources

Consider adjacent logical pairs occupying physical sites $`(A,B)`$ and $`(C,D)`$, where $`B`$ and $`C`$ are neighbors. For their logical bits $`r,s`$,

```math
N_B=1-r,
\qquad N_C=s,
\qquad N_j=(I-Z_j)/2.
```

The native diagonal gates

```math
V=\exp(i\pi N_BN_C),
\qquad
W=\exp(i\pi N_C)
```

act together on the logical subspace as

```math
WV=(-1)^{(1-r)s+s}=(-1)^{rs}=CZ_L.
```

Both factors may be applied on the same boundary pair $`(B,C)`$. Their product is the allowed physical two-qubit matrix $`\mathrm{diag}(1,-1,1,1)`$ in the ordered basis $`00,01,10,11`$. A logical CNOT follows from target Hadamards:

```math
\mathrm{CNOT}_{r\to r+1}
=H_{r+1}\,CZ_{r,r+1}\,H_{r+1}.
```

Retaining $`V`$ and $`W`$ as separate native gates gives four gates and depth four per logical CNOT. No inter-rail SWAP or ancilla is needed for this operation. The CNOT chain uses at most $`4(m-1)`$ gates and depth $`4(m-1)`$.

Compile the fixed wire permutation by odd-even adjacent-SWAP sorting of each wire's target position. This uses at most $`n`$ parallel sorting phases and at most $`n(n-1)/2`$ SWAP gates. SWAP preserves charge. The resulting conservative encoder bounds are

```math
d_E\le4(m-1)+n=3n-4,
\qquad
g_E\le4(m-1)+\frac{n(n-1)}2.
```

Including the initial logical product-state choices adds $`O(n)`$ gates and at most a constant depth. The complete source uses $`n`$ physical qubits, no ancilla, $`O(n)`$ depth, and $`O(n^2)`$ native two-qubit gates per example.

## 7. Exact decoder and matching-skeleton expressivity

Applying $`E^\dagger`$ returns the control state and the original nuisance product input. Choose a logical unitary $`R_u`$ satisfying

```math
R_u|u,+\rangle=|0_L\rangle,
\qquad
R_u|u,-\rangle=|1_L\rangle.
```

Then $`R_uE^\dagger`$, followed by measurement of physical $`Z_0`$, predicts the label with zero error for every nuisance value. The named axes use

```math
R_Z=I,
\qquad R_X=H,
\qquad R_Y=HS^\dagger,
```

where $`S^\dagger`$ acts before $`H`$. One general logical $`U(2)`$ gate can implement the final rotation; the explicit named-gate construction uses at most two. Its depth is therefore at most $`3n-2`$ under the conservative encoder bound.

Each layer of this explicit decoder has a prescribed even or odd matching parity: a CNOT component uses one edge, and every sorting layer uses disjoint edges of one parity. The ring's unused edges can carry identities. Let $`L=O(n)`$ be the resulting prescribed matching-word length.

For an independently sampled sequence of $`D`$ fair matching choices, embed the decoder greedily. At each layer, execute its next required layer if the parity matches and otherwise wait. After a successful match, advance to the next decoder layer. Set all other gates to identity.

Conditional on the past, each match succeeds with probability $`1/2`$. These success indicators can be extended after completion to independent Bernoulli variables. Therefore

```math
\Pr(\text{decoder does not fit})
=\Pr\!\left[\mathrm{Bin}(D,1/2)\lt L\right]
\le e^{-D/16},
\qquad D\ge4L.
```

At $`D=\alpha n^2`$ for fixed positive $`\alpha`$, the sampled architecture contains an exact classifier with probability $`1-e^{-\Omega(n^2)}`$. This is an expressivity statement about allowed gate assignments on the sampled skeleton. It makes no assertion about reaching those assignments from Haar initialization.

## 8. Per-example resource account

For the random classifier used in the gradient theorem, one shot requires preparation followed by $`nD/2`$ classifier gates and one physical $`Z_0`$ measurement. Its gate count is

```math
g_{\mathrm{shot}}\le \frac{nD}{2}+g_E+O(n).
```

At diffusive depth $`D=\Theta(n^2)`$, this is $`\Theta(n^3)`$ gates, while encoder depth and gate count remain lower order. The exact target decoder has $`O(n)`$ depth and $`O(n^2)`$ gates. The relative-phase examples are therefore structured states with a known efficient classifier; no computational-hardness separation is assumed.

The deterministic native-gate construction is checked by [verify_encoder.py](../verification/verify_encoder.py), with [reference output](../verification/encoder_expected.json). It tests $`n=4,8`$, the six logical control states, and every nuisance input at those sizes. The $`n=4`$ instance checks the encoder only and does not change the transport theorem's $`n\ge8`$ hypothesis.
