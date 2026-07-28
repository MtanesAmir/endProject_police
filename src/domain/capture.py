from typing import Tuple, Union, Optional, Iterable, Set
from src.domain.grid import GridPos, legal_moves
from src.domain.distance import manhattan_distance, chebyshev_distance

PositionInput = Union[GridPos, Tuple[int, int]]

COP_CAPTURE_SCORE = 20
THIEF_CAPTURE_SCORE = 5

def _to_grid_pos(pos: PositionInput) -> GridPos:
    if isinstance(pos, tuple):
        return GridPos(pos[0], pos[1])
    return pos

def check_capture(
    police_pos: PositionInput,
    thief_pos: PositionInput,
    radius: int = 1
) -> bool:
    """Returns True if police_pos is within radius of thief_pos.
    Radius 0: exact same cell (direct capture).
    Radius 1: same cell or adjacent (distance <= 1).
    """
    p_pos, t_pos = _to_grid_pos(police_pos), _to_grid_pos(thief_pos)
    # Check Manhattan or Chebyshev distance <= radius
    return manhattan_distance(p_pos, t_pos) <= radius or chebyshev_distance(p_pos, t_pos) <= radius

class CaptureDetector:
    COP_CAPTURE_SCORE: int = COP_CAPTURE_SCORE
    THIEF_CAPTURE_SCORE: int = THIEF_CAPTURE_SCORE

    @staticmethod
    def check_direct_capture(
        cop_pos: PositionInput,
        thief_pos: PositionInput,
        radius: int = 0
    ) -> bool:
        """Direct collision check (cop_pos == thief_pos if radius == 0)."""
        p_pos, t_pos = _to_grid_pos(cop_pos), _to_grid_pos(thief_pos)
        if radius == 0:
            return p_pos == t_pos
        return check_capture(p_pos, t_pos, radius=radius)

    @staticmethod
    def check_trapped_capture(
        thief_pos: PositionInput,
        barriers: Optional[Iterable[PositionInput]] = None,
        grid_size: Union[int, Tuple[int, int]] = 7
    ) -> bool:
        """Returns True if thief has no non-STAY legal moves available due to surrounding barriers or boundaries."""
        t_pos = _to_grid_pos(thief_pos)
        moves = legal_moves(t_pos, grid_size=grid_size, barriers=barriers)
        # Moves list includes STAY (t_pos itself) if valid. Filter out STAY to check if moving away is impossible.
        non_stay_moves = [m for m in moves if m != t_pos]
        return len(non_stay_moves) == 0

    @staticmethod
    def check_capture(
        police_pos: PositionInput,
        thief_pos: PositionInput,
        radius: int = 1
    ) -> bool:
        return check_capture(police_pos, thief_pos, radius=radius)
