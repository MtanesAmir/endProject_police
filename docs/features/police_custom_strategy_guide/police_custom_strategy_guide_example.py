"""Example custom user brain implementation inheriting from BrainBase."""
import os
import sys
from typing import Dict, Any, Tuple

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.strategy.base_brain import BrainBase

class CustomPoliceBrainExample(BrainBase):
    def __init__(self, grid_size: int = 7):
        super().__init__(grid_size=grid_size)

    def _decide_move(self, state: Dict[str, Any]) -> Tuple[int, int]:
        return (0, 1)

    def _pick_move(self, state: Dict[str, Any]) -> Tuple[int, int]:
        return self._decide_move(state)

    def _decide_bluff(self, state: Dict[str, Any]) -> str:
        return "Heading towards lower quadrant"

if __name__ == "__main__":
    brain = CustomPoliceBrainExample()
    move = brain._decide_move({"my_pos": (0, 0)})
    print(f"[Custom Brain Example] Selected move: {move}")
