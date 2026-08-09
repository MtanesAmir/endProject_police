"""Example snippet for export-artifacts CLI command simulation."""
import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

def export_artifacts_example(outdir: str = "results"):
    os.makedirs(outdir, exist_ok=True)
    summary = {
        "status": "SUCCESS",
        "files": ["declaration_police.json", "config_police.json", "log_police.json", "result_police.json"]
    }
    with open(os.path.join(outdir, "export_manifest.json"), "w") as f:
        json.dump(summary, f, indent=2)
    return summary

if __name__ == "__main__":
    res = export_artifacts_example()
    print(f"[CLI Export Example] Manifest exported: {res}")
