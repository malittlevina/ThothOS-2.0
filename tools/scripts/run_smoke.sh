#!/usr/bin/env bash
set -euo pipefail

echo "[smoke] registry test"
python3 tools/scripts/test_registry.py

echo "[smoke] scheduler test"
python3 tools/scripts/test_scheduler.py

echo "[smoke] OK"
