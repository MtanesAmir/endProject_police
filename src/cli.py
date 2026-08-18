"""CLI Entry Point Runner module for police_thief P2P agent."""

import argparse
import sys
import os
import json
from typing import List, Optional

from src.p2p.server import FastMCPServer
from src.gui.replay_verifier import ReplayVerifier
from src.automation.reporting import GmailReporter


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser with subcommands 'peer', 'replay', and 'report'."""
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

    # Subcommand: report
    report_parser = subparsers.add_parser("report", help="Compile and export match JSON artifacts")
    report_parser.add_argument("--summary", default="logs/police_match.json", help="Path to match summary JSON")
    report_parser.add_argument("--outdir", default="results", help="Target output directory (default: results)")

    return parser


def main(args_list: Optional[List[str]] = None) -> int:
    """Main CLI execution handler."""
    parser = create_parser()
    args = parser.parse_args(args_list)

    if args.command == "peer":
        server_name = f"{args.role}_peer"
        
        if args.opponent_url:
            os.environ["OPPONENT_URL"] = args.opponent_url
            
        # Import mcp containing the newly defined @mcp.tools
        from src.network.mcp_server import mcp, orchestrator
        
        # We can configure the orchestrator role if needed
        # orchestrator.role = args.role
        
        print(f"[{args.role.upper()} PEER] FastMCP server '{server_name}' running on {args.host}:{args.port}")
        
        # Invoke the blocking loop from mcp_server using standard fastmcp SSE
        mcp.run(transport="sse", host=args.host, port=args.port)
        
        return 0

    elif args.command == "replay":
        verifier = ReplayVerifier()
        result = verifier.replay(args.log)
        status = result.get("status", "UNKNOWN")
        print(f"[REPLAY VERIFIER] Log: {args.log} -> Result: {status}")
        return 0 if status == "Verified OK" else 1

    elif args.command == "report":
        reporter = GmailReporter()
        summary_data = {}
        if os.path.exists(args.summary):
            try:
                with open(args.summary, "r", encoding="utf-8") as f:
                    summary_data = json.load(f)
            except Exception:
                pass

        artifacts = reporter.compile_match_reports(summary_data)
        os.makedirs(args.outdir, exist_ok=True)
        for name, content in artifacts.items():
            outpath = os.path.join(args.outdir, name)
            with open(outpath, "w", encoding="utf-8") as f:
                json.dump(content, f, indent=2)
        print(f"[REPORT ARTIFACTS] Exported {len(artifacts)} signed JSON match artifacts to '{args.outdir}/'")
        return 0

    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
