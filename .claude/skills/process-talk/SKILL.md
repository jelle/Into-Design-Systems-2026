# Process Talk

Reconstruct a conference talk into a narrative article with embedded screenshots.

Use this skill when the user says "process talk", "reconstruct talk", "build presentation for", or provides a talk ID to process.

## Input

A talk page ID (210-231) and optional title slug.

## Steps

1. **Check if transcript exists** in `talks/transcripts/`. If not, download it first (requires browser auth on videos.intodesignsystems.com).

2. **Screenshot video frames** via Chrome DevTools MCP:
   - Navigate to `https://videos.intodesignsystems.com/videos/<page_id>`
   - Click play, pause, then seek every 60 seconds
   - Screenshot the `mux-player` element to `talks/<id>-<slug>/frame-XXXX.jpg`
   - This requires an active authenticated browser session

3. **Read the full transcript** and view key screenshots to understand slide content.

4. **Write a narrative reconstruction** as `talks/<id>-<slug>/presentation.md`:
   - NOT a transcript dump — a coherent article that tells the talk's story
   - Organize around key ideas/sections, not timestamps
   - Embed screenshots at narrative-appropriate moments using relative paths
   - Include speaker name, role, and talk metadata at the top
   - Distill Q&A into topical highlights at the end
   - Use `![description](frame-XXXX.jpg)` for images

5. **Render HTML**: `python3 scripts/preview_md.py talks/<id>-<slug>/presentation.md`

6. **Update CLAUDE.md** talk catalog to mark the presentation as Done.
