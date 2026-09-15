---
id: wayfinder
name: wayfinder
display_name: Wayfinder
description: Plan genuinely multi-session work when the destination is known but the
  route and dependencies are still unclear.
type: skill
category: planning
capabilities:
- planning
- project-decomposition
- long-horizon-work
activation: contextual
requires: null
conflicts: null
risk: medium
disable-model-invocation: false
---

# Wayfinder
## When to use
The work is genuinely too big for one session, and the route to the goal
is still unclear — not just "many steps" but "unclear which steps, in
what order, touching what." Reaching for this on a well-scoped single
feature is the common mistake; if scope is already clear, use
`grill-with-docs` instead and skip the overhead.

## What it does
- Maps the effort as tickets with explicit blocking relationships between
  them, rather than a flat to-do list — so it's clear what can start now
  versus what's waiting on something else.
- Delegates the actual resolution of each ticket to a narrower skill:
  planning/decision tickets go to a grilling-style interview, research
  tickets run in isolation so their reading doesn't pollute the main
  session, implementation tickets go straight to build.
- The map lives wherever the project already tracks issues, not as a
  one-off document that goes stale.

## Explicitly out of scope
- Small, clearly-scoped changes — the ticket-map overhead isn't worth it.
- Does not implement anything itself; it schedules other skills/agents.

## Notes
Treat this as a scheduler, not a planner in its own right — its value is
in decomposition and sequencing, not in generating plan content.
