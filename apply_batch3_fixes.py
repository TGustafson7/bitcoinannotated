#!/usr/bin/env python3
"""
Apply batch 3 editorial corrections to bitcoinannotated entries.

7 fixes across 5 entries:
- Whitepaper: math error (68→64 days), restore exact abstract quote
- Bitcoin Orange: remove fabricated Coldcard bag color claim and pizza box claim
- Mt. Gox Collapse: replace "single sophisticated actor" with documented Russian theft ring
- Lightning Whitepaper: drop unsourced AT&T claim, attribute to Bitrefill (the verifiable service)
- Block Size Wars: fix reversed chronology (BCH forked Aug 1, SegWit activated Aug 24)

Run from repo root:
    python3 apply_batch3_fixes.py
"""

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
ENTRIES_DIR = REPO_ROOT / "src" / "content" / "entries"

FIXES = [
    # ---- Whitepaper ----
    {
        "file": "btc-2008-001-the-whitepaper.md",
        "old": "Hal Finney was the first to respond constructively. Sixty-eight days later, on January 3, 2009, the network would be live.",
        "new": "Hal Finney was the first to respond constructively. Sixty-four days later, on January 3, 2009, the network would be live.",
        "reason": "Math correction: October 31, 2008 to January 3, 2009 is 64 days, not 68. (Oct: 1 day remaining + Nov: 30 + Dec: 31 + Jan: 3 = 64.)",
    },
    {
        "file": "btc-2008-001-the-whitepaper.md",
        "old": "Its first sentence — *a purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution* — is among the most-quoted sentences in modern computing.",
        "new": "Its first sentence — *a purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without the burdens of going through a financial institution* — is among the most-quoted sentences in modern computing.",
        "reason": "Restore 'the burdens of' to make the quote exact. The original whitepaper abstract reads '...without the burdens of going through a financial institution.'",
    },

    # ---- Bitcoin Orange ----
    {
        "file": "btc-2010-001-bitcoin-orange.md",
        "old": "*Laser eyes*, the 2021 profile-picture campaign that pushed the price toward six figures, would not have been recognizable as bitcoin-coded without the orange that surrounded the eyes. The hardware wallet manufacturer Coldcard packages its devices in orange anti-static bags. The bitcoin pizza parties on May 22 are reliably catered with pizzas whose boxes are, by some quiet convention, also orange.",
        "new": "*Laser eyes*, the 2021 profile-picture campaign that pushed the price toward six figures, would not have been recognizable as bitcoin-coded without the orange that surrounded the eyes. The hardware wallet manufacturer Coldcard prints its branding — and its tamper-evident bag numbers — in orange. The Bitcoin Magazine cover, the Bitcoin 2021 Miami stage, the Bitcoin 2024 Nashville stage, the El Salvador Bitcoin Office's logo: orange. Once one starts cataloging the convention, it becomes difficult to find a bitcoin-aligned product that breaks it.",
        "reason": "Remove two fabricated specifics. (1) Coldcard's tamper-evident bag is actually a clear plastic bag with a blue border and orange Coinkite branding text — it is not 'orange anti-static bags.' (2) Pizza boxes for Bitcoin Pizza Day are not 'by some quiet convention' orange — Papa John's branding is red, and there is no documented orange-pizza-box convention. Replacing both with verifiable orange-branding examples.",
    },

    # ---- Mt. Gox Collapse ----
    {
        "file": "btc-2014-002-the-mt-gox-collapse.md",
        "old": "The thefts were traced to a single sophisticated actor whose techniques exploited the same auditor-account vulnerability that had produced the 2011 flash crash. Karpelès, in this telling, had not stolen the missing bitcoin. He had simply failed, for two and a half years, to discover that they were being stolen, and the company's accounting infrastructure had been incapable of detecting the discrepancy.",
        "new": "The 2023 indictment unsealed in the Southern District of New York attributed the long-running theft to two Russian nationals — Alexey Bilyuchenko and Aleksandr Verner — together with unnamed co-conspirators, who had obtained unauthorized access to a Mt. Gox server housing the exchange's wallet keys and had drained at least 647,000 of the missing bitcoin between 2011 and 2014. A substantial share of the stolen bitcoin was laundered through BTC-e, the exchange that Bilyuchenko ran together with Alexander Vinnik, until BTC-e was seized by United States law enforcement in 2017. Karpelès, in this telling, had not stolen the missing bitcoin. He had simply failed, for more than two years, to discover that they were being stolen, and the company's accounting infrastructure had been incapable of detecting the discrepancy.",
        "reason": "Major correction. The 'single sophisticated actor' framing is wrong. Per the 2023 SDNY indictment, the long-running Mt. Gox theft is attributed to Russian nationals Alexey Bilyuchenko and Aleksandr Verner with unnamed co-conspirators, who drained at least 647,000 BTC via unauthorized server access; much was laundered through BTC-e (run with Alexander Vinnik). Also drops the unsourced 'auditor-account vulnerability' linkage to the 2011 flash crash.",
    },

    # ---- Lightning Whitepaper ----
    {
        "file": "btc-2016-001-lightning-whitepaper.md",
        "old": "The first Lightning payment on the bitcoin mainnet was conducted by Alex Bosworth on December 27, 2017, paying his AT&T phone bill.",
        "new": "The first widely reported Lightning payment on the bitcoin mainnet was conducted by Alex Bosworth in late December 2017, who paid an actual phone bill through the prepaid-mobile service Bitrefill and announced the transaction on Twitter on December 28.",
        "reason": "The AT&T detail is not in any of the contemporary coverage of the transaction. Bosworth used Bitrefill (a prepaid mobile top-up service that supports many carriers), and his tweet only describes 'my actual phone bill.' Fix to match the documented record.",
    },

    # ---- Block Size Wars ----
    {
        "file": "btc-2017-002-the-block-size-wars.md",
        "old": "The resolution came in two phases. In August 2017, a soft-fork upgrade called Segregated Witness — *SegWit* — activated on the bitcoin network. SegWit restructured how transaction data was organized to effectively increase block capacity without raising the formal one-megabyte limit. It had been authored primarily by Pieter Wuille, a long-tenured core developer, and shipped after a complex multi-year coordination effort. Two days later, on August 1, 2017, the large-block faction executed what they had been threatening: a hard fork creating a new chain called Bitcoin Cash, with an eight-megabyte block size.",
        "new": "The resolution came in two phases. On August 1, 2017, the large-block faction executed what they had been threatening: a hard fork at block 478,558 creating a new chain called Bitcoin Cash, with an eight-megabyte block size. Twenty-three days later, on August 24, 2017, a soft-fork upgrade called Segregated Witness — *SegWit* — activated on the original bitcoin network at block 481,824. SegWit restructured how transaction data was organized to effectively increase block capacity without raising the formal one-megabyte limit. It had been authored primarily by Pieter Wuille, a long-tenured core developer, and shipped after a complex multi-year coordination effort.",
        "reason": "Significant chronology fix. Entry had the order reversed. Bitcoin Cash forked first (August 1, 2017, block 478,558). SegWit activated 23 days later (August 24, 2017, block 481,824). The entry's framing of 'two days later' was wrong in both direction and duration.",
    },
]


def apply_fix(fix: dict, dry_run: bool = False) -> bool:
    path = ENTRIES_DIR / fix["file"]
    if not path.exists():
        print(f"  ❌ Missing file: {path}")
        return False

    text = path.read_text(encoding="utf-8")
    if fix["old"] not in text:
        print(f"  ❌ NOT FOUND in {fix['file']}")
        print(f"     Looking for: {fix['old'][:120]}...")
        return False

    new_text = text.replace(fix["old"], fix["new"], 1)
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    print(f"  ✅ Fixed: {fix['file']}")
    print(f"     Reason: {fix['reason']}")
    return True


def main():
    if not ENTRIES_DIR.exists():
        print(f"ERROR: entries directory not found at {ENTRIES_DIR}")
        print("Run this script from the repo root.")
        sys.exit(1)

    dry_run = "--dry-run" in sys.argv
    mode = "DRY RUN" if dry_run else "APPLYING"
    print(f"{mode} batch 3 fixes to: {REPO_ROOT}\n")

    applied = 0
    for fix in FIXES:
        if apply_fix(fix, dry_run=dry_run):
            applied += 1
        print()

    print("=" * 41)
    print(f"Applied: {applied} / {len(FIXES)}")
    print("=" * 41)

    if applied != len(FIXES):
        sys.exit(1)


if __name__ == "__main__":
    main()
