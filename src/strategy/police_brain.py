"""Police strategy decision engine implementing MyPoliceBrain."""

import math
from typing import Any, Dict, List, Optional, Tuple, Set
from src.strategy.base_brain import ACTIONS, GRID_SIZE, BrainBase
from src.strategy.q_learning import QLearningAgent


class MyPoliceBrain(BrainBase):
    """Police strategy brain overriding _pick_move and _decide_move with heuristic & Q-learning support."""

    def __init__(
        self,
        grid_size: int = GRID_SIZE,
        use_q_learning: bool = False,
        q_agent: Optional[QLearningAgent] = None,
    ):
        super().__init__(grid_size=grid_size)
        self.use_q_learning = use_q_learning
        self.q_agent = q_agent or (QLearningAgent() if use_q_learning else None)

    def _manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two grid points."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def _get_target_position(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Determine target position from state (exact thief position or max belief cell)."""
        thief_pos = state.get("thief_pos")
        if thief_pos is not None:
            return thief_pos

        belief_grid = state.get("belief_grid")
        if belief_grid:
            max_prob = -1.0
            best_cell = (self.grid_size // 2, self.grid_size // 2)
            if isinstance(belief_grid, dict):
                for cell, prob in belief_grid.items():
                    if prob > max_prob:
                        max_prob = prob
                        best_cell = cell
                return best_cell
            elif isinstance(belief_grid, list):
                for r in range(len(belief_grid)):
                    for c in range(len(belief_grid[r])):
                        prob = belief_grid[r][c]
                        if prob > max_prob:
                            max_prob = prob
                            best_cell = (c, r)
                return best_cell

        # Default fallback to center of grid
        return (self.grid_size // 2, self.grid_size // 2)

    def _pick_move(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Pick preferred move direction or target coordinate based on Manhattan distance heuristic."""
        police_pos = state.get("police_pos", (0, 0))
        target_pos = self._get_target_position(state)

        dx = target_pos[0] - police_pos[0]
        dy = target_pos[1] - police_pos[1]

        if abs(dx) >= abs(dy) and dx != 0:
            step_x = 1 if dx > 0 else -1
            return (police_pos[0] + step_x, police_pos[1])
        elif dy != 0:
            step_y = 1 if dy > 0 else -1
            return (police_pos[0], police_pos[1] + step_y)

        return police_pos

    def _decide_move(
        self,
        state: Dict[str, Any],
        barriers: Optional[Set[Tuple[int, int]]] = None,
    ) -> Tuple[int, int]:
        """Decide next valid grid position, prioritizing distance minimization to target or Q-learning action."""
        police_pos = state.get("police_pos", (0, 0))
        target_pos = self._get_target_position(state)

        valid_moves: List[Tuple[str, Tuple[int, int]]] = []
        for action_name, (dx, dy) in ACTIONS.items():
            candidate_pos = (police_pos[0] + dx, police_pos[1] + dy)
            if not self.is_valid_position(candidate_pos):
                continue
            if self.is_path_blocked(police_pos, candidate_pos, barriers):
                continue
            valid_moves.append((action_name, candidate_pos))

        if not valid_moves:
            return police_pos

        if self.use_q_learning and self.q_agent is not None:
            state_key = f"{police_pos}_{target_pos}"
            valid_action_names = [name for name, _ in valid_moves]
            chosen_action_name = self.q_agent.choose_action(state_key, valid_action_names)
            for name, pos in valid_moves:
                if name == chosen_action_name:
                    return pos

        # Heuristic decision: minimize Manhattan distance to target position
        best_pos = police_pos
        min_dist = float("inf")
        for _, candidate_pos in valid_moves:
            dist = self._manhattan_distance(candidate_pos, target_pos)
            if dist < min_dist:
                min_dist = dist
                best_pos = candidate_pos

        return best_pos
