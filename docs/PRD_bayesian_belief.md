# Mechanism PRD: Bayesian Belief Grid Engine

### 1. Overview
The Bayesian Belief Grid maintains a 2D probability distribution map over the discrete $7 \times 7$ grid representing the Cop's probability estimate of the Thief's position $P(\text{Thief} = s | \text{hints}, \text{scent})$.

### 2. Functional Requirements
- **FR-01**: Initialize uniform probability prior over all valid grid cells ($P(s_i) = 1 / N_{cells}$).
- **FR-02**: Update prior using Bayes' rule upon receiving scent emission values $\tau_{ij}$.
- **FR-03**: Incorporate verbal direction hints with reliability weight parameters.
- **FR-04**: Normalize probability grid after every turn update ($\sum P(s_i) = 1.0$).

### 3. Implementation References
- Implementation: `src/domain/belief.py` & `src/strategy/bayesian.py`
- Test suite: `tests/test_police_bayesian_belief.py`
