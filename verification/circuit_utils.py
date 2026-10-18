"""Small statevector utilities for the stated conserving matching ensemble."""
import numpy as np


def haar_u1(rng):
    z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q @ np.diag(d / np.abs(d))
    out = np.zeros((4, 4), complex)
    out[0, 0], out[3, 3] = np.exp(2j * np.pi * rng.random(2))
    out[1:3, 1:3] = q
    return out


def apply_two(state, gate, a, b, n):
    axes = [a, b] + [j for j in range(n) if j not in (a, b)]
    permuted = state.reshape([2] * n).transpose(axes).reshape(4, -1)
    result = (gate @ permuted).reshape([2] * n).transpose(np.argsort(axes))
    return result.reshape(-1)


def random_layers(rng, n, depth):
    layers = []
    for _ in range(depth):
        parity = int(rng.integers(2))
        for i in range(parity, n + parity, 2):
            layers.append((i % n, (i + 1) % n, haar_u1(rng)))
    return layers


def evolve(state, layers, n):
    for a, b, u in layers:
        state = apply_two(state, u, a, b, n)
    return state
