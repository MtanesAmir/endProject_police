"""Unit tests for ThiefBrain and MatchRunner modules."""

import os
import pytest
from src.strategy.thief_brain import ThiefBrain
from src.core.match_runner import MatchRunner


def test_thief_brain_pick_move():
    brain = ThiefBrain(start_pos=(3, 3), grid_size=7)
    valid_moves = [(2, 3), (4, 3), (3, 4), (3, 2)]
    move = brain._pick_move({"cop_position": (0, 0)}, valid_moves)
    assert move in valid_moves


def test_thief_brain_decide_bluff():
    brain = ThiefBrain()
    bluff = brain._decide_bluff({}, (3, 4))
    assert isinstance(bluff, str)
    assert "I moved" in bluff


def test_match_runner_execution():
    runner = MatchRunner(grid_size=7, max_turns=10)
    summary = runner.run_match()
    assert "outcome" in summary
    assert summary["total_turns"] > 0
    assert os.path.exists("logs/police_match.json")
