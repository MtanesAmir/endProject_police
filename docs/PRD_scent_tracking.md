# Mechanism PRD: Dynamic Scent Emission & Decay Model

### 1. Overview
The Scent Tracking engine models indirect stigmergic coordination via radial scent trail emission at the Thief's position and exponential decay over time.

### 2. Functional Requirements
- **FR-01**: Emit radial 5x5 scent pattern centered at Thief's position with max intensity $\tau_{center} = 0.9$.
- **FR-02**: Apply turn-by-turn exponential decay rule: $\tau_{ij}(t+1) = \max(0, (1-\rho)\tau_{ij}(t) + \Delta\tau_{ij})$ with decay rate $\rho = 0.10$.
- **FR-03**: Maintain scent map history for trajectory reconstruction.

### 3. Implementation References
- Implementation: `src/domain/scent.py`
- Test suite: `tests/test_police_scent_tracking.py`
