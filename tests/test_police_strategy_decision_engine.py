"""Unit tests for police_strategy_decision_engine feature."""

import pytest
from src.strategy.base_brain import BrainBase, GRID_SIZE
from src.strategy.police_brain import MyPoliceBrain
from src.strategy.q_learning import QLearningAgent


def test_brain_base_grid_bounds():
    brain = MyPoliceBrain(grid_size=7)
    assert brain.is_valid_position((0, 0))
    assert brain.is_valid_position((6, 6))
    assert not brain.is_valid_position((-1, 0))
    assert not brain.is_valid_position((7, 3))


def test_brain_base_barriers():
    brain = MyPoliceBrain(grid_size=7)
    barriers = [((2, 2), (2, 3))]
    assert brain.is_path_blocked((2, 2), (2, 3), barriers)
    assert brain.is_path_blocked((2, 3), (2, 2), barriers)
    assert not brain.is_path_blocked((2, 2), (3, 2), barriers)


def test_my_police_brain_pick_and_decide_move_deterministic():
    brain = MyPoliceBrain(grid_size=7, use_q_learning=False)
    state = {
        "police_pos": (1, 1),
        "thief_pos": (4, 1),
    }

    # _pick_move should move horizontally towards thief_pos (4, 1) -> step right to (2, 1)
    pick = brain._pick_move(state)
    assert pick == (2, 1)

    # _decide_move without barriers should pick (2, 1) to minimize distance from (1, 1) to (4, 1)
    decide = brain._decide_move(state)
    assert decide == (2, 1)


def test_my_police_brain_decide_move_with_barrier_avoidance():
    brain = MyPoliceBrain(grid_size=7, use_q_learning=False)
    # Barrier right between (1,1) and (2,1)
    barriers = [((1, 1), (2, 1))]
    state = {
        "police_pos": (1, 1),
        "thief_pos": (4, 1),
    }

    decide = brain._decide_move(state, barriers=barriers)
    # Because (2, 1) is blocked by barrier, should choose non-blocked move closest to target
    assert decide != (2, 1)
    assert brain.is_valid_position(decide)


def test_my_police_brain_belief_grid_target():
    brain = MyPoliceBrain(grid_size=7)
    state = {
        "police_pos": (0, 0),
        "belief_grid": {
            (0, 0): 0.1,
            (5, 5): 0.8,
            (2, 2): 0.1,
        },
    }
    target = brain._get_target_position(state)
    assert target == (5, 5)


def test_q_learning_agent_update():
    agent = QLearningAgent(alpha=0.5, gamma=0.9, epsilon=0.0)
    state_key = "(1, 1)_(4, 1)"
    action = "RIGHT"
    next_state_key = "(2, 1)_(4, 1)"

    initial_q = agent.get_q_value(state_key, action)
    assert initial_q == 0.0

    # Reward of +10 for moving closer
    agent.update(state_key, action, 10.0, next_state_key)
    updated_q = agent.get_q_value(state_key, action)

    # Q(s,a) = 0 + 0.5 * (10.0 + 0.9*0 - 0) = 5.0
    assert updated_q == pytest.approx(5.0)


def test_my_police_brain_with_q_learning():
    q_agent = QLearningAgent(alpha=1.0, gamma=0.9, epsilon=0.0)
    # Set high Q-value for UP action from state
    state_key = "(3, 3)_(3, 0)"
    q_agent.q_table[(state_key, "UP")] = 100.0

    brain = MyPoliceBrain(use_q_learning=True, q_agent=q_agent)
    state = {
        "police_pos": (3, 3),
        "thief_pos": (3, 0),
    }

    move = brain._decide_move(state)
    # UP from (3,3) leads to (3,2)
    assert move == (3, 2)
