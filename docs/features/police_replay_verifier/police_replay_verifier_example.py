"""Example demonstrating Replay Verifier post-mortem log audit with SHA-256 validation."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.gui.replay_verifier import ReplayVerifier

def main():
    verifier = ReplayVerifier()
    print("ReplayVerifier ready for match replay and SHA-256 audit log verification.")

if __name__ == "__main__":
    main()
