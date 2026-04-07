#!/usr/bin/env python3
"""Screenshot video frames from Into Design Systems using Playwright."""

import asyncio
import os
import sys
import json
from playwright.async_api import async_playwright

COOKIES = [
    {
        "name": "XSRF-TOKEN",
        "value": "eyJpdiI6InIvb0hiOC80b0Vnbkw1bG5JUFBvOWc9PSIsInZhbHVlIjoiVUYrdGFhU1RZaWdxekdzRExxbDM0SVpDbm95Y3hGUm1Vakxuc2dmYzl4UXpDSE8zbGZZRG5MZTBDZWltcm5Sb3F6QzIrMzhJOWhsWHNmdU91WEMxOVRDbEZWYmx1VGpOWG5zbDM2bHlyYncxVkx0THJRS2U2djh5SVhOeXE5TDYiLCJtYWMiOiJkZGEyZTBmMTlhZWI3ZDhkYjVmNjVhNjhhNWY3NzQxNTY2ZWQ4OTM3Y2ZlN2U5YTdiMGM1MmE5Y2M4ZGQzMDc0IiwidGFnIjoiIn0=",
        "domain": "videos.intodesignsystems.com",
        "path": "/",
        "secure": True,
        "sameSite": "Lax",
    },
    {
        "name": "into_design_systems_session",
        "value": "eyJpdiI6ImNIQVlHR1BWNlZrazZxRDZMNE1YOWc9PSIsInZhbHVlIjoiTHh1aVU4bHpLUllvYnJ0Z0t6VVBGQklVOXN6SDE0ZDM0SG5uZ3BRRE1kL1dCS3JDamFDNkxrbVM5VTRESTkwR1RsOUFkMjdtRFJPY3BWaTZjZVBDL2NNbGhEVDdabVRZRUJWRmhHWS9PNWU0QUJMWThUaHFpVkZUOXdoaHI4U2QiLCJtYWMiOiI0OGUyYTM3OGRmYzZmMDFkNWM0NWE3MmFhZGE5OWZmMzE4ODNkODIyZDQ2NzRlZjk4ZjhhNTcyMGQ4ZTJlMDBjIiwidGFnIjoiIn0=",
        "domain": "videos.intodesignsystems.com",
        "path": "/",
        "secure": False,
        "httpOnly": True,
        "sameSite": "Lax",
    },
]


async def capture_video_frames(page_id, title_slug, interval=20):
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "talks", f"{page_id}-{title_slug}", "img"
    )
    os.makedirs(output_dir, exist_ok=True)

    url = f"https://videos.intodesignsystems.com/videos/{page_id}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="chrome")
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
        )
        await context.add_cookies(COOKIES)

        page = await context.new_page()
        print(f"  Navigating to {url}...")
        await page.goto(url, wait_until="networkidle", timeout=30000)

        # Wait for Mux player to load
        await page.wait_for_selector("mux-player", timeout=15000)
        await asyncio.sleep(2)

        # Get video duration and start playback briefly to init decoder
        duration = await page.evaluate("""() => {
            const p = document.querySelector('mux-player');
            p.play();
            return p.duration;
        }""")
        await asyncio.sleep(1)
        await page.evaluate("() => document.querySelector('mux-player').pause()")

        print(f"  Duration: {int(duration)}s ({int(duration/60)}min). Interval: {interval}s")

        total_frames = int(duration / interval)
        captured = 0

        for t in range(0, int(duration), interval):
            # Seek
            await page.evaluate(f"() => {{ document.querySelector('mux-player').currentTime = {t}; }}")
            await asyncio.sleep(0.4)  # wait for frame decode

            # Screenshot just the video player
            player = page.locator("mux-player")
            filename = f"frame-{t:04d}.jpg"
            filepath = os.path.join(output_dir, filename)
            await player.screenshot(path=filepath, type="jpeg", quality=80)

            captured += 1
            if captured % 10 == 0:
                print(f"  [{captured}/{total_frames}] at {t}s...")

        print(f"  Done! {captured} frames saved to {output_dir}")
        await browser.close()

    return output_dir, captured


async def main():
    if len(sys.argv) < 3:
        print("Usage: python screenshot_video.py <page_id> <title_slug> [interval_seconds]")
        print("Example: python screenshot_video.py 216 product-primitives 20")
        sys.exit(1)

    page_id = int(sys.argv[1])
    title_slug = sys.argv[2]
    interval = int(sys.argv[3]) if len(sys.argv) > 3 else 20

    output_dir, count = await capture_video_frames(page_id, title_slug, interval)
    print(f"\n{count} frames captured → {output_dir}")


if __name__ == "__main__":
    asyncio.run(main())
