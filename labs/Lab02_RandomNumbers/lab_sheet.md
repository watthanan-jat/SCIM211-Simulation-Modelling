# Lab 2: Can Computers Really Be Random?

## Theme

Every simulation model depends on random numbers.

If the random numbers are poor, the simulation results may be misleading.

In this lab students investigate:

- pseudo-random numbers
- seeds
- reproducibility
- periods
- randomness diagnostics
- customer arrival generation

The lab is designed for a 2-hour session.

## Learning Objectives

By the end of this lab students should be able to:

1. Explain why computers generate pseudo-random rather than truly random numbers.
2. Explain the concepts of seed and period.
3. Implement a linear congruential generator (LCG).
4. Compare different random-number generators.
5. Use graphical diagnostics to evaluate randomness.
6. Generate customer arrival times from uniform random numbers.
7. Explain why random-number quality matters in simulation.

## Lab Timing

| Time | Activity |
|---:|---|
| 0-10 min | Motivation and prediction |
| 10-25 min | Randomness challenge |
| 25-50 min | Build an LCG |
| 50-75 min | Diagnosing randomness |
| 75-100 min | Generating customer arrivals |
| 100-115 min | Investigation |
| 115-120 min | Checkpoint |

## Part 0: Motivation

Scenario:

The coffee shop owner asks:

> "How do you know your simulation is not just making up nonsense?"

Discussion:

Imagine two simulation teams.

Team A:

Uses a poor random-number generator.

Team B:

Uses a high-quality generator.

Questions:

1. Could they get different simulation results?
2. Why?
3. What makes a random number generator good?

## Part A: Randomness Challenge

### Instructor Demo

Show these sequences:

Sequence A:

```text
0.13
0.72
0.54
0.19
0.88
0.44
```

Sequence B:

```text
0.11
0.22
0.33
0.44
0.55
0.66
```

Sequence C:

```text
0.12
0.81
0.12
0.81
0.12
0.81
```

Students vote:

Which sequence looks most random?

Discussion:

Can humans reliably detect randomness?

## Part B: What is a Seed?

### Instructor Demo

Run:

```python
rng = np.random.default_rng(211)
rng.random(5)
```

Run again.

Questions:

1. Why are the numbers identical?
2. Is that a bug?
3. Why is reproducibility important in simulation?

Students repeat with:

```text
211
212
213
```

and compare outputs.

## Part C: Build Your Own Random Number Generator

Introduce:

```text
X_(n+1) = (aX_n + c) mod m
U_n = X_n / m
```

Students complete:

```python
def lcg(a, c, m, x0, n):
    ...
```

Test:

Generator A:

```text
a=5
c=0
m=8
x0=3
```

Generator B:

```text
a=5
c=1
m=16
x0=3
```

Generator C:

```text
a=13
c=7
m=31
x0=3
```

## Part D: Find the Period

Students investigate:

1. Does the sequence repeat?
2. When?
3. Which generator has the longest period?

Complete:

| Generator | Period |
|---|---:|
| A | |
| B | |
| C | |

Discussion:

Why is a short period dangerous?

## Part E: Diagnosing Randomness

Generate 1000 values.

Create:

Histogram

```python
plt.hist(...)
```

Questions:

1. Is the histogram roughly uniform?
2. Are some regions overrepresented?

Then create:

Scatter plot

```text
(U_i, U_{i+1})
```

Questions:

1. Do points fill the square?
2. Do lines or patterns appear?
3. Why is this bad?

## Part F: From Uniform Numbers to Customer Arrivals

Coffee shop arrival rate:

```text
lambda = 6 customers/hour
```

Generate:

```text
interarrival = -log(U)/lambda
arrival_times = cumulative sum
```

Questions:

1. Why are arrival times increasing?
2. Why are gaps not equal?
3. Which customer arrives first?

## Part G: Investigation

Compare:

Quiet hour:

```text
lambda = 3
```

Normal hour:

```text
lambda = 6
```

Rush hour:

```text
lambda = 10
```

For each case:

Generate 20 customers.

Plot arrival times.

Complete:

| Scenario | Average gap |
|---|---:|
| Quiet | |
| Normal | |
| Rush | |

Questions:

1. Which hour feels busiest?
2. How does arrival rate affect waiting?
3. What do you predict for the queue?

## Bonus Challenge

The coffee shop experiences a flash sale.

For the first hour:

```text
lambda = 15
```

After that:

```text
lambda = 4
```

Generate arrivals for the day.

Plot arrival times.

What difficulties might this create?

## Checkpoint Submission

Students submit:

1. LCG implementation
2. Generator period table
3. Histogram
4. Scatter plot
5. Arrival-time plot
6. Reflection

## Reflection Questions

Write 150-200 words.

1. Why is reproducibility useful?
2. Why is a short period dangerous?
3. Why does a simulation model depend heavily on random numbers?
4. Which randomness diagnostic did you find most convincing?

Include AI use statement.
