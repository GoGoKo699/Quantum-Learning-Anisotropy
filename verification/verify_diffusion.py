"""Finite Fourier identities and the readout lower bound; no scaling inference."""
import json
import math
import numpy as np


def fourier_checks():
    rows = []
    min_ratio = float("inf")
    max_relative_error = 0.0
    for n in (8, 12, 16, 24, 32, 64, 128, 256):
        a = n // 4
        q = -np.ones(n)
        q[(np.arange(n // 2) + a + 1) % n] = 1
        k = np.arange(n)
        lam = np.cos(np.pi * k / n) ** 2
        base = math.ceil(n * n / np.pi ** 2)
        for mult in (1, 2, 4):
            depth = base * mult
            # Remove the constant mode before taking differences to avoid
            # cancellation against the stationary component.
            eig = lam ** depth
            eig[0] = 0
            kernel = np.fft.ifft(eig).real
            evolved = np.fft.ifft(np.fft.fft(q) * eig).real
            exact_q = -4 / n * np.sum(lam[1::2] ** depth)
            actual_q = evolved[a] - evolved[(a + 1) % n]
            max_relative_error = max(max_relative_error, abs(actual_q - exact_q) / abs(exact_q))
            actual_b = kernel[a] - kernel[(a + 1) % n]
            claimed_b = 2 / n * np.sin(np.pi / n) * lam[1] ** depth
            ratio = actual_b / claimed_b
            min_ratio = min(min_ratio, ratio)
            assert ratio >= 1 - 1e-10, (n, depth, ratio)
            assert abs(actual_q - exact_q) <= 1e-10 * abs(exact_q)
        rows.append({"n": n, "base_depth": base})
    return {"sizes_and_depths": rows, "minimum_readout_bound_ratio": min_ratio,
            "maximum_relative_domain_wall_identity_error": max_relative_error}

if __name__ == "__main__":
    print(json.dumps(fourier_checks(), indent=2))
