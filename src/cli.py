"""CLI Entry Point Runner module for police_thief P2P agent."""

import argparse
import sys
import os
from typing import List, Optional

from src.p2p.server import FastMCPServer
from src.gui.replay_verifier import ReplayVerifier


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser with subcommands 'peer' and 'replay'."""
    parser = argparse.ArgumentParser(
        prog="police_thief",
        description="Distributed Cops-and-Robbers over a Peer-to-Peer Network (Dec-POMDP) CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: peer
    peer_parser = subparsers.add_parser("peer", help="Run local P2P FastMCP peer server")
    peer_parser.add_argument(
        "--role",
        choices=["police", "thief"],
        default="police",
        help="Agent role (default: police)"
    )
    peer_parser.add_argument("--host", default="0.0.0.0", help="Host IP binding (default: 0.0.0.0)")
    peer_parser.add_argument("--port", type=int, default=8000, help="Port number (default: 8000)")
    peer_parser.add_argument("--opponent-url", help="Opponent peer FastMCP URL endpoint")
    peer_parser.add_argument("--config", default="config/game.json", help="Path to shared contract JSON file")

    # Subcommand: replay
    replay_parser = subparsers.add_parser("replay", help="Replay and verify match log integrity")
    replay_parser.add_argument("--log", required=True, help="Path to match JSON log file")

    return parser


def main(args_list: Optional[List[str]] = None) -> int:
    """Main CLI execution handler."""
    parser = create_parser()
    args = parser.parse_args(args_list)

    if args.command == "peer":
        server_name = f"{args.role}_peer"
        server = FastMCPServer(
            name=server_name,
            host=args.host,
            port=args.port,
            opponent_url=args.opponent_url
        )
        server.start()
        print(f"[{args.role.upper()} PEER] FastMCP server '{server_name}' running on {args.host}:{args.port}")
        return 0

    elif args.command == "replay":
        verifier = ReplayVerifier()
        result = verifier.replay(args.log)
        status = result.get("status", "UNKNOWN")
        print(f"[REPLAY VERIFIER] Log: {args.log} -> Result: {status}")
        return 0 if status == "Verified OK" else 1

    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
