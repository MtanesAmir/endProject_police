# Granular Developer TODO Checklist
## Feature: Police Bayesian Belief Map Engine (`police_bayesian_belief`)

This task list breaks down the implementation plan from `police_bayesian_belief_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_bayesian_belief`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_bayesian_belief.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create BayesianBeliefMap in src/strategy/bayesian.py and src/domain/belief.py
- [x] Task 2.2: Implement update_from_scent(scent_matrix)
- [x] Task 2.3: Implement update_from_hint(hint_text, opponent_direction, reliability=0.8)
- [x] Task 2.4: Implement normalize() to maintain sum(b(s)) == 1.0
- [x] Task 2.5: Write unit tests verifying belief concentration on highest likelihood cells

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_bayesian_belief` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_bayesian_belief_prd.md`.
