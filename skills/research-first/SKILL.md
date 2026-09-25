---
id: research-first
name: research-first
display_name: Research First
description: Research current or uncertain external technical facts before deciding when freshness, versions, evidence, or real-world experience could materially change the answer.
type: skill
category: research
capabilities:
  - technical-research
  - source-verification
  - current-information
activation: contextual
requires: []
conflicts: []
risk: low
disable-model-invocation: false
---

# Research First

## When to use

Use this skill when a task materially depends on information outside the
current repository or conversation that may be:

- current or recently changed
- version-specific
- unfamiliar or uncertain
- disputed
- poorly documented
- dependent on real-world experience

Typical examples include:

- evaluating a new model, framework, agent, library, plugin, or repository
- comparing current tools or architectures
- checking Linux/software behavior that may have changed
- investigating recent releases, regressions, issues, or compatibility
- validating a technical claim before making an architectural decision
- deep-diving an external project

Do not use it merely because web access exists.

For self-contained implementation, debugging, or review work where current
external facts cannot materially affect the result, work directly from the
repository instead.

## Research workflow

### 1. Define the uncertainty

Identify the specific question, claim, comparison, or decision that requires
external evidence.

Do not begin with broad undirected searching.

### 2. Prefer primary evidence

Use the strongest relevant source available.

Prefer roughly:

1. official documentation and specifications
2. upstream source code and release notes
3. primary papers or technical research
4. GitHub issues, pull requests, commits, and maintainer discussions
5. Hugging Face repositories/model cards when relevant
6. project or Linux community forums
7. Reddit and similar communities for experience reports

Community discussions are useful for operational experience but are not
automatically authoritative.

### 3. Check freshness and applicability

Verify when relevant:

- publication or release date
- software/model version
- operating-system or platform assumptions
- whether an issue is still open or already fixed
- whether documentation describes the current release
- whether a benchmark actually measures the claimed workload

Do not silently apply evidence from an old version to a current one.

### 4. Inspect implementation when necessary

When documentation and observed behavior disagree, inspect source code,
commits, issues, or tests when practical.

Do not rely on search-result snippets when the underlying source can be read.

### 5. Cross-check consequential claims

For claims that materially affect an architecture, migration, purchase,
security decision, or significant implementation choice, seek independent
confirmation where practical.

Do not collect additional sources once they are unlikely to change the
decision.

### 6. Separate evidence from judgment

Distinguish clearly between:

- verified facts
- maintainer/vendor claims
- community experience
- inference
- recommendation
- unresolved uncertainty

Do not turn anecdotal consensus into a verified fact.

## Output

Synthesize the evidence rather than dumping search results.

Lead with the finding that matters to the task.

Include the important tradeoffs and uncertainty.

Cite or identify the sources supporting consequential claims.

If current evidence does not support a confident conclusion, say so.

## Context discipline

Keep research isolated from the main task as much as practical.

Do not load large unrelated pages, repositories, issue threads, or documents
into context.

Extract only the evidence necessary for the current decision.

If research grows into a genuinely multi-session investigation with unclear
dependencies, hand planning off to `wayfinder`.
