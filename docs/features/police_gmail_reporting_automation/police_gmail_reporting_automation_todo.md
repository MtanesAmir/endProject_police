# Granular Developer TODO Checklist
## Feature: Police Match Report Builder & Automated Gmail Reporter (`police_gmail_reporting_automation`)

This task list breaks down the implementation plan from `police_gmail_reporting_automation_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_gmail_reporting_automation`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_gmail_reporting_automation.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create report_compiler.py and gmail_reporter.py in src/reporting/
- [x] Task 2.2: Implement compile_match_reports(match_data) -> dict[filename, content]
- [x] Task 2.3: Implement send_gmail_report(recipient, subject, body_json)
- [x] Task 2.4: Ensure credentials.json and token.json are listed in .gitignore
- [x] Task 2.5: Write unit tests for report package JSON schema validity

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_gmail_reporting_automation` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_gmail_reporting_automation_prd.md`.
