# Granular Developer TODO Checklist
## Feature: Police Manhattan Distance & Target Heuristics (`police_distance_heuristics`)

This task list breaks down the implementation plan from `police_distance_heuristics_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_distance_heuristics`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_distance_heuristics.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create DistanceHeuristics in src/strategy/heuristics.py
- [x] Task 2.2: Implement manhattan_distance(a, b) -> int
- [x] Task 2.3: Implement select_closest_move(current_pos, target_pos, legal_moves) -> Direction
- [x] Task 2.4: Write unit tests for Manhattan distance calculation across grid corners
- [x] Task 2.5: Write unit tests for path choice around single barrier obstacles

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_distance_heuristics` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_distance_heuristics_prd.md`.
