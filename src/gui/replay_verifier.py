"""Police Replay Viewer & Cryptographic Log Verifier.

Loads match replay JSON logs, performs step-by-step cryptographic verification
of SHA-256 commitments, and detects log tampering.
"""

import hashlib
import json
import secrets
from typing import List, Dict, Any, Union, Optional


class ReplayVerifier:
    """Cryptographic Log Verifier and Replay Reader for Police match logs."""

    @staticmethod
    def compute_hash(
        nonce: str,
        move: Union[str, Dict[str, Any], List[Any]],
        intent: Union[str, Dict[str, Any], List[Any]] = "",
        state: Union[str, Dict[str, Any], List[Any]] = ""
    ) -> str:
        """Compute SHA-256 commitment hash using canonical JSON payload."""
        payload = {"intent": intent, "move": move, "state": state}
        serialized = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        seed = f"{serialized}|{nonce}"
        return hashlib.sha256(seed.encode("utf-8")).hexdigest()

    def verify_step(self, log_entry: Dict[str, Any]) -> str:
        """Verify a single match log entry step.
        
        Returns:
            "Verified OK" if recomputed hash matches original commit hash.
            "TAMPERED" if hash mismatch or entry invalid/corrupted.
        """
        if not isinstance(log_entry, dict):
            return "TAMPERED"

        # Extract required fields
        commit_hash = log_entry.get("commit_hash") or log_entry.get("hash")
        nonce = log_entry.get("nonce")
        move = log_entry.get("move", "")
        intent = log_entry.get("intent", "")
        state = log_entry.get("state", "")

        if not commit_hash or nonce is None:
            return "TAMPERED"

        recomputed = self.compute_hash(nonce=str(nonce), move=move, intent=intent, state=state)

        if secrets.compare_digest(recomputed.lower(), str(commit_hash).lower()):
            return "Verified OK"
        return "TAMPERED"

    def replay(self, log_filepath_or_entries: Union[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Replay match trajectory from JSON log file path or list of entries.
        
        Walks through steps, verifying cryptographic commitments.
        Returns summary status report.
        """
        entries: List[Dict[str, Any]] = []

        if isinstance(log_filepath_or_entries, str):
            try:
                with open(log_filepath_or_entries, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        entries = data
                    elif isinstance(data, dict) and "steps" in data:
                        entries = data["steps"]
                    elif isinstance(data, dict) and "logs" in data:
                        entries = data["logs"]
                    elif isinstance(data, dict) and "trajectory" in data:
                        entries = data["trajectory"]
                    else:
                        entries = [data]
            except Exception as e:
                return {
                    "status": "TAMPERED",
                    "error": f"Failed to read log file: {str(e)}",
                    "verified_steps": 0,
                    "total_steps": 0
                }
        elif isinstance(log_filepath_or_entries, list):
            entries = log_filepath_or_entries
        else:
            return {
                "status": "TAMPERED",
                "error": "Invalid log format",
                "verified_steps": 0,
                "total_steps": 0
            }

        verified_steps = 0
        step_results = []

        for idx, entry in enumerate(entries):
            step_status = self.verify_step(entry)
            step_results.append({
                "step": idx,
                "status": step_status,
                "entry": entry
            })
            if step_status == "Verified OK":
                verified_steps += 1
            else:
                return {
                    "status": "TAMPERED",
                    "first_tampered_step": idx,
                    "verified_steps": verified_steps,
                    "total_steps": len(entries),
                    "step_results": step_results,
                    "final_score": {"cop": 0, "thief": 0}
                }

        return {
            "status": "Verified OK",
            "verified_steps": verified_steps,
            "total_steps": len(entries),
            "step_results": step_results
        }
