"""Example CLI runner snippet for police_cli_entrypoint_runner feature."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Police-Thief P2P Peer CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Subcommand: peer
    peer_parser = subparsers.add_parser("peer", help="Run peer server agent")
    peer_parser.add_argument("--role", choices=["police", "thief"], default="police", help="Agent role")
    peer_parser.add_argument("--host", default="0.0.0.0", help="Host binding IP")
    peer_parser.add_argument("--port", type=int, default=8000, help="Port number")
    peer_parser.add_argument("--opponent-url", help="Opponent P2P URL endpoint")

    # Subcommand: replay
    replay_parser = subparsers.add_parser("replay", help="Replay and audit match log")
    replay_parser.add_argument("--log", required=True, help="Path to match JSON log file")

    args = parser.parse_args()

    if args.command == "peer":
        print(f"[CLI Example] Starting {args.role} peer server on {args.host}:{args.port}...")
    elif args.command == "replay":
        print(f"[CLI Example] Verifying match log integrity: {args.log}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
