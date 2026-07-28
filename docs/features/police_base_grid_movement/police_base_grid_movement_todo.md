# Granular Developer TODO Checklist
## Feature: Police Base Grid & Movement Engine (`police_base_grid_movement`)

This task list breaks down the implementation plan from `police_base_grid_movement_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_base_grid_movement`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_base_grid_movement.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create GridPos dataclass in src/domain/grid.py
- [ ] Task 2.2: Implement legal_moves(pos, grid_size, barriers) method
- [ ] Task 2.3: Write unit tests for 7x7 boundary constraints
- [ ] Task 2.4: Write unit tests for orthogonal direction application
- [ ] Task 2.5: Add state inspection helper methods for Orchestrator

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_base_grid_movement` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_base_grid_movement_prd.md`.
