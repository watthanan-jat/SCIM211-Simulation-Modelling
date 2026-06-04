# Lab 7: Validation and Final Recommendation

## Theme

A simulation model is only useful if its inputs, outputs, assumptions, and recommendations are checked carefully.

In this lab, you will use service-time data, fit a service-time distribution, run repeated simulations, calculate confidence intervals, and write a final recommendation for the Coffee Shop Simulation Project.

## Part 0: Setup

Open `starter.ipynb` in this folder.

Use:

```text
service_times.csv
```

This file contains observed service-time data in minutes.

## Part A: Input Data Check

Load the service-time data.

Calculate:

- count
- mean
- standard deviation
- minimum
- maximum
- histogram

Answer:

1. What is a typical service time?
2. Are there very short or very long service times?
3. Does the data look symmetric or skewed?

## Part B: Fit an Exponential Service Distribution

Fit an exponential distribution using:

```text
mean service time = sample mean
rate = 1 / sample mean
```

Generate fitted exponential samples.

Create a histogram comparison:

- observed service times
- fitted exponential service times

Answer:

1. Does the exponential distribution match the observed data well?
2. Where does it fit poorly?
3. Is it good enough for a simple course project model?

## Part C: Replication Model

Use your fitted service-time model in a simple coffee shop queue simulation.

Run one replication with:

- customer arrivals
- sampled service times
- one barista
- first come, first served

Return:

```text
average_wait
max_wait
max_queue_length
number_served
```

## Part D: Run 30 Replications

Run 30 independent replications.

Create a DataFrame with:

```text
replication, average_wait, max_wait, max_queue_length, number_served
```

Why 30 replications?

Repeated simulation runs help estimate uncertainty in the output.

## Part E: Confidence Intervals

Calculate a 95% confidence interval for:

- average waiting time
- maximum queue length
- number served

Use:

```text
mean ± 1.96 * standard error
```

Answer:

1. Which output is most uncertain?
2. What does the interval say that a single run cannot?
3. How should uncertainty affect the final recommendation?

## Part F: Final Recommendation

Write a recommendation for the coffee shop manager.

Your recommendation should include:

- main simulation result
- confidence interval evidence
- model assumptions
- validation comment
- one limitation
- one practical action

## Checkpoint Submission

Submit:

1. input data summary
2. histogram comparison
3. 30-replication table
4. confidence interval table
5. final recommendation
6. AI use statement

## Reflection Questions

Write 150-200 words:

1. Why is validation important?
2. Did the exponential service-time model seem reasonable?
3. Why are multiple replications better than one run?
4. What final recommendation would you make?
5. Include an AI use statement.
