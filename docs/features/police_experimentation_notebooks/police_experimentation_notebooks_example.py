"""Example experiment script for police_experimentation_notebooks feature."""

import json
import time


def run_experiment_benchmark(num_trials: int = 10, decay_rate: float = 0.10) -> dict:
    """Run benchmark simulation evaluating scent decay rate and game survival."""
    results = []
    for trial in range(num_trials):
        # Simulated steps to capture / end of match
        steps = 15 + (trial % 10)
        captured = steps < 35
        results.append({
            "trial": trial + 1,
            "decay_rate": decay_rate,
            "steps": steps,
            "outcome": "COP_WIN" if captured else "THIEF_WIN"
        })

    summary = {
        "num_trials": num_trials,
        "decay_rate": decay_rate,
        "mean_steps": sum(r["steps"] for r in results) / num_trials,
        "cop_wins": sum(1 for r in results if r["outcome"] == "COP_WIN"),
        "thief_wins": sum(1 for r in results if r["outcome"] == "THIEF_WIN"),
        "trials": results
    }
    return summary


if __name__ == "__main__":
    benchmark_data = run_experiment_benchmark(num_trials=5, decay_rate=0.10)
    print(f"[Benchmark Example] Completed {benchmark_data['num_trials']} trial runs.")
    print(f"Mean Steps: {benchmark_data['mean_steps']}, Cop Wins: {benchmark_data['cop_wins']}")
