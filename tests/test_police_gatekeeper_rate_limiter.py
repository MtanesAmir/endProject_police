"""Unit tests for Police Gatekeeper Rate Limiter & DOS Detector (police_gatekeeper_rate_limiter)."""

import time
import pytest
from src.domain.gatekeeper import Gatekeeper, TokenBucket, DOSDetector


def test_token_bucket_initial_capacity_and_allow():
    bucket = TokenBucket(capacity=5.0, refill_rate=1.0)
    # Burst 5 requests should succeed
    for _ in range(5):
        assert bucket.allow(cost=1.0) is True

    # 6th request should fail immediately due to capacity clamping
    assert bucket.allow(cost=1.0) is False


def test_token_bucket_continuous_refill():
    bucket = TokenBucket(capacity=2.0, refill_rate=10.0)  # 10 tokens / sec
    assert bucket.allow(2.0) is True
    assert bucket.allow(1.0) is False

    # Sleep 0.25 seconds -> should refill 2.5 tokens (clamped to capacity 2.0)
    time.sleep(0.25)
    assert bucket.allow(2.0) is True


def test_dos_detector_anomaly_detection():
    detector = DOSDetector(max_requests=5, window_seconds=1.0)
    now = time.monotonic()

    # Record 5 normal requests
    for i in range(5):
        assert detector.record_request(now=now + i * 0.1) is False

    # 6th request within same window triggers anomaly
    assert detector.record_request(now=now + 0.5) is True
    assert detector.is_dos_detected() is True

    # Reset clears flag
    detector.reset()
    assert detector.is_dos_detected() is False


def test_gatekeeper_validate_request_workflow():
    gatekeeper = Gatekeeper(capacity=3.0, refill_rate=1.0, max_requests=10)

    # Valid requests
    assert gatekeeper.validate_request({"action": "ping"}) is True
    assert gatekeeper.validate_request({"action": "move"}) is True
    assert gatekeeper.validate_request({"action": "status"}) is True

    # Token bucket exhausted
    assert gatekeeper.validate_request({"action": "extra"}) is False


def test_gatekeeper_circuit_breaker():
    gatekeeper = Gatekeeper(capacity=10.0, refill_rate=1.0, max_requests=3)

    assert gatekeeper.validate_request() is True
    assert gatekeeper.validate_request() is True
    assert gatekeeper.validate_request() is True

    # 4th request within 1s window trips circuit breaker
    assert gatekeeper.validate_request() is False
    assert gatekeeper.circuit_breaker_open is True

    # Subsequent requests are rejected by open circuit breaker
    assert gatekeeper.validate_request() is False

    # Reset restores functionality
    gatekeeper.reset()
    assert gatekeeper.circuit_breaker_open is False
    assert gatekeeper.validate_request() is True
