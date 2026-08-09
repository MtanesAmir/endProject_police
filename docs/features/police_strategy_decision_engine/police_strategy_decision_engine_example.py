"""Example demonstrating Police decision engine combining Manhattan heuristics, Bayesian belief, and barrier placement."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.strategy.police_brain import MyPoliceBrain

def main():
    brain = MyPoliceBrain(grid_size=7)
    move = brain._pick_move(state={"my_pos": (0, 0), "enemy_pos": None, "barriers": []})
    print(f"Police decision engine selected move: {move}")

if __name__ == "__main__":
    main()
