# Granular Developer TODO Checklist
## Feature: Police Scent Field & Stigmergic Trail Tracker (`police_scent_tracking`)

This task list breaks down the implementation plan from `police_scent_tracking_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_scent_tracking`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_scent_tracking.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create ScentTracker in src/domain/scent.py
- [ ] Task 2.2: Implement apply_emission(center_pos, tau_center=0.9)
- [ ] Task 2.3: Implement apply_decay(rho=0.10) per full turn cycle
- [ ] Task 2.4: Write unit tests for 5x5 radial distribution math
- [ ] Task 2.5: Write unit tests for multi-turn decay progression matching textbook graph (Fig 5)

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_scent_tracking` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_scent_tracking_prd.md`.
