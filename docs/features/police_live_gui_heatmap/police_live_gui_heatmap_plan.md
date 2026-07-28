# Technical Development Plan
## Feature: Police Live GUI & Belief Heatmap Visualizer (`police_live_gui_heatmap`)

### 1. Technical Architecture & Component Design
As Team Leader, this development plan outlines the engineering implementation of `police_live_gui_heatmap` based on the product requirements defined in `police_live_gui_heatmap_prd.md`.

#### Module Architecture
This feature resides within the Police agent codebase and integrates into the system via clean interface boundaries.

```mermaid
graph TD
    Orchestrator[Police Orchestrator] --> FeatureModule[Police Live GUI & Belief Heatmap Visualizer]
    FeatureModule --> DomainState[Domain State / Grid State]
    FeatureModule --> Logger[Audit Logger]
```

### 2. Technical Component Breakdown
- **Component 1**: Build LiveGUI window using Tkinter or PyQt in src/gui/live_gui.py.
- **Component 2**: Implement GridCanvas drawing 7x7 cells, Cop icon (C), and barriers (B).
- **Component 3**: Implement HeatmapRenderer mapping float probabilities [0.0..1.0] to color gradients.
- **Component 4**: Implement BannerController updating turn state text and color.

### 3. Dependencies & Internal Integrations
- **Language / Runtime**: Python 3.11+
- **Internal Modules**: `src/core/orchestrator.py`, `src/core/state_machine.py`, `src/domain/`
- **External Libraries**: Standard Python Library (`hashlib`, `secrets`, `dataclasses`, `typing`, `json`, `math`, `asyncio`).

### 4. Implementation Strategy & Risk Mitigation
- **Phased Rollout**: Implement core interface data types first, followed by business logic and unit test suite.
- **Risk Mitigation**: Strict boundary checks and zero-trust verification to prevent invalid game state transitions or out-of-order execution.
