---
id: grill-with-docs
name: grill-with-docs
display_name: Grill With Docs
description: Pressure-test a repo-level plan while recording only durable decisions
  and terminology that should survive the session.
type: skill
category: engineering
capabilities:
- planning
- documentation
- architecture-decisions
activation: explicit
requires:
- grill-me
conflicts: null
risk: low
disable-model-invocation: true
---

# Grill With Docs
## When to use
Same trigger as `grill-me` — a plan or design you want pressure-tested —
but for work landing in a real, ongoing repo, where you also want the
resolved decisions to stick around for the next session or the next
person.

## What it does
Runs the same relentless-interview pattern as `grill-me`, but writes as it
resolves things:
- A running glossary of project-specific terms, written once their
  meaning has actually been pinned down in conversation — not
  speculatively.
- A short decision record for any choice that clears three bars: it was
  genuinely contested, it would be expensive to reverse, and future-you
  would otherwise have to re-derive the reasoning. Skip anything that
  doesn't clear all three.
- Nothing gets written if nothing in the session actually got pinned
  down.

## Explicitly out of scope
- Work spanning multiple sessions — that's `wayfinder`; this skill can be
  one of the things wayfinder calls into for a single ticket.
- Needs a repo to write into. Use `grill-me` if there's nowhere safe to
  write, or you don't want files yet.

## Notes
Depends on `grill-me` for the interview mechanics — this skill only adds
the "write it down as you go" behavior on top.
