#!/usr/bin/env python3
"""
Batch 2 fixes for bitcoinannotated catalog.

Applies factual corrections identified through deep-dive verification.
Each fix is a (filepath, old_str, new_str) tuple. Script reports what
matched and what didn't, so any mismatches can be fixed by hand.

Run from repo root: python3 apply_batch2_fixes.py
"""

import os
import sys
from pathlib import Path

# Repo-relative paths
ENTRIES_DIR = "src/content/entries"

FIXES = [
    # ----------------------------------------------------------------
    # GENESIS BLOCK — math error, place name, soften "two surviving copies"
    # ----------------------------------------------------------------
    {
        "file": "btc-2009-001-genesis-block.md",
        "old": "Six days is forty-eight thousand percent longer than the design target.",
        "new": "Six days is roughly eighty-six thousand percent longer than the design target — more than eight hundred times longer.",
        "reason": "Math correction: 6 days = 8640 minutes, 8640/10 = 864x = ~86,400% longer (entry said 48,000%)",
    },
    {
        "file": "btc-2009-001-genesis-block.md",
        "old": "Of the verified surviving complete copies — meaning the full newspaper, not just the front page — only two are publicly accounted for, both acquired from the British National Archives by collectors in 2014.",
        "new": "For years, the verified surviving complete copies — meaning the full newspaper, not just the front page — were thought to be limited to a small handful, with two acquired from the London National Archives by collectors in January 2014. As bitcoin's profile rose, additional copies surfaced from private collections; one was offered for public auction at Bitcoin 2026 in Las Vegas.",
        "reason": "Fix: 'British National Archives' should be 'London National Archives' (per the cited source thetimes03jan2009.com). Soften 'only two' claim — more copies have surfaced, including a January 2026 BMAG auction.",
    },

    # ----------------------------------------------------------------
    # THE PIZZA — Sturdivant nationality / location correction
    # ----------------------------------------------------------------
    {
        "file": "btc-2010-002-the-pizza.md",
        "old": "Another forum user, posting from the United Kingdom, ordered the pizzas online for delivery to Hanyecz's address.",
        "new": "Another forum user — a 19-year-old in California named Jeremy Sturdivant, posting under the handle *jercos* — ordered the pizzas from a Jacksonville Papa John's, paying with his own debit card.",
        "reason": "Sturdivant was a 19-year-old in California, not the UK. He ordered pizzas from California to be delivered in Florida.",
    },

    # ----------------------------------------------------------------
    # SILK ROAD — Ulbricht's school/origin, altoid breadcrumb, petition signatures
    # ----------------------------------------------------------------
    {
        "file": "btc-2011-001-silk-road.md",
        "old": "Its creator was a 26-year-old physics graduate from Austin named Ross Ulbricht, working initially under the username *Admin* and later, on the advice of an associate, under the more cinematic alias *Dread Pirate Roberts* — borrowed from *The Princess Bride*, in which the title is passed from one captain to the next so the legend never dies.",
        "new": "Its creator was Ross Ulbricht, a 26-year-old from Austin, Texas — a physics undergraduate from the University of Texas at Dallas with a master's in materials science from Penn State — working initially under the username *Admin* and later, by 2012, under the more cinematic alias *Dread Pirate Roberts*, borrowed from *The Princess Bride*, in which the title is passed from one captain to the next so the legend never dies.",
        "reason": "Ulbricht was a UT Dallas physics undergrad with Penn State MS in materials science, not a 'physics graduate from Austin'. He was from Austin (Eagle Scout there) but degree was elsewhere. He adopted DPR around 2012 (not 'on advice of an associate' — too specific).",
    },
    {
        "file": "btc-2011-001-silk-road.md",
        "old": "The decisive break came from an Internal Revenue Service investigator named Gary Alford, who searched old internet forums for the username *altoid* and found a 2011 BitcoinTalk post in which a user by that name had advertised Silk Road and, separately, listed a personal Gmail address in the form *firstname.lastname@gmail.com*.",
        "new": "The decisive break came from an Internal Revenue Service investigator named Gary Alford, who searched old internet forums for the username *altoid*. The trail had two pieces. In January 2011, before Silk Road launched, *altoid* had advertised the new marketplace on a magic mushrooms forum. Months later, *altoid* posted on BitcoinTalk asking for IT help with a venture-backed bitcoin startup, and gave the contact email rossulbricht@gmail.com.",
        "reason": "The 'altoid' breadcrumb was actually two distinct posts: the Silk Road advertisement was on a magic mushrooms forum (Jan 27, 2011), and the BitcoinTalk post asked for IT help and contained the Gmail. Entry conflated them.",
    },
    {
        "file": "btc-2011-001-silk-road.md",
        "old": "His mother Lyn Ulbricht spent the next decade running a clemency campaign that gathered more than 170,000 signatures.",
        "new": "His mother Lyn Ulbricht spent the next decade running a clemency campaign whose petition gathered hundreds of thousands of signatures.",
        "reason": "Petition signature count: by 2024 the campaign had over 300,000 signatures (sources differ on exact total). The '170,000' figure is from earlier years and undersells the count by arrest time.",
    },

    # ----------------------------------------------------------------
    # FIRST MT GOX HACK — soften unverifiable specifics
    # ----------------------------------------------------------------
    {
        "file": "btc-2011-002-first-mt-gox-hack.md",
        "old": "The first sign of trouble came two days earlier. On June 17, an anonymous user calling themselves *~cRazIeStinGeR~* posted to Pastebin offering to sell a copy of the Mt. Gox user database. Karpelès denied the breach.",
        "new": "Trouble had been mounting for days. On June 13, Mt. Gox publicly disclosed that approximately 25,000 BTC had been stolen from 478 user accounts. Days later, the exchange's user database was leaked online. Karpelès initially downplayed the severity.",
        "reason": "The specific cRazIeStinGeR/Pastebin claim is unverifiable in primary sources. Replacing with documented June 13 25,000 BTC disclosure and database leak (per multiple sources).",
    },
    {
        "file": "btc-2011-002-first-mt-gox-hack.md",
        "old": "The largest single transaction observed was a sale of 261,383.7630 bitcoin at one cent each, executed at 17:51:16 UTC.",
        "new": "The largest single transaction observed was a sale of more than 260,000 bitcoin at one cent each.",
        "reason": "The specific timestamp 17:51:16 UTC is unverifiable. The exact 261,383.7630 figure also requires sourcing not present in available materials. Softening to 'more than 260,000' is well-supported.",
    },
    {
        "file": "btc-2011-002-first-mt-gox-hack.md",
        "old": "The total exposure was estimated at approximately \\$8.75 million in bitcoin equivalent, affecting around nine hundred user accounts.",
        "new": "Karpelès estimated the actual financial exposure at approximately two thousand bitcoin extracted before the cap held, a sum the exchange claimed it would absorb.",
        "reason": "The '$8.75 million / 900 accounts' figures are not well-supported. Multiple sources note the actual extracted amount was ~2,000 BTC. Restating in those terms.",
    },

    # ----------------------------------------------------------------
    # MAGIC INTERNET MONEY — drop fabricated South Park production claim
    # ----------------------------------------------------------------
    {
        "file": "btc-2013-002-magic-internet-money.md",
        "old": "*South Park*'s art department drafted the flyer in early November 2013, three days after the bitcoin ad went live. The episode was already in production by then. Whether the resemblance is deliberate homage or coincidence has never been formally addressed by *South Park*'s creators. It is, regardless, the second time the same image had appeared on a major media platform within seven days, and the timing is difficult to attribute to chance.",
        "new": "Whether the resemblance is deliberate homage or coincidence has never been formally addressed by *South Park*'s creators. Cartman's wizard-king costume in *Black Friday* drew on existing material from *South Park: The Stick of Truth*, then in pre-release marketing, so the visual lineage is not strictly causal. What is true is that the same wizard-in-robes silhouette appeared on two major media platforms within seven days. Readers can decide what to do with the timing.",
        "reason": "The 'art department drafted the flyer three days after the bitcoin ad went live' claim is unsourced and likely fabricated. South Park's wizard-king visual draws on the existing Stick of Truth game promotional material. Reframe as 'visual lineage exists, timing is what it is.'",
    },

    # ----------------------------------------------------------------
    # CYPRUS — fix the parliamentary vote claim
    # ----------------------------------------------------------------
    {
        "file": "btc-2013-003-cyprus.md",
        "old": "The Cypriot parliament voted the proposal down on Tuesday, March 19, in a unanimous rejection that included every member of the ruling party.",
        "new": "The Cypriot parliament voted the proposal down on Tuesday, March 19. The result was 36 against, 19 abstentions, and zero in favor — every member of the ruling DISY party abstained, leaving the bill without a single supportive vote.",
        "reason": "The original claim of 'unanimous rejection' was wrong. The ruling DISY party didn't vote against — they abstained (19 abstentions). The opposition voted no (36 against). Zero votes in favor.",
    },

    # ----------------------------------------------------------------
    # BITCOIN PIZZA DAY — Sturdivant nationality + NYT date precision
    # ----------------------------------------------------------------
    {
        "file": "btc-2014-001-bitcoin-pizza-day.md",
        "old": "A British teenager named Jeremy Sturdivant — username *jercos* — took the deal, called Papa John's, paid in dollars, and had the pizzas delivered.",
        "new": "A 19-year-old in California named Jeremy Sturdivant — username *jercos* — took the deal, called a Jacksonville Papa John's, paid in dollars on his debit card, and had the pizzas delivered cross-country to Hanyecz's home in Florida.",
        "reason": "Sturdivant was a 19-year-old California resident, not a 'British teenager.' He ordered from California for delivery to Florida.",
    },
    {
        "file": "btc-2014-001-bitcoin-pizza-day.md",
        "old": "*The New York Times* ran a piece on Hanyecz's transaction in early 2014.",
        "new": "*The New York Times* ran a piece on Hanyecz's transaction in late 2013, written by Nick Bilton.",
        "reason": "NYT article was December 2013 (per VentureBeat coverage), not 'early 2014.' Author was Nick Bilton.",
    },
    {
        "file": "btc-2014-001-bitcoin-pizza-day.md",
        "old": "Sturdivant, the British teenager who took the order, spent the bitcoin on travel within weeks.",
        "new": "Sturdivant, the Californian who took the order, spent the bitcoin within months on a road trip with his then-girlfriend and on computer parts.",
        "reason": "Same nationality fix; his actual stated use of the bitcoin was a road trip and computer parts.",
    },

    # ----------------------------------------------------------------
    # TREZOR — soften unverifiable claim about Stick
    # ----------------------------------------------------------------
    {
        "file": "btc-2014-003-trezor.md",
        "old": "Pavol *Stick* Rusnák, a software engineer who had been writing for the cypherpunks since the late 2000s.",
        "new": "Pavol *Stick* Rusnák, a software engineer active in the early Czech bitcoin and open-source communities.",
        "reason": "The 'writing for the cypherpunks since the late 2000s' claim is not well-sourced and is a soft fabrication. Replacing with a verifiable description.",
    },

    # ----------------------------------------------------------------
    # BITLICENSE — Lawsky departure timing
    # ----------------------------------------------------------------
    {
        "file": "btc-2015-001-the-bitlicense.md",
        "old": "Lawsky resigned from the NYDFS the same month the BitLicense became final and joined a private practice that, among other clients, advised cryptocurrency firms on compliance.",
        "new": "Lawsky departed the NYDFS the following month, in July 2015 — having announced his exit earlier that spring — and founded a private consultancy that, among other clients, advised cryptocurrency firms on compliance.",
        "reason": "Lawsky left in July 2015 (the month after the BitLicense was finalized in June 2015), having announced the departure earlier that spring. Entry's 'same month' is wrong.",
    },
]


def apply_fixes(repo_root: Path):
    fixes_applied = 0
    fixes_failed = []

    for fix in FIXES:
        filepath = repo_root / ENTRIES_DIR / fix["file"]
        if not filepath.exists():
            print(f"  ❌ FILE NOT FOUND: {filepath}")
            fixes_failed.append((fix["file"], "FILE NOT FOUND"))
            continue

        content = filepath.read_text(encoding="utf-8")

        if fix["old"] not in content:
            # try with a normalized version of the dollar sign escape
            old_alt = fix["old"].replace("\\$", "$")
            if old_alt in content:
                # match via the unescaped dollar sign
                content_new = content.replace(old_alt, fix["new"], 1)
            else:
                print(f"  ⚠️  NO MATCH in {fix['file']}")
                print(f"     Looking for: {fix['old'][:80]}…")
                fixes_failed.append((fix["file"], fix["old"][:80]))
                continue
        else:
            content_new = content.replace(fix["old"], fix["new"], 1)

        filepath.write_text(content_new, encoding="utf-8")
        print(f"  ✅ Fixed: {fix['file']}")
        print(f"     Reason: {fix['reason']}")
        fixes_applied += 1

    print()
    print(f"=========================================")
    print(f"Applied: {fixes_applied} / {len(FIXES)}")
    if fixes_failed:
        print(f"Failed:  {len(fixes_failed)}")
        for f, snippet in fixes_failed:
            print(f"  - {f}: {snippet}")
    print(f"=========================================")
    return fixes_applied, fixes_failed


if __name__ == "__main__":
    if len(sys.argv) > 1:
        repo_root = Path(sys.argv[1]).resolve()
    else:
        repo_root = Path.cwd()

    if not (repo_root / ENTRIES_DIR).exists():
        print(f"❌ Could not find {ENTRIES_DIR} under {repo_root}")
        print(f"   Run from repo root, or pass repo path as argument.")
        sys.exit(1)

    print(f"Applying batch 2 fixes to: {repo_root}\n")
    apply_fixes(repo_root)
