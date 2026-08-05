# Product Requirements Document (PRD)
## Feature: Match Artifact Export CLI Subcommand (`police_artifact_export_cli_cmd`)

### 1. Product Overview & Problem Statement
Section 9.3.3 and Appendix Table 20 of `police_thief_p2p.pdf` require exporting 4 mandatory signed JSON match artifacts upon game completion:
- `declaration_police.json`
- `config_police.json`
- `log_police.json`
- `result_police.json`

A CLI subcommand `report` added to `main.py` / `src/cli.py` enables students or automated evaluators to trigger artifact compilation directly from the command line.

### 2. Product Objectives & Target Capabilities
- **CLI `report` Subcommand**: Command `python main.py report --summary logs/police_match.json` compiling the 4 JSON artifacts into `results/`.
- **Artifact Formatter**: Formats artifacts with SHA-256 signatures, git commit hash, grid config parameters, step trajectory, and token consumption statistics.

### 3. Detailed Feature Requirements
- **FR-01**: Add `report` subcommand to `create_parser()` in `src/cli.py`.
- **FR-02**: Support `--summary` (path to match JSON file) and `--outdir` (output directory, default `results/`).
- **FR-03**: Call `GmailReporter.compile_match_reports()` to generate the 4 signed JSON files.
- **FR-04**: Write artifact files to target output directory.

### 4. Non-Functional Requirements (NFRs)
- **Formatting**: JSON output structured with key sorting and readable 2-space indentation.
- **CLI Feedback**: Prints created artifact file paths upon completion.

### 5. Success Metrics & Acceptance Criteria
- Executing `python main.py report` writes all 4 JSON artifacts to `results/`.
- Unit tests pass in `tests/test_cli.py`.
