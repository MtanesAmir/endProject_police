# Example Document Structure
## Academic Report & Mechanism PRD Specification Example

### Dec-POMDP Formalization Summary
The system is modeled as an 8-tuple:
$$\langle n, S, \{A_i\}, P, R, \{\Omega_i\}, O, \gamma \rangle$$

Where:
- $n = 2$ agents (Police and Thief)
- $S$: Full state space (Positions of agents, static barriers, scent grid)
- $A_i$: Action space (`N`, `S`, `E`, `W`, `STAY`)
- $P(s' | s, a_1, a_2)$: Transition function
- $R$: Reward function (Score table defined in `config/game.json`)
- $\Omega_i$: Local observations (Local scent values, verbal hint messages)
- $O$: Observation probability function
- $\gamma = 0.95$: Discount factor

### Protocol Flow Example
1. **Turn Start**: Police and Thief compute move & bluff.
2. **Commit Phase**: Exchange SHA-256 hash $H_{commit} = \text{SHA256}(\text{CanonicalJSON}(S, Move, Intent, Nonce))$.
3. **Ack Phase**: Peers lock move decisions upon hash receipt.
4. **Reveal Phase**: Peers exchange actual move & verbal hint ($Nonce$ hidden).
5. **Final Audit**: End of game reveal of all nonces verifying zero tampering (`Verified OK`).
