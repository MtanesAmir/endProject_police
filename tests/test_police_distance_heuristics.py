import math
import pytest
from src.domain.grid import GridPos, legal_moves
from src.domain.distance import (
    manhattan_distance,
    chebyshev_distance,
    euclidean_distance,
    shortest_path_distance,
    select_closest_move,
)
from src.strategy.heuristics import DistanceHeuristics

def test_manhattan_distance():
    assert manhattan_distance((0, 0), (6, 6)) == 12
    assert manhattan_distance(GridPos(0, 0), GridPos(0, 0)) == 0
    assert manhattan_distance(GridPos(1, 3), GridPos(4, 1)) == 5

def test_chebyshev_distance():
    assert chebyshev_distance((0, 0), (6, 6)) == 6
    assert chebyshev_distance(GridPos(1, 5), GridPos(4, 2)) == 3
    assert chebyshev_distance(GridPos(3, 3), GridPos(3, 3)) == 0

def test_euclidean_distance():
    assert euclidean_distance((0, 0), (3, 4)) == 5.0
    assert euclidean_distance(GridPos(0, 0), GridPos(0, 0)) == 0.0
    assert math.isclose(euclidean_distance(GridPos(1, 1), GridPos(4, 5)), 5.0)

def test_shortest_path_distance_no_barriers():
    assert shortest_path_distance((0, 0), (6, 6), grid_size=7) == 12.0
    assert shortest_path_distance((0, 0), (0, 0), grid_size=7) == 0.0

def test_shortest_path_distance_with_barriers():
    # Barrier blocking direct path (0,1) -> (2,1), barrier at (1,1)
    barriers = [(1, 1)]
    dist = shortest_path_distance((0, 1), (2, 1), grid_size=7, barriers=barriers)
    assert dist == 4.0  # (0,1) -> (0,0) -> (1,0) -> (2,0) -> (2,1) or via col 2

def test_shortest_path_unreachable():
    # Enclose target (1,1) with barriers
    barriers = [(0, 1), (1, 0), (2, 1), (1, 2)]
    dist = shortest_path_distance((0, 0), (1, 1), grid_size=7, barriers=barriers)
    assert math.isinf(dist)

def test_select_closest_move():
    pos = GridPos(0, 0)
    target = GridPos(6, 6)
    moves = legal_moves(pos, grid_size=7)
    # Available moves from (0,0): (0,0), (1,0), (0,1)
    best = select_closest_move(pos, target, moves)
    # Moving to (1,0) or (0,1) reduces manhattan distance to 11
    assert best in [GridPos(1, 0), GridPos(0, 1)]

def test_select_closest_move_with_barrier():
    pos = GridPos(1, 1)
    target = GridPos(3, 1)
    # Barrier at (2,1) - directly down
    barriers = [GridPos(2, 1)]
    moves = legal_moves(pos, grid_size=7, barriers=barriers)
    best = select_closest_move(pos, target, moves, barriers=barriers)
    # Best step should move around barrier e.g. (1,0) or (1,2)
    assert best in [GridPos(1, 0), GridPos(1, 2)]

def test_distance_heuristics_wrapper():
    assert DistanceHeuristics.manhattan((0, 0), (3, 3)) == 6
    assert DistanceHeuristics.chebyshev((0, 0), (3, 3)) == 3
    assert math.isclose(DistanceHeuristics.euclidean((0, 0), (3, 4)), 5.0)
    assert DistanceHeuristics.shortest_path((0, 0), (2, 0), grid_size=7) == 2.0
