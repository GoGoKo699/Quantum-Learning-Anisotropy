# What the explicit bounds certify at finite size

The [main theorem](model.md#4-full-gradient-separation) establishes a
polynomial density-gradient floor and an exponential phase-gradient upper
at fixed diffusive depth. Its constants come from deliberately conservative
concentration and Fourier estimates. Evaluating those constants clarifies
the theorem's quantitative scope.

The calculation below evaluates scalar inequalities. It does not simulate
training, estimate typical gradient sizes, or fit an asymptotic exponent.

## 1. Quantities being evaluated

Use the fixed-weight nuisance source and take $`D=\lceil n^2/8\rceil`$.
This choice has $`\alpha=1/8>1/\pi^2`$, so the density bound is applicable
for every size in the table. Define

```math
p=\frac{\lfloor(n/2)/8\rfloor}{n/2-1},\qquad
\lambda_1=\cos^2(\pi/n),\qquad
c_n=\cos(2\pi/n),
```

```math
\beta=\frac2\pi-\frac14,\qquad
m_*=[\beta n-\pi]_+,\qquad
r_D=D/2+\sqrt{nD},\qquad M=3nD.
```

The conservative density floor and the matching-averaged phase upper are

```math
B_Z=\frac{8(1-2p)^2}{3n^4}\lambda_1^{2(D-1)},
```

```math
B_\perp=M\min\left\{1,\,
4\exp\left[-\frac{m_*^2c_n^{2r_D}}{8n}\right]+e^{-2n}
\right\}.
```

They obey $`\mathbb E\mathcal G_Z\ge B_Z`$ and
$`\mathbb E\mathcal G_X,\mathbb E\mathcal G_Y\le B_\perp`$.
The density proof also supplies a stronger finite floor retaining
$`\sin^2(\pi/n)`$; the table uses the simpler displayed bound.

Because $`B_Z>0`$, their ratio gives the valid implication

```math
\frac{\mathbb E\mathcal G_X}{\mathbb E\mathcal G_Z},
\quad
\frac{\mathbb E\mathcal G_Y}{\mathbb E\mathcal G_Z}
\le\frac{B_\perp}{B_Z}.
```

This is a comparison of ensemble moments. It does not compare the two
energies pointwise for every initialized circuit.

## 2. Scalar evaluation

The following values are rounded from
[the recorded verification output](../verification/reference_result.json).
A negative logarithm means that the bound is smaller than one.

| Qubits $`n`$ | Matching layers $`D`$ | $`\log_{10}B_Z`$ | $`\log_{10}B_\perp`$ |
|---:|---:|---:|---:|
| 256 | 8,192 | −10.531 | 6.799 |
| 1,024 | 131,072 | −12.937 | 8.605 |
| 4,096 | 2,097,152 | −15.345 | 8.756 |
| 16,384 | 33,554,432 | −17.753 | 2.719 |
| 65,536 | 536,870,912 | −20.161 | −28.069 |

At the first two sizes the phase estimate is only the trivial total
coordinate bound $`M`$. At 4,096 and 16,384 qubits it improves on $`M`$
but still does not certify phase energy below the density floor. At the
last displayed size it certifies
$`B_\perp/B_Z\approx1.24\times10^{-8}`$.
These are bounds, so the physical energies need not be close to either
number.

The very large last depth is part of this explicit illustration. The
table does not claim a useful numerical gap on a near-term device. It
also does not imply that the separation starts at the last displayed size:
the bound may be loose at every size, and no onset is inferred from it.

## 3. Why a valid asymptotic theorem can have loose constants

For fixed $`\alpha`$ and $`D\sim\alpha n^2`$,

```math
\frac{m_*^2c_n^{2r_D}}{8n}
=\frac{\beta^2e^{-2\pi^2\alpha}}8\,n\,[1+o(1)].
```

The positive coefficient of $`n`$ proves exponential decay, but can be
small. The energy upper also contains the polynomial coordinate count
$`M`$. For the upper to fall below a small polynomial density floor,
the concentration exponent must dominate both that count and the inverse
floor.

Several steps leave room for better constants: the lower bound
$`m_*\le\langle P_{\sigma_1}f,q^{(x)}\rangle`$, the use of a worst-case
branch profile within the nuisance family, the denominator $`8n`$ in
concentration, and the tail bound on matching switches. The proof
identifies an exact weight sum that permits the denominator $`3n`$,
and an exact binomial average can replace the tail split. These potential
improvements do not turn the current inequalities into measured values.

The [logarithmic depth window](coherence_bound.md#7-matching-statistics-and-the-logarithmic-window)
likewise specifies a range in which the proof remains informative
asymptotically. Failure of a bound outside that range does not establish
a dynamical transition or a revived training gradient.

## 4. Reproduction and numerical stability

Run

```bash
python3 verification/evaluate_bounds.py
```

or use the complete [verification suite](../verification/README.md).
The implementation calculates

```math
\log\lambda_1=\log\!\left[1-\sin^2(\pi/n)\right],\qquad
\log c_n=\log\!\left[1-2\sin^2(\pi/n)\right]
```

with `log1p` and combines exponentially small terms in the logarithmic
domain. It avoids subtracting two nearly equal powers and underflow in
the reported energy bounds. Floating-point evaluation is a reproducibility
check on the displayed constants; the inequalities themselves are proved in
[coherence](coherence_bound.md) and [density transport](density_transport.md).
