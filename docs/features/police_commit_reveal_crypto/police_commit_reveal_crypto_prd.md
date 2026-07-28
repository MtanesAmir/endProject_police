# Product Requirements Document (PRD)
## Feature: Police Cryptographic Commit-Reveal Protocol Engine (`police_commit_reveal_crypto`)

### 1. Product Overview & Problem Statement
Zero-knowledge non-repudiation security layer executing 4-stage SHA-256 Commit-Reveal protocol to prevent cheat attempts and move tampering.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Generate cryptographically secure 16-byte random hex Nonces using secrets.token_hex(16).
- **FR-02**: Serialize state, move, intent, and nonce into Canonical JSON (sorted keys, fixed separators).
- **FR-03**: Compute SHA-256 hash commitment H_commit = SHA256(canonical_payload).
- **FR-04**: Execute 4-stage turn sequence: 1. Commit -> 2. Acknowledge -> 3. Reveal -> 4. Audit.
- **FR-05**: Validate revealed payloads against initial H_commit commitments.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
