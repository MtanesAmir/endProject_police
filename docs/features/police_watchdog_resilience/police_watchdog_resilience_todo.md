# Granular Developer TODO Checklist
## Feature: Police Watchdog & Deadline Tracker System (`police_watchdog_resilience`)

This task list breaks down the implementation plan from `police_watchdog_resilience_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_watchdog_resilience`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_watchdog_resilience.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create watchdog.py and deadline_tracker.py in src/reliability/
- [ ] Task 2.2: Implement DeadlineTracker.check_deadline(start_time, timeout=30)
- [ ] Task 2.3: Implement watchdog_check() returning ALIVE or SHUTDOWN
- [ ] Task 2.4: Implement persist_state() writing emergency recovery JSON
- [ ] Task 2.5: Write unit tests for timeout detection and state persistence trigger

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_watchdog_resilience` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_watchdog_resilience_prd.md`.
