"""Unit tests for Police Match Report Builder & Automated Gmail Reporter (`police_gmail_reporting_automation`)."""

import os
import pytest
from src.automation.reporting import GmailReporter
from src.reporting.report_compiler import ReportCompiler


def test_compile_match_reports_schema():
    """Verify compile_match_reports generates the 4 mandatory JSON match report artifacts."""
    reporter = GmailReporter()
    summary = {
        "commit_hash": "a1b2c3d4e5f678901234567890abcdef12345678",
        "github_repo_url": "https://github.com/MtanesAmir/endProject_police",
        "outcome": "POLICE_WIN",
        "total_steps": 12,
        "final_score": 100,
        "token_stats": {"prompt_tokens": 1200, "completion_tokens": 350}
    }

    artifacts = reporter.compile_match_reports(summary)

    # 4 mandatory JSON report files
    assert "declaration_police.json" in artifacts
    assert "config_police.json" in artifacts
    assert "log_police.json" in artifacts
    assert "result_police.json" in artifacts

    # Declaration schema
    dec = artifacts["declaration_police.json"]
    assert dec["agent_role"] == "Police"
    assert dec["commit_hash"] == summary["commit_hash"]
    assert dec["github_repo_url"] == summary["github_repo_url"]
    assert "signature" in dec

    # Config schema
    cfg = artifacts["config_police.json"]
    assert cfg["grid_size"] == 7
    assert cfg["agent_role"] == "Police"

    # Log schema
    log = artifacts["log_police.json"]
    assert log["total_steps"] == 12
    assert log["verified_ok"] is True

    # Result schema
    res = artifacts["result_police.json"]
    assert res["outcome"] == "POLICE_WIN"
    assert res["final_score"] == 100
    assert res["token_consumption_stats"]["prompt_tokens"] == 1200


def test_send_gmail_report():
    """Verify send_gmail_report formatting and transmission execution."""
    reporter = GmailReporter(evaluator_email="test_evaluator@example.com")
    body = {
        "artifacts": {
            "declaration_police.json": {},
            "config_police.json": {},
            "log_police.json": {},
            "result_police.json": {}
        }
    }

    response = reporter.send_gmail_report(
        recipient="test_evaluator@example.com",
        subject="Match Summary Test",
        body_json=body
    )

    assert response["status"] == "SENT"
    assert response["recipient"] == "test_evaluator@example.com"
    assert response["subject"] == "Match Summary Test"
    assert response["artifacts_count"] == 4
    assert "message_id" in response


def test_send_match_report_end_to_end():
    """Verify send_match_report compiles and sends end-to-end report."""
    reporter = GmailReporter(evaluator_email="evaluator@domain.com")
    summary = {
        "outcome": "POLICE_WIN",
        "final_score": 95,
        "total_steps": 8
    }

    result = reporter.send_match_report(summary)

    assert result["status"] == "SENT"
    assert "Police Match Report" in result["subject"]
    assert result["recipient"] == "evaluator@domain.com"


def test_gitignore_contains_credentials():
    """Verify gitignore lists credentials.json and token.json for OAuth security."""
    gitignore_path = ".gitignore"
    assert os.path.exists(gitignore_path)

    with open(gitignore_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "credentials.json" in content
    assert "token.json" in content


def test_report_compiler_wrapper():
    """Verify ReportCompiler wrapper forwards artifact compilation correctly."""
    compiler = ReportCompiler()
    artifacts = compiler.compile_match_reports({"outcome": "DRAW"})
    assert len(artifacts) == 4
