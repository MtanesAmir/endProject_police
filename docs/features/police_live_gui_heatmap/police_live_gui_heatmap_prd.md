# Product Requirements Document (PRD)
## Feature: Police Live GUI & Belief Heatmap Visualizer (`police_live_gui_heatmap`)

### 1. Product Overview & Problem Statement
Interactive graphical user interface displaying Police local truth view, dynamic Bayesian belief heatmap, and real-time turn status banner.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Render 7x7 grid visualization showing local truth (Police position, placed barriers).
- **FR-02**: Display dynamic Bayesian belief heatmap overlay mapping probability b(s) to color intensity (higher probability -> deeper red).
- **FR-03**: Display Turn Status Banner: GREEN "YOUR TURN" (inputs enabled) vs GRAY "LOCKED" (waiting for opponent / commit sent).
- **FR-04**: Strictly enforce local truth isolation: NEVER display global Thief position (no bird's-eye cheating view).
- **FR-05**: Provide responsive UI event loop without blocking networking or decision threads.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
