# Granular Developer TODO Checklist
## Feature: Application CLI Runner & Executable Entry Points (`police_cli_entrypoint_runner`)

### Task Breakdown & Progress Tracking

#### Phase 1: CLI Argument Parsing & Setup
- [x] Task 1.1: Create `src/cli.py` implementing `parse_args()` with `peer` and `replay` subparsers.
- [x] Task 1.2: Create root `main.py` delegating execution to `src/cli.py`.

#### Phase 2: Subcommand Execution Wiring
- [x] Task 2.1: Wire `peer` subcommand to start `FastMCPServer` with `--role`, `--host`, `--port` flags.
- [x] Task 2.2: Wire `replay` subcommand to execute `ReplayVerifierEngine` on `--log` files.
- [x] Task 2.3: Add signal handling for graceful shutdown on Ctrl+C (SIGINT).

#### Phase 3: Testing & CLI Verification
- [x] Task 3.1: Write unit tests in `tests/test_cli.py` testing argument parser options.
- [x] Task 3.2: Verify CLI invocation via `python main.py peer --role police --port 8000`.

### Definition of Done (DoD)
- [x] CLI entry point fully functional.
- [x] All subcommands and flags verified via tests.
