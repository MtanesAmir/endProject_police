# Granular Developer TODO Checklist
## Feature: Police Strategy Engine & Brain Base Subclass (`police_strategy_decision_engine`)

This task list breaks down the implementation plan from `police_strategy_decision_engine_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_strategy_decision_engine`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_strategy_decision_engine.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create base_brain.py and police_brain.py in src/strategy/
- [ ] Task 2.2: Implement MyPoliceBrain overriding _pick_move and _decide_move
- [ ] Task 2.3: Implement Q-learning helper in src/strategy/q_learning.py with Bellman update
- [ ] Task 2.4: Write unit tests verifying deterministic move output from heuristic strategy
- [ ] Task 2.5: Write unit tests verifying Q-learning table updates after state-reward transitions

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_strategy_decision_engine` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_strategy_decision_engine_prd.md`.
