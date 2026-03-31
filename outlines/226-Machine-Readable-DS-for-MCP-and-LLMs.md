# Machine-Readable Design Systems for MCP and LLMs
**Speaker**: Diana Ojosin, Senior Design System Designer at Indeed
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **AI is a new user of your design system** — Just as you structure components for human designers and developers, you now need to structure your knowledge so an LLM can parse, reason over, and build with it.

2. **Format matters more than content** — The same design system knowledge fed to an LLM in different formats produces dramatically different results; choosing the right format is not a technical detail, it is a design decision.

3. **Human-readable docs are not machine-readable docs** — MDX and narrative documentation written for humans is inconsistent, full of edge cases, and hard to parse reliably; a separate structured metadata layer is required for LLM consumption.

4. **JSON is the winner for component APIs** — After benchmarking Markdown, hybrid Markdown+JSON, and TSON (token-oriented object notation), structured JSON produced the highest LLM accuracy and the lowest token cost — 80% fewer tokens than the hybrid format for the same or better accuracy.

5. **Use Markdown (with frontmatter) for rules and instructions, not component specs** — Natural language in clean Markdown works well for behavioral guidelines; JSON works for component contracts (props, variants, constraints).

6. **The MCP is deterministic; the LLM is stochastic** — Send the same query to an MCP and you get the same result every time; send the same MCP output to an LLM and you get a different response every time — structured input reduces but does not eliminate that variation.

7. **Structured metadata measurably reduces hallucinations** — Benchmarking 1,056 prompts across 8 MCP configurations showed that JSON-based MCPs produced the most consistent, accurate responses with the fewest hallucinations compared to less structured formats.

8. **Build parsers to transform your existing docs into metadata** — You do not need to rewrite all documentation from scratch; JavaScript or Python parsers can transform MDX into structured JSON per component and automate this on every documentation update.

9. **Automate ingestion so the MCP stays fresh** — A CI/CD pipeline triggered on every docs commit runs the parsers, updates the JSON, chunks and indexes the metadata into the vector database — the LLM always receives current knowledge.

10. **Chunking strategy directly impacts retrieval quality** — The goal is the sharpest possible chunks so the vector similarity search returns the most relevant context; poorly chunked data returns noisy results even if the underlying documentation is good.

11. **Progressive disclosure is the load strategy** — Critical rules (spacing, color, typography) are always present in context (like a CLAUDE.md or rules file); component-specific knowledge is on-demand via MCP; this avoids burning the context window on irrelevant data.

12. **An AGENT.md is the orchestration layer** — Rules files are the safety net, MCP is the retrieval layer, AGENT.md is the orchestration layer; together they form a "plugin" — the convention now being adopted by Cursor and Claude Code.

13. **Token cost will be enforced eventually** — AI tool providers are currently not charging hard limits, but that will change; start measuring input and output tokens per MCP query now so you are not caught off guard when pricing tightens.

14. **Start by asking AI how to build the MCP** — The fastest way to learn this stack as a designer is to open Cursor, describe what you want to build, and iterate from there; no engineering background is required to get started.
