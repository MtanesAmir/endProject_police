# Product Requirements Document (PRD)
## Feature: Thief Evasion Strategy Brain & Dual Match Simulator (`police_thief_evasion_brain`)

### 1. Product Overview & Problem Statement
The Cops-and-Robbers game is a symmetric Dec-POMDP multi-agent competition. While `PoliceBrain` handles Cop pursuit logic, a standalone `ThiefBrain` implementation (`src/strategy/thief_brain.py`) is required to simulate Thief evasion dynamics, scent trail deception, bluffing, and survival optimization up to turn 35.

Without an independent `ThiefBrain`, full P2P end-to-end simulations cannot be tested locally.

### 2. Product Objectives & Target Capabilities
- **Independent Thief AI (`ThiefBrain`)**: Subclass of `BrainBase` optimizing Thief distance maximize (Manhattan distance from Cop), barrier-aware survival, and scent trail dilution.
- **Deception & Bluff Generation**: Produce verbal bluffs (e.g. misleading directional hints) to confuse the Cop's Bayesian belief map while maintaining strict physical move legality.
- **Dual Match Orchestrator**: Run complete Cop vs Thief peer matches over FastMCP/JSON-RPC without central server dependency.

### 3. Detailed Feature Requirements
- **FR-01**: Implement `ThiefBrain` in `src/strategy/thief_brain.py` inheriting from `BrainBase`.
- **FR-02**: Implement `_pick_move(state, valid_moves)` selecting moves that maximize Manhattan distance from Cop while avoiding dead-ends and barriers.
- **FR-03**: Implement `_decide_bluff(state, chosen_move)` generating deceptive verbal hints (e.g., announcing "I moved North" when moving East).
- **FR-04**: Support Q-learning and heuristic fallback policy modes for the Thief agent.
- **FR-05**: Implement `MatchRunner` orchestrating a full 35-turn game between `PoliceBrain` and `ThiefBrain`.

### 4. Non-Functional Requirements (NFRs)
- **Zero Memory Leak**: Thief state and Cop state must execute in separate memory spaces (`Processes` or isolated classes).
- **Latency**: Move decision calculation must take < 50ms per step.
- **Determinism**: Supports fixed seed mode for repeatable test scenarios.

### 5. Success Metrics & Acceptance Criteria
- `ThiefBrain` achieves survival up to 35 steps against baseline heuristic Cop strategies in test environments.
- 100% legal physical moves generated (no wall collisions or invalid diagonal steps).
- Passing unit test suite covering `ThiefBrain` and `MatchRunner`.
