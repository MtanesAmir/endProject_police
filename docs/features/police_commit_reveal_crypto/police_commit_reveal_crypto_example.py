"""Example demonstrating SHA-256 Commit-Reveal cryptographic scheme with secure nonces."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.security.commit_reveal import CommitmentScheme

def main():
    scheme = CommitmentScheme()
    payload = {"move": "N", "intent": "lie"}
    h_commit, nonce = scheme.create_commitment(move=payload)
    print(f"Commit Hash: {h_commit}")
    is_valid = scheme.verify_reveal(commitment=h_commit, move=payload, nonce=nonce)
    print(f"Verification result: {is_valid}")

if __name__ == "__main__":
    main()
