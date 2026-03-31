# Building Real Design Systems with Agents
**Speaker**: Jan Six, Product Designer at GitHub (also co-creator of Token Studio)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Agents are your new primary design system user** — More PRs are now created by coding agents than ever before, meaning your system must be legible to machines, not just humans.

2. **Designers can now ship production code without learning to code** — Tools like Claude Code, GitHub Copilot CLI, and desktop agent wrappers have removed the skill barrier entirely; the question is no longer "should designers code" but "who owns the front end now."

3. **Codebase drift is the #1 reason agents fail your system** — Conflicting CSS rules, outdated components, and mixed icon libraries cause agents to guess and take the path of least resistance instead of following your intent.

4. **Tribal knowledge kills agent output quality** — Unwritten rules are invisible to agents; anything not documented is something they will hallucinate around.

5. **Co-locate everything the agent needs** — Scattered docs force agents to miss context; a single folder per component (or a mono-repo approach) dramatically improves agent accuracy.

6. **Semantic token naming is not optional** — `green-600` tells an agent nothing; `color-danger-background` tells it everything, especially when colors morph across modes.

7. **Docs are now primarily consumed by agents, not humans** — Structured frontmatter, machine-readable metadata, and avoiding visual-only elements (badge images, etc.) should drive how you write component documentation.

8. **Build a prototyping environment close to production** — A lightweight sandbox using your real components lets designers and PMs build real ideas fast without polluting the production codebase; Notion and GitHub both use this pattern.

9. **Treat agent instructions as a router, not a dump** — Instead of one massive instructions file, route the agent to specific sub-documents (component specs, token rules, doc guidelines) based on what it is doing.

10. **MCPs and CLIs make your brand queryable** — An MCP for your tokens, icons, or brand rules lets agents pull the right context on demand without cluttering the repository; GitHub's Primer MCP is a live example.

11. **Skills and subagents let you delegate clean work** — Reusable skills handle repeat tasks; subagents do isolated work (e.g. accessibility review) without polluting the main agent's context window.

12. **A "brand core agent" is the next step beyond an MCP** — Instead of exposing raw tokens and components, a dedicated agent aggregates tokens, voice guidelines, rules, and component docs into one coherent response for your main coding agent.

13. **Automated agents can handle design system maintenance** — Scheduled cloud agents (GitHub Agent Workflows, Cursor background agents) can run daily audits, catch drift, and create issues without a human trigger.

14. **Spend time slowing down to audit before you speed up** — Any day invested in cleaning drift, co-locating docs, and writing specs pays back exponentially once agents are working in your actual codebase.
