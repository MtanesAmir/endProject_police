"""Example demonstrating automated match reporting payload creation and dispatching."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.automation.reporting import GmailReporter

def main():
    reporter = GmailReporter()
    print(f"GmailReporter configured for evaluator: {reporter.evaluator_email}")

if __name__ == "__main__":
    main()
