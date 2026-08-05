# Product Requirements Document (PRD)
## Feature: Annotated Git Submission Tagging (`police_git_submission_tagging`)

### 1. Product Overview & Problem Statement
Per Section 9.4 and Appendix G of `police_thief_p2p.pdf`, final course evaluations require a specific annotated Git submission tag (`v1.0-submission`) on the repository. Evaluators clone tagged release points rather than unstable head commits.

### 2. Product Objectives & Target Capabilities
- **Annotated Release Tag**: Create Git tag `v1.0-submission` containing team identification, release message, and verified commit pointer.
- **Verification Script**: Utility to verify tag creation, commit hash matching, and remote push status.

### 3. Detailed Feature Requirements
- **FR-01**: Execute `git tag -a v1.0-submission -m "Final submission: Police-Thief P2P, group Police-Thief-Team"`.
- **FR-02**: Push tag to remote GitHub repository (`git push origin v1.0-submission`).
- **FR-03**: Verify tag pointer (`git show v1.0-submission`).

### 4. Non-Functional Requirements (NFRs)
- **Immutability**: Once created, submission tag must point to verified test-passing commit.
- **Traceability**: Commit message must match submission guidelines format.

### 5. Success Metrics & Acceptance Criteria
- Git tag `v1.0-submission` present locally and on GitHub origin repository.
- Tag points to commit passing 100% of unit test suite.
