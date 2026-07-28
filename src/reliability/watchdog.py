"""
Watchdog monitor for Police agent liveness and emergency state persistence.
"""

from enum import Enum
import json
import logging
import os
import time
from typing import Any, Dict, Optional, Union

logger = logging.getLogger(__name__)


class WatchdogStatus(str, Enum):
    ALIVE = "ALIVE"
    SHUTDOWN = "SHUTDOWN"


ALIVE = WatchdogStatus.ALIVE
SHUTDOWN = WatchdogStatus.SHUTDOWN


def watchdog_check(
    last_heartbeat: float,
    timeout_sec: float = 180.0,
    current_time: Optional[float] = None,
) -> WatchdogStatus:
    """
    Evaluates main loop liveness.
    Returns ALIVE if elapsed time since last heartbeat <= timeout_sec, else SHUTDOWN.
    """
    if current_time is None:
        current_time = time.time()

    elapsed = current_time - last_heartbeat
    if elapsed > timeout_sec:
        logger.error(f"Watchdog check failed! Elapsed: {elapsed:.2f}s, Timeout: {timeout_sec:.2f}s")
        return WatchdogStatus.SHUTDOWN

    return WatchdogStatus.ALIVE


def persist_state(
    state_data: Dict[str, Any],
    filepath: str = "data/police_emergency_state.json",
) -> bool:
    """
    Dumps emergency recovery state JSON to specified disk location.
    """
    try:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2, default=str)
        logger.info(f"Emergency state successfully persisted to {filepath}")
        return True
    except Exception as e:
        logger.error(f"Failed to persist state to {filepath}: {e}")
        return False


def controlled_shutdown(reason: str = "Watchdog timeout") -> None:
    """
    Executes controlled shutdown releasing resources.
    """
    logger.critical(f"Initiating controlled shutdown: {reason}")


class Watchdog:
    """
    Watchdog component managing main loop heartbeats and state persistence.
    """

    def __init__(
        self,
        timeout_sec: float = 180.0,
        persistence_path: str = "data/police_emergency_state.json",
    ):
        self.timeout_sec = timeout_sec
        self.persistence_path = persistence_path
        self.last_heartbeat: float = time.time()

    def update_heartbeat(self) -> float:
        """
        Record a heartbeat tick.
        """
        self.last_heartbeat = time.time()
        return self.last_heartbeat

    def check(self, current_time: Optional[float] = None) -> WatchdogStatus:
        """
        Run watchdog check on current heartbeat.
        """
        return watchdog_check(
            self.last_heartbeat,
            timeout_sec=self.timeout_sec,
            current_time=current_time,
        )

    def persist_current_state(self, state_data: Dict[str, Any]) -> bool:
        """
        Persist state using configured persistence path.
        """
        return persist_state(state_data, self.persistence_path)
