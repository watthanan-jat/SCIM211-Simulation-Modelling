"""Placeholder tests for queue simulator helpers."""

import pandas as pd
import pytest

from src.queue_simulator import simulate_mm1_queue


@pytest.mark.xfail(reason="simulate_mm1_queue is currently a TODO stub")
def test_simulate_queue_returns_expected_object_types():
    """Queue simulation should return a tabular result object."""
    result = simulate_mm1_queue(arrival_rate=1.0, service_rate=1.5, n_customers=5, seed=1)

    assert isinstance(result, pd.DataFrame)
