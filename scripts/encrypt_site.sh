#!/usr/bin/env bash
# Encrypt all presentation HTML + index.html in place using StatiCrypt.
# Re-run this after regenerating HTML from markdown (preview_md.py / render_all.py).
#
# Usage:
#   STATICRYPT_PASSWORD=yourpassword ./scripts/encrypt_site.sh
#   or just run it and enter the password when prompted.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ -z "${STATICRYPT_PASSWORD:-}" ]; then
    read -s -p "StatiCrypt password: " STATICRYPT_PASSWORD
    echo
    export STATICRYPT_PASSWORD
fi

TITLE="Into Design Systems 2026 — Protected"
INSTRUCTIONS="Shared by Jelle — password required."

encrypt_file() {
    local file="$1"
    local dir
    dir="$(dirname "$file")"
    echo "Encrypting $file"
    npx --yes staticrypt@latest "$file" \
        -d "$dir" \
        --short \
        --template-title "$TITLE" \
        --template-instructions "$INSTRUCTIONS" \
        --template-color-primary "#111" \
        --template-color-secondary "#f5f5f5" \
        > /dev/null
}

encrypt_file "index.html"

for html in talks/*/presentation.html; do
    encrypt_file "$html"
done

echo "Done. $(find talks -name presentation.html | wc -l | tr -d ' ') talk pages + index.html encrypted."
