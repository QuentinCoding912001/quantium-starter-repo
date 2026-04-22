#!/usr/bin/env bash

set -e

# If a local venv exists in the repo, use it
if [ -f "./.venv/Scripts/activate" ]; then
  echo "Activating local virtual environment..."
  source ./.venv/Scripts/activate
else
  echo "No local .venv found. Using system Python..."
fi

# Run tests
echo "Running tests..."
py -m pytest -v

# Capture exit code
STATUS=$?

if [ $STATUS -eq 0 ]; then
  echo "All tests passed"
  exit 0
else
  echo "Tests failed"
  exit 1
fi