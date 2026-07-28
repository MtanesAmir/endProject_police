# Granular Developer TODO Checklist
## Feature: Police Capture Detection & Claim Engine (`police_capture_mechanics`)

This task list breaks down the implementation plan from `police_capture_mechanics_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_capture_mechanics`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_capture_mechanics.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create CaptureDetector class in src/domain/capture.py
- [ ] Task 2.2: Implement check_direct_capture(cop_pos, thief_pos) -> bool
- [ ] Task 2.3: Implement check_trapped_capture(thief_pos, barriers, grid_size) -> bool
- [ ] Task 2.4: Integrate scoring map (20 points for Cop capture win)
- [ ] Task 2.5: Write unit tests verifying direct and trapped capture detection

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_capture_mechanics` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_capture_mechanics_prd.md`.
