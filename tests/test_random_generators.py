"""Placeholder tests for random generator utilities."""

import pytest

from src.random_generators import linear_congruential_generator


@pytest.mark.xfail(reason="linear_congruential_generator is currently a TODO stub")
def test_lcg_returns_correct_length():
    """LCG should return the requested number of uniform values."""
    values = linear_congruential_generator(a=5, c=1, m=16, seed=3, n=10)

    assert len(values) == 10
