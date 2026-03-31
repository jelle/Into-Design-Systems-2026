#!/usr/bin/env python3
"""
Convert a markdown file to styled HTML and open in browser.
Usage: python3 preview_md.py <path-to-markdown-file>
"""

import sys
import os
import tempfile
import webbrowser
import re

def md_to_html(md_text):
    """Simple markdown to HTML converter — no dependencies needed."""
    html = md_text

    # Escape HTML entities (but preserve our own tags)
    html = html.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Code blocks (fenced) — must come before inline processing
    def replace_code_block(match):
        lang = match.group(1) or ""
        code = match.group(2)
        lang_attr = f' class="language-{lang}"' if lang else ""
        return f"<pre><code{lang_attr}>{code}</code></pre>"

    html = re.sub(r"```(\w*)\n(.*?)```", replace_code_block, html, flags=re.DOTALL)

    # Inline code
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)

    # Headers
    html = re.sub(r"^######\s+(.+)$", r"<h6>\1</h6>", html, flags=re.MULTILINE)
    html = re.sub(r"^#####\s+(.+)$", r"<h5>\1</h5>", html, flags=re.MULTILINE)
    html = re.sub(r"^####\s+(.+)$", r"<h4>\1</h4>", html, flags=re.MULTILINE)
    html = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^#\s+(.+)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", html)
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)

    # Horizontal rules
    html = re.sub(r"^---+$", "<hr>", html, flags=re.MULTILINE)

    # Tables
    def replace_table(match):
        lines = match.group(0).strip().split("\n")
        if len(lines) < 2:
            return match.group(0)

        rows = []
        for i, line in enumerate(lines):
            line = line.strip().strip("|")
            cells = [c.strip() for c in line.split("|")]

            # Skip separator row
            if all(re.match(r"^[-:]+$", c) for c in cells):
                continue

            tag = "th" if i == 0 else "td"
            row_html = "".join(f"<{tag}>{c}</{tag}>" for c in cells)
            rows.append(f"<tr>{row_html}</tr>")

        return "<table>" + "".join(rows) + "</table>"

    html = re.sub(r"(?:^\|.+\|$\n?)+", replace_table, html, flags=re.MULTILINE)

    # Unordered lists
    def replace_ul(match):
        items = re.findall(r"^[-*]\s+(.+)$", match.group(0), re.MULTILINE)
        li = "".join(f"<li>{item}</li>" for item in items)
        return f"<ul>{li}</ul>"

    html = re.sub(r"(?:^[-*]\s+.+$\n?)+", replace_ul, html, flags=re.MULTILINE)

    # Ordered lists
    def replace_ol(match):
        items = re.findall(r"^\d+\.\s+(.+)$", match.group(0), re.MULTILINE)
        li = "".join(f"<li>{item}</li>" for item in items)
        return f"<ol>{li}</ol>"

    html = re.sub(r"(?:^\d+\.\s+.+$\n?)+", replace_ol, html, flags=re.MULTILINE)

    # Images (must come before links)
    # Collect images first, replace with placeholders, then restore after paragraph wrapping
    _images = []
    def replace_image(match):
        alt = match.group(1)
        src = match.group(2)
        # Convert absolute paths to file:// URLs
        if src.startswith('/'):
            from urllib.parse import quote
            src = 'file://' + quote(src, safe='/:@')
        idx = len(_images)
        _images.append(f'<figure><img src="{src}" alt="{alt}" loading="lazy"><figcaption>{alt}</figcaption></figure>')
        return f'__IMG_PLACEHOLDER_{idx}__'

    html = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_image, html)

    # Blockquotes
    def replace_blockquote(match):
        lines = match.group(0).strip().split('\n')
        content = ' '.join(line.lstrip('> ').strip() for line in lines)
        return f'<blockquote><p>{content}</p></blockquote>'

    html = re.sub(r'(?:^&gt;\s*.+$\n?)+', replace_blockquote, html, flags=re.MULTILINE)

    # Links
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)

    # Paragraphs — wrap loose text lines
    lines = html.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped and not re.match(r"<(h[1-6]|ul|ol|li|pre|code|table|tr|th|td|hr|div|blockquote)", stripped):
            result.append(f"<p>{stripped}</p>")
        else:
            result.append(line)

    html_out = "\n".join(result)

    # Restore image placeholders
    for idx, img_html in enumerate(_images):
        # Remove paragraph wrapping around image placeholders
        html_out = html_out.replace(f'<p>__IMG_PLACEHOLDER_{idx}__</p>', img_html)
        html_out = html_out.replace(f'__IMG_PLACEHOLDER_{idx}__', img_html)

    return html_out


def build_html(title, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Charter:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: Charter, Georgia, 'Times New Roman', serif;
    background: #fff;
    color: #1a1a1a;
    font-size: 20px;
    line-height: 1.8;
    padding: 3rem 1.5rem;
    max-width: 740px;
    margin: 0 auto;
    -webkit-font-smoothing: antialiased;
  }}

  h1 {{
    font-family: Inter, -apple-system, sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #0a0a0a;
    margin: 0 0 0.5rem;
    line-height: 1.2;
    letter-spacing: -0.02em;
  }}

  h2 {{
    font-family: Inter, -apple-system, sans-serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: #0a0a0a;
    margin: 3rem 0 1rem;
    line-height: 1.3;
    letter-spacing: -0.01em;
  }}

  h3 {{
    font-family: Inter, -apple-system, sans-serif;
    font-size: 1.3rem;
    font-weight: 600;
    color: #1a1a1a;
    margin: 2rem 0 0.75rem;
    line-height: 1.4;
  }}

  h4, h5, h6 {{
    font-family: Inter, -apple-system, sans-serif;
    font-weight: 600;
    color: #1a1a1a;
    margin: 1.5rem 0 0.5rem;
  }}

  p {{
    margin: 1.25rem 0;
    color: #292929;
  }}

  a {{
    color: #1a8917;
    text-decoration: underline;
    text-decoration-color: rgba(26, 137, 23, 0.3);
    text-underline-offset: 2px;
    transition: text-decoration-color 0.2s;
  }}

  a:hover {{
    text-decoration-color: #1a8917;
  }}

  strong {{
    color: #0a0a0a;
    font-weight: 700;
  }}

  em {{
    font-style: italic;
  }}

  code {{
    font-family: 'SF Mono', 'Fira Code', Menlo, monospace;
    background: #f2f2f2;
    color: #1a1a1a;
    padding: 0.15em 0.4em;
    border-radius: 3px;
    font-size: 0.85em;
  }}

  pre {{
    background: #f7f7f7;
    border-radius: 6px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
    border: 1px solid #e6e6e6;
  }}

  pre code {{
    background: none;
    padding: 0;
    font-size: 0.8em;
    line-height: 1.6;
  }}

  ul, ol {{
    margin: 1.25rem 0;
    padding-left: 1.75rem;
  }}

  li {{
    margin: 0.6rem 0;
    color: #292929;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    font-size: 0.9em;
  }}

  th {{
    background: #f7f7f7;
    text-align: left;
    padding: 0.75rem 1rem;
    font-weight: 600;
    border-bottom: 2px solid #e0e0e0;
    font-family: Inter, -apple-system, sans-serif;
  }}

  td {{
    padding: 0.65rem 1rem;
    border-bottom: 1px solid #f0f0f0;
  }}

  hr {{
    border: none;
    height: 1px;
    background: #e0e0e0;
    margin: 3rem auto;
    max-width: 100px;
  }}

  blockquote {{
    border-left: 3px solid #1a1a1a;
    padding: 0.25rem 1.25rem;
    margin: 1.5rem 0;
    color: #555;
    font-style: italic;
  }}

  figure {{
    margin: 2.5rem -16rem;
    text-align: center;
  }}

  figure img {{
    width: 100%;
    max-width: 1800px;
    border-radius: 8px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
  }}

  figcaption {{
    font-family: Inter, -apple-system, sans-serif;
    font-size: 0.8rem;
    color: #999;
    margin-top: 0.75rem;
    font-style: normal;
  }}

  /* First paragraph after h1 = subtitle styling */
  h1 + p {{
    font-family: Inter, -apple-system, sans-serif;
    font-size: 0.95rem;
    color: #757575;
    line-height: 1.6;
    margin-bottom: 2rem;
    border-bottom: 1px solid #e6e6e6;
    padding-bottom: 1.5rem;
  }}

  ::-webkit-scrollbar {{ width: 6px; }}
  ::-webkit-scrollbar-track {{ background: transparent; }}
  ::-webkit-scrollbar-thumb {{ background: #ccc; border-radius: 3px; }}
</style>
</head>
<body>
{body_html}
</body>
</html>"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 preview_md.py <markdown-file>")
        sys.exit(1)

    md_path = sys.argv[1]

    if not os.path.exists(md_path):
        print(f"File not found: {md_path}")
        sys.exit(1)

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    title = os.path.basename(md_path).replace(".md", "")
    body_html = md_to_html(md_text)
    full_html = build_html(title, body_html)

    # Write HTML next to the markdown file (so relative image paths work)
    # Fall back to temp dir if the md file dir isn't writable
    md_dir = os.path.dirname(os.path.abspath(md_path))
    md_basename = os.path.basename(md_path).replace(".md", "")
    html_path = os.path.join(md_dir, f"{md_basename}.html")

    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)
    except OSError:
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(full_html)
            html_path = f.name

    webbrowser.open(f"file://{html_path}")
    print(f"Preview opened: {html_path}")


if __name__ == "__main__":
    main()
