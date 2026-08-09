# Custom Strategy Brain Integration Guide

## 1. Overview
The Police-Thief multi-agent system uses a modular decision brain architecture. Both Police and Thief agents inherit from the abstract base class `BrainBase` (`src/strategy/base_brain.py`).

Teams can plug in custom decision logic by creating a subclass and referencing it in `config/game.toml`:
```toml
[strategy]
police_class = "src.strategy.police_brain:MyPoliceBrain"
thief_class = "src.strategy.thief_brain:ThiefBrain"
```

---

## 2. BrainBase Abstract Interface

Every custom brain must inherit from `BrainBase` and implement two core methods:

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple, Optional, List

class BrainBase(ABC):
    def __init__(self, grid_size: int = 7):
        self.grid_size = grid_size

    @abstractmethod
    def _pick_move(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Pick a preferred target grid position based on state."""
        pass

    @abstractmethod
    def _decide_move(
        self,
        state: Dict[str, Any],
        barriers: Optional[List[Tuple[Tuple[int, int], Tuple[int, int]]]] = None
    ) -> Tuple[int, int]:
        """Decide the next valid orthogonal move respecting boundaries and barriers."""
        pass
```

---

## 3. Available Strategy Implementations

### A. Distance Heuristics (`MyPoliceBrain`)
- **Manhattan Distance**: $D = |x_1 - x_2| + |y_1 - y_2|$
- **Shortest Path (BFS)**: Computes optimal paths around static barriers.
- **Bayesian Belief Map**: Updates 2D probability map $P(\text{Thief} = s | \text{hints}, \text{scent})$ to estimate the opponent's hidden location under partial observability.

### B. Reinforcement Learning (`QLearningAgent`)
- **Bellman Equation**:
  $$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$
- **Exploration Policy**: $\epsilon$-Greedy action selection ($\epsilon = 0.10, \alpha = 0.10, \gamma = 0.95$).

### C. Thief Evasion & Deception (`ThiefBrain`)
- Maximizes distance from Police position estimate while generating misleading verbal hints.
