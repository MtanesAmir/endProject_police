# Product Requirements Document (PRD)
## Feature: Police Scent Field & Stigmergic Trail Tracker (`police_scent_tracking`)

### 1. Product Overview & Problem Statement
Passive scent perception system tracking thief movement trails via 5x5 dynamic scent emission fields and exponential per-turn decay.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Parse 5x5 scent emission grid centered at agent positions with center intensity tau = 0.90.
- **FR-02**: Apply radial intensity decay for surrounding cells in the 5x5 window.
- **FR-03**: Apply per-turn global scent decay rate rho = 0.10 (90% intensity retention per turn).
- **FR-04**: Accumulate historical scent levels across turns to reconstruct opponent movement trails.
- **FR-05**: Expose scent matrix data to the Bayesian belief update engine.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
