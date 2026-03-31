# AI Without the Chaos — Context-Based Design Systems to the Rescue
**Speakers**: TJ (South Left agency, design systems + AI), Brad Frost, Ian Frost
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Design systems are the guard rail for generative AI** — Generative AI can produce anything, but without the constraints and standards of a design system, the output is chaos; the two need each other.

2. **The "check engine light" problem is widespread** — Most organizations have a design system that mostly works, but drift accumulates silently — in tokens, components, metadata — until something breaks expensively.

3. **Figma MCP opened the door to programmatic design work** — Figma Console MCP enables AI agents to read, modify, and audit Figma files directly from the terminal, making design engineering workflows possible.

4. **Figma Lint was born from agency self-defense** — When inheriting design files before dev handoff, the team needed automated checks for missing components, hardcoded values, and absent metadata; they built the linter themselves.

5. **Design-to-code parity checks catch drift early** — Running a parity check between the Figma component and its code counterpart surfaces exactly what diverged, who should fix it, and how far it's drifted.

6. **The canonical source of truth is flexible** — Sometimes design leads, sometimes code leads; the important thing is knowing which direction to sync and using tooling to measure the gap, not assuming alignment.

7. **Cross-library component pulling is now scriptable** — An agent can be prompted to pull the button from four different shared libraries, drop them on a shared canvas, and label each one by source in a single run.

8. **Leave comments or file tickets, don't just fix silently** — After a parity check, the right action depends on role: designers get a Figma comment, developers get a GitHub issue; AI can create both automatically.

9. **Context-based design systems make AI generation reliable** — When components are built with rich context (purpose, constraints, usage rules) embedded in Storybook or docs, AI can generate correct variations without hallucinating.

10. **Story UI solves the estimation problem for agencies** — When every composed component variation could be infinite, an AI tool that understands your component context can generate Storybook stories on demand, capping scope creep.

11. **Three lenses for AI + design systems** — Use AI to make design systems better (linting, parity), use them together to build better products (generation with context), and use them together to shape the future of UX (new interaction paradigms).

12. **Communication is always the core problem** — Across every design systems team they've worked with, the pattern is the same: tooling helps, but the real issue is always communication between design and engineering, and AI can mediate that gap.
