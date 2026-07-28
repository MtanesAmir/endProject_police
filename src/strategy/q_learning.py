"""Q-Learning reinforcement learning module for Police strategy decision engine."""

import random
from typing import Any, Dict, List, Optional, Tuple


class QLearningAgent:
    """Q-learning agent supporting Q-table state-action updates via Bellman equation."""

    def __init__(
        self,
        alpha: float = 0.1,
        gamma: float = 0.9,
        epsilon: float = 0.1,
        actions: Optional[List[str]] = None,
    ):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions or ["STAY", "UP", "DOWN", "LEFT", "RIGHT"]
        self.q_table: Dict[Tuple[str, str], float] = {}

    def get_q_value(self, state_key: str, action: str) -> float:
        """Retrieve Q-value for given state key and action."""
        return self.q_table.get((state_key, action), 0.0)

    def choose_action(self, state_key: str, valid_actions: Optional[List[str]] = None) -> str:
        """Choose action using epsilon-greedy strategy."""
        actions_to_choose = valid_actions if valid_actions else self.actions
        if not actions_to_choose:
            return "STAY"

        if random.random() < self.epsilon:
            return random.choice(actions_to_choose)

        q_values = [self.get_q_value(state_key, a) for a in actions_to_choose]
        max_q = max(q_values)
        # Handle ties by random choice among best actions
        best_actions = [a for a, q in zip(actions_to_choose, q_values) if q == max_q]
        return random.choice(best_actions)

    def update(
        self,
        state_key: str,
        action: str,
        reward: float,
        next_state_key: str,
        next_valid_actions: Optional[List[str]] = None,
    ) -> None:
        """Bellman equation Q-value update:

        Q(s,a) <- Q(s,a) + alpha * (reward + gamma * max_a' Q(s',a') - Q(s,a))
        """
        current_q = self.get_q_value(state_key, action)
        next_actions = next_valid_actions if next_valid_actions else self.actions
        next_max_q = max([self.get_q_value(next_state_key, a) for a in next_actions], default=0.0)

        td_target = reward + self.gamma * next_max_q
        td_error = td_target - current_q
        new_q = current_q + self.alpha * td_error

        self.q_table[(state_key, action)] = new_q
