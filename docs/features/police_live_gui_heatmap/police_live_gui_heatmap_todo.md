# Granular Developer TODO Checklist
## Feature: Police Live GUI & Belief Heatmap Visualizer (`police_live_gui_heatmap`)

This task list breaks down the implementation plan from `police_live_gui_heatmap_plan.md` into small, trackable tasks for developers.

### Task Breakdown & Progress Tracking

#### Phase 1: Setup & Interface Definition
- [x] Task 1.1: Define data types, constants, and interface stubs for `police_live_gui_heatmap`.
- [x] Task 1.2: Set up unit test file in `tests/test_police_live_gui_heatmap.py`.

#### Phase 2: Core Feature Implementation
- [x] Task 2.1: Create live_gui.py in src/gui/
- [x] Task 2.2: Build Tkinter/PyQt window layout with 7x7 grid canvas and status banner
- [x] Task 2.3: Implement update_heatmap(belief_matrix) updating cell background colors
- [x] Task 2.4: Implement update_banner(state_string) changing between GREEN YOUR TURN and GRAY LOCKED
- [x] Task 2.5: Write unit tests verifying local truth filter (ensuring Thief secret position is never rendered)

#### Phase 3: Integration & Testing
- [x] Task 3.1: Wire feature module into `PoliceOrchestrator` gateway (`src/core/orchestrator.py`).
- [x] Task 3.2: Run pytest test suite for `police_live_gui_heatmap` and ensure 100% pass rate.
- [x] Task 3.3: Verify zero-trust environment separation (no shared memory or leaked thief information).

### Definition of Done (DoD)
- [x] All code implemented in `src/` following code style standards.
- [x] Unit tests written and passing in `tests/`.
- [x] Feature verified against requirements in `police_live_gui_heatmap_prd.md`.
