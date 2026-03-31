# From Falling for Markdown to Solving Real Problems with Scripts
**Speaker**: Laura, Designer at Figma (previously HelloFresh)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Markdown isn't about formatting — it's about communication** — Plain text with structure is the bridge between human intent and machine understanding; without it, AI guesses wrong.

2. **Documentation has two audiences now** — Humans skim, machines parse; AI-readable guidelines must be structured, explicit, modular, and predictable, not conversational.

3. **Guidelines are context, not laws** — A rule file enriches the AI's environment, but prompts always win; the goal is literacy, not control.

4. **Split your Markdown into multiple small files** — A single giant doc overloads the context window and causes errors; modular files let the agent recall details accurately.

5. **Use frequency data in token docs** — Annotating spacing or typography tokens with usage percentages tells AI when and how often to apply them, reducing wrong picks.

6. **Add alternative names to components** — If your component has an unusual internal name, map it to common names so the AI matches intent correctly (e.g., "Lawson" → describe what it actually is).

7. **Curate options aggressively** — Agents perform worst when given too many choices; narrow the variants you expose to reduce token waste and wrong decisions.

8. **Messy Figma files produce messy code** — Inconsistent naming and structure in the design file directly cause inconsistent, broken AI output; clean inputs are non-negotiable.

9. **Drag-and-drop Markdown folders into Figma Make** — Guidelines can be structured as a folder and loaded into Figma Make's code editor tab without consuming any prompt credits.

10. **Obsidian is useful for building a design system mental model** — Its linked-note graph mirrors how language models connect concepts, making it a good companion for structuring DS docs.

11. **AI-era work is siloing designers again** — Individuals working in agents on local machines are recreating the silos design systems spent years tearing down; collaboration discipline matters more now.

12. **React-to-SwiftUI conversion is harder than it looks** — Cross-language framework translation via scripts and guidelines gets close but fails on fine details like SF Symbols, icon mapping, and native feel.

13. **Code is the source of truth** — When design and code diverge, the thing that reaches the user is what's valid; DS docs should trace back to the repo, not just Figma.

14. **The opportunity is enriching what already exists** — Most teams already have the knowledge; it's scattered across Figma, Notion, and docs. Structuring it compounds; rebuilding from scratch doesn't.
