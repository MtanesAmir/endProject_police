# Mechanism PRD: SHA-256 Commit-Reveal Cryptographic Protocol

### 1. Overview
The SHA-256 Commit-Reveal protocol provides cryptographic non-repudiation and zero-trust verification for turn-based moves between P2P peers (Cop and Thief).

### 2. Functional Requirements
- **FR-01**: Generate 16-byte random hex Nonce (`secrets.token_hex(16)`).
- **FR-02**: Serialize state, move, intent, and nonce into Canonical JSON.
- **FR-03**: Calculate hash $H_{commit} = \text{SHA256}(\text{CanonicalJSON})$.
- **FR-04**: Execute 4-stage turn sequence: 1. Commit -> 2. Acknowledge -> 3. Reveal -> 4. Audit.
- **FR-05**: Detect log tampering and output `Verified OK` or `TAMPERED`.

### 3. Implementation References
- Implementation: `src/security/commit_reveal.py` & `src/domain/crypto.py`
- Test suite: `tests/test_police_commit_reveal_crypto.py`
