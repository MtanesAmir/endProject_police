# Granular Developer TODO Checklist
## Feature: Police Watchdog & Deadline Tracker System (`police_watchdog_resilience`)

This task list breaks down the implementation plan from `police_watchdog_resilience_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_watchdog_resilience`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_watchdog_resilience.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create watchdog.py and deadline_tracker.py in src/reliability/
- [x] Task 2.2: Implement DeadlineTracker.check_deadline(start_time, timeout=30)
- [x] Task 2.3: Implement watchdog_check() returning ALIVE or SHUTDOWN
- [x] Task 2.4: Implement persist_state() writing emergency recovery JSON
- [x] Task 2.5: Write unit tests for timeout detection and state persistence trigger

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_watchdog_resilience` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_watchdog_resilience_prd.md`.
