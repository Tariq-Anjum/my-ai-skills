# JuliusBrussee/caveman

Repo: https://github.com/JuliusBrussee/caveman
License: MIT (skill/CLI surfaces) / BSL-1.1 (engine/proxy) — per upstream
README, verify before relying on this.
What we took: the *idea* of a terse-output communication mode, reimplemented
as `skills/terse-output/SKILL.md`.
What we did NOT take: the read-side compression proxy (a local process that
shrinks logs/diffs/JSON before they reach the model). That's real
infrastructure with its own benchmarks and licensing split — if you want it,
install it directly from upstream rather than treating it as part of this
registry:
  npm install -g @caveman-ai/cli && caveman setup --install
Status: partially derived (skill) + not absorbed (proxy).
