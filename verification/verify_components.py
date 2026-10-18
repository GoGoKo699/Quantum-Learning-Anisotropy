"""Finite checks for the transport/coherence gradient theorem.

These checks examine exact finite-dimensional identities and bound constants.
They do not establish asymptotic scaling or literature novelty.
"""
import itertools
import json
import math
from collections import Counter
import numpy as np
from circuit_utils import apply_two, haar_u1, evolve, random_layers


def matching(q, parity):
    n = len(q)
    r = q.copy()
    for j in range(parity, n + parity, 2):
        a, b = j % n, (j + 1) % n
        r[a] = r[b] = (q[a] + q[b]) / 2
    return r


def wall(n):
    a = n // 4
    q = -np.ones(n)
    q[(np.arange(n // 2) + a + 1) % n] = 1
    f = np.sin(2 * np.pi * (np.arange(n) - a - .5) / n)
    return q, f, a


def harmonic_and_schedule_checks():
    max_error = 0.
    total = 0
    for n in (8, 12, 16, 32):
        q, f, a = wall(n)
        avoiding = 1 - a % 2
        m0 = 2 / np.sin(np.pi / n)
        c = np.cos(2 * np.pi / n)
        assert np.max(np.abs(matching(q, avoiding) - q)) == 0
        for depth in range(1, 9):
            counts = Counter()
            for schedule in itertools.product((0, 1), repeat=depth):
                profile = q.copy()
                for parity in schedule:
                    profile = matching(profile, parity)
                nu = int(schedule[0] != avoiding)
                nu += sum(x != y for x, y in zip(schedule, schedule[1:]))
                counts[nu] += 1
                predicted = m0 * c ** nu
                error = abs(np.dot(f, profile) - predicted)
                max_error = max(max_error, error)
                assert error < 2e-12 * n
                total += 1
            assert [counts[k] for k in range(depth + 1)] == [
                math.comb(depth, k) for k in range(depth + 1)]
    return {"enumerated_schedule_instances": total,
            "max_harmonic_identity_absolute_error": max_error,
            "binomial_switch_count_exact": True}



def tangent_basis():
    i2 = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], complex)
    y = np.array([[0, -1j], [1j, 0]], complex)
    z = np.diag([1., -1.]).astype(complex)
    return [np.eye(4, dtype=complex), np.kron(z, i2), np.kron(i2, z),
            np.kron(z, z), (np.kron(x, x)+np.kron(y, y))/2,
            (np.kron(x, y)-np.kron(y, x))/2]


def basis_and_conditional_density_checks():
    basis = tangent_basis()
    charge = np.diag([0., 1., 1., 2.])
    for h in basis:
        assert np.linalg.norm(h @ charge-charge @ h) < 1e-14
        assert np.max(np.abs(np.linalg.eigvalsh(h))) <= 1 + 1e-14
        assert np.max(np.abs(np.linalg.eigvalsh(h)-np.rint(np.linalg.eigvalsh(h)))) < 1e-14
    real_vectors = np.stack([np.r_[h.real.ravel(), h.imag.ravel()] for h in basis])
    assert np.linalg.matrix_rank(real_vectors) == 6
    rng = np.random.default_rng(260018)
    h = basis[4]
    sigma_y = np.array([[0, -1j], [1j, 0]])
    sigma_z = np.diag([1., -1.])
    max_error = 0.
    for _ in range(50):
        probs = rng.dirichlet(np.ones(4))
        rho = np.diag(probs)
        b = rng.normal(size=2)
        observable = b[0] * basis[1] + b[1] * basis[2]
        g = haar_u1(rng)
        direct = np.trace((g @ rho @ g.conj().T)
                          @ (1j * (h @ observable-observable @ h))).real
        block = g[1:3, 1:3]
        ny = np.trace(sigma_y @ block @ sigma_z @ block.conj().T).real / 2
        dq = 2 * (probs[1]-probs[2])
        predicted = dq * (b[0]-b[1]) * ny
        max_error = max(max_error, abs(direct-predicted))
        assert abs(direct-predicted) < 1e-12
    return {"lie_algebra_rank": 6,
            "all_generators_charge_preserving_norm_one_integer_spectrum": True,
            "max_conditional_density_gradient_error": max_error}


def quantum_projection_and_parseval_checks():
    rng = np.random.default_rng(20261802)
    n = 8
    q, f, a = wall(n)
    bits = ((1-q)/2).astype(int)
    z_index = int("".join(map(str, bits)), 2)
    zbar_index = (2**n-1) ^ z_index
    ket_z = np.zeros(2**n, complex)
    ket_bar = ket_z.copy()
    ket_z[z_index] = 1
    ket_bar[zbar_index] = 1
    labels = np.arange(2**n)
    all_bits = ((labels[:, None] >> np.arange(n-1, -1, -1)) & 1)
    z0 = 1-2*all_bits[:, 0]
    statistic = (1-2*all_bits) @ f
    positive = statistic > 0
    worst_projector_excess = -np.inf
    worst_parseval_excess = -np.inf
    max_four_shift_error = 0.
    cases = 0
    basis = tangent_basis()
    for depth in (2, 5, 12):
        gates = random_layers(rng, n, depth)
        for h in (basis[1], basis[4], basis[5]):
            mark = int(rng.integers(len(gates)))
            site_a, site_b, g = gates[mark]
            before_z = evolve(ket_z, gates[:mark], n)
            before_bar = evolve(ket_bar, gates[:mark], n)
            vals, vecs = np.linalg.eigh(h)
            def evaluate(theta):
                r = (vecs*np.exp(-1j*theta*vals)) @ vecs.conj().T
                marked_gate = r @ g
                after_z = apply_two(before_z, marked_gate, site_a, site_b, n)
                after_bar = apply_two(before_bar, marked_gate, site_a, site_b, n)
                dz = -1j*apply_two(after_z, h, site_a, site_b, n)
                db = -1j*apply_two(after_bar, h, site_a, site_b, n)
                oz = evolve(after_z, gates[mark+1:], n)
                ob = evolve(after_bar, gates[mark+1:], n)
                odz = evolve(dz, gates[mark+1:], n)
                odb = evolve(db, gates[mark+1:], n)
                cross = np.vdot(oz, z0*ob)
                cross_derivative = np.vdot(odz, z0*ob)+np.vdot(oz, z0*odb)
                error = np.sum(np.abs(oz[~positive])**2)+np.sum(np.abs(ob[positive])**2)
                return cross, -.5*cross_derivative.real, error
            cross2, grad2 = [], []
            for angle in 2*np.pi*np.arange(16)/16:
                cross, grad, err = evaluate(angle)
                excess = abs(cross)**2-2*err
                worst_projector_excess = max(worst_projector_excess, excess)
                assert excess <= 1e-12
                cross2.append(abs(cross)**2)
                grad2.append(grad**2)
            excess = np.mean(grad2)-np.mean(cross2)
            worst_parseval_excess = max(worst_parseval_excess, excess)
            assert excess <= 1e-12
            angle = .317
            coefficient = (1-np.sqrt(2))/2
            def signal(t):
                return .5-.5*evaluate(t)[0].real
            shifted = (signal(angle+np.pi/4)-signal(angle-np.pi/4)
                       +coefficient*(signal(angle+np.pi/2)-signal(angle-np.pi/2)))
            error = abs(evaluate(angle)[1]-shifted)
            max_four_shift_error = max(max_four_shift_error, error)
            assert error < 1e-12
            cases += 1
    return {"n": n, "circuit_and_generator_cases": cases,
            "angle_grid_points_per_case": 16,
            "maximum_projector_inequality_excess": worst_projector_excess,
            "maximum_parseval_inequality_excess": worst_parseval_excess,
            "maximum_four_shift_gradient_error": max_four_shift_error}


if __name__ == "__main__":
    print(json.dumps({
        "scope": "Finite component checks, not an asymptotic proof",
        "harmonic_schedule": harmonic_and_schedule_checks(),
        "native_tangents": basis_and_conditional_density_checks(),
        "quantum_bounds": quantum_projection_and_parseval_checks()
    }, indent=2))

