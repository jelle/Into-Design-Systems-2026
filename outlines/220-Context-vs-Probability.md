# Context vs Probability — Design Systems as AI Infrastructure
**Speaker**: Jesse Gardner, Director of Accessibility and Design Systems, New York State Office of Information Technology Services
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Without context, AI defaults to the average of the internet** — Every new AI chat is like hiring a contractor with no brief. You will get the most probable output — likely Tailwind and React — not the correct output for your organization.

2. **AI does not fix design fragmentation — it amplifies it** — The old problem of different teams solving the same problems in isolation still exists. AI makes it worse in two ways: speed (it generates far more code, faster) and access (anyone can now ship without going through design or engineering review).

3. **Design systems are the AI infrastructure layer** — Tokens, components, usage guidelines, and accessibility standards are not just consistency tools; they are the structured context that makes AI output trustworthy and repeatable.

4. **Demonstrated with a real PDF-to-app build** — A 5-page government foster parent form was turned into a multi-step TypeScript web app in 13 minutes using the NY State design system MCP server. Imperfect, but days of work compressed into minutes.

5. **Use AI to audition components at scale** — Jesse generated 40 interaction patterns, built them all out using design system tokens, took Playwright screenshots at desktop and mobile, and dumped them into FigJam for team review. Gap analysis was automatic.

6. **The gap analysis revealed real system gaps** — Running components side by side at scale exposed mismatches (e.g. select height not matching input height) that are invisible in isolation. AI-accelerated exploration surfaces design debt fast.

7. **Connectedness is the core design system superpower** — When AI builds using design system components, every product stays connected to the source. A token change, accessibility fix, or dark mode rollout flows everywhere automatically. Custom AI-generated code is frozen the moment it ships.

8. **Accessibility baked in beats accessibility bolted on** — Components tested with native screen reader users encode that knowledge permanently. When AI builds from those components, it inherits that reflection. When it does not, it just goes fast — and nobody benefits.

9. **Reflect before you ship — speed is the enemy of judgment** — When things move fast, reflection is the first thing to go. The hardest design system work — deciding what to standardize, what makes a good experience for screen reader users, whether a pattern is right or just fast — requires slowing down.

10. **Intent is the designer's job now** — The question is not whether AI can generate interfaces; it can. The question is how well the design intent is encoded into structured, machine-readable infrastructure. Figma is one way to articulate intent, but how that intent gets translated will evolve.

11. **MCP servers are best for structured read-only context; skills for editable content** — When AI needs to query reference content, an MCP is ideal. When it needs to revise or update something, a markdown skill file that it can rewrite is better.

12. **For leadership: design systems are not a nice-to-have, they are core AI infrastructure** — Investing in a design system pays dividends across the entire organization as AI code generation scales. Structured context is what gets you speed at scale without sacrificing quality.

13. **Healthy AI skepticism is valid and important** — Especially in the public sector. Accessibility, privacy, and governance are not checkboxes. The 30% accessibility pass rate on AI-generated pages is a real problem, and human judgment cannot be fully delegated.

14. **Designers should learn to read code, not necessarily write it** — When designers understand code, they design better. Pairing designers with engineers to close that gap is what unlocks AI infrastructure. Better prompts alone do not get you there.
