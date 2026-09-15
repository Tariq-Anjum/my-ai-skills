---
id: grill-me
name: grill-me
display_name: Grill Me
description: Pressure-test a plan or decision through a focused, one-question-at-a-time
  interview before committing to implementation.
type: skill
category: planning
capabilities:
- planning
- reasoning
- decision-review
activation: explicit
requires: null
conflicts: null
risk: low
disable-model-invocation: true
---

# Grill Me
## When to use
Invoke this manually when you have a plan, design, or decision that feels
settled but hasn't actually been stress-tested — before committing time or
code to it.

## What it does
Runs a structured interview instead of accepting the plan as given:
- Surfaces every branch point in the plan and asks about it explicitly,
  one round at a time, rather than one giant list of questions.
- For each question, states its own best guess first, so you're
  confirming or correcting rather than answering from a blank page.
- Treats an unengaged "agreed" as a failure mode — if you're approving
  everything in one word, the skill should slow down and ask a sharper
  question instead of moving on.
- Ends only when every open branch has an explicit answer, not when the
  conversation "feels" done.

## Explicitly out of scope
- Writing files, specs, or code — this is pure conversation. For the
  interview plus written docs, use `grill-with-docs` instead.
- Anything bigger than one sitting — hand that to `wayfinder`.

## Notes
Manual on purpose: an agent that decides on its own when your plan "needs"
grilling will annoy you constantly. You ask for this.
