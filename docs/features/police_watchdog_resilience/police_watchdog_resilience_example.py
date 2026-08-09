"""Example demonstrating Watchdog timer, heartbeat monitoring, and safe state persistence."""
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.reliability.watchdog import Watchdog

def main():
    watchdog = Watchdog(timeout_sec=60.0)
    print(f"Watchdog initialized with timeout: {watchdog.timeout_sec}s")
    watchdog.update_heartbeat()
    print(f"Watchdog status: {watchdog.check()}")

if __name__ == "__main__":
    main()
