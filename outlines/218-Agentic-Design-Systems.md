# Agentic Design Systems
**Speaker**: Romina (design systems practitioner, designsystem.guide)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Design systems are infrastructure, not deliverables** — Frame them to leadership as the API that allows AI to build your product safely. The same way a database or pipeline is infrastructure, so is your design system.

2. **AI makes design systems more critical, not less** — AI generates code at scale; design systems generate understanding. Without the system governing it, AI-generated code creates inconsistency at scale. The risk of not having a strong system just got much higher.

3. **The shift from synthetic to semantic** — Developers now spend less time writing code and more time asking "what should this component do and why?" Design systems need to encode intent, not just structure — naming conventions, component purpose, usage guidelines, combination rules.

4. **Agents need something to read** — An agent without context will hallucinate. The foundation is a machine-readable index: component descriptions with intent, token taxonomy, relationship maps showing how components combine, and usage guidelines written for both humans and AI.

5. **MCP vs CLI: different tools for different jobs** — CLI is for direct, local, low-context tasks (change colors, resize images). MCP is for multi-agent orchestration where structured data from multiple tools (Figma, GitHub, analytics, docs) needs to be combined and acted on.

6. **Plant seeds before expecting a tree** — Fully autonomous agents that fix everything sound appealing but don't work without foundations. Naming conventions, token structure, and component intent descriptions must come first. The automation is built on top of that.

7. **The self-healing loop: monitor, analyze, plan, execute** — Inspired by IBM's MAPE framework (used in network infrastructure), this applies the same logic to design systems: detect signals (token drift, hex codes used instead of tokens), analyze health, plan fixes, execute with appropriate trust level.

8. **Trust levels govern agent autonomy** — Agents start as interns: they can flag issues and create PR tickets, but cannot execute changes autonomously. As they demonstrate accuracy, permissions expand. You decide what they can fix without review.

9. **The Tidy plugin: audit, validate, and compose in Figma** — A custom Figma plugin that audits token naming, scores design system health across six categories, validates new variables against naming conventions, and can compose component patterns (e.g., "create a login form" triggers the right components with correct tokens applied).

10. **A knowledge graph connects the whole system** — Figma, GitHub, Storybook, PostHog (usage analytics), Chromatic, Linear — all feeding into a unified graph. This lets agents know not just what components exist, but how they're used in the wild and what's drifting.

11. **A dashboard makes the invisible visible** — A vibe-coded dashboard gives a visual overview of what markdown files exist, which tools are connected, what errors are occurring, and what's in the inbox awaiting decisions. Built for herself as a visual person, it became essential for oversight.

12. **Automated documentation removes the biggest maintenance burden** — Using Mintlify (or Astro Starlight for free), a script watches for Figma changes and pushes updated documentation automatically. On a schedule or on every change — the docs stay current without manual effort.

13. **If rebuilding from scratch: nail the foundations, pair with a developer daily** — Spend the time you saved on AI execution on better design craft and deeper brand alignment. And don't work in isolation — pairing with a developer gives different perspectives and dramatically accelerates quality.
