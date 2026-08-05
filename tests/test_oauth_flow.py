"""Unit tests for OAuthSetupManager module."""

import pytest
from src.automation.oauth_flow import OAuthSetupManager


def test_oauth_setup_manager_status():
    manager = OAuthSetupManager()
    status = manager.get_auth_status()
    assert isinstance(status, dict)
    assert "mode" in status
    assert "scope" in status
    assert status["scope"] == "https://www.googleapis.com/auth/gmail.send"


def test_oauth_flow_execution():
    manager = OAuthSetupManager()
    res = manager.run_oauth_flow()
    assert "status" in res
    assert "message" in res
