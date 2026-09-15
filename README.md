# my-ai-skills

A curated, version-controlled skill registry for ZHOOR and other AI agents.

This repository is deliberately **not** a mirror of upstream projects. It has two roles:

1. **Curate small reusable skills** that can be installed globally.
2. **Record pointers** to larger workflows/plugins that should remain owned by their upstream projects.

## Design principle

**Global availability is not global activation.**

Every agent should be able to discover the registry and its skills, while only a small number of relevant skills are actually loaded for a task.

```text
task
  ↓
skill-router
  ↓
INDEX.md
  ↓
category
  ↓
smallest matching skill set
  ↓
SKILL.md on demand
```

`skill-router` is the only foundational always-on skill. It exists to route work; it is not domain expertise.

## Asset types

| Type | Purpose | Runtime treatment |
|---|---|---|
| `skill` | Narrow, reusable instructions | Installed into Agent Skills locations |
| `guidance` | Behavioral reference layer | Installed in the durable registry, not auto-linked as a skill |
| `workflow` | External development method/tool | Pointer + install recipe only |
| `plugin` | External agent/tool integration | Pointer + install recipe only |

## Progressive disclosure

Read `INDEX.md` first. Open a category only when it matches the task. Load a full skill only after the task has matched it.

Curated `SKILL.md` files contain standard `name` and `description` metadata so Agent Skills-compatible harnesses can discover them. Explicit/manual skills also use `disable-model-invocation: true` where supported, keeping them user-invoked rather than ambient.

## Current curated collection

The initial registry includes:

- planning: `grill-me`, `grill-with-docs`, `wayfinder`, `file-based-planning`
- continuity/maintenance: `handoff`, `session-reconcile`
- context engineering: `context-fundamentals`, `skill-router`
- communication: `terse-output`
- guidance: `karpathy-guidelines`
- external workflow pointers: OpenSpec, BMAD, Acontext
- external plugin pointer: Understand Anything
- upstream pointer: Caveman

Descriptions are intentionally short so agents can choose quickly.

## Durable local runtime

The repository is the source of truth. The local machine keeps a runtime copy:

```text
~/AI-tools/
├── my-ai-skills/              # git checkout
├── skills/
│   ├── INDEX.md               # points back to repository index
│   ├── catalog.yaml           # generated registry
│   ├── installed/             # runtime skill copies
│   └── state/                 # install state/checksums
├── mcp/
├── plugins/
├── tools/
├── memory/
└── raw/
```

This fits the existing `AI-tools` organization, where `skills/`, `mcp/`, `plugins/`, `docs/`, and `raw/` already exist as separate infrastructure areas.

## Commands

The scripts use a small private Python environment for PyYAML when the host
Python does not already provide it. They do **not** install packages into
system Python. The first command may create `.venv/`.

```bash
python3 build_registry.py
./scripts/validate.sh
./scripts/install.sh --all
./scripts/install.sh --system --all
./scripts/doctor.sh
./scripts/update.sh
./scripts/sync.sh
./scripts/uninstall.sh <id>
./bin/ai-skills list
./bin/ai-skills resolve "large unfamiliar codebase"
./bin/ai-skills info wayfinder
```

## Adding a skill

Add:

```text
skills/<id>/SKILL.md
skills/<id>/source.yaml
```

Use the Agent Skills frontmatter plus this registry's extra metadata. Then run:

```bash
./build_registry.py
./scripts/validate.sh
```

For upstream projects, prefer a `workflow/` or `plugin/` manifest rather than copying an entire repository.

## Provenance

Every curated skill records its inspiration/source in `source.yaml`. External projects remain under their own licenses; this repository does not claim ownership over upstream code or documentation.

## Security

Treat every skill as executable agent instructions. Review new or updated skills before making them globally discoverable. Global skills may be able to invoke shell commands, modify files, access credentials, or call network tools depending on the harness.

## Recovery

On a new machine:

```bash
git clone https://github.com/Tariq-Anjum/my-ai-skills ~/AI-tools/my-ai-skills
cd ~/AI-tools/my-ai-skills
./scripts/sync.sh
```

See `SYSTEM-INSTALL.md` for system-level details.
