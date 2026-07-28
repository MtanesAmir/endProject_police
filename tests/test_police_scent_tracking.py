"""Unit tests for Police Scent Field & Stigmergic Trail Tracker (police_scent_tracking)."""

import math
import pytest
from src.domain.scent import ScentTracker, GRID_SIZE, DEFAULT_TAU_CENTER, DEFAULT_RHO


def test_scent_tracker_initialization():
    tracker = ScentTracker()
    assert tracker.grid_size == GRID_SIZE
    matrix = tracker.get_matrix()
    assert len(matrix) == 7
    for row in matrix:
        assert len(row) == 7
        assert all(val == 0.0 for val in row)


def test_apply_emission_center_and_radial_5x5():
    tracker = ScentTracker()
    center_pos = (3, 3)
    tracker.apply_emission(center_pos, tau_center=0.90)

    # Center cell dist = 0 -> 0.90 / (1 + 0) = 0.90
    assert pytest.approx(tracker.get_scent_level((3, 3)), 1e-5) == 0.90

    # Orthogonal neighbor (3, 4) dist = 1 -> 0.90 / (1 + 1) = 0.45
    assert pytest.approx(tracker.get_scent_level((3, 4)), 1e-5) == 0.45
    assert pytest.approx(tracker.get_scent_level((2, 3)), 1e-5) == 0.45

    # Diagonal neighbor (4, 4) dist = sqrt(2) -> 0.90 / (1 + sqrt(2))
    expected_diag = 0.90 / (1.0 + math.sqrt(2))
    assert pytest.approx(tracker.get_scent_level((4, 4)), 1e-5) == expected_diag

    # Distance 2 cell (3, 5) dist = 2 -> 0.90 / (1 + 2) = 0.30
    assert pytest.approx(tracker.get_scent_level((3, 5)), 1e-5) == 0.30

    # Outside 5x5 window cell (3, 6) dist = 3 -> 0.0
    assert tracker.get_scent_level((3, 6)) == 0.0
    assert tracker.get_scent_level((0, 0)) == 0.0


def test_apply_emission_boundary():
    tracker = ScentTracker()
    tracker.apply_emission((0, 0), tau_center=0.90)

    assert pytest.approx(tracker.get_scent_level((0, 0)), 1e-5) == 0.90
    assert pytest.approx(tracker.get_scent_level((0, 1)), 1e-5) == 0.45
    assert pytest.approx(tracker.get_scent_level((1, 0)), 1e-5) == 0.45
    # Scent outside bounds is ignored without error
    assert tracker.get_scent_level((6, 6)) == 0.0


def test_apply_decay_single_turn():
    tracker = ScentTracker()
    tracker.apply_emission((3, 3), tau_center=0.90)
    initial_center = tracker.get_scent_level((3, 3))

    tracker.apply_decay(rho=0.10)
    decayed_center = tracker.get_scent_level((3, 3))

    assert pytest.approx(decayed_center, 1e-5) == initial_center * 0.90


def test_multi_turn_decay_progression():
    tracker = ScentTracker()
    tracker.apply_emission((3, 3), tau_center=1.0)
    initial = tracker.get_scent_level((3, 3))

    # Simulate 5 turns of decay
    rho = 0.10
    retention = 1.0 - rho
    current = initial
    for turn in range(1, 6):
        tracker.apply_decay(rho=rho)
        current *= retention
        assert pytest.approx(tracker.get_scent_level((3, 3)), 1e-5) == current

    # Exponential decay formula test: tau(t) = tau(0) * (1-rho)^t
    expected_t5 = initial * (retention**5)
    assert pytest.approx(tracker.get_scent_level((3, 3)), 1e-5) == expected_t5


def test_multiple_emissions_accumulation():
    tracker = ScentTracker()
    tracker.apply_emission((3, 3), tau_center=0.90)
    tracker.apply_emission((3, 3), tau_center=0.50)

    # Accumulation at center
    assert pytest.approx(tracker.get_scent_level((3, 3)), 1e-5) == 1.40


def test_reset_and_matrix_copy():
    tracker = ScentTracker()
    tracker.apply_emission((2, 2), tau_center=0.90)
    matrix_copy = tracker.get_matrix()
    matrix_copy[2][2] = 999.0

    # Ensure internal matrix not modified
    assert tracker.get_scent_level((2, 2)) != 999.0

    tracker.reset()
    assert tracker.get_scent_level((2, 2)) == 0.0
