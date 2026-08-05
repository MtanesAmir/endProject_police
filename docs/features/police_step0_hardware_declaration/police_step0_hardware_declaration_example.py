"""Example implementation snippet for Step-0 hardware auto-discovery."""

import platform
import os
import sys
import subprocess
from typing import Dict, Any


class SystemProfilerExample:
    """Hardware and environment profiler for Step-0 declaration."""

    @staticmethod
    def get_git_commit_hash() -> str:
        """Retrieve current Git commit hash or fallback string."""
        try:
            result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except Exception:
            return "0000000000000000000000000000000000000000"

    @classmethod
    def get_system_specs(cls) -> Dict[str, Any]:
        """Collect local hardware and execution environment specifications."""
        return {
            "os_name": platform.system(),
            "os_release": platform.release(),
            "python_version": sys.version.split()[0],
            "cpu_cores": os.cpu_count() or 1,
            "commit_hash": cls.get_git_commit_hash(),
        }


if __name__ == "__main__":
    specs = SystemProfilerExample.get_system_specs()
    print("[Hardware Example] Auto-discovered Step-0 System Specs:")
    for k, v in specs.items():
        print(f"  {k}: {v}")
