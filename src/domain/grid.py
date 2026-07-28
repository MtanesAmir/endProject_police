from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Union, Optional, Set, Iterable

@dataclass(frozen=True)
class GridPos:
    row: int
    col: int

    def to_tuple(self) -> Tuple[int, int]:
        return (self.row, self.col)

    def is_valid(self, grid_size: Union[int, Tuple[int, int]] = 7) -> bool:
        if isinstance(grid_size, int):
            max_r, max_c = grid_size, grid_size
        else:
            max_r, max_c = grid_size
        return 0 <= self.row < max_r and 0 <= self.col < max_c


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    STAY = (0, 0)

    # Aliases
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    WEST = (0, -1)
    EAST = (0, 1)


def legal_moves(
    pos: Union[GridPos, Tuple[int, int]],
    grid_size: Union[int, Tuple[int, int]] = 7,
    barriers: Optional[Iterable[Union[GridPos, Tuple[int, int]]]] = None
) -> List[GridPos]:
    """Returns a list of legal target GridPos positions from current pos.
    
    Orthogonal moves: UP, DOWN, LEFT, RIGHT, STAY.
    Constrained by grid boundaries [0..grid_size-1] and optional barriers.
    """
    if isinstance(pos, tuple):
        pos = GridPos(pos[0], pos[1])

    if isinstance(grid_size, int):
        max_r, max_c = grid_size, grid_size
    else:
        max_r, max_c = grid_size

    barrier_set: Set[Tuple[int, int]] = set()
    if barriers:
        for b in barriers:
            if isinstance(b, GridPos):
                barrier_set.add(b.to_tuple())
            elif isinstance(b, tuple):
                barrier_set.add(b)

    deltas = [
        (0, 0),   # STAY
        (-1, 0),  # UP / NORTH
        (1, 0),   # DOWN / SOUTH
        (0, -1),  # LEFT / WEST
        (0, 1),   # RIGHT / EAST
    ]

    valid_positions: List[GridPos] = []
    for dr, dc in deltas:
        new_r, new_c = pos.row + dr, pos.col + dc
        if 0 <= new_r < max_r and 0 <= new_c < max_c:
            if (new_r, new_c) not in barrier_set:
                valid_positions.append(GridPos(new_r, new_c))

    return valid_positions


class MovementEngine:
    """Movement Engine for managing position state and moves."""
    
    def __init__(self, initial_pos: Union[GridPos, Tuple[int, int]] = GridPos(0, 0), grid_size: Union[int, Tuple[int, int]] = 7):
        if isinstance(initial_pos, tuple):
            initial_pos = GridPos(initial_pos[0], initial_pos[1])
        self.pos = initial_pos
        self.grid_size = grid_size

    def get_position(self) -> GridPos:
        return self.pos

    def preview_move(self, direction: Union[Direction, Tuple[int, int]]) -> GridPos:
        delta = direction.value if isinstance(direction, Direction) else direction
        return GridPos(self.pos.row + delta[0], self.pos.col + delta[1])

    def get_legal_moves(self, barriers: Optional[Iterable[Union[GridPos, Tuple[int, int]]]] = None) -> List[GridPos]:
        return legal_moves(self.pos, self.grid_size, barriers)

    def move(self, direction: Union[Direction, Tuple[int, int]], barriers: Optional[Iterable[Union[GridPos, Tuple[int, int]]]] = None) -> bool:
        target = self.preview_move(direction)
        if target in self.get_legal_moves(barriers):
            self.pos = target
            return True
        return False
