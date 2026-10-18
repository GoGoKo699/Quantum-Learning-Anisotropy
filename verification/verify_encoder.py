"""Small deterministic audit of the native U(1) encoder/decoder construction.

Checks n=4,8 and logical 0,1,+,-,+i,-i by full state vectors.  This is a
construction check, not a statistical test of the random-circuit theorem.
Site zero is the most significant computational-basis bit.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


H_LOGICAL = np.eye(4, dtype=complex)
H_LOGICAL[1:3, 1:3] = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
S_DAG_LOGICAL = np.diag([1, 1, -1j, 1]).astype(complex)
PHYSICAL_CZ = np.diag([1, 1, 1, -1]).astype(complex)
PHASE_ON_RIGHT = np.diag([1, -1, 1, -1]).astype(complex)
SWAP = np.array(
    [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
    dtype=complex,
)
LOCAL_CHARGE = np.diag([0, 1, 1, 2])


def apply_gate(state, n, left, gate):
    axes = [left, left + 1] + [j for j in range(n) if j not in (left, left + 1)]
    tensor = state.reshape([2] * n).transpose(axes).reshape(4, -1)
    return (gate @ tensor).reshape([2] * n).transpose(np.argsort(axes)).reshape(-1)


def execute(state, n, layers, inverse=False):
    result = state.copy()
    selected = reversed(layers) if inverse else layers
    for layer in selected:
        gates = reversed(layer) if inverse else layer
        for left, gate, _name in gates:
            result = apply_gate(result, n, left, gate.conj().T if inverse else gate)
    return result


def basis_state(bits):
    vector = np.zeros(2 ** len(bits), dtype=complex)
    vector[int("".join(map(str, bits)), 2)] = 1
    return vector


def encoder_layers(n):
    # CNOT chain.  H acts inside the target pair; CZ is realized on the
    # adjacent boundary rails (2j+1,2j+2) by two diagonal native gates.
    layers = []
    for j in range(n // 2 - 1):
        boundary = 2 * j + 1
        target_pair = 2 * j + 2
        layers.extend([
            [(target_pair, H_LOGICAL, "logical_H")],
            [(boundary, PHYSICAL_CZ, "physical_CZ")],
            [(boundary, PHASE_ON_RIGHT, "phase_on_target_left_rail")],
            [(target_pair, H_LOGICAL, "logical_H")],
        ])

    # Choose a fixed permutation that maps alternating logical zero to the
    # specified domain wall. Assign each source wire its target rank, then
    # odd-even transposition sort those ranks. Gates are fixed in advance.
    a = n // 4
    q = [1 if a + 1 <= j <= a + n // 2 else -1 for j in range(n)]
    z = [(1 - entry) // 2 for entry in q]
    alternating = [j % 2 for j in range(n)]
    targets = {bit: [j for j, value in enumerate(z) if value == bit] for bit in (0, 1)}
    used = {0: 0, 1: 0}
    wire_ranks = []
    for bit in alternating:
        wire_ranks.append(targets[bit][used[bit]])
        used[bit] += 1
    permutation = wire_ranks.copy()
    for phase in range(n):
        layer = []
        for left in range(phase % 2, n - 1, 2):
            if wire_ranks[left] > wire_ranks[left + 1]:
                wire_ranks[left], wire_ranks[left + 1] = wire_ranks[left + 1], wire_ranks[left]
                layer.append((left, SWAP, "physical_SWAP"))
        if layer:
            layers.append(layer)
    assert wire_ranks == list(range(n))
    return layers, z, permutation


def check(n):
    layers, z, permutation = encoder_layers(n)
    w = [1 - bit for bit in z]
    rail_zero = [j % 2 for j in range(n)]
    rail_one = rail_zero.copy()
    rail_one[:2] = [1, 0]
    input_zero = basis_state(rail_zero)
    input_one = basis_state(rail_one)
    encoded_zero = basis_state(z)
    encoded_one = basis_state(w)
    logical_states = {
        "0": (1, 0, "Z", 1),
        "1": (0, 1, "Z", -1),
        "+": (1 / np.sqrt(2), 1 / np.sqrt(2), "X", 1),
        "-": (1 / np.sqrt(2), -1 / np.sqrt(2), "X", -1),
        "+i": (1 / np.sqrt(2), 1j / np.sqrt(2), "Y", 1),
        "-i": (1 / np.sqrt(2), -1j / np.sqrt(2), "Y", -1),
    }
    basis_rotations = {
        "Z": [],
        "X": [[(0, H_LOGICAL, "logical_H")]],
        "Y": [[(0, S_DAG_LOGICAL, "logical_S_dagger")], [(0, H_LOGICAL, "logical_H")]],
    }
    charge_by_basis = np.array([index.bit_count() for index in range(2**n)])
    z0_by_basis = 1 - 2 * ((np.arange(2**n) >> (n - 1)) & 1)
    results = {}
    for name, (alpha, beta, axis, label) in logical_states.items():
        initial = alpha * input_zero + beta * input_one
        expected = alpha * encoded_zero + beta * encoded_one
        encoded = execute(initial, n, layers)
        decoded = execute(encoded, n, layers, inverse=True)
        readout = execute(decoded, n, basis_rotations[axis])
        results[name] = {
            "encoding_vector_error": float(np.linalg.norm(encoded - expected)),
            "decoding_vector_error": float(np.linalg.norm(decoded - initial)),
            "wrong_charge_probability": float(np.sum(np.abs(encoded[charge_by_basis != n // 2]) ** 2)),
            "readout_expectation_Z0": float(np.sum(np.abs(readout) ** 2 * z0_by_basis).real),
            "expected_label": label,
        }
        assert results[name]["encoding_vector_error"] < 1e-12
        assert results[name]["decoding_vector_error"] < 1e-12
        assert results[name]["wrong_charge_probability"] < 1e-12
        assert abs(results[name]["readout_expectation_Z0"] - label) < 1e-12

    # The same decoder must work without knowing any nuisance bits. Exhaust
    # all nuisance inputs at these two small sizes, including profiles outside
    # the sparse-profile family used by the separate hydrodynamic theorem.
    nuisance_results = []
    m = n // 2
    for nuisance_index in range(2 ** (m - 1)):
        nuisance = [int(bit) for bit in f"{nuisance_index:0{m - 1}b}"]
        rail_bits_zero = [bit for logical in [0] + nuisance for bit in (logical, 1 - logical)]
        rail_bits_one = rail_bits_zero.copy()
        rail_bits_one[:2] = [1, 0]
        cumulative_y = [0]
        for logical in nuisance:
            cumulative_y.append(cumulative_y[-1] ^ logical)
        intermediate_bits = [bit for logical in cumulative_y for bit in (logical, 1 - logical)]
        branch_zero_bits = [0] * n
        for source, target in enumerate(permutation):
            branch_zero_bits[target] = intermediate_bits[source]
        branch_one_bits = [1 - bit for bit in branch_zero_bits]
        input_zero_x = basis_state(rail_bits_zero)
        input_one_x = basis_state(rail_bits_one)
        branch_zero_x = basis_state(branch_zero_bits)
        branch_one_x = basis_state(branch_one_bits)
        encoding_errors, decoding_errors, label_errors = [], [], []
        for _name, (alpha, beta, axis, label) in logical_states.items():
            initial = alpha * input_zero_x + beta * input_one_x
            expected = alpha * branch_zero_x + beta * branch_one_x
            encoded = execute(initial, n, layers)
            decoded = execute(encoded, n, layers, inverse=True)
            readout = execute(decoded, n, basis_rotations[axis])
            encoding_errors.append(float(np.linalg.norm(encoded - expected)))
            decoding_errors.append(float(np.linalg.norm(decoded - initial)))
            label_errors.append(abs(float(np.sum(np.abs(readout) ** 2 * z0_by_basis).real) - label))
        record = {
            "nuisance_x": "".join(map(str, nuisance)),
            "positive_branch_y": "".join(map(str, cumulative_y)),
            "positive_branch_physical_string": "".join(map(str, branch_zero_bits)),
            "control_states_checked": len(logical_states),
            "max_encoding_vector_error": max(encoding_errors),
            "max_decoding_vector_error": max(decoding_errors),
            "max_label_expectation_error": max(label_errors),
        }
        assert record["max_encoding_vector_error"] < 1e-12
        assert record["max_decoding_vector_error"] < 1e-12
        assert record["max_label_expectation_error"] < 1e-12
        nuisance_results.append(record)

    all_gates = [gate for layer in layers for _left, gate, _name in layer]
    max_commutator = max(np.linalg.norm(gate @ LOCAL_CHARGE - LOCAL_CHARGE @ gate) for gate in all_gates)
    max_unitary_error = max(np.linalg.norm(gate.conj().T @ gate - np.eye(4)) for gate in all_gates)
    assert max_commutator == 0
    assert max_unitary_error < 1e-12
    for layer in layers:
        occupied = [site for left, _gate, _name in layer for site in (left, left + 1)]
        assert len(occupied) == len(set(occupied))
        assert len({left % 2 for left, _gate, _name in layer}) == 1

    return {
        "n": n,
        "domain_wall_z": "".join(map(str, z)),
        "native_encoder_depth": len(layers),
        "native_encoder_gate_count": len(all_gates),
        "max_gate_charge_commutator_norm": float(max_commutator),
        "max_gate_unitarity_error": float(max_unitary_error),
        "states": results,
        "all_nuisance_inputs": nuisance_results,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON result path; the checked-in reference is never overwritten by default.",
    )
    args = parser.parse_args()
    result = {
        "description": "Deterministic statevector audit of explicit local U1 dual-rail encoder and inverse decoder; no random-circuit simulation.",
        "checks": [check(4), check(8)],
    }
    if args.output is not None:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
