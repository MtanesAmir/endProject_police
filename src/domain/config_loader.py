"""ConfigLoader module for loading and validating contract and settings files."""

import json
import os
from typing import Dict, Any, Optional

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore


class ConfigLoader:
    """Loader and validator for shared contract (game.json) and private config (game.toml)."""

    def __init__(
        self,
        contract_path: str = "config/game.json",
        private_config_path: str = "config/config.toml"
    ):
        self.contract_path = contract_path
        self.private_config_path = private_config_path

    def load_contract(self) -> Dict[str, Any]:
        """Load and validate shared contract JSON file."""
        if not os.path.exists(self.contract_path):
            raise FileNotFoundError(f"Contract file not found at: {self.contract_path}")

        with open(self.contract_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.validate_contract(data)
        return data

    def validate_contract(self, data: Dict[str, Any]) -> bool:
        """Validate shared contract schema and mandatory fields."""
        required_keys = [
            "schema_version",
            "board_and_agents",
            "movement_and_barriers",
            "scoring",
            "pheromones",
        ]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Invalid contract: missing required section '{key}'")

        board = data.get("board_and_agents", {})
        if board.get("grid_size", 0) < 5:
            raise ValueError("Invalid contract: grid_size must be >= 5")

        return True

    def load_private_config(self, role: Optional[str] = None) -> Dict[str, Any]:
        """Load private per-peer TOML config file with zero-trust role path resolution."""
        target_path = self.private_config_path

        if role:
            role_specific_path = f"config/{role}/config.toml"
            if os.path.exists(role_specific_path):
                target_path = role_specific_path

        if not os.path.exists(target_path):
            # Return standard default dictionary if TOML config is not present
            return {
                "network": {"my_port": 8802, "opponent_url": "http://127.0.0.1:8801/mcp"},
                "strategy": {"police_class": "src.strategy.police_brain:MyPoliceBrain"},
            }

        with open(target_path, "rb") as f:
            return tomllib.load(f)
