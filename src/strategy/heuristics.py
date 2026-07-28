from typing import List, Tuple, Union, Optional, Iterable
from src.domain.grid import GridPos
from src.domain.distance import (
    manhattan_distance,
    chebyshev_distance,
    euclidean_distance,
    shortest_path_distance,
    select_closest_move,
)

class DistanceHeuristics:
    @staticmethod
    def manhattan(pos_a: Union[GridPos, Tuple[int, int]], pos_b: Union[GridPos, Tuple[int, int]]) -> int:
        return manhattan_distance(pos_a, pos_b)

    @staticmethod
    def chebyshev(pos_a: Union[GridPos, Tuple[int, int]], pos_b: Union[GridPos, Tuple[int, int]]) -> int:
        return chebyshev_distance(pos_a, pos_b)

    @staticmethod
    def euclidean(pos_a: Union[GridPos, Tuple[int, int]], pos_b: Union[GridPos, Tuple[int, int]]) -> float:
        return euclidean_distance(pos_a, pos_b)

    @staticmethod
    def shortest_path(
        pos_a: Union[GridPos, Tuple[int, int]],
        pos_b: Union[GridPos, Tuple[int, int]],
        grid_size: Union[int, Tuple[int, int]] = 7,
        barriers: Optional[Iterable[Union[GridPos, Tuple[int, int]]]] = None
    ) -> float:
        return shortest_path_distance(pos_a, pos_b, grid_size=grid_size, barriers=barriers)

    @staticmethod
    def select_best_move(
        current_pos: Union[GridPos, Tuple[int, int]],
        target_pos: Union[GridPos, Tuple[int, int]],
        legal_moves_list: List[GridPos],
        barriers: Optional[Iterable[Union[GridPos, Tuple[int, int]]]] = None,
        grid_size: Union[int, Tuple[int, int]] = 7
    ) -> GridPos:
        return select_closest_move(current_pos, target_pos, legal_moves_list, barriers=barriers, grid_size=grid_size)
