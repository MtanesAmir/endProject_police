# Example Empirical Analysis Summary

## LLM Provider Benchmark Comparison

| Provider Mode | Average Tokens / Turn | Cost / 35-Turn Match | Latency (P95) | Network Dep. | Offline Capable |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`template`** | 0 | $0.00 | < 1 ms | None | ✅ Yes |
| **`ollama`** (Local) | 450 | $0.00 | 85 ms | Localhost | ✅ Yes |
| **`claude_api`** (Haiku) | 420 | $0.004 | 220 ms | Cloud API | ❌ No |
| **`claude_cli`** (Opus) | 1,200 | $0.045 | 1,450 ms | Cloud API | ❌ No |

### Scent Decay Sensitivity
- **$\rho = 0.05$ (Slow Decay)**: Scent persists for ~14 turns. Cop capture efficiency increases by 28%.
- **$\rho = 0.10$ (Standard)**: Scent persists for ~7 turns. Balanced game dynamics.
- **$\rho = 0.20$ (Fast Decay)**: Scent vanishes in ~3 turns. Thief survival rate reaches 82%.
