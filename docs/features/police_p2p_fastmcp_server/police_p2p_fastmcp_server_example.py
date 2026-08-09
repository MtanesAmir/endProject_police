"""Example demonstrating FastMCP P2P server setup and tool endpoints."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.p2p.server import FastMCPServer

def main():
    server = FastMCPServer(name="police_node", port=8000)
    print(f"Created FastMCP P2P server instance: {server.name} on port {server.port}")

if __name__ == "__main__":
    main()
