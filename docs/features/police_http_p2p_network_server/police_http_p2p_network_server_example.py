"""Example demonstrating FastMCPServer network binding and JSON-RPC dispatching."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.p2p.server import FastMCPServer

def main():
    server = FastMCPServer(name="test_peer", host="127.0.0.1", port=9090)
    print(f"[FastMCP Server] Initialized {server.name} at {server.host}:{server.port}")

if __name__ == "__main__":
    main()
