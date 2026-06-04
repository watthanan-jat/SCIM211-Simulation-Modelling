# Lab 1: From Real System to Simulation Model

## Theme

Before you simulate, make sure you can answer:
1. What system are we modelling?
2. What state variables matter?
3. What events change the state?
4. Which simulation worldview should we use?
5. How do we represent the model in Python?

## Part 0: Setup

Open:

```text
notebooks/Lab01_SystemConcepts.ipynb
```

Run:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

If libraries do not load:

```bash
pip install -r requirements.txt
```

## Part A: Python Warm-up for Simulation

The three main libraries for this lab are:

- `numpy` = random numbers, arrays, numerical calculations
- `pandas` = tables and data frames
- `matplotlib` = plots and visualisation

Use this data:

```python
arrival = [1, 2, 5, 6, 10]
service = [3, 4, 2, 3, 2]
```

### A1. Numerical summaries

Compute:

```python
np.mean(service)
np.max(service)
np.min(service)
np.cumsum(service)
```

Answer:
1. What is the mean service time?
2. Which customer has the longest service time?
3. What does cumulative sum mean here?

### A2. Create a DataFrame

Create:

```python
df = pd.DataFrame({
    "customer": [1, 2, 3, 4, 5],
    "arrival": arrival,
    "service": service
})
df
```

Answer:
1. Why is a DataFrame useful for simulation output?
2. What does each row represent?
3. What does each column represent?

### A3. Plot arrival times

Create:

```python
plt.plot(df["customer"], df["arrival"], marker="o")
plt.xlabel("Customer")
plt.ylabel("Arrival time")
plt.title("Customer arrival times")
plt.show()
```

Answer:

What does this plot tell us?

## Part B: Coffee Shop as a System

Scenario:

A small coffee shop has one barista. Customers arrive, wait if the barista is busy, receive service, and leave.

Complete this table:

| Concept | Coffee Shop Example |
|---|---|
| Entity | |
| Temporary entity | |
| Permanent entity | |
| Resource | |
| Activity | |
| Event 1 | |
| Event 2 | |
| State variable 1 | |
| State variable 2 | |
| Input randomness 1 | |
| Input randomness 2 | |
| Output measure 1 | |
| Output measure 2 | |

## Part C: Simulation Worldviews

There are different ways to describe the same simulation model.

### C1. Event-Scheduling Worldview

Think like a clock manager.

"What is the next event, and how does it change the state?"

Coffee shop:

- Arrival event
- Departure event
- Next event = earliest scheduled event

Best for discrete-event simulation coding.

| Event | What changes? |
|---|---|
| Arrival | customer enters; queue/server state may change |
| Departure | customer leaves; next service may start |

Pseudocode:

```text
Set current time t = 0
Schedule first arrival
While shop is open:
    Choose the next event
    Move clock to that event time
    Update system state
    Schedule future events
```

Answer:

Why is this efficient?

### C2. Process-Interaction Worldview

Think like a customer story.

"What happens to one customer from arrival to departure?"

Coffee shop:

```text
Customer arrives -> waits -> receives service -> leaves
```

Best for intuitive modelling.

Answer:

Why is this easier to understand than event scheduling?

### C3. Activity-Scanning Worldview

Think like a rule checker.

"At each time step, what activities can happen?"

Coffee shop:

- If a customer arrives, add to queue.
- If barista is free and queue is non-empty, start service.
- If service is complete, customer leaves.

Best for simple time-step simulations, but less efficient.

Answer:

Why can this be inefficient?

### C4. Compare the three views

Complete this table:

| Worldview | Main idea | Coffee-shop interpretation | Strength | Weakness |
|---|---|---|---|---|
| Event scheduling | | | | |
| Process interaction | | | | |
| Activity scanning | | | | |

## Part D: Manual Simulation

Use this table:

| Customer | Arrival time | Service time |
|---:|---:|---:|
| 1 | 1 | 3 |
| 2 | 2 | 4 |
| 3 | 5 | 2 |
| 4 | 6 | 3 |
| 5 | 10 | 2 |

Complete:

| Customer | Arrival | Service starts | Service ends | Waiting time | Barista status after arrival |
|---:|---:|---:|---:|---:|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Hints:

```text
service_start = max(arrival_time, previous_service_end)
service_end = service_start + service_time
waiting_time = service_start - arrival_time
```

Answer:
1. Which customer waited longest?
2. What is the average waiting time?
3. When was the barista idle?
4. When was the queue longest?

## Part E: Python Implementation

Complete the notebook code.

The code should produce a DataFrame with:

```text
customer, arrival, service, start, end, wait
```

Expected columns:

```python
df["start"]
df["end"]
df["wait"]
```

## Part F: Investigation

Change the first service time from 3 to 10:

```python
service = [10, 4, 2, 3, 2]
```

Repeat the simulation.

Compare:

| Case | Average waiting time | Longest waiting time |
|---|---:|---:|
| Original | | |
| Slow first customer | | |

Answer:
1. Why does one slow service affect later customers?
2. What is a bottleneck?
3. How might a manager reduce this problem?

## Checkpoint Submission

Submit:
1. completed notebook
2. completed worldview comparison table
3. original average waiting time
4. new average waiting time after slow first customer
5. reflection in `reports/Lab01_Report.md`

## Reflection Questions

Write 150-200 words:
1. Which simulation worldview feels most natural to you and why?
2. Which worldview is probably best for coding a discrete-event simulation?
3. What was the most important state variable in today's model?
4. What assumption in today's model is unrealistic?
5. Include an AI use statement.
