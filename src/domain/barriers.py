from typing import Set, Tuple, Union, Optional, Iterable
from src.domain.grid import GridPos
from src.domain.distance import manhattan_distance, chebyshev_distance

PositionInput = Union[GridPos, Tuple[int, int]]

def _to_grid_pos(pos: PositionInput) -> GridPos:
    if isinstance(pos, tuple):
        return GridPos(pos[0], pos[1])
    return pos

class BarrierManager:
    """Manages placement and tracking of physical barriers on the grid."""

    def __init__(self, max_barriers: int = 14, grid_size: Union[int, Tuple[int, int]] = 7):
        self.max_barriers = max_barriers
        if isinstance(grid_size, int):
            self.max_r, self.max_c = grid_size, grid_size
        else:
            self.max_r, self.max_c = grid_size
        self._barriers: Set[Tuple[int, int]] = set()

    @property
    def remaining_barriers(self) -> int:
        return self.max_barriers - len(self._barriers)

    def is_blocked(self, pos: PositionInput) -> bool:
        gp = _to_grid_pos(pos)
        return gp.to_tuple() in self._barriers

    def get_barriers(self) -> Set[GridPos]:
        return {GridPos(r, c) for r, c in self._barriers}

    def place_barrier(
        self,
        barrier_pos: PositionInput,
        police_pos: Optional[PositionInput] = None,
        occupied_positions: Optional[Iterable[PositionInput]] = None
    ) -> bool:
        """Places a physical barrier at barrier_pos if allowed.
        
        Validation rules:
        1. Remaining barrier quota > 0.
        2. barrier_pos is within grid boundaries.
        3. If police_pos specified, distance between police_pos and barrier_pos must be <= 1.
        4. barrier_pos is not already blocked or occupied by entities.
        """
        if self.remaining_barriers <= 0:
            return False

        b_pos = _to_grid_pos(barrier_pos)
        if not (0 <= b_pos.row < self.max_r and 0 <= b_pos.col < self.max_c):
            return False

        if self.is_blocked(b_pos):
            return False

        if police_pos is not None:
            p_pos = _to_grid_pos(police_pos)
            # Distance 1 constraint (adjacent or same cell, but not same as police pos)
            dist = chebyshev_distance(p_pos, b_pos)
            if dist > 1 or b_pos == p_pos:
                return False

        if occupied_positions:
            occ_set = {_to_grid_pos(op).to_tuple() for op in occupied_positions}
            if b_pos.to_tuple() in occ_set:
                return False

        self._barriers.add(b_pos.to_tuple())
        return True
