# Lab 5: Discrete-Event Simulation of a Coffee Shop Queue

## Theme

Labs 3 and 4 generated random service times and used replications to estimate expected values. In this lab you put those pieces together in time: you simulate a single-barista coffee shop as an M/M/1 queue, compare calm, normal, rush, and overloaded demand levels, check the simulation against M/M/1 theory, and use replications to evaluate a manager's proposal.

Chapter 7 introduced events, the event list, the M/M/1 queue, and the steady-state formulas.

## Lab Settings

Use these settings throughout. They are defined in the first code cell of `starter.ipynb`.

```text
server           = one barista
queue discipline = first come, first served (FCFS)
seed             = 211 for every single-run result in Parts B-D
customers        = 500 per simulation run
rates            = per hour; all simulated times in minutes
```

Before each scenario, predict whether the queue should stay short, grow slowly, or become unstable. After running the code, compare the output with your prediction.

## Part A: Event Logic

The two events are:

| Event | Meaning |
|---|---|
| Arrival | customer enters the system |
| Departure | customer finishes service and leaves |

**How this lab's code represents events.** The Chapter 7 pseudocode keeps an event list and repeatedly jumps the clock to the next arrival or departure. With one FCFS server there is a shortcut: customers are served in arrival order, so

```text
start[i] = max(arrival[i], end[i-1])
end[i]   = start[i] + service[i]
```

This recursion produces exactly the same arrival and departure times as the event-list algorithm. Part C rebuilds the ordered event sequence from these times to measure the queue.

Write short answers in the notebook:

1. Which event can increase queue length?
2. Which event frees the barista?
3. Why does customer `i` depend on customer `i-1`'s service end time?

## Part B: Build an M/M/1 Queue

An M/M/1 queue has exponential interarrival times (rate `lambda`), exponential service times (rate `mu`), and one FCFS server. `rng.exponential` takes the **mean** (`scale`), not the rate, so convert hourly rates to mean times in minutes:

```text
mean interarrival minutes = 60 / arrival_rate
mean service minutes      = 60 / service_rate
rho                       = arrival_rate / service_rate
```

The steady-state model exists only when `rho < 1`.

Complete `simulate_mm1` so that it returns a DataFrame with columns

```text
customer, arrival, service, start, end, wait, time_in_system
```

Generate all interarrival gaps first, then all service times, then convert the gaps to arrival times with a cumulative sum. Run the Normal scenario (arrival rate 6, service rate 8) with seed 211 and 500 customers.

### Trial Checks

Run the three diagnostic cases with seed 211 and 500 customers:

| Case | Arrival rate | Service rate | rho | Prediction |
|---|---:|---:|---:|---|
| Low load | 2 | 10 | 0.2 | most customers wait close to 0 |
| Near capacity | 7.8 | 8 | 0.975 | waiting is large and very variable from run to run |
| Overloaded | 10 | 8 | 1.25 | the queue tends to grow |

Then rerun the near-capacity case with seeds 1, 2, 3, 4, and 5 to see the run-to-run variation.

If your overloaded case looks calm, you have probably passed a **rate** where NumPy expects a **mean**. That gives mean gaps of 10 minutes and mean services of 8 minutes, which turns `rho = 1.25` into `rho = 0.8`. This is the same mean-versus-rate trap as Lab 3 Part B.

Think about the following questions. You do not need to write answers, but the TA may ask you to explain your reasoning:

1. Why does the overloaded case have no steady-state queue?
2. The five near-capacity runs use the same model. Why are their average waits so different?
3. Why must `rng.exponential` receive `60 / rate` rather than `rate`?

## Checkpoint 1: Event Logic and Queue Model (1 of 3 Points)

Target time: approximately 60 minutes into the lab.

Show your notebook to the TA after completing Parts A-B. To receive the first 1 point, your notebook must contain:

1. the three Part A responses;
2. a working `simulate_mm1` and the Normal-scenario table with the required columns; and
3. the trial-check table and the five-seed near-capacity table.

Be ready to explain the rate-to-mean conversion, the recursion `start = max(arrival, previous_end)`, and why `rho >= 1` means there is no steady-state queue. Continue with Parts C-E.

## Part C: Queue Output Measures

For the Normal scenario, complete `summarise_queue` to calculate:

- average waiting time;
- longest waiting time;
- average time in system;
- server utilisation: total service time divided by the time from the first arrival to the last departure; and
- maximum queue length (waiting customers, excluding the one in service).

The event reconstruction, sanity checks, and queue-length plot are provided. If a sanity check fails, debug the event logic before interpreting any result.

Think about the following questions:

1. The plot shows the queue repeatedly emptying and building up in bursts. Why, when `rho = 0.75 < 1`?
2. What would change if the utilisation window ended at the last arrival instead of the last departure?

## Part D: Scenario Comparison

For a stable M/M/1 queue, Chapter 7 gives the steady-state mean wait in the queue

$$
W_q=\frac{\rho}{\mu-\lambda}\ \text{hours}\qquad(\rho<1),
$$

that is, $60\rho/(\mu-\lambda)$ minutes. Complete `mm1_theory_wait`, then run the four scenarios with seed 211 and 500 customers:

| Scenario | Arrival rate | Service rate | rho |
|---|---:|---:|---:|
| Calm | 4 | 8 | 0.5 |
| Normal | 6 | 8 | 0.75 |
| Rush | 7.5 | 8 | 0.9375 |
| Overloaded | 9 | 8 | 1.125 |

The provided table reports the five output measures, the theory value `theory_wait`, and `run_hours`, the length of each run in hours. Reusing one seed in every scenario means all scenarios are driven by the same underlying random numbers (common random numbers).

Write short answers in the notebook:

1. How do the average wait, longest wait, and maximum queue length change as `rho` approaches and then exceeds 1?
2. Compare `average_wait` with `theory_wait`. In which scenario is the gap largest? Give one reason why a single 500-customer run that starts with an empty shop can differ from the steady-state value.
3. Roughly how many hours of continuous operation does each run represent? What does this mean if we want to describe a real morning rush that lasts one or two hours?

Think about the following question:

4. The overloaded run finishes and produces finite numbers. Why does that not contradict the statement that it has no steady state?

## Part E: Manager Challenge

The manager asks whether raising the rush service rate from 8 to 10 customers per hour (mean service time from 7.5 to 6 minutes) is worth it.

One run can be lucky or unlucky, so compare the two cases over **20 replications** with seeds 211 to 230, using the **same seeds for both cases**. Complete `replicate_average_wait`, which returns one average wait per seed. The provided code reports, for each case, the mean of the 20 average waits, the sample SD, the Lab 4 interval (mean ± 1.96 × SD / sqrt(20)), and the theory value, together with the mean paired reduction and the number of seeds on which the improvement helped.

Write short answers in the notebook:

1. Does the 95% interval for the rush case contain `theory_wait`? If not, does that mean the simulator is wrong? Explain what adding replications fixes and what it does not fix.
2. By how much does the improvement reduce average waiting time, and how consistent is the reduction across seeds?

Think about the following question:

3. Why is it better to use the same seeds for both cases than different seeds?

## Recommendation, Reflection, and AI Use

In the notebook, write:

1. **Manager recommendation** using the Part D and Part E evidence. State what operational change (for example, staff training, pre-preparing ingredients, a simpler rush menu, or a second preparation station) could realistically deliver the faster service rate, and one important model limitation.
2. **Reflection:** what makes this a discrete-event simulation; what happened as the arrival rate approached the service rate; which output measure was most useful; and which assumption is least realistic.
3. **AI-use statement:** the tool, how it was used, and how you checked its output, or a statement that AI was not used.

## Checkpoint 2: Final Submission

Show the completed Parts C-E, recommendation, reflection, and AI-use statement to the TA. Be prepared to answer one code question and one modelling question, for example why the rush simulation does not match $W_q$. After the final checkpoint, save the notebook as:

```text
Lab05_StudentID.ipynb
```

For example, student ID 6812345 should submit `Lab05_6812345.ipynb`.

Upload the completed notebook to the **Lab 05** assignment in Google Classroom before leaving the lab. The notebook must include:

1. completed and executed Python code;
2. all requested tables and the queue-length plot;
3. the written responses for Parts A, D, and E;
4. the manager recommendation and reflection; and
5. the AI-use statement.

Before uploading, restart the kernel, run all cells from top to bottom, check that there are no errors, and save the notebook.
