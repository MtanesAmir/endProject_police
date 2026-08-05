# Granular Developer TODO Checklist
## Feature: Step-0 System Hardware Auto-Discovery (`police_step0_hardware_declaration`)

### Task Breakdown & Progress Tracking

#### Phase 1: Hardware Profiler Implementation
- [x] Task 1.1: Create `src/domain/hardware.py` defining `SystemProfiler`.
- [x] Task 1.2: Implement `get_system_specs()` collecting OS, CPU, Python version, and Git commit hash.

#### Phase 2: Artifact & Reporter Integration
- [x] Task 2.1: Integrate `SystemProfiler.get_system_specs()` into `GmailReporter.compile_match_reports()`.
- [x] Task 2.2: Ensure `declaration_police.json` includes `hardware_specs` payload.

#### Phase 3: Testing & Verification
- [x] Task 3.1: Write unit tests in `tests/test_hardware.py`.
- [x] Task 3.2: Verify hardware specs dictionary structure.

### Definition of Done (DoD)
- [x] Hardware profiler module implemented, integrated, and verified via tests.
