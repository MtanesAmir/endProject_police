"""Police Gatekeeper Rate Limiter & DOS Detector (`police_gatekeeper_rate_limiter`)."""

import time
from typing import Any, Dict, List, Optional


class TokenBucket:
    """Token Bucket rate limiter with continuous refill calculation."""

    def __init__(self, capacity: float = 10.0, refill_rate: float = 2.0):
        self.capacity = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.tokens = capacity
        self.last_update = time.monotonic()

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self.last_update
        if elapsed > 0:
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_update = now

    def allow(self, cost: float = 1.0) -> bool:
        """Consumes cost tokens if available. Returns True if request is allowed, False otherwise."""
        self._refill()
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False

    def get_token_count(self) -> float:
        self._refill()
        return self.tokens


class DOSDetector:
    """Detects rapid anomalous request patterns indicating potential DOS attacks."""

    def __init__(self, max_requests: int = 20, window_seconds: float = 1.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.timestamps: List[float] = []
        self.dos_flagged = False

    def record_request(self, now: Optional[float] = None) -> bool:
        """Records an incoming request timestamp. Returns True if DOS anomaly detected."""
        if now is None:
            now = time.monotonic()

        # Prune old timestamps
        cutoff = now - self.window_seconds
        self.timestamps = [t for t in self.timestamps if t > cutoff]
        self.timestamps.append(now)

        if len(self.timestamps) > self.max_requests:
            self.dos_flagged = True
            return True
        return False

    def is_dos_detected(self) -> bool:
        return self.dos_flagged

    def reset(self) -> None:
        self.timestamps.clear()
        self.dos_flagged = False


class Gatekeeper:
    """Gatekeeper rate limiter and network defense layer."""

    def __init__(
        self,
        capacity: float = 10.0,
        refill_rate: float = 2.0,
        max_requests: int = 20,
        window_seconds: float = 1.0,
    ):
        self.token_bucket = TokenBucket(capacity=capacity, refill_rate=refill_rate)
        self.dos_detector = DOSDetector(
            max_requests=max_requests, window_seconds=window_seconds
        )
        self.circuit_breaker_open = False

    def validate_request(self, payload: Any = None) -> bool:
        """Validates incoming request payload against rate limiter, DOS detector, and circuit breaker.

        Returns True if request is allowed, False if rate limited or rejected.
        """
        if self.circuit_breaker_open:
            return False

        # Record request for DOS detection
        if self.dos_detector.record_request():
            self.circuit_breaker_open = True
            return False

        # Check Token Bucket rate limit
        if not self.token_bucket.allow(cost=1.0):
            return False

        return True

    def trip_circuit_breaker(self) -> None:
        """Sever connection manually."""
        self.circuit_breaker_open = True

    def reset(self) -> None:
        """Resets rate limiter, DOS detector, and circuit breaker."""
        self.token_bucket = TokenBucket(
            capacity=self.token_bucket.capacity,
            refill_rate=self.token_bucket.refill_rate,
        )
        self.dos_detector.reset()
        self.circuit_breaker_open = False
