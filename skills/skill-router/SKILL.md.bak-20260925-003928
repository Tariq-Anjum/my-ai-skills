---
id: skill-router
name: skill-router
description: Route non-trivial tasks to the smallest relevant ZHOOR skill, guidance, workflow, or plugin without loading unrelated context.
type: skill
category: meta
capabilities:
  - capability-routing
  - context-management
  - progressive-disclosure
activation: contextual
risk: low
disable-model-invocation: false
---

# Skill Router

For non-trivial work:

1. Read `$AI_SKILLS_REGISTRY`.
2. Open only the category that matches the task.
3. Load only the smallest relevant skill set.
4. Never recursively search the entire `my-ai-skills` repository just to discover capabilities.
5. For `guidance`, `workflow`, or `plugin` decisions, read `$AI_TOOLS_ROOT/capabilities.md`.
6. For coding, implementation, debugging, or code-review work, check `$AI_TOOLS_ROOT/guidance/INDEX.md` and load only matching guidance.
7. Check `requires` and `conflicts` before composing skills.
8. For external workflows/plugins, use their exact manifest and `command -v`/equivalent to determine runtime availability.
9. Do not install anything unless the user explicitly authorizes installation.
10. If a task is simple and no specialized capability clearly helps, do not load one.

The registry is a routing catalog, not a prompt dump.
