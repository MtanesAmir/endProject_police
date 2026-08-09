# Product Requirements Document (PRD)
## Feature: Custom Strategy Brain Integration Guide (`police_custom_strategy_guide`)

### 1. Product Overview & Problem Statement
Chapter 6 (Section 6.2) and Appendix F (Table 22) of `police_thief_p2p.pdf` specify that student teams must be able to plug in custom decision brains for both Police and Thief agents by specifying the class path (`package.module:Class`) in `config/game.toml`.

`docs/STRATEGY.md` must clearly document the `BrainBase` abstract API, heuristic implementations, Bayesian belief integration, and dynamic class loading mechanisms.

### 2. Product Objectives & Target Capabilities
- **Strategy Integration Guide**: Complete `docs/STRATEGY.md` detailing subclassing from `BrainBase`.
- **Dynamic Brain Loader**: Support loading custom brain classes dynamically from `package.module:Class` string format.
- **Decision Engine Interface**: Define `_pick_move(state, valid_moves)` and `_decide_move(state, barriers)` contracts.

### 3. Detailed Feature Requirements
- **FR-01**: Author `docs/STRATEGY.md` with complete API reference for `BrainBase`, `MyPoliceBrain`, and `ThiefBrain`.
- **FR-02**: Document Manhattan heuristic, Chebyshev distance, and shortest path BFS algorithms.
- **FR-03**: Document Q-learning Bellman update equations and hyperparameters ($\alpha=0.10, \gamma=0.95, \epsilon=0.10$).
- **FR-04**: Provide code examples demonstrating dynamic brain loading via `importlib`.

### 4. Non-Functional Requirements (NFRs)
- **Modularity**: Brain strategies must remain decoupled from network transport and P2P communication.
- **Clarity**: Clear mathematical formulations and Python snippets.

### 5. Success Metrics & Acceptance Criteria
- `docs/STRATEGY.md` authored and referenced in project documentation.
- Custom brain subclasses loadable and executable via standard configuration strings.
