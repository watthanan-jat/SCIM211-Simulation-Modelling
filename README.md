# SCIM211 Simulation Modelling

Welcome to **SCIM211 Simulation Modelling**, a second-year course for Industrial Mathematics and Data Science students.

This course introduces simulation as a practical way to study systems involving uncertainty, queues, random behaviour, operational decisions, and performance measurement. Across the semester, students build one connected **Coffee Shop Simulation Project** that grows from a simple queue into a richer model for analysis and recommendation.

## Course At A Glance

| Item | Details |
|---|---|
| Level | Second-year undergraduate |
| Programme | Industrial Mathematics and Data Science |
| Duration | 15 weeks |
| Theory | 2 hours every week |
| Lab | 2 hours every even week |
| Main project | Coffee Shop Simulation Project |
| Tools | Python, NumPy, pandas, matplotlib, SciPy, Jupyter |

## Start Here

| Page | Purpose |
|---|---|
| [Syllabus](syllabus.md) | Course aims, topics, learning outcomes, and expectations |
| [Schedule](schedule.md) | Weekly theory and lab plan |
| [Assessment](assessment.md) | Assessment structure and submission expectations |
| [AI Policy](ai_policy.md) | Responsible AI use for labs and project work |

## Coffee Shop Simulation Project

The course labs are connected through one semester-long project. Students gradually model a coffee shop by studying:

- Customer arrivals
- Drink orders and service times
- Queues and waiting times
- Rush-hour behaviour
- Profit and promotion decisions
- Customer loyalty
- Input/output analysis and validation

The project is designed to help students practise both mathematical modelling and clear communication. The goal is not only to run code, but to explain what the model represents, what assumptions were made, and how results should be interpreted.

## Lab Pathway

| Lab | Topic | Project Role |
|---:|---|---|
| [Lab 1](labs/Lab01_SystemConcepts/lab_sheet.md) | From Real System to Simulation Model | Define the coffee shop system and first queue calculations |
| [Lab 2](labs/Lab02_RandomNumbers/lab_sheet.md) | Random Numbers and Interarrival Times | Generate arrivals using pseudo-random numbers |
| [Lab 3](labs/Lab03_RandomVariables/lab_sheet.md) | Random Variables and Drink Service Times | Simulate drink orders and service-time variation |
| [Lab 4](labs/Lab04_MonteCarlo/lab_sheet.md) | Monte Carlo Profit and Promotion Decision | Estimate profit, risk, and promotion outcomes |
| [Lab 5](labs/Lab05_DES/lab_sheet.md) | Discrete-Event Simulation of an M/M/1 Queue | Compare calm, normal, rush, and overloaded conditions |
| [Lab 6](labs/Lab06_MarkovChains/lab_sheet.md) | Markov Chains and Customer Loyalty | Model loyalty transitions and retention |
| [Lab 7](labs/Lab07_Validation/lab_sheet.md) | Validation and Final Recommendation | Use data, replications, confidence intervals, and recommendations |

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

## Repository Map

| Folder | Contents |
|---|---|
| `lectures/` | Lecture materials |
| `exercises/` | Practice questions and short activities |
| `labs/` | Lab sheets, starter notebooks, and report templates |
| `data/` | Sample datasets for modelling and validation |
| `src/` | Source-code stubs and reusable simulation helpers |
| `tests/` | Placeholder tests for future implementations |
| `.github/workflows/` | Automated test workflow |

## Working With The Materials

Students should read the lab sheet before each lab, complete the TODO cells in the starter notebook, and submit the report template as instructed. Lab work should be kept organised because later labs build on earlier modelling decisions.

All submitted work should be reproducible, clearly explained, and consistent with the course [AI Policy](ai_policy.md).

## Learning Focus

By the end of the course, students should be able to:

- Translate a real system into a simulation model.
- Generate and use random numbers responsibly.
- Simulate random variables and queue behaviour.
- Run Monte Carlo and discrete-event simulation experiments.
- Analyse simulation output using confidence intervals.
- Discuss assumptions, limitations, and validation.
- Communicate simulation-based recommendations clearly.
