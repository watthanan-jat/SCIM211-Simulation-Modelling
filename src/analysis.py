"""Input and output analysis helpers for SCIM211 simulations."""


def load_service_times(path):
    """Load service-time observations from a CSV file."""
    # TODO: Read a CSV file and return service-time data.
    raise NotImplementedError


def fit_exponential_rate(service_times):
    """Estimate an exponential rate parameter from service-time data."""
    # TODO: Estimate rate as the reciprocal of the sample mean.
    raise NotImplementedError


def confidence_interval_mean(values, confidence=0.95):
    """Calculate a confidence interval for a sample mean."""
    # TODO: Compute sample mean, standard error, and confidence interval.
    raise NotImplementedError


def summarise_replications(replication_results):
    """Summarise output measures across simulation replications."""
    # TODO: Aggregate replication outputs into report-ready measures.
    raise NotImplementedError
