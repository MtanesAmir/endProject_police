# Product Requirements Document (PRD)
## Feature: Police Single Gateway Orchestrator (`police_orchestrator_gateway`)

### 1. Product Overview & Problem Statement
Central Orchestrator component acting as a Single Gateway between P2P network, state machine, strategy engine, logger, and watchdog.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Implement Single Gateway pattern (Orchestrator) routing all incoming and outgoing messages.
- **FR-02**: Decouple sub-systems: network server, FSM, strategy brain, log manager, watchdog.
- **FR-03**: Prevent direct cross-module calls without Orchestrator mediation.
- **FR-04**: Handle turn lifecycle from incoming P2P call to commit, reveal, and state transition.
- **FR-05**: Gracefully handle component exceptions and trigger safe shutdown on failure.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
