#!/usr/bin/env python3
"""Synchronize the canonical mini-project site into the GitHub Pages folder."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MINI_PROJECT_DIR = PROJECT_ROOT / "mini_project"
SOURCE_DIR = MINI_PROJECT_DIR / "site"
PAGES_DIR = PROJECT_ROOT / "docs"

# Deployed filename -> canonical source. The browser checker loads the same
# checker file that students run from the command line.
SITE_FILES: dict[str, Path] = {
    "mini-project.html": SOURCE_DIR / "mini-project.html",
    "mini-project.css": SOURCE_DIR / "mini-project.css",
    "mini-project.js": SOURCE_DIR / "mini-project.js",
    "mini-project-worker.js": SOURCE_DIR / "mini-project-worker.js",
    "mini-project-template.py": MINI_PROJECT_DIR / "cafe_model_template.py",
    "mini-project-checker.py": MINI_PROJECT_DIR / "check_cafe_submission.py",
    "mini-project-AI_USE_template.md": MINI_PROJECT_DIR / "AI_USE_template.md",
    "mini-project-instructions.pdf": MINI_PROJECT_DIR / "SCIM211_Cafe_Poisson_Project_Instructions.pdf",
}

# Files from earlier versions that should no longer be deployed.
RETIRED_FILES: tuple[str, ...] = ("mini-project-browser-checker.py",)


def out_of_date_files() -> list[str]:
    """Return deployment files that are missing, differ from their source, or are retired."""
    stale: list[str] = []
    for deployed_name, source in SITE_FILES.items():
        deployed = PAGES_DIR / deployed_name
        if not source.is_file():
            raise FileNotFoundError(f"Missing canonical source file: {source}")
        if not deployed.is_file() or not filecmp.cmp(source, deployed, shallow=False):
            stale.append(deployed_name)
    stale.extend(f"{name} (retired; delete it)" for name in RETIRED_FILES if (PAGES_DIR / name).exists())
    return stale


def synchronize() -> None:
    """Copy all canonical files into the GitHub Pages directory."""
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    for deployed_name, source in SITE_FILES.items():
        if not source.is_file():
            raise FileNotFoundError(f"Missing canonical source file: {source}")
        destination = PAGES_DIR / deployed_name
        shutil.copy2(source, destination)
        print(f"updated {destination.relative_to(PROJECT_ROOT)}")
    for name in RETIRED_FILES:
        retired = PAGES_DIR / name
        if retired.exists():
            try:
                retired.unlink()
                print(f"removed retired {retired.relative_to(PROJECT_ROOT)}")
            except OSError as exc:
                print(f"WARNING: could not remove retired {retired.relative_to(PROJECT_ROOT)}: {exc}")


def main() -> int:
    """Run the synchronization or a read-only consistency check."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale deployment files without modifying docs/")
    args = parser.parse_args()

    if args.check:
        stale = out_of_date_files()
        if stale:
            print("OUT OF DATE: " + ", ".join(stale))
            return 1
        print("PASS: docs/ mini-project deployment matches its canonical sources")
        return 0

    synchronize()
    print("PASS: mini-project site synchronized to docs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
