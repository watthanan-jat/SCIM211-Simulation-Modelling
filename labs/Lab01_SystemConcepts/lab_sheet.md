# Lab 1: From Real System to Simulation Model

## Purpose

In this lab, you will move from a real-world coffee shop system to a small deterministic queue model. You will review basic Python tools, identify simulation components, compare simulation worldviews, and implement simple queue calculations.

This lab is the first step in the semester-long Coffee Shop Simulation Project.

## Learning Outcomes

By the end of this lab, you should be able to:

- Use basic `numpy`, `pandas`, and `matplotlib` commands.
- Work with Python lists, arrays, DataFrames, and simple plots.
- Identify entities, resources, attributes, activities, events, and state variables in a coffee shop system.
- Explain three simulation worldviews: event scheduling, process interaction, and activity scanning.
- Manually calculate a small deterministic single-server queue.
- Implement service start time, service end time, and waiting time in Python.
- Investigate how one long service time affects later customers.

## 2-Hour Timing Plan

| Time | Activity |
|---:|---|
| 0-10 min | Lab briefing and Coffee Shop Simulation Project context |
| 10-30 min | Python warm-up: lists, arrays, DataFrames, and plots |
| 30-50 min | Coffee shop system components |
| 50-70 min | Simulation worldviews and comparison |
| 70-95 min | Manual deterministic queue calculation |
| 95-115 min | Python queue implementation and long-service investigation |
| 115-120 min | Checkpoint submission and reflection |

## Part A: Python Warm-Up

Open `starter.ipynb` and complete the warm-up TODO cells.

You will review:

- Python lists for storing customer names or arrival times.
- `numpy` arrays for numerical calculations.
- `pandas` DataFrames for tabular customer records.
- Simple `matplotlib` plots for viewing arrival, service, or waiting-time patterns.

Do not worry about advanced programming style in this lab. Focus on making the data clear and checking that each calculation makes sense.

## Part B: Coffee Shop System Components

Consider a small coffee shop with one counter and one barista. Customers arrive, wait if the barista is busy, receive service, and leave.

Identify the following:

| Component | Meaning in Simulation | Coffee Shop Example |
|---|---|---|
| Entity | Object that moves through the system | Customer |
| Resource | Limited item or worker needed for service | Barista |
| Attribute | Value attached to an entity | Arrival time, service time, drink type |
| Activity | Process that takes time | Making a drink |
| Event | Instant that changes the system | Customer arrival, service start, service end |
| State variable | Value describing the system at a time | Queue length, barista status, number served |

In your report, add one more example for each component.

## Part C: Simulation Worldviews

Simulation worldviews describe different ways to organise the logic of a simulation.

### Event Scheduling

The simulation advances from one event time to the next. The model keeps an event list and updates the system when an event occurs.

Coffee shop example: process the next customer arrival or service completion, whichever happens first.

### Process Interaction

Each entity follows a process. A customer process might include arrive, wait, receive service, and leave.

Coffee shop example: each customer follows their own path through the shop.

### Activity Scanning

The simulation repeatedly checks whether activities can start or finish based on system conditions.

Coffee shop example: check whether a customer is waiting and the barista is free, then start service.

### Comparison Table

| Worldview | Main Idea | Strength | Challenge | Coffee Shop Focus |
|---|---|---|---|---|
| Event scheduling | Move from event to event | Efficient for event-driven systems | Event list logic can be detailed | Arrival and service-completion events |
| Process interaction | Describe each entity's journey | Natural for customer-flow models | Requires process control logic | Customer path through waiting and service |
| Activity scanning | Check conditions for activities | Clear link to rules and conditions | Can be inefficient if many checks are needed | Whether service can start |

## Part D: Manual Deterministic Coffee Shop Queue

Use the following deterministic customer data:

| Customer | Arrival Time | Service Time |
|---:|---:|---:|
| 1 | 0 | 3 |
| 2 | 1 | 2 |
| 3 | 2 | 4 |
| 4 | 5 | 2 |
| 5 | 6 | 3 |

Assume:

- There is one barista.
- Service is first-come, first-served.
- A customer starts service immediately if the barista is free.
- All times are in minutes.

For each customer, calculate:

- Service start time
- Service end time
- Waiting time

Use these relationships:

```text
service_start = max(arrival_time, previous_service_end)
service_end = service_start + service_time
waiting_time = service_start - arrival_time
```

Complete the manual table in your report before coding.

## Part E: Python Queue Implementation

In `starter.ipynb`, implement the same calculations using Python.

Your code should calculate:

- `service_start`
- `service_end`
- `waiting_time`

Use a loop so that each customer's service start depends on the previous customer's service end.

## Part F: Long-Service Investigation

Change the first customer's service time from `3` to a longer value, such as `8`.

Investigate:

- How does this change the waiting time of later customers?
- Which customer is affected the most?
- Does the effect disappear quickly, or does it continue through the queue?
- What does this show about congestion in a queue?

Use a DataFrame and at least one simple plot to support your answer.

## Checkpoint Submission

Submit the following at the end of the lab:

- Completed `starter.ipynb` with TODO cells filled in.
- Completed `report_template.md`.
- A short AI use statement, even if you did not use AI.

This is a checkpoint submission. It is intended to show progress, not a polished final project.

## Reflection Questions

Answer these in `report_template.md`:

1. What is one important difference between a real coffee shop and your simplified model?
2. Which simulation worldview feels most natural for the coffee shop system? Why?
3. Why does the service time of one early customer affect later customers?
4. What state variables would you track in a larger coffee shop simulation?
5. What would need to change if the coffee shop had two baristas?

## AI Use Statement

Include a short statement in your report:

- Name the AI tool used, if any.
- Describe what you used it for.
- State what you checked or changed yourself.

Example:

```text
AI use statement: I used [tool name] to help debug a plotting error. I checked the DataFrame calculations myself and wrote the interpretation in my own words.
```

If you did not use AI, write:

```text
AI use statement: I did not use AI tools for this lab.
```
