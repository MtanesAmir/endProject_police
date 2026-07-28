import pytest
from src.domain.grid import GridPos, Direction, legal_moves, MovementEngine

def test_gridpos_creation_and_immutability():
    pos = GridPos(0, 0)
    assert pos.row == 0
    assert pos.col == 0
    assert pos.to_tuple() == (0, 0)
    assert pos.is_valid(7) is True

    # Immutability test
    with pytest.raises(AttributeError):
        pos.row = 1  # type: ignore

def test_gridpos_validity_boundaries():
    assert GridPos(0, 0).is_valid(7) is True
    assert GridPos(6, 6).is_valid(7) is True
    assert GridPos(7, 0).is_valid(7) is False
    assert GridPos(0, 7).is_valid(7) is False
    assert GridPos(-1, 0).is_valid(7) is False

def test_legal_moves_origin_corner():
    # At (0,0) in 7x7 grid: stay (0,0), down (1,0), right (0,1)
    moves = legal_moves(GridPos(0, 0), grid_size=7)
    expected = {GridPos(0, 0), GridPos(1, 0), GridPos(0, 1)}
    assert set(moves) == expected
    assert len(moves) == 3

def test_legal_moves_center():
    # At (3,3) in 7x7 grid: stay, up, down, left, right (5 moves)
    moves = legal_moves(GridPos(3, 3), grid_size=7)
    expected = {
        GridPos(3, 3),  # STAY
        GridPos(2, 3),  # UP
        GridPos(4, 3),  # DOWN
        GridPos(3, 2),  # LEFT
        GridPos(3, 4),  # RIGHT
    }
    assert set(moves) == expected
    assert len(moves) == 5

def test_legal_moves_bottom_right_corner():
    # At (6,6) in 7x7 grid: stay (6,6), up (5,6), left (6,5)
    moves = legal_moves(GridPos(6, 6), grid_size=7)
    expected = {GridPos(6, 6), GridPos(5, 6), GridPos(6, 5)}
    assert set(moves) == expected
    assert len(moves) == 3

def test_legal_moves_with_barriers():
    # At (3,3) with barriers at (2,3) [UP] and (3,4) [RIGHT]
    barriers = [GridPos(2, 3), (3, 4)]
    moves = legal_moves(GridPos(3, 3), grid_size=7, barriers=barriers)
    expected = {
        GridPos(3, 3),  # STAY
        GridPos(4, 3),  # DOWN
        GridPos(3, 2),  # LEFT
    }
    assert set(moves) == expected
    assert len(moves) == 3

def test_movement_engine():
    engine = MovementEngine(initial_pos=(0, 0), grid_size=7)
    assert engine.get_position() == GridPos(0, 0)
    
    # Try invalid move (UP from 0,0)
    assert engine.move(Direction.UP) is False
    assert engine.get_position() == GridPos(0, 0)

    # Valid move (DOWN to 1,0)
    assert engine.move(Direction.DOWN) is True
    assert engine.get_position() == GridPos(1, 0)

    # Valid move (RIGHT to 1,1)
    assert engine.move(Direction.RIGHT) is True
    assert engine.get_position() == GridPos(1, 1)

    # Preview move without changing state
    preview = engine.preview_move(Direction.LEFT)
    assert preview == GridPos(1, 0)
    assert engine.get_position() == GridPos(1, 1)
