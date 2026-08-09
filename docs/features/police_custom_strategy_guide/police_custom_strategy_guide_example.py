"""Example demonstrating custom BrainBase subclass implementation and dynamic loading."""

import importlib
from typing import Dict, Any, Tuple, Optional, List
from src.strategy.base_brain import BrainBase


class CustomHeuristicBrain(BrainBase):
    """Custom user-defined BrainBase implementation example."""

    def __init__(self, grid_size: int = 7):
        super().__init__(grid_size=grid_size)

    def _pick_move(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Custom heuristic pick move logic."""
        pos = state.get("police_pos", (0, 0))
        target = state.get("thief_pos", (3, 3))
        dx = 1 if target[0] > pos[0] else (-1 if target[0] < pos[0] else 0)
        dy = 1 if target[1] > pos[1] else (-1 if target[1] < pos[1] else 0)
        if dx != 0:
            return (pos[0] + dx, pos[1])
        return (pos[0], pos[1] + dy)

    def _decide_move(
        self,
        state: Dict[str, Any],
        barriers: Optional[List[Tuple[Tuple[int, int], Tuple[int, int]]]] = None,
    ) -> Tuple[int, int]:
        """Custom decide move logic."""
        return self._pick_move(state)


def load_brain_class(class_path: str) -> type:
    """Dynamically load brain class from package.module:ClassName string."""
    module_path, class_name = class_path.split(":")
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


if __name__ == "__main__":
    brain = CustomHeuristicBrain()
    move = brain._decide_move({"police_pos": (0, 0), "thief_pos": (3, 3)})
    print(f"[Custom Brain Example] Decided move: {move}")
