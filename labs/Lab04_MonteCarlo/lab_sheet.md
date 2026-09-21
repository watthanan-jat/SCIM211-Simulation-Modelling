# Lab 4 · Week 8 — Should We Run the Promotion?

Use Monte Carlo experiments to compare expected profit, loss risk, and uncertainty before recommending whether the café should run a matcha promotion.

## How to Use This Lab

Open `starter.ipynb`. The notebook is both your workspace and your report: it carries the explanation, the code TODOs, and **six short written responses**. Complete them, then submit one copy. The daily-profit model is provided and must not be edited.

Several questions in the notebook are marked *think about* or *be ready to say aloud*. These are not written up — the TA asks them at the checkpoints.

Aim to reach Checkpoint 1 at about **minute 65** and Checkpoint 2 at about **minute 105**, leaving the last ten minutes for restart-and-run-all and upload.

| Section | Active time | Main result | Written response |
|---|---:|---|:--:|
| A1: the integral at four sample sizes | 10 min | The average settles near 1/3 | — |
| A2: 200 repeated estimates | 8 min | Spread matches sigma_h / sqrt(n) | 1 |
| A3: coverage of 200 intervals | 7 min | About 95% contain the true value | 1 |
| B: define the decision | 5 min | Bad day defined before simulating | 1 |
| C: read the model, controlled cost check | 10 min | Only the cost changed | 1 |
| D: 1,000 days per case | 12 min | Profit summary for both cases | — |
| E: bad-day risk | 4 min | Probability of a loss | — |
| F: interval, café check, stability | 14 min | CI, two histograms, 1/sqrt(n) rate | 2 |
| G: recommendation and AI statement | 13 min | Evidence-based decision | 2 |

## Part A: How Much Can You Trust One Simulated Number?

By the end of today you hand the manager a single number. First find out how much such a number moves when the same experiment is run again. You cannot learn that from the café model, because nobody knows its true answer — so practise on the integral of x² from 0 to 1, whose exact value is 1/3.

**A1 — one growing experiment.** Use a continuing generator seeded 211 to estimate the integral at n = 10, 100, 1,000 and 10,000, then plot it. With more draws the average tends to settle near 1/3, but the error need not fall at every step. Nothing to write up.

**A2 — repeat the whole experiment.** Make 200 estimates at n = 100 and 200 more at n = 400. The Central Limit Theorem predicts their spread exactly: sigma_h = sqrt(4/45) = 0.29814, so the SDs should be about **0.02981** and **0.01491**. *Write two or three sentences* comparing what you observed with the prediction, and saying by what factor the SD changed against the factor predicted.

**A3 — one coverage check.** A 95% interval is estimate ± 1.96 × SE, using the sample SD because sigma_h is unknown in real problems. Count how many of the 200 intervals at n = 100 contain 1/3. *Write one or two sentences* giving the coverage and saying which is random — the interval, or the value 1/3.

## Part B: Define the Decision

The manager is considering a matcha promotion. It may raise demand and spending, but adds a campaign cost and may change risk. *Write two or three sentences* saying what counts as a bad day and why that must be fixed before simulating, and which inputs are uncertain rather than controlled. Save the judgement itself for Part G.

## Part C: The Provided Daily-Profit Model

The model draws demand, then one spend per customer, and returns

    profit = total spending − variable cost × demand − fixed cost − promotion cost

Run the five-day check. Nothing to write up, but **be ready to say aloud** why the spending draw uses `size=demand` and why demand must be an integer, why the generator is passed into the function, and which quantities are random.

Complete the controlled check for promotion costs 0, 70 and 300, each from check seed 212 so demand and spending are unchanged. *Write one or two sentences* on what changed and why the repeated seed isolates the cost.

## Part D: Run Many Replications

With seed 211, simulate **1,000 days per case**. Build the 2,000-row DataFrame with columns `replication`, `case`, `profit`, and report the mean, SD, minimum and maximum for each case. Nothing to write up; the discussion questions are for the checkpoint.

### Checkpoint 1 — About Minute 65 (1 of 3 points)

Show the TA Parts A–D: the A1 table and plot, the A2 comparison and histogram, the A3 coverage table, your four written responses so far, and the profit DataFrame with its summary. Be ready to answer any of the three model-reading questions, or to say why one simulated day is not a decision.

## Part E: Bad-Day Probability

A bad day means `profit < 0`. Estimate its probability in each case by averaging zero-one indicators, since `E[1_A] = P(A)`. Nothing to write up.

## Part F: Applying the Interval, and the Convergence Rate

For each case compute a 95% interval for **expected daily profit**: mean ± 1.96 × sample SD / sqrt(n). The interval is about the mean, not the range of individual days. Then repeat the experiment at 100, 1,000 and 10,000 replications from the same seed — these rows are nested views of one stream, not independent checks.

**Does any of this apply to the café?** The provided cells rerun the full 1,000-replication promotion experiment 200 times, so you can see the 200 answers you might have reported. *Write two or three sentences* explaining to the manager why the histogram of individual daily profits is wide while the histogram of mean profit is narrow, and whether the spread of the 200 means matches the predicted SE.

**The rate.** Chapter 6 says Monte Carlo error is O(n^(-1/2)), so 100 times the replications should give about 10 times the precision. *Write one or two sentences* giving the two width ratios from your table and one reason they are not exactly 10.

## Part G: Recommend a Decision

Write a short manager recommendation using estimated expected profit, bad-day probability, the confidence intervals, and one model limitation. Include your AI-use statement.

### Checkpoint 2 — About Minute 105 (final submission)

Show Parts E–G, the recommendation and the AI-use statement to the TA. Save as `Lab04_StudentID.ipynb` (for example `Lab04_6812345.ipynb`), restart the kernel, run all cells top to bottom, check for errors, save, and upload the single notebook to the **Lab 04** Google Classroom assignment before leaving.

## Optional: If You Finish Early

After Checkpoint 2 you may try the antithetic-variables exercise at the end of the notebook: the same integral as Part A, estimated by pairing each U with 1 − U. It is not assessed.
