# Granular Developer TODO Checklist
## Feature: Interactive Notebook Plots & Visualizations (`police_interactive_notebook_plots`)

### Task Breakdown & Progress Tracking

#### Phase 1: Plotting Utility Engine
- [x] Task 1.1: Create `src/experiments/plotter.py` with matplotlib plot generators.
- [x] Task 1.2: Implement `plot_scent_decay()`, `plot_belief_heatmap()`, `plot_strategy_winrates()`.

#### Phase 2: Notebook & Asset Export Integration
- [x] Task 2.1: Integrate plot generator into `src/experiments/benchmark.py`.
- [x] Task 2.2: Export PNG plot artifacts to `assets/` directory.

#### Phase 3: Testing & Verification
- [x] Task 3.1: Write unit tests in `tests/test_plotter.py`.
- [x] Task 3.2: Verify PNG plot creation in `assets/`.

### Definition of Done (DoD)
- [x] Plotting utility implemented, PNG plots exported to `assets/`, and tests passing.
