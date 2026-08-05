#!/bin/bash
# Example shell script for creating and verifying submission tag

echo "[Git Tag Example] Checking repository status..."
git status

echo "[Git Tag Example] Creating annotated submission tag v1.0-submission..."
git tag -a v1.0-submission -m "Final submission: Police-Thief P2P, group Police-Thief-Team"

echo "[Git Tag Example] Verifying tag..."
git show v1.0-submission --stat
