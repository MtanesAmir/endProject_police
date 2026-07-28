# Granular Developer TODO Checklist
## Feature: Police Replay Viewer & Cryptographic Log Verifier (`police_replay_verifier`)

This task list breaks down the implementation plan from `police_replay_verifier_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_replay_verifier`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_replay_verifier.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create replay_verifier.py in src/gui/
- [ ] Task 2.2: Implement verify_step(log_entry) -> str ("Verified OK" or "TAMPERED")
- [ ] Task 2.3: Implement replay(log_filepath) trajectory reader loop
- [ ] Task 2.4: Write unit tests for valid log verification returning Verified OK
- [ ] Task 2.5: Write unit tests for tampered log detection returning TAMPERED

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_replay_verifier` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_replay_verifier_prd.md`.
