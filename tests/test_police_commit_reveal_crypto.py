"""Unit tests for Police Cryptographic Commit-Reveal Protocol Engine (police_commit_reveal_crypto)."""

import json
import secrets
import pytest
from src.domain.crypto import CommitmentScheme, CommitRevealEngine
from src.security.commit_reveal import CommitRevealEngine as SecurityEngine


def test_nonce_generation_length_and_randomness():
    scheme = CommitmentScheme()
    nonce1 = scheme.generate_nonce(16)
    nonce2 = scheme.generate_nonce(16)

    # 16 bytes hex string has length 32 characters
    assert len(nonce1) == 32
    assert len(nonce2) == 32
    assert nonce1 != nonce2


def test_canonical_serialization_byte_identical():
    scheme = CommitmentScheme()
    payload_a = {"move": (2, 3), "nonce": "abc12345", "state": {"turn": 1}}
    payload_b = {"state": {"turn": 1}, "nonce": "abc12345", "move": (2, 3)}

    ser_a = scheme.canonical_serialize(payload_a)
    ser_b = scheme.canonical_serialize(payload_b)

    assert ser_a == ser_b


def test_create_commitment_and_verify_reveal_valid():
    scheme = CommitmentScheme()
    move = (3, 4)
    commitment_hash, nonce = scheme.create_commitment(move)

    assert isinstance(commitment_hash, str)
    assert len(commitment_hash) == 64  # SHA-256 hex string length

    # Verify reveal succeeds with matching move and nonce
    is_valid = scheme.verify_reveal(commitment_hash, move, nonce)
    assert is_valid is True


def test_verify_reveal_detects_move_tampering():
    scheme = CommitmentScheme()
    move = (3, 4)
    commitment_hash, nonce = scheme.create_commitment(move)

    # Attempt to reveal modified move (tampered)
    tampered_move = (3, 5)
    is_valid = scheme.verify_reveal(commitment_hash, tampered_move, nonce)
    assert is_valid is False


def test_verify_reveal_detects_nonce_tampering():
    scheme = CommitmentScheme()
    move = (1, 2)
    commitment_hash, nonce = scheme.create_commitment(move)

    # Attempt to reveal with wrong nonce
    wrong_nonce = secrets.token_hex(16)
    is_valid = scheme.verify_reveal(commitment_hash, move, wrong_nonce)
    assert is_valid is False


def test_commit_reveal_engine_full_workflow():
    engine = CommitRevealEngine()
    state = {"turn": 5, "police_pos": (2, 2)}
    move = (2, 3)
    intent = "PURSUIT"

    commitment, nonce = engine.commit(state, move, intent)

    # Verify with correct parameters
    assert engine.verify(commitment, state, move, intent, nonce) is True

    # Verify tampering intent fails
    assert engine.verify(commitment, state, move, "PATROL", nonce) is False

    # Verify tampering state fails
    assert engine.verify(commitment, {"turn": 6, "police_pos": (2, 2)}, move, intent, nonce) is False


def test_security_engine_alias():
    engine = SecurityEngine()
    hash_val, nonce = engine.commit({"a": 1}, (0, 0), "TEST")
    assert engine.verify(hash_val, {"a": 1}, (0, 0), "TEST", nonce) is True
