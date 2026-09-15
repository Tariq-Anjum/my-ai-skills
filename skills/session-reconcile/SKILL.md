---
id: session-reconcile
name: session-reconcile
display_name: Session Reconcile
description: Reconcile session changes against project docs, agent instructions, and
  memory so the recorded system state does not drift from reality.
type: skill
category: meta
capabilities:
- maintenance
- documentation-hygiene
- memory-hygiene
activation: contextual
requires: null
conflicts: null
risk: low
disable-model-invocation: false
---

# Session Reconcile
## When to use
At the end of a working session, before closing out — especially one that
touched code, docs, or made decisions worth remembering.

## What it does
Checks what actually changed in the session against three places that
tend to drift out of sync with reality:
- The docs (README, architecture notes) — do they still describe the
  system as it now stands?
- The root agent-instructions file (CLAUDE.md/AGENTS.md-equivalent) — did
  this session establish a convention or constraint that belongs there?
- The agent's own memory system — is there a fact or decision from this
  session worth persisting that hasn't been?
Flags mismatches rather than auto-editing everything silently — a
reconciliation pass should surface drift for a human decision, not
quietly rewrite documentation based on inference.

## Explicitly out of scope
- Not a substitute for `handoff` — reconcile keeps the project's own
  record straight; handoff gets a specific next session up to speed.

## Notes
Good closing habit, but keep it contextual/manual rather than automatic —
you don't want every trivial session triggering a full pass.
