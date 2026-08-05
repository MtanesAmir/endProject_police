"""MatchRunner module for orchestrating P2P Cop vs Thief match simulation."""

import os
import json
import time
from typing import Dict, Any, List

from src.domain.grid import legal_moves
from src.strategy.police_brain import MyPoliceBrain
from src.strategy.thief_brain import ThiefBrain
from src.domain.scent import ScentTracker
from src.domain.capture import CaptureDetector
from src.security.commit_reveal import CommitRevealEngine


class MatchRunner:
    """Orchestrates 35-turn Dec-POMDP Cop vs Thief competition match."""

    def __init__(self, grid_size: int = 7, max_turns: int = 35):
        self.grid_size = grid_size
        self.max_turns = max_turns
        self.police_brain = MyPoliceBrain(grid_size=grid_size)
        self.thief_brain = ThiefBrain(start_pos=(3, 3), grid_size=grid_size)
        self.scent_tracker = ScentTracker(grid_size=grid_size)
        self.capture_detector = CaptureDetector()
        self.crypto_engine = CommitRevealEngine()

    def run_match(self) -> Dict[str, Any]:
        """Run complete 35-turn simulation loop between Cop and Thief agents."""
        trajectory: List[Dict[str, Any]] = []
        cop_pos = (0, 0)
        thief_pos = (3, 3)
        outcome = "THIEF_WIN"

        for turn in range(1, self.max_turns + 1):
            state_cop = {"police_pos": cop_pos, "thief_pos": thief_pos, "turn": turn}
            state_thief = {"cop_position": cop_pos, "thief_position": thief_pos, "turn": turn}

            # Step 1: Brain decisions
            cop_next = self.police_brain._decide_move(state_cop)
            thief_next = self.thief_brain._decide_move(state_thief)

            # Step 2: Commit-Reveal
            cop_commit, cop_nonce = self.crypto_engine.commit(str(state_cop), str(cop_next), "COP_MOVE")
            thief_commit, thief_nonce = self.crypto_engine.commit(str(state_thief), str(thief_next), "THIEF_MOVE")

            cop_pos = cop_next
            thief_pos = thief_next

            # Step 3: Scent emission and decay
            self.scent_tracker.apply_emission(thief_pos)
            self.scent_tracker.apply_decay(rho=0.10)

            # Step 4: Check capture
            if self.capture_detector.check_direct_capture(cop_pos, thief_pos, radius=0):
                outcome = "COP_WIN"
                trajectory.append({"turn": turn, "cop": cop_pos, "thief": thief_pos, "event": "CAPTURE"})
                break

            trajectory.append({
                "turn": turn,
                "cop": cop_pos,
                "thief": thief_pos,
                "cop_commit": cop_commit,
                "thief_commit": thief_commit,
            })

        summary = {
            "total_turns": len(trajectory),
            "outcome": outcome,
            "trajectory": trajectory,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }

        # Save trajectory log
        os.makedirs("logs", exist_ok=True)
        with open("logs/police_match.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        return summary
