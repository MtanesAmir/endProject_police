# Granular Developer TODO Checklist
## Feature: Police Game Phase Finite State Machine (FSM) (`police_state_machine`)

This task list breaks down the implementation plan from `police_state_machine_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_state_machine`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_state_machine.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create state_machine.py in src/core/
- [x] Task 2.2: Implement GamePhaseMachine with TRANSITIONS dictionary matching textbook Fig 11
- [x] Task 2.3: Implement transition(target) raising ValueError on illegal state jump
- [x] Task 2.4: Write unit tests for happy path state cycle
- [x] Task 2.5: Write unit tests verifying illegal transition rejection and TECHNICAL_LOSS fallback

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_state_machine` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_state_machine_prd.md`.
