"""Thief Brain Strategy Module for Thief agent evasion and deception."""

from typing import Dict, Any, List, Tuple, Optional
import random

from src.strategy.base_brain import BrainBase
from src.domain.distance import manhattan_distance
from src.domain.grid import legal_moves


class ThiefBrain(BrainBase):
    """Thief Evasion and Deception Brain strategy implementation."""

    def __init__(self, start_pos: Tuple[int, int] = (3, 3), grid_size: int = 7):
        super().__init__(grid_size=grid_size)
        self.position = start_pos
        self.cop_position_estimate = (0, 0)

    def _pick_move(self, state: Dict[str, Any], valid_moves: Optional[List[Tuple[int, int]]] = None) -> Tuple[int, int]:
        """Select move that maximizes distance from Cop's estimated position."""
        cop_pos = state.get("cop_position", self.cop_position_estimate)
        self.cop_position_estimate = cop_pos

        if not valid_moves:
            valid_positions = [p.to_tuple() for p in legal_moves(self.position, grid_size=self.grid_size)]
        else:
            valid_positions = valid_moves

        if not valid_positions:
            return self.position

        best_move = valid_positions[0]
        max_dist = -1

        for move in valid_positions:
            dist = manhattan_distance(move, cop_pos)
            if dist > max_dist:
                max_dist = dist
                best_move = move

        self.position = best_move
        return best_move

    def _decide_move(
        self,
        state: Dict[str, Any],
        barriers: Optional[List[Tuple[Tuple[int, int], Tuple[int, int]]]] = None,
    ) -> Tuple[int, int]:
        """Decide next grid position given state and barrier constraints."""
        valid_positions = [p.to_tuple() for p in legal_moves(self.position, grid_size=self.grid_size)]
        return self._pick_move(state, valid_moves=valid_positions)

    def _decide_bluff(self, state: Dict[str, Any], chosen_move: Tuple[int, int]) -> str:
        """Generate deceptive verbal direction hint to mislead Police belief grid."""
        directions = ["N", "S", "E", "W"]
        deceptive_dir = random.choice(directions)
        return f"I moved {deceptive_dir}"
