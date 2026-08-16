"""Police Bayesian Belief Map Engine (`police_bayesian_belief`)."""

from typing import List, Tuple, Optional, Dict, Any

GRID_SIZE = 7


class BeliefGrid:
    """7x7 Bayesian belief estimator for tracking thief probability distribution."""

    def __init__(self, grid_size: int = GRID_SIZE):
        self.grid_size = grid_size
        self.total_cells = grid_size * grid_size
        self.grid: List[List[float]] = [
            [1.0 / self.total_cells for _ in range(grid_size)] for _ in range(grid_size)
        ]

    def normalize(self) -> None:
        """Normalizes grid matrix probabilities so that sum(b(s)) == 1.0."""
        total_prob = sum(sum(row) for row in self.grid)
        if total_prob > 0.0:
            for r in range(self.grid_size):
                for c in range(self.grid_size):
                    self.grid[r][c] /= total_prob
        else:
            # Fallback to uniform distribution if sum is zero
            uniform_val = 1.0 / self.total_cells
            self.grid = [
                [uniform_val for _ in range(self.grid_size)]
                for _ in range(self.grid_size)
            ]

    def update_belief(self, observation: Any) -> None:
        """Updates belief distribution given an observation (scent matrix or dict).

        Observation can be a 2D scent matrix (List[List[float]]) or dict with 'scent' / 'hint'.
        """
        if isinstance(observation, list):
            self.update_from_scent(observation)
        elif isinstance(observation, dict):
            if "scent" in observation:
                self.update_from_scent(observation["scent"])
            if "hint" in observation:
                hint_info = observation["hint"]
                pos = hint_info.get("position")
                rel = hint_info.get("reliability", 0.8)
                if pos:
                    self.update_from_hint(pos, reliability=rel)
        self.normalize()

    def update_from_scent(self, scent_matrix: List[List[float]]) -> None:
        """Bayes rule update based on scent field intensity observations.

        b_{t+1}(r, c) = P(scent | (r, c)) * b_t(r, c) / P(scent)
        """
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                scent_val = scent_matrix[r][c] if r < len(scent_matrix) and c < len(scent_matrix[r]) else 0.0
                # Likelihood factor: higher scent level -> higher probability of thief presence
                likelihood = 1.0 + 2.0 * scent_val
                self.grid[r][c] *= likelihood
        self.normalize()

    def update_from_hint(
        self, direction: str, reliability: float = 0.8
    ) -> None:
        """Updates probabilities based on opponent verbal direction hint using Bayes' rule."""
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                likelihood = 1.0
                if direction == "N" and r < self.grid_size // 2:
                    likelihood = reliability
                elif direction == "S" and r > self.grid_size // 2:
                    likelihood = reliability
                elif direction == "W" and c < self.grid_size // 2:
                    likelihood = reliability
                elif direction == "E" and c > self.grid_size // 2:
                    likelihood = reliability
                else:
                    likelihood = 1.0 - reliability
                self.grid[r][c] *= likelihood
        self.normalize()

    def detect_bluff(
        self, scent_matrix: List[List[float]], hint_position: Tuple[int, int], threshold: float = 0.10
    ) -> bool:
        """Detects if a verbal hint is a bluff by checking if scent level at hint_position is below threshold."""
        hr, hc = hint_position
        if 0 <= hr < self.grid_size and 0 <= hc < self.grid_size:
            scent_level = scent_matrix[hr][hc]
            return scent_level < threshold
        return True

    def get_most_likely_position(self) -> Tuple[int, int]:
        """Outputs highest probability thief location argmax_s b(s)."""
        max_prob = -1.0
        best_pos = (0, 0)
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] > max_prob:
                    max_prob = self.grid[r][c]
                    best_pos = (r, c)
        return best_pos

    def get_grid(self) -> List[List[float]]:
        """Returns a copy of the 7x7 probability grid."""
        return [row[:] for row in self.grid]

    def reset(self) -> None:
        """Resets belief grid to 7x7 uniform prior distribution."""
        uniform_val = 1.0 / self.total_cells
        self.grid = [
            [uniform_val for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]


# Alias for backward compatibility if referenced as BayesianBeliefMap
BayesianBeliefMap = BeliefGrid
