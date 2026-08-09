"""Example snippet demonstrating Thief evasion brain move decision."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.strategy.thief_brain import ThiefBrain

def main():
    brain = ThiefBrain(grid_size=7)
    action = brain._pick_move(state={"my_pos": (3, 3), "police_pos": (0, 0), "barriers": set()})
    print(f"[Thief Brain Example] Evasion brain selected action: {action}")

if __name__ == "__main__":
    main()
