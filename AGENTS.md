# Agent instructions for my-ai-skills

Before non-trivial work, read `INDEX.md`.

Do not load every skill. Use the registry to identify the smallest relevant set, then read only those skill files.

`explicit` and `manual` skills are user-invoked. Do not infer them.

When changing registry structure or metadata:
1. edit the asset files, not `catalog.yaml`;
2. run `python3 build_registry.py`;
3. run `./scripts/validate.sh`;
4. run `./scripts/doctor.sh` against a test `AI_TOOLS_ROOT` when possible.

Keep external workflows/plugins as pointers unless there is a deliberate decision to curate an independent skill from them.

Never place credentials, API keys, machine-specific state, or runtime caches in this repository.
