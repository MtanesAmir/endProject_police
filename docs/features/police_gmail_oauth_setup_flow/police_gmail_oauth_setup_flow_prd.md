# Product Requirements Document (PRD)
## Feature: Gmail OAuth 2.0 Setup Utility Flow (`police_gmail_oauth_setup_flow`)

### 1. Product Overview & Problem Statement
Appendix A of `police_thief_p2p.pdf` details the 5 setup steps for Google OAuth 2.0 Gmail API integration to automatically transmit signed match reports (`declaration_*.json`, `config_*.json`, `log_*.json`, `result_*.json`) to the evaluator email.

Setting up OAuth tokens manually via web browser flows can be error-prone for students. A dedicated helper module (`src/automation/oauth_flow.py`) automates token authentication and token refresh.

### 2. Product Objectives & Target Capabilities
- **OAuth Setup Helper**: Module `src/automation/oauth_flow.py` guiding the student through Google Cloud Console authorization.
- **Token Manager**: Converts `credentials.json` into `token.json` using `google-auth-oauthlib`.
- **Offline Fallback**: Automatically falls back to mock/offline mode when running in automated test environments without credentials.

### 3. Detailed Feature Requirements
- **FR-01**: Implement `run_oauth_flow()` in `src/automation/oauth_flow.py`.
- **FR-02**: Load client secrets from `credentials.json` with scope `https://www.googleapis.com/auth/gmail.send`.
- **FR-03**: Save refresh token and access token into `token.json`.
- **FR-04**: Refresh expired access tokens automatically using `RefreshRequest()`.

### 4. Non-Functional Requirements (NFRs)
- **Least Privilege Scope**: Request ONLY `gmail.send` scope (never full mail read/modify scope).
- **Security**: Ensures `credentials.json` and `token.json` are listed in `.gitignore`.

### 5. Success Metrics & Acceptance Criteria
- `token.json` created successfully upon completing authentication flow.
- Graceful mock fallback in CI/test environments without throwing exceptions.
