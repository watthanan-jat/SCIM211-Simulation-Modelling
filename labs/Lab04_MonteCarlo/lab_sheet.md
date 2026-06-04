# Lab 4: Monte Carlo Profit and Promotion Decision

## Theme

Monte Carlo simulation helps make decisions when demand, revenue, and cost are uncertain.

In this lab, you will evaluate a matcha promotion for the coffee shop. The question is not only whether the promotion has a high average profit, but also whether it increases risk.

## Part 0: Setup

Open `starter.ipynb` in this folder and run the imports.

Use a fixed seed so your results can be checked and repeated.

## Part A: The Decision Problem

The coffee shop manager is considering a matcha promotion.

Possible benefits:

- more customers
- higher matcha sales
- stronger brand visibility

Possible costs:

- promotion cost
- longer service times
- more overloaded days
- more bad-day risk

Answer:

1. Why is average profit not enough for this decision?
2. What does a bad day mean for a coffee shop?
3. What uncertainty should be included in the model?

## Part B: Build One Simulated Day

Create assumptions for one business day.

Suggested baseline:

| Quantity | Example assumption |
|---|---|
| Number of customers | random normal or Poisson |
| Average spend per customer | random normal |
| Variable cost per customer | fixed or random |
| Fixed daily cost | fixed |

Create one simulated baseline profit:

```text
profit = revenue - variable cost - fixed cost
```

Then create one simulated promotion profit with:

- higher expected demand
- promotion cost
- possible higher average spend

## Part C: Run Many Replications

Run at least 1000 replications for:

1. baseline case
2. matcha promotion case

Create a DataFrame with:

```text
replication, case, profit
```

Calculate:

- mean profit
- standard deviation of profit
- minimum profit
- maximum profit

## Part D: Bad-Day Probability

Define a bad day threshold, such as:

```text
profit < 0
```

or another threshold that makes sense for your assumptions.

Calculate:

```text
bad-day probability = number of bad days / number of replications
```

Answer:

1. Which case has the lower bad-day probability?
2. Does the promotion increase expected profit?
3. Does the promotion also increase risk?

## Part E: Confidence Interval

Calculate a 95% confidence interval for mean profit.

Use:

```text
mean ± 1.96 * standard error
```

where:

```text
standard error = sample standard deviation / sqrt(number of replications)
```

Compare the baseline and promotion intervals.

## Part F: Promotion Recommendation

Use the simulation output to make a recommendation.

Your recommendation should mention:

- expected profit
- bad-day probability
- confidence interval
- at least one limitation of the model

## Checkpoint Submission

Submit:

1. completed notebook
2. assumptions table
3. profit summary table
4. bad-day probability
5. confidence interval
6. recommendation
7. AI use statement

## Reflection Questions

Write 150-200 words:

1. Why is Monte Carlo useful for this decision?
2. Why can expected profit be misleading?
3. How did the bad-day probability affect your recommendation?
4. What assumption would you most want to replace with real data?
5. Include an AI use statement.
