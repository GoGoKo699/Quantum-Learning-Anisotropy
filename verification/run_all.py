"""Run the finite verification suite and save its complete measured output."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import platform

import numpy as np

from evaluate_bounds import evaluate_bounds
from verify_components import (
    basis_and_conditional_density_checks,
    harmonic_and_schedule_checks,
    quantum_projection_and_parseval_checks,
)
from verify_diffusion import fourier_checks
from verify_encoder import check as check_encoder


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "latest.json",
        help="Complete result path (default: verification/results/latest.json).",
    )
    args = parser.parse_args()
    result = {
        "status": "passed",
        "scope": "Finite verification of identities and constructions; not an asymptotic or novelty proof.",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "utc_time": datetime.now(timezone.utc).isoformat(),
        },
        "harmonic_schedule": harmonic_and_schedule_checks(),
        "native_tangents": basis_and_conditional_density_checks(),
        "quantum_bounds": quantum_projection_and_parseval_checks(),
        "fourier_bounds": fourier_checks(),
        "encoder_decoder": [check_encoder(4), check_encoder(8)],
        "analytic_bound_evaluation": evaluate_bounds(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PASS: all finite identity and construction assertions.")
    print("PASS: analytic bounds evaluated in their stated domain.")
    print(f"Complete output: {args.output}")


if __name__ == "__main__":
    main()
