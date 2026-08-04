# Granular Developer TODO Checklist
## Feature: Thief Evasion Strategy Brain & Dual Match Simulator (`police_thief_evasion_brain`)

### Task Breakdown & Progress Tracking

#### Phase 1: ThiefBrain Core Strategy Implementation
- [x] Task 1.1: Create `src/strategy/thief_brain.py` with `ThiefBrain` inheriting from `BrainBase`.
- [x] Task 1.2: Implement `_pick_move()` maximizing distance from Cop's estimated position.
- [x] Task 1.3: Implement `_decide_bluff()` generating deceptive directional hints.

#### Phase 2: Dual Match Simulator Runner
- [x] Task 2.1: Create `src/core/match_runner.py` to run multi-turn matches.
- [x] Task 2.2: Implement turn sequence handling (Commit -> Ack -> Reveal -> State Update -> Scent Decay).
- [x] Task 2.3: Record trajectory logs in `logs/police_match.json` format.

#### Phase 3: Testing & Verification
- [x] Task 3.1: Write unit tests in `tests/test_thief_brain.py`.
- [x] Task 3.2: Run full simulation test verifying Thief evasion up to 35 steps.

### Definition of Done (DoD)
- [x] `ThiefBrain` implemented and passing all tests.
- [x] `MatchRunner` capable of running full end-to-end games.
