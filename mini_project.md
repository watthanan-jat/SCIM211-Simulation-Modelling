# Mini Project: Coffee Shop Simulation Decision Challenge

## Project Overview

Build a reusable simulation model of a small coffee shop, then use it to support an operational decision.

Your model should not be hard-coded for one fixed case. It should be flexible enough to test new situations by changing parameters such as arrival rate, service speed, drink mix, staffing, or promotion assumptions.

The central question is:

> Based on simulation evidence, which operating policy should the coffee shop choose, and why?

## Core System

Your coffee shop model should include:

- customer arrivals
- drink choices
- drink-dependent service times
- one or more baristas
- waiting time and queue length
- server utilisation
- number of customers served
- daily profit or service-quality output
- optional customer loyalty state

## Required Policy Comparison

Compare a baseline system with at least one improvement policy.

Possible policies:

- add one barista during rush hour
- simplify the menu during rush hour
- run a matcha promotion
- improve preparation speed
- introduce a loyalty card
- add a pre-ordering or pickup option
- limit queue length or model customers leaving

Choose a policy that creates a real trade-off. For example, adding a barista may reduce waiting time but increase staffing cost.

## Required Methods

Your project must use ideas from the course labs and lecture notes.

| Course idea | Project requirement |
|---|---|
| System concepts | Define entities, resources, events, activities, state variables, inputs, and outputs. |
| Random numbers | Use fixed seeds and explain reproducibility. |
| Random variables | Generate arrivals, service times, drink choices, or demand using suitable distributions. |
| Monte Carlo | Estimate at least one expected value, probability, or integral-based quantity. |
| Discrete-event simulation | Simulate the queue and track event-based system behaviour. |
| Markov chains | Include a small loyalty or repeat-visit model, or justify why it is not needed. |
| Input/output analysis | Run multiple replications and report confidence intervals. |
| Validation | Compare assumptions with data, plots, or reasoned checks. |

## Required Outputs

Report at least these outputs:

- average waiting time
- maximum waiting time
- maximum queue length
- server utilisation
- number of customers served
- expected profit or bad-day probability
- 95% confidence interval for at least one key output

You may include additional outputs if they support your decision.

## Unseen Stress Test

Near the end of the course, each group will receive one unseen scenario. You will modify your model, run the simulation, and produce a short decision note.

Possible stress-test scenarios:

- arrival rate increases by 30%
- matcha demand doubles
- service times increase by 20%
- one barista is unavailable for the first hour
- a promotion increases demand but adds preparation time
- customers leave if waiting time exceeds 10 minutes
- fixed daily cost increases
- service-time data contains one unusually long observation

Your stress-test response should answer:

1. What changed in the model?
2. What outputs changed?
3. How many replications did you run?
4. What confidence interval or uncertainty measure did you use?
5. What recommendation would you make?
6. What limitation should the manager remember?

## Deliverables

Submit:

1. `project_notebook.ipynb`
2. `project_report.md` or PDF, about 6-10 pages
3. 5-minute presentation
4. one-page stress-test response
5. AI use statement

## Suggested Report Structure

1. Decision question
2. System description
3. Inputs and assumptions
4. Random-variable generation
5. Discrete-event queue model
6. Monte Carlo replications
7. Markov chain or loyalty component
8. Output analysis and confidence intervals
9. Baseline versus policy comparison
10. Stress-test response
11. Recommendation and limitations
12. AI use statement

## Grading Guide

| Component | Weight |
|---|---:|
| Model structure and assumptions | 20% |
| Correct simulation implementation | 25% |
| Statistical output analysis | 20% |
| Stress-test response | 15% |
| Recommendation and communication | 15% |
| Reproducibility and AI statement | 5% |

## What Makes a Strong Project

A strong project:

- has a clear decision question
- uses a model that can be changed without rewriting everything
- explains assumptions honestly
- uses enough replications for uncertainty analysis
- compares policies using both service quality and cost or risk
- gives a recommendation supported by evidence
- states limitations clearly

The goal is not to build a perfect coffee shop simulator. The goal is to show that you can design a simulation study, run experiments, interpret uncertainty, and communicate a decision.
