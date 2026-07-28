# Product Requirements Document (PRD)
## Feature: Police Bayesian Belief Map Engine (`police_bayesian_belief`)

### 1. Product Overview & Problem Statement
Probabilistic Bayesian estimator maintaining a 7x7 probability map b(s) = P(thief = s | scent, hints) combining scent trails and opponent verbal hints.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Maintain normalized probability distribution b(s) over all 49 cells of the 7x7 grid.
- **FR-02**: Update probabilities based on observed scent matrix intensity.
- **FR-03**: Incorporate opponent verbal hints (with reliability coefficient weighting).
- **FR-04**: Detect bluffing when verbal hints contradict observed scent trails.
- **FR-05**: Output highest probability thief location argmax_s b(s).

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
