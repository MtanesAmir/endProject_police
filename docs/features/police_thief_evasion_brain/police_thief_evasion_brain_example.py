"""Example implementation snippet for ThiefBrain strategy module."""

from typing import Tuple, List, Dict, Any
import random


class ThiefBrainExample:
    """Simplified Thief evasion strategy brain example."""

    def __init__(self, start_pos: Tuple[int, int] = (3, 3)):
        self.position = start_pos
        self.cop_position_estimate = (0, 0)
        self.move_history: List[str] = []

    def select_evasion_move(self, valid_moves: List[Tuple[str, Tuple[int, int]]]) -> Tuple[str, Tuple[int, int]]:
        """Select move that maximizes Manhattan distance from Cop's position estimate."""
        best_move = valid_moves[0]
        max_dist = -1

        for direction, new_pos in valid_moves:
            dist = abs(new_pos[0] - self.cop_position_estimate[0]) + abs(new_pos[1] - self.cop_position_estimate[1])
            if dist > max_dist:
                max_dist = dist
                best_move = (direction, new_pos)

        self.position = best_move[1]
        self.move_history.append(best_move[0])
        return best_move

    def generate_deceptive_bluff(self, actual_direction: str) -> str:
        """Generate a deceptive direction hint."""
        opposites = {"N": "S", "S": "N", "E": "W", "W": "E", "STAY": "N"}
        fake_direction = opposites.get(actual_direction, "N")
        return f"I moved {fake_direction}"


if __name__ == "__main__":
    thief = ThiefBrainExample()
    moves = [("N", (2, 3)), ("S", (4, 3)), ("E", (3, 4)), ("W", (3, 2))]
    chosen = thief.select_evasion_move(moves)
    bluff = thief.generate_deceptive_bluff(chosen[0])
    print(f"Thief chosen move: {chosen}, Deceptive bluff: '{bluff}'")
