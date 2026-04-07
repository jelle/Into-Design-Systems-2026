# Into Design Systems AI Conference 2026

**16 conference talks reconstructed as shareable blog-style articles** with embedded video screenshots and narrative summaries.

Open `index.html` to browse all talks, or dive into any `talks/*/presentation.html` directly.

---

## What is this?

I attended the [Into Design Systems AI Conference](https://www.intodesignsystems.com/) (March 19-20, 2026) and wanted to share key talks with colleagues who couldn't make it. Rather than just forwarding video links, I used Claude Code to reconstruct each talk as a readable article — think Medium post with embedded screenshots.

**The result**: 16 self-contained HTML articles that anyone can read in a browser, no video platform access needed.

---

## How it was built

This entire project was built in a single Claude Code session using browser automation and parallel AI agents. Here's the pipeline:

```
  VIDEO PLATFORM                    CLAUDE CODE                         OUTPUT
  ┌─────────────┐                  ┌─────────────┐                   ┌──────────┐
  │              │   Chrome DevTools│             │                   │          │
  │  DRM Video   │───── MCP ──────>│  Screenshot  │──> img/*.jpg ──>│  HTML    │
  │  (Mux/Vdo)   │   seek + play   │  every 60s   │                  │ Articles │
  │              │                  │             │                   │          │
  │  Subtitles   │──── download ──>│  Transcript  │──> .txt ───────>│          │
  │  (VTT)       │                  │  extraction  │                  │          │
  └─────────────┘                  └──────┬──────┘                   └──────────┘
                                          │
                                  ┌───────▼───────┐
                                  │ AI Narrative   │
                                  │ Writing Agent  │
                                  │ (background)   │
                                  │               │
                                  │ transcript +   │
                                  │ screenshots +  │
                                  │ template ──>   │
                                  │ presentation.md│
                                  └───────┬───────┘
                                          │
                                  ┌───────▼───────┐
                                  │  preview_md.py │
                                  │  render HTML   │
                                  └───────────────┘
```

### Step 1: Screenshot extraction

The video platform uses **DRM-protected streams** (Mux with Widevine). Regular tools like Playwright or headless Chrome can't capture the video frames. The solution: **Chrome DevTools MCP** — a protocol that attaches to a real Chrome window with full DRM support.

For each talk, Claude Code:
- Navigates to the video page
- Uses JavaScript to seek the video player to each 60-second mark
- Plays briefly (1.5s) so the DRM frame renders, then pauses
- Screenshots the player element and saves to disk

This produces ~40-80 frames per talk depending on duration.

**Key learning**: Mux player requires `play()` after `seek()` for frames to render. Just setting `currentTime` while paused shows a stale frame due to DRM decryption.

### Step 2: Transcript extraction

Transcripts were extracted from Mux VTT subtitle streams. The `scripts/download_ids_transcripts.py` script fetches the subtitle manifest, downloads all VTT chunks, strips timestamps, and concatenates into clean text files.

### Step 3: Narrative writing (parallel agents)

This is where the magic happens. While screenshots were being captured sequentially (one browser, one video at a time), **background AI agents** wrote the narrative articles in parallel.

Each agent receives:
- The full transcript
- The reference template (talk 216's structure)
- Instructions to view key screenshots for slide content
- Style rules: third-person prose, bold key concepts, no bullet lists

The agents write a `presentation.md` file and render it to HTML.

### Step 4: HTML rendering

`scripts/preview_md.py` converts markdown to styled HTML with a Medium-like design. `scripts/render_all.py` batch-renders all 16 presentations with navigation (back to index, prev/next talk).

---

## Project structure

```
Into Design Systems 2026/
├── index.html                     # Overview page with all talks
├── CLAUDE.md                      # AI workspace instructions
├── README.md                      # This file
├── .claude/
│   └── skills/
│       └── process-talk/          # Slash command for processing a talk
├── talks/
│   ├── 210-spotify-design-system/
│   │   ├── presentation.md        # Narrative source
│   │   ├── presentation.html      # Rendered article
│   │   └── img/
│   │       └── frame-*.jpg        # Video screenshots (every 60s)
│   ├── 214-prototyping-for-the-unknown/
│   │   └── ...
│   ├── ... (16 talk folders)
│   └── transcripts/               # Raw transcripts (all talks)
├── outlines/                      # Quick bullet summaries per talk
├── slides/                        # PDF slide decks (where available)
└── scripts/
    ├── preview_md.py              # Markdown to styled HTML renderer
    ├── render_all.py              # Batch re-render all presentations
    ├── download_ids_transcripts.py # Subtitle extraction from Mux
    └── screenshot_video.py        # Video screenshot automation
```

---

## Tools used

| Tool | Role |
|------|------|
| **Claude Code (Opus)** | Orchestration, narrative writing, HTML generation |
| **Chrome DevTools MCP** | Browser automation for DRM video screenshots |
| **Background agents** | Parallel narrative writing while screenshots captured |
| **CLAUDE.md** | Project instructions and talk catalog |
| **Custom skills** | `/process-talk` slash command for repeatable workflow |

---

## Reproducing this

If you have access to the video platform:

1. Open a Chrome window and log in to `videos.intodesignsystems.com`
2. Connect Chrome DevTools MCP to that browser
3. Run `/process-talk <page_id> <title-slug>` in Claude Code
4. The skill handles screenshots, narrative writing, and HTML rendering

For a new conference, adapt the `CLAUDE.md` catalog and the `/process-talk` skill.

---

## Lessons learned

- **DRM is the bottleneck**: Headless browsers (Playwright, agent-browser) can't render DRM video frames. Only a real Chrome with Widevine works, via Chrome DevTools Protocol.
- **Play-pause trick**: Mux player won't render new frames on seek alone — you must `play()` briefly after setting `currentTime`.
- **Parallel agents save hours**: While screenshots are sequential (one browser), narrative writing runs in parallel background agents. A 50-min talk gets its article written while the next talk's screenshots are captured.
- **Verify screenshots**: Early on, we captured 40 identical frames because the video wasn't actually playing. Always spot-check a few frames per talk.
- **Template consistency**: Having a reference article (talk 216) that all agents copy ensures visual and structural consistency across all 16 presentations.

---

## Talk catalog

| # | Talk | Speaker | Duration |
|---|------|---------|----------|
| Bonus | Spotify Design System | Victoria Tholeus & Aleksander Djordjevic | 19 min |
| 1 | Prototyping for the Unknown | Nate Baldwin (Adobe Spectrum) | 40 min |
| 2 | WhatsApp Web: Vibe Coding | Sebastian Rousseau (WhatsApp) | 45 min |
| 3 | Product Primitives | Yesenia Perez-Cruz | 47 min |
| 4 | AI-Enabled Design System | Andressa Lombardo & Eddie Machado (Miro) | 50 min |
| 5 | Agentic Design Systems | Romina Kavcic | 54 min |
| 6 | I'm Not an Engineer but I Ship Code | Freya Stockman (Relevance AI) | 52 min |
| 7 | Context > Probability | Jesse Gardner (NY State) | 54 min |
| 8 | Encoding Governance | Cristian Morales Achiardi (Enara Health) | 38 min |
| 9 | Building Real DS with Agents | Jan Six (GitHub) | 49 min |
| 10 | Vibe Coding Zero Drift | Shuaiqi Sun | 76 min |
| 11 | Machine-Readable DS for MCP/LLMs | Diana Wolosin (Indeed) | 46 min |
| 12 | From Markdown to Real Problems | Laura Fehre (Figma) | 49 min |
| 13 | Ship It! Figma Plugin | Davy Fung (Atlassian) | 50 min |
| 14 | Designers Who Ship (48hr Plugin) | Hellmuth, Pereira & Sandu | 53 min |
| 15 | AI Without the Chaos | Brad Frost, Ian Frost & TJ Pitre | 78 min |
