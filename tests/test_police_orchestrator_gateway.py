import pytest
import os
import sys
import tempfile
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.orchestrator import PoliceOrchestrator
from src.core.state_machine import GamePhaseMachine, GamePhase
from src.reliability.watchdog import Watchdog, WatchdogStatus, SHUTDOWN, ALIVE
from src.reliability.deadline_tracker import DeadlineTracker


def test_orchestrator_initialization():
    orchestrator = PoliceOrchestrator()
    assert isinstance(orchestrator.fsm, GamePhaseMachine)
    assert isinstance(orchestrator.watchdog, Watchdog)
    assert isinstance(orchestrator.deadline_tracker, DeadlineTracker)
    assert orchestrator.fsm.current_state == GamePhase.WAITING_FOR_OPPONENT
    assert orchestrator.police_pos == (0, 0)
    assert orchestrator.current_turn == 0


def test_handle_incoming_message_ping():
    orchestrator = PoliceOrchestrator()
    res = orchestrator.handle_incoming_message("PING")
    assert res["status"] == "PONG"
    assert "timestamp" in res


def test_handle_incoming_message_turn_init():
    orchestrator = PoliceOrchestrator()
    res = orchestrator.handle_incoming_message("TURN_INIT", {"turn": 3})
    assert res["status"] == "ACK"
    assert res["turn"] == 3
    assert orchestrator.current_turn == 3


def test_process_turn_happy_path():
    orchestrator = PoliceOrchestrator(police_pos=(1, 1))
    res = orchestrator.process_turn({"opponent": "thief_pos"})

    assert res["success"] is True
    assert res["state"] == GamePhase.WAITING_FOR_OPPONENT
    assert res["data"]["police_pos"] == (2, 1)  # Advanced by 1 on x axis
    assert res["data"]["verified"] is True
    assert orchestrator.current_turn == 1
    # Check history went through full turn cycle
    history = orchestrator.fsm.history
    assert GamePhase.COMPUTING_MOVE in history
    assert GamePhase.COMMITTING in history
    assert GamePhase.AWAITING_REVEAL in history
    assert GamePhase.VERIFYING in history


def test_process_turn_with_custom_strategy():
    mock_strategy = MagicMock()
    mock_strategy.compute_next_move.return_value = (3, 4)

    orchestrator = PoliceOrchestrator(strategy_engine=mock_strategy, police_pos=(0, 0))
    res = orchestrator.process_turn()

    assert res["success"] is True
    assert orchestrator.police_pos == (3, 4)
    mock_strategy.compute_next_move.assert_called_once()


def test_process_turn_watchdog_shutdown_failure():
    mock_watchdog = MagicMock()
    mock_watchdog.check.return_value = SHUTDOWN

    with tempfile.TemporaryDirectory() as tmpdir:
        mock_watchdog.persistence_path = os.path.join(tmpdir, "emergency.json")
        orchestrator = PoliceOrchestrator(watchdog=mock_watchdog)
        res = orchestrator.process_turn()

        assert res["success"] is False
        assert "Watchdog shutdown" in res["error"]
        assert orchestrator.fsm.current_state == GamePhase.TECHNICAL_LOSS


def test_process_turn_exception_handling():
    mock_strategy = MagicMock()
    mock_strategy.compute_next_move.side_effect = RuntimeError("Strategy Engine crashed")

    with tempfile.TemporaryDirectory() as tmpdir:
        watchdog = Watchdog(persistence_path=os.path.join(tmpdir, "emergency.json"))
        orchestrator = PoliceOrchestrator(strategy_engine=mock_strategy, watchdog=watchdog)

        res = orchestrator.process_turn()

        assert res["success"] is False
        assert "Strategy Engine crashed" in res["error"]
        assert orchestrator.fsm.current_state == GamePhase.TECHNICAL_LOSS
        assert os.path.exists(watchdog.persistence_path)
