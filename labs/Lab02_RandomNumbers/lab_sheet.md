# Lab 2: Can Computers Really Be Random?

## Theme

Simulation models depend on pseudo-random numbers. A useful stream should be reproducible when needed, have a sufficiently long period, cover the unit interval, and avoid obvious dependence.

The instructor demo has already covered short-sequence judgement, seeds, state, and reproducibility.


## Part A: Build Your Own Random-Number Generator

Use:

```text
X_(n+1) = (aX_n + c) mod m
U_n = X_n / m
```

Complete:

```python
def lcg(a, c, m, x0, n):
    ...
```

Test these generators:

| Generator | a | c | m | x0 |
|---|---:|---:|---:|---:|
| A | 5 | 0 | 8 | 3 |
| B | 5 | 1 | 16 | 3 |
| C | 13 | 7 | 31 | 3 |

Check that every generated `U` lies in `[0, 1)`.

## Part B: Find the Period

A period is the length of the repeating cycle.

Complete a function that:

1. stores previously seen integer states `X`;
2. generates the next state;
3. stops when a state repeats; and
4. returns the cycle length.

Complete:

| Generator | Period |
|---|---:|
| A | |
| B | |
| C | |

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Which generator has the longest period?
2. Why is a short period dangerous in a long simulation?

## Part C: Diagnose Generator B

Generate 1,000 values from Generator B.

Create:

1. a histogram of the `U` values; and
2. a scatter plot of `(U_i, U_(i+1))`.

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Does the histogram cover the interval reasonably?
2. Does the scatter plot contain repeated points or visible structure?
3. What does the scatter plot reveal that the histogram can hide?

## Checkpoint 1: First Half (1 of 3 Points)

Target time: approximately 60 minutes into the lab.

Show your notebook to the TA after completing Parts A-C. To receive the first 1 point, your notebook must contain:

1. a completed and executed LCG function;
2. the first 10 values from Generators A, B, and C, with confirmation that all `U` values lie in `[0, 1)`;
3. the completed period table; and
4. Generator B's histogram and successive-value scatter plot.

The TA may ask you to explain your reasoning about the period, histogram, or scatter plot. The TA will record the checkpoint during the lab. You do not need to upload the notebook yet; continue with Parts D-E.

## Part D: Compare Generator B with NumPy

Generate 1,000 NumPy values using the documented seed `211`.

Compare NumPy and Generator B using:

- mean;
- minimum;
- maximum;
- number of distinct values; and
- the successive-value scatter plots.

Complete:

| Source | Mean | Min | Max | Distinct values | Visible scatter pattern? |
|---|---:|---:|---:|---:|---|
| NumPy | | | | | |
| Generator B | | | | | |

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Which source would you trust for a real simulation?
2. Why can two sources have similar means but very different quality?

## Part E: Interpretation, Seeds, and Reproducibility

Repeat the seed experiment from the instructor demo:

1. create a NumPy generator with seed `211` and record its first five values;
2. create a new NumPy generator with seed `211` and record its first five values; and
3. create a new NumPy generator with seed `212` and record its first five values.

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Are the two sequences generated with seed `211` identical? Why?
2. How does the sequence generated with seed `212` differ?
3. Does setting a seed make the simulation model deterministic? Explain the difference between a stochastic model and a reproducible sample path.
4. Why should the seed be recorded in a simulation report?

Include an AI-use statement.

## Checkpoint 2: Final Submission

Show the completed Parts D-E and AI-use statement to the TA. Be prepared to explain what the seed experiment demonstrates about reproducibility. After the final checkpoint, save the notebook as:

```text
Lab02_StudentID.ipynb
```

For example, student ID 6812345 should submit `Lab02_6900789.ipynb`.

Upload the completed notebook to the **Lab 02** assignment in Google Classroom before leaving the lab. The notebook must include:

1. completed and executed Python code;
2. the period table;
3. Generator B's histogram and scatter plot;
4. the NumPy-versus-B comparison table and plots;
5. the completed seed experiment; and
6. the AI-use statement.

Before uploading, restart the kernel, run all cells from top to bottom, check that there are no errors, and save the notebook.
