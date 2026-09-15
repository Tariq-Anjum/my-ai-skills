#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$ROOT/.venv"
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
fi
if ! "$VENV/bin/python" -c 'import yaml' >/dev/null 2>&1; then
  echo "my-ai-skills: installing Python dependency PyYAML into $VENV" >&2
  "$VENV/bin/python" -m pip install --disable-pip-version-check -r "$ROOT/requirements.txt"
fi
exec "$VENV/bin/python" "$@"
