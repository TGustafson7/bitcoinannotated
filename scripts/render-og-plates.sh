#!/bin/bash
# Renders SVG plates to 1200×630 PNGs for OG/Twitter card unfurls.
# Preserves 800×600 plate aspect by letterboxing onto paper-cream background.
# Run manually when plates are added or modified: bash scripts/render-og-plates.sh

set -e

SRC_DIR="public/images/entries"
OUT_DIR="public/images/og"
PAPER_CREAM="#f8f4ed"

mkdir -p "$OUT_DIR"

count=0
for svg in "$SRC_DIR"/*.svg; do
  [ -e "$svg" ] || continue
  fname=$(basename "$svg" .svg)
  out="$OUT_DIR/${fname}.png"

  # Stage 1: render SVG to 840x630 (preserves 800x600 plate aspect at target height)
  tmp="/tmp/${fname}-inner.png"
  rsvg-convert -h 630 -b "$PAPER_CREAM" "$svg" -o "$tmp"

  # Stage 2: composite onto 1200x630 paper-cream canvas, centered
  magick -size 1200x630 "xc:${PAPER_CREAM}" "$tmp" -gravity center -composite "$out"

  rm -f "$tmp"
  count=$((count + 1))
  echo "  rendered: ${fname}.png"
done

echo ""
echo "Rendered $count plates to $OUT_DIR/"
