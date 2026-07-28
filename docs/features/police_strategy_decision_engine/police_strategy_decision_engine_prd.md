# Product Requirements Document (PRD)
## Feature: Police Strategy Engine & Brain Base Subclass (`police_strategy_decision_engine`)

### 1. Product Overview & Problem Statement
Core decision-making module extending BrainBase (MyPoliceBrain) that separates movement choices from verbal text generation and supports optional Q-learning.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Subclass BrainBase into MyPoliceBrain in src/strategy/police_brain.py.
- **FR-02**: Override _pick_move(state) and _decide_move(state, barriers) methods.
- **FR-03**: Integrate Manhattan distance and Bayesian belief heuristics for movement calculation.
- **FR-04**: Provide optional Q-learning RL module (Q(s,a) updates, Bellman equation, epsilon-greedy).
- **FR-05**: Strictly enforce architectural separation: movement logic must not depend on LLM text output.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
