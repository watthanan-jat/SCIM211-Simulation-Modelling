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
| Audience | Second-year Industrial Mathematics and Data Science |
| Duration | 16 teaching weeks, including the Week 17 review, plus the midterm break |
| Theory class | Tuesday 10:00-12:00 |
| Lab class | Designated Wednesdays; check the timetable for changes |
| First class | Tuesday 4 August |
| Midterm week | 28 September-2 October, no class |
| Final teaching week | 23-27 November |
| Main project | Coffee Shop Simulation Project |
| Main tools | Python, NumPy, pandas, matplotlib, SciPy, Jupyter |

## Start Here

If this is your first time opening the repository, start with these pages:

| Page | What You Will Find |
|---|---|
| [Syllabus](syllabus.md) | What the course covers and what you should be able to do by the end |
| [Schedule](schedule.md) | What happens each week |
| [Assessment](assessment.md) | How course work and project work are handled |
| [Mini Project](docs/mini-project.html) | Student handout, in-browser code checker, and Week 16 Coffee Shop Simulation Hackathon |
| [Practice Exercises](exercises/index.md) | Chapter-by-chapter practice questions |
| [AI Policy](ai_policy.md) | How to use AI tools responsibly in this course |

For lab work, go to the relevant folder in [`labs/`](labs/).

## Publishing Lab Materials

Keep unfinished and instructor-only materials out of the public repository:

- Never push `labSoln/` or `future_labs/` to GitHub.
- When a lab is ready to release, move or copy the approved student-facing files from `future_labs/` into the matching folder under `labs/` first.
- Publish only `starter.ipynb` and `lab_sheet.md` for each released lab.
- Do not publish solution notebooks, demo notebooks, instructor guides, report templates, checkpoints, or other development files.

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

The semester mini project is the **Coffee Shop Simulation Hackathon**. In a group of three, you will build a reusable simulation model, verify its common interface using the published checker, and respond to an unseen operational scenario during the Week 16 Wednesday lab.

Read the [student handout and run the in-browser code checker](docs/mini-project.html) before the hackathon.

## Lab Pathway

| Lab | Topic | What You Will Do |
|---:|---|---|
| [Lab 1](labs/Lab01_SystemConcepts/lab_sheet.md) | From Real System to Simulation Model | Describe the coffee shop system and calculate a first simple queue |
| Lab 2 | Random Numbers and Interarrival Times | Releases in Week 4 |
| Lab 3 | Random Variables and Drink Service Times | Releases in Week 6 |
| Lab 4 | Monte Carlo Profit and Promotion Decision | Releases in Week 8 |
| Lab 5 | Discrete-Event Simulation of an M/M/1 Queue | Week 11 session |
| Lab 6 | Markov Chains and Customer Loyalty | Releases in Week 12 |
| Lab 7 | Validation and Final Recommendation | Releases in Week 14 |

## Weekly Roadmap

| Teaching Week | Date and Time | Focus | Lab / Notes |
|---:|---|---|---|
| 1 | Tue 4 Aug, 10:00-12:00 | Introduction | - |
| 2 | Tue 11 Aug, 10:00-12:00 | System concepts | Lab 1 rescheduled from Wed 12 Aug |
| 3 | Tue 18 Aug, 10:00-12:00 | Probability review | Wed 19 Aug, 09:00-11:00: Lab 1 |
| 4 | Tue 25 Aug, 10:00-12:00 | Random number generation, pseudo-random numbers, and seeds | Wed 26 Aug, 10:00-12:00: Lab 2 |
| 5 | Tue 1 Sep, 10:00-12:00 | MCGs, LCGs, and periods; Quiz 1 | - |
| 6 | Tue 8 Sep, 10:00-12:00 | Simulating random variables I | Wed 9 Sep, 10:00-12:00: Lab 3 |
| 7 | Tue 15 Sep, 10:00-12:00 | Simulating random variables II; Quiz 2 | - |
| 8 | Tue 22 Sep, 10:00-12:00 | Review | Wed 23 Sep, 10:00-12:00: Lab 4 |
| - | 28 Sep-2 Oct | Midterm week | No class |
| 10 | Tue 6 Oct, 10:00-12:00 | Monte Carlo simulation and Lab 4 demos | ~~Wed 7 Oct, 10:00-12:00: Lab 5~~ Postponed due to the midterm examination |
| 11 | ~~Tue 13 Oct, 10:00-12:00: lecture~~ | Public holiday | Wed 14 Oct, 09:00-12:00: discrete-event simulation and Lab 5 demo |
| 12 | Tue 20 Oct, 10:00-12:00 | Markov chains I | **Wed 21 Oct, 09:00-12:00**: Lab 6 |
| 13 | Tue 27 Oct, 10:00-12:00 | Markov chains II; Quiz 3 | - |
| 14 | Tue 3 Nov, 10:00-12:00 | Input/output analysis | Wed 4 Nov, 10:00-12:00: Lab 7 |
| 15 | Tue 10 Nov, 10:00-12:00 | Variance reduction and validation | - |
| 16 | Tue 17 Nov, 10:00-12:00 | Hackathon briefing | Wed 18 Nov, 10:00-12:00: Coffee Shop Simulation Hackathon |
| 17 | Tue 24 Nov, 10:00-12:00 | Course review; Quiz 4 | - |

## How To Use Each Lab

Each lab folder contains:

- `lab_sheet.md`: what to do during the lab
- `starter.ipynb`: a Jupyter notebook with TODO cells

Recommended workflow:

1. Read the lab sheet first.
2. Open the starter notebook.
3. Complete the TODO cells during the lab.
4. Add your AI use statement before submitting.

The notebooks are intentionally not full solutions. They are there to guide your work while still leaving the modelling and coding decisions to you.

## Repository Map

| Folder | What It Contains |
|---|---|
| `lectures/` | Lecture materials |
| `exercises/` | Chapter-by-chapter practice questions and short activities |
| `labs/` | Released lab sheets and starter notebooks |
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
