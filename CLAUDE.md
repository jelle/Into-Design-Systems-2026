# Into Design Systems AI Conference 2026

Knowledge base for the Into Design Systems AI Conference (March 19-20, 2026). Contains transcripts, outlines, slide screenshots, and full narrative reconstructions of conference talks.

## Purpose

- Personal knowledge base for Jelle (attended the conference)
- Share key talks with colleagues via GitHub
- Each talk gets a reconstructed "presentation article" combining screenshots + narrative

## Structure

```
Into Design Systems 2026/
├── CLAUDE.md              # This file
├── talks/                 # Full presentation reconstructions (one folder per talk)
│   ├── 216-product-primitives/
│   │   ├── presentation.md    # Narrative source (markdown)
│   │   ├── presentation.html  # Rendered for sharing
│   │   └── img/
│   │       └── frame-*.jpg    # Video screenshots
│   └── transcripts/           # Raw transcripts (all talks)
├── outlines/              # Quick 10-15 bullet summaries per talk
├── slides/                # PDF slide decks (where available)
└── scripts/               # Tools for processing talks
    ├── preview_md.py              # Render markdown as Medium-style HTML
    ├── download_ids_transcripts.py # Download subtitles from Mux
    └── screenshot_video.py         # Screenshot video frames via Playwright
```

## How to Process a New Talk

Use `/process-talk <page_id> <title-slug>` or follow these manual steps:

### 1. Transcripts (already done for all 20 talks)
Raw transcripts live in `talks/transcripts/`. These were extracted from Mux VTT subtitles.

### 2. Outlines (already done for all 16 main talks)
Quick 10-15 bullet summaries in `outlines/`. Good for scanning what a talk covers.

### 3. Full Presentation Reconstruction
This is the premium artifact — a narrative article with embedded screenshots.

**Step 1: Screenshot the video frames**
- Requires Chrome DevTools MCP (Playwright can't bypass DRM)
- Navigate to `https://videos.intodesignsystems.com/videos/<page_id>`
- Seek every 60s, take screenshot of the `mux-player` element
- Save as `talks/<id>-<slug>/img/frame-XXXX.jpg`

**Step 2: Write the narrative**
- Read the full transcript from `talks/transcripts/`
- View key screenshots to understand slide content
- Write a coherent article (NOT a transcript dump) that follows the talk's arc
- Use relative image paths: `![alt](img/frame-XXXX.jpg)`
- Save as `talks/<id>-<slug>/presentation.md`

**Step 3: Render HTML**
```bash
python3 scripts/preview_md.py talks/<id>-<slug>/presentation.md
```
This generates `presentation.html` next to the markdown, with images embedded.

## Talk Catalog

| ID | Title | Transcript | Outline | Presentation |
|----|-------|-----------|---------|-------------|
| 210 | Bonus: Spotify Design System | Yes | Yes | Done |
| 211 | Bonus: Context-Based Design Systems | - | - | - |
| 212 | Bonus: Escaping the AI pit of death | - | - | - |
| 213 | Day 1 - Intro | Yes | - | - |
| 214 | Prototyping for the unknown | Yes | Yes | - |
| 215 | WhatsApp Web: Vibe Coding | Yes | Yes | - |
| 216 | Product Primitives | Yes | Yes | Done |
| 217 | Path to AI-enabled design system (Miro) | Yes | Yes | - |
| 218 | Agentic Design Systems | Yes | Yes | - |
| 219 | I'm not an engineer but I ship code | Yes | Yes | - |
| 220 | Context > Probability: DS as AI infra | Yes | Yes | - |
| 221 | Encoding governance on agentic DS | Yes | Yes | - |
| 222 | Day 1 - Outro | Yes | - | - |
| 223 | Day 2 - Intro | Yes | - | - |
| 224 | Building real DS with agents | Yes | Yes | - |
| 225 | Vibe coding zero drift (Figma→Storybook→Prod) | Yes | Yes | - |
| 226 | Machine-Readable DS for MCP and LLMs | Yes | Yes | - |
| 227 | From markdown to solving real problems | Yes | Yes | - |
| 228 | Ship It! Vibe Coding Figma Plugin | Yes | Yes | - |
| 229 | Designers Who Ship (48hr plugin) | Yes | Yes | - |
| 230 | AI Without the Chaos | Yes | Yes | - |
| 231 | Day 2 - Outro | Yes | - | - |

## Video Platform Access

- Platform: `videos.intodesignsystems.com` (magic-link auth, email-based)
- Video hosting: Mux (JWT-signed HLS streams, Widevine DRM)
- Subtitles: English VTT via Mux CDN (signed URLs, fetched via browser auth)
- Screenshots: Only possible via Chrome DevTools MCP (DRM blocks Playwright/canvas)

## Scripts

- `scripts/preview_md.py <file.md>` — Render markdown as styled HTML (Medium-like). Generates `.html` next to the `.md` file. Images use relative paths.
- `scripts/download_ids_transcripts.py` — Batch download all Mux subtitles. Requires fresh signed URLs from browser session (URLs expire).
- `scripts/screenshot_video.py <page_id> <slug> [interval]` — Screenshot video frames. Note: only works with Chrome DevTools MCP due to Widevine DRM.

## For Colleagues

The `talks/*/presentation.html` files are self-contained and viewable in any browser. Share the repo and point people to these files. Each one is a full narrative reconstruction of the talk with embedded screenshots.
