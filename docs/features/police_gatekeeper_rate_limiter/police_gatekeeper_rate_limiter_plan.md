# Technical Development Plan
## Feature: Police Gatekeeper Rate Limiter & DOS Detector (`police_gatekeeper_rate_limiter`)

### 1. Technical Architecture & Component Design
As Team Leader, this development plan outlines the engineering implementation of `police_gatekeeper_rate_limiter` based on the product requirements defined in `police_gatekeeper_rate_limiter_prd.md`.

#### Module Architecture
This feature resides within the Police agent codebase and integrates into the system via clean interface boundaries.

```mermaid
graph TD
    Orchestrator[Police Orchestrator] --> FeatureModule[Police Gatekeeper Rate Limiter & DOS Detector]
    FeatureModule --> DomainState[Domain State / Grid State]
    FeatureModule --> Logger[Audit Logger]
```

### 2. Technical Component Breakdown
- **Component 1**: Create TokenBucket class in src/infra/rate_limiter.py with capacity C and refill_rate r.
- **Component 2**: Implement allow(cost=1.0) -> bool method.
- **Component 3**: Create DOSDetector monitoring incoming request rates.
- **Component 4**: Integrate Gatekeeper middleware before outgoing MCP client calls.

### 3. Dependencies & Internal Integrations
- **Language / Runtime**: Python 3.11+
- **Internal Modules**: `src/core/orchestrator.py`, `src/core/state_machine.py`, `src/domain/`
- **External Libraries**: Standard Python Library (`hashlib`, `secrets`, `dataclasses`, `typing`, `json`, `math`, `asyncio`).

### 4. Implementation Strategy & Risk Mitigation
- **Phased Rollout**: Implement core interface data types first, followed by business logic and unit test suite.
- **Risk Mitigation**: Strict boundary checks and zero-trust verification to prevent invalid game state transitions or out-of-order execution.
