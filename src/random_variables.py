"""Random variable simulation helpers for SCIM211."""


def exponential_from_uniform(uniform_values, rate):
    """Transform uniform random numbers into exponential random variables.

    Parameters
    ----------
    uniform_values : sequence of float
        Uniform values in the interval (0, 1).
    rate : float
        Exponential rate parameter.

    Returns
    -------
    list[float]
        Exponential random variates.
    """
    # TODO: Apply inverse transform sampling for exponential variables.
    raise NotImplementedError


def simulate_drink_orders(drinks, probabilities, n_customers, seed=None):
    """Simulate customer drink orders from a categorical distribution."""
    # TODO: Sample drink labels according to the provided probabilities.
    raise NotImplementedError


def simulate_drink_service_times(orders, mean_service_by_drink, seed=None):
    """Generate drink-dependent service times for a sequence of orders."""
    # TODO: Generate service times using the mean for each drink type.
    raise NotImplementedError
