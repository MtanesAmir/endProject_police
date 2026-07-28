"""Unit tests for police_p2p_fastmcp_server feature."""

import hashlib
import pytest
from src.p2p.server import FastMCPServer
from src.network.mcp_server import FastMCPServer as NetworkFastMCPServer


def test_fastmcp_server_initialization_and_status():
    server = FastMCPServer(name="police_thief_peer", host="0.0.0.0", port=8000, opponent_url="http://localhost:8001")
    assert not server.is_running
    server.start()
    assert server.is_running

    status = server.get_status()
    assert status["name"] == "police_thief_peer"
    assert status["port"] == 8000
    assert status["running"] is True
    assert status["opponent_url"] == "http://localhost:8001"

    server.stop()
    assert not server.is_running


def test_receive_move_acceptance_and_rejection():
    server = FastMCPServer()

    # Valid signed move
    res_valid = server.receive_move(signed_move="MOVE:UP", signature="sig_abc123")
    assert res_valid["status"] == "accepted"

    # Missing parameters
    res_missing = server.receive_move(signed_move="", signature="")
    assert res_missing["status"] == "rejected"

    # Invalid signature check
    res_invalid = server.receive_move(signed_move="MOVE:UP", signature="invalid_signature")
    assert res_invalid["status"] == "rejected"


def test_commitment_and_reveal_flow():
    server = FastMCPServer()
    move = "MOVE:(2,3)"
    salt = "random_salt_123"
    commitment_hash = hashlib.sha256(f"{move}:{salt}".encode("utf-8")).hexdigest()

    # Step 1: Send commitment
    res_commit = server.send_commitment(commitment_hash=commitment_hash, turn=1, sender_id="thief")
    assert res_commit["status"] == "accepted"

    # Step 2: Reveal move with correct move & salt
    res_reveal = server.reveal_move(move=move, salt=salt, turn=1, sender_id="thief")
    assert res_reveal["status"] == "verified"
    assert res_reveal["move"] == move

    # Step 3: Reveal with bad salt should reject
    res_bad_reveal = server.reveal_move(move=move, salt="wrong_salt", turn=2, sender_id="thief")
    assert res_bad_reveal["status"] == "rejected"


def test_jsonrpc_handling():
    server = FastMCPServer()

    request = {
        "jsonrpc": "2.0",
        "method": "send_commitment",
        "params": {"commitment_hash": "hash123", "turn": 5, "sender_id": "thief"},
        "id": 42,
    }

    response = server.handle_jsonrpc(request)
    assert response["id"] == 42
    assert response["result"]["status"] == "accepted"

    # Unknown method
    bad_request = {"jsonrpc": "2.0", "method": "unknown_method", "id": 99}
    bad_response = server.handle_jsonrpc(bad_request)
    assert "error" in bad_response
    assert bad_response["error"]["code"] == -32601


def test_network_mcp_server_reexport():
    server = NetworkFastMCPServer()
    assert server.name == "police_thief_peer"
