"""Example snippet for TunnelManager public HTTPS tunneling."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

class TunnelManagerExample:
    def __init__(self, port: int = 8000):
        self.port = port
        self.public_url = None

    def start_tunnel(self) -> str:
        self.public_url = f"https://mock-tunnel.ngrok-free.app:{self.port}"
        return self.public_url

if __name__ == "__main__":
    manager = TunnelManagerExample(port=8000)
    url = manager.start_tunnel()
    print(f"[Tunnel Example] Exposing port {manager.port} via public URL: {url}")
