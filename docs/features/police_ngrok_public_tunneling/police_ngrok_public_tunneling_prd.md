# Product Requirements Document (PRD)
## Feature: Public Tunneling Integration (`police_ngrok_public_tunneling`)

### 1. Product Overview & Problem Statement
Section 2.4 of `police_thief_p2p.pdf` details public internet tunneling via `ngrok` or `Localtonet`. In remote league matches against opponent teams across different local networks, peers cannot connect directly to `http://localhost:8000` due to NAT routers.

A public HTTPS tunnel exposes the local FastMCP server port safely to a public URL endpoint.

### 2. Product Objectives & Target Capabilities
- **Tunnel Manager**: Module `src/network/tunnel.py` creating ngrok/HTTP tunnels for local port bindings.
- **Public URL Resolution**: Expose public HTTPS endpoint URL to opponent peer.
- **NAT Traversal**: Enables remote P2P FastMCP communication.

### 3. Detailed Feature Requirements
- **FR-01**: Implement `TunnelManager` in `src/network/tunnel.py`.
- **FR-02**: Support starting ngrok tunnel on specified local port (`port = 8000`).
- **FR-03**: Retrieve public HTTPS endpoint URL (`https://xxxx.ngrok-free.app`).
- **FR-04**: Support mock fallback for offline or local testing.

### 4. Non-Functional Requirements (NFRs)
- **Security**: Public tunnel handles HTTPS encryption for transit data.
- **Fault Tolerance**: Automatically shuts down tunnel on server exit.

### 5. Success Metrics & Acceptance Criteria
- Public URL successfully generated for port bindings.
- Passing unit tests in `tests/test_tunnel.py`.
