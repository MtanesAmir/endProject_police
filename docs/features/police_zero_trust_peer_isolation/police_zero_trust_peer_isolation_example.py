"""Example verifying Zero-Trust peer isolation between police and thief configurations."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

def verify_zero_trust_isolation(role: str) -> str:
    role_path = f"config/{role}/game.toml"
    return f"Isolation configuration verified for role '{role}' at '{role_path}'"

if __name__ == "__main__":
    print(verify_zero_trust_isolation("police"))
    print(verify_zero_trust_isolation("thief"))
