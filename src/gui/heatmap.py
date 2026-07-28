"""Police Live GUI & Belief Heatmap Visualizer.

Renders 7x7 grid, local truth (police position, barriers),
dynamic Bayesian belief heatmap, and turn status banner.
"""

from typing import List, Tuple, Set, Optional, Dict, Any, Union


class HeatmapVisualizer:
    """Visualizer for Police local truth and Bayesian belief heatmap on a 7x7 grid."""

    GRID_SIZE = 7

    def __init__(self, grid_size: int = 7, root: Any = None):
        self.grid_size = grid_size
        self.root = root
        self.police_pos: Optional[Tuple[int, int]] = None
        self.barriers: Set[Tuple[int, int]] = set()
        self.belief_matrix: List[List[float]] = [
            [1.0 / (grid_size * grid_size) for _ in range(grid_size)]
            for _ in range(grid_size)
        ]
        self.banner_status: str = "LOCKED"
        self.banner_color: str = "GRAY"
        self.inputs_enabled: bool = False

    def update_heatmap(self, belief_matrix: List[List[float]]) -> None:
        """Update the 7x7 Bayesian belief matrix."""
        if len(belief_matrix) != self.grid_size or any(
            len(row) != self.grid_size for row in belief_matrix
        ):
            raise ValueError(f"Belief matrix must be {self.grid_size}x{self.grid_size}")
        
        # Clamp and normalize belief probabilities
        new_matrix = []
        for r in range(self.grid_size):
            row = []
            for c in range(self.grid_size):
                val = float(belief_matrix[r][c])
                val = max(0.0, min(1.0, val))
                row.append(val)
            new_matrix.append(row)
        self.belief_matrix = new_matrix

    def update_belief(self, belief_matrix: List[List[float]]) -> None:
        """Alias for update_heatmap."""
        self.update_heatmap(belief_matrix)

    def update_banner(self, status: Union[str, bool]) -> None:
        """Update the turn status banner.
        
        If status is True or contains 'YOUR TURN' / 'GREEN', sets status to GREEN / 'YOUR TURN'.
        Otherwise sets status to GRAY / 'LOCKED'.
        """
        if isinstance(status, bool):
            if status:
                self.banner_status = "YOUR TURN"
                self.banner_color = "GREEN"
                self.inputs_enabled = True
            else:
                self.banner_status = "LOCKED"
                self.banner_color = "GRAY"
                self.inputs_enabled = False
        else:
            status_str = str(status).strip().upper()
            if "YOUR TURN" in status_str or "GREEN" in status_str:
                self.banner_status = "YOUR TURN"
                self.banner_color = "GREEN"
                self.inputs_enabled = True
            else:
                self.banner_status = "LOCKED"
                self.banner_color = "GRAY"
                self.inputs_enabled = False

    def update_local_truth(
        self,
        police_pos: Optional[Tuple[int, int]],
        barriers: Optional[Union[Set[Tuple[int, int]], List[Tuple[int, int]]]] = None,
        **kwargs: Any
    ) -> None:
        """Update Police local truth state (police position and barriers).
        
        Enforces local truth isolation: any secret global state (e.g. thief position)
        passed in kwargs is explicitly ignored/stripped.
        """
        # Strict local truth isolation filter: discard any thief position keys if present
        if "thief_pos" in kwargs:
            kwargs.pop("thief_pos")
        if "thief_position" in kwargs:
            kwargs.pop("thief_position")
        if "global_thief" in kwargs:
            kwargs.pop("global_thief")

        if police_pos is not None:
            r, c = police_pos
            if not (0 <= r < self.grid_size and 0 <= c < self.grid_size):
                raise ValueError(f"Police position {police_pos} out of grid bounds")
            self.police_pos = (r, c)

        if barriers is not None:
            self.barriers = set(barriers)

    def get_cell_color(self, r: int, c: int) -> str:
        """Map belief probability [0.0..1.0] at cell (r, c) to hex color gradient.
        
        0.0 -> White (#ffffff)
        1.0 -> Deep Red (#ff0000)
        """
        prob = self.belief_matrix[r][c]
        # Red component stays 255, Green and Blue decrease from 255 to 0 as prob increases
        gb = int((1.0 - prob) * 255)
        gb = max(0, min(255, gb))
        return f"#ff{gb:02x}{gb:02x}"

    def get_grid_state(self) -> Dict[str, Any]:
        """Return full visual representation of local grid state."""
        cell_colors = [
            [self.get_cell_color(r, c) for c in range(self.grid_size)]
            for r in range(self.grid_size)
        ]
        return {
            "grid_size": self.grid_size,
            "police_pos": self.police_pos,
            "barriers": list(self.barriers),
            "belief_matrix": self.belief_matrix,
            "cell_colors": cell_colors,
            "banner_status": self.banner_status,
            "banner_color": self.banner_color,
            "inputs_enabled": self.inputs_enabled,
        }

    def render(self) -> Dict[str, Any]:
        """Render frame representation of the GUI state."""
        return self.get_grid_state()
