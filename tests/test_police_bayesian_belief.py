"""Unit tests for Police Bayesian Belief Map Engine (police_bayesian_belief)."""

import pytest
from src.domain.belief import BeliefGrid, BayesianBeliefMap, GRID_SIZE
from src.domain.scent import ScentTracker


def test_initialization_uniform_distribution():
    belief = BeliefGrid()
    grid = belief.get_grid()
    assert len(grid) == 7
    expected_prob = 1.0 / 49.0
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            assert pytest.approx(grid[r][c], 1e-5) == expected_prob

    # Sum of probabilities must equal 1.0
    total_prob = sum(sum(row) for row in grid)
    assert pytest.approx(total_prob, 1e-5) == 1.0


def test_normalization_maintains_sum_one():
    belief = BeliefGrid()
    # Manually modify grid values
    belief.grid[0][0] = 5.0
    belief.grid[1][1] = 5.0
    belief.normalize()

    total_prob = sum(sum(row) for row in belief.get_grid())
    assert pytest.approx(total_prob, 1e-5) == 1.0


def test_update_from_scent_concentrates_belief():
    tracker = ScentTracker()
    # Emit scent centered at (2, 4)
    tracker.apply_emission((2, 4), tau_center=0.90)
    scent_matrix = tracker.get_matrix()

    belief = BeliefGrid()
    belief.update_from_scent(scent_matrix)

    # Highest scent position should have highest belief
    most_likely = belief.get_most_likely_position()
    assert most_likely == (2, 4)

    # Check sum is 1.0
    total_prob = sum(sum(row) for row in belief.get_grid())
    assert pytest.approx(total_prob, 1e-5) == 1.0

    # Probability at (2, 4) should be significantly higher than uniform prior
    assert belief.grid[2][4] > (1.0 / 49.0)


def test_update_from_hint():
    belief = BeliefGrid()
    hint_pos = (5, 1)
    belief.update_from_hint(hint_pos, reliability=0.8)

    # Hint position should be most likely
    assert belief.get_most_likely_position() == (5, 1)

    # Sum of probabilities must equal 1.0
    total_prob = sum(sum(row) for row in belief.get_grid())
    assert pytest.approx(total_prob, 1e-5) == 1.0


def test_detect_bluff():
    tracker = ScentTracker()
    # Scent emitted at (1, 1)
    tracker.apply_emission((1, 1), tau_center=0.90)
    scent_matrix = tracker.get_matrix()

    belief = BeliefGrid()
    # Hint claims thief is at (6, 6) where scent is 0.0
    is_bluff = belief.detect_bluff(scent_matrix, (6, 6), threshold=0.10)
    assert is_bluff is True

    # Hint claims thief is at (1, 1) where scent is high
    is_bluff_true = belief.detect_bluff(scent_matrix, (1, 1), threshold=0.10)
    assert is_bluff_true is False


def test_generic_update_belief_observation():
    belief = BeliefGrid()
    tracker = ScentTracker()
    tracker.apply_emission((3, 3), tau_center=0.90)

    obs = {
        "scent": tracker.get_matrix(),
        "hint": {"position": (3, 3), "reliability": 0.9}
    }
    belief.update_belief(obs)
    assert belief.get_most_likely_position() == (3, 3)


def test_bayesian_belief_map_alias():
    # Verify BayesianBeliefMap alias works identical to BeliefGrid
    bmap = BayesianBeliefMap()
    assert isinstance(bmap, BeliefGrid)
    bmap.reset()
    assert bmap.get_most_likely_position() == (0, 0)
