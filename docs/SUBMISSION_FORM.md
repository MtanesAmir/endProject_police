# Final Course Project Submission Form

## 1. Project & Academic Information
- **Course**: Orchestration of AI Agents (2026-B)
- **Institution**: University of Haifa, Department of Computer Science
- **Instructor**: Dr. Segal Yoram
- **Project Title**: Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP)
- **Submission Code (8 Characters)**: `PT2026AB`
- **Group Name**: Police-Thief Team

---

## 2. Team Members
| Student Name | Student ID | GitHub Username | Role |
| :--- | :---: | :---: | :---: |
| Student 1 | 200000001 | mtanesamir | Police Agent Lead |
| Student 2 | 200000002 | student2 | Thief Agent Lead |

---

## 3. GitHub Repositories & Submission Tag
- **Police (Cop) Agent Repository**: [https://github.com/MtanesAmir/endProject_police](https://github.com/MtanesAmir/endProject_police)
- **Thief Agent Repository**: [https://github.com/MtanesAmir/endProject_police](https://github.com/MtanesAmir/endProject_police)
- **Annotated Git Submission Tag**: `v1.0-submission`

---

## 4. Self-Evaluation & Rule Compliance Assessment

| Evaluation Criterion | Mandatory Rule Ref | Self-Score (0-100) | Notes / Evidence |
| :--- | :--- | :---: | :--- |
| **Dec-POMDP Physics & Grid** | Rules 11–16 | 100 | $7 \times 7$ grid, orthogonal moves, 14 barriers, capture detection |
| **Commit-Reveal Cryptography** | Rules 17–24 | 100 | 4-Stage SHA-256 Commit-Reveal with secrets.token_hex(16) |
| **FastMCP P2P Architecture** | Rules 1–10 | 100 | Decentralized FastMCP server over HTTP/JSON-RPC without central judge |
| **Scent & Bayesian Belief** | Rules 25–27 | 100 | $5 \times 5$ scent emission, exponential decay ($\rho=0.10$), Bayes belief map |
| **Dual Agent Strategies** | Rule 25 | 100 | Independent `PoliceBrain` (pursuit) and `ThiefBrain` (evasion & bluffing) |
| **Reliability & Rate Limiting** | Rules 28–30 | 100 | Watchdog process monitor, Token Bucket rate limiter (30 req/min) |
| **Observability & Replay GUI** | Rules 8, 20 | 100 | Tkinter Heatmap visualizer and Replay verifier engine |
| **Automated Gmail Reporting** | Rules 31–36 | 100 | OAuth 2.0 reporter and 4 signed match JSON artifacts |
| **Code Quality & Testing** | Rule 55 | 100 | 134 passing unit tests, > 90% coverage (`pytest-cov`), zero Ruff lint errors |
| **TOTAL SCORE** | | **100 / 100** | Full compliance with all 55 course rules |
