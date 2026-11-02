# Lab 7: Input Modelling, Validation, and a Final Recommendation

## Theme

Labs 5 and 6 built simulators and checked them against theory. In this lab you ask whether a simulation is credible enough to support a decision. You check observed service-time data, fit and test an exponential model, verify the code against an exact benchmark, run replications with confidence intervals and a stopping rule, test how sensitive the conclusions are to the input model, and write a final recommendation for the coffee-shop manager.

The hints in brackets, such as (Chapter 9), tell you where to look in the lecture notes.

## Lab Settings

Use these settings throughout. They are defined in the first code cell of `starter.ipynb`.

```text
data         = data/service_times.csv   (20 observed service times, minutes)
seed         = 211 for the fitted sample; replication r uses seed 211 + r
day          = arrivals accepted for 480 minutes; everyone who arrived is served
arrivals     = exponential gaps, 12 customers per hour
server       = one barista, first come first served
replications = 30 days
```

The notebook finds the data file whether Jupyter starts at the repository root or in the lab folder. Use the 20-row file in `data/`; an assert stops you if an older copy is used.

## Part A: Check the Observed Input Data (Chapter 9)

Load the data and compute the count, mean, sample SD, minimum, median, maximum and coefficient of variation (SD / mean). The provided code checks that all times are positive and draws a histogram.

Write short answers in the notebook:

1. Describe a typical service time, the spread, and the shape of the histogram.
2. An exponential distribution always has coefficient of variation 1. What does the observed value suggest before any fitting?

## Part B: Fit an Exponential Distribution and Check It (Chapter 9)

1. Fit the exponential model: mean $=\bar x$, rate $\hat\lambda=1/\bar x$ (the maximum-likelihood estimate).
2. Generate 10,000 fitted service times with seed 211. The provided code compares histograms and the observed ECDF with the fitted CDF.
3. Chi-square goodness-of-fit test: use 4 bins with probability $\tfrac14$ each under the fitted model, so each expected count is 5. The inner bin edges are the fitted quartiles $x_q=-\bar x\ln(1-q)$ for $q=\tfrac14,\tfrac12,\tfrac34$. Compute $\chi^2=\sum_i(O_i-E_i)^2/E_i$. One parameter is estimated, so $\mathrm{df}=4-1-1=2$ and the 5% critical value is 5.991.

Write short answers in the notebook:

1. Judge the exponential fit using the histogram, the ECDF, the coefficient of variation and the chi-square result. Where exactly does it fit poorly?
2. Why does matching the sample mean not validate the exponential model?
3. With only 20 observations and 4 bins, how much weight should one test result carry?

## Part C: A One-Day Model (Chapter 7, Lab 5)

Complete `simulate_day(service_model, seed)`:

1. generate arrival times by adding exponential gaps (mean $60/12=5$ minutes) until minute 480;
2. generate service times from the chosen model: `"exponential"` (the Part B fit) or `"empirical"` (resampling the 20 observed values with replacement, which is provided; Chapter 9);
3. apply the first-come-first-served recursion from Lab 5.

All arrival times are generated before any service time, so two service models run with the same seed see the same customers. The provided code returns the average wait, the longest wait, the maximum number of customers already in line when someone arrives, and the number served. Run one day with the exponential model and seed 212.

Write a short answer in the notebook:

1. This one day had an average wait of about 3.7 minutes. Is that what a typical day looks like? How would you find out?

## Part D: Replications, Verification, and a Stopping Rule

1. Run 30 days with the exponential model; day $r$ uses seed $211+r$.
2. Complete `confidence_interval`: mean, sample SD, and half-width $1.96\,s/\sqrt n$ (Chapter 9). The provided code builds the interval table and histograms of the daily average wait and the longest wait.
3. **Verification (Chapter 10; $W_q$ from Chapter 7).** With exponential service the model is an M/M/1 queue with $\lambda=0.2$ per minute and $\mu=1/\bar x$. Compute $\rho=\lambda/\mu$ and $W_q=\rho/(\mu-\lambda)$ in minutes. The provided code checks whether $W_q$ lies inside the interval for the mean daily average wait.
4. **Stopping rule (Chapter 9).** Compute the number of days needed for a 95% margin below $d=0.1$ minutes: $k\ge(1.96\,s/d)^2$ with $s$ from the 30 days. The provided code runs that many days and reports the achieved margin.

Write short answers in the notebook:

1. Which output is the most uncertain relative to its mean? What does the interval for the average wait say that the single day in Part C could not?
2. Does the model pass the verification check? Explain what a pass does and does not show.
3. If the exponential input model is wrong, will running the stopping-rule number of days fix that?

## Part E: Sensitivity to the Input Model (Validation, Chapter 10)

Sensitivity analysis is a validation check. Rerun the same 30 days (seeds $211+r$) with the empirical service model. The provided code compares the intervals for the average wait, longest wait and maximum queue under both models, and gives a paired interval for the difference in average wait (Chapter 9).

Write short answers in the notebook:

1. How much does the choice of input model change the average wait and the longest wait? Which model would you trust more for this shop, and what is the main weakness of each?
2. Is the model credible enough to support a staffing recommendation? Name the evidence for and against.
3. Why does the input model change the average wait so much when both models have the same mean service time?

## Recommendation, Reflection, and AI Use

In the notebook, write:

1. **Manager recommendation.** The manager asks whether one barista is enough on a typical day. Include a specific decision, numerical results with confidence intervals, a comment on the service-time model (fit and sensitivity), one limitation that could change the conclusion, and one practical next action.
2. **Reflection:** the difference between verification and validation and the evidence of each you produced; why replications are better than one day; what the sensitivity analysis added.
3. **AI-use statement:** the tool, how it was used, and how you checked its output, or a statement that AI was not used.

A recommendation without uncertainty sounds more confident than the evidence allows. A recommendation without a practical action is not useful for decision-making.

## Final Submission

Lab 7 is assessed from the submitted notebook only. Complete Parts A-E, the recommendation, the reflection, and the AI-use statement. Then:

1. save the notebook as `Lab07_StudentID.ipynb`, for example `Lab07_6900789.ipynb`;
2. restart the kernel and run all cells from top to bottom;
3. check that there are no errors;
4. save the notebook; and
5. upload the single completed `.ipynb` file to the **Lab 07** assignment in Google Classroom.

The notebook must include:

1. completed and executed Python code;
2. all requested tables and plots;
3. the written answers for Parts A-E (every **ANSWER:** box);
4. the manager recommendation and reflection; and
5. the AI-use statement.
