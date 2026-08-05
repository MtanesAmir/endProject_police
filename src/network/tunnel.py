"""Public Tunneling Manager module for ngrok / Localtonet HTTPS tunnel bindings."""

import os
from typing import Dict, Any, Optional


class TunnelManager:
    """Manages public HTTPS tunneling for local P2P FastMCP servers."""

    def __init__(self, port: int = 8000, host: str = "127.0.0.1"):
        self.port = port
        self.host = host
        self.public_url: Optional[str] = None
        self.is_active = False

    def start_tunnel(self) -> str:
        """Start public HTTPS tunnel or return mock localhost URL."""
        self.is_active = True
        self.public_url = f"http://{self.host}:{self.port}"
        return self.public_url

    def stop_tunnel(self) -> None:
        """Stop public tunnel binding."""
        self.is_active = False
        self.public_url = None

    def get_status(self) -> Dict[str, Any]:
        """Return status summary of tunnel manager."""
        return {
            "active": self.is_active,
            "port": self.port,
            "public_url": self.public_url,
        }
