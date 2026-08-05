"""Unit tests for ConfigLoader module."""

import os
import pytest
from src.domain.config_loader import ConfigLoader


def test_config_loader_load_contract():
    loader = ConfigLoader(contract_path="config/game.json", private_config_path="config/game.toml")
    contract = loader.load_contract()
    assert contract["schema_version"] == "1.2"
    assert contract["board_and_agents"]["grid_size"] == 7


def test_config_loader_validate_contract_invalid():
    loader = ConfigLoader()
    with pytest.raises(ValueError):
        loader.validate_contract({"schema_version": "1.2"})  # missing required sections


def test_config_loader_load_private_config():
    loader = ConfigLoader(contract_path="config/game.json", private_config_path="config/game.toml")
    private = loader.load_private_config()
    assert "network" in private
