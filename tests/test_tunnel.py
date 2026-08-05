"""Unit tests for TunnelManager module."""

import pytest
from src.network.tunnel import TunnelManager


def test_tunnel_manager_lifecycle():
    manager = TunnelManager(port=8000)
    url = manager.start_tunnel()
    assert "8000" in url
    assert manager.is_active is True

    status = manager.get_status()
    assert status["active"] is True
    assert status["public_url"] == url

    manager.stop_tunnel()
    assert manager.is_active is False
    assert manager.public_url is None
