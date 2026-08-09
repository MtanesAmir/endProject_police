"""Example demonstrating base grid movement, boundaries, and legal action generation."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.grid import MovementEngine, legal_moves

def main():
    pos = (3, 3)
    moves = legal_moves(pos, barriers={(3, 4)}, grid_size=7)
    print(f"Current Position: {pos}")
    print(f"Legal moves: {moves}")

if __name__ == "__main__":
    main()
