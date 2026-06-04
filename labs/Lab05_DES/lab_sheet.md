# Lab 5: Discrete-Event Simulation of a Coffee Shop Queue

## Theme

Discrete-event simulation focuses on changes that happen at event times.

In this lab, you will simulate a single-barista coffee shop queue using arrival and service-completion logic. You will compare calm, normal, rush, and overloaded scenarios.

## Part 0: Setup

Open `starter.ipynb` in this folder and run the imports.

Use one server:

```text
server = one barista
queue discipline = first come, first served
```

## Part A: Event Logic

The two core events are:

| Event | Meaning |
|---|---|
| Arrival | customer enters the system |
| Departure | customer finishes service and leaves |

For each customer, calculate:

```text
arrival_time
service_time
service_start
service_end
waiting_time
time_in_system
```

Answer:

1. Which event changes queue length?
2. Which event frees the barista?
3. Why does the next customer depend on the previous service end time?

## Part B: Build an M/M/1 Queue

Use exponential interarrival times and exponential service times.

```text
interarrival time ~ exponential(arrival rate)
service time ~ exponential(service rate)
```

Create a simulation function that returns a DataFrame with:

```text
customer, arrival, service, start, end, wait, time_in_system
```

## Part C: Queue Output Measures

For one scenario, calculate:

- average waiting time
- longest waiting time
- average time in system
- server utilisation estimate
- maximum queue length

Create at least one plot of queue behaviour.

## Part D: Scenario Comparison

Compare four scenarios:

| Scenario | Arrival rate | Service rate |
|---|---:|---:|
| Calm | 4 | 8 |
| Normal | 6 | 8 |
| Rush | 7.5 | 8 |
| Overloaded | 9 | 8 |

Run the same number of customers for each scenario.

Complete:

| Scenario | Average wait | Longest wait | Maximum queue length | Comment |
|---|---:|---:|---:|---|
| Calm | | | | |
| Normal | | | | |
| Rush | | | | |
| Overloaded | | | | |

## Part E: Manager Challenge

The manager wants to reduce waiting time during rush periods.

Test one possible change:

- faster service rate
- lower arrival rate during peak time
- second preparation station
- simpler menu during rush

Compare the rush scenario before and after your change.

## Checkpoint Submission

Submit:

1. completed notebook
2. scenario comparison table
3. queue plot
4. manager challenge result
5. recommendation
6. AI use statement

## Reflection Questions

Write 150-200 words:

1. What makes this a discrete-event simulation?
2. What happened as arrival rate approached service rate?
3. Which output measure was most useful?
4. What assumption is most unrealistic?
5. Include an AI use statement.
