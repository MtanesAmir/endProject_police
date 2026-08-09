"""Example snippet for Gmail API OAuth 2.0 flow initialization."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_oauth_scopes():
    return SCOPES

if __name__ == "__main__":
    scopes = get_oauth_scopes()
    print(f"[OAuth Setup] Scopes configured: {scopes}")
