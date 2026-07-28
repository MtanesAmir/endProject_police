# Product Requirements Document (PRD)
## Feature: Police Game Phase Finite State Machine (FSM) (`police_state_machine`)

### 1. Product Overview & Problem Statement
Strict FSM governing valid game states and transitions to prevent deadlocks, out-of-order execution, and technical vulnerabilities.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Maintain strict state machine with phases: WAITING_FOR_OPPONENT, COMPUTING_MOVE, COMMITTING, AWAITING_REVEAL, VERIFYING, TECHNICAL_LOSS.
- **FR-02**: Enforce valid transition lookup table (TRANSITIONS dictionary).
- **FR-03**: Raise ValueError or transition to TECHNICAL_LOSS upon any illegal transition attempt.
- **FR-04**: Ensure immutable current state inspection API for Orchestrator.
- **FR-05**: Prevent deadlock conditions during turn synchronization.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
