#!/usr/bin/env bash
set -euo pipefail

echo "[smoke] Starting Phase-1 checks..."

# If you already have test scripts for each module, call them here.
# For now, we just check that key directories exist.

check_dir() {
    if [ ! -d "$1" ]; then
        echo "::error ::Missing directory: $1"
        exit 1
    fi
    echo "[ok] Found $1"
}

check_dir kernel/ipc
check_dir kernel/sched
check_dir kernel/pm
check_dir kernel/security
check_dir kernel/observability
check_dir daemons/prom
check_dir codex/vectorstore
check_dir codex/memory_graph
check_dir codex/timeline
check_dir scrolls/engine
check_dir scrolls/rituals
check_dir bridges
check_dir docs
check_dir tools/scripts

echo "[smoke] All required dirs present."

# Optional: if you have Python unit tests later
# python3 -m unittest discover -s tests

echo "[smoke] Finished successfully."
