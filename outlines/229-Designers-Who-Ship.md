# Designers Who Ship — Building a Real Plugin in 48 Hours with AI
**Speakers**: Raquel (Lead Designer, Portugal), Cassandra Sandhu (Design System Specialist, Denmark), Christoph Helmut (Design System Lead, Germany) — Hackathon winners, Into Design Systems 2026
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Don't open Cursor first** — Spending the first few hours on product scope definition (must-have / nice-to-have / out of scope) saved the team from building the wrong thing under time pressure.

2. **Do technical research before writing any prompts** — The team discovered a critical Figma API constraint (no external library browsing from inside a plugin) only through pre-prompting research; finding it late would have wasted hours.

3. **A vague prompt is 500x more expensive than a clear one** — Tested side by side: a vague prompt cost ~$9 and took minutes with low accuracy; a well-structured prompt cost almost nothing and answered in seconds.

4. **Good prompts have three ingredients: clarity, context, constraints** — Specify exactly what you want, give the AI your tech stack and goals, and tell it what to avoid; missing any one of these makes the AI guess.

5. **Start a new session for each new feature** — Mixing features in the same context window balloons token usage and degrades output quality; session hygiene is a real cost lever.

6. **GitHub is non-negotiable for team vibe coding** — With 10 people across time zones, a shared repo was the only way to have a source of truth, track changes, and roll back when things broke.

7. **Use AI to generate UI variations, then curate the best parts** — Rather than designing from scratch, the team prompted for multiple interface options and combined the strongest elements into a cohesive design.

8. **Debug mode beats trial-and-error fixing** — Providing a screenshot of the broken state and asking the AI to add instrumentation logs before guessing at fixes resolved most bugs in one shot.

9. **Version control before every change** — Committing working code before each agent session means catastrophic failures are always recoverable in seconds, not hours.

10. **AI skills transform a general agent into a domain expert** — A Figma plugin developer skill (trigger + instructions + reusable code snippets) gave the agent deep API knowledge without burning tokens re-learning it each session.

11. **4,000 lines of prototype code needs a post-hackathon refactor** — Shipping a working prototype and then cleaning up the architecture separately is a valid strategy; the refactor is where the plugin becomes maintainable.

12. **Your plugin CSS is your brand guide** — Reusing the plugin's existing styles in Lovable to generate a marketing landing page took under an hour and required no design work from scratch.

13. **Figma community listing is a discoverability decision** — Choosing the right category, adding keywords, and completing the data security section determines whether enterprise users can even access the plugin.

14. **The workflow is universal** — Plan before prompt, use the right mode (plan / agent / ask / debug), test after each feature, roll back on breaks; the tools will change but these principles stay constant.
