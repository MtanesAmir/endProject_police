# Granular Developer TODO Checklist
## Feature: Shared Contract & Configuration Management (`police_config_contract_management`)

### Task Breakdown & Progress Tracking

#### Phase 1: Configuration Schema & Contract Files
- [x] Task 1.1: Create `config/game.json` containing the official 7x7 grid shared contract parameters.
- [x] Task 1.2: Create `config/game.toml` containing default per-peer private network and LLM settings.
- [x] Task 1.3: Create `.env-example` template for environment secrets.

#### Phase 2: Build & Dependency Management
- [x] Task 2.1: Create root `pyproject.toml` with `uv` dependencies, ruff lint rules, and pytest coverage thresholds.
- [x] Task 2.2: Generate `uv.lock` for exact dependency version locking.
- [x] Task 2.3: Verify `.gitignore` includes secret files (`.env`, `credentials.json`, `token.json`).

#### Phase 3: Validation & Integration Testing
- [x] Task 3.1: Implement contract loader and validator module in `src/domain/config_loader.py`.
- [x] Task 3.2: Write unit tests in `tests/test_config_loader.py` validating schema parsing and error handling.
- [x] Task 3.3: Verify contract parameters match Chapter 3 and Appendix B of `police_thief_p2p.pdf`.

### Definition of Done (DoD)
- [x] `config/game.json` and `config/game.toml` created and verified.
- [x] Root `pyproject.toml` and `.env-example` present.
- [x] All configuration tests passing with zero secret leakage.
