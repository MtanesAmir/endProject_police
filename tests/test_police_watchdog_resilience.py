import pytest
import os
import sys
import time
import json
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.reliability.deadline_tracker import DeadlineTracker
from src.reliability.watchdog import (
    Watchdog,
    WatchdogStatus,
    watchdog_check,
    persist_state,
    controlled_shutdown,
    ALIVE,
    SHUTDOWN,
)


def test_deadline_tracker_within_timeout():
    start_time = 1000.0
    current_time = 1020.0  # 20s elapsed
    expired = DeadlineTracker.check_deadline(start_time, timeout=30.0, current_time=current_time)
    assert expired is False


def test_deadline_tracker_exceeded_timeout():
    start_time = 1000.0
    current_time = 1035.0  # 35s elapsed
    expired = DeadlineTracker.check_deadline(start_time, timeout=30.0, current_time=current_time)
    assert expired is True


def test_deadline_tracker_raise_on_timeout():
    start_time = 1000.0
    current_time = 1035.0
    with pytest.raises(TimeoutError):
        DeadlineTracker.check_deadline(
            start_time, timeout=30.0, current_time=current_time, raise_on_timeout=True
        )


def test_watchdog_check_alive():
    last_heartbeat = 1000.0
    current_time = 1100.0  # 100s elapsed <= 180s timeout
    status = watchdog_check(last_heartbeat, timeout_sec=180.0, current_time=current_time)
    assert status == ALIVE
    assert status == WatchdogStatus.ALIVE


def test_watchdog_check_shutdown():
    last_heartbeat = 1000.0
    current_time = 1200.0  # 200s elapsed > 180s timeout
    status = watchdog_check(last_heartbeat, timeout_sec=180.0, current_time=current_time)
    assert status == SHUTDOWN
    assert status == WatchdogStatus.SHUTDOWN


def test_persist_state():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test_emergency_state.json")
        state_data = {
            "game_phase": "COMPUTING_MOVE",
            "turn": 5,
            "police_pos": (2, 3),
            "status": "EMERGENCY_DUMP",
        }

        success = persist_state(state_data, filepath=filepath)
        assert success is True
        assert os.path.exists(filepath)

        with open(filepath, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)

        assert loaded_data["game_phase"] == "COMPUTING_MOVE"
        assert loaded_data["turn"] == 5


def test_watchdog_class_instance():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "state.json")
        wd = Watchdog(timeout_sec=50.0, persistence_path=filepath)

        hb = wd.update_heartbeat()
        assert hb > 0

        # Alive check
        assert wd.check(current_time=hb + 10.0) == ALIVE

        # Timeout check
        assert wd.check(current_time=hb + 60.0) == SHUTDOWN

        # Persist current state
        res = wd.persist_current_state({"key": "value"})
        assert res is True
