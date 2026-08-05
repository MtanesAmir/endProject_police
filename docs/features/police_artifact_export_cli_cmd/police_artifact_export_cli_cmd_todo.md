# Granular Developer TODO Checklist
## Feature: Match Artifact Export CLI Subcommand (`police_artifact_export_cli_cmd`)

### Task Breakdown & Progress Tracking

#### Phase 1: CLI Subparser Addition
- [x] Task 1.1: Update `create_parser()` in `src/cli.py` to add `report` subcommand.
- [x] Task 1.2: Add `--summary` and `--outdir` flags.

#### Phase 2: Artifact Exporter Handler
- [x] Task 2.1: Implement artifact compiler integration in `src/cli.py`.
- [x] Task 2.2: Export `declaration_police.json`, `config_police.json`, `log_police.json`, `result_police.json` to `results/`.

#### Phase 3: Testing & Verification
- [x] Task 3.1: Write unit tests in `tests/test_cli.py` for `report` subcommand.
- [x] Task 3.2: Verify 4 JSON files created in `results/`.

### Definition of Done (DoD)
- [x] CLI `report` subcommand implemented, documented, and passing tests.
