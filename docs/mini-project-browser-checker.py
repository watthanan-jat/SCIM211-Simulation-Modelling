"""Browser-side readiness checks for the SCIM211 café simulation contract."""

from __future__ import annotations

import copy
import json
import math
import traceback
from collections.abc import Mapping
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

REQUIRED_RESULT_FIELDS = (
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

COUNT_FIELDS = (
    "n_arrivals",
    "n_served",
    "n_lost",
    "n_served_simple",
    "n_served_complex",
)

NONNEGATIVE_FIELDS = (
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
    """A student-facing readiness failure."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def as_number(value: Any, field: str) -> float:
    require(not isinstance(value, bool), f"{field} must be numeric, not Boolean")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise CheckFailure(f"{field} must be numeric") from exc
    require(math.isfinite(number), f"{field} must be finite")
    return number


def close(actual: Any, expected: Any, tolerance: float = 1e-7) -> bool:
    return math.isclose(
        as_number(actual, "actual value"),
        as_number(expected, "expected value"),
        rel_tol=tolerance,
        abs_tol=tolerance,
    )


def validate_result(result: Any, config: Mapping[str, Any], label: str) -> dict[str, Any]:
    require(isinstance(result, dict), f"{label}: simulate_cafe must return a dictionary")
    missing = [field for field in REQUIRED_RESULT_FIELDS if field not in result]
    require(not missing, f"{label}: missing fields: {', '.join(missing)}")

    numbers = {field: as_number(result[field], field) for field in REQUIRED_RESULT_FIELDS}
    for field in NONNEGATIVE_FIELDS:
        require(numbers[field] >= 0.0, f"{label}: {field} cannot be negative")
    for field in COUNT_FIELDS:
        require(numbers[field].is_integer(), f"{label}: {field} must be a whole number")

    require(close(numbers["run_minutes"], config["run_minutes"]), f"{label}: run_minutes must copy config")
    require(numbers["finish_time"] + 1e-7 >= numbers["run_minutes"], f"{label}: finish_time is before closing")
    require(numbers["utilisation"] <= 1.0 + 1e-7, f"{label}: utilisation must be between 0 and 1")
    require(
        close(numbers["n_arrivals"], numbers["n_served"] + numbers["n_lost"]),
        f"{label}: n_arrivals must equal n_served + n_lost",
    )
    require(
        close(numbers["n_served"], numbers["n_served_simple"] + numbers["n_served_complex"]),
        f"{label}: n_served must equal simple + complex served",
    )
    require(numbers["mean_wait"] <= numbers["max_wait"] + 1e-7, f"{label}: mean_wait exceeds max_wait")
    require(numbers["p90_wait"] <= numbers["max_wait"] + 1e-7, f"{label}: p90_wait exceeds max_wait")

    expected_throughput = numbers["n_served"] / (float(config["run_minutes"]) / 60.0)
    require(close(numbers["throughput_per_hour"], expected_throughput), f"{label}: throughput is inconsistent")

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
    require(close(numbers["total_cost"], expected_cost), f"{label}: total_cost is inconsistent")
    require(close(numbers["profit"], numbers["revenue"] - numbers["total_cost"]), f"{label}: profit must equal revenue - total_cost")

    if numbers["n_served"] == 0:
        for field in ("mean_wait", "p90_wait", "max_wait"):
            require(close(numbers[field], 0.0), f"{label}: {field} must be 0 when nobody is served")

    return result


def projection(result: Mapping[str, Any]) -> tuple[float, ...]:
    return tuple(as_number(result[field], field) for field in REQUIRED_RESULT_FIELDS)


def perform_checks(student_source: str) -> list[str]:
    lines = ["SCIM211 Coffee Shop Simulation readiness check", ""]
    namespace: dict[str, Any] = {"__name__": "student_submission"}
    compiled = compile(student_source, "cafe_model.py", "exec")
    exec(compiled, namespace)
    lines.append("✓ The Python file executes without an import or syntax error.")

    simulate = namespace.get("simulate_cafe")
    replicate = namespace.get("run_replications")
    require(callable(simulate), "missing callable simulate_cafe(config, seed)")
    require(callable(replicate), "missing callable run_replications(config, seeds)")
    lines.append("✓ Both required functions exist.")

    config = copy.deepcopy(STANDARD_CONFIG)
    untouched = copy.deepcopy(config)
    first = validate_result(simulate(config, 211), config, "standard run")
    require(config == untouched, "simulate_cafe modified the supplied config dictionary")
    lines.append("✓ The official configuration runs and returns every required result.")
    lines.append("✓ Counts, waiting measures, throughput, and finances are internally consistent.")
    lines.append("✓ simulate_cafe leaves the supplied configuration unchanged.")

    repeated = validate_result(simulate(copy.deepcopy(config), 211), config, "repeated-seed run")
    require(projection(first) == projection(repeated), "the same configuration and seed did not reproduce the same result")
    different = validate_result(simulate(copy.deepcopy(config), 212), config, "different-seed run")
    stochastic_fields = ("n_arrivals", "n_served_simple", "mean_wait", "p90_wait", "max_wait")
    require(
        any(not close(first[field], different[field]) for field in stochastic_fields),
        "different seeds produced identical stochastic outputs; check that seed is used",
    )
    lines.append("✓ Seeds reproduce a run and different seeds produce stochastic variation.")

    zero_config = copy.deepcopy(STANDARD_CONFIG)
    zero_config["arrival_rate_per_hour"] = 0.0
    zero = validate_result(simulate(zero_config, 301), zero_config, "zero-arrival run")
    for field in (*COUNT_FIELDS, "mean_wait", "p90_wait", "max_wait", "throughput_per_hour", "revenue"):
        require(close(zero[field], 0.0), f"zero-arrival run: {field} must be 0")
    lines.append("✓ Zero demand produces zero arrivals and zero service outputs.")

    simple_config = copy.deepcopy(STANDARD_CONFIG)
    simple_config.update({
        "run_minutes": 60.0,
        "simple_order_probability": 1.0,
        "price_simple": 91.0,
        "cost_simple": 17.0,
        "max_queue": None,
    })
    simple = validate_result(simulate(simple_config, 401), simple_config, "simple-only run")
    require(close(simple["n_served_complex"], 0), "simple_order_probability=1 still produced complex orders")

    complex_config = copy.deepcopy(STANDARD_CONFIG)
    complex_config.update({
        "run_minutes": 60.0,
        "simple_order_probability": 0.0,
        "price_complex": 137.0,
        "cost_complex": 43.0,
        "max_queue": None,
    })
    complex_result = validate_result(simulate(complex_config, 402), complex_config, "complex-only run")
    require(close(complex_result["n_served_simple"], 0), "simple_order_probability=0 still produced simple orders")
    lines.append("✓ Order probabilities, prices, costs, and run length come from config.")

    unlimited_config = copy.deepcopy(STANDARD_CONFIG)
    unlimited_config.update({
        "arrival_rate_per_hour": 72.0,
        "n_baristas": 1,
        "mean_service_simple": 5.0,
        "mean_service_complex": 7.0,
        "max_queue": None,
    })
    capped_config = copy.deepcopy(unlimited_config)
    capped_config["max_queue"] = 0
    unlimited = validate_result(simulate(unlimited_config, 503), unlimited_config, "unlimited-queue run")
    capped = validate_result(simulate(capped_config, 503), capped_config, "zero-queue run")
    require(close(unlimited["n_lost"], 0), "max_queue=None must not refuse customers because of queue length")
    require(float(capped["n_lost"]) > 0, "max_queue=0 did not refuse any customers in the stress run")
    lines.append("✓ max_queue=None and max_queue=0 produce the required admission behaviour.")

    heavy_one = copy.deepcopy(STANDARD_CONFIG)
    heavy_one.update({"arrival_rate_per_hour": 54.0, "n_baristas": 1, "max_queue": None})
    heavy_three = copy.deepcopy(heavy_one)
    heavy_three["n_baristas"] = 3
    one_barista = validate_result(simulate(heavy_one, 907), heavy_one, "one-barista stress run")
    three_baristas = validate_result(simulate(heavy_three, 907), heavy_three, "three-barista stress run")
    require(
        float(three_baristas["mean_wait"]) <= float(one_barista["mean_wait"]) + 1e-7,
        "three baristas increased mean waiting in the stress run",
    )
    lines.append("✓ Increasing baristas does not increase mean waiting in the stress run.")

    seeds = [11, 22, 33, 44]
    replication_config = copy.deepcopy(STANDARD_CONFIG)
    frame = replicate(replication_config, seeds)
    require(replication_config == STANDARD_CONFIG, "run_replications modified the supplied config dictionary")
    require(isinstance(frame, pd.DataFrame), "run_replications must return a pandas DataFrame")
    require(len(frame) == len(seeds), "run_replications must return exactly one row per seed")
    required_columns = ("seed", *REQUIRED_RESULT_FIELDS)
    missing_columns = [field for field in required_columns if field not in frame.columns]
    require(not missing_columns, f"replication DataFrame is missing: {', '.join(missing_columns)}")
    require(frame["seed"].tolist() == seeds, "replication rows must preserve the supplied seed order")

    for index, seed in enumerate(seeds):
        row = {field: frame.iloc[index][field] for field in REQUIRED_RESULT_FIELDS}
        validate_result(row, STANDARD_CONFIG, f"replication row for seed {seed}")

    direct = validate_result(simulate(copy.deepcopy(STANDARD_CONFIG), seeds[0]), STANDARD_CONFIG, "direct replication check")
    require(
        all(close(frame.iloc[0][field], direct[field]) for field in REQUIRED_RESULT_FIELDS),
        "the first replication row does not match simulate_cafe for the same seed",
    )
    lines.append("✓ run_replications returns one valid and reproducible row per seed.")
    lines.extend(["", "PASS: cafe_model.py", "Your file meets the automated readiness contract."])
    return lines


def check_source(student_source: str) -> dict[str, Any]:
    try:
        lines = perform_checks(student_source)
    except CheckFailure as exc:
        return {
            "passed": False,
            "lines": [
                "SCIM211 Coffee Shop Simulation readiness check",
                "",
                "FAIL: cafe_model.py",
                str(exc),
                "",
                "Fix this failure and run the checker again.",
            ],
        }
    except Exception as exc:
        detail = "".join(traceback.format_exception_only(type(exc), exc)).strip()
        return {
            "passed": False,
            "lines": [
                "SCIM211 Coffee Shop Simulation readiness check",
                "",
                "FAIL: cafe_model.py",
                detail,
                "",
                "The file raised an error while loading or running. Fix it and test again.",
            ],
        }
    return {"passed": True, "lines": lines}


def check_source_json(student_source: str) -> str:
    return json.dumps(check_source(student_source), ensure_ascii=False)
