"""Markov chain models for customer loyalty examples."""


def validate_transition_matrix(matrix):
    """Check whether a transition matrix has valid probabilities."""
    # TODO: Check shape, non-negative entries, and row sums equal to 1.
    raise NotImplementedError


def simulate_customer_path(states, transition_matrix, initial_state, n_steps, seed=None):
    """Simulate one customer's loyalty-state path over time."""
    # TODO: Move between states using transition probabilities.
    raise NotImplementedError


def simulate_many_customers(states, transition_matrix, initial_distribution, n_customers, n_steps, seed=None):
    """Simulate loyalty states for many customers over multiple steps."""
    # TODO: Simulate many independent customer paths.
    raise NotImplementedError


def transition_matrix_power(transition_matrix, power):
    """Compute a transition matrix power for multi-step behaviour."""
    # TODO: Return the matrix raised to the requested power.
    raise NotImplementedError
