# A Design System That Enables Humans and Machines to Co-Create Production-Ready UI at Scale
**Speaker**: Victoria (web engineer) & Alex (product designer), Encore Design System team
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Design systems now have two audiences** — Encore was built for human designers and engineers, but AI coding agents have become a parallel consumer that the system must also serve.

2. **The communication path is breaking** — Previously, teams came to Encore directly for answers. Now they go to AI first, which may generate code that ignores design system standards entirely.

3. **Adoption at scale creates high stakes** — Encore's shared styles are used 220,000+ times, components appear in 86,000 places, and it holds a 93% satisfaction rate. That reach makes irrelevance a real risk.

4. **Build an MCP for your design system** — Spotify is building an Encore MCP (Model Context Protocol) so AI agents like Cursor have direct access to documentation, guidelines, and standards when generating code.

5. **Validate AI output, don't just hope** — They built a testing framework that evaluates LLM responses against Encore's actual components, checking linked errors, similarity scores, and visual output — not just code correctness.

6. **Rigid component architecture trips up AI too** — The current "bundles of behavior + style" model is inflexible for humans and creates large, confusing context bubbles for AI agents.

7. **Introducing a layered architecture** — Encore is separating components into three distinct layers: foundations, component styles, and component behaviors — so users (and AI) can mix and match precisely what they need.

8. **Build on headless component systems** — By using React ARIA or Base UI as the behavioral foundation, Encore offloads interaction logic (keyboard, accessibility, toggle states) and stays focused on what makes things feel like Spotify.

9. **Smaller context = better AI output** — With a layered architecture, AI agents can reason about one focused layer at a time instead of wrestling with a monolithic component definition.

10. **Your user base just expanded** — With AI lowering the barrier to building, the design system's users now include product managers, marketers, and anyone with an idea — not just designers and engineers.

11. **Be embedded everywhere, not just in documentation** — Encore's goal is to appear wherever someone is working: Slack bots, prototyping tools, Figma agents — meeting users in their workflow rather than waiting for them to visit the docs.

12. **The goal is human-machine co-creation** — The ultimate vision is a design system that enables anyone at Spotify — human or AI agent — to produce production-ready UI faster than ever before.
