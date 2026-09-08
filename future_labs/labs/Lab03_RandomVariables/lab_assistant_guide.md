# Lab 3 Worked Solution and Teaching Guide

## Purpose

The instructor demo introduces inverse-transform and accept-reject sampling before the assessed lab begins. The assessed notebook follows this reasoning chain:

```text
transform uniforms -> verify a package method -> sample a custom density
-> build mixed coffee-shop inputs -> investigate a demand change
```

The notebook is both the practical activity and the report. Discussion questions are assessed orally; students should spend their time generating, checking, and interpreting evidence.

All reference results below use NumPy's default generator with seed `211`. Small differences are acceptable if a student uses a different, clearly documented stream-management convention.

## Part A: Inverse-Transform Exponential Times

Starting from `F(x) = 1 - exp(-lambda*x)`, solve `U = F(x)` for `x`:

```text
x = -log(1 - U) / lambda
```

```python
rng = np.random.default_rng(211)
mean_service = 3.0
lambda_rate = 1 / mean_service
u = rng.random(1000)
service_inverse = -np.log1p(-u) / lambda_rate
```

| Count | Mean | Sample SD | Min | Max |
|---:|---:|---:|---:|---:|
| 1000 | 3.0464 | 3.1839 | 0.0065 | 20.0137 |

All values are non-negative. The right-skewed histogram should contain many short services and a small number of long services. A long service can delay every customer behind it.

## Part B: Confirm Against NumPy's Generator

```python
rng = np.random.default_rng(211)
service_numpy = rng.exponential(scale=mean_service, size=1000)
```

The provided check prints means `3.0464` and `2.9718` against the model mean `3.0`, then passes with `rtol=0.15`. Exact equality is inappropriate because these are different random samples. A difference near 50% would suggest a coding or parameterisation error, especially confusing the exponential mean (`scale`) with the rate.

## Part C: Accept-Reject Sampling

```python
rng = np.random.default_rng(211)
accepted = []
proposals = 0

while len(accepted) < 1000:
    x = rng.random()
    u = rng.random()
    proposals += 1
    if u <= x:
        accepted.append(x)

accepted = np.asarray(accepted)
acceptance_rate = len(accepted) / proposals
```

Reference result: 1,000 accepted values from 2,053 proposals, acceptance rate `0.4871`, and sample mean `0.6744`. Theory gives acceptance rate `1/2` and target mean `2/3`.

The histogram rises toward 1. Rejections are part of the algorithm: accepting a uniform proposal `x` with probability `x` produces the normalized density `2x`. Count every proposal, including rejected proposals, when calculating the acceptance rate.

## Part D: Drink Orders and Service Times

```python
drinks = np.array(["Coffee", "Tea", "Chocolate", "Matcha"])
baseline_probabilities = np.array([0.35, 0.20, 0.30, 0.15])
means = {"Coffee": 2.0, "Tea": 1.5, "Chocolate": 4.0, "Matcha": 5.0}

rng = np.random.default_rng(211)
cut_points = np.cumsum(baseline_probabilities)
choice_u = rng.random(1000)
order_index = np.searchsorted(cut_points, choice_u, side="left")
orders = drinks[np.clip(order_index, 0, len(drinks) - 1)]
service_u = rng.random(1000)
scales = np.array([means[drink] for drink in orders])
service = -np.log1p(-service_u) * scales
baseline_data = pd.DataFrame({"Drink": orders, "Service time": service})
```

| Drink | Count | Simulated proportion | Average service time |
|---|---:|---:|---:|
| Coffee | 352 | 0.352 | 1.8916 |
| Tea | 207 | 0.207 | 1.5713 |
| Chocolate | 293 | 0.293 | 3.8763 |
| Matcha | 148 | 0.148 | 5.3778 |

The overall average is `2.9228` minutes and the longest service is `28.6390` minutes. Simulated proportions do not exactly equal model probabilities because the 1,000 orders are a random sample. Drink choice must come first because it selects the service-time distribution used for that customer. The step-shaped discrete CDF has no ordinary inverse; `searchsorted` implements its generalised inverse.

## Part E: Matcha-Trend Reflection

```python
trend_probabilities = np.append(baseline_probabilities[:3] * (0.65 / 0.85), 0.35)
drink_means = np.array([means[drink] for drink in drinks])
baseline_expected_service = baseline_probabilities @ drink_means
trend_expected_service = trend_probabilities @ drink_means
```

| Scenario | Expected service time |
|---|---:|
| Baseline | 2.9500 |
| Matcha trend | 3.4324 |

No new simulation is required. The trend raises expected service demand by `0.4824` minutes per customer, or about `16.35%`, because probability moves toward the slowest drink. A sample maximum need not move in the same direction because it is highly variable. Before acting, the manager should validate the drink mix, service-time distributions, arrival rates, and peak-period patterns.

## Three-Point Check

| Point | Evidence |
|---:|---|
| 1 | Completed inverse-transform, NumPy consistency check, and accept-reject work at Checkpoint 1 |
| 2 | Completed discrete inverse-transform drink simulation and drink-level summary |
| 3 | Student explains one generation method and gives an evidence-based manager recommendation |

## Oral Questions

- Why must the exponential scale equal the model mean?
- What does inverse transform do to a uniform probability?
- Why does the Part B check use a tolerance rather than exact equality?
- Why do rejected proposals still count?
- Why does the accept-reject histogram rise toward 1?
- Why is service time conditional on drink choice?
- How does `searchsorted` act as a discrete inverse CDF?
- Why do simulated proportions differ from input probabilities?
- Why can an expectation rise even if a future sample maximum does not?
- Which result supports the manager recommendation?

## Common Errors

- Using `mean_service` as the exponential rate instead of the scale.
- Omitting the negative sign in the inverse-transform formula.
- Comparing two random samples only by element-wise equality.
- Stopping accept-reject sampling after 1,000 proposals instead of 1,000 acceptances.
- Dividing by accepted values rather than all proposals for the acceptance rate.
- Using drink probabilities that do not sum to 1 or failing to construct cumulative cut points.
- Generating service times before assigning drinks.
- Running another trend simulation instead of using the expectation formula requested in Part E.
