# Prototyping for the Unknown
**Speaker**: Nate Baldwin, Senior Design Systems Designer (enterprise design systems, 10+ years)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Validation is the wrong tool for complex systems** — Validation only works when you already understand the problem. With complex systems, what you need first is discovery.

2. **Paving before exploring locks you in** — Teams under pressure implement the first reasonable idea, pour concrete, and end up on a path of no return — one that will never reach the intended destination.

3. **Use prototypes for discovery, not validation** — AI-assisted prototyping can reveal hidden constraints and system requirements you didn't know to ask about, before you've written a line of production code.

4. **Branch and burn: embrace productive failure** — Create dedicated git branches purely for sloppy AI explorations, let the AI fail freely, extract the insights, then delete the branch and keep only what you learned.

5. **SLOP reveals requirements** — Even when vibe-coded output is wrong or broken, the process of building it surfaces constraints, edge cases, and requirements you didn't know you had.

6. **Fragile prototypes destroy team trust** — A buggy prototype won't teach your team anything useful; they'll dismiss it. Aim for near-production quality so colleagues can evaluate actual viability, not just paper over bugs.

7. **Four-step structured prompting for production-quality output** — Context priming (deep analysis of existing system) → Detailed planning (comprehensive prompt-formatted plan) → Plan refinement (answer clarifying questions, review) → Implementation (execute the plan phase by phase).

8. **AI is exceptional at writing prompts for other AI** — When building the detailed plan, ask the agent to format it as prompts for an AI agent to follow — it will produce better instructions than you'd write manually.

9. **Force the agent to reuse existing code** — Without explicit instruction to use existing functions and components, AI will recreate them every time — even if your project rules say otherwise. Repeat yourself.

10. **Build tests into every implementation phase** — Without iterative tests during implementation, AI-generated code becomes so tangled that even the agent can't identify how to fix it.

11. **Human judgment is irreplaceable at the domain layer** — AI defaults to generic, shallow knowledge about design tokens. Deep expertise — knowing why basic data modeling principles apply to tokens — can't be prompted in from scratch.

12. **Eight weeks to a breakthrough** — One designer, working largely solo, used this process to prototype a complete token authoring ecosystem: taxonomy-based naming, multi-tenancy via GitHub, multi-dimensional token values, and a Figma variables pipeline.

13. **The prototype becomes a team compass** — Sharing the working prototype gave the whole team shared context, aligned conversations, and the clarity to plan a real build — something no slide deck or spec doc could have achieved.
