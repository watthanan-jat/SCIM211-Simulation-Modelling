# SCIM211 Coffee Shop Simulation Mini Project

This folder is the canonical home for all **student-facing mini-project source
files**.

## Student materials

| File or folder | Purpose |
|---|---|
| `coffee_shop_hackathon_handout.md` | Complete student handout |
| `mini_project_rubric.md` | Analytic 9-mark rubric |
| `cafe_model_template.py` | Downloadable starter structure |
| `check_cafe_submission.py` | Command-line readiness checker |
| `site/` | Source files for the GitHub Pages handout and browser checker |
| `sync_site_to_docs.py` | Copies the website source into `docs/` for deployment |

The files named `docs/mini-project*` are generated deployment copies. Edit the
files in `mini_project/site/`, then synchronize them with:

```bash
python mini_project/sync_site_to_docs.py
```

Check that the deployed copies are current without changing files:

```bash
python mini_project/sync_site_to_docs.py --check
```

## Instructor-only materials

Solutions, marking guidance, release-day challenge cards, and the printable
challenge-card PDF remain under `labSoln/mini_project/`. They are deliberately
not stored here because this folder is intended for publication to students.

Never publish `labSoln/` or `future_labs/`.
