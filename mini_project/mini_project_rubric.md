# SCIM211 Coffee Shop Simulation Hackathon Rubric

## Total: 9 marks

The prepared model, live challenge, and pitch communication contribute a shared group mark out of 8. The final oral-understanding mark out of 1 is awarded individually, so members of the same group may receive different totals.

| Section | Assessment basis | Marks |
|---|---|---:|
| A. Prepared café simulation | Group | 4 |
| B. Live assigned challenge | Group | 3 |
| C. Pitch communication | Group | 1 |
| D. Individual understanding | Individual | 1 |
| **Total for each student** |  | **9** |

## Readiness-Check Rule

The submitted `cafe_model.py` must display **PASS** in the published checker before the hackathon.

- PASS is compulsory but does not earn marks automatically.
- If the submitted file displays FAIL, criterion A2 receives 0 because the common interface is not operational.
- Other criteria are marked from evidence that genuinely runs and can be explained.
- Results that cannot be reproduced from the submitted code cannot receive experiment or recommendation marks.

## A. Prepared Café Simulation: 4 Marks, Group

### A1. Simulation Logic and Correctness: 1.5 Marks

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Correct arrivals, order types, service times, queue discipline, barista allocation, queue limit, service completion, and customer accounting. Outputs are credible and important edge cases work. | 1.5 |
| Mostly complete | Core model is correct, with a minor defect or unclear assumption that does not substantially invalidate the outputs. | 1.0 |
| Partial | Model runs, but an important part of the queue, event, resource, or customer logic is missing or incorrect. | 0.5 |
| Not demonstrated | Model does not run, produces unusable outputs, or the group cannot explain its basic event logic. | 0 |

### A2. Common Interface and Configurability: 1 Mark

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Checker displays PASS. Both required functions work, all required inputs come from `config`, and scenarios can be changed without rewriting the model. | 1.0 |
| Mostly complete | Checker displays PASS, but one part still depends on avoidable hard-coding or manual intervention. | 0.75 |
| Partial | Interface works only after a small manual correction, or several inputs are hard-coded. | 0.5 |
| Minimal | File requires substantial editing before it can be tested. | 0.25 |
| Not operational | Checker displays FAIL for the submitted version. | 0 |

### A3. Reproducibility, Replications, and Outputs: 1 Mark

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Seeds reproduce results; `run_replications` works; required counts, waits, utilisation, and financial measures are correct; uncertainty can be estimated across replications. | 1.0 |
| Mostly complete | Reproducibility and replication work, but one output or uncertainty calculation has a minor problem. | 0.75 |
| Partial | Multiple runs are possible, but seeds, output definitions, or replication structure are incomplete. | 0.5 |
| Minimal | Only isolated runs are available, or outputs cannot be reproduced reliably. | 0.25 |
| Not demonstrated | No valid simulation output is produced. | 0 |

### A4. Verification, Documentation, and Assumptions: 0.5 Marks

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | `model_notes.md` explains the model, units, assumptions, at least three meaningful verification checks, and one genuine limitation. `AI_USE.md` is complete. | 0.5 |
| Mostly complete | Documentation is understandable but one required element is weak or missing. | 0.4 |
| Partial | Some assumptions or checks are listed without explaining what they establish. | 0.25 |
| Minimal | Documentation is very limited or inconsistent with the code. | 0.1 |
| Not demonstrated | Required documentation is absent. | 0 |

## B. Live Assigned Challenge: 3 Marks, Group

### B1. Implementation of the Assigned Change: 1 Mark

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | The assigned operational change and all policy alternatives are implemented correctly without breaking the baseline model. | 1.0 |
| Mostly complete | Main change is correct, with a minor defect in one policy or output. | 0.75 |
| Partial | Challenge is attempted, but an important rule is simplified incorrectly or only some alternatives run. | 0.5 |
| Minimal | A visible edit is made, but it does not represent the assigned decision adequately. | 0.25 |
| Not demonstrated | No working challenge modification is produced. | 0 |

### B2. Experimental Design and Uncertainty: 1 Mark

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Policies use the same supplied seeds, at least 40 replications each, suitable measures, a useful graph and table, and a correctly interpreted 95% confidence interval. | 1.0 |
| Mostly complete | Comparison is sound, with one minor weakness in replications, display, or uncertainty interpretation. | 0.75 |
| Partial | Policies are compared, but the design is inconsistent or uncertainty is calculated or interpreted poorly. | 0.5 |
| Minimal | Conclusions rely mainly on one run or on incomparable scenarios. | 0.25 |
| Not demonstrated | No reproducible comparison is produced. | 0 |

### B3. Recommendation and Limitation: 1 Mark

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Recommendation answers the assigned decision, uses numerical evidence and uncertainty, considers service and financial trade-offs, and identifies a limitation that could change the decision. | 1.0 |
| Mostly complete | Recommendation is supported, but one trade-off, uncertainty statement, or limitation is underdeveloped. | 0.75 |
| Partial | A recommendation is stated but relies on limited evidence or gives a generic limitation. | 0.5 |
| Minimal | Recommendation is only loosely connected to the simulation results. | 0.25 |
| Not demonstrated | No defensible recommendation is made. | 0 |

## C. Pitch Communication: 1 Mark, Group

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Four-minute pitch clearly explains the challenge, comparison, main evidence, recommendation, and limitation. The visual is readable and the team stays within time. | 1.0 |
| Mostly complete | Pitch is clear but one required element, visual, or timing aspect needs improvement. | 0.75 |
| Partial | Main idea is understandable, but the evidence or recommendation is difficult to follow. | 0.5 |
| Minimal | Pitch is incomplete, substantially over time, or unsupported by a readable result. | 0.25 |
| Not demonstrated | No pitch is delivered. | 0 |

## D. Individual Understanding: 1 Mark per Student

| Performance | Descriptor | Marks |
|---|---|---:|
| Complete | Student independently explains their contribution, relevant code, modelling choice, output, and answer to the instructor's question accurately. | 1.0 |
| Mostly complete | Student shows clear understanding but needs a small prompt or makes a minor error. | 0.75 |
| Partial | Student understands the overall project but cannot explain an important part of the code, experiment, or result. | 0.5 |
| Minimal | Student gives only a superficial explanation or relies heavily on teammates. | 0.25 |
| Not demonstrated | Student does not participate or cannot demonstrate understanding of the submitted work. | 0 |

## Marker Summary

| Criterion | Maximum | Awarded |
|---|---:|---:|
| A1. Simulation logic and correctness | 1.5 |  |
| A2. Common interface and configurability | 1.0 |  |
| A3. Reproducibility, replications, and outputs | 1.0 |  |
| A4. Verification, documentation, and assumptions | 0.5 |  |
| B1. Assigned change | 1.0 |  |
| B2. Experimental design and uncertainty | 1.0 |  |
| B3. Recommendation and limitation | 1.0 |  |
| C. Pitch communication | 1.0 |  |
| D. Individual understanding | 1.0 |  |
| **Total** | **9.0** |  |

Academic-integrity and responsible-AI requirements apply separately. Fabricated results or work that students cannot explain are handled under the published course policy rather than treated as ordinary rubric weaknesses.
