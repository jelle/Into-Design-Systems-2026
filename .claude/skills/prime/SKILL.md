---
name: prime
description: Load full workspace context at the start of a new session. Use this skill whenever Jelle starts a new conversation, says "prime", "load context", "start session", "good morning", or when you detect this is the beginning of a fresh session without prior context. This is the bootstrap command — run it before doing anything else in a new session.
---

# Prime

Bootstrap the Yellow workspace by loading all context so you can be an effective assistant from the first message.

## Why this matters

Without priming, you'd be starting from zero every session — no idea who Jelle is, what projects are active, or what's been learned before. Priming takes 10 seconds and saves hours of re-explaining.

## Steps

1. Read the workspace structure by listing all files and folders in this project
2. Read `CLAUDE.md` in the project root
3. Read all files in `./context/` in order (01 through 04)
4. Check the auto-memory directory for any persistent memory files and read them

## Output

Respond with a brief summary covering:
- Who Jelle is and what this workspace is for
- What commands and tools are available
- Any active learning paths or priorities from context
- Any relevant memories from previous sessions
- Confirm you're ready to assist

Keep the summary under 15 lines. Be direct — Jelle values conciseness.
