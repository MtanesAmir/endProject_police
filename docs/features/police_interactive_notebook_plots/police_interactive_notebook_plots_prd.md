# Product Requirements Document (PRD)
## Feature: Interactive Notebook Plots & Visualizations (`police_interactive_notebook_plots`)

### 1. Product Overview & Problem Statement
Per Section 9 of *Software Submission Guidelines V3*, empirical research notebooks (`notebooks/analysis.ipynb`) must include inline visualizations (line charts, heatmaps, bar charts) evaluating game mechanics.

Visual plots demonstrate scent decay trajectories, Bayesian belief grid probability convergence, and strategy win rates.

### 2. Product Objectives & Target Capabilities
- **Inline Matplotlib Plotting**: Generate inline plots in `notebooks/analysis.ipynb` visualizing scent intensity over time and belief grid distributions.
- **Exported Asset Artifacts**: Save high-resolution PNG plot artifacts to `assets/` directory (`assets/scent_decay_plot.png`, `assets/belief_heatmap.png`, `assets/strategy_winrates.png`).

### 3. Detailed Feature Requirements
- **FR-01**: Implement `plot_scent_decay(decay_rate=0.10)` generating turn-by-turn intensity decay curve.
- **FR-02**: Implement `plot_belief_heatmap(belief_matrix)` rendering 2D probability colormap.
- **FR-03**: Implement `plot_strategy_winrates(summary_data)` rendering Cop vs Thief win-rate bar chart.
- **FR-04**: Save plots to `assets/` as PNG files.

### 4. Non-Functional Requirements (NFRs)
- **High Resolution**: Minimum 300 DPI for exported PNG plots.
- **Zero Headless Failures**: Supports non-interactive `Agg` backend execution for CI test environments.

### 5. Success Metrics & Acceptance Criteria
- PNG plot artifacts generated in `assets/`.
- Notebook executes top-to-bottom without plotting errors.
