#!/usr/bin/env python3
import os, yaml, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RUNTIME=Path(os.environ.get("AI_TOOLS_ROOT", os.path.expanduser("~/AI-tools")))
INST=RUNTIME/"skills/installed"
STATE=RUNTIME/"skills/state/install-manifest.yaml"
cat=yaml.safe_load((ROOT/"catalog.yaml").read_text())["skills"]
ids={e["id"]:e for e in cat}
if not INST.exists():
    print(f"not installed yet: {INST}")
    raise SystemExit(0)
state=(yaml.safe_load(STATE.read_text()) or {}) if STATE.exists() else {"installed":{}}
installed={p.name:p for p in INST.iterdir() if p.is_dir()}
stale=sorted(set(installed)-set(ids))
print(f"runtime: {RUNTIME}")
print(f"installed: {len(installed)}")
if stale: print("stale:", ", ".join(stale))
bad=[]
for i,p in installed.items():
    e=ids.get(i)
    if not e: continue
    expected=(ROOT/Path(e["path"]).parent/"SKILL.md").exists()
    if e["type"]=="skill" and not (p/"SKILL.md").exists(): bad.append(i)
if bad: print("missing SKILL.md:", ", ".join(bad))
for target in [Path(os.path.expanduser("~/.agents/skills")),Path(os.path.expanduser("~/.pi/agent/skills")),Path(os.path.expanduser("~/.codex/skills")),Path(os.path.expanduser("~/.claude/skills"))]:
    if target.exists():
        count=sum(1 for p in target.iterdir() if p.is_symlink() and p.resolve().parent==INST)
        print(f"linked {count}: {target}")
if stale or bad: raise SystemExit(1)
print("doctor: OK")
