"""Required interface for the SCIM211 Coffee Shop Simulation Hackathon.

Rename a copy of this file to ``cafe_model.py`` and complete the model.
Do not change the names or arguments of the two required functions.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

import pandas as pd


BASE_CONFIG: dict[str, Any] = {
    "run_minutes": 120.0,
    "arrival_rate_per_hour": 24.0,
    "n_baristas": 2,
    "simple_order_probability": 0.45,
    "mean_service_simple": 2.0,
    "mean_service_complex": 4.0,
    "price_simple": 85.0,
    "price_complex": 120.0,
    "cost_simple": 25.0,
    "cost_complex": 40.0,
    "barista_cost_per_hour": 120.0,
    "max_queue": 8,
}


def simulate_cafe(config: Mapping[str, Any], seed: int) -> dict[str, float | int]:
    """Run one complete café replication and return the required dictionary."""
    # TODO: Validate or copy the configuration without modifying the input object.
    # TODO: Create one random-number generator from seed.
    # TODO: Generate arrivals and order types.
    # TODO: Simulate the queue and barista service-completion events.
    # TODO: Calculate all required counts, waiting measures, and financial outputs.
    raise NotImplementedError("Complete simulate_cafe before running the checker")


def run_replications(config: Mapping[str, Any], seeds: Iterable[int]) -> pd.DataFrame:
    """Run one replication per seed and return one result row per seed."""
    rows: list[dict[str, float | int]] = []

    for seed in seeds:
        result = simulate_cafe(config, int(seed))
        rows.append({"seed": int(seed), **result})

    return pd.DataFrame(rows)
