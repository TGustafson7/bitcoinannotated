#!/usr/bin/env python3
"""
Bitcoin Annotated — Schema Simplification Step 1
Migrates the `status` field per the next-session handoff:
  - status: "Foundational" → add `foundational: true`, drop status line
  - status: "Living" → drop status line entirely
  - status: "Dormant" → drop status line entirely

Run from repo root: python3 migrate_status.py [--dry-run]
"""
import sys
import re
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv
ENTRIES_DIR = Path("src/content/entries")

if not ENTRIES_DIR.exists():
    print(f"ERROR: {ENTRIES_DIR} not found. Run from the repo root (~/bitcoinannotated).")
    sys.exit(1)

files = sorted(ENTRIES_DIR.glob("*.md"))
print(f"Found {len(files)} entries.\n")

stats = {"foundational": 0, "dropped": 0, "no_status": 0, "unknown": 0}
changes = []

for p in files:
    text = p.read_text()
    # Match the status line within the frontmatter, capturing the value
    # Frontmatter is between the first two `---` lines
    fm_match = re.match(r'^(---\n)(.*?)(\n---\n)(.*)$', text, re.DOTALL)
    if not fm_match:
        print(f"  SKIP (no frontmatter): {p.name}")
        continue

    fm_open, fm_body, fm_close, rest = fm_match.groups()

    status_match = re.search(r'^status:\s*"?([^"\n]+)"?\s*$', fm_body, re.MULTILINE)

    if not status_match:
        stats["no_status"] += 1
        continue

    status_value = status_match.group(1).strip()
    status_line_pattern = r'^status:\s*"?[^"\n]+"?\s*\n'

    if status_value == "Foundational":
        # Replace status line with foundational: true
        new_fm = re.sub(status_line_pattern, "foundational: true\n", fm_body, count=1, flags=re.MULTILINE)
        stats["foundational"] += 1
        changes.append((p.name, f'status: "Foundational" → foundational: true'))
    elif status_value in ("Living", "Dormant", "Locked"):
        # Drop the line entirely
        new_fm = re.sub(status_line_pattern, "", fm_body, count=1, flags=re.MULTILINE)
        stats["dropped"] += 1
        changes.append((p.name, f'status: "{status_value}" → (removed)'))
    else:
        stats["unknown"] += 1
        print(f"  WARN unknown status '{status_value}' in {p.name} — leaving alone")
        continue

    new_text = fm_open + new_fm + fm_close + rest

    if not DRY_RUN:
        p.write_text(new_text)

# Report
print("\n=== CHANGES ===")
for name, change in changes:
    print(f"  {name:<50} {change}")

print(f"\n=== SUMMARY ===")
print(f"  Foundational → boolean:  {stats['foundational']}")
print(f"  status dropped:          {stats['dropped']}")
print(f"  No status field:         {stats['no_status']}")
print(f"  Unknown values:          {stats['unknown']}")
print(f"  Total files:             {len(files)}")

if DRY_RUN:
    print("\n*** DRY RUN — no files were modified. Re-run without --dry-run to apply. ***")
else:
    print("\n*** Files updated. ***")
