"""Placeholder tests for random variable helpers."""

import pytest

from src.random_variables import exponential_from_uniform


@pytest.mark.xfail(reason="exponential_from_uniform is currently a TODO stub")
def test_exponential_samples_are_positive():
    """Exponential samples generated from valid uniforms should be positive."""
    samples = exponential_from_uniform([0.2, 0.5, 0.8], rate=2.0)

    assert all(sample > 0 for sample in samples)
