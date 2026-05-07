#!/usr/bin/env python3
"""
Bitcoin Annotated — Foundational Entries Block Height Backfill

Adds blockHeightAtOrigin to the 24 remaining foundational entries.
Source values are best-effort estimates anchored on halving block numbers
plus verified data points from web sources.

Run from repo root: python3 backfill_block_heights.py [--dry-run]

Confidence legend (visible only in this script's output, not in the entry files):
  verified — block height confirmed by primary or near-primary sources
  high     — backed by well-documented price/event records
  medium   — estimated from date + halving interpolation, event is dated
  low      — estimated, but the entry's date itself is approximate
"""
import sys
import re
from pathlib import Path
from typing import Optional

DRY_RUN = "--dry-run" in sys.argv
ENTRIES_DIR = Path("src/content/entries")

if not ENTRIES_DIR.exists():
    print(f"ERROR: {ENTRIES_DIR} not found. Run from the repo root (~/bitcoinannotated).")
    sys.exit(1)

# (filename, block_height, confidence, notes)
backfill = [
    ("btc-2009-002-running-bitcoin.md",                78,     "medium",   "Hal Finney said 'block 70-something'"),
    ("btc-2010-001-bitcoin-orange.md",                 88000,  "low",      "Bitcoin Orange iconography — date is approximate"),
    ("btc-2010-002-the-pizza.md",                      57043,  "verified", "Famous, confirmed via multiple sources"),
    ("btc-2011-002-first-mt-gox-hack.md",              133000, "low",      "Day of the hack"),
    ("btc-2013-001-hodl.md",                           275000, "medium",   "The Bitcointalk post"),
    ("btc-2013-003-cyprus.md",                         227000, "medium",   "Cyprus bailout announcement"),
    ("btc-2014-002-the-mt-gox-collapse.md",            286000, "medium",   "Day Karpeles closed exchange"),
    ("btc-2014-003-trezor.md",                         311500, "low",      "First shipment date varies by source"),
    ("btc-2016-003-the-bitfinex-hack.md",              424200, "medium",   "Day of hack"),
    ("btc-2017-003-the-symbol.md",                     472500, "medium",   "Unicode 10.0 release date"),
    ("btc-2017-001-buy-bitcoin-sign.md",               475800, "medium",   "Yellen testimony day"),
    ("btc-2017-002-the-block-size-wars.md",            478558, "low",      "UASF/BIP148 fork block"),
    ("btc-2018-001-the-bitcoin-standard.md",           519500, "low",      "Book publication date"),
    ("btc-2019-003-lightning-torch.md",                558000, "low",      "Hodlonaut's first send"),
    ("btc-2021-001-laser-eyes.md",                     669000, "medium",   "Saylor adoption period"),
    ("btc-2021-005-the-china-mining-ban.md",           684500, "medium",   "Day of policy announcement"),
    ("btc-2021-008-the-bitcoin-2021-miami-stage.md",   686500, "medium",   "Conference dates Jun 4-5"),
    ("btc-2021-007-the-69k-top.md",                    709300, "high",     "Well-documented price-history block"),
    ("btc-2021-006-taproot.md",                        709632, "verified", "The activation block itself"),
    ("btc-2022-002-terra-luna-collapse.md",            736500, "medium",   "Day UST depegged"),
    ("btc-2022-001-the-ftx-collapse.md",               763500, "medium",   "Day FTX filed Chapter 11"),
    ("btc-2024-001-spot-etf-approval.md",              825500, "medium",   "Day SEC approved"),
    ("btc-2024-002-trump-nashville.md",                853500, "medium",   "Conference keynote day"),
    ("btc-2025-002-free-ross.md",                      881000, "medium",   "Trump's pardon day"),
]

def insert_block_height(text: str, block: int) -> Optional[str]:
    """Insert blockHeightAtOrigin: <block> after the date: line in frontmatter."""
    # Already has blockHeightAtOrigin? Skip.
    if re.search(r'^blockHeightAtOrigin:', text, re.MULTILINE):
        return None
    # Find the date: line and add blockHeightAtOrigin after it
    new_text, count = re.subn(
        r'(^date: \S+)$',
        rf'\1\nblockHeightAtOrigin: {block}',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    return new_text if count else None

print(f"Backfilling block heights for {len(backfill)} entries.\n")
print(f"{'FILE':<48} {'BLOCK':>10}  {'CONF':<10} NOTES")
print("-" * 100)

stats = {"updated": 0, "already_set": 0, "missing": 0}
for filename, block, conf, notes in backfill:
    path = ENTRIES_DIR / filename
    if not path.exists():
        print(f"{filename:<48} {'—':>10}  {'MISSING':<10} (file not found)")
        stats["missing"] += 1
        continue

    text = path.read_text()
    new_text = insert_block_height(text, block)

    if new_text is None:
        print(f"{filename:<48} {block:>10,}  {'SKIP':<10} (already set)")
        stats["already_set"] += 1
        continue

    print(f"{filename:<48} {block:>10,}  {conf:<10} {notes}")
    stats["updated"] += 1

    if not DRY_RUN:
        path.write_text(new_text)

print(f"\n=== SUMMARY ===")
print(f"  Updated:        {stats['updated']}")
print(f"  Already set:    {stats['already_set']}")
print(f"  Missing files:  {stats['missing']}")
print(f"  Total in batch: {len(backfill)}")

if DRY_RUN:
    print("\n*** DRY RUN — no files were modified. Re-run without --dry-run to apply. ***")
else:
    print("\n*** Files updated. ***")
