#!/usr/bin/env python3
"""Re-render all presentation.md files with navigation."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from preview_md import md_to_html, build_html

TALKS = [
    ("talks/210-spotify-design-system", "Bonus: Spotify Design System"),
    ("talks/214-prototyping-for-the-unknown", "Prototyping for the Unknown"),
    ("talks/215-whatsapp-vibe-coding", "WhatsApp Web: Vibe Coding"),
    ("talks/216-product-primitives", "Product Primitives"),
    ("talks/217-ai-enabled-design-system-miro", "AI-Enabled Design System (Miro)"),
    ("talks/218-agentic-design-systems", "Agentic Design Systems"),
    ("talks/219-designers-ship-code", "I'm Not an Engineer but I Ship Code"),
    ("talks/220-context-probability-ds-ai-infra", "Context > Probability"),
    ("talks/221-encoding-governance-agentic-ds", "Encoding Governance"),
    ("talks/224-building-real-ds-with-agents", "Building Real DS with Agents"),
    ("talks/225-vibe-coding-zero-drift", "Vibe Coding Zero Drift"),
    ("talks/226-machine-readable-ds-mcp-llms", "Machine-Readable DS for MCP/LLMs"),
    ("talks/227-markdown-to-real-problems", "From Markdown to Real Problems"),
    ("talks/228-ship-it-vibe-coding-figma-plugin", "Ship It! Figma Plugin"),
    ("talks/229-designers-who-ship-48hr-plugin", "Designers Who Ship (48hr Plugin)"),
    ("talks/230-ai-without-chaos", "AI Without the Chaos"),
]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def relative_path(from_dir, to_dir):
    """Get relative path from one talk dir to another."""
    from_parts = from_dir.split("/")
    to_parts = to_dir.split("/")
    return f"../{to_parts[-1]}/presentation.html"

for i, (talk_dir, talk_title) in enumerate(TALKS):
    md_path = os.path.join(ROOT, talk_dir, "presentation.md")
    if not os.path.exists(md_path):
        print(f"  SKIP {talk_dir} (no presentation.md)")
        continue

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    title = os.path.basename(talk_dir)
    body_html = md_to_html(md_text)

    # Wrap "Key Insights" section in a collapsible details element
    import re as _re
    insights_match = _re.search(
        r'(<h2>Key Insights.*?</h2>)(.*?)(?=<nav class="nav-bottom"|$)',
        body_html, _re.DOTALL
    )
    if insights_match:
        h2_tag = insights_match.group(1)
        content = insights_match.group(2)
        replacement = (
            f'<details class="insights"><summary>Key Insights &amp; Takeaways</summary>'
            f'<p class="insights-disclaimer">AI-generated analysis based on the talk content. These insights are not from the speaker.</p>'
            f'{h2_tag}{content}</details>'
        )
        body_html = body_html[:insights_match.start()] + replacement + body_html[insights_match.end():]

    # Build back link
    # Depth from talk dir to root is 2 levels (talks/xxx/)
    nav_top = '<div class="nav-back"><a href="../../index.html">&larr; All talks</a></div>'

    # Build prev/next
    nav_parts = []
    if i > 0:
        prev_dir, prev_title = TALKS[i - 1]
        prev_href = relative_path(talk_dir, prev_dir)
        nav_parts.append(
            f'<a class="nav-prev" href="{prev_href}">'
            f'<span class="nav-label">&larr; Previous</span><span class="nav-title">{prev_title}</span></a>'
        )
    else:
        nav_parts.append('<span></span>')

    if i < len(TALKS) - 1:
        next_dir, next_title = TALKS[i + 1]
        next_href = relative_path(talk_dir, next_dir)
        nav_parts.append(
            f'<a class="nav-next" href="{next_href}">'
            f'<span class="nav-label">Next &rarr;</span><span class="nav-title">{next_title}</span></a>'
        )
    else:
        nav_parts.append('<span></span>')

    nav_bottom = f'<nav class="nav-bottom">{"".join(nav_parts)}</nav>'

    full_html = build_html(title, body_html, nav_top=nav_top, nav_bottom=nav_bottom)

    html_path = os.path.join(ROOT, talk_dir, "presentation.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"  OK {talk_dir}")

print(f"\nRendered {len(TALKS)} presentations.")
