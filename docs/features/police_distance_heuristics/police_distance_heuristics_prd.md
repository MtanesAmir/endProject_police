# Product Requirements Document (PRD)
## Feature: Police Manhattan Distance & Target Heuristics (`police_distance_heuristics`)

### 1. Product Overview & Problem Statement
Pathfinding and target selection heuristic module calculating Manhattan distance D = |x_cop - x_target| + |y_cop - y_target| towards highest probability belief targets.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Calculate Manhattan distance between Police location and any target grid cell.
- **FR-02**: Identify target cell s_target = argmax_s b(s) from Bayesian belief map.
- **FR-03**: Evaluate candidate moves (N, S, E, W, STAY) to minimize Manhattan distance to target.
- **FR-04**: Account for impassable barriers when selecting optimal step direction.
- **FR-05**: Provide fallback exploration moves when belief map is uniform.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
