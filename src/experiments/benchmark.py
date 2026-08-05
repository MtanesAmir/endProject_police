"""Benchmark script for running automated Monte Carlo match simulations."""

import os
import json
import time
from typing import Dict, Any, List

from src.core.match_runner import MatchRunner


def run_benchmark_suite(num_matches: int = 10, grid_size: int = 7) -> Dict[str, Any]:
    """Execute automated Monte Carlo benchmark suite across Cop vs Thief strategies."""
    results: List[Dict[str, Any]] = []

    for match_id in range(1, num_matches + 1):
        runner = MatchRunner(grid_size=grid_size, max_turns=35)
        summary = runner.run_match()
        results.append({
            "match_id": match_id,
            "outcome": summary.get("outcome"),
            "total_turns": summary.get("total_turns"),
        })

    cop_wins = sum(1 for r in results if r["outcome"] == "COP_WIN")
    thief_wins = sum(1 for r in results if r["outcome"] == "THIEF_WIN")
    mean_turns = sum(r["total_turns"] for r in results) / len(results) if results else 0

    benchmark_summary = {
        "num_matches": num_matches,
        "grid_size": grid_size,
        "cop_wins": cop_wins,
        "thief_wins": thief_wins,
        "mean_turns": mean_turns,
        "matches": results,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    os.makedirs("results", exist_ok=True)
    os.makedirs("assets", exist_ok=True)

    with open("results/benchmark_summary.json", "w", encoding="utf-8") as f:
        json.dump(benchmark_summary, f, indent=2)

    return benchmark_summary


if __name__ == "__main__":
    summary = run_benchmark_suite(num_matches=5)
    print(f"[BENCHMARK] Completed {summary['num_matches']} matches.")
    print(f"Cop Wins: {summary['cop_wins']}, Thief Wins: {summary['thief_wins']}, Mean Turns: {summary['mean_turns']}")
