#!/usr/bin/env python3
"""
Bitcoin Annotated — Block Height Corrections, Batch 2

Final batch of corrections from mempool.space verifications.
Running Bitcoin (block 78) stays as-is per editorial decision.
"""
import sys
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv
ENTRIES_DIR = Path("src/content/entries")

if not ENTRIES_DIR.exists():
    print(f"ERROR: {ENTRIES_DIR} not found. Run from the repo root.")
    sys.exit(1)

corrections = [
    ("btc-2011-002-first-mt-gox-hack.md",     133000, 131750, "2011-06-19 00:24:07 UTC"),
    ("btc-2013-003-cyprus.md",                227000, 226100, "2013-03-16 00:16:23 UTC"),
    ("btc-2013-001-hodl.md",                  275000, 275600, "2013-12-18 04:37:14 UTC"),
    ("btc-2014-002-the-mt-gox-collapse.md",   286000, 287515, "2014-02-24 01:38:32 UTC"),
    ("btc-2014-003-trezor.md",                311500, 313000, "2014-07-29 07:05:31 UTC"),
    ("btc-2016-003-the-bitfinex-hack.md",     424200, 423300, "2016-08-02 05:26:04 UTC"),
    ("btc-2017-003-the-symbol.md",            472500, 472100, "2017-06-20 06:20:09 UTC"),
    # Block Size Wars stays at 478,558 — BIP148 activation block, the event itself
]

print(f"Applying {len(corrections)} block height corrections.\n")
print(f"{'FILE':<48} {'OLD':>10} → {'NEW':>10}  STATUS")
print("-" * 90)

stats = {"updated": 0, "no_match": 0, "missing": 0}
for filename, old, new, ts in corrections:
    path = ENTRIES_DIR / filename
    if not path.exists():
        print(f"{filename:<48} {old:>10,} → {new:>10,}  MISSING")
        stats["missing"] += 1
        continue

    text = path.read_text()
    pattern = f"blockHeightAtOrigin: {old}"
    replacement = f"blockHeightAtOrigin: {new}"

    if pattern not in text:
        if f"blockHeightAtOrigin: {new}" in text:
            print(f"{filename:<48} {old:>10,} → {new:>10,}  ALREADY DONE")
        else:
            print(f"{filename:<48} {old:>10,} → {new:>10,}  NO MATCH")
        stats["no_match"] += 1
        continue

    new_text = text.replace(pattern, replacement)
    print(f"{filename:<48} {old:>10,} → {new:>10,}  ✓ verified at {ts}")
    stats["updated"] += 1

    if not DRY_RUN:
        path.write_text(new_text)

print(f"\n=== SUMMARY ===")
print(f"  Updated:        {stats['updated']}")
print(f"  No match:       {stats['no_match']}")
print(f"  Missing files:  {stats['missing']}")

if DRY_RUN:
    print("\n*** DRY RUN — no files were modified. ***")
else:
    print("\n*** Files updated. ***")
