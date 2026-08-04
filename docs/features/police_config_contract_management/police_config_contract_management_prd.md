# Product Requirements Document (PRD)
## Feature: Shared Contract & Configuration Management (`police_config_contract_management`)

### 1. Product Overview & Problem Statement
In a fully decentralized Dec-POMDP multi-agent environment, both peer agents (Police and Thief) must share a cryptographically immutable contract (`config/game.json`) while maintaining strict environment isolation for private configuration files (`config/game.toml`, `.env`).

Without a formal contract management system, peers could run mismatching grid configurations, illegal board sizes, or conflicting turn timeouts, violating zero-trust computational fairness.

### 2. Product Objectives & Target Capabilities
- **Signed Shared Contract**: Enforce standardized shared configuration schema (`config/game.json`) covering grid dimensions, agent start points, scoring rules, scent parameters, and rate limits.
- **Environment Isolation**: Support private per-peer TOML configurations (`config/game.toml`) for port binding, strategy overrides, and local LLM settings without leaking state to opponents.
- **Dependency & Build Standards**: Standardize root dependencies via `pyproject.toml`, lockfiles via `uv.lock`, and environment templates via `.env-example`.

### 3. Detailed Feature Requirements
- **FR-01**: Define `config/game.json` with mandatory keys: `schema_version`, `agreed_between`, `board_and_agents` (`grid_size`, `num_agents`, `thief_start`, `cop_start`, `axis_origin_corner`), `world`, `movement_and_barriers`, `scoring`, `pheromones`, `network_and_league`, and `rate_limiter_gatekeeper`.
- **FR-02**: Support private TOML config (`config/game.toml`) containing `[game]`, `[network]` (`my_port`, `opponent_url`), `[strategy]`, `[trash_talk]`, `[llm]`, and `[email]`.
- **FR-03**: Implement configuration loader with validation against contract rules and environment variable overrides.
- **FR-04**: Generate `.env-example` with placeholders for `API_KEY`, `OAUTH_TOKEN`, and `GMAIL_CREDENTIALS`.
- **FR-05**: Include root `pyproject.toml` with `uv` dependency specifications, `ruff` linter configuration (`select = ["E","F","W","I","N","UP","B","C4","SIM"]`), `pytest` settings, and coverage threshold (`fail_under = 85`).

### 4. Non-Functional Requirements (NFRs)
- **Security & Zero-Trust**: Secrets and private TOML parameters must never be included in `config/game.json` or committed to public Git repositories.
- **Validation**: Contract loader must reject invalid schema versions or out-of-bounds start coordinates upon startup.
- **Reproducibility**: `uv.lock` ensures identical dependency versions across execution environments.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Appendix B / Table 20 format specified in course documentation.
- Automated validation tests pass for both valid and invalid configuration files.
- Zero secret leakage verified via `.gitignore` and `ruff` checks.
