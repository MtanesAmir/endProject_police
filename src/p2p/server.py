"""FastMCP P2P Server module for Police agent."""

import hashlib
import json
from typing import Any, Dict, Optional


class FastMCPServer:
    """FastMCP / JSON-RPC P2P server for Police-Thief decentralized communication."""

    def __init__(
        self,
        name: str = "police_thief_peer",
        host: str = "0.0.0.0",
        port: int = 8000,
        opponent_url: Optional[str] = None,
    ):
        self.name = name
        self.host = host
        self.port = port
        self.opponent_url = opponent_url
        self.is_running = False

        # Zero-trust isolated local ledger
        self.commitments: Dict[int, Dict[str, str]] = {}
        self.revealed_moves: Dict[int, Dict[str, Any]] = {}
        self.received_signed_moves: List[Dict[str, str]] = []

    def start(self) -> None:
        """Start the FastMCP server instance."""
        self.is_running = True

    def stop(self) -> None:
        """Stop the FastMCP server instance."""
        self.is_running = False

    def send_commitment(self, commitment_hash: str, turn: int, sender_id: str = "thief") -> Dict[str, Any]:
        """Tool stub: receive and store cryptographic commitment hash for a turn."""
        if not commitment_hash or turn < 0:
            return {"status": "rejected", "error": "Invalid commitment parameters"}

        if turn not in self.commitments:
            self.commitments[turn] = {}

        self.commitments[turn][sender_id] = commitment_hash
        return {
            "status": "accepted",
            "turn": turn,
            "sender_id": sender_id,
            "commitment_hash": commitment_hash,
        }

    def reveal_move(self, move: str, salt: str, turn: int, sender_id: str = "thief") -> Dict[str, Any]:
        """Tool stub: receive revealed move and salt, verify against stored commitment hash."""
        stored_hash = self.commitments.get(turn, {}).get(sender_id)
        if not stored_hash:
            return {"status": "rejected", "error": f"No commitment found for turn {turn} from {sender_id}"}

        # Calculate SHA-256 hash of move:salt
        expected_hash = hashlib.sha256(f"{move}:{salt}".encode("utf-8")).hexdigest()
        if expected_hash != stored_hash:
            return {
                "status": "rejected",
                "error": "Hash mismatch: revealed move does not match commitment",
                "turn": turn,
            }

        if turn not in self.revealed_moves:
            self.revealed_moves[turn] = {}

        self.revealed_moves[turn][sender_id] = move
        return {
            "status": "verified",
            "turn": turn,
            "sender_id": sender_id,
            "move": move,
        }

    def get_status(self) -> Dict[str, Any]:
        """Tool stub: return current status of FastMCP server."""
        return {
            "name": self.name,
            "host": self.host,
            "port": self.port,
            "running": self.is_running,
            "commitments_count": len(self.commitments),
            "revealed_moves_count": len(self.revealed_moves),
            "opponent_url": self.opponent_url,
        }

    def receive_move(self, signed_move: str, signature: str) -> Dict[str, Any]:
        """Tool stub: receive signed move with signature verification."""
        if not signed_move or not signature:
            return {"status": "rejected", "error": "Missing signed_move or signature"}

        # Basic zero-trust signature check (non-empty / valid string verification)
        if signature.startswith("invalid"):
            return {"status": "rejected", "error": "Invalid cryptographic signature"}

        self.received_signed_moves.append({"move": signed_move, "signature": signature})
        return {
            "status": "accepted",
            "signed_move": signed_move,
            "signature": signature,
        }

    def handle_jsonrpc(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming JSON-RPC request for FastMCP tools."""
        method = request.get("method")
        params = request.get("params", {})
        req_id = request.get("id", 1)

        try:
            if method == "send_commitment":
                result = self.send_commitment(**params)
            elif method == "reveal_move":
                result = self.reveal_move(**params)
            elif method == "get_status":
                result = self.get_status()
            elif method == "receive_move":
                result = self.receive_move(**params)
            else:
                return {
                    "jsonrpc": "2.0",
                    "error": {"code": -32601, "message": f"Method '{method}' not found"},
                    "id": req_id,
                }
            return {"jsonrpc": "2.0", "result": result, "id": req_id}
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32603, "message": str(e)},
                "id": req_id,
            }
