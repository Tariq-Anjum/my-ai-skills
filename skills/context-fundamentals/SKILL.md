---
id: context-fundamentals
name: context-fundamentals
display_name: Context Fundamentals
description: Apply progressive disclosure and context-budget discipline when designing
  or debugging an agent harness, skill registry, or context-loading workflow.
type: skill
category: meta
capabilities:
- context-management
- harness-design
activation: contextual
requires: null
conflicts: null
risk: low
disable-model-invocation: false
---

# Context Fundamentals
## When to use
When designing, debugging, or reasoning about the harness/registry itself
— not a specific task, but how tasks get context in the first place. Read
this before changing how skills are indexed, loaded, or summarized.

## What it does
A short set of working principles, not a full course:
- Context is everything in the model's attention at once — system text,
  tool definitions, retrieved files, history, tool output — not just the
  user's prompt. All of it competes for the same limited attention.
- Quality beats quantity: a shorter, curated context that's actually
  relevant beats a longer one padded with things that merely seemed
  related.
- Attention degrades over a long context, particularly toward the middle
  — put the most decision-relevant material near the start or end of
  what's loaded, not buried in the middle of a long dump.
- Prefer loading by reference (an index entry, a file path) over loading
  full content speculatively. Full content comes in only once something
  has actually matched the task.

## Explicitly out of scope
- Doesn't cover specific optimization tactics (compaction thresholds,
  summarization strategies) — those are tactics on top of these
  principles, and belong in dedicated skills once actually needed.

## Notes
Exists to keep `INDEX.md` and this registry honest — re-read it if the
index starts trending toward "load everything."
