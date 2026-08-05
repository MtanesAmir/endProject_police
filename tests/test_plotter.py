"""Unit tests for ExperimentPlotter module."""

import os
import pytest
from src.experiments.plotter import ExperimentPlotter


def test_experiment_plotter_scent_decay():
    plotter = ExperimentPlotter(output_dir="assets")
    path = plotter.plot_scent_decay(decay_rate=0.10, turns=10)
    assert os.path.exists(path)


def test_experiment_plotter_strategy_winrates():
    plotter = ExperimentPlotter(output_dir="assets")
    path = plotter.plot_strategy_winrates(cop_wins=5, thief_wins=5)
    assert os.path.exists(path)
