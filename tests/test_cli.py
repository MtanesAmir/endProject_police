"""Unit tests for CLI runner module."""

import pytest
from src.cli import create_parser, main


def test_cli_parser_peer():
    parser = create_parser()
    args = parser.parse_args(["peer", "--role", "police", "--port", "8000"])
    assert args.command == "peer"
    assert args.role == "police"
    assert args.port == 8000


def test_cli_parser_replay():
    parser = create_parser()
    args = parser.parse_args(["replay", "--log", "logs/police_match.json"])
    assert args.command == "replay"
    assert args.log == "logs/police_match.json"


def test_cli_main_peer_execution():
    exit_code = main(["peer", "--role", "thief", "--port", "8001"])
    assert exit_code == 0
