"""
Reliability package containing watchdog and deadline tracker.
"""

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

__all__ = [
    "DeadlineTracker",
    "Watchdog",
    "WatchdogStatus",
    "watchdog_check",
    "persist_state",
    "controlled_shutdown",
    "ALIVE",
    "SHUTDOWN",
]
