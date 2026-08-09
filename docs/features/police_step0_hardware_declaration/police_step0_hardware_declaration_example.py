"""Example snippet for Step-0 Hardware and Match Declaration creation."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.hardware import SystemProfiler

class Step0DeclarationExample:
    @staticmethod
    def create_declaration():
        return SystemProfiler.get_system_specs()

if __name__ == "__main__":
    decl = Step0DeclarationExample.create_declaration()
    print(f"[Step-0 Example] System Hardware info: OS={decl.get('os_name')}, CPU={decl.get('cpu_brand')}, RAM={decl.get('ram_gb', 0):.1f}GB")
