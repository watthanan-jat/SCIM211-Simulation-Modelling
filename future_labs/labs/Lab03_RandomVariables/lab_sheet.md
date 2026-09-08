# Lab 3: From Random Numbers to Random Variables

## Theme

Lab 2 produced uniform pseudo-random numbers. In this lab, you transform those numbers into realistic coffee-shop inputs: service times and drink choices.

The instructor demo has already introduced inverse-transform sampling, accept-reject sampling, NumPy's distribution generators, and discrete inverse-transform sampling.

## Part A: Generate Exponential Service Times

Assume a customer's service time is exponential with a mean of 3 minutes. For a uniform value `U` in `(0, 1)`, use:

```text
lambda = 1 / mean_service
X = -log(1 - U) / lambda
```

Using seed `211`, generate 1,000 service times with the inverse-transform formula.

Create:

1. a table containing the sample mean, standard deviation, minimum, and maximum; and
2. a histogram of the service times.

Check that every generated service time is non-negative.

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Why are most service times short while a few are long?
2. Why can a long service time matter in a queue?
3. Why does this method start with uniform random numbers?

## Part B: Confirm Against NumPy's Generator

Create a new generator with seed `211` and generate another 1,000 exponential service times using:

```python
rng.exponential(scale=mean_service, size=1000)
```

Run the provided consistency check. It prints the manual sample mean, the NumPy sample mean, and the model mean, then checks that the two sample means are reasonably close. If the check fails, first inspect whether `rng.exponential` received the mean (`scale`) rather than the rate.

Write a short response explaining:

1. why the check uses a tolerance rather than exact equality; and
2. what a difference of about 50% between the two sample means would suggest.

## Part C: Use Accept-Reject Sampling

Generate values from the density `f(x) = 2x` on `[0, 1]`. Use the following procedure:

1. propose `x` from `Uniform(0, 1)`;
2. generate `u` from `Uniform(0, 1)`;
3. accept `x` when `u <= x`; and
4. otherwise reject it and try again.

Using seed `211`, continue until you have 1,000 accepted values. Report:

1. the total number of proposals;
2. the acceptance rate;
3. the sample mean; and
4. a histogram of the accepted values.

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Why should the histogram contain more values near 1 than near 0?
2. Why are rejected proposals not coding errors?
3. What feature of an accept-reject method determines its efficiency?

## Checkpoint 1: First Half (1 of 3 Points)

Target time: approximately 60 minutes into the lab.

Show your notebook to the TA after completing Parts A-C. To receive the first 1 point, your notebook must contain:

1. 1,000 inverse-transform exponential service times and their summary table;
2. the NumPy sample, passed consistency check, and written response;
3. 1,000 accepted values from `f(x) = 2x`; and
4. the accept-reject proposal count, acceptance rate, sample mean, and histogram.

The TA may ask you to explain the shape of either distribution or the accept-reject rule. The TA will record the checkpoint during the lab. You do not need to upload the notebook yet; continue with Parts D-E.

## Part D: Simulate Drink Orders and Service Times

Use the following baseline model:

| Drink | Probability | Mean service time (minutes) |
|---|---:|---:|
| Coffee | 0.35 | 2.0 |
| Tea | 0.20 | 1.5 |
| Chocolate | 0.30 | 4.0 |
| Matcha | 0.15 | 5.0 |

Using seed `211`:

1. build the cumulative probabilities (the discrete CDF) for the four drinks;
2. generate one uniform value per customer and use `np.searchsorted` to map it to the first cumulative cut point that contains it;
3. generate a second uniform value per customer, after assigning the drink, and apply the inverse-transform formula using that drink's mean;
4. create a table of counts, simulated proportions, and average service times by drink; and
5. report the overall average and longest service times.

Do not use `rng.choice` for the drink assignment. This part assesses the discrete inverse-transform method introduced in the demo.

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Why do the simulated proportions not exactly equal the model probabilities?
2. Which drink contributes most to the workload?
3. Why should drink choice be generated before service time?
4. Why can the continuous inverse-transform proof not be applied directly to a step-shaped discrete CDF? How does selecting the first cut point at or above `U` solve the problem?

## Part E: Reflect on a Matcha Trend

No new simulation is required. Suppose matcha's probability rises from `0.15` to `0.35`. Reduce the other three probabilities in the same proportion, leaving their relative mix unchanged:

| Drink | Baseline | Matcha trend |
|---|---:|---:|
| Coffee | 0.35 | $0.35(0.65/0.85) \\approx 0.2676$ |
| Tea | 0.20 | $0.20(0.65/0.85) \\approx 0.1529$ |
| Chocolate | 0.30 | $0.30(0.65/0.85) \\approx 0.2294$ |
| Matcha | 0.15 | 0.35 |

Keep the drink-specific mean service times from Part D. Use

$$
E[T] = \\sum_j p_j \\mu_j
$$

to answer the following in the notebook:

1. Calculate the expected service time under the baseline and matcha-trend probabilities. Which direction does expected workload move, and why?
2. Does the longest observed service time in a 1,000-customer sample necessarily move in the same direction as the expected service time? Why or why not?
3. What should a manager check in real data before acting on this predicted shift?

Include a short manager recommendation and an AI-use statement in the notebook.

## Checkpoint 2: Final Submission

Show the completed Part D simulation and summary, Part E expectation-based reflection, manager recommendation, and AI-use statement to the TA. Be prepared to explain how the matcha trend changes predicted workload without claiming that this lab has simulated a queue. After the final checkpoint, save the notebook as:

```text
Lab03_StudentID.ipynb
```

For example, student ID 6812345 should submit `Lab03_6812345.ipynb`.

Upload the completed notebook to the **Lab 03** assignment in Google Classroom before leaving the lab. The notebook must include:

1. completed and executed Python code;
2. all requested summary tables and plots;
3. the Part E expectation calculations and written reflection;
4. the manager recommendation; and
5. the AI-use statement.

Before uploading, restart the kernel, run all cells from top to bottom, check that there are no errors, and save the notebook.
