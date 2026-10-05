#!/usr/bin/env python3
"""Check the common interface and basic consistency of café submissions.

Usage:
    python mini_project/check_cafe_submission.py GROUP_01/cafe_model.py
    python mini_project/check_cafe_submission.py submissions/*/cafe_model.py
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import math
import traceback
from collections.abc import Mapping, Sequence
from pathlib import Path
from types import ModuleType
from typing import Any

import pandas as pd


STANDARD_CONFIG: dict[str, Any] = {
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

REQUIRED_RESULT_FIELDS: tuple[str, ...] = (
    "run_minutes",
    "finish_time",
    "n_arrivals",
    "n_served",
    "n_lost",
    "n_served_simple",
    "n_served_complex",
    "mean_wait",
    "p90_wait",
    "max_wait",
    "throughput_per_hour",
    "utilisation",
    "revenue",
    "total_cost",
    "profit",
)

COUNT_FIELDS: tuple[str, ...] = (
    "n_arrivals",
    "n_served",
    "n_lost",
    "n_served_simple",
    "n_served_complex",
)

NONNEGATIVE_FIELDS: tuple[str, ...] = (
    "run_minutes",
    "finish_time",
    *COUNT_FIELDS,
    "mean_wait",
    "p90_wait",
    "max_wait",
    "throughput_per_hour",
    "utilisation",
    "revenue",
    "total_cost",
)


class CheckFailure(Exception):
    """Raised when a student-facing readiness check fails."""


def require(condition: bool, message: str) -> None:
    """Raise a readable check failure when condition is false."""
    if not condition:
        raise CheckFailure(message)


def load_module(path: Path) -> ModuleType:
    """Import one submission from an explicit file path."""
    require(path.is_file(), f"file does not exist: {path}")
    require(path.suffix == ".py", "submission must be a .py file")

    module_name = f"scim211_cafe_{abs(hash(path.resolve()))}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    require(spec is not None and spec.loader is not None, "could not create an import specification")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def as_finite_number(value: Any, field: str) -> float:
    """Return value as float after rejecting booleans and non-finite values."""
    require(not isinstance(value, bool), f"{field} must be numeric, not Boolean")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise CheckFailure(f"{field} must be numeric") from exc
    require(math.isfinite(number), f"{field} must be finite")
    return number


def close(actual: Any, expected: Any, *, tolerance: float = 1e-7) -> bool:
    """Compare two numeric values using a small scale-aware tolerance."""
    actual_number = as_finite_number(actual, "actual value")
    expected_number = as_finite_number(expected, "expected value")
    return math.isclose(actual_number, expected_number, rel_tol=tolerance, abs_tol=tolerance)


def validate_result(result: Any, config: Mapping[str, Any], label: str) -> dict[str, Any]:
    """Validate one result dictionary and its required accounting identities."""
    require(isinstance(result, dict), f"{label}: simulate_cafe must return a dictionary")

    missing = [field for field in REQUIRED_RESULT_FIELDS if field not in result]
    require(not missing, f"{label}: missing result fields: {', '.join(missing)}")

    numbers = {field: as_finite_number(result[field], field) for field in REQUIRED_RESULT_FIELDS}

    for field in NONNEGATIVE_FIELDS:
        require(numbers[field] >= 0.0, f"{label}: {field} cannot be negative")

    for field in COUNT_FIELDS:
        require(numbers[field].is_integer(), f"{label}: {field} must be a whole number")

    require(close(numbers["run_minutes"], config["run_minutes"]), f"{label}: run_minutes must copy config")
    require(
        numbers["finish_time"] + 1e-7 >= numbers["run_minutes"],
        f"{label}: finish_time cannot be earlier than closing time",
    )
    require(numbers["utilisation"] <= 1.0 + 1e-7, f"{label}: utilisation must be between 0 and 1")
    require(
        close(numbers["n_arrivals"], numbers["n_served"] + numbers["n_lost"]),
        f"{label}: n_arrivals must equal n_served + n_lost",
    )
    require(
        close(numbers["n_served"], numbers["n_served_simple"] + numbers["n_served_complex"]),
        f"{label}: n_served must equal simple + complex served",
    )
    require(numbers["mean_wait"] <= numbers["max_wait"] + 1e-7, f"{label}: mean_wait cannot exceed max_wait")
    require(numbers["p90_wait"] <= numbers["max_wait"] + 1e-7, f"{label}: p90_wait cannot exceed max_wait")

    expected_throughput = numbers["n_served"] / (float(config["run_minutes"]) / 60.0)
    require(
        close(numbers["throughput_per_hour"], expected_throughput),
        f"{label}: throughput_per_hour is inconsistent with n_served and run_minutes",
    )

    expected_revenue = (
        numbers["n_served_simple"] * float(config["price_simple"])
        + numbers["n_served_complex"] * float(config["price_complex"])
    )
    require(close(numbers["revenue"], expected_revenue), f"{label}: revenue is inconsistent with completed orders")

    expected_cost = (
        numbers["n_served_simple"] * float(config["cost_simple"])
        + numbers["n_served_complex"] * float(config["cost_complex"])
        + float(config["n_baristas"])
        * float(config["barista_cost_per_hour"])
        * (float(config["run_minutes"]) / 60.0)
    )
    require(close(numbers["total_cost"], expected_cost), f"{label}: total_cost is inconsistent with orders and staffing")
    require(close(numbers["profit"], numbers["revenue"] - numbers["total_cost"]), f"{label}: profit must equal revenue - total_cost")

    if numbers["n_served"] == 0:
        for field in ("mean_wait", "p90_wait", "max_wait"):
            require(close(numbers[field], 0.0), f"{label}: {field} must be 0 when nobody is served")

    return result


def required_projection(result: Mapping[str, Any]) -> tuple[float, ...]:
    """Create a comparable tuple containing only required result fields."""
    return tuple(as_finite_number(result[field], field) for field in REQUIRED_RESULT_FIELDS)


def check_submission(path: Path) -> None:
    """Run all readiness checks for one submission."""
    module = load_module(path)
    simulate = getattr(module, "simulate_cafe", None)
    replicate = getattr(module, "run_replications", None)
    require(callable(simulate), "missing callable simulate_cafe(config, seed)")
    require(callable(replicate), "missing callable run_replications(config, seeds)")

    config = copy.deepcopy(STANDARD_CONFIG)
    untouched = copy.deepcopy(config)
    first = validate_result(simulate(config, 211), config, "standard run")
    require(config == untouched, "simulate_cafe modified the supplied configuration dictionary")

    repeated = validate_result(simulate(copy.deepcopy(config), 211), config, "repeated-seed run")
    require(
        required_projection(first) == required_projection(repeated),
        "the same configuration and seed did not reproduce the same result",
    )

    different = validate_result(simulate(copy.deepcopy(config), 212), config, "different-seed run")
    stochastic_fields = ("n_arrivals", "n_served_simple", "mean_wait", "p90_wait", "max_wait")
    require(
        any(not close(first[field], different[field]) for field in stochastic_fields),
        "different seeds produced identical stochastic outputs; check that seed is used",
    )

    zero_config = copy.deepcopy(STANDARD_CONFIG)
    zero_config["arrival_rate_per_hour"] = 0.0
    zero = validate_result(simulate(zero_config, 301), zero_config, "zero-arrival run")
    for field in ("n_arrivals", "n_served", "n_lost", "n_served_simple", "n_served_complex"):
        require(close(zero[field], 0.0), f"zero-arrival run: {field} must be 0")
    for field in ("mean_wait", "p90_wait", "max_wait", "throughput_per_hour", "revenue"):
        require(close(zero[field], 0.0), f"zero-arrival run: {field} must be 0")

    simple_config = copy.deepcopy(STANDARD_CONFIG)
    simple_config.update(
        {
            "run_minutes": 60.0,
            "simple_order_probability": 1.0,
            "price_simple": 91.0,
            "cost_simple": 17.0,
            "max_queue": None,
        }
    )
    simple = validate_result(simulate(simple_config, 401), simple_config, "simple-only run")
    require(close(simple["n_served_complex"], 0), "simple_order_probability=1 still produced complex orders")

    complex_config = copy.deepcopy(STANDARD_CONFIG)
    complex_config.update(
        {
            "run_minutes": 60.0,
            "simple_order_probability": 0.0,
            "price_complex": 137.0,
            "cost_complex": 43.0,
            "max_queue": None,
        }
    )
    complex_result = validate_result(simulate(complex_config, 402), complex_config, "complex-only run")
    require(close(complex_result["n_served_simple"], 0), "simple_order_probability=0 still produced simple orders")

    unlimited_config = copy.deepcopy(STANDARD_CONFIG)
    unlimited_config.update(
        {
            "arrival_rate_per_hour": 72.0,
            "n_baristas": 1,
            "mean_service_simple": 5.0,
            "mean_service_complex": 7.0,
            "max_queue": None,
        }
    )
    capped_config = copy.deepcopy(unlimited_config)
    capped_config["max_queue"] = 0
    unlimited = validate_result(simulate(unlimited_config, 503), unlimited_config, "unlimited-queue run")
    capped = validate_result(simulate(capped_config, 503), capped_config, "zero-queue run")
    require(close(unlimited["n_lost"], 0), "max_queue=None must not refuse customers because of queue length")
    require(float(capped["n_lost"]) > 0, "max_queue=0 did not refuse any customers in the stress run")

    heavy_one = copy.deepcopy(STANDARD_CONFIG)
    heavy_one.update({"arrival_rate_per_hour": 54.0, "n_baristas": 1, "max_queue": None})
    heavy_three = copy.deepcopy(heavy_one)
    heavy_three["n_baristas"] = 3
    one_barista = validate_result(simulate(heavy_one, 907), heavy_one, "one-barista stress run")
    three_baristas = validate_result(simulate(heavy_three, 907), heavy_three, "three-barista stress run")
    require(
        float(three_baristas["mean_wait"]) <= float(one_barista["mean_wait"]) + 1e-7,
        "three baristas increased mean waiting time in the stress check",
    )

    seeds = [11, 22, 33, 44]
    replication_config = copy.deepcopy(STANDARD_CONFIG)
    frame = replicate(replication_config, seeds)
    require(replication_config == STANDARD_CONFIG, "run_replications modified the supplied configuration dictionary")
    require(isinstance(frame, pd.DataFrame), "run_replications must return a pandas DataFrame")
    require(len(frame) == len(seeds), "run_replications must return exactly one row per seed")

    required_columns = ("seed", *REQUIRED_RESULT_FIELDS)
    missing_columns = [column for column in required_columns if column not in frame.columns]
    require(not missing_columns, f"replication DataFrame is missing columns: {', '.join(missing_columns)}")
    require(frame["seed"].tolist() == seeds, "replication rows must preserve the supplied seed order")

    for index, seed in enumerate(seeds):
        row_result = {field: frame.iloc[index][field] for field in REQUIRED_RESULT_FIELDS}
        validate_result(row_result, STANDARD_CONFIG, f"replication row for seed {seed}")

    direct = validate_result(simulate(copy.deepcopy(STANDARD_CONFIG), seeds[0]), STANDARD_CONFIG, "direct replication check")
    first_row = frame.iloc[0]
    require(
        all(close(first_row[field], direct[field]) for field in REQUIRED_RESULT_FIELDS),
        "the first replication row does not match simulate_cafe for the same seed",
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse one or more submission paths."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submissions", nargs="+", type=Path, help="one or more cafe_model.py files")
    parser.add_argument("--debug", action="store_true", help="show a traceback for unexpected errors")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """Check every supplied file and return a shell-friendly status code."""
    args = parse_args(argv)
    failures = 0

    for path in args.submissions:
        try:
            check_submission(path)
        except CheckFailure as exc:
            failures += 1
            print(f"FAIL: {path}")
            print(f"  {exc}")
        except Exception as exc:  # Keep unexpected student-code errors readable.
            failures += 1
            print(f"FAIL: {path}")
            print(f"  {type(exc).__name__}: {exc}")
            if args.debug:
                traceback.print_exc()
        else:
            print(f"PASS: {path}")

    if len(args.submissions) > 1:
        passed = len(args.submissions) - failures
        print(f"SUMMARY: {passed} passed, {failures} failed")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
