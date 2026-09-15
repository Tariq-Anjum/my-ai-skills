# Changelog

## 2026-09-15 — registry hardening
- Fixed executable permissions on all shell/Python tooling.
- Added the missing `build_registry.py` generator.
- Removed the stale documentation dependency on a non-existent registry table.
- Added Agent Skills-standard `description` metadata to curated skills.
- Added `disable-model-invocation` for explicit skills.
- Added `skill-router` as the single foundational always-on routing skill.
- Added a durable system runtime installer for `~/AI-tools`.
- Added shared Agent Skills links for `~/.agents/skills/` plus detected Pi/Codex/Claude user skill directories.
- Added deterministic `ai-skills resolve`, `list`, and `info` commands.
- Added runtime checksums/state and safer doctor/sync flows.
- Updated external workflow/plugin pointers against current upstream installation guidance.
- Added Caveman as an upstream pointer without absorbing its proxy/runtime tooling.

## Initial
- Initial curated registry and source provenance structure.
