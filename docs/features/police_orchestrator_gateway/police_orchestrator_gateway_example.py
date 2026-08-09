"""Example demonstrating Orchestrator single gateway dispatching across subsystems."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.core.orchestrator import PoliceOrchestrator

def main():
    orchestrator = PoliceOrchestrator()
    print(f"PoliceOrchestrator initialized. Current state: {orchestrator.fsm.current_state}")

if __name__ == "__main__":
    main()
