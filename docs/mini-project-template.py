"""Required interface for the SCIM211 Coffee Shop Simulation Hackathon.

Save your completed file as ``cafe_model.py``. Do not change the names or
arguments of the two required functions. Follow the model rules in the
handout: Poisson arrivals, exponential service times by order type, uniform
patience between 0.5 and 1.5 times ``mean_patience``, one FCFS queue, and the
``max_queue`` rule.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

import numpy as np
import pandas as pd


BASE_CONFIG: dict[str, Any] = {
    "run_minutes": 120.0,
    "arrival_rate_per_hour": 30.0,
    "n_baristas": 2,
    "simple_order_probability": 0.45,
    "mean_service_simple": 2.0,
    "mean_service_complex": 4.0,
    "mean_patience": 10.0,
    "price_simple": 85.0,
    "price_complex": 120.0,
    "cost_simple": 25.0,
    "cost_complex": 40.0,
    "barista_cost_per_hour": 120.0,
    "max_queue": 8,
}


def simulate_cafe(config: Mapping[str, Any], seed: int) -> dict[str, float | int]:
    """Run one complete café replication and return the required dictionary."""
    # TODO: Read every value from config. Do not modify config itself.
    # TODO: Create one generator from seed, e.g. rng = np.random.default_rng(seed).
    # TODO: Generate customers: arrival time, order type, service time, patience.
    #       mean_patience = None means the customer never leaves the queue.
    # TODO: Simulate arrival, service-start, service-completion, and
    #       patience-expiry (reneging) events in time order.
    #       An arriving customer balks if every barista is busy and max_queue
    #       customers are already waiting (max_queue = None means no limit).
    # TODO: Calculate all required counts, waiting measures, and financial
    #       outputs, then return them in one dictionary.
    raise NotImplementedError("Complete simulate_cafe before running the checker")


def run_replications(config: Mapping[str, Any], seeds: Iterable[int]) -> pd.DataFrame:
    """Run one replication per seed and return one result row per seed."""
    rows: list[dict[str, float | int]] = []

    for seed in seeds:
        result = simulate_cafe(config, int(seed))
        rows.append({"seed": int(seed), **result})

    return pd.DataFrame(rows)


if __name__ == "__main__":
    # Experiments and plots belong here, so they do not run when the checker
    # imports this file.
    results = run_replications(BASE_CONFIG, range(1000, 1040))
    print(results[["mean_wait", "n_reneged", "profit"]].describe())
