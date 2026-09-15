#!/usr/bin/env python3
"""Checks that every catalog.yaml entry has a matching file, required
frontmatter fields present, and requires/conflicts point at real ids."""
import sys, os, yaml
from _lib import load_catalog, find, REPO_ROOT

REQUIRED_SKILL_FIELDS = {"id", "name", "type", "category", "capabilities", "activation", "risk"}
REQUIRED_MANIFEST_FIELDS = {"id", "name", "type", "category", "capabilities", "activation", "risk", "upstream", "install", "summary"}

def read_frontmatter(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm)

def main():
    entries = load_catalog()
    errors = []
    ids = {e["id"] for e in entries}

    for e in entries:
        full_path = os.path.join(REPO_ROOT, e["path"])
        if not os.path.exists(full_path):
            errors.append(f"{e['id']}: missing file {e['path']}")
            continue
        if e["type"] in ("skill", "guidance"):
            fm = read_frontmatter(full_path)
            if fm is None:
                errors.append(f"{e['id']}: no frontmatter in {e['path']}")
            else:
                missing = REQUIRED_SKILL_FIELDS - set(fm.keys())
                if missing:
                    errors.append(f"{e['id']}: missing frontmatter fields {missing}")
            src_path = os.path.join(os.path.dirname(full_path), "source.yaml")
            if not os.path.exists(src_path):
                errors.append(f"{e['id']}: missing source.yaml (provenance)")
        else:
            with open(full_path) as f:
                m = yaml.safe_load(f)
            missing = REQUIRED_MANIFEST_FIELDS - set(m.keys())
            if missing:
                errors.append(f"{e['id']}: manifest missing fields {missing}")

        for dep in e.get("requires", []) or []:
            if dep not in ids:
                errors.append(f"{e['id']}: requires unknown id '{dep}'")
        for dep in e.get("conflicts", []) or []:
            if dep not in ids:
                errors.append(f"{e['id']}: conflicts references unknown id '{dep}'")

    if errors:
        print(f"{len(errors)} problem(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    print(f"OK — {len(entries)} entries validated.")

if __name__ == "__main__":
    main()
