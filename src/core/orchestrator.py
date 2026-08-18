"""
Police Single Gateway Orchestrator (PoliceOrchestrator)
Central gateway routing network messages, phase transitions, watchdog liveness, and turn execution.
"""

import time
import logging
from typing import Any, Dict, Optional, Tuple

from src.core.state_machine import (
    GamePhaseMachine,
    GamePhase,
    WAITING_FOR_OPPONENT,
    COMPUTING_MOVE,
    COMMITTING,
    AWAITING_REVEAL,
    VERIFYING,
    TECHNICAL_LOSS,
)
from src.reliability.watchdog import (
    Watchdog,
    WatchdogStatus,
    watchdog_check,
    persist_state,
    controlled_shutdown,
    ALIVE,
    SHUTDOWN,
)
from src.reliability.deadline_tracker import DeadlineTracker

logger = logging.getLogger(__name__)


class PoliceOrchestrator:
    """
    Central Orchestrator for Police agent.
    Single Gateway wiring domain modules, state machine, reliability (watchdog/deadlines), and strategy.
    """

    def __init__(
        self,
        fsm: Optional[GamePhaseMachine] = None,
        watchdog: Optional[Watchdog] = None,
        deadline_tracker: Optional[DeadlineTracker] = None,
        strategy_engine: Optional[Any] = None,
        p2p_server: Optional[Any] = None,
        police_pos: Tuple[int, int] = (0, 0),
    ):
        self.fsm = fsm if fsm is not None else GamePhaseMachine()
        self.watchdog = watchdog if watchdog is not None else Watchdog()
        self.deadline_tracker = deadline_tracker if deadline_tracker is not None else DeadlineTracker()
        self.strategy_engine = strategy_engine
        self.p2p_server = p2p_server
        self.police_pos = police_pos
        self.current_turn = 0
        self.last_action_data: Optional[Dict[str, Any]] = None
        logger.info("PoliceOrchestrator initialized")

    def handle_incoming_message(self, msg_type: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Routes incoming network messages through the single gateway.
        """
        payload = payload or {}
        self.watchdog.update_heartbeat()
        logger.info(f"Orchestrator received message: {msg_type}")

        if msg_type in ("PING", "receive_control"):
            return {"status": "PONG", "timestamp": time.time()}

        if msg_type in ("TURN_INIT", "negotiate"):
            # Do NOT increment current_turn here. It should start at 1 when we process our first turn.
            return {"status": "ACK", "turn": self.current_turn, "state": self.fsm.current_state}

        if msg_type in ("PROCESS_TURN", "receive_turn"):
            return self.process_turn(payload)

        if msg_type == "submit_audit":
            self.fsm.transition(GamePhase.VERIFYING)
            return {"status": "OK", "msg_type": msg_type, "state": self.fsm.current_state}

        return {"status": "OK", "msg_type": msg_type, "state": self.fsm.current_state}

    def process_turn(self, opponent_move_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Executes complete turn lifecycle: WAITING -> COMPUTING -> COMMITTING -> AWAITING_REVEAL -> VERIFYING -> WAITING.
        """
        start_time = self.deadline_tracker.start_timer()

        # Check Watchdog health
        if self.watchdog.check() == SHUTDOWN:
            logger.error("Watchdog status is SHUTDOWN. Aborting turn processing.")
            self.fsm.force_technical_loss()
            self.emergency_shutdown(reason="Watchdog shutdown")
            return {
                "success": False,
                "error": "Watchdog shutdown",
                "state": self.fsm.current_state,
            }

        try:
            # 1. Transition to COMPUTING_MOVE
            self.fsm.transition(GamePhase.COMPUTING_MOVE)

            # Compute move
            if self.strategy_engine and hasattr(self.strategy_engine, "compute_next_move"):
                next_pos = self.strategy_engine.compute_next_move(self.police_pos, opponent_move_data)
            else:
                x, y = self.police_pos
                next_pos = (min(6, x + 1), y)

            self.police_pos = next_pos

            # Check deadline after computation
            if self.deadline_tracker.check_deadline(start_time, timeout=self.deadline_tracker.default_timeout):
                logger.error("Deadline exceeded during move computation!")
                self.fsm.transition(GamePhase.TECHNICAL_LOSS)
                return {
                    "success": False,
                    "error": "Turn computation deadline exceeded",
                    "state": self.fsm.current_state,
                }

            # 2. Transition to COMMITTING
            self.fsm.transition(GamePhase.COMMITTING)
            commit_hash = f"commit_{self.police_pos}_{time.time()}"

            # 3. Transition to AWAITING_REVEAL
            self.fsm.transition(GamePhase.AWAITING_REVEAL)

            # 4. Transition to VERIFYING
            self.fsm.transition(GamePhase.VERIFYING)
            verification_status = True

            # 5. Return to WAITING_FOR_OPPONENT
            self.fsm.transition(GamePhase.WAITING_FOR_OPPONENT)
            self.current_turn += 1

            self.last_action_data = {
                "step": self.current_turn,
                "sender": "police",
                "commit": commit_hash,
                "hint": "Police move.",
                "timestamp": str(time.time()),
                "smell_grid": {},
                "barrier_placed": None,
                "capture_claim": list(self.police_pos),
                "claim_response": None,
                "win_claim": None,
            }

            if self.p2p_server:
                self.p2p_server.call_opponent("receive_turn", self.last_action_data)

            return {
                "success": True,
                "state": self.fsm.current_state,
                "data": self.last_action_data,
            }

        except Exception as e:
            logger.error(f"Error encountered during turn processing: {e}")
            self.fsm.force_technical_loss()
            self.emergency_shutdown(reason=str(e))
            return {
                "success": False,
                "error": str(e),
                "state": self.fsm.current_state,
            }

    def emergency_shutdown(self, reason: str = "Unhandled exception") -> None:
        """
        Triggers emergency state dump and controlled shutdown.
        """
        state_dump = {
            "current_turn": self.current_turn,
            "police_pos": self.police_pos,
            "fsm_state": str(self.fsm.current_state),
            "fsm_history": [str(s) for s in self.fsm.history],
            "reason": reason,
            "timestamp": time.time(),
        }
        self.watchdog.persist_current_state(state_dump)
        controlled_shutdown(reason)
