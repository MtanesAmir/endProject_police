# Technical Development Plan
## Feature: Police LLM Verbal Hint & Bluff Generator (`police_llm_bluff_generator`)

### 1. Technical Architecture & Component Design
As Team Leader, this development plan outlines the engineering implementation of `police_llm_bluff_generator` based on the product requirements defined in `police_llm_bluff_generator_prd.md`.

#### Module Architecture
This feature resides within the Police agent codebase and integrates into the system via clean interface boundaries.

```mermaid
graph TD
    Orchestrator[Police Orchestrator] --> FeatureModule[Police LLM Verbal Hint & Bluff Generator]
    FeatureModule --> DomainState[Domain State / Grid State]
    FeatureModule --> Logger[Audit Logger]
```

### 2. Technical Component Breakdown
- **Component 1**: Design LLMProvider factory pattern in src/infra/llm_provider.py.
- **Component 2**: Implement TemplateProvider (0 tokens, python fallback strings).
- **Component 3**: Implement OllamaProvider, ClaudeAPIProvider, and ClaudeCLIProvider adapters.
- **Component 4**: Build TokenBudgetTracker monitoring cumulative token usage.

### 3. Dependencies & Internal Integrations
- **Language / Runtime**: Python 3.11+
- **Internal Modules**: `src/core/orchestrator.py`, `src/core/state_machine.py`, `src/domain/`
- **External Libraries**: Standard Python Library (`hashlib`, `secrets`, `dataclasses`, `typing`, `json`, `math`, `asyncio`).

### 4. Implementation Strategy & Risk Mitigation
- **Phased Rollout**: Implement core interface data types first, followed by business logic and unit test suite.
- **Risk Mitigation**: Strict boundary checks and zero-trust verification to prevent invalid game state transitions or out-of-order execution.
