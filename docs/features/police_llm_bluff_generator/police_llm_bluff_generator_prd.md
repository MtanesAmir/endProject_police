# Product Requirements Document (PRD)
## Feature: Police LLM Verbal Hint & Bluff Generator (`police_llm_bluff_generator`)

### 1. Product Overview & Problem Statement
Psychological verbal communication module generating text hints and bluffs (trash_talk) across multiple providers while adhering to token budgets.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Support 4 LLM providers for trash_talk: template (0 tokens), ollama (local), claude_api, claude_cli.
- **FR-02**: Enforce hard token usage budget per series (default token_budget_per_series = 200,000).
- **FR-03**: Generate deceptive or truthful text hints about Police movement intentions.
- **FR-04**: Isolate text generation failures so they never crash or corrupt movement calculation.
- **FR-05**: Enforce max word limit per hint (default hint_max_words = 15).

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
