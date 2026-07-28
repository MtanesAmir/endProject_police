"""Police Cryptographic Commit-Reveal Protocol Engine (`police_commit_reveal_crypto`)."""

import hashlib
import json
import secrets
from typing import Any, Dict, Optional, Tuple


class CommitmentScheme:
    """SHA-256 Commit-Reveal protocol scheme for secure move submission."""

    @staticmethod
    def generate_nonce(num_bytes: int = 16) -> str:
        """Generates a cryptographically secure hex nonce string using secrets.token_hex(16)."""
        return secrets.token_hex(num_bytes)

    @staticmethod
    def canonical_serialize(payload: Any) -> str:
        """Serializes payload into canonical JSON string (sorted keys, compact separators)."""
        return json.dumps(payload, sort_keys=True, separators=(",", ":"))

    def create_commitment(
        self, move: Any, nonce: Optional[str] = None
    ) -> Tuple[str, str]:
        """Creates SHA-256 commitment hash from move and nonce.

        Returns tuple of (commitment_hash, nonce). If nonce is not provided, one is generated.
        """
        if nonce is None:
            nonce = self.generate_nonce(16)

        payload = {"move": move, "nonce": nonce}
        serialized = self.canonical_serialize(payload)
        commitment_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        return commitment_hash, nonce

    def verify_reveal(self, commitment: str, move: Any, nonce: str) -> bool:
        """Verifies if revealed (move, nonce) matches original commitment hash using timing-safe comparison."""
        recalculated_hash, _ = self.create_commitment(move, nonce)
        return secrets.compare_digest(commitment, recalculated_hash)


class CommitRevealEngine:
    """Cryptographic engine managing state, move, and intent commitments across 4-stage protocol."""

    def __init__(self):
        self.scheme = CommitmentScheme()

    def commit(
        self, state: Any, move: Any, intent: Any = None, nonce: Optional[str] = None
    ) -> Tuple[str, str]:
        """Generates SHA-256 commitment for state, move, and intent tuple."""
        if nonce is None:
            nonce = self.scheme.generate_nonce(16)

        payload = {"intent": intent, "move": move, "nonce": nonce, "state": state}
        serialized = self.scheme.canonical_serialize(payload)
        commitment_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        return commitment_hash, nonce

    def verify(
        self, commitment: str, state: Any, move: Any, intent: Any, nonce: str
    ) -> bool:
        """Verifies revealed state, move, intent, and nonce against original commitment."""
        payload = {"intent": intent, "move": move, "nonce": nonce, "state": state}
        serialized = self.scheme.canonical_serialize(payload)
        recalculated_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        return secrets.compare_digest(commitment, recalculated_hash)
