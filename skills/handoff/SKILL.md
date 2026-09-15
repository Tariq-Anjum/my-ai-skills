---
id: handoff
name: handoff
display_name: Handoff
description: Create a compact continuation note for a new session, agent, or collaborator
  without duplicating the project's existing plan or specs.
type: skill
category: productivity
capabilities:
- context-transfer
- session-continuity
activation: explicit
requires: null
conflicts: null
risk: low
disable-model-invocation: true
---

# Handoff
## When to use
- You're ending a session before the task is finished.
- You're delegating a slice of work to a subagent or a fresh session and
  don't want it re-reading everything from scratch.

## What it does
Produces one compact document that lets a new session pick up exactly
where this one left off:
- What's actually done vs. still open, stated plainly.
- The decisions already made and why — pointing at existing specs/ADRs/
  plans rather than restating them. A handoff doc that duplicates the
  plan it's handing off is doing too much.
- Anything the next session should NOT redo (dead ends already explored,
  approaches already rejected and why).

## Explicitly out of scope
- Not a replacement for the underlying plan/spec/ADR files — it points at
  them, it doesn't copy them.

## Notes
Pairs naturally with `file-based-planning`: if the task was already using
persistent plan files, this should mostly summarize their current state
rather than re-deriving it.
