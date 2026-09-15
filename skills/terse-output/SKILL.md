---
id: terse-output
name: terse-output
display_name: Terse Output
description: Reduce non-technical conversational verbosity while preserving code,
  commands, errors, warnings, and required technical detail exactly.
type: skill
category: productivity
capabilities:
- communication
- token-efficiency
activation: explicit
requires: null
conflicts: null
risk: low
disable-model-invocation: true
---

# Terse Output
## When to use
Turn on deliberately, per session or per task, when you want shorter
replies — long explanatory prose costs both your time reading it and
tokens billed for writing it, and often neither is buying you anything.

## What it does
- Drops throat-clearing, restated context, and hedging language from
  prose replies.
- Leaves code, commands, file paths, and exact error text untouched —
  only the surrounding prose gets compressed, never anything that has to
  be copy-paste-exact.
- Scales the savings with how verbose the answer would otherwise have
  been: an answer that's already just a code diff won't shrink much,
  because there's nothing to cut.

## Explicitly out of scope
- Never on by default for a session — it changes how the agent
  communicates, and that should be your call each time, not an ambient
  setting.
- Not a substitute for shrinking what gets read back in (large logs,
  diffs, search results) — that's a separate problem this skill doesn't
  attempt. A read-side compression proxy exists upstream if you want
  that; see `sources/juliusbrussee.md`.

## Notes
Cheap to load, meaningfully changes behavior — good candidate to mention
per-task in `INDEX.md`, bad candidate for always-on.
