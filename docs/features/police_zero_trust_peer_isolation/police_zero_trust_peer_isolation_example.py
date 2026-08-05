"""Example snippet demonstrating zero-trust role config resolution."""

import os
from typing import Dict, Any


def resolve_peer_config(role: str) -> str:
    """Resolve private config file path based on peer role."""
    role_path = f"config/{role}/game.toml"
    default_path = "config/game.toml"
    if os.path.exists(role_path):
        return role_path
    return default_path


if __name__ == "__main__":
    cop_config = resolve_peer_config("police")
    thief_config = resolve_peer_config("thief")
    print(f"[Isolation Example] Cop config path: {cop_config}")
    print(f"[Isolation Example] Thief config path: {thief_config}")
