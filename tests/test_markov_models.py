"""Placeholder tests for Markov chain helpers."""

import numpy as np
import pytest

from src.markov_models import simulate_customer_path


@pytest.mark.xfail(reason="simulate_customer_path is currently a TODO stub")
def test_simulate_customer_returns_correct_path_length():
    """A simulated customer path should include the initial state and n steps."""
    states = ["loyal", "occasional", "inactive"]
    transition_matrix = np.array(
        [
            [0.7, 0.2, 0.1],
            [0.3, 0.5, 0.2],
            [0.1, 0.2, 0.7],
        ]
    )

    path = simulate_customer_path(
        states=states,
        transition_matrix=transition_matrix,
        initial_state="loyal",
        n_steps=4,
        seed=1,
    )

    assert len(path) == 5
