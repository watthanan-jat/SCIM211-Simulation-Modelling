"""Random number generator utilities for SCIM211 lab work."""


def linear_congruential_generator(a, c, m, seed, n):
    """Generate pseudo-random numbers using a linear congruential generator.

    Parameters
    ----------
    a : int
        Multiplier.
    c : int
        Increment.
    m : int
        Modulus.
    seed : int
        Initial value.
    n : int
        Number of values to generate.

    Returns
    -------
    list[float]
        Uniform values between 0 and 1.
    """
    # TODO: Implement the LCG recurrence and return uniform values.
    raise NotImplementedError


def estimate_period(a, c, m, seed, max_steps=None):
    """Estimate the period of an LCG sequence from a starting seed."""
    # TODO: Track generated states until a repeated state is found.
    raise NotImplementedError


def lag_pairs(values):
    """Create pairs (U_i, U_{i+1}) for scatter-plot diagnostics."""
    # TODO: Return adjacent value pairs for plotting.
    raise NotImplementedError
