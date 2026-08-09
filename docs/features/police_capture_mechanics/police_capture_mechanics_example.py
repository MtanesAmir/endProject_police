"""Example demonstrating capture evaluation and scoring outcomes."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.capture import check_capture, CaptureDetector

def main():
    is_captured = check_capture(police_pos=(3, 3), thief_pos=(3, 3))
    print(f"Cop captures Thief at same cell: {is_captured}")
    is_not_captured = check_capture(police_pos=(0, 0), thief_pos=(6, 6))
    print(f"Cop at (0,0) and Thief at (6,6) captured: {is_not_captured}")

if __name__ == "__main__":
    main()
