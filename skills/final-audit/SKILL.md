---
id: final-audit
name: final-audit
display_name: Final Audit
description: Independently audit completed implementation work before acceptance when another agent, developer, or prior pass claims the task is finished, production-ready, safe, or ready to merge.
type: skill
category: engineering
capabilities:
  - code-review
  - implementation-audit
  - production-readiness
  - verification
activation: contextual
requires: []
conflicts: []
risk: low
disable-model-invocation: false
---

# Final Audit

## When to use

Use this skill when the user asks to:

- audit an implementation
- review work completed by another agent
- verify a "done" or "production-ready" claim
- check a patch before merge
- perform a final review
- provide an independent second opinion on completed engineering work

Do not use it for ordinary implementation unless the task includes a review or
acceptance decision.

## Core rule

Review independently.

Do not assume work is correct because:

- another model says it is complete
- tests were reported as passing
- a previous review approved it
- the implementation looks plausible
- the user expects it to be finished

Verify material claims against the actual repository and evidence.

## Audit workflow

### 1. Establish scope

Identify:

- requested behavior
- applicable AGENTS.md instructions
- relevant architecture or design constraints
- changed files or diff
- tests and validation that were claimed

Avoid widening the audit into unrelated refactoring.

If the current directory is not a repository, identify the intended repository
from the user's request, current project context, or an unambiguous active
worktree.

Do not silently combine unrelated dirty repositories into one audit. If more
than one repository is plausibly the target, state the ambiguity and restrict
the audit to the repository best supported by the available context.

### 2. Inspect actual implementation

Prefer direct evidence:

- git diff
- changed files
- surrounding code
- configuration
- schemas and interfaces
- tests
- relevant documentation

Do not review only an agent's summary when the implementation is available.

### 3. Check correctness

Look for material issues including:

- incorrect behavior
- incomplete implementation
- regression risk
- unhandled failure modes
- invalid assumptions
- edge cases
- stale or inconsistent state
- error propagation problems

### 4. Check boundaries

When relevant, inspect:

- authorization and permissions
- input validation
- secret handling
- privilege boundaries
- external egress
- concurrency and races
- cancellation
- retries and idempotency
- resource lifecycle
- persistence consistency

### 5. Check architectural fit

Verify that the implementation respects established project boundaries and
does not silently introduce:

- unwanted vendor coupling
- unnecessary dependencies
- duplicated abstractions
- bypasses around policy or validation layers
- excessive background resource use
- brittle shell or filesystem assumptions

### 6. Verify claims

Run the smallest relevant validation needed to substantiate the review when
testing is authorized and appropriate.

Never claim that a test, build, lint, benchmark, or command passed unless it
actually ran and succeeded.

If something cannot be verified, state that explicitly.

## Findings

Prioritize concrete issues.

For each significant finding, include:

- severity
- affected file or component
- evidence
- practical impact
- recommended correction

Distinguish:

- blockers
- important non-blockers
- optional improvements

Do not manufacture findings merely to make the review appear rigorous.

## Completion

If no material defects are found, say so clearly.

Still report:

- what was inspected
- what was verified
- what was not verified
- residual risks or uncertainty

Do not keep extending the review after additional work is unlikely to change
the acceptance decision.
