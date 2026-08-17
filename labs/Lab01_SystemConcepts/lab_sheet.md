# Lab 1: From Real System to Simulation Model

## Theme

Before you simulate, make sure you can answer:
1. What system are we modelling?
2. What state variables matter?
3. What events change the state?
4. Which simulation worldview should we use?
5. How do we represent the model in Python?

## How to Use This Lab

Use the notebook for both code and written answers. This sheet provides supporting instructions and explanations.

Do not try to make the code perfect on the first attempt. The purpose is to see how queue logic works, make small mistakes, diagnose them, and then connect the Python calculation back to the system description.

Recommended workflow:

1. Read the short explanation before each task.
2. Predict what should happen before running code.
3. Run the code or complete the TODO.
4. Compare the result with your prediction.
5. If the result is different, write down what changed and why.

Keep notes on failed attempts. In simulation modelling, a wrong first result is often useful because it reveals which part of the system logic was misunderstood.

## Part 0: Setup

Open:

```text
labs/Lab01_SystemConcepts/starter.ipynb
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
manual_df["start"]
manual_df["end"]
manual_df["wait"]
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

Show the completed notebook to the TA during the lab. After the TA checkpoint, save the notebook as:

```text
Lab01_StudentID.ipynb
```

For example, student ID 6812345 should submit `Lab01_6812345.ipynb`.

Upload the completed notebook to the **Lab 01** assignment in Google Classroom before leaving the lab. The notebook must include:

1. completed Python code and output
2. Python warm-up interpretations
3. system-component and worldview tables
4. manual-simulation results
5. original and slow-first-customer results
6. 150-200 word reflection
7. AI use statement

Before uploading, restart the kernel, run all cells from top to bottom, check that there are no errors, and save the notebook.

## Reflection Questions

Write 150-200 words:
1. Which simulation worldview feels most natural to you and why?
2. Which worldview is probably best for coding a discrete-event simulation?
3. What was the most important state variable in today's model?
4. What assumption in today's model is unrealistic?

Complete the separate AI Use Statement section in the notebook.
