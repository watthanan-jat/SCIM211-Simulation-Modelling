# Lab 6: Markov Chains and Customer Loyalty

## Theme

Lab 5 followed customers through one day in continuous time. In this lab you follow customers from week to week. A customer's loyalty is modelled as a Markov chain: you build and check a transition matrix, simulate customers from uniform random numbers, compare the simulation with exact matrix calculations, find the long-run customer mix, test the warm-up and dependence warnings from Chapter 8, and evaluate a loyalty card for the manager.

Chapter 8 introduced transition matrices, $n$-step probabilities, stationary distributions, the ergodic theorem, and the slotted coffee-shop queue.

## Lab Settings

Use these settings throughout. They are defined in the first code cell of `starter.ipynb`.

```text
states    = Loyal, Occasional, Inactive   (in this order)
seed      = 211 for every random result
weeks     = 12
customers = 1,000
```

Start each simulation in Parts B and C with a fresh generator, `np.random.default_rng(211)`. Part D uses one generator for all 200 runs.

Use the row-vector convention: if $\pi_n$ is the distribution in week $n$, then $\pi_{n+1}=\pi_nP$ and $\pi_n=\pi_0P^n$.

## Part A: The Transition Matrix

| From / To | Loyal | Occasional | Inactive |
|---|---:|---:|---:|
| Loyal | 0.70 | 0.20 | 0.10 |
| Occasional | 0.25 | 0.55 | 0.20 |
| Inactive | 0.10 | 0.25 | 0.65 |

Enter `P` and complete `validate_transition_matrix`, which must check that the matrix is square, every entry is in $[0,1]$, and every row sums to 1. The provided trials check that a row summing to 1.2 and a row containing a negative entry are both rejected.

Write short answers in the notebook:

1. What does the Loyal row mean?
2. The `bad_negative` row sums to 1. Why is it still not a valid row?
3. State the Markov assumption for this model in one sentence, and give one real reason it might fail.

Think about the following question. You do not need to write an answer, but the TA may ask you to explain your reasoning:

4. What information about a real customer is lost when we use only three states?

## Part B: Simulate Customers

Chapter 8 simulates one step by drawing $U\sim\mathrm{Uniform}(0,1)$ and comparing it with the cumulative probabilities of the current row. This is the discrete inverse-transform method from Lab 3 Part D.

1. Complete `sample_state(probabilities, u)`: return the index of the first cumulative probability at or above `u`, using `np.searchsorted`. Do **not** use `rng.choice`.
2. Complete `simulate_path(matrix, start, n_steps, rng)`, which draws one uniform number per step.
3. Simulate one customer who starts Loyal, for 12 weeks, with seed 211.
4. Complete `simulate_customers`: each of 1,000 customers draws a starting state from the current mix $\pi_0=(0.50,\ 0.35,\ 0.15)$ and then follows the chain for 12 weeks (seed 211).
5. Compute the exact distributions $\pi_0P^n$ for $n=0,\dots,12$. The provided table and plot compare them with the simulation.

Think about the following questions:

1. The single path left Loyal and later came back. What does one path tell a manager, and what does it not?
2. Why do the simulated week-12 proportions differ slightly from $\pi_0P^{12}$? Which of the two is random?
3. Why does a 12-step path contain 13 states?

## Checkpoint 1: Matrix and Simulation (1 of 3 Points)

Target time: approximately 60 minutes into the lab.

Show your notebook to the TA after completing Parts A-B. To receive the first 1 point, your notebook must contain:

1. the validated matrix, the passed trial checks, and the three Part A responses;
2. `sample_state` passing the hand checks and the reproducible 12-week path; and
3. the 1,000-customer comparison table and plot.

Be prepared to explain how one uniform number becomes the next state, and why the simulated and exact week-12 proportions differ. Continue with Parts C-E.

## Part C: Long-Run Behaviour

A stationary distribution satisfies $\pi=\pi P$ and $\sum_j\pi_j=1$. For an irreducible, aperiodic chain the rows of $P^n$ converge to $\pi$, and the fraction of time one long path spends in each state converges to $\pi$ (ergodic theorem). Estimate $\pi$ three ways:

1. compute $P^1, P^2, P^5, P^{10}, P^{20}$;
2. complete `stationary_distribution`, which solves $(P^{\mathsf T}-I)\pi^{\mathsf T}=0$ with the last equation replaced by $\sum_j\pi_j=1$ (in NumPy, `matrix.T` is $P^{\mathsf T}$ and `np.eye(n)` is $I$); and
3. simulate one path of 20,000 weeks from Loyal (seed 211), discard weeks 0-100 as warm-up, and compute the fraction of the remaining weeks spent in each state.

The provided table also shows the week-12 proportions of the 1,000 customers from Part B: many independent customers observed at one late time.

Write short answers in the notebook:

1. What happens to the rows of $P^n$ as $n$ grows, and what does that mean for a customer who is Loyal today?
2. Compare the four rows. Which are exact once $P$ is fixed, and which are random? Why can one long path, or many customers observed in week 12, estimate $\pi$ at all?

Think about the following question:

3. If Inactive $\to$ Inactive were 0.95 instead of 0.65, which way would the long-run Inactive proportion move?

## Part D: Warm-Up and Dependence

Chapter 8 §8.11 models the coffee shop once per minute: $X_n\in\{0,1,2,3\}$ customers, arrival probability $p=\tfrac14$, service-completion probability $q=\tfrac12$. The matrix $Q$ is provided. Its exact stationary distribution is $\pi=\frac{1}{53}(27,18,6,2)$, with long-run mean $36/53\approx0.679$ customers. Your Part A and Part C functions must reproduce this.

Run 200 independent runs of 1,000 minutes, each starting from an empty shop, using one generator with seed 211 for all runs. For each run record:

1. the run average $\frac1{1000}\sum_{n=1}^{1000}X_n$; and
2. the naive standard error $s/\sqrt{1000}$ computed from that run alone.

The provided code

- compares the proportion of time the shop spends in each state, pooled over all minutes of all runs and at minute 1000 across the 200 runs, with the solved $\pi$;
- compares the typical naive standard error with the actual standard deviation of the 200 run averages; and
- plots the mean of $X_n$ over the first 50 minutes.

Write short answers in the notebook:

1. Compare the naive standard error from one run with the actual standard deviation of the 200 run averages. Which should you trust, and why are they different?
2. What does the warm-up plot show? How does it explain why a short run that starts empty underestimates the long-run mean (compare Lab 5's rush scenario)?

Think about the following questions:

3. Why is the warm-up bias small here but large in Lab 5's rush scenario?
4. In the table of state proportions, which result justifies each simulated row? The first row is closer to $\pi$ than the second, even though its minutes are dependent. Why?

## Part E: Manager Challenge — a Loyalty Card

The manager proposes a loyalty card. Its **assumed** effect is:

| From / To | Loyal | Occasional | Inactive |
|---|---:|---:|---:|
| Loyal | 0.80 | 0.15 | 0.05 |
| Occasional | 0.35 | 0.50 | 0.15 |
| Inactive | 0.15 | 0.30 | 0.55 |

These are exact model quantities, so no new simulation is needed. Complete `distribution_after(matrix, initial, n)`, which returns $\pi_0P^n$. The provided code compares baseline and card at weeks 1, 4 and 12 and in the long run, and then changes one baseline row at a time to its card row.

Write short answers in the notebook:

1. Describe the effect of the card on the Loyal share over time. How quickly does most of the effect appear?
2. Which single row change matters most for the long-run Loyal share? Why might that be?

Think about the following question:

3. The card matrix is an assumption. What data would you need before trusting it?

## Recommendation, Reflection, and AI Use

In the notebook, write:

1. **Manager recommendation** using the Part E evidence: what the model predicts, how quickly, and what evidence is needed before rolling the card out.
2. **Reflection:** the Markov assumption; why one path is not enough; what matrix powers and the stationary distribution added; what Part D showed about simulating long runs.
3. **AI-use statement:** the tool, how it was used, and how you checked its output, or a statement that AI was not used.

## Optional Bonus (not assessed): Markov Chain Monte Carlo

The last notebook cell builds a Markov chain whose stationary distribution is a target drink-preference distribution (Coffee 0.50, Latte 0.30, Matcha 0.20) using the Metropolis acceptance rule $\min(1,\ \text{target[new]}/\text{target[current]})$. Complete the acceptance probability and compare the sampled proportions with the target.

## Checkpoint 2: Final Submission

Show the completed Parts C-E, recommendation, reflection, and AI-use statement to the TA. Be prepared to answer one code question and one modelling question, for example why the naive standard error in Part D is too small. After the final checkpoint, save the notebook as:

```text
Lab06_StudentID.ipynb
```

For example, student ID 6812345 should submit `Lab06_6812345.ipynb`.

Upload the completed notebook to the **Lab 06** assignment in Google Classroom before leaving the lab. The notebook must include:

1. completed and executed Python code;
2. all requested tables and plots;
3. the written responses for Parts A, C, D, and E;
4. the manager recommendation and reflection; and
5. the AI-use statement.

Before uploading, restart the kernel, run all cells from top to bottom, check that there are no errors, and save the notebook.
