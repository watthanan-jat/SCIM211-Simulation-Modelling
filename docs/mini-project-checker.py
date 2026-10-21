#!/usr/bin/env python3
"""Readiness checker for the SCIM211 Coffee Shop Simulation Hackathon.

Usage (from the repository root):
    python mini_project/check_cafe_submission.py GROUP_01/cafe_model.py
    python mini_project/check_cafe_submission.py submissions/*/cafe_model.py

The same file powers the browser checker on the course website.

The checker has two parts.

1. Contract checks: the file loads, both functions exist, every required
   result is present and internally consistent, seeds reproduce runs, the
   configuration is not modified, and simple edge cases behave correctly.
2. Statistical checks: the model is run for 100 seeds in each of several
   different configurations. For each output, the mean over those seeds is
   compared with the mean from the reference model (5,000 seeds)
   using
       z = (student mean - reference mean) / (reference SD * sqrt(1/100 + 1/5000)).
   A correct model following the handout's rules has |z| > 5 with negligible
   probability, so |z| > 5 is reported as a failure. Your numbers will not
   equal the reference numbers exactly, and they do not need to.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import subprocess
import sys
import time
import traceback
import types
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

import pandas as pd


STANDARD_CONFIG: dict[str, Any] = {
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

REQUIRED_RESULT_FIELDS: tuple[str, ...] = (
    "run_minutes",
    "finish_time",
    "n_arrivals",
    "n_served",
    "n_lost",
    "n_balked",
    "n_reneged",
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
    "n_balked",
    "n_reneged",
    "n_served_simple",
    "n_served_complex",
)

NONNEGATIVE_FIELDS: tuple[str, ...] = tuple(
    field for field in REQUIRED_RESULT_FIELDS if field != "profit"
)

# ---------------------------------------------------------------------------
# Statistical scenarios. Each changes several inputs so that a model which
# ignores or misuses an input produces a clearly different average output.
# ---------------------------------------------------------------------------

STAT_SEEDS: tuple[int, ...] = tuple(range(20_260_000, 20_260_100))
Z_LIMIT = 5.0
RARE_COUNT = 1.0  # count outputs averaging below this are not compared
SD_RATIO_RANGE = (0.6, 1.5)  # allowed spread of n_arrivals relative to the reference

STAT_METRICS: tuple[str, ...] = (
    "n_arrivals",
    "n_served",
    "n_balked",
    "n_reneged",
    "n_served_simple",
    "mean_wait",
    "p90_wait",
    "max_wait",
    "utilisation",
    "finish_time",
    "profit",
)

SCENARIOS: tuple[dict[str, Any], ...] = (
    {
        "name": "baseline",
        "tests": "the standard café",
        "overrides": {},
    },
    {
        "name": "single barista, patient customers",
        "tests": "the basic FCFS queue with one barista, no reneging, and no queue limit",
        "overrides": {
            "arrival_rate_per_hour": 15.0,
            "n_baristas": 1,
            "mean_patience": None,
            "max_queue": None,
        },
    },
    {
        "name": "busy café with a short queue limit",
        "tests": "balking when all baristas are busy and max_queue customers are waiting",
        "overrides": {
            "arrival_rate_per_hour": 60.0,
            "n_baristas": 2,
            "mean_patience": None,
            "max_queue": 3,
        },
    },
    {
        "name": "impatient customers",
        "tests": "reneging: patience applies only while waiting and uses the prescribed distribution",
        "overrides": {
            "arrival_rate_per_hour": 36.0,
            "n_baristas": 1,
            "mean_patience": 4.0,
            "max_queue": None,
        },
    },
    {
        "name": "three baristas, different menu and prices",
        "tests": "use of every configuration value together",
        "overrides": {
            "arrival_rate_per_hour": 70.0,
            "n_baristas": 3,
            "simple_order_probability": 0.2,
            "mean_service_simple": 1.5,
            "mean_service_complex": 5.0,
            "mean_patience": 12.0,
            "price_simple": 70.0,
            "price_complex": 140.0,
            "cost_simple": 20.0,
            "cost_complex": 55.0,
            "barista_cost_per_hour": 150.0,
            "max_queue": 6,
        },
    },
    {
        "name": "long quiet day",
        "tests": "run length, a high simple-order share, and closing-time logic",
        "overrides": {
            "run_minutes": 240.0,
            "arrival_rate_per_hour": 20.0,
            "simple_order_probability": 0.7,
            "mean_patience": 15.0,
        },
    },
)

# BEGIN REFERENCE (generated by labSoln/mini_project/build_checker_reference.py; do not edit)
REFERENCE: dict[str, Any] = {'replications': 5000,
 'seed_start': 900000000,
 'scenarios': {'baseline': {'n_arrivals': [60.1294, 7.686252, 5000],
                            'n_served': [56.8814, 6.76935, 5000],
                            'n_balked': [0.2486, 0.830263, 5000],
                            'n_reneged': [2.9994, 3.232258, 5000],
                            'n_served_simple': [25.6108, 4.986572, 5000],
                            'mean_wait': [1.85153, 0.919902, 5000],
                            'p90_wait': [5.191619, 1.97859, 5000],
                            'max_wait': [8.486079, 2.511915, 5000],
                            'utilisation': [0.700803, 0.101977, 5000],
                            'finish_time': [125.342361, 5.088887, 5000],
                            'profit': [3558.296, 481.013941, 5000]},
               'single barista, patient customers': {'n_arrivals': [30.1646, 5.437961, 5000],
                                                     'n_served': [30.1646, 5.437961, 5000],
                                                     'n_balked': [0.0, 0.0, 5000],
                                                     'n_reneged': [0.0, 0.0, 5000],
                                                     'n_served_simple': [13.604, 3.59168, 5000],
                                                     'mean_wait': [6.738501, 6.20647, 5000],
                                                     'p90_wait': [15.093624, 10.92714, 5000],
                                                     'max_wait': [19.659898, 11.850832, 5000],
                                                     'utilisation': [0.712002, 0.149732, 5000],
                                                     'finish_time': [129.684096, 12.051187, 5000],
                                                     'profit': [1901.088, 390.876673, 5000]},
               'busy café with a short queue limit': {'n_arrivals': [120.1596, 10.977023, 5000],
                                                      'n_served': [75.3816, 7.782628, 5000],
                                                      'n_balked': [44.778, 12.207134, 5000],
                                                      'n_reneged': [0.0, 0.0, 5000],
                                                      'n_served_simple': [34.0278, 6.18164, 5000],
                                                      'mean_wait': [2.896365, 0.650742, 5000],
                                                      'p90_wait': [6.705422, 1.424179, 5000],
                                                      'max_wait': [11.756378, 3.040577, 5000],
                                                      'utilisation': [0.912275, 0.041446, 5000],
                                                      'finish_time': [127.756513, 5.351772, 5000],
                                                      'profit': [4869.972, 537.294087, 5000]},
               'impatient customers': {'n_arrivals': [72.1438, 8.50983, 5000],
                                       'n_served': [35.8692, 5.722084, 5000],
                                       'n_balked': [0.0, 0.0, 5000],
                                       'n_reneged': [36.2746, 9.123741, 5000],
                                       'n_served_simple': [16.1854, 4.403829, 5000],
                                       'mean_wait': [1.860346, 0.378277, 5000],
                                       'p90_wait': [3.942233, 0.500457, 5000],
                                       'max_wait': [5.06041, 0.487856, 5000],
                                       'utilisation': [0.888024, 0.056412, 5000],
                                       'finish_time': [124.873538, 4.132862, 5000],
                                       'profit': [2305.828, 395.353937, 5000]},
               'three baristas, different menu and prices': {'n_arrivals': [140.2198, 11.886082, 5000],
                                                             'n_served': [87.798, 9.377461, 5000],
                                                             'n_balked': [43.0288, 12.197038, 5000],
                                                             'n_reneged': [9.393, 3.681747, 5000],
                                                             'n_served_simple': [17.5862, 4.607648, 5000],
                                                             'mean_wait': [4.834153, 0.792547, 5000],
                                                             'p90_wait': [8.859956, 1.070174, 5000],
                                                             'max_wait': [12.628029, 1.690658, 5000],
                                                             'utilisation': [0.93804, 0.03137, 5000],
                                                             'finish_time': [134.114854, 6.664023, 5000],
                                                             'profit': [5947.313, 706.163946, 5000]},
               'long quiet day': {'n_arrivals': [80.1394, 8.99365, 5000],
                                  'n_served': [79.964, 8.903177, 5000],
                                  'n_balked': [0.0142, 0.182222, 5000],
                                  'n_reneged': [0.1612, 0.601737, 5000],
                                  'n_served_simple': [55.971, 7.39537, 5000],
                                  'mean_wait': [0.575833, 0.422925, 5000],
                                  'p90_wait': [2.09363, 1.674672, 5000],
                                  'max_wait': [6.095329, 2.923102, 5000],
                                  'utilisation': [0.427861, 0.070567, 5000],
                                  'finish_time': [242.533317, 3.745733, 5000],
                                  'profit': [4317.7, 595.066795, 5000]}}}
# END REFERENCE


class CheckFailure(Exception):
    """Raised when a readiness check fails."""


def require(condition: bool, message: str) -> None:
    """Raise a readable check failure when condition is false."""
    if not condition:
        raise CheckFailure(message)


def as_finite_number(value: Any, field: str) -> float:
    """Return value as float after rejecting Booleans, None, and non-finite values."""
    require(not isinstance(value, bool), f"{field} must be numeric, not Boolean")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise CheckFailure(f"{field} must be numeric, got {value!r}") from exc
    require(math.isfinite(number), f"{field} must be finite, got {number}")
    return number


def close(actual: Any, expected: Any, *, tolerance: float = 1e-7) -> bool:
    """Compare two numeric values using a small scale-aware tolerance."""
    return math.isclose(
        as_finite_number(actual, "actual value"),
        as_finite_number(expected, "expected value"),
        rel_tol=tolerance,
        abs_tol=tolerance,
    )


def config_with(**overrides: Any) -> dict[str, Any]:
    """Return a fresh copy of the standard configuration with overrides."""
    config = copy.deepcopy(STANDARD_CONFIG)
    config.update(overrides)
    return config


# ---------------------------------------------------------------------------
# Loading student code
# ---------------------------------------------------------------------------


def load_module_from_source(source: str, filename: str = "cafe_model.py") -> types.ModuleType:
    """Execute student source as a registered module.

    Registering the module in ``sys.modules`` lets dataclasses and similar
    tools that look up their defining module work normally.
    """
    module_name = "scim211_student_cafe_model"
    module = types.ModuleType(module_name)
    module.__file__ = filename
    sys.modules[module_name] = module
    try:
        exec(compile(source, filename, "exec"), module.__dict__)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module


# ---------------------------------------------------------------------------
# Contract checks
# ---------------------------------------------------------------------------


def validate_result(result: Any, config: Mapping[str, Any], label: str) -> dict[str, float]:
    """Validate one result dictionary and its required accounting identities."""
    require(isinstance(result, Mapping), f"{label}: simulate_cafe must return a dictionary")
    missing = [field for field in REQUIRED_RESULT_FIELDS if field not in result]
    require(not missing, f"{label}: missing result fields: {', '.join(missing)}")

    n = {field: as_finite_number(result[field], f"{label}: {field}") for field in REQUIRED_RESULT_FIELDS}

    for field in NONNEGATIVE_FIELDS:
        require(n[field] >= 0.0, f"{label}: {field} cannot be negative")
    for field in COUNT_FIELDS:
        require(n[field].is_integer(), f"{label}: {field} must be a whole number")

    run_minutes = float(config["run_minutes"])
    require(close(n["run_minutes"], run_minutes), f"{label}: run_minutes must copy config")
    require(n["finish_time"] + 1e-7 >= run_minutes, f"{label}: finish_time cannot be earlier than closing time")
    require(n["utilisation"] <= 1.0 + 1e-7, f"{label}: utilisation cannot exceed 1")

    require(close(n["n_lost"], n["n_balked"] + n["n_reneged"]), f"{label}: n_lost must equal n_balked + n_reneged")
    require(close(n["n_arrivals"], n["n_served"] + n["n_lost"]), f"{label}: n_arrivals must equal n_served + n_lost")
    require(
        close(n["n_served"], n["n_served_simple"] + n["n_served_complex"]),
        f"{label}: n_served must equal n_served_simple + n_served_complex",
    )
    require(n["mean_wait"] <= n["max_wait"] + 1e-7, f"{label}: mean_wait cannot exceed max_wait")
    require(n["p90_wait"] <= n["max_wait"] + 1e-7, f"{label}: p90_wait cannot exceed max_wait")

    if config["max_queue"] is None:
        require(close(n["n_balked"], 0), f"{label}: n_balked must be 0 when max_queue is None")
    if config["mean_patience"] is None:
        require(close(n["n_reneged"], 0), f"{label}: n_reneged must be 0 when mean_patience is None")
    else:
        require(
            n["max_wait"] <= 1.5 * float(config["mean_patience"]) + 1e-7,
            f"{label}: a served customer waited longer than the largest possible patience "
            f"(1.5 * mean_patience); check the reneging rule",
        )

    require(
        close(n["throughput_per_hour"], n["n_served"] / (run_minutes / 60.0)),
        f"{label}: throughput_per_hour must equal n_served / (run_minutes / 60)",
    )
    expected_revenue = n["n_served_simple"] * float(config["price_simple"]) + n["n_served_complex"] * float(
        config["price_complex"]
    )
    require(close(n["revenue"], expected_revenue), f"{label}: revenue must come from completed orders only")
    expected_cost = (
        n["n_served_simple"] * float(config["cost_simple"])
        + n["n_served_complex"] * float(config["cost_complex"])
        + float(config["n_baristas"]) * float(config["barista_cost_per_hour"]) * run_minutes / 60.0
    )
    require(
        close(n["total_cost"], expected_cost),
        f"{label}: total_cost must equal ingredient cost of completed orders plus "
        f"n_baristas * barista_cost_per_hour * run_minutes / 60",
    )
    require(close(n["profit"], n["revenue"] - n["total_cost"]), f"{label}: profit must equal revenue - total_cost")

    if n["n_served"] == 0:
        for field in ("mean_wait", "p90_wait", "max_wait"):
            require(close(n[field], 0.0), f"{label}: {field} must be 0 when nobody is served")
    return n


def projection(result: Mapping[str, Any]) -> tuple[float, ...]:
    """Return only the required fields so reproducibility checks ignore extras."""
    return tuple(as_finite_number(result[field], field) for field in REQUIRED_RESULT_FIELDS)


def run_contract_checks(module: types.ModuleType, report: Callable[[str], None]) -> Callable:
    """Run interface and consistency checks; return simulate_cafe."""
    simulate = getattr(module, "simulate_cafe", None)
    replicate = getattr(module, "run_replications", None)
    require(callable(simulate), "missing callable simulate_cafe(config, seed)")
    require(callable(replicate), "missing callable run_replications(config, seeds)")
    report("Both required functions exist.")

    config = config_with()
    untouched = copy.deepcopy(config)
    first = simulate(config, 211)
    require(config == untouched, "simulate_cafe modified the supplied configuration dictionary")
    validate_result(first, config, "standard run")
    report("The standard configuration runs, all required results are present, and the accounting balances.")

    repeated = simulate(config_with(), 211)
    require(projection(first) == projection(repeated), "the same configuration and seed did not reproduce the same result")
    different = simulate(config_with(), 212)
    require(
        projection(first) != projection(different),
        "different seeds produced identical results; check that seed is used to create the random generator",
    )
    report("The same seed reproduces a run and a different seed changes it.")

    zero_config = config_with(arrival_rate_per_hour=0.0)
    zero = validate_result(simulate(zero_config, 301), zero_config, "zero-arrival run")
    for field in COUNT_FIELDS + ("mean_wait", "p90_wait", "max_wait", "throughput_per_hour", "revenue", "utilisation"):
        require(close(zero[field], 0.0), f"zero-arrival run: {field} must be 0")
    require(close(zero["finish_time"], zero_config["run_minutes"]), "zero-arrival run: finish_time must equal run_minutes")
    report("Zero demand gives zero customers, zero service, and finish_time = run_minutes.")

    simple_config = config_with(simple_order_probability=1.0, max_queue=None, mean_patience=None)
    simple = validate_result(simulate(simple_config, 401), simple_config, "simple-only run")
    require(close(simple["n_served_complex"], 0), "simple_order_probability = 1 still produced complex orders")
    complex_config = config_with(simple_order_probability=0.0, max_queue=None, mean_patience=None)
    complex_result = validate_result(simulate(complex_config, 402), complex_config, "complex-only run")
    require(close(complex_result["n_served_simple"], 0), "simple_order_probability = 0 still produced simple orders")
    report("Order probabilities of 0 and 1 behave correctly; None disables queue limits and reneging.")

    capped_config = config_with(arrival_rate_per_hour=90.0, n_baristas=1, max_queue=0, mean_patience=None)
    capped = validate_result(simulate(capped_config, 503), capped_config, "zero-queue run")
    require(capped["n_balked"] > 0, "max_queue = 0 did not turn away any customers in a very busy café")
    require(close(capped["mean_wait"], 0.0), "max_queue = 0 means nobody can wait, so mean_wait must be 0")
    report("max_queue = 0 turns customers away and nobody waits.")

    seeds = [11, 22, 33, 44]
    replication_config = config_with()
    frame = replicate(replication_config, seeds)
    require(replication_config == STANDARD_CONFIG, "run_replications modified the supplied configuration dictionary")
    require(isinstance(frame, pd.DataFrame), "run_replications must return a pandas DataFrame")
    require(len(frame) == len(seeds), "run_replications must return exactly one row per seed")
    missing_columns = [column for column in ("seed", *REQUIRED_RESULT_FIELDS) if column not in frame.columns]
    require(not missing_columns, f"replication DataFrame is missing columns: {', '.join(missing_columns)}")
    require([int(seed) for seed in frame["seed"].tolist()] == seeds, "replication rows must keep the supplied seed order")
    for index, seed in enumerate(seeds):
        row = {field: frame.iloc[index][field] for field in REQUIRED_RESULT_FIELDS}
        validate_result(row, STANDARD_CONFIG, f"replication row for seed {seed}")
        direct = simulate(config_with(), seed)
        require(
            all(close(row[field], direct[field]) for field in REQUIRED_RESULT_FIELDS),
            f"replication row for seed {seed} does not match simulate_cafe(config, {seed})",
        )
    report("run_replications returns one correct row per seed, in order.")
    return simulate


# ---------------------------------------------------------------------------
# Statistical checks
# ---------------------------------------------------------------------------


def summarise(rows: Sequence[Mapping[str, float]], metrics: Sequence[str]) -> dict[str, list[float]]:
    """Return [mean, sample standard deviation, count] for each metric."""
    summary = {}
    for metric in metrics:
        values = [float(row[metric]) for row in rows]
        count = len(values)
        mean = sum(values) / count
        variance = sum((value - mean) ** 2 for value in values) / (count - 1) if count > 1 else 0.0
        summary[metric] = [mean, math.sqrt(variance), count]
    return summary


def compare_to_reference(name: str, student: Mapping[str, list[float]]) -> tuple[float, list[str]]:
    """Return the largest |z| and a list of failing metric descriptions."""
    reference = REFERENCE["scenarios"][name]
    worst = 0.0
    problems = []
    for metric in STAT_METRICS:
        s_mean, s_sd, s_n = student[metric]
        r_mean, r_sd, r_n = reference[metric]
        if metric in COUNT_FIELDS and 0.0 < r_mean < RARE_COUNT:
            # Rare events (for example balking in a quiet café) are too skewed
            # for a normal approximation with 100 runs; other scenarios test them.
            continue
        # Under the hypothesis that the model is correct, both samples share the
        # reference variance. Using it (rather than the student's sample
        # variance) keeps rare outcomes, such as balking in a quiet café, from
        # producing a spuriously tiny standard error.
        standard_error = r_sd * math.sqrt(1.0 / s_n + 1.0 / r_n)
        if standard_error < 1e-12:
            z = 0.0 if math.isclose(s_mean, r_mean, rel_tol=1e-9, abs_tol=1e-9) else math.inf
        else:
            z = (s_mean - r_mean) / standard_error
        worst = max(worst, abs(z))
        if abs(z) > Z_LIMIT:
            problems.append(
                f"{metric}: your mean {s_mean:.3f}, reference {r_mean:.3f} "
                f"(z = {z:+.1f})"
            )
    # The number of arrivals in a Poisson process has variance equal to its
    # mean, so the spread of n_arrivals is checked as well as its average. This
    # catches, for example, a fixed number of customers per run.
    s_sd, r_sd = student["n_arrivals"][1], reference["n_arrivals"][1]
    if r_sd > 0 and not SD_RATIO_RANGE[0] <= s_sd / r_sd <= SD_RATIO_RANGE[1]:
        problems.append(
            f"n_arrivals: standard deviation across seeds is {s_sd:.2f}, but a Poisson arrival "
            f"process gives about {r_sd:.2f}"
        )
    return worst, problems


def run_statistical_checks(simulate: Callable, report: Callable[[str], None]) -> None:
    """Compare average outputs with the reference model in every scenario."""
    require(bool(REFERENCE), "checker reference statistics are missing; please report this on Google Classroom")
    for scenario in SCENARIOS:
        config = config_with(**scenario["overrides"])
        rows = []
        for seed in STAT_SEEDS:
            rows.append(validate_result(simulate(copy.deepcopy(config), seed), config, f"{scenario['name']} (seed {seed})"))
        worst, problems = compare_to_reference(scenario["name"], summarise(rows, STAT_METRICS))
        settings = ", ".join(f"{key}={value}" for key, value in scenario["overrides"].items()) or "standard configuration"
        require(
            not problems,
            f"statistical check '{scenario['name']}' ({settings}) disagrees with the reference model.\n"
            f"  This scenario tests {scenario['tests']}.\n  " + "\n  ".join(problems),
        )
        report(f"Scenario '{scenario['name']}': {len(STAT_METRICS)} averages agree with the reference (largest |z| = {worst:.1f}).")


# ---------------------------------------------------------------------------
# Running one submission
# ---------------------------------------------------------------------------


def check_source(source: str, filename: str = "cafe_model.py", *, progress: Callable[[str], None] | None = None) -> dict[str, Any]:
    """Run every check on student source and return a JSON-serialisable report."""
    lines: list[str] = []

    def report(message: str) -> None:
        lines.append(f"✓ {message}")
        if progress is not None:
            progress(message)

    started = time.perf_counter()
    try:
        module = load_module_from_source(source, filename)
        report("The file loads without an import or syntax error.")
        simulate = run_contract_checks(module, report)
        run_statistical_checks(simulate, report)
    except CheckFailure as exc:
        return {"passed": False, "lines": lines, "failure": str(exc)}
    except Exception as exc:  # Student code raised an error.
        detail = "".join(traceback.format_exception_only(type(exc), exc)).strip()
        return {"passed": False, "lines": lines, "failure": f"your code raised an error: {detail}"}
    finally:
        sys.modules.pop("scim211_student_cafe_model", None)
    lines.append(f"(checks took {time.perf_counter() - started:.0f} s)")
    return {"passed": True, "lines": lines, "failure": None}


def check_source_json(source: str, progress: Callable[[str], None] | None = None) -> str:
    """Browser entry point. ``progress`` receives each passed check as it happens."""
    return json.dumps(check_source(source, progress=progress), ensure_ascii=False)


def check_path_in_subprocess(path: Path, timeout: float) -> dict[str, Any]:
    """Check one file in a fresh Python process so a hang or crash is contained."""
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", str(path)]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {
            "passed": False,
            "lines": [],
            "failure": f"the checks did not finish within {timeout:.0f} s; look for an infinite loop "
            f"(for example a zero time step when the arrival rate is 0)",
        }
    output = completed.stdout.strip().splitlines()
    if completed.returncode != 0 or not output:
        tail = (completed.stderr or completed.stdout).strip().splitlines()[-3:]
        return {"passed": False, "lines": [], "failure": "the checker process stopped: " + " | ".join(tail)}
    return json.loads(output[-1])


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check SCIM211 café model submissions.")
    parser.add_argument("submissions", nargs="+", type=Path, help="one or more cafe_model.py files")
    parser.add_argument("--timeout", type=float, default=600.0, help="seconds allowed per submission (default 600)")
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if args.worker:  # Internal: run in the child process and print one JSON line.
        path = args.submissions[0]
        sys.path.insert(0, str(path.resolve().parent))
        result = check_source(path.read_text(encoding="utf-8"), str(path))
        sys.stdout.flush()
        print("\n" + json.dumps(result, ensure_ascii=False))
        return 0

    failures = 0
    for path in args.submissions:
        if not path.is_file() or path.suffix != ".py":
            result = {"passed": False, "lines": [], "failure": f"not a .py file: {path}"}
        else:
            result = check_path_in_subprocess(path, args.timeout)
        for line in result["lines"]:
            print(f"  {line}")
        if result["passed"]:
            print(f"PASS: {path}")
        else:
            failures += 1
            print(f"FAIL: {path}")
            print(f"  {result['failure']}")
        if len(args.submissions) > 1:
            print()

    if len(args.submissions) > 1:
        print(f"SUMMARY: {len(args.submissions) - failures} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__" and sys.platform != "emscripten":
    raise SystemExit(main())
