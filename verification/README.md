# Reproduce the finite verification

The scripts check finite identities and the explicit native encoder and
decoder used in the scientific account. The general-size inequalities are
established in [the written proofs](../science/model.md); finite enumeration
does not establish their asymptotic scaling or literature novelty.

## Run the complete suite

Use Python 3.10 or later with NumPy installed. From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 verification/run_all.py
```

The first command is needed only if NumPy is not already available.
Run Python normally, without `-O`, because the finite tolerances are checked
with assertions. The suite requires no network access, external datasets,
quantum hardware, or QRAM.

A successful run prints:

```text
PASS: all finite identity and construction assertions.
PASS: analytic bounds evaluated in their stated domain.
Complete output: <local path>/verification/results/latest.json
```

The default result directory is ignored by git. To choose another path:

```bash
python3 verification/run_all.py --output /tmp/qml-verification.json
```

[reference_result.json](reference_result.json) records one actual complete
run, including the Python and NumPy versions. It is evidence of that finite
run, rather than an exact cross-platform byte-comparison target. The
independent encoder reference is [encoder_expected.json](encoder_expected.json).

The recorded run used Python 3.12.14 and NumPy 2.3.5. Its maximum
matching-harmonic error was $`3.56\times10^{-15}`$, maximum conditional
density-response error was $`1.34\times10^{-15}`$, and maximum four-shift
error was $`6.60\times10^{-17}`$ after rounding upward. Both recorded
quantum-inequality excesses were zero. The smallest Fourier readout ratio
was approximately 1.786, above its required lower threshold of one.
All encoder and decoder assertions also passed.

## What is checked

| Component | Finite coverage and acceptance criterion | Scientific role |
|---|---|---|
| Matching harmonics | All matching words of lengths 1–8 at $`n=8,12,16,32`$: 2,040 instances; harmonic absolute error below $`2\times10^{-12}n`$; exact integer binomial multiplicities | Checks the projection identity and switch-count law used in [coherence](../science/coherence_bound.md) |
| Native tangent basis | Six generators: charge commutators, norm and integer spectra within $`10^{-14}`$; real rank exactly six | Checks the local coordinate convention and finite Fourier frequencies |
| Conditional density response | 50 seeded Haar blocks with independently sampled diagonal input probabilities and readout coefficients; absolute derivative error below $`10^{-12}`$ | Checks the local signed identity used in [density transport](../science/density_transport.md) |
| Quantum matrix-element and derivative bounds | Nine cases at $`n=8`$, with depths 2, 5, 12 and three generator types; 16 equally spaced angles per case; inequality excess at most $`10^{-12}`$ | Checks the commuting-projector inequality, finite-frequency Parseval step, and four-shift rule |
| Fourier readout and wall response | $`n=8,12,16,24,32,64,128,256`$ and three depths per size; readout lower-bound ratio at least $`1-10^{-10}`$ and wall-identity relative error at most $`10^{-10}`$ | Checks the finite Fourier normalization and lower-bound constants |
| Native encoder and decoder | $`n=4,8`$; all nuisance inputs and all six logical Pauli eigenstates; vector and label errors below $`10^{-12}`$; all implemented gates conserve charge and are unitary within tolerance | Checks the exact [data construction](../science/data_encoding.md) independently of random-circuit training |
| Explicit analytic bounds | Five scalar sizes at $`D=\lceil n^2/8\rceil`$, with the density suffix condition checked | Reproduces the table and the interpretation in [finite-size bounds](../science/finite_size.md) |

The $`n=4`$ encoder check tests the gate construction only. The transport
theorem has the separate domain $`n\ge8`$, $`n\in4\mathbb N`$.
The encoder enumeration also includes nuisance strings outside the sparse
profile family: the decoder works on all strings, while the gradient
comparison requires the stated harmonic overlap.

Sixteen angle samples exactly resolve the trigonometric polynomials used
in the finite Parseval check up to floating-point error. Nine small-circuit
cases do not exhaust all Haar gates or all circuit sizes. Those
quantifiers are supplied by the algebraic proof.

## Run one component

```bash
python3 verification/verify_components.py
python3 verification/verify_diffusion.py
python3 verification/verify_encoder.py
python3 verification/evaluate_bounds.py
```

Each component prints structured JSON. The encoder accepts an optional
`--output` path. The suite has fixed random seeds for its finite quantum
and Haar-block checks; normal differences in numerical libraries may change
the last few digits of recorded errors.

## What remains a proof obligation

Negative association is imported from the exact theorems cited in the
[coherence proof](../science/coherence_bound.md); it is not inferred from
samples. Haar invariance, extension to every native tangent, nuisance
averaging, population noncancellation, general-size Fourier estimates,
and the decoder's architectural embedding are justified in their respective
scientific files.

The scripts neither measure a training success rate nor infer a typical
density-gradient lower bound. They do not certify a quantum advantage,
an exponential sampling lower bound, noise robustness, or a sharp
dynamical crossover.
