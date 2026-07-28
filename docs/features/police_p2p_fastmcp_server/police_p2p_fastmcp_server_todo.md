# Granular Developer TODO Checklist
## Feature: Police FastMCP P2P Server & Networking Infrastructure (`police_p2p_fastmcp_server`)

This task list breaks down the implementation plan from `police_p2p_fastmcp_server_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_p2p_fastmcp_server`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_p2p_fastmcp_server.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create mcp_server.py in src/network/
- [ ] Task 2.2: Define FastMCP("police_thief_peer") instance and @mcp.tool receive_move handler
- [ ] Task 2.3: Implement signature verification check before accepting move
- [ ] Task 2.4: Add configuration loader for local port and opponent URL
- [ ] Task 2.5: Write unit tests for receive_move endpoint acceptance and rejection

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_p2p_fastmcp_server` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_p2p_fastmcp_server_prd.md`.
