"""Unit tests for SystemProfiler hardware discovery module."""

import pytest
from src.domain.hardware import SystemProfiler


def test_get_system_specs():
    specs = SystemProfiler.get_system_specs()
    assert isinstance(specs, dict)
    assert "os_name" in specs
    assert "python_version" in specs
    assert "cpu_cores" in specs
    assert "commit_hash" in specs


def test_get_git_commit_hash():
    commit_hash = SystemProfiler.get_git_commit_hash()
    assert isinstance(commit_hash, str)
    assert len(commit_hash) >= 7
