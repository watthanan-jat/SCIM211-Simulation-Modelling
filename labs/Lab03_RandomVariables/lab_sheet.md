# Lab 3: From Random Numbers to Random Variables

## Theme

Random numbers become useful in simulation when they are transformed into realistic model inputs.

In this lab, you will use random numbers to simulate:

1. customer drink choices
2. exponential service times
3. drink-dependent service times
4. the effect of a matcha trend on workload

The coffee shop model becomes more realistic because customers do not all order the same drink and drinks do not all take the same time to prepare.

## Part 0: Setup

Open `starter.ipynb` in this folder.

Run:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Use a fixed seed when comparing scenarios so that your work is reproducible.

## Part A: Why Random Variables?

In Lab 2, you generated uniform random numbers. Uniform numbers are useful, but coffee shop inputs usually do not look uniform.

Examples:

- service time is often positive and right-skewed
- drink type is categorical
- customer spend may vary by order
- busy periods may change the mix of orders

Answer:

1. Why is it unrealistic to give every customer the same service time?
2. Why might different drinks need different service-time assumptions?
3. What could go wrong if the service-time model is too simple?

## Part B: Exponential Service Times

Start with one drink type and assume service time follows an exponential distribution.

Use:

```text
mean service time = 3 minutes
```

Generate 100 service times and create:

- summary statistics
- histogram
- short interpretation

Answer:

1. Are all service times close to 3 minutes?
2. Are there unusually long service times?
3. Why might long service times matter in a queue?

## Part C: Simulate Drink Orders

Use this baseline menu:

| Drink | Probability |
|---|---:|
| Coffee | 0.35 |
| Tea | 0.20 |
| Latte | 0.30 |
| Matcha | 0.15 |

Generate 100 customer drink orders.

Create:

- a frequency table
- a bar chart of drink counts

Answer:

1. Did the simulated proportions exactly match the probabilities?
2. Why should small samples be expected to vary?
3. Which drink appeared most often?

## Part D: Drink-Dependent Service Times

Use these mean service times:

| Drink | Mean service time |
|---|---:|
| Coffee | 2.0 |
| Tea | 1.5 |
| Latte | 3.5 |
| Matcha | 4.0 |

For each simulated order, generate a service time based on the drink type.

Create a DataFrame with:

```text
customer, drink, service_time
```

Then calculate:

- average service time by drink
- overall average service time
- longest service time

Answer:

1. Which drink creates the highest average workload?
2. Which drink is quickest?
3. Why does drink mix matter for queueing?

## Part E: Matcha Trend Investigation

The coffee shop notices a matcha trend.

Change the drink probabilities to:

| Drink | Probability |
|---|---:|
| Coffee | 0.25 |
| Tea | 0.15 |
| Latte | 0.25 |
| Matcha | 0.35 |

Repeat the simulation for 100 customers.

Compare:

| Case | Average service time | Matcha count | Longest service time |
|---|---:|---:|---:|
| Baseline | | | |
| Matcha trend | | | |

Answer:

1. How did the average service time change?
2. Why did the matcha trend affect workload?
3. What might happen to waiting time in the next lab?

## Part F: Manager Interpretation

Use your simulation results to write a short recommendation.

Consider:

- staffing
- drink preparation process
- menu design
- whether matcha should be promoted during rush hour

## Checkpoint Submission

Submit:

1. completed notebook
2. baseline drink count table
3. baseline service-time summary
4. matcha-trend comparison table
5. completed report template
6. AI use statement

## Reflection Questions

Write 150-200 words:

1. Why are random variables needed after random numbers?
2. Which assumption in this lab is most important?
3. How could real coffee shop data improve the model?
4. How does this lab prepare the model for queue simulation?
5. Include an AI use statement.
