---
id: karpathy-guidelines
name: karpathy-guidelines
display_name: Karpathy Guidelines
description: Coding-behavior guardrails inspired by the cited Karpathy-skills project.
type: guidance
category: meta
capabilities:
- coding-behavior
- quality-guardrails
activation: contextual
requires: []
conflicts: []
risk: low
---

# Karpathy Guidelines
## When to use
As background instruction for any coding agent/session — cheap to load,
broadly applicable, not tied to one task type.

## What it says
Four working rules distilled from commonly observed LLM coding failure
patterns:
1. **Don't silently assume.** If a requirement is ambiguous, say so and
   pick a stated, reasonable default — don't quietly run with a guess and
   let the person discover it later.
2. **Don't overbuild.** Prefer the smallest implementation that actually
   satisfies the ask. A 1000-line abstraction for a 100-line problem is a
   failure, not thoroughness.
3. **Stay in scope.** Don't edit, "clean up", or remove code or comments
   that weren't part of the request, even when they look wrong — flag it
   instead of touching it.
4. **State goals, not just steps, when possible.** Given a clear success
   condition, let the agent iterate and verify against it rather than
   spelling out every micro-step.

## Notes
Independently written, condensed version of the idea — not a copy of any
upstream file. Treat as a starting baseline; edit as you notice your own
recurring failure patterns.
