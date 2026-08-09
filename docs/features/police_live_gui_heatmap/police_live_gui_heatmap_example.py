"""Example demonstrating live GUI heatmap model data generation and turn banner states."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.gui.heatmap import HeatmapVisualizer

def main():
    visualizer = HeatmapVisualizer(grid_size=7)
    print(f"HeatmapVisualizer initialized with grid size: {visualizer.grid_size}")

if __name__ == "__main__":
    main()
