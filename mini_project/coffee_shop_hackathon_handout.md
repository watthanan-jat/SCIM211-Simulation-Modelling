# SCIM211 Coffee Shop Simulation Hackathon

## Group Mini Project: 9%

You will work in a group of **three students** to build a reusable coffee-shop simulation. In the Week 16 Wednesday lab, your group will receive one unseen operational challenge and will have one hour to adapt and analyse your model. The second hour will be used for group pitches and questions.

The purpose of the project is not to build the most complicated café. The purpose is to build a simulation that is correct, configurable, reproducible, and useful for making a decision.

## Assessment

| Component | Marks |
|---|---:|
| Prepared and reusable café simulation | 4 |
| Live challenge implementation and experiment | 3 |
| Pitch communication | 1 |
| Individual oral understanding | 1 |
| **Total** | **9** |

All three group members must understand the submitted code and be ready to explain it.

## What Every Café Simulation Must Include

Your prepared model must contain:

1. a 120-minute café operating period, with time measured in minutes;
2. random customer arrivals;
3. simple and complex drink orders;
4. random service times that depend on order type;
5. a configurable number of baristas;
6. a customer queue, initially using first-come, first-served;
7. arrival, service-start, and service-completion logic;
8. system state, including the clock, waiting customers, and barista availability;
9. a configurable maximum queue length, with refused customers recorded as lost;
10. revenue, ingredient cost, staffing cost, and profit calculations;
11. controlled random seeds so a result can be reproduced;
12. repeated simulation runs using a supplied list of seeds; and
13. the required output measures listed below.

Your model must be written so that inputs can be changed without rewriting the entire program. The live challenge may change arrivals, staffing, service times, customer priority, queue admission, the menu, a promotion, an equipment condition, or a closing policy.

## Required Submission Files

Before the hackathon, submit a folder named with your group number:

```text
GROUP_01/
├── cafe_model.py
├── model_notes.md
└── AI_USE.md
```

You may also keep a development notebook, but the assessed simulation must run from `cafe_model.py`. The checker will not extract code from a notebook.

### `model_notes.md`

Briefly describe:

- the real system represented by the model;
- the arrival and service-time assumptions;
- how the queue and baristas operate;
- the meaning and units of the outputs;
- at least three checks used to verify the model; and
- one important limitation.

### `AI_USE.md`

If your group used an AI tool, state:

- which tool was used;
- how it was used; and
- how your group checked, corrected, or revised its output.

If no AI tool was used, state that explicitly.

## Compulsory Python Interface

The file `cafe_model.py` must define both functions below with exactly these names and arguments:

```python
def simulate_cafe(config, seed):
    """Run one complete café replication and return a result dictionary."""


def run_replications(config, seeds):
    """Run one replication per seed and return a pandas DataFrame."""
```

Do not rename these functions. Do not request keyboard input, open a notebook, display a menu, or require the instructor to edit your code before it runs.

Your code may define any additional classes or helper functions you need.

## Configuration Dictionary

`simulate_cafe(config, seed)` must use all of the following configuration entries:

| Key | Meaning |
|---|---|
| `run_minutes` | Time during which new customers may arrive |
| `arrival_rate_per_hour` | Mean number of arrivals per hour |
| `n_baristas` | Number of identical baristas |
| `simple_order_probability` | Probability that an arriving customer orders a simple drink |
| `mean_service_simple` | Mean service time for a simple drink, in minutes |
| `mean_service_complex` | Mean service time for a complex drink, in minutes |
| `price_simple` | Selling price of a simple drink, in baht |
| `price_complex` | Selling price of a complex drink, in baht |
| `cost_simple` | Ingredient cost of a simple drink, in baht |
| `cost_complex` | Ingredient cost of a complex drink, in baht |
| `barista_cost_per_hour` | Staffing cost per barista per hour, in baht |
| `max_queue` | Maximum number waiting, or `None` for no limit |

The official checker will supply its own configuration. Values must not be hard-coded in the simulation.

The baseline configuration used during development is:

```python
BASE_CONFIG = {
    "run_minutes": 120.0,
    "arrival_rate_per_hour": 24.0,
    "n_baristas": 2,
    "simple_order_probability": 0.45,
    "mean_service_simple": 2.0,
    "mean_service_complex": 4.0,
    "price_simple": 85.0,
    "price_complex": 120.0,
    "cost_simple": 25.0,
    "cost_complex": 40.0,
    "barista_cost_per_hour": 120.0,
    "max_queue": 8,
}
```

Customers may arrive only before `run_minutes`, but accepted customers must be allowed to finish service. Therefore, `finish_time` can be later than `run_minutes`.

## Required Result Dictionary

`simulate_cafe(config, seed)` must return a Python dictionary containing every field below:

| Field | Required meaning |
|---|---|
| `run_minutes` | Copy of the configured arrival horizon |
| `finish_time` | Later of closing time and the last service completion |
| `n_arrivals` | Total number of customer arrivals |
| `n_served` | Number completing service |
| `n_lost` | Number refused because the queue is full |
| `n_served_simple` | Simple orders completed |
| `n_served_complex` | Complex orders completed |
| `mean_wait` | Mean waiting time of served customers, in minutes |
| `p90_wait` | 90th percentile of served-customer waiting time |
| `max_wait` | Maximum served-customer waiting time |
| `throughput_per_hour` | `n_served / (run_minutes / 60)` |
| `utilisation` | Total busy barista time divided by `n_baristas * finish_time` |
| `revenue` | Revenue from completed orders |
| `total_cost` | Ingredient cost plus scheduled barista cost |
| `profit` | `revenue - total_cost` |

When no customers are served, all waiting-time outputs must be `0.0` rather than missing or undefined.

The following count identities must hold:

```text
n_arrivals = n_served + n_lost
n_served = n_served_simple + n_served_complex
```

`run_replications(config, seeds)` must return a pandas DataFrame with one row per supplied seed. It must contain a `seed` column and all the result fields listed above.

## The Compulsory Readiness Check

Your group will receive:

- `cafe_model_template.py`, which shows the required structure; and
- [`check_cafe_submission.py`](check_cafe_submission.py), which is the same checker used by the instructor.

From the repository root, place or copy your completed `cafe_model.py` into your group folder and run:

```bash
python mini_project/check_cafe_submission.py GROUP_01/cafe_model.py
```

Replace `GROUP_01` with your actual folder name.

The final line must be:

```text
PASS: GROUP_01/cafe_model.py
```

The instructor can check all eight submissions with one command:

```bash
python mini_project/check_cafe_submission.py submissions/*/cafe_model.py
```

### What the Checker Tests

The checker verifies that:

- the file imports without an error;
- both required functions exist;
- the official configuration can be used without editing the file;
- all required outputs are present, numeric, finite, and within sensible bounds;
- customer and order counts balance;
- revenue, cost, profit, and throughput are internally consistent;
- the supplied `seed` makes a run reproducible;
- different seeds can produce different stochastic results;
- a zero-arrival café produces zero arrivals and zero service outputs;
- increasing the number of baristas does not increase waiting under the checker's heavy-load scenario;
- the configuration dictionary is not modified; and
- the replication function returns one correct row per seed.

**A submission that prints `FAIL` is not a working submission. Fix every reported failure before the hackathon.** Passing the checker confirms the required interface and basic consistency; it does not prove that every modelling assumption or calculation is correct.

Run the checker again after every important change. Do not wait until the hackathon to try it for the first time.

## Week 16 Hackathon

### First hour: assigned challenge

At the beginning of the Wednesday lab, each group will receive a different challenge card. During the first hour, your group must:

1. adapt its prepared simulation;
2. compare the required policies or scenarios;
3. use the instructor-supplied seeds;
4. run at least 40 replications per policy;
5. prepare one comparison table and one graph;
6. calculate a 95% confidence interval for the main outcome;
7. make a practical recommendation; and
8. identify one assumption or limitation that could affect the recommendation.

At the end of the first hour, submit:

- the modified code;
- the results table;
- the graph; and
- the pitch slide.

### Second hour: pitch and questions

Each group receives six minutes:

- four minutes for the pitch; and
- two minutes for questions.

All three students must speak. A suggested division is:

1. model and assigned problem;
2. experiment and results; and
3. recommendation and limitation.

## Marking Guide

### Prepared simulation: 4 marks

| Criterion | Marks |
|---|---:|
| Correct entities, queue, resources, events, and random inputs | 1.5 |
| Reusable and configurable implementation | 1.0 |
| Replications, seeds, outputs, and uncertainty analysis | 1.0 |
| Verification, documentation, and assumptions | 0.5 |

### Live challenge: 3 marks

| Criterion | Marks |
|---|---:|
| Correct implementation of the assigned change | 1.0 |
| Appropriate experiment using replications and uncertainty | 1.0 |
| Evidence-based recommendation and meaningful limitation | 1.0 |

### Pitch communication: 1 mark

| Criterion | Marks |
|---|---:|
| Clear four-minute explanation supported by an effective table or graph | 1.0 |

### Individual understanding: 1 mark per student

| Criterion | Marks |
|---|---:|
| Explains their contribution, relevant code, modelling choice, result, and answer to the instructor's question independently | 1.0 |

The project is assessed on modelling quality, reproducibility, experimental reasoning, and explanation. It is not a competition to produce the highest simulated profit.

See the [detailed analytic rubric](mini_project_rubric.md) for performance-level descriptors and the readiness-check scoring rule.

## Responsible AI Use

The course AI Collaboration Level 3 policy applies. AI tools may support idea generation, explanation, drafting, or code feedback, but your group must check and understand all submitted work. During the pitch, any group member may be asked to explain an AI-assisted part of the code.

Undisclosed AI use, fabricated results, or code that the group cannot explain will be handled under the course academic-integrity policy.
