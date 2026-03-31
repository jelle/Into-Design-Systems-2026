#!/usr/bin/env python3
"""Download all Into Design Systems AI Conference 2026 transcripts from Mux subtitle manifests."""

import os
import re
import json
import asyncio
import aiohttp

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "ids-conference")

VIDEOS = [
    {"pageId": 213, "title": "Day 1 - Intro", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/J9t00tKLZnb8D00V00X8hrGvesTcL4trJekMtCEVAYEkGTlCNjBlb00suCz02n5cEBI01bxi94f1PKDzY/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmNfMDcwYjFiYTc1NTM5OTg5NjAxNGYwYzgzZjEyMGFiNTljZjVkNGNjNTRiZjk0Y2JjZTkzMTYwMzk4M2Y4NjYyYg=="},
    {"pageId": 214, "title": "Prototyping for the unknown", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/IcDENLLapAPa1RlmUXKoTOdXXnTDXOksQYfgwLeqmMRGyco00pAN3eBVXdv01bDsXscv3d2PmQ39Q/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmRfZmJhYWE4YWVkNmRmOTRhMzc2YWIyZDBlYmU1ZDUzYmFiZmMyNjJkOWU0OWNjY2IzNzJlNTdlNWI2ZWViNWEwYg=="},
    {"pageId": 215, "title": "WhatsApp Web - Reclaiming UI Excellence through Vibe Coding", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/BihEchS8NJ29CN6SKDM1TJSBnxYFFNBsK9oQZyGu0100YONuT8Mc11phdW4ZaPsELWeT6Xde00xL02Q/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmRfNjQ5OTlmNWM3YjE4NDg1ZjFmNWZlZjJhOWExMDI3ZTIzY2I5MGJiYTFlMzk1NmQwNWJkMzg5YjE4MzIzNDg0MA=="},
    {"pageId": 216, "title": "Product Primitives - The New Material of Design System", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/ghcwgHljZJ9YVUNthUe65RZk8wgaMWDzAESPE200kluD4JfO5vDkTl02WjjuiUHntxgaT01C9LAZAs/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmRfNThhMjAyMmFjODM1MDI2ZDFhZmQ5ODdhYjVlMDk4MzFjZDQ5NTg4YWFjMjE2Mzc3ZTA2OTM2NWE2OTFlNzcxMg=="},
    {"pageId": 217, "title": "The path to an AI enabled design system", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/To7XDXJ3h023koPpIDOt62ocl52LGqNU6DExgXPudc2X8TRgiTMd00pEKF7jMRjHOQk2nrvWvf4Po/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmVfOTc1MDc2MDlmOGYzNTJjNjEyZjg0ZTQyZjEzM2FhOTg5MGYxZTViZWY4MmUxNjRjYTA5N2JjMDEyMGI1ZTBjNQ=="},
    {"pageId": 218, "title": "Agentic Design Systems", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/qsA5qX1lOz01Q6h3DGxX4lKBP01017crx3cOdD2opdZ9VnbmuEkyjzlS3sli500KIQLlqOdKkg02L5Wo/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmVfYjk0OWQ5OTdkMDc2ODQwMmFiYmRjM2FlNjgzNTRjNDYxZTRhZTIzZTY2ZTkwNzE4MDQ1NGEyZDlkYTc1YTJmYg=="},
    {"pageId": 219, "title": "Im not an engineer but I ship code", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/ZI7WEK02ioJs2AyNJ02vqjdTpQ6tvBASwREC7Qi3Oj1nwXGx5g5PA00WFYFqdqvvuWwp02kYZ9eObkw/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmVfOWIwOGJhZWVkNzkwMzk1NTdkN2ViMGVkNGQyY2YxYzc2MzcxNmFlY2M4NjZlY2MwYzhhYTcwMmNiOTc4NzczZg=="},
    {"pageId": 220, "title": "Context vs Probability - Design systems as AI infrastructure", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/PyJiaUVIRmbENynsqXkqS302k8VHYB2KabEZkpj7LKRHa9JJPSwjNNdrCQDsyAdOdNaCHz5UPLmc/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmZfZWE4OWZjMzM1ODUxY2ZkMjdlM2M1NGRlYmRiNmY3ZDMwMmI3MzEwNTEwZGViNDc2OTM5ZDg1NGU2Y2I0MDQwNA=="},
    {"pageId": 221, "title": "Encoding governance on agentic design systems", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/WKURTeG6ghpJgXmOHB202tkf1NLWCE4nbP017ewd8Y3Hyr6rvFMqdmaCgq5Pu7X9lWa9bLI009ZtoQ/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYmZfNDgwYjRhN2YxYmE2NmE1YzBhZWJkYTFmNDg4MmE0N2ZmOGRlMDY0YjViMDNkMjUwODAyNjQ3MDk4ODNmZGU5Yg=="},
    {"pageId": 222, "title": "Day 1 - Outro", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/jFlquNrQwW7MrrqqlIp4gbTaUHtZNFoGprpVHzF4jgBPlXcckfr6ajnY6PdD1PHioqcNPebQNUY/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzBfYTYyNjhhYTA0MTdjMWQ3OWQ1MDlkYzQ2ZmJjZmI3OGFiMGMzY2ZhN2ViNGZiYjAzZTUzZThmNmQ2OGM2ZTdlOQ=="},
    {"pageId": 223, "title": "Day 2 - Intro", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/4D01EFIndouceFgojm02FU01YCzUhrmvrRwxHiup3K50101nezt8Gxm00XF801SR01w6T00uTnaCHF33F84s/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzBfNTcxN2IzNzhlZDc2NDEwMzI4ZDA1MmFiYTk0YzM0YmEzMjg2NTJhOGE0Y2IyNzM5OTYwN2U5MmZjYzZhYWNjNg=="},
    {"pageId": 224, "title": "Building real design systems with agents", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/t8SXSX3FVZkIrAVUm28DVvgYTsQC01VEgkQjdH4D01thqbN01vAbv8jfB01cpprm3nfQFjlbPvLDfeU/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzBfNWNkZGY0MDQ4ZjEyNDgzZGE4ZjRkN2U1NDE1NzVmY2NkMWVlYWQ3MDg4YzVmNjI4NjY3OGY4MDI1MDRjOTU5ZA=="},
    {"pageId": 225, "title": "Vibe coding with zero drift - Figma to Storybook to Production", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/00rp02lXwibi9GWvF8LAcBmosy6lDiER5WGU8FDNC01C02LWpLkFTNtCcYeb02ConaxGiq3AdC5O01QOk/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzFfMmNhZTBlNmJlNjcxMzUyMTA1YmE2MTk1ZDQzMGJkY2VkZTBjZTVhOWU4ZGRhMWE3MzY0NWFiM2JhODgzNGY5ZA=="},
    {"pageId": 226, "title": "Machine-Readable Design Systems for MCP and LLMs", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/mHsg301stNPXHCeJI9x02mXMSi00NjIKcLIuI6NZWnkk02wHHo3B1xS1QqrUIGtgG4KBvFLPUKKzJGI/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzFfMDM3YTU4ZjQzN2E5NmQxMjM1MmIwMTA5MWM2MzM4MGZkY2MzZmU3MWQ2NzdmMmM5YTc2NWUxNzc5YWFiMTcwYw=="},
    {"pageId": 227, "title": "From falling for markdown to solving real problems with scripts", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/N20200iMdt5HShH8siBTeQZgMDVGGqJ01CsWXBv00eGI1YCVN0201srLoD0202ICD28Qi00Ye012P0196qSHio/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzFfYzAyMzkxNGQzNjdmNjExYmMxM2Y2MDdiNmRiODE3YjI0Y2ZmMzEwNjlhM2ExY2QwMDUzZDMwZmJhMDFiNGIwYw=="},
    {"pageId": 228, "title": "Ship It - Vibe Coding Your First Figma Plugin", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/NnhoCGnAzqJxHWU4d00FXVxEeGjNcdRSYzI2rsrrqtUIhf5BPpD01AqiAbFmo5Knk7C4zUC5T00WVs/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzJfMDM1MzE5MzJlZTRkOWJhMGQwZGYzOTQ4MWVjNmU5Nzc5NjE5NGIzZjE1YTFhZTg0NjA1YTUwOTliM2NlZDYwZA=="},
    {"pageId": 229, "title": "Designers Who Ship - Building a Real Plugin in 48 Hours with AI", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/l018ykihS00r011ItnzS9O5CeKmt3fsxYJyEFFOauKresRKjn3gZ5ZLr02LGzv02GypOr4L5C701mD00OY/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzJfYWFiNDk3OTI2ZWQ5MWNlM2IzMjFlZjhhMDg2OTg3NGM5YmZmNWU4NTFiZThhMzUzMWViNDQ2ZjIwMWU3ZWU0Nw=="},
    {"pageId": 230, "title": "AI Without the Chaos - Context-Based Design Systems to the Rescue", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/5roSILQum024UoPUitTSz9n0001UGBvgZbqZf81ivt24iE8Uzsga3ZtcQBzvcIQJ700y3QwjWnoSbPg/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzJfMzhmYjg3ZWVkMjVjZDVhMDJlMTg1OTA0NmZlZGNmZWJiOTBmYzljOGExM2FjYzlhMTUzNGQ4NzQ4NGVjY2JlOA=="},
    {"pageId": 231, "title": "Day 2 - Outro", "subtitleManifest": "https://manifest-oci-us-ashburn-1-vop1.edgemv.mux.com/E02acnLAMbHH4dXhss8AcTsjKf100FbHlEV01SKWnG1kn9Pc6vT9o5XlJ3006tPVQVSQLER02Q1sE01z00/subtitles.m3u8?cdn=edgemv&expires=1774900800&skid=edgemv-default-1&signature=NjljYWQzYzNfYTQ3ZDQxZjUwMmM2YjEzYmI5MzQ3YTUxNjBlM2Y5NDQwMjc0MzY1MmIxZjllNDI1MjViN2E0OWQ3ZTBiZTM4Yg=="},
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
