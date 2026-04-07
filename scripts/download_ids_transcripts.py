#!/usr/bin/env python3
"""Download all Into Design Systems AI Conference 2026 transcripts from Mux subtitle manifests."""

import os
import re
import json
import asyncio
import aiohttp

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "ids-conference")

# NOTE: Subtitle manifest URLs are signed and expire. To use this script,
# you need to obtain fresh signed URLs from a browser session on
# videos.intodesignsystems.com (inspect network requests for .m3u8 files).
VIDEOS = [
    {"pageId": 213, "title": "Day 1 - Intro", "subtitleManifest": ""},
    {"pageId": 214, "title": "Prototyping for the unknown", "subtitleManifest": ""},
    {"pageId": 215, "title": "WhatsApp Web - Reclaiming UI Excellence through Vibe Coding", "subtitleManifest": ""},
    {"pageId": 216, "title": "Product Primitives - The New Material of Design System", "subtitleManifest": ""},
    {"pageId": 217, "title": "The path to an AI enabled design system", "subtitleManifest": ""},
    {"pageId": 218, "title": "Agentic Design Systems", "subtitleManifest": ""},
    {"pageId": 219, "title": "Im not an engineer but I ship code", "subtitleManifest": ""},
    {"pageId": 220, "title": "Context vs Probability - Design systems as AI infrastructure", "subtitleManifest": ""},
    {"pageId": 221, "title": "Encoding governance on agentic design systems", "subtitleManifest": ""},
    {"pageId": 222, "title": "Day 1 - Outro", "subtitleManifest": ""},
    {"pageId": 223, "title": "Day 2 - Intro", "subtitleManifest": ""},
    {"pageId": 224, "title": "Building real design systems with agents", "subtitleManifest": ""},
    {"pageId": 225, "title": "Vibe coding with zero drift - Figma to Storybook to Production", "subtitleManifest": ""},
    {"pageId": 226, "title": "Machine-Readable Design Systems for MCP and LLMs", "subtitleManifest": ""},
    {"pageId": 227, "title": "From falling for markdown to solving real problems with scripts", "subtitleManifest": ""},
    {"pageId": 228, "title": "Ship It - Vibe Coding Your First Figma Plugin", "subtitleManifest": ""},
    {"pageId": 229, "title": "Designers Who Ship - Building a Real Plugin in 48 Hours with AI", "subtitleManifest": ""},
    {"pageId": 230, "title": "AI Without the Chaos - Context-Based Design Systems to the Rescue", "subtitleManifest": ""},
    {"pageId": 231, "title": "Day 2 - Outro", "subtitleManifest": ""},
]


def sanitize_filename(title):
    return re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '-')[:80]


async def download_transcript(session, video):
    page_id = video["pageId"]
    title = video["title"]
    manifest_url = video["subtitleManifest"]

    if not manifest_url:
        print(f"  [{page_id}] {title} — no subtitles, skipping")
        return

    # Fetch subtitle manifest
    async with session.get(manifest_url) as resp:
        manifest = await resp.text()

    # Extract VTT chunk URLs
    vtt_urls = [line for line in manifest.split('\n') if line.startswith('https://')]

    if not vtt_urls:
        print(f"  [{page_id}] {title} — no VTT chunks found")
        return

    # Download all chunks concurrently (batches of 20)
    all_text = []
    for i in range(0, len(vtt_urls), 20):
        batch = vtt_urls[i:i+20]
        tasks = [session.get(url) for url in batch]
        responses = await asyncio.gather(*tasks)
        for r in responses:
            vtt = await r.text()
            for line in vtt.split('\n'):
                line = line.strip()
                if line == 'WEBVTT' or line == '' or re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}', line):
                    continue
                all_text.append(line)

    transcript = ' '.join(all_text)

    # Save to file
    filename = f"{page_id}-{sanitize_filename(title)}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(f"# {title}\n")
        f.write(f"# Into Design Systems AI Conference 2026\n")
        f.write(f"# Source: https://videos.intodesignsystems.com/videos/{page_id}\n\n")
        f.write(transcript)

    print(f"  [{page_id}] {title} — {len(transcript):,} chars, {len(vtt_urls)} chunks → {filename}")


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Downloading {len(VIDEOS)} transcripts from Into Design Systems AI Conference 2026...\n")

    async with aiohttp.ClientSession() as session:
        # Process sequentially to avoid overwhelming the CDN
        for video in VIDEOS:
            await download_transcript(session, video)

    print(f"\nDone! Transcripts saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
