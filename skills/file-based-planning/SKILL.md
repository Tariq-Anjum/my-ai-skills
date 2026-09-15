---
id: file-based-planning
name: file-based-planning
display_name: File-Based Planning
description: Persist the plan, findings, decisions, and errors for long-running work
  so progress survives context resets or crashes.
type: skill
category: planning
capabilities:
- planning
- persistence
- crash-recovery
activation: contextual
requires: null
conflicts: null
risk: low
priority: foundational
disable-model-invocation: false
---

# File-Based Planning
## When to use
Any task long enough, or with enough tool calls, that losing the thread
after a context reset, a crash, or a `/clear` would actually cost you
something.

## What it does
Keeps three small files on disk instead of only in the conversation:
- A plan file: the phases of the task and which are done.
- A findings file: anything discovered mid-task (search results read,
  files inspected, dead ends) — updated as it happens, not reconstructed
  from memory afterward.
- A decisions/errors log: anything that took a wrong turn or required a
  judgment call, so it isn't repeated.
The plan file gets re-read before any major action, specifically to
counter the failure mode where an agent forgets its original goal after
enough tool calls have gone by.

## Explicitly out of scope
- Short, single-shot tasks — the file overhead isn't worth it if the
  whole task fits in one exchange.

## Notes
Directly supports the disaster-recovery goal behind this whole registry:
work survives even if the session doesn't.
