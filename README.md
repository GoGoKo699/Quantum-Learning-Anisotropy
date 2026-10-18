# Quantum Learning Anisotropy

**How does conserved transport select which labels produce gradients in a
quantum classifier?** This project gives a rigorous separation between
density and relative-phase labels at diffusive depth in local
particle-number-conserving random circuits.

The two tasks use the same circuit ensemble, local readout, conserved charge,
and efficient encoder. They have **exactly the same unlabeled average density
operator**, including for one data source with exponentially many nuisance
configurations.

At depth $`D=\lfloor\alpha n^2\rfloor`$, with fixed
$`\alpha>1/\pi^2`$, the expected squared norm of the complete native
gate gradient obeys:

| Label information | Full-gradient energy at initialization |
|---|---|
| Conserved-density branch | $`\mathbb E\lVert\nabla L_Z\rVert^2=\Omega(n^{-4})`$ |
| Relative quantum phase | $`\mathbb E\lVert\nabla L_X\rVert^2,\mathbb E\lVert\nabla L_Y\rVert^2\le e^{-\Omega(n)}`$ |

The loss is the expected binary error of the measured prediction. The bounds
include all specified norm-one tangent directions of every two-qubit gate.
The density result is an ensemble moment, while the phase upper also yields
typical small full gradients. Neither result is an optimizer-convergence
claim.

## Mechanism

A macroscopic charge statistic still identifies the complementary branches
after diffusive evolution. A commuting-projector inequality converts that
branch distinguishability into a bound on the local interference amplitude.
Haar invariance and a finite-frequency derivative identity then control every
local phase-loss derivative. The density floor follows from the signed
response of the surviving first Fourier mode.

The same fixed inverse encoder perfectly classifies every nuisance input
after the appropriate logical basis rotation. Preparation and decoding use
$`O(n)`$ depth and $`O(n^2)`$ nearest-neighbor conserving gates, without
ancillas or QRAM. With overwhelming probability, the random architecture
contains this perfect classifier as an allowed assignment of its gates.

## Read the science

Start with the [model and exact results](science/model.md).

| To understand | Read |
|---|---|
| Common circuit, loss, tangent metric, and theorem domains | [Model](science/model.md) |
| Extensive nuisance source, same average state, and exact native decoder | [Data encoding](science/data_encoding.md) |
| Conditional exclusion dynamics and the full phase-gradient upper | [Coherence bound](science/coherence_bound.md) |
| Signed population response and the polynomial lower | [Density transport](science/density_transport.md) |
| Logical-axis covariance, alternative losses, and measurement resources | [Loss and geometry](science/loss_and_geometry.md) |
| Physical meaning and the limits of a gradient diagnosis | [Interpretation](science/interpretation.md) |
| Quantitative meaning of the explicit estimates | [Finite-size bounds](science/finite_size.md) |
| Established ingredients and closely related results | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

[The LLM reading guide](llms.txt) maps questions to authoritative files.

## Reproduce the finite checks

With Python and NumPy available, run from the repository root:

```bash
python3 verification/run_all.py
```

The suite checks Fourier identities, matching-switch counts, the native
tangent basis, small-circuit projector and derivative bounds, and the exact
encoder and decoder. [Verification instructions](verification/README.md)
state the requirements, tolerances, and scope of each check.
The analytical and asymptotic claims rest on the written proofs and cited
theorems, rather than finite enumeration.

## Scope

The model is a half-filled periodic qubit ring with independent Haar gates
from the full local conserving group and uniformly selected even/odd matching
layers. It includes interacting phases. It fixes the stochastic
classification-error loss and a native local tangent normalization.

The supplied data is structured and has a known efficient decoder. There is
no quantum-advantage or data-hardness claim. The average input state agrees
across tasks, but their labeled pure-state decompositions differ. The
logarithmic depth extension is an estimate window, not a sharp crossover.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
