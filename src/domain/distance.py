import math
from collections import deque
from typing import List, Tuple, Union, Optional, Set, Iterable
from src.domain.grid import GridPos

PositionInput = Union[GridPos, Tuple[int, int]]

def _to_grid_pos(pos: PositionInput) -> GridPos:
    if isinstance(pos, tuple):
        return GridPos(pos[0], pos[1])
    return pos

def manhattan_distance(pos_a: PositionInput, pos_b: PositionInput) -> int:
    pa, pb = _to_grid_pos(pos_a), _to_grid_pos(pos_b)
    return abs(pa.row - pb.row) + abs(pa.col - pb.col)

def chebyshev_distance(pos_a: PositionInput, pos_b: PositionInput) -> int:
    pa, pb = _to_grid_pos(pos_a), _to_grid_pos(pos_b)
    return max(abs(pa.row - pb.row), abs(pa.col - pb.col))

def euclidean_distance(pos_a: PositionInput, pos_b: PositionInput) -> float:
    pa, pb = _to_grid_pos(pos_a), _to_grid_pos(pos_b)
    return math.sqrt((pa.row - pb.row) ** 2 + (pa.col - pb.col) ** 2)

def shortest_path_distance(
    pos_a: PositionInput,
    pos_b: PositionInput,
    grid_size: Union[int, Tuple[int, int]] = 7,
    barriers: Optional[Iterable[PositionInput]] = None
) -> float:
    """Calculates shortest path distance using BFS with barrier avoidance.
    Returns float('inf') if no path exists.
    """
    start, target = _to_grid_pos(pos_a), _to_grid_pos(pos_b)
    if start == target:
        return 0.0

    if isinstance(grid_size, int):
        max_r, max_c = grid_size, grid_size
    else:
        max_r, max_c = grid_size

    barrier_set: Set[Tuple[int, int]] = set()
    if barriers:
        for b in barriers:
            gb = _to_grid_pos(b)
            barrier_set.add(gb.to_tuple())

    # Target itself must not be impassable unless target == start
    if target.to_tuple() in barrier_set:
        return float('inf')

    queue = deque([(start.row, start.col, 0)])
    visited = {(start.row, start.col)}

    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (target.row, target.col):
            return float(dist)

        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if 0 <= nr < max_r and 0 <= nc < max_c:
                if (nr, nc) not in visited and (nr, nc) not in barrier_set:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return float('inf')

def select_closest_move(
    current_pos: PositionInput,
    target_pos: PositionInput,
    legal_moves_list: List[GridPos],
    barriers: Optional[Iterable[PositionInput]] = None,
    grid_size: Union[int, Tuple[int, int]] = 7
) -> GridPos:
    """Selects move from legal_moves_list that minimizes distance to target_pos.
    Uses shortest_path_distance if barriers present, else manhattan_distance.
    """
    if not legal_moves_list:
        return _to_grid_pos(current_pos)

    best_move = legal_moves_list[0]
    best_dist = float('inf')

    for move in legal_moves_list:
        if barriers:
            dist = shortest_path_distance(move, target_pos, grid_size=grid_size, barriers=barriers)
        else:
            dist = manhattan_distance(move, target_pos)

        if dist < best_dist:
            best_dist = dist
            best_move = move

    return best_move
