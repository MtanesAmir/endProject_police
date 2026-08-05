# Granular Developer TODO Checklist
## Feature: Gmail OAuth 2.0 Setup Utility Flow (`police_gmail_oauth_setup_flow`)

### Task Breakdown & Progress Tracking

#### Phase 1: OAuth Setup Manager Implementation
- [x] Task 1.1: Create `src/automation/oauth_flow.py` with `OAuthSetupManager`.
- [x] Task 1.2: Implement `get_credentials()` with `token.json` refresh and mock fallback.

#### Phase 2: GmailReporter Integration
- [x] Task 2.1: Wire `OAuthSetupManager` into `GmailReporter.send_gmail_report()`.
- [x] Task 2.2: Verify least-privilege `gmail.send` scope usage.

#### Phase 3: Testing & Verification
- [x] Task 3.1: Write unit tests in `tests/test_oauth_flow.py`.
- [x] Task 3.2: Verify offline mock fallback mode in automated test runs.

### Definition of Done (DoD)
- [x] OAuth setup manager implemented, integrated, and passing tests.
