# Product Requirements Document (PRD)
## Feature: Police Capture Detection & Claim Engine (`police_capture_mechanics`)

### 1. Product Overview & Problem Statement
Rules and triggers for detecting when the Thief is caught (occupying same cell or fully enclosed by barriers) and issuing a formal cryptographic Capture Claim.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Detect direct capture when Police position matches Thief position on the 7x7 grid.
- **FR-02**: Detect indirect trapping when Thief has 0 legal moves available due to surrounding barriers/edges.
- **FR-03**: Trigger formal Capture Claim declaration in turn payload (capture_cop = 20 score, capture_thief = 5 score).
- **FR-04**: Validate capture claims against opponent revealed positions.
- **FR-05**: End match upon successful capture verification.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
