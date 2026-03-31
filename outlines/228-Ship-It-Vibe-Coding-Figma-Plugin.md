# Ship It — Vibe Coding Your First Figma Plugin
**Speaker**: Davey Owens, Design System Designer at Atlassian (formerly Meta)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Every design system maintainer can build their own plugins** — With an AI agent and basic prompting skills, you don't need to be a developer to automate your own repetitive Figma tasks.

2. **Three files, that's all a plugin is** — `manifest.json` (the ID), `code.js` (the logic), and optional `ui.html` (the interface); understanding this unlocks everything.

3. **You need Figma desktop to sideload plugins safely** — Desktop dev mode lets you run your plugin locally without publishing it, so you can iterate freely without touching production.

4. **Headless vs. UI plugin is a scope question** — If it's just for you and does one thing, headless is fine; if others will use it or it needs inputs, build a UI.

5. **Prompt structure matters more than prompt length** — Define the task, the inputs, the edge cases to avoid, and the success notification; that structure produces reliable output every time.

6. **Use AI to improve your prompt before running it** — Paste your initial prompt into Claude or Gemini and ask for improvements first; this catches missing constraints before they cost you tokens.

7. **AI takes you literally, not intentionally** — Saying "make it two times bigger" will double the size numerically; vague language produces technically correct but wrong results.

8. **Token drift detection is a high-value plugin use case** — Davey's token sync plugin at Atlassian detects drift between design token packages and what's in Figma, flagging mismatches automatically.

9. **Metadata enrichment is underrated** — Bulk-adding component descriptions, keywords, and legacy name mappings via plugin turns a multi-day manual job into a two-minute automated one.

10. **Publishing to the community means you own it forever** — Once public, users will file requests and expect maintenance; be intentional about whether to keep plugins internal or share them.

11. **Plugin API has real limits** — Plugins operate within the current file only; they can't touch external libraries or run without manual initiation, so architect around those constraints early.

12. **The real next step is the REST API and pipelines** — Once comfortable with plugins, the evolution is token automation at the CI/CD level — GitHub Actions, Bitbucket pipelines — which is where persistent value lives.
