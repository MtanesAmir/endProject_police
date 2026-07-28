# Granular Developer TODO Checklist
## Feature: Police Cryptographic Commit-Reveal Protocol Engine (`police_commit_reveal_crypto`)

This task list breaks down the implementation plan from `police_commit_reveal_crypto_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_commit_reveal_crypto`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_commit_reveal_crypto.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create commit_reveal.py in src/security/ and src/domain/crypto.py
- [x] Task 2.2: Implement commit() with secrets.token_hex(16) and json.dumps(sort_keys=True)
- [x] Task 2.3: Implement verify() with hashlib.sha256 and secrets.compare_digest
- [x] Task 2.4: Write unit tests for byte-identical serialization across instances
- [x] Task 2.5: Write unit tests detecting modified move or intent payload tampering

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_commit_reveal_crypto` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_commit_reveal_crypto_prd.md`.
