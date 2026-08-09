# Product Requirements Document (PRD)
## Feature: Empirical Research & Performance Analysis Report (`police_research_performance_report`)

### 1. Product Overview & Problem Statement
Appendix D (Section 4) and Guidelines Section 9 require a comprehensive performance analysis research document (`docs/RESEARCH-REPORT-Performance-Analysis.md`).

This report provides quantitative analysis of LLM providers (Template, Ollama, Claude API, Claude CLI), token budgets, execution latency, rate-limit backoff dynamics, and parameter sensitivity for scent decay ($\rho$).

### 2. Product Objectives & Target Capabilities
- **LLM Provider Comparison**: Benchmark token consumption, monetary cost, and response latency across Template, Ollama, Claude API (Haiku/Opus), and Claude CLI.
- **Sensitivity Analysis**: Quantitative evaluation of scent decay rates ($\rho \in [0.05, 0.20]$) and impact on Cop capture steps.
- **System Robustness Analysis**: Evaluation of Gatekeeper rate limiting and Watchdog resilience under high concurrency.

### 3. Detailed Feature Requirements
- **FR-01**: Author `docs/RESEARCH-REPORT-Performance-Analysis.md` with comparative benchmarking tables.
- **FR-02**: Analyze token cost vs reasoning performance for bluff generation.
- **FR-03**: Document exponential backoff and rate-limit recovery under Google API quota limits.
- **FR-04**: Present empirical data from 50 Monte Carlo match simulations.

### 4. Non-Functional Requirements (NFRs)
- **Academic Rigor**: Formally structured with introduction, experimental methodology, quantitative tables, and conclusion.
- **Reproducibility**: Clear instructions to reproduce benchmark metrics using `src/experiments/benchmark.py`.

### 5. Success Metrics & Acceptance Criteria
- `docs/RESEARCH-REPORT-Performance-Analysis.md` authored and complete.
- Contains verified metrics matching textbook Appendix D standards.
