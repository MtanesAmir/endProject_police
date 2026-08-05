"""Hardware and System Profiler module for Step-0 declaration."""

import os
import platform
import subprocess
import sys
from typing import Dict, Any


class SystemProfiler:
    """System and hardware specification profiler for Step-0 computational fairness."""

    @staticmethod
    def get_git_commit_hash() -> str:
        """Retrieve current Git commit hash or fallback string."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except Exception:
            return "0000000000000000000000000000000000000000"

    @classmethod
    def get_system_specs(cls) -> Dict[str, Any]:
        """Collect local hardware and environment specifications."""
        return {
            "os_name": platform.system(),
            "os_release": platform.release(),
            "python_version": sys.version.split()[0],
            "cpu_cores": os.cpu_count() or 1,
            "architecture": platform.machine(),
            "commit_hash": cls.get_git_commit_hash(),
        }
