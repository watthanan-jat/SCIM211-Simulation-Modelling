# Lab 6: Markov Chains and Customer Loyalty

## Theme

A Markov chain models how a system moves between states over time.

In this lab, you will model coffee shop customer loyalty using transition probabilities. You will compare one customer path, many customer paths, matrix powers, and a loyalty-card investigation.

## Part 0: Setup

Open `starter.ipynb` in this folder and run the imports.

Use these states:

```text
Loyal
Occasional
Inactive
```

## Part A: Define the States

Use the following interpretation:

| State | Meaning |
|---|---|
| Loyal | visits regularly |
| Occasional | visits sometimes |
| Inactive | rarely or no longer visits |

Answer:

1. Why is customer loyalty a state?
2. What real behaviour might cause a customer to move between states?
3. What information is lost when only three states are used?

## Part B: Transition Matrix

Use a baseline transition matrix:

| From / To | Loyal | Occasional | Inactive |
|---|---:|---:|---:|
| Loyal | 0.70 | 0.20 | 0.10 |
| Occasional | 0.25 | 0.55 | 0.20 |
| Inactive | 0.10 | 0.25 | 0.65 |

Check:

```text
each row sums to 1
all probabilities are between 0 and 1
```

Answer:

1. What does the Loyal row mean?
2. Why must each row sum to 1?
3. Which state is most likely to remain unchanged?

## Part C: Simulate One Customer Path

Start one customer in the `Loyal` state.

Simulate 12 weeks.

Record the sequence of states.

Answer:

1. Did the path stay loyal?
2. Did it move to inactive?
3. Why can one path be misleading?

## Part D: Simulate Many Customers

Simulate 1000 customers for 12 weeks.

Use an initial distribution such as:

| State | Initial proportion |
|---|---:|
| Loyal | 0.50 |
| Occasional | 0.35 |
| Inactive | 0.15 |

Create:

- state counts by week
- state proportions by week
- line plot of proportions over time

## Part E: Matrix Powers

Calculate:

```text
P^2
P^5
P^10
P^20
```

Use the powers to describe longer-run behaviour.

Answer:

1. What happens as the number of steps increases?
2. Do rows begin to look similar?
3. What does this suggest about long-run loyalty?

## Part F: Loyalty-Card Investigation

The coffee shop introduces a loyalty card.

Modify the transition matrix so that:

- loyal customers are more likely to remain loyal
- occasional customers are more likely to become loyal
- inactive customers are slightly more likely to return

Compare baseline and loyalty-card outcomes after 12 weeks.

Complete:

| Case | Loyal proportion | Occasional proportion | Inactive proportion |
|---|---:|---:|---:|
| Baseline | | | |
| Loyalty card | | | |

## Checkpoint Submission

Submit:

1. transition matrix check
2. one customer path
3. many-customer plot
4. matrix-power interpretation
5. loyalty-card comparison
6. AI use statement

## Reflection Questions

Write 150-200 words:

1. What does the Markov assumption mean here?
2. Why is one customer path not enough?
3. What did matrix powers add to the analysis?
4. Did the loyalty card help? Explain using results.
5. Include an AI use statement.
