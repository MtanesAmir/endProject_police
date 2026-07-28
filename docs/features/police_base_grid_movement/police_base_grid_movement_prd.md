# Product Requirements Document (PRD)
## Feature: Police Base Grid & Movement Engine (`police_base_grid_movement`)

### 1. Product Overview & Problem Statement
Core grid representation (7x7), coordinate system, boundary validation, and legal orthogonal movement choices (UP, DOWN, LEFT, RIGHT, STAY) for the Police agent.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Support discrete 7x7 grid (or configurable N x N) with origin (0,0) at top-left corner.
- **FR-02**: Maintain Police initial position at (0,0) index.
- **FR-03**: Enforce orthogonal movement set: NORTH (up), SOUTH (down), EAST (right), WEST (left), STAY.
- **FR-04**: Prevent diagonal moves or moves outside grid boundaries [0..6].
- **FR-05**: Provide API to query current position and preview target positions.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
