#!/usr/bin/env bash
set -e
echo "Checking dev environment..."
python3 --version || true
rustc --version || true
node --version || true
echo "OK (adjust as needed)."
