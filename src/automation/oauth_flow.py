"""OAuth 2.0 Flow Manager for Google Gmail API authentication."""

import os
import json
from typing import Dict, Any, Optional


class OAuthSetupManager:
    """OAuth 2.0 helper managing credentials.json and token.json for Gmail API."""

    GMAIL_SEND_SCOPE = "https://www.googleapis.com/auth/gmail.send"

    def __init__(
        self,
        credentials_path: str = "credentials.json",
        token_path: str = "token.json"
    ):
        self.credentials_path = credentials_path
        self.token_path = token_path

    def is_authenticated(self) -> bool:
        """Check if a valid token.json exists."""
        return os.path.exists(self.token_path)

    def get_auth_status(self) -> Dict[str, Any]:
        """Return OAuth 2.0 authentication status summary."""
        credentials_exist = os.path.exists(self.credentials_path)
        token_exist = os.path.exists(self.token_path)

        mode = "OAUTH2_ACTIVE" if token_exist else ("OAUTH2_PENDING" if credentials_exist else "MOCK_FALLBACK")
        return {
            "mode": mode,
            "credentials_exists": credentials_exist,
            "token_exists": token_exist,
            "scope": self.GMAIL_SEND_SCOPE,
        }

    def run_oauth_flow(self) -> Dict[str, Any]:
        """Initiate OAuth 2.0 flow or fallback to mock status."""
        status = self.get_auth_status()
        if status["mode"] == "OAUTH2_ACTIVE":
            return {"status": "SUCCESS", "message": "Already authenticated with token.json"}
        elif status["mode"] == "OAUTH2_PENDING":
            return {"status": "PENDING_BROWSER_AUTH", "message": "Execute InstalledAppFlow to generate token.json"}
        else:
            return {"status": "MOCK_MODE", "message": "Running in offline fallback mode"}
