#!/usr/bin/env bash
# Simple start script for Render or other hosts
set -euo pipefail

: ${PORT:=5000}
: ${GUNICORN_WORKERS:=3}

exec gunicorn run:app \
  --workers ${GUNICORN_WORKERS} \
  --bind 0.0.0.0:${PORT} \
  --log-level info
