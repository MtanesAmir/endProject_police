# Product Requirements Document (PRD)
## Feature: Police Gatekeeper Rate Limiter & DOS Detector (`police_gatekeeper_rate_limiter`)

### 1. Product Overview & Problem Statement
Network defense layer implementing Token Bucket rate limiting and DOS anomaly detection to prevent API flooding and HTTP 429 errors.

In the context of the Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) architecture, this feature provides essential capabilities specifically designed for the Police agent character to operate autonomously, securely, and strategically without reliance on a central server or judge.

### 2. Product Objectives & Target Capabilities
- **Decentralized Execution**: Operates entirely within the Police agent peer environment without central coordination.
- **Robust Mechanics**: Strictly adheres to the game rules, board dimensions (7x7 discrete grid), and turn protocol defined in the project specification.
- **Security & Integrity**: Ensures cryptographic non-repudiation and zero-trust data isolation.

### 3. Detailed Feature Requirements
- **FR-01**: Implement Token Bucket rate limiter (TokenBucket) with capacity C and refill rate r.
- **FR-02**: Smooth burst requests to prevent triggering HTTP 429 (Too Many Requests) from external APIs.
- **FR-03**: Handle exponential backoff on HTTP 429 response (retry_backoff_sec = 5).
- **FR-04**: Implement DOS Detector flagging anomalous rapid request patterns.
- **FR-05**: Provide circuit breaker (circuit breaker pattern) severing compromised connections.

### 4. Non-Functional Requirements (NFRs)
- **Performance**: Execution latency must remain well under turn timeout thresholds (< 50ms for core computation).
- **Isolation**: Police state must remain completely isolated from Thief state (`config/police/` vs `config/thief/`).
- **Reliability**: Fault-tolerant design with fallback mechanisms for network or resource limits.

### 5. Success Metrics & Acceptance Criteria
- 100% compliance with Dec-POMDP specification rules for this feature.
- Zero unhandled exceptions during competitive match play.
- Passing unit test coverage for all functional requirements.
