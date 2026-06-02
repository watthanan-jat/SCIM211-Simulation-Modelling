"""Monte Carlo simulation helpers for coffee shop decision analysis."""


def simulate_daily_profit(demand_model, revenue_model, cost_model, seed=None):
    """Simulate profit for one coffee shop day.

    Parameters
    ----------
    demand_model : object
        Placeholder for demand assumptions or a demand-generating function.
    revenue_model : object
        Placeholder for revenue assumptions or a revenue-generating function.
    cost_model : object
        Placeholder for cost assumptions or a cost-generating function.
    seed : int, optional
        Random seed.

    Returns
    -------
    float
        Simulated daily profit.
    """
    # TODO: Combine simulated demand, revenue, and cost into daily profit.
    raise NotImplementedError


def run_profit_replications(n_replications, scenario, seed=None):
    """Run repeated Monte Carlo profit simulations for one scenario."""
    # TODO: Run independent daily profit replications and collect results.
    raise NotImplementedError


def estimate_bad_day_probability(profits, threshold):
    """Estimate the probability that profit is below a bad-day threshold."""
    # TODO: Count the proportion of simulated profits below the threshold.
    raise NotImplementedError
