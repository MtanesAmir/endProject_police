"""Example snippet for TunnelManager public HTTPS tunneling."""

import os
from typing import Optional


class TunnelManagerExample:
    """Manager for binding ngrok / HTTP tunnels to local FastMCP servers."""

    def __init__(self, port: int = 8000):
        self.port = port
        self.public_url: Optional[str] = None

    def start_tunnel((self)) -> str:
        """Start public tunnel or return mock localhost URL."""
        # Simulated tunnel startup
        self.public_url = f"https://mock-tunnel.ngrok-free.app:{self.port}"
        return self.public_url

    def stop_tunnel(self) -> None:
        """Stop active tunnel."""
        self.public_url = None


if __name__ == "__main__":
    manager = TunnelManagerExample(port=8000)
    url = manager.start_tunnel()
    print(f"[Tunnel Example] Exposing port {manager.port} via public URL: {url}")
