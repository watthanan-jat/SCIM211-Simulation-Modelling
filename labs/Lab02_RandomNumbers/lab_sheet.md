# Lab 2: Random Numbers and Interarrival Times

## Theme

Random number generation for the Coffee Shop Simulation Project.

## Scenario

The coffee shop needs simulated customer arrivals. Before using built-in random functions, you will study how pseudo-random numbers are generated and how uniform random numbers can be transformed into exponential interarrival times.

## Learning Objectives

- Implement a linear congruential generator (LCG).
- Explain seed, sequence, and period.
- Use histograms and scatter plots to inspect random numbers.
- Plot `U_i` against `U_{i+1}`.
- Generate exponential interarrival times for customer arrivals.

## 2-Hour Timing Plan

| Time | Activity |
|---:|---|
| 0-10 min | Recap Lab 1 and introduce random numbers |
| 10-25 min | Instructor demo: LCG and seed |
| 25-45 min | Guided task: generate and inspect uniforms |
| 45-70 min | Coding task: histogram and scatter plot |
| 70-100 min | Exponential interarrival times |
| 100-115 min | Investigation: seed and period effects |
| 115-120 min | Checkpoint submission |

## Instructor Demo

The instructor will show how an LCG creates a deterministic sequence from:

```text
X_{n+1} = (a X_n + c) mod m
U_n = X_n / m
```

The demo will compare two different seeds and discuss why a repeatable random sequence is useful for simulation testing.

## Guided Task

Use the starter notebook to generate a short LCG sequence. Record the integer values and the corresponding uniform values.

Discuss:

- What happens when the seed changes?
- What does period mean?
- Why is a short period a problem?

## Coding Task

Complete the TODO cells to:

- Generate at least 100 uniform values.
- Draw a histogram of the values.
- Draw a scatter plot of `U_i` versus `U_{i+1}`.
- Generate exponential interarrival times using inverse transform logic.

## Investigation

Try at least two different seeds and one deliberately small modulus. Compare the histogram, scatter plot, and approximate period.

Then generate customer arrival times from exponential interarrival times and describe what the pattern suggests about the coffee shop.

## Checkpoint Submission

Submit:

- Completed `starter.ipynb`.
- Completed `report_template.md`.
- Histogram and scatter plot screenshots or summaries.
- AI use statement.

## Reflection Questions

1. Why does simulation use pseudo-random numbers instead of truly random numbers?
2. What role does the seed play?
3. What visual pattern would make you suspicious of a random number generator?
4. Why are exponential interarrival times useful for modelling customer arrivals?
5. How would poor random numbers affect the Coffee Shop Simulation Project?

## AI Use Statement

State whether you used AI, what you used it for, and what you checked yourself. If you did not use AI, write: `AI use statement: I did not use AI tools for this lab.`
