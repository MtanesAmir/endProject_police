# Granular Developer TODO Checklist
## Feature: Police Gatekeeper Rate Limiter & DOS Detector (`police_gatekeeper_rate_limiter`)

This task list breaks down the implementation plan from `police_gatekeeper_rate_limiter_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_gatekeeper_rate_limiter`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_gatekeeper_rate_limiter.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create rate_limiter.py and dos_detector.py in src/infra/
- [ ] Task 2.2: Implement TokenBucket with time.monotonic() continuous refill calculation
- [ ] Task 2.3: Implement allow() returning True/False based on available tokens
- [ ] Task 2.4: Implement DOSDetector detecting frequency anomalies
- [ ] Task 2.5: Write unit tests verifying rate limiting continuous refill and burst clamping

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_gatekeeper_rate_limiter` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_gatekeeper_rate_limiter_prd.md`.
