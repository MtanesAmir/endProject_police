"""Example snippet for generating strategy comparison plots."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

def sample_decay_calculation(initial_intensity: float, decay_rate: float, steps: int):
    values = []
    intensity = initial_intensity
    for _ in range(steps):
        values.append(round(intensity, 4))
        intensity = max(0.0, intensity * (1.0 - decay_rate))
    return values

if __name__ == "__main__":
    decay_curve = sample_decay_calculation(0.9, 0.1, 5)
    print(f"[Plot Helper] Sample decay progression over 5 steps: {decay_curve}")
