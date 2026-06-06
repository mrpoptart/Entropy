#!/usr/bin/env bash
# Per-chapter diagnostics for a given book directory.
# Usage: scripts/chapter-stats.sh book-two
# Reports: em-dash count, line count, word count, and a rough count of
# unattributed-looking quoted lines (lines starting with a quote and ending
# with closing-quote-plus-punctuation, no "said"/"asked" nearby).

set -euo pipefail

book="${1:-book-two}"
dir="$(cd "$(dirname "$0")/.." && pwd)/$book"

if [[ ! -d "$dir" ]]; then
  echo "no such book dir: $dir" >&2
  exit 1
fi

printf '%-16s %6s %6s %8s %8s\n' file em-dash lines words bare-quote
for f in "$dir"/chapter-*.md; do
  [[ -e "$f" ]] || continue
  name=$(basename "$f")
  em=$(grep -c '—' "$f" || true)
  lines=$(wc -l < "$f")
  words=$(wc -w < "$f")
  # Lines that are pure dialogue with no tag/beat on the same line.
  bare=$(grep -cE '^"[^"]+[\.\?\!]"\s*$' "$f" || true)
  printf '%-16s %6s %6s %8s %8s\n' "$name" "$em" "$lines" "$words" "$bare"
done
