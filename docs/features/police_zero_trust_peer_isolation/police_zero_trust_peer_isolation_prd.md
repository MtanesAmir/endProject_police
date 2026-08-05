# Product Requirements Document (PRD)
## Feature: Zero-Trust Peer Config Isolation (`police_zero_trust_peer_isolation`)

### 1. Product Overview & Problem Statement
Section 2.4.2 of `police_thief_p2p.pdf` mandates strict zero-trust environment separation between Police and Thief peer agents (`config/police/` vs `config/thief/`).

Shared memory references or unified config folders risk leaking hidden game state (such as Thief coordinates or nonce seeds) between opponent processes.

### 2. Product Objectives & Target Capabilities
- **Isolated Peer Config Directories**: Support distinct configuration paths (`config/police/game.toml` and `config/thief/game.toml`).
- **Role-Based Config Loader**: `ConfigLoader` loads private TOML configuration based on active role (`--role police` vs `--role thief`).
- **Zero-Trust Memory Guard**: Enforce strict copy-by-value data isolation across network boundaries.

### 3. Detailed Feature Requirements
- **FR-01**: Create `config/police/game.toml` with Police-specific settings (`my_port = 8802`, `opponent_url = "http://127.0.0.1:8801/mcp"`).
- **FR-02**: Create `config/thief/game.toml` with Thief-specific settings (`my_port = 8801`, `opponent_url = "http://127.0.0.1:8802/mcp"`).
- **FR-03**: Update `ConfigLoader` to support role-specific directory resolution.
- **FR-04**: Validate that no shared mutable state exists between peers during simulation runs.

### 4. Non-Functional Requirements (NFRs)
- **Security**: Zero state leakage across process boundaries.
- **Backward Compatibility**: Fallback to `config/game.toml` if role subdirectory is absent.

### 5. Success Metrics & Acceptance Criteria
- `config/police/game.toml` and `config/thief/game.toml` created and loaded independently.
- Tests pass verifying isolated config loading for both roles.
