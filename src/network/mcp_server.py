"""Network MCP server wrapper module."""

from fastmcp import FastMCP
from src.p2p.server import FastMCPServer

mcp = FastMCP("police_thief_peer")

__all__ = ["FastMCPServer", "mcp"]

if __name__ == "__main__":
    # Ensure transport and port are specified so FastMCP runs continuously
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
