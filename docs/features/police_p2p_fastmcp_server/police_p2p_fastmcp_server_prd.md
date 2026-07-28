# Product Requirements Document (PRD)
## Feature: Police FastMCP P2P Server & Networking Infrastructure (`police_p2p_fastmcp_server`)

### 1. Product Overview & Problem Statement
Decentralized peer-to-peer communication node using FastMCP framework to expose tools over HTTP and communicate with Thief peer.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Instantiate local FastMCP server instance named police_thief_peer.
- **FR-02**: Expose @mcp.tool receive_move(signed_move: str, signature: str) -> dict.
- **FR-03**: Ensure zero-trust isolation: Police server maintains local truth only.
- **FR-04**: Support HTTP transport binding on 0.0.0.0:8000 (or configured port).
- **FR-05**: Integrate public internet tunneling tools (ngrok / Localtonet) for cross-network play.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
