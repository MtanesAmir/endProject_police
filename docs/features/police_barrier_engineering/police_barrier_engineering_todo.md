# Granular Developer TODO Checklist
## Feature: Police Spatial Engineering & Barrier Placement (`police_barrier_engineering`)

This task list breaks down the implementation plan from `police_barrier_engineering_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_barrier_engineering`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_barrier_engineering.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create BarrierManager module in src/domain/barriers.py
- [ ] Task 2.2: Implement place_barrier(pos) with distance-1 and quota check
- [ ] Task 2.3: Add remaining_barriers counter and immutability rules for placed barriers
- [ ] Task 2.4: Write unit tests for max_barriers quota enforcement (14 barriers max)
- [ ] Task 2.5: Write unit tests for invalid placement attempts (out of bounds, distance > 1)

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_barrier_engineering` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_barrier_engineering_prd.md`.
