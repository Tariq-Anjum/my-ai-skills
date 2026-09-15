# System installation

`my-ai-skills` is the canonical source. Your durable runtime is `~/AI-tools`.

## One-time install

```bash
git clone https://github.com/Tariq-Anjum/my-ai-skills ~/AI-tools/my-ai-skills
cd ~/AI-tools/my-ai-skills
./build_registry.py
./scripts/validate.sh
./scripts/install.sh --all
./scripts/system_link.py
```

This does four things:

1. Installs curated `skill` and `guidance` assets into `~/AI-tools/skills/installed/`.
2. Exposes the routing index at `~/AI-tools/skills/INDEX.md`.
3. Creates one shared Agent Skills location at `~/.agents/skills/` and symlinks supported user-level agent skill directories when those harnesses are present.
4. Keeps workflows/plugins as pointers; it does not silently install external infrastructure.

## Portable command

```bash
AI_TOOLS_ROOT="$HOME/AI-tools" ./scripts/install.sh --system --all
```

## Resolver

```bash
~/AI-tools/my-ai-skills/bin/ai-skills resolve "I need to understand a large unfamiliar repository before changing it"
```

The resolver is a deterministic catalog helper, not an LLM. Agents should still use the routing index and their own judgment.

## Recovery on a new machine

```bash
git clone https://github.com/Tariq-Anjum/my-ai-skills ~/AI-tools/my-ai-skills
cd ~/AI-tools/my-ai-skills
./scripts/sync.sh
```

## Important limitation

There is no single global-skill mechanism shared by every agent harness. This repository therefore uses the Agent Skills format and a shared `~/.agents/skills/` location where supported, plus symlinks for detected Pi/Codex/Claude user skill directories. Other agents can consume the same curated files through their own native skill path or settings.
