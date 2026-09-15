#!/usr/bin/env python3
from pathlib import Path
from _bootstrap import ensure_yaml
ensure_yaml()
import re
import yaml
ROOT=Path(__file__).resolve().parents[1]
cat=yaml.safe_load((ROOT/"catalog.yaml").read_text(encoding="utf-8"))
entries=cat.get("skills",[])
errors=[]
ids={e["id"] for e in entries}
for e in entries:
    p=ROOT/e["path"]
    if not p.exists(): errors.append(f"{e['id']}: missing {e['path']}"); continue
    if e["id"]!=re.sub(r"[^a-z0-9-]+","-",e["id"].lower()).strip("-"): errors.append(f"{e['id']}: invalid id")
    for k in ("name","type","category","capabilities","activation","risk"): 
        if not e.get(k): errors.append(f"{e['id']}: missing catalog field {k}")
    for x in e.get("requires",[]) or []:
        if x not in ids: errors.append(f"{e['id']}: unknown requires {x}")
    for x in e.get("conflicts",[]) or []:
        if x not in ids: errors.append(f"{e['id']}: unknown conflicts {x}")
    if e["type"] in ("skill","guidance"):
        text=p.read_text(encoding="utf-8")
        if not text.startswith("---"): errors.append(f"{e['id']}: no frontmatter")
        else:
            _,fm,_=text.split("---",2); fm=yaml.safe_load(fm) or {}
            for k in ("id","name","description","type","category","activation","risk"):
                if not fm.get(k): errors.append(f"{e['id']}: missing frontmatter {k}")
            if e["type"]=="skill":
                if len(fm.get("name",""))>64: errors.append(f"{e['id']}: name > 64 chars")
                if len(fm.get("description",""))>1024: errors.append(f"{e['id']}: description > 1024 chars")
                if "disable-model-invocation" not in fm: errors.append(f"{e['id']}: missing disable-model-invocation")
        src=p.parent/"source.yaml"
        if not src.exists(): errors.append(f"{e['id']}: missing source.yaml")
    else:
        m=yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for k in ("upstream","install","summary"): 
            if not m.get(k): errors.append(f"{e['id']}: manifest missing {k}")
if errors:
    print("\n".join(f"- {x}" for x in errors)); raise SystemExit(1)
print(f"OK — {len(entries)} entries validated.")
