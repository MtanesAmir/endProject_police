# Mechanism PRD: Gatekeeper & Token Bucket Rate Limiter

### 1. Overview
The Gatekeeper Rate Limiter and DOS Detector control outgoing API traffic, enforcing token bucket rate limits and preventing API quota exhaustion or denial-of-service loops.

### 2. Functional Requirements
- **FR-01**: Token Bucket rate limiting enforcing max 30 requests/minute with continuous refill rate $r$.
- **FR-02**: Detect burst request spikes and queue excessive calls up to `queue_depth = 100`.
- **FR-03**: Detect loop bugs or DOS anomalies and trigger circuit breaker isolation.

### 3. Implementation References
- Implementation: `src/domain/gatekeeper.py` & `src/infra/rate_limiter.py`
- Test suite: `tests/test_police_gatekeeper_rate_limiter.py`
