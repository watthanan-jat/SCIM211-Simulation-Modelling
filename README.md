# SCIM211 Simulation Modelling

Welcome to **SCIM211 Simulation Modelling**.

This repository is your home base for the course. You will find the weekly schedule, lab sheets, starter notebooks, report templates, data files, and Python code stubs here.

The course is built around one continuing project: the **Coffee Shop Simulation Project**. We start with a simple real-world question, such as "How long do customers wait?", then gradually add randomness, queues, decisions, data analysis, and recommendations.

## What This Course Is About

Simulation is a way to study systems that are difficult to solve exactly. Instead of only writing formulas, we build a model, run experiments, and use the results to understand what might happen.

In this course, you will practise how to:

- Turn a real situation into a simulation model.
- Use probability and random numbers in a careful way.
- Write small Python programs for simulation.
- Analyse waiting time, profit, customer behaviour, and uncertainty.
- Explain your assumptions and results clearly.

You do not need to be a perfect programmer before starting. The labs are designed to build skills step by step.

## Course At A Glance

| Item | Details |
|---|---|
| Course | SCIM211 Simulation Modelling |
| Students | Second-year Industrial Mathematics and Data Science |
| Duration | 15 weeks |
| Theory class | 2 hours every week |
| Lab class | 2 hours every even week |
| Main project | Coffee Shop Simulation Project |
| Main tools | Python, NumPy, pandas, matplotlib, SciPy, Jupyter |

## Start Here

If this is your first time opening the repository, start with these pages:

| Page | What You Will Find |
|---|---|
| [Syllabus](syllabus.md) | What the course covers and what you should be able to do by the end |
| [Schedule](schedule.md) | What happens each week |
| [Assessment](assessment.md) | How course work and project work are handled |
| [AI Policy](ai_policy.md) | How to use AI tools responsibly in this course |

For lab work, go to the relevant folder in [`labs/`](labs/).

## Coffee Shop Simulation Project

Throughout the semester, we will use a coffee shop as our main example. This gives us one familiar system that can grow with the course.

You will model questions such as:

- When do customers arrive?
- How long does each drink take to prepare?
- How long do customers wait?
- What happens during rush hour?
- Should the shop run a matcha promotion?
- How can we describe customer loyalty?
- How confident are we in our simulation results?

Each lab adds one new piece to the project. By the end, you should have a clearer sense of how a simulation study is built from data, assumptions, code, output analysis, and judgement.

## Lab Pathway

| Lab | Topic | What You Will Do |
|---:|---|---|
| [Lab 1](labs/Lab01_SystemConcepts/lab_sheet.md) | From Real System to Simulation Model | Describe the coffee shop system and calculate a first simple queue |
| [Lab 2](labs/Lab02_RandomNumbers/lab_sheet.md) | Random Numbers and Interarrival Times | Generate random arrivals and inspect random-number quality |
| [Lab 3](labs/Lab03_RandomVariables/lab_sheet.md) | Random Variables and Drink Service Times | Simulate drink orders and drink-dependent service times |
| [Lab 4](labs/Lab04_MonteCarlo/lab_sheet.md) | Monte Carlo Profit and Promotion Decision | Estimate profit, risk, and whether a promotion is worthwhile |
| [Lab 5](labs/Lab05_DES/lab_sheet.md) | Discrete-Event Simulation of an M/M/1 Queue | Simulate calm, normal, rush, and overloaded queue scenarios |
| [Lab 6](labs/Lab06_MarkovChains/lab_sheet.md) | Markov Chains and Customer Loyalty | Model how customers move between loyalty states |
| [Lab 7](labs/Lab07_Validation/lab_sheet.md) | Validation and Final Recommendation | Use data, replications, confidence intervals, and a final recommendation |

## Weekly Roadmap

| Week | Focus | Lab |
|---:|---|---|
| 1 | Introduction | - |
| 2 | System concepts | Lab 1 |
| 3 | Probability review | - |
| 4 | Random number generation | Lab 2 |
| 5 | Simulating random variables I | - |
| 6 | Simulating random variables II | Lab 3 |
| 7 | Monte Carlo I | - |
| 8 | Monte Carlo II | Lab 4 |
| 9 | Midterm/review | - |
| 10 | Discrete-event simulation I | Lab 5 |
| 11 | Discrete-event simulation II | - |
| 12 | Markov chains I | Lab 6 |
| 13 | Markov chains II | - |
| 14 | Input/output analysis | Lab 7 |
| 15 | Variance reduction, validation, and project wrap-up | - |

## How To Use Each Lab

Each lab folder contains:

- `lab_sheet.md`: what to do during the lab
- `starter.ipynb`: a Jupyter notebook with TODO cells
- `report_template.md`: a short report structure for your answers

Recommended workflow:

1. Read the lab sheet first.
2. Open the starter notebook.
3. Complete the TODO cells during the lab.
4. Use the report template to explain your results.
5. Add your AI use statement before submitting.

The notebooks are intentionally not full solutions. They are there to guide your work while still leaving the modelling and coding decisions to you.

## Repository Map

| Folder | What It Contains |
|---|---|
| `lectures/` | Lecture materials |
| `exercises/` | Practice questions and short activities |
| `labs/` | Lab sheets, starter notebooks, and report templates |
| `data/` | Data files used in labs and validation |
| `src/` | Python function stubs for future implementation |
| `tests/` | Placeholder tests for source-code functions |
| `.github/workflows/` | Automated test workflow |

## A Note On Learning

Simulation is not only about producing numbers. A good simulation answer should explain:

- What system was modelled
- What assumptions were made
- What random behaviour was included
- What output was measured
- What the results suggest
- What limitations remain

If your code runs but you cannot explain the model, the work is not finished yet. If your explanation is clear, even a simple model can be valuable.
