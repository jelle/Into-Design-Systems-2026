# The Path to an AI-Enabled Design System
**Speaker**: Andressa (design system lead, Miro) and Eddie (design engineer, Miro)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **The threat is real and it came fast** — Miro's leadership explored whether AI could auto-generate a design system from brand guidelines without involving the DS team. The team realized: if they didn't make AI work within the system, someone else would do it without them.

2. **Treat AI as a new hire, not a tool** — They framed AI as "Ora" — a new team member who is enthusiastic, capable, extremely literal, and has zero tolerance for ambiguity. This mindset reframed everything from documentation to onboarding to testing.

3. **Three onboarding principles that also work for AI** — Show don't tell (explain the why and the why-not), be consistent (mixed messages break AI reasoning), give room to experiment (space to try, fail, and self-correct).

4. **Bad output is a documentation problem, not an AI problem** — When Ora picked the wrong icons, it wasn't a model failure — the icons were named for visual appearance, not usage. Adding descriptions, use cases, and "do not use for" rules fixed the errors completely.

5. **Token ambiguity is equally lethal** — Two tokens both labeled "white" led to using a deprecated token. Adding clear descriptions ("background for toolbars and panels, do not use for cards") resolved the issue. Context quality determines output quality.

6. **The unglamorous work is the foundation** — Senior leadership told them documentation had no value. But without legible metadata, no MCP or AI integration produces good results. The lesson: prove concept first, explain value second.

7. **Build an MCP to control output when you can't control input** — Since humans prompt unpredictably, they built a custom MCP (starting with just two tools: list components, get component docs) to standardize what AI reads. Support questions in their Slack channel dropped 70-80%.

8. **Skills before MCP tools** — When building new capabilities (search icons, search tokens), they built Claude skills first — simple, fast to iterate, and compressible. One skill went from 33,000 tokens down to 410 tokens (98% reduction) after optimization with /simplify.

9. **A "wrap-up" skill standardizes all contributions** — Before submitting a PR, the skill runs the linter, checks accessibility and localization, writes commit descriptions, and structures the PR from a template. More contributions come in because the friction is gone.

10. **Ora filed 17 PRs in one hour on her first day of bug work** — After tagging Jira tickets as "Ora ready," she scans them, does the work, runs the wrap-up skill, and submits. Autonomous token renaming and icon cleanup are next.

11. **Frictionless MCP adoption kills your own visibility** — When Ora became invisible in workflows (a good sign), the team lost direct metrics on usage. Any figure is better than no figure — even testimonials from engineers on time saved.

12. **You don't need a perfect system, you need a legible one** — The core lesson: extract everything that lives in your heads into markdown files. You don't need a fancy AI integration to start. A system that is legible enough to teach is enough.

13. **The design systems role is evolving to teacher and onboarder** — Your job was always to document and govern. AI doesn't change that — it makes it more urgent. The person who knows how the system works and can teach it is still irreplaceable.
