"""Unit tests for Police Replay Viewer & Cryptographic Log Verifier (`police_replay_verifier`)."""

import json
import pytest
from src.gui.replay_verifier import ReplayVerifier


def test_compute_hash_consistency():
    """Verify SHA-256 computation returns deterministic hash."""
    verifier = ReplayVerifier()
    hash1 = verifier.compute_hash(nonce="secret123", move="MOVE_UP", intent="CATCH_THIEF", state="STATE_NORMAL")
    hash2 = verifier.compute_hash(nonce="secret123", move="MOVE_UP", intent="CATCH_THIEF", state="STATE_NORMAL")
    assert hash1 == hash2
    assert len(hash1) == 64  # SHA-256 hex string length


def test_verify_step_valid_ok():
    """Verify verify_step returns 'Verified OK' for authentic commitment hash."""
    verifier = ReplayVerifier()
    nonce = "random_nonce_99"
    move = "MOVE_DOWN"
    intent = "PATROL"
    state = {"police_pos": [1, 2]}
    
    expected_hash = verifier.compute_hash(nonce=nonce, move=move, intent=intent, state=state)
    
    log_entry = {
        "nonce": nonce,
        "move": move,
        "intent": intent,
        "state": state,
        "commit_hash": expected_hash
    }
    
    result = verifier.verify_step(log_entry)
    assert result == "Verified OK"


def test_verify_step_tampered_hash_mismatch():
    """Verify verify_step returns 'TAMPERED' when commitment hash does not match."""
    verifier = ReplayVerifier()
    
    log_entry = {
        "nonce": "nonce_1",
        "move": "MOVE_LEFT",
        "intent": "PATROL",
        "state": "NORMAL",
        "commit_hash": "0000000000000000000000000000000000000000000000000000000000000000"
    }
    
    result = verifier.verify_step(log_entry)
    assert result == "TAMPERED"


def test_verify_step_missing_fields():
    """Verify verify_step returns 'TAMPERED' for malformed or missing fields."""
    verifier = ReplayVerifier()
    assert verifier.verify_step({}) == "TAMPERED"
    assert verifier.verify_step({"nonce": "123"}) == "TAMPERED"
    assert verifier.verify_step("not a dict") == "TAMPERED"


def test_replay_trajectory_valid_log(tmp_path):
    """Verify replay loop succeeds for valid match replay JSON file."""
    verifier = ReplayVerifier()
    
    steps = []
    for i in range(5):
        nonce = f"nonce_{i}"
        move = f"MOVE_{i}"
        intent = f"INTENT_{i}"
        h = verifier.compute_hash(nonce=nonce, move=move, intent=intent)
        steps.append({
            "nonce": nonce,
            "move": move,
            "intent": intent,
            "commit_hash": h
        })
        
    log_file = tmp_path / "police_match.json"
    log_file.write_text(json.dumps({"steps": steps}))
    
    res = verifier.replay(str(log_file))
    assert res["status"] == "Verified OK"
    assert res["verified_steps"] == 5
    assert res["total_steps"] == 5


def test_replay_trajectory_tampered_log(tmp_path):
    """Verify replay loop halts and reports 'TAMPERED' on modified log entry."""
    verifier = ReplayVerifier()
    
    steps = []
    for i in range(4):
        nonce = f"nonce_{i}"
        move = f"MOVE_{i}"
        intent = f"INTENT_{i}"
        h = verifier.compute_hash(nonce=nonce, move=move, intent=intent)
        steps.append({
            "nonce": nonce,
            "move": move,
            "intent": intent,
            "commit_hash": h
        })
        
    # Tamper step 2
    steps[2]["move"] = "TAMPERED_MOVE"
    
    log_file = tmp_path / "police_match_tampered.json"
    log_file.write_text(json.dumps({"steps": steps}))
    
    res = verifier.replay(str(log_file))
    assert res["status"] == "TAMPERED"
    assert res["first_tampered_step"] == 2
    assert res["verified_steps"] == 2
    assert res["total_steps"] == 4
