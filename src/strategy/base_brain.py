"""Base brain module defining the abstract interface for Police strategies."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple

GRID_SIZE = 7

# Directions defined as (dx, dy) offsets
ACTIONS = {
    "STAY": (0, 0),
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}


class BrainBase(ABC):
    """Abstract base class for Police agent decision brains."""

    def __init__(self, grid_size: int = GRID_SIZE):
        self.grid_size = grid_size

    @abstractmethod
    def _pick_move(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Pick a move direction or target coordinate based on current state."""
        pass

    @abstractmethod
    def _decide_move(
        self,
        state: Dict[str, Any],
        barriers: Optional[List[Tuple[Tuple[int, int], Tuple[int, int]]]] = None,
    ) -> Tuple[int, int]:
        """Decide next grid position given current state and barrier constraints."""
        pass

    def is_valid_position(self, pos: Tuple[int, int]) -> bool:
        """Check if position is within bounds of the discrete grid."""
        x, y = pos
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

    def is_path_blocked(
        self,
        from_pos: Tuple[int, int],
        to_pos: Tuple[int, int],
        barriers: Optional[List[Tuple[Tuple[int, int], Tuple[int, int]]]] = None,
    ) -> bool:
        """Check if movement from from_pos to to_pos crosses any barrier."""
        if not barriers:
            return False
        for p1, p2 in barriers:
            if (from_pos == p1 and to_pos == p2) or (from_pos == p2 and to_pos == p1):
                return True
        return False
