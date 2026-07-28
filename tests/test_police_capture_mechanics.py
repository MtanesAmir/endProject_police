import pytest
from src.domain.grid import GridPos
from src.domain.capture import (
    check_capture,
    CaptureDetector,
    COP_CAPTURE_SCORE,
    THIEF_CAPTURE_SCORE,
)

def test_check_capture_direct():
    police = GridPos(3, 3)
    thief = GridPos(3, 3)
    assert check_capture(police, thief, radius=1) is True
    assert check_capture(police, thief, radius=0) is True

def test_check_capture_adjacent():
    police = GridPos(3, 3)
    thief_orthogonal = GridPos(3, 4)
    thief_diagonal = GridPos(4, 4)
    thief_far = GridPos(5, 5)

    # Orthogonal adjacent
    assert check_capture(police, thief_orthogonal, radius=1) is True
    assert check_capture(police, thief_orthogonal, radius=0) is False

    # Diagonal adjacent
    assert check_capture(police, thief_diagonal, radius=1) is True
    assert check_capture(police, thief_diagonal, radius=0) is False

    # Far away
    assert check_capture(police, thief_far, radius=1) is False

def test_capture_detector_direct_capture():
    police = (2, 2)
    thief = (2, 2)
    detector = CaptureDetector()

    assert detector.check_direct_capture(police, thief) is True
    assert detector.check_direct_capture((2, 2), (2, 3)) is False

def test_capture_detector_trapped_capture_corner():
    # Corner (0,0): only adjacent cells are (0,1) and (1,0). If both blocked, trapped!
    thief = GridPos(0, 0)
    barriers = [GridPos(0, 1), GridPos(1, 0)]
    assert CaptureDetector.check_trapped_capture(thief, barriers=barriers, grid_size=7) is True

def test_capture_detector_trapped_capture_center():
    # Center (3,3): adjacent cells are (2,3), (4,3), (3,2), (3,4)
    thief = GridPos(3, 3)
    barriers = [GridPos(2, 3), GridPos(4, 3), GridPos(3, 2), GridPos(3, 4)]
    assert CaptureDetector.check_trapped_capture(thief, barriers=barriers, grid_size=7) is True

def test_capture_detector_not_trapped():
    thief = GridPos(3, 3)
    barriers = [GridPos(2, 3), GridPos(4, 3), GridPos(3, 2)]
    # (3,4) is free
    assert CaptureDetector.check_trapped_capture(thief, barriers=barriers, grid_size=7) is False

def test_scoring_map_values():
    assert COP_CAPTURE_SCORE == 20
    assert THIEF_CAPTURE_SCORE == 5
    assert CaptureDetector.COP_CAPTURE_SCORE == 20
    assert CaptureDetector.THIEF_CAPTURE_SCORE == 5
