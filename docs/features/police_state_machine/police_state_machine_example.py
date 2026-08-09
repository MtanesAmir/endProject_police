"""Example demonstrating game phase state machine and strict transition validation."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.core.state_machine import GamePhaseMachine, GamePhase

def main():
    sm = GamePhaseMachine()
    print(f"Initial State: {sm.current_state}")
    sm.transition(GamePhase.COMPUTING_MOVE)
    print(f"State after transition: {sm.current_state}")
    sm.transition(GamePhase.COMMITTING)
    print(f"State after transition: {sm.current_state}")

if __name__ == "__main__":
    main()
