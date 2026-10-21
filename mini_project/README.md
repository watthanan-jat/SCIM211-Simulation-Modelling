# SCIM211 Coffee Shop Simulation Mini Project

This folder is the canonical home for all **student-facing mini-project source
files**.

## Student materials

| File or folder | Purpose |
|---|---|
| `coffee_shop_hackathon_handout.md` | Complete student handout |
| `mini_project_rubric.md` | Analytic 9-mark rubric |
| `cafe_model_template.py` | Downloadable starter structure |
| `AI_USE_template.md` | Form for the group's AI Use Acknowledgment Statement (`AI_USE.md`) |
| `check_cafe_submission.py` | Readiness checker, used both from the command line and by the browser checker |
| `site/` | HTML, CSS, and JavaScript for the GitHub Pages handout and browser checker |
| `sync_site_to_docs.py` | Copies the website, template, and checker into `docs/` for deployment |

The files named `docs/mini-project*` are generated deployment copies.
`docs/mini-project-template.py` is a copy of `cafe_model_template.py`, and
`docs/mini-project-checker.py` is a copy of `check_cafe_submission.py`. Edit the
canonical files here, then synchronize them with:

```bash
python mini_project/sync_site_to_docs.py
```

Check that the deployed copies are current without changing files:

```bash
python mini_project/sync_site_to_docs.py --check
```

## Checker reference statistics

The statistical part of the checker compares each submission with stored means
and standard deviations from the private reference model. After changing the
model rules, `STANDARD_CONFIG`, or `SCENARIOS`, regenerate them and resynchronize:

```bash
python labSoln/mini_project/build_checker_reference.py
python mini_project/sync_site_to_docs.py
```

## Instructor-only materials

Solutions, marking guidance, release-day challenge cards, and the printable
challenge-card PDF remain under `labSoln/mini_project/`. They are deliberately
not stored here because this folder is intended for publication to students.

The private challenge simulator, calibration results, and human feasibility
record also stay there. They are not part of the student checker or site sync.

Never publish `labSoln/` or `future_labs/`.
