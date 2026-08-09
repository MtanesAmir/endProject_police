# Product Requirements Document (PRD)
## Feature: P2P FastMCP HTTP Server Transport Binding (`police_http_p2p_network_server`)

### 1. Product Overview & Problem Statement
Chapter 2 (Section 2.3) and Chapter 10 (Phase 2) require running local FastMCP peer servers over real HTTP transport, allowing Cop and Thief processes in separate terminal windows to send and receive live JSON-RPC messages (`http://127.0.0.1:8802/mcp` and `http://127.0.0.1:8801/mcp`).

Without background HTTP server listening, inter-process communication between independently running terminals cannot exchange live turn messages.

### 2. Product Objectives & Target Capabilities
- **HTTP Server Transport**: Support starting a background non-blocking HTTP server in `FastMCPServer.start(background=True)` listening for HTTP POST requests.
- **JSON-RPC Dispatcher**: Parse JSON-RPC 2.0 requests for `send_commitment`, `reveal_move`, `receive_move`, and `get_status`.
- **Inter-Peer HTTP Client**: Support sending JSON-RPC HTTP POST requests to the opponent peer URL (`opponent_url`).

### 3. Detailed Feature Requirements
- **FR-01**: Implement lightweight HTTP request handler `FastMCPHTTPHandler` in `src/p2p/server.py`.
- **FR-02**: Support background thread HTTP server (`threading.Thread` with `http.server.HTTPServer`).
- **FR-03**: Handle HTTP POST requests containing JSON-RPC payloads and respond with JSON results.
- **FR-04**: Implement client method `call_opponent(method, params)` sending HTTP POST requests to `opponent_url`.
- **FR-05**: Implement graceful server shutdown via `server.stop()`.

### 4. Non-Functional Requirements (NFRs)
- **Zero Heavy Dependencies**: Built on standard Python `http.server` and `urllib.request` with optional `fastmcp` / `requests` enhancements.
- **Thread Safe**: Server operations and commitment ledgers protected via thread synchronization.

### 5. Success Metrics & Acceptance Criteria
- Cop and Thief servers can send and receive HTTP POST requests across ports.
- 100% test coverage in `tests/test_police_p2p_fastmcp_server.py`.
