"""Example demonstrating Bayesian belief heatmap updates from scent and verbal hints."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.domain.belief import BayesianBeliefMap

def main():
    belief = BayesianBeliefMap(grid_size=7)
    pos = belief.get_most_likely_position()
    print(f"Initial most likely position: {pos}")

if __name__ == "__main__":
    main()
