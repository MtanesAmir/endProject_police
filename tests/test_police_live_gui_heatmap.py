"""Unit tests for Police Live GUI & Belief Heatmap Visualizer (`police_live_gui_heatmap`)."""

import pytest
from src.gui.heatmap import HeatmapVisualizer
from src.gui.live_gui import HeatmapVisualizer as LiveGUIHeatmapVisualizer


def test_visualizer_initialization():
    """Verify 7x7 grid layout and initial state defaults."""
    viz = HeatmapVisualizer(grid_size=7)
    assert viz.grid_size == 7
    assert viz.police_pos is None
    assert len(viz.barriers) == 0
    assert len(viz.belief_matrix) == 7
    assert all(len(row) == 7 for row in viz.belief_matrix)
    assert viz.banner_status == "LOCKED"
    assert viz.banner_color == "GRAY"
    assert not viz.inputs_enabled


def test_update_heatmap_color_gradient():
    """Verify belief matrix update and cell color gradient calculation."""
    viz = HeatmapVisualizer(grid_size=7)
    
    # Custom belief matrix
    matrix = [[0.0 for _ in range(7)] for _ in range(7)]
    matrix[0][0] = 0.0
    matrix[3][3] = 0.5
    matrix[6][6] = 1.0
    
    viz.update_heatmap(matrix)
    
    # Cell 0,0 (prob 0.0) -> White #ffffff
    assert viz.get_cell_color(0, 0) == "#ffffff"
    
    # Cell 6,6 (prob 1.0) -> Deep Red #ff0000
    assert viz.get_cell_color(6, 6) == "#ff0000"
    
    # Cell 3,3 (prob 0.5) -> Mid intensity gradient
    color_mid = viz.get_cell_color(3, 3)
    assert color_mid.startswith("#ff")
    assert color_mid != "#ffffff" and color_mid != "#ff0000"


def test_invalid_heatmap_dimensions():
    """Verify error handling on invalid matrix dimensions."""
    viz = HeatmapVisualizer(grid_size=7)
    invalid_matrix = [[0.1 for _ in range(5)] for _ in range(5)]
    
    with pytest.raises(ValueError):
        viz.update_heatmap(invalid_matrix)


def test_update_banner_turn_status():
    """Verify turn status banner transitions between GREEN YOUR TURN and GRAY LOCKED."""
    viz = HeatmapVisualizer(grid_size=7)
    
    # Test transition to YOUR TURN
    viz.update_banner("YOUR TURN")
    assert viz.banner_status == "YOUR TURN"
    assert viz.banner_color == "GREEN"
    assert viz.inputs_enabled is True
    
    # Test transition with boolean True
    viz.update_banner(True)
    assert viz.banner_status == "YOUR TURN"
    assert viz.banner_color == "GREEN"
    assert viz.inputs_enabled is True

    # Test transition to LOCKED
    viz.update_banner("LOCKED")
    assert viz.banner_status == "LOCKED"
    assert viz.banner_color == "GRAY"
    assert viz.inputs_enabled is False

    # Test transition with boolean False
    viz.update_banner(False)
    assert viz.banner_status == "LOCKED"
    assert viz.banner_color == "GRAY"
    assert viz.inputs_enabled is False


def test_local_truth_isolation_filter():
    """Verify local truth filter ensures secret global Thief position is NEVER rendered or stored."""
    viz = HeatmapVisualizer(grid_size=7)
    
    # Update local truth with police pos and barriers, passing forbidden thief_pos in kwargs
    viz.update_local_truth(
        police_pos=(2, 3),
        barriers=[(1, 1), (4, 4)],
        thief_pos=(5, 5),  # Secret thief position
        thief_position=(5, 5),
        global_thief=(5, 5)
    )
    
    state = viz.get_grid_state()
    
    assert state["police_pos"] == (2, 3)
    assert (1, 1) in state["barriers"]
    assert (4, 4) in state["barriers"]
    
    # Ensure secret thief position key is NOT in grid state output
    assert "thief_pos" not in state
    assert "thief_position" not in state
    assert "global_thief" not in state
    assert not hasattr(viz, "thief_pos")
    assert not hasattr(viz, "thief_position")


def test_render_representation():
    """Verify render output structure."""
    viz = HeatmapVisualizer(grid_size=7)
    viz.update_local_truth(police_pos=(0, 0), barriers=[(0, 1)])
    viz.update_banner("YOUR TURN")
    
    frame = viz.render()
    assert frame["grid_size"] == 7
    assert frame["police_pos"] == (0, 0)
    assert (0, 1) in frame["barriers"]
    assert frame["banner_status"] == "YOUR TURN"
    assert frame["banner_color"] == "GREEN"
    assert len(frame["cell_colors"]) == 7
