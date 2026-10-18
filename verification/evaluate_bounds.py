"""Evaluate the proved scalar bounds, without simulating quantum circuits."""
import json
import math


def logaddexp(a, b):
    largest = max(a, b)
    return largest + math.log1p(math.exp(min(a, b) - largest))


def evaluate(n):
    if n < 8 or n % 4:
        raise ValueError("n must be a multiple of four and at least eight")
    # These sizes make n^2/8 an integer. Integer arithmetic keeps D exact.
    depth = (n * n + 7) // 8
    assert depth - 1 >= math.ceil(n * n / math.pi**2)
    m = n // 2
    p = (m // 8) / (m - 1)
    beta = 2 / math.pi - 1 / 4
    m_star = max(beta * n - math.pi, 0)
    sin_squared = math.sin(math.pi / n) ** 2
    log_lambda = math.log1p(-sin_squared)
    log_c = math.log1p(-2 * sin_squared)
    r_depth = depth / 2 + math.sqrt(n * depth)
    concentration_exponent = (
        m_star**2 / (8 * n) * math.exp(2 * r_depth * log_c)
    )
    log_density_lower = (
        math.log(8 / 3)
        + 2 * math.log1p(-2 * p)
        - 4 * math.log(n)
        + 2 * (depth - 1) * log_lambda
    )
    log_coordinates = math.log(3 * n * depth)
    log_phase_upper = log_coordinates + min(
        0,
        logaddexp(math.log(4) - concentration_exponent, -2 * n),
    )
    return {
        "n": n,
        "depth": depth,
        "log10_density_energy_lower": log_density_lower / math.log(10),
        "log10_phase_energy_upper": log_phase_upper / math.log(10),
        "log10_upper_to_lower_ratio": (
            log_phase_upper - log_density_lower
        ) / math.log(10),
        "concentration_exponent": concentration_exponent,
    }


def evaluate_bounds():
    return {
        "scope": "Evaluation of analytic inequalities; no circuit simulation or fitted scaling.",
        "depth_rule": "D = ceil(n^2/8)",
        "source": "Fixed-weight nuisance source in science/model.md",
        "rows": [evaluate(n) for n in (256, 1024, 4096, 16384, 65536)],
    }


if __name__ == "__main__":
    print(json.dumps(evaluate_bounds(), indent=2))
