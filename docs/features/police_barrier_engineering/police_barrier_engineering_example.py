"""Example demonstrating police barrier engineering and validation."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.barriers import BarrierManager

def main():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    print(f"Initial remaining barriers: {manager.remaining_barriers}")
    cop_pos = (0, 0)
    target = (0, 1)
    success = manager.place_barrier(target, cop_pos)
    print(f"Place barrier at {target}: {success}")
    print(f"Is barrier at {target}: {manager.is_blocked(target)}")
    print(f"Remaining barriers: {manager.remaining_barriers}")

if __name__ == "__main__":
    main()
