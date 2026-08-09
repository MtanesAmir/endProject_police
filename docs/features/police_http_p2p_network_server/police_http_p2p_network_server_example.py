"""Example demonstrating FastMCP HTTP server start and inter-peer JSON-RPC call."""

import time
import json
import urllib.request
from src.p2p.server import FastMCPServer


def run_http_server_example():
    """Start local peer server and query status via HTTP."""
    server = FastMCPServer(name="test_peer", host="127.0.0.1", port=9090)
    server.start(background=True)
    time.sleep(0.1)

    req_payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "get_status",
        "params": {},
        "id": 1
    }).encode("utf-8")

    req = urllib.request.Request(
        "http://127.0.0.1:9090/mcp",
        data=req_payload,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("[HTTP Server Example] Response from FastMCP peer:")
        print(json.dumps(res, indent=2))

    server.stop()


if __name__ == "__main__":
    run_http_server_example()
