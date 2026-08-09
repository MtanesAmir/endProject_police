"""Example demonstrating Gatekeeper token-bucket rate limiter and DOS prevention."""
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.infra.rate_limiter import TokenBucket, Gatekeeper
from src.infra.dos_detector import DOSDetector

def main():
    bucket = TokenBucket(capacity=5.0, refill_rate=0.8)
    gatekeeper = Gatekeeper(capacity=5.0, refill_rate=0.8)
    detector = DOSDetector(max_requests=20, window_seconds=1.0)
    print(f"Initial request allowed: {bucket.allow(1.0)}")
    print(f"Gatekeeper validate_request: {gatekeeper.validate_request()}")
    detector.record_request()
    print(f"DOS detected: {detector.is_dos_detected()}")

if __name__ == "__main__":
    main()
