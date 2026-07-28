# Product Requirements Document (PRD)
## Feature: Police Match Report Builder & Automated Gmail Reporter (`police_gmail_reporting_automation`)

### 1. Product Overview & Problem Statement
Automated submission pipeline compiling 4 signed JSON match artifacts and transmitting them via OAuth 2.0 Gmail API to the evaluator.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Compile 4 mandatory JSON report files: declaration_*.json, config_*.json, log_*.json, result_*.json.
- **FR-02**: Include commit hash, GitHub repo URLs, token consumption stats, and final scores.
- **FR-03**: Authenticate via OAuth 2.0 with send-only scope (https://www.googleapis.com/auth/gmail.send).
- **FR-04**: Load credentials from credentials.json and token.json (ensuring gitignore protection).
- **FR-05**: Send automated match summary email to evaluator address upon match completion.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
