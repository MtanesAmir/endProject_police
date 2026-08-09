# Product Requirements Document (PRD)
## Feature: Academic Submission Form Evaluation Summary (`police_submission_form_evaluation`)

### 1. Product Overview & Problem Statement
Chapter 11 (Section 11.5) and Table 11 (Rules 43-45) of `police_thief_p2p.pdf` require completing the official course submission template documenting group member IDs, 8-character unique team submission code, cross-repository links (Cop and Thief), and self-assessment evaluation scores.

### 2. Product Objectives & Target Capabilities
- **Submission Form Summary**: Complete `docs/SUBMISSION_FORM.md` following course submission template guidelines.
- **Repository Links**: Cross-link Cop and Thief GitHub repositories.
- **Verification Score**: Provide self-assessment grade based on code quality and Dec-POMDP adherence.

### 3. Detailed Feature Requirements
- **FR-01**: Author `docs/SUBMISSION_FORM.md` with group metadata, members, and 8-character code (`PT2026AB`).
- **FR-02**: Document repository links (`https://github.com/MtanesAmir/endProject_police`).
- **FR-03**: Fill out self-evaluation metrics checklist based on 55 mandatory course rules.

### 4. Non-Functional Requirements (NFRs)
- **Completeness**: All form fields filled according to course guidelines without missing entries.

### 5. Success Metrics & Acceptance Criteria
- `docs/SUBMISSION_FORM.md` present and filled out.
