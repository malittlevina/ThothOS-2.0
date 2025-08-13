#!/usr/bin/env python3
"""
Update the % column in docs/TRACKER.md based on docs/progress.yaml.
It matches rows by Task ID (e.g., "IPC-1", "SCHED-2") inside Markdown tables.
Idempotent, minimal diff.
"""
from __future__ import annotations
import re, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
TRACKER = ROOT / "docs" / "TRACKER.md"
PROGRESS = ROOT / "docs" / "progress.yaml"

def load_progress():
    if not PROGRESS.exists():
        print(f"[update_tracker] progress file not found: {PROGRESS}", file=sys.stderr)
        return {}
    return yaml.safe_load(PROGRESS.read_text()) or {}

def update_tracker(md: str, progress: dict) -> str:
    """
    We look for Markdown table rows that start with a pipe and have Task ID in col 1.
    Columns (by your file): Task ID | Task | Description | Dependency Modules | Owner | % | Notes
    """
    def repl(match):
        row = match.group(0)
        cells = [c.strip() for c in row.strip().split("|")[1:-1]]  # drop first/last empty (pipes)
        if len(cells) < 7:
            return row
        task_id = cells[0]
        if task_id in progress:
            # Replace % column (index 5)
            old = cells[5]
            cells[5] = str(progress[task_id])
            new_row = "| " + " | ".join(cells) + " |\n"
            return new_row
        return row

    # Only transform rows inside tables (lines that start with a pipe and have 6+ pipes)
    pattern = re.compile(r"^\|.*\|\s*$", re.MULTILINE)
    return pattern.sub(repl, md)

def main():
    progress = load_progress()
    if not progress:
        print("[update_tracker] no progress values to apply; exiting.")
        return 0
    before = TRACKER.read_text()
    after = update_tracker(before, progress)
    if after != before:
        TRACKER.write_text(after)
        print("[update_tracker] TRACKER.md updated.")
    else:
        print("[update_tracker] no changes required.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
