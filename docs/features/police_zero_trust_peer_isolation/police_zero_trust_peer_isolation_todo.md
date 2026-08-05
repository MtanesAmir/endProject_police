# Granular Developer TODO Checklist
## Feature: Zero-Trust Peer Config Isolation (`police_zero_trust_peer_isolation`)

### Task Breakdown & Progress Tracking

#### Phase 1: Isolated Directory Structure
- [x] Task 1.1: Create `config/police/game.toml` for Police agent settings.
- [x] Task 1.2: Create `config/thief/game.toml` for Thief agent settings.

#### Phase 2: Loader Role Resolution
- [x] Task 2.1: Enhance `ConfigLoader.load_private_config(role="police")` to resolve `config/<role>/game.toml`.
- [x] Task 2.2: Add fallback logic for root `config/game.toml`.

#### Phase 3: Testing & Verification
- [x] Task 3.1: Write unit tests in `tests/test_config_loader.py` validating role-based TOML loading.
- [x] Task 3.2: Verify zero state leakage between Cop and Thief configs.

### Definition of Done (DoD)
- [x] Config isolation implemented, documented, and passing tests.
