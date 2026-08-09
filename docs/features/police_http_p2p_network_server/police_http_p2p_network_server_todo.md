# Granular Developer TODO Checklist
## Feature: P2P FastMCP HTTP Server Transport Binding (`police_http_p2p_network_server`)

### Task Breakdown & Progress Tracking

#### Phase 1: HTTP Request Handler Implementation
- [x] Task 1.1: Implement `FastMCPHTTPHandler` in `src/p2p/server.py`.
- [x] Task 1.2: Handle POST routes `/` and `/mcp` dispatching JSON-RPC requests.

#### Phase 2: Background Server & Client Methods
- [x] Task 2.1: Implement `start(background=True)` launching `HTTPServer` on daemon thread.
- [x] Task 2.2: Implement `call_opponent(method, params)` sending JSON-RPC POST requests.
- [x] Task 2.3: Implement `stop()` shutting down server cleanly.

#### Phase 3: Testing & Inter-Process Verification
- [x] Task 3.1: Write unit tests in `tests/test_police_p2p_fastmcp_server.py`.
- [x] Task 3.2: Verify inter-peer HTTP request exchange across two ports.

### Definition of Done (DoD)
- [x] Real HTTP transport implemented and verified via unit tests.
