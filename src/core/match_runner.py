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
from src.domain.barriers import BarrierManager
from src.domain.config_loader import ConfigLoader
from src.domain.belief import BeliefGrid
from src.domain.trash_talk import TrashTalkProfiler


class MatchRunner:
    """Orchestrates 35-turn Dec-POMDP Cop vs Thief competition match."""

    def __init__(self, grid_size: int = 7, max_turns: int = 35):
        self.grid_size = grid_size
        self.max_turns = max_turns
        
        try:
            config = ConfigLoader().load_contract()
            max_barriers = config.get("movement_and_barriers", {}).get("max_barriers", 14)
        except Exception:
            max_barriers = 14
            
        self.barrier_manager = BarrierManager(max_barriers=max_barriers, grid_size=grid_size)
        
        self.police_brain = MyPoliceBrain(grid_size=grid_size)
        self.thief_brain = ThiefBrain(start_pos=(3, 3), grid_size=grid_size)
        self.scent_tracker = ScentTracker(grid_size=grid_size)
        self.belief_grid = BeliefGrid(grid_size=grid_size)
        self.trash_talk_profiler = TrashTalkProfiler()
        self.capture_detector = CaptureDetector()
        self.crypto_engine = CommitRevealEngine()

    def run_match(self) -> Dict[str, Any]:
        """Run complete 35-turn simulation loop between Cop and Thief agents."""
        trajectory: List[Dict[str, Any]] = []
        cop_pos = (0, 0)
        thief_pos = (3, 3)
        outcome = "THIEF_WIN"

        for turn in range(1, self.max_turns + 1):
            state_cop = {
                "police_pos": cop_pos, 
                "thief_pos": None, 
                "turn": turn, 
                "belief_grid": self.belief_grid.get_grid()
            }
            state_thief = {"cop_position": cop_pos, "thief_position": thief_pos, "turn": turn}

            # Step 1: Brain decisions
            current_barriers = {b.to_tuple() for b in self.barrier_manager.get_barriers()}
            cop_next = self.police_brain._decide_move(state_cop, barriers=current_barriers)
            thief_next = self.thief_brain._decide_move(state_thief, barriers=current_barriers)

            # Step 1b: Barrier Placement Logic (STAY)
            barrier_placed = None
            if cop_next == cop_pos:
                # Attempt to place barrier in adjacent cell prioritizing direction towards thief
                dx = thief_pos[0] - cop_pos[0]
                dy = thief_pos[1] - cop_pos[1]
                
                directions = []
                if dx != 0: directions.append((1 if dx > 0 else -1, 0))
                if dy != 0: directions.append((0, 1 if dy > 0 else -1))
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if d not in directions:
                        directions.append(d)
                
                for dx_b, dy_b in directions:
                    b_pos = (cop_pos[0] + dx_b, cop_pos[1] + dy_b)
                    if self.barrier_manager.place_barrier(b_pos, police_pos=cop_pos, occupied_positions=[cop_pos, thief_pos]):
                        barrier_placed = b_pos
                        break

            # Step 2: Commit-Reveal
            cop_commit, cop_nonce = self.crypto_engine.commit(str(state_cop), str(cop_next), "COP_MOVE")
            thief_commit, thief_nonce = self.crypto_engine.commit(str(state_thief), str(thief_next), "THIEF_MOVE")

            cop_pos = cop_next
            thief_pos = thief_next

            # Step 3: Scent decay and emission (decay first to match math formula)
            self.scent_tracker.apply_decay(rho=0.10)
            self.scent_tracker.apply_emission(thief_pos)
            self.belief_grid.update_from_scent(self.scent_tracker.get_matrix())
            
            # Step 3b: Process verbal hint
            thief_hint = self.thief_brain._decide_bluff(state_thief, thief_next)
            direction = thief_hint.split()[-1] if thief_hint else "N"
            reliability = self.trash_talk_profiler.evaluate_truthfulness(thief_hint, self.scent_tracker.get_matrix())
            self.belief_grid.update_from_hint(direction, reliability)

            # Step 4: Check capture
            if self.capture_detector.check_direct_capture(cop_pos, thief_pos, radius=0):
                outcome = "COP_WIN"
                trajectory.append({"turn": turn, "cop": cop_pos, "thief": thief_pos, "event": "CAPTURE_CLAIM"})
                break

            trajectory.append({
                "turn": turn,
                "cop": cop_pos,
                "thief": thief_pos,
                "cop_commit": cop_commit,
                "thief_commit": thief_commit,
                "barrier_placed": barrier_placed,
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
