"""
Police Game Phase Finite State Machine (FSM)
Governs valid game states and transitions for the Police agent.
"""

from enum import Enum
from typing import Dict, List, Union
import logging

logger = logging.getLogger(__name__)


class GamePhase(str, Enum):
    WAITING_FOR_OPPONENT = "WAITING_FOR_OPPONENT"
    COMPUTING_MOVE = "COMPUTING_MOVE"
    COMMITTING = "COMMITTING"
    AWAITING_REVEAL = "AWAITING_REVEAL"
    VERIFYING = "VERIFYING"
    TECHNICAL_LOSS = "TECHNICAL_LOSS"


WAITING_FOR_OPPONENT = GamePhase.WAITING_FOR_OPPONENT
COMPUTING_MOVE = GamePhase.COMPUTING_MOVE
COMMITTING = GamePhase.COMMITTING
AWAITING_REVEAL = GamePhase.AWAITING_REVEAL
VERIFYING = GamePhase.VERIFYING
TECHNICAL_LOSS = GamePhase.TECHNICAL_LOSS

TRANSITIONS: Dict[Union[GamePhase, str], List[Union[GamePhase, str]]] = {
    GamePhase.WAITING_FOR_OPPONENT: [GamePhase.COMPUTING_MOVE, GamePhase.VERIFYING, GamePhase.TECHNICAL_LOSS],
    GamePhase.COMPUTING_MOVE: [GamePhase.COMMITTING, GamePhase.TECHNICAL_LOSS],
    GamePhase.COMMITTING: [GamePhase.AWAITING_REVEAL, GamePhase.TECHNICAL_LOSS],
    GamePhase.AWAITING_REVEAL: [GamePhase.VERIFYING, GamePhase.TECHNICAL_LOSS],
    GamePhase.VERIFYING: [GamePhase.WAITING_FOR_OPPONENT, GamePhase.TECHNICAL_LOSS],
    GamePhase.TECHNICAL_LOSS: [GamePhase.WAITING_FOR_OPPONENT],
}


class GamePhaseMachine:
    """
    Finite State Machine governing Police game phase transitions.
    """

    TRANSITIONS = TRANSITIONS

    def __init__(self, initial_state: Union[GamePhase, str] = GamePhase.WAITING_FOR_OPPONENT):
        self._current_state = GamePhase(initial_state) if isinstance(initial_state, str) else initial_state
        self.history: List[GamePhase] = [self._current_state]

    @property
    def current_state(self) -> GamePhase:
        return self._current_state

    def transition(self, target: Union[GamePhase, str]) -> GamePhase:
        """
        Transition to target state if valid, else raise ValueError.
        """
        try:
            target_phase = GamePhase(target) if isinstance(target, str) else target
        except ValueError:
            logger.error(f"Unknown game phase: {target}")
            raise ValueError(f"Unknown target state: {target}")

        allowed = self.TRANSITIONS.get(self._current_state, [])
        if target_phase not in allowed:
            logger.error(f"Illegal state transition attempted: {self._current_state} -> {target_phase}")
            raise ValueError(f"Invalid state transition from {self._current_state} to {target_phase}")

        self._current_state = target_phase
        self.history.append(target_phase)
        logger.info(f"State transitioned from {self.history[-2]} to {target_phase}")
        return target_phase

    def force_technical_loss(self) -> GamePhase:
        """
        Fallback mechanism to immediately enter TECHNICAL_LOSS.
        """
        self._current_state = GamePhase.TECHNICAL_LOSS
        self.history.append(GamePhase.TECHNICAL_LOSS)
        logger.warning("Forced transition to TECHNICAL_LOSS")
        return GamePhase.TECHNICAL_LOSS
