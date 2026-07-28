import pytest
import sys
import os

# Add src to python path if needed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.state_machine import (
    GamePhaseMachine,
    GamePhase,
    TRANSITIONS,
    WAITING_FOR_OPPONENT,
    COMPUTING_MOVE,
    COMMITTING,
    AWAITING_REVEAL,
    VERIFYING,
    TECHNICAL_LOSS,
)


def test_initial_state():
    fsm = GamePhaseMachine()
    assert fsm.current_state == GamePhase.WAITING_FOR_OPPONENT
    assert fsm.history == [GamePhase.WAITING_FOR_OPPONENT]


def test_happy_path_cycle():
    fsm = GamePhaseMachine()

    # Step 1: WAITING_FOR_OPPONENT -> COMPUTING_MOVE
    state = fsm.transition(GamePhase.COMPUTING_MOVE)
    assert state == GamePhase.COMPUTING_MOVE
    assert fsm.current_state == GamePhase.COMPUTING_MOVE

    # Step 2: COMPUTING_MOVE -> COMMITTING
    state = fsm.transition(GamePhase.COMMITTING)
    assert state == GamePhase.COMMITTING
    assert fsm.current_state == GamePhase.COMMITTING

    # Step 3: COMMITTING -> AWAITING_REVEAL
    state = fsm.transition(GamePhase.AWAITING_REVEAL)
    assert state == GamePhase.AWAITING_REVEAL
    assert fsm.current_state == GamePhase.AWAITING_REVEAL

    # Step 4: AWAITING_REVEAL -> VERIFYING
    state = fsm.transition(GamePhase.VERIFYING)
    assert state == GamePhase.VERIFYING
    assert fsm.current_state == GamePhase.VERIFYING

    # Step 5: VERIFYING -> WAITING_FOR_OPPONENT
    state = fsm.transition(GamePhase.WAITING_FOR_OPPONENT)
    assert state == GamePhase.WAITING_FOR_OPPONENT
    assert fsm.current_state == GamePhase.WAITING_FOR_OPPONENT

    assert len(fsm.history) == 6


def test_illegal_transition_raises_value_error():
    fsm = GamePhaseMachine()
    assert fsm.current_state == GamePhase.WAITING_FOR_OPPONENT

    # WAITING_FOR_OPPONENT cannot jump directly to COMMITTING
    with pytest.raises(ValueError) as exc_info:
        fsm.transition(GamePhase.COMMITTING)
    assert "Invalid state transition" in str(exc_info.value)
    assert fsm.current_state == GamePhase.WAITING_FOR_OPPONENT  # State unchanged


def test_invalid_target_string_raises_value_error():
    fsm = GamePhaseMachine()
    with pytest.raises(ValueError) as exc_info:
        fsm.transition("INVALID_STATE_NAME")
    assert "Unknown target state" in str(exc_info.value)


def test_transition_to_technical_loss():
    # Test transition to TECHNICAL_LOSS from various states
    for initial_phase in [
        GamePhase.WAITING_FOR_OPPONENT,
        GamePhase.COMPUTING_MOVE,
        GamePhase.COMMITTING,
        GamePhase.AWAITING_REVEAL,
        GamePhase.VERIFYING,
    ]:
        fsm = GamePhaseMachine(initial_state=initial_phase)
        fsm.transition(GamePhase.TECHNICAL_LOSS)
        assert fsm.current_state == GamePhase.TECHNICAL_LOSS


def test_force_technical_loss():
    fsm = GamePhaseMachine(initial_state=GamePhase.COMPUTING_MOVE)
    res = fsm.force_technical_loss()
    assert res == GamePhase.TECHNICAL_LOSS
    assert fsm.current_state == GamePhase.TECHNICAL_LOSS


def test_transitions_dictionary_structure():
    assert GamePhase.WAITING_FOR_OPPONENT in TRANSITIONS
    assert GamePhase.COMPUTING_MOVE in TRANSITIONS[GamePhase.WAITING_FOR_OPPONENT]
    assert GamePhase.TECHNICAL_LOSS in TRANSITIONS[GamePhase.WAITING_FOR_OPPONENT]
