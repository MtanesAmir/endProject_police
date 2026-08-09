"""Example snippet for benchmark experimentation and analytics recording."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

def record_experiment_trial(trial_id: int, winner: str, turns: int, cop_score: int, thief_score: int):
    return {
        "trial": trial_id,
        "winner": winner,
        "turns": turns,
        "cop_score": cop_score,
        "thief_score": thief_score
    }

if __name__ == "__main__":
    result = record_experiment_trial(1, "police", 14, 20, 5)
    print(f"[Experiment Benchmark] Recorded trial outcome: {result}")
