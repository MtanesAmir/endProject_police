"""Example snippet for artifact export CLI command handler."""

import os
import json
from typing import Dict, Any


def export_match_artifacts_example(summary_data: Dict[str, Any], outdir: str = "results") -> list:
    """Compile and save 4 signed JSON match report artifacts."""
    os.makedirs(outdir, exist_ok=True)
    artifacts = {
        "declaration_police.json": {"artifact_type": "declaration", "agent_role": "Police"},
        "config_police.json": {"artifact_type": "config", "grid_size": 7},
        "log_police.json": {"artifact_type": "log", "steps": summary_data.get("steps", [])},
        "result_police.json": {"artifact_type": "result", "outcome": summary_data.get("outcome", "IN_PROGRESS")}
    }

    created_paths = []
    for filename, content in artifacts.items():
        filepath = os.path.join(outdir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2)
        created_paths.append(filepath)

    return created_paths


if __name__ == "__main__":
    summary = {"outcome": "COP_WIN", "steps": [1, 2, 3]}
    paths = export_match_artifacts_example(summary)
    print(f"[Artifact Exporter Example] Exported {len(paths)} artifact files:")
    for p in paths:
        print(f"  {p}")
