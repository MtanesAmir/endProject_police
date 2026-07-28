"""
Deadline Tracker for active network call timers and request timeouts.
"""

import time
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class DeadlineTracker:
    """
    Tracks operation deadlines and request timeouts.
    """

    DEFAULT_TIMEOUT_SEC: float = 30.0

    def __init__(self, default_timeout: float = DEFAULT_TIMEOUT_SEC):
        self.default_timeout = default_timeout
        self.start_time: Optional[float] = None

    def start_timer(self) -> float:
        """
        Record the start time of an operation.
        """
        self.start_time = time.time()
        return self.start_time

    @staticmethod
    def check_deadline(
        start_time: float,
        timeout: float = 30.0,
        current_time: Optional[float] = None,
        raise_on_timeout: bool = False,
    ) -> bool:
        """
        Check if the operation started at start_time has exceeded timeout (seconds).
        Returns True if deadline has expired (exceeded timeout), False otherwise.
        """
        if current_time is None:
            current_time = time.time()

        elapsed = current_time - start_time
        is_expired = elapsed > timeout

        if is_expired:
            logger.warning(f"Deadline expired! Elapsed: {elapsed:.2f}s, Timeout: {timeout:.2f}s")
            if raise_on_timeout:
                raise TimeoutError(f"Operation timed out after {elapsed:.2f} seconds (timeout={timeout}s)")

        return is_expired

    def is_current_timer_expired(self, timeout: Optional[float] = None) -> bool:
        """
        Check if self.start_time has expired.
        """
        if self.start_time is None:
            return False
        eff_timeout = timeout if timeout is not None else self.default_timeout
        return self.check_deadline(self.start_time, timeout=eff_timeout)
