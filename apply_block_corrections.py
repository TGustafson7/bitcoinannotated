#!/usr/bin/env python3
"""
Bitcoin Annotated — Block Height Corrections (from mempool.space verifications)

Applies real block heights from mempool.space lookups to replace earlier estimates.
Idempotent: safe to re-run; only changes lines whose old value is found.

Run from repo root: python3 apply_block_corrections.py [--dry-run]
"""
import sys
import re
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv
ENTRIES_DIR = Path("src/content/entries")

if not ENTRIES_DIR.exists():
    print(f"ERROR: {ENTRIES_DIR} not found. Run from the repo root.")
    sys.exit(1)

# (filename, old_value, new_value, verified_timestamp)
corrections = [
    ("btc-2010-001-bitcoin-orange.md",                 88000,  88940,  "2010-11-01 02:38:43 UTC"),
    ("btc-2017-001-buy-bitcoin-sign.md",               475800, 475425, "2017-07-12 02:26:54 UTC"),
    ("btc-2018-001-the-bitcoin-standard.md",           519500, 519690, "2018-04-24 03:46:39 UTC"),
    ("btc-2019-003-lightning-torch.md",                558000, 559130, "2019-01-19 02:23:08 UTC"),
    ("btc-2021-001-laser-eyes.md",                     669000, 670820, "2021-02-16 02:21:15 UTC"),
    ("btc-2021-005-the-china-mining-ban.md",           684500, 684400, "2021-05-21 02:17:11 UTC"),
    ("btc-2021-008-the-bitcoin-2021-miami-stage.md",   686500, 686330, "2021-06-05 01:11:35 UTC"),
    ("btc-2021-007-the-69k-top.md",                    709300, 709030, "2021-11-10 01:42:15 UTC"),
    ("btc-2022-002-terra-luna-collapse.md",            736500, 735575, "2022-05-09 02:46:38 UTC"),
    ("btc-2022-001-the-ftx-collapse.md",               763500, 762690, "2022-11-11 05:28:52 UTC"),
    ("btc-2024-001-spot-etf-approval.md",              825500, 825100, "2024-01-10 01:07:06 UTC"),
    ("btc-2024-002-trump-nashville.md",                853500, 854145, "2024-07-27 03:22:19 UTC"),
    ("btc-2025-002-free-ross.md",                      881000, 880175, "2025-01-21 02:10:07 UTC"),
]

print(f"Applying {len(corrections)} block height corrections.\n")
print(f"{'FILE':<48} {'OLD':>10} → {'NEW':>10}  STATUS")
print("-" * 90)

stats = {"updated": 0, "no_match": 0, "missing": 0}
for filename, old, new, ts in corrections:
    path = ENTRIES_DIR / filename
    if not path.exists():
        print(f"{filename:<48} {old:>10,} → {new:>10,}  MISSING (file not found)")
        stats["missing"] += 1
        continue

    text = path.read_text()
    pattern = f"blockHeightAtOrigin: {old}"
    replacement = f"blockHeightAtOrigin: {new}"

    if pattern not in text:
        # Already at new value? Check.
        if f"blockHeightAtOrigin: {new}" in text:
            print(f"{filename:<48} {old:>10,} → {new:>10,}  ALREADY DONE")
        else:
            print(f"{filename:<48} {old:>10,} → {new:>10,}  NO MATCH (current value differs)")
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
    print("\n*** DRY RUN — no files were modified. Re-run without --dry-run to apply. ***")
else:
    print("\n*** Files updated. ***")
