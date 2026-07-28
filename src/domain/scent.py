"""Police Scent Field & Stigmergic Trail Tracker (`police_scent_tracking`)."""

import math
from typing import List, Tuple

GRID_SIZE = 7
DEFAULT_TAU_CENTER = 0.90
DEFAULT_RHO = 0.10


class ScentTracker:
    """Tracks scent field grid over a 7x7 discrete game board."""

    def __init__(self, grid_size: int = GRID_SIZE):
        self.grid_size = grid_size
        self.matrix: List[List[float]] = [
            [0.0 for _ in range(grid_size)] for _ in range(grid_size)
        ]

    def apply_emission(
        self, center_pos: Tuple[int, int], tau_center: float = DEFAULT_TAU_CENTER
    ) -> None:
        """Emits scent centered at center_pos with a 5x5 radial distribution field."""
        r_c, c_c = center_pos
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                r = r_c + dr
                c = c_c + dc
                if 0 <= r < self.grid_size and 0 <= c < self.grid_size:
                    dist = math.sqrt(dr * dr + dc * dc)
                    intensity = tau_center / (1.0 + dist)
                    self.matrix[r][c] += intensity

    def apply_decay(self, rho: float = DEFAULT_RHO) -> None:
        """Applies global per-turn scent decay rate rho (e.g. rho=0.10 => 90% retention).

        Formula: tau_{ij}(t+1) = max(0, (1 - rho) * tau_{ij}(t))
        """
        retention = 1.0 - rho
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                self.matrix[r][c] = max(0.0, retention * self.matrix[r][c])

    def get_scent_level(self, pos: Tuple[int, int]) -> float:
        """Returns scent intensity level at given position (r, c)."""
        r, c = pos
        if 0 <= r < self.grid_size and 0 <= c < self.grid_size:
            return self.matrix[r][c]
        return 0.0

    def get_matrix(self) -> List[List[float]]:
        """Exposes scent matrix data (e.g. for Bayesian belief engine)."""
        return [row[:] for row in self.matrix]

    def reset(self) -> None:
        """Resets all scent intensity values in matrix to 0.0."""
        self.matrix = [
            [0.0 for _ in range(self.grid_size)] for _ in range(self.grid_size)
        ]
