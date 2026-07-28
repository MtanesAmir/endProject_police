# Product Requirements Document (PRD)
## Feature: Police Replay Viewer & Cryptographic Log Verifier (`police_replay_verifier`)

### 1. Product Overview & Problem Statement
Post-match audit tool and replay viewer loading match JSON logs, performing step-by-step cryptographic verification of SHA-256 commitments, and detecting tampering.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Load match replay JSON file (logs/police_match.json).
- **FR-02**: Step through recorded turns (nonce, move, intent, commit hash).
- **FR-03**: Recompute SHA-256 hash for each step: recomputed = SHA256(nonce | move | intent | state).
- **FR-04**: Compare recomputed hash against original commit hash stored in log.
- **FR-05**: Display GREEN "Verified OK" stamp if all match, or RED "TAMPERED" banner disqualifying match on first mismatch.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
