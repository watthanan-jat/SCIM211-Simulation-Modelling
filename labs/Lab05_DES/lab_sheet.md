# Lab 5: Discrete-Event Simulation of an M/M/1 Coffee Shop Queue

## Theme

Discrete-event simulation for a single-server coffee shop queue.

## Scenario

The coffee shop manager wants to understand waiting time under calm, normal, rush, and overloaded conditions. You will build a small M/M/1 queue simulation and compare scenarios.

## 2-Hour Timing Plan

| Time | Activity |
|---:|---|
| 0-10 min | Recap Monte Carlo and queue motivation |
| 10-30 min | Instructor demo: DES event logic |
| 30-50 min | Guided task: trace a small event sequence |
| 50-85 min | Coding task: M/M/1 simulation |
| 85-105 min | Scenario comparison |
| 105-115 min | Manager challenge |
| 115-120 min | Checkpoint submission |

## Instructor Demo

The instructor will trace arrival and departure events and show how the event clock, queue length, and server status change over time.

## Guided Task

Manually trace a short queue with three customers before completing the notebook.

## Coding Task

Complete the TODO cells to:

- Generate exponential interarrival and service times.
- Calculate arrival times, service start, service end, and waiting time.
- Track queue length over time.
- Plot queue length for one scenario.

## Investigation

Compare calm, normal, rush, and overloaded scenarios by changing arrival and service rates.

## Manager Challenge

Recommend one operational action for the manager, such as adding staff during rush periods or reducing service time for complex drinks.

## Checkpoint Submission

Submit the notebook, report, scenario table, queue plot, manager recommendation, and AI use statement.

## Reflection Questions

1. What makes this a discrete-event simulation?
2. What changes when the system becomes overloaded?
3. Which output measure is most useful for the manager?
4. What assumptions make the M/M/1 model simple?
5. What would change if there were two baristas?

## AI Use Statement

State whether you used AI, what you used it for, and what you checked yourself.
