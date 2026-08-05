"""Example snippet for Gmail OAuth 2.0 flow manager."""

import os
from typing import Dict, Any


class OAuthSetupManagerExample:
    """OAuth 2.0 helper managing credentials.json and token.json."""

    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    def __init__(self, credentials_path: str = "credentials.json", token_path: str = "token.json"):
        self.credentials_path = credentials_path
        self.token_path = token_path

    def is_authenticated(self) -> bool:
        """Check if token.json exists."""
        return os.path.exists(self.token_path)

    def get_status(self) -> Dict[str, Any]:
        """Return OAuth status summary."""
        return {
            "credentials_exists": os.path.exists(self.credentials_path),
            "token_exists": self.token_path and os.path.exists(self.token_path),
            "scope": self.SCOPES[0],
            "mode": "OAUTH2" if self.is_authenticated() else "MOCK_FALLBACK"
        }


if __name__ == "__main__":
    manager = OAuthSetupManagerExample()
    status = manager.get_status()
    print(f"[OAuth Example] Status: {status['mode']}")
    print(f"  Credentials file: {status['credentials_exists']}")
    print(f"  Token file: {status['token_exists']}")
