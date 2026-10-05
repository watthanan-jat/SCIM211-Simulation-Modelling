#!/usr/bin/env python3
"""Synchronize the canonical mini-project site into the GitHub Pages folder."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "mini_project" / "site"
PAGES_DIR = PROJECT_ROOT / "docs"
SITE_FILES = (
    "mini-project.html",
    "mini-project.css",
    "mini-project.js",
    "mini-project-worker.js",
    "mini-project-browser-checker.py",
    "mini-project-template.py",
)


def out_of_date_files() -> list[str]:
    """Return deployment files that are missing or differ from their source."""
    stale: list[str] = []
    for filename in SITE_FILES:
        source = SOURCE_DIR / filename
        deployed = PAGES_DIR / filename
        if not source.is_file():
            raise FileNotFoundError(f"Missing canonical site file: {source}")
        if not deployed.is_file() or not filecmp.cmp(source, deployed, shallow=False):
            stale.append(filename)
    return stale


def synchronize() -> None:
    """Copy all canonical site files into the GitHub Pages directory."""
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    for filename in SITE_FILES:
        source = SOURCE_DIR / filename
        destination = PAGES_DIR / filename
        if not source.is_file():
            raise FileNotFoundError(f"Missing canonical site file: {source}")
        shutil.copy2(source, destination)
        print(f"updated {destination.relative_to(PROJECT_ROOT)}")


def main() -> int:
    """Run the synchronization or a read-only consistency check."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report stale deployment files without modifying docs/",
    )
    args = parser.parse_args()

    if args.check:
        stale = out_of_date_files()
        if stale:
            print("OUT OF DATE: " + ", ".join(stale))
            return 1
        print("PASS: docs/ mini-project deployment matches mini_project/site/")
        return 0

    synchronize()
    print("PASS: mini-project site synchronized to docs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
