import pytest
from src.domain.grid import GridPos
from src.domain.barriers import BarrierManager

def test_barrier_manager_initialization():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    assert manager.max_barriers == 14
    assert manager.remaining_barriers == 14
    assert len(manager.get_barriers()) == 0

def test_place_barrier_valid():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    police_pos = GridPos(3, 3)
    barrier_target = GridPos(3, 4)

    assert manager.place_barrier(barrier_target, police_pos=police_pos) is True
    assert manager.remaining_barriers == 13
    assert manager.is_blocked(barrier_target) is True
    assert GridPos(3, 4) in manager.get_barriers()

def test_place_barrier_quota_enforcement():
    manager = BarrierManager(max_barriers=2, grid_size=7)
    assert manager.place_barrier((0, 0)) is True
    assert manager.place_barrier((0, 1)) is True
    assert manager.remaining_barriers == 0
    # Third barrier should fail due to quota limit
    assert manager.place_barrier((0, 2)) is False
    assert manager.remaining_barriers == 0

def test_place_barrier_invalid_distance():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    police_pos = GridPos(0, 0)
    # Distance > 1 (e.g., 2,2)
    far_target = GridPos(2, 2)
    assert manager.place_barrier(far_target, police_pos=police_pos) is False
    assert manager.is_blocked(far_target) is False

def test_place_barrier_on_police_cell():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    police_pos = GridPos(3, 3)
    # Attempt to place barrier on police's own position
    assert manager.place_barrier(police_pos, police_pos=police_pos) is False

def test_place_barrier_out_of_bounds():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    assert manager.place_barrier((-1, 0)) is False
    assert manager.place_barrier((7, 3)) is False

def test_place_barrier_duplicate_placement():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    assert manager.place_barrier((2, 2)) is True
    assert manager.remaining_barriers == 13
    # Second placement at same location should return False
    assert manager.place_barrier((2, 2)) is False
    assert manager.remaining_barriers == 13

def test_place_barrier_occupied_position():
    manager = BarrierManager(max_barriers=14, grid_size=7)
    police_pos = GridPos(1, 1)
    thief_pos = GridPos(1, 2)
    # Cannot place barrier on occupied thief cell
    assert manager.place_barrier(thief_pos, police_pos=police_pos, occupied_positions=[police_pos, thief_pos]) is False
