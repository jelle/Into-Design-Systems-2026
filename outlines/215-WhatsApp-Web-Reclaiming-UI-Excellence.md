# WhatsApp Web: Reclaiming UI Excellence through Vibe Coding
**Speaker**: Sebastian Rousseau, Web Design System Lead, WhatsApp
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **A product is what your code says it is, not what your Figma file says** — Design files show intent; code is what users actually experience. AI coding finally gives designers the tools to close that gap themselves.

2. **A lean team forced a rethink** — WhatsApp web had 400M monthly active users but a 10-year-old experience. With one engineer and one designer, Sebastian had to find a fundamentally different way to ship.

3. **Machine-readable assets are the prerequisite** — Before AI tools could be useful, all design assets, documentation, and components needed to be in machine-readable formats with proper MCP connections set up.

4. **Three use cases that matter most** — Auditing the codebase (understand before designing), exploring designs in code (replace Figma prototypes with real implementations), and shipping small fixes directly as a designer.

5. **Use AI to audit the codebase before designing** — Instead of reading docs and asking engineers, Sebastian asks Claude Code to find all instances of a component, list its properties, and show where it's used — surfacing legacy naming and real usage before touching a design.

6. **Skip the Figma prototype, go straight to code** — For interaction-heavy decisions (muscle memory, spacing, animation, keyboard nav), Figma can't give you the answer. Getting to code fast lets you sit with the real thing for days before deciding.

7. **Death by a thousand cuts, fixed at scale** — Small visual inconsistencies are impossible to justify as one-off engineer tasks. With AI coding, designers can fix tokens, icons, spacing, and outdated components themselves — over 100 fixes shipped solo in months.

8. **Start small at enterprise scale** — Begin with color token changes and icon swaps, not features. Stability matters more at enterprise scale than the startup "go wild" approach. Gradually extend to components, then features.

9. **Always read the output, even if you can't write it** — You don't need to have written the code yourself, but you need to understand what the AI produced before it goes to review. Think: you can read a language you can't yet speak.

10. **Multiple safeguards still matter** — Every AI-generated code change runs through automated linters (flagging hard-coded values vs. tokens), passes a human engineer review, and still goes through design reviews. It's fast, but not ungoverned.

11. **The designer role expands, the team speeds up** — Designers spend more time per feature, but the org as a whole moves much faster because engineers aren't blocked waiting on specs and handoffs.

12. **Code is becoming the source of truth** — Design files go stale and are expensive to keep in sync. The closer you get to treating code as the authoritative record of design decisions, the better it serves every role on the team.

13. **Build a visual prompting tool to onboard the team** — WhatsApp built an internal browser plugin that lets anyone hover over a UI element and fire a prompt with full React context auto-attached — dramatically lowering the bar for non-engineers to start coding.
