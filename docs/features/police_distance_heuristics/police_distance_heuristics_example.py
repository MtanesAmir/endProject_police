"""Example demonstrating Manhattan distance calculation and directional heuristics."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.distance import manhattan_distance, select_closest_move
from src.domain.grid import GridPos

def main():
    pos_cop = (0, 0)
    pos_target = (3, 3)
    dist = manhattan_distance(pos_cop, pos_target)
    print(f"Manhattan distance between {pos_cop} and {pos_target}: {dist}")
    best_move = select_closest_move(current_pos=pos_cop, target_pos=pos_target, legal_moves_list=[GridPos(0, 1), GridPos(1, 0)])
    print(f"Optimal heuristic step towards target: {best_move}")

if __name__ == "__main__":
    main()
