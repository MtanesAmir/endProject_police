# Granular Developer TODO Checklist
## Feature: Police LLM Verbal Hint & Bluff Generator (`police_llm_bluff_generator`)

This task list breaks down the implementation plan from `police_llm_bluff_generator_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [ ] Task 1.1: Define data types, constants, and interface stubs for `police_llm_bluff_generator`.
- [ ] Task 1.2: Set up unit test file in `tests/test_police_llm_bluff_generator.py`.

#### Phase 2: Core Feature Implementation
- [ ] Task 2.1: Create llm_provider.py in src/infra/
- [ ] Task 2.2: Implement TemplateProvider returning template text with 0 token consumption
- [ ] Task 2.3: Implement OllamaProvider and ClaudeAPIProvider client wrappers
- [ ] Task 2.4: Implement TokenBudgetTracker throwing budget alert when threshold reached
- [ ] Task 2.5: Write unit tests for fallback to TemplateProvider on network error

#### Phase 3: Integration & Testing
- [ ] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [ ] Task 3.2: Run pytest test suite for `police_llm_bluff_generator` and ensure 100% pass rate.
- [ ] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [ ] All code implemented in `src/` following code style standards.
- [ ] Unit tests written and passing in `tests/`.
- [ ] Feature verified against requirements in `police_llm_bluff_generator_prd.md`.
