"""Example snippet for generating experiment analysis plots."""

import os
from typing import Dict, Any


def generate_example_scent_decay_data(turns: int = 20, rho: float = 0.10) -> list:
    """Simulate scent decay intensity values over time."""
    intensity = 0.9
    data = [intensity]
    for _ in range(1, turns):
        intensity = max(0.0, (1 - rho) * intensity)
        data.append(round(intensity, 4))
    return data


if __name__ == "__main__":
    decay_curve = generate_example_scent_decay_data()
    print("[Plotter Example] Generated Scent Decay Intensity Curve (turns 1-20):")
    print(decay_curve)
