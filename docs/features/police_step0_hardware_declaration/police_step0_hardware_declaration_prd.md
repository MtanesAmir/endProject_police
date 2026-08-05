# Product Requirements Document (PRD)
## Feature: Step-0 System Hardware Auto-Discovery (`police_step0_hardware_declaration`)

### 1. Product Overview & Problem Statement
Section 5.5 (*Step-0 and Computational Fairness*) requires automatic reporting of hardware specs (OS, CPU model, RAM size, VRAM/GPU, Python runtime version, and current Git commit hash) before game execution starts.

Without automated hardware discovery, human error or manual config mistakes could invalidate the `declaration_police.json` artifact submitted to the evaluator.

### 2. Product Objectives & Target Capabilities
- **Automated Hardware Profiler**: Auto-detect OS platform, CPU architecture/core count, total RAM, GPU presence, Python version, and current Git commit hash.
- **Declaration Artifact Integration**: Inject auto-discovered hardware specs into `declaration_police.json` and `declaration_thief.json`.

### 3. Detailed Feature Requirements
- **FR-01**: Implement `get_system_specs()` in `src/domain/hardware.py`.
- **FR-02**: Retrieve platform OS (`platform.system()`, `platform.release()`).
- **FR-03**: Retrieve CPU core count (`os.cpu_count()`) and RAM size.
- **FR-04**: Extract current Git commit hash (`git rev-parse HEAD` via subprocess).
- **FR-05**: Include hardware dict inside `GmailReporter.compile_match_reports()`.

### 4. Non-Functional Requirements (NFRs)
- **Fallback Safe**: Must fail gracefully to default string values if system commands (e.g. `git`) are unavailable.
- **Zero Overhead**: Discovery completed in < 10ms.

### 5. Success Metrics & Acceptance Criteria
- `declaration_police.json` contains complete hardware profile dict.
- 100% test coverage in `tests/test_hardware.py`.
