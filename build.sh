#!/usr/bin/env bash
set -euo pipefail

BOOK_DIR="$(cd "$(dirname "$0")/book-one" && pwd)"
OUTPUT="$BOOK_DIR/The Brightest Fire.epub"

# Gather chapter files in order
chapters=()
for f in "$BOOK_DIR"/chapter-??.md; do
  chapters+=("$f")
done

if [ ${#chapters[@]} -eq 0 ]; then
  echo "No chapter files found." >&2
  exit 1
fi

echo "Building epub from ${#chapters[@]} chapters..."

pandoc \
  --metadata-file="$BOOK_DIR/metadata.yaml" \
  --epub-cover-image="$BOOK_DIR/Brightest_Fire_cover.png" \
  --toc \
  --toc-depth=1 \
  -o "$OUTPUT" \
  "${chapters[@]}"

echo "Built: $OUTPUT"
