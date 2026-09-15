#!/usr/bin/env bash
set -euo pipefail
AI_TOOLS_ROOT="${AI_TOOLS_ROOT:-${AI_TOOLS:-$HOME/AI-tools}}"
TARGET="$AI_TOOLS_ROOT/skills/installed"
if [ $# -eq 0 ]; then echo "Usage: ./scripts/uninstall.sh <id>..." >&2; exit 1; fi
for id in "$@"; do
  rm -rf -- "$TARGET/$id"
  for dest in "$HOME/.agents/skills" "$HOME/.pi/agent/skills" "$HOME/.codex/skills" "$HOME/.claude/skills"; do
    [ -L "$dest/$id" ] && rm -f "$dest/$id" || true
  done
  echo "removed $id"
done
