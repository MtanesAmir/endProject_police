# Product Requirements Document (PRD)
## Feature: Application CLI Runner & Executable Entry Points (`police_cli_entrypoint_runner`)

### 1. Product Overview & Problem Statement
To execute, evaluate, and test the Police-Thief P2P system according to the project specification (Chapter 14 of course book), a unified command-line entry point is required.

The system must support standard commands:
- `uv run python -m police_thief peer --role police`
- `uv run python -m police_thief peer --role thief`
- `uv run python -m police_thief replay --log logs/police_match.json`

### 2. Product Objectives & Target Capabilities
- **CLI Commands**: Provide CLI subcommands `peer` and `replay` via `argparse`.
- **Peer Role Launcher**: Launch either Cop (`--role police`) or Thief (`--role thief`) FastMCP server instances bound to configured host/ports.
- **Match Replay CLI**: Inspect and verify past match logs (`logs/police_match.json`) with cryptographic integrity verification, reporting `Verified OK` or `TAMPERED`.
- **Configuration Parameter Overrides**: Accept `--config`, `--port`, `--host`, and `--opponent-url` command-line overrides.

### 3. Detailed Feature Requirements
- **FR-01**: Implement package entry point `src/cli.py` and top-level executable `main.py`.
- **FR-02**: Parse subcommands `peer` (flags: `--role`, `--host`, `--port`, `--opponent-url`, `--config`) and `replay` (flags: `--log`).
- **FR-03**: Bind and start `FastMCPServer` in standard HTTP transport mode.
- **FR-04**: Execute replay engine on specified log files and output pass/fail verdict with terminal color highlights.
- **FR-05**: Support graceful shutdown via SIGINT / SIGTERM signals handled by Watchdog.

### 4. Non-Functional Requirements (NFRs)
- **Compatibility**: Compatible with Python 3.11+ and standard `uv run` invocations.
- **CLI Error Handling**: Clear error messages and non-zero exit codes for invalid options or missing log files.
- **Zero Configuration Leakage**: Role specific settings applied dynamically based on role flags.

### 5. Success Metrics & Acceptance Criteria
- All standard commands specified in Chapter 14 of course documentation execute successfully.
- Replay verifier CLI correctly identifies valid logs as `Verified OK` and tampered logs as `TAMPERED`.
- Passing unit test coverage for CLI argument parser and execution dispatcher.
