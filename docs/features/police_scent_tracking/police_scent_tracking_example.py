"""Example demonstrating scent field emission, exponential decay, and stigmergy tracking."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.scent import ScentTracker

def main():
    tracker = ScentTracker(grid_size=7)
    tracker.apply_emission((3, 3))
    print(f"Scent at emission center (3, 3): {tracker.get_scent_level((3, 3)):.2f}")
    tracker.apply_decay()
    print(f"Scent at (3, 3) after 1 turn decay: {tracker.get_scent_level((3, 3)):.2f}")

if __name__ == "__main__":
    main()
