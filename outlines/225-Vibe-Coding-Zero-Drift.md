# Vibe Coding with Zero Drift — Figma to Storybook to Production
**Speaker**: Mr. Biscuit, co-creator of Variable Visualizer and design system UI kit
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **The wrong component problem is unsolvable by humans alone** — Visually similar components (chip vs. navigation tab, icon vs. button) are trivially misused by both humans and LLMs; the solution is to reduce choices, not add documentation.

2. **Merge components that share the same function and layout** — Categorize by function first, then merge those with identical purpose into fewer, smarter components rather than maintaining a sprawling library.

3. **Contextual awareness is the design principle that replaces component explosion** — A single component can morph into different visual states based on the container it lives in; this is achieved entirely through multi-modal Figma variables.

4. **Multi-modal variables are the core mechanism** — Stacking multiple variable collections (color mode, interactive state, panel context, density) lets one component adapt its appearance, visibility, spacing, and typography without forking into separate components.

5. **Contextual awareness is infinitely nestable** — A parent container can dictate mode to all children (dark/light), the interactive state collection adds hover/active layers on top, and a panel-type collection adds a third layer — you can stack as many levels as the component needs.

6. **Figma MCP translates bound variables directly into code** — When all layers have variables explicitly bound, the Figma MCP passes variable names and relationships to the LLM, which uses them to generate accurate, on-brand component code without guessing color values.

7. **The current Figma MCP gap: explicit mode overrides on layers** — The MCP does not yet pass which modes are explicitly set on individual layers, which is why Mr. Biscuit built a custom plugin to export the full variable logic as XML for the LLM.

8. **90% of the styling work happens in Figma, not in code** — Because all logic (color, visibility, spacing, font weight) is encoded as variables, the LLM only needs to wire them up; the hard decisions are already made in the design tool.

9. **Storybook is the verification layer before production** — Components land in Storybook first, all modes and states are validated, then the same component moves to production — the drift is zero because the source of truth is the Figma variable logic.

10. **Feed LLMs atomic components + molecules, not raw tokens or full screens** — Raw tokens leave too much room for misuse; full screens are too expensive to index; the sweet spot is bound components at atomic and molecule level, which carry tokens implicitly.

11. **JIT (just-in-time) composition is the near future** — AI will generate screens on demand for each user; a lightweight, contextually-aware component library is the right foundation for this; bloated libraries with hundreds of components will struggle.

12. **JIT component origination is also coming** — Beyond generating screens, AI will need to generate net-new molecule and pattern components from atomic building blocks; keeping the atom layer lean and well-structured is the prerequisite.

13. **Variable Visualizer exists because Figma tables break down at scale** — When aliasing spans three or four collections simultaneously, you lose sight of what flows where; a graph view across collections restores that clarity without leaving Figma.
