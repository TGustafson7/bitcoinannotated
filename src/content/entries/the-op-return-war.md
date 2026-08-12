---
title: "The OP_RETURN War"
deck: "A fight over eighty bytes of arbitrary data split bitcoin's node software in two and asked, again, what the chain is for."
era: "Now"
type: "Event"
date: 2025-10-10
sourcePlatform: "GitHub"
locked: false
blockHeightAtOrigin: 918450
related:
  - "ordinals"
  - "the-block-size-wars"
  - "bip-110"
  - "segwit-activation"
  - "nothing-stops-this-train"
sources:
  - url: "https://bitcoincore.org/en/releases/30.0/"
    label: "Bitcoin Core 30.0 release notes (OP_RETURN / datacarriersize)"
    primary: true
  - url: "https://github.com/bitcoin/bitcoin/pull/32359"
    label: "Bitcoin Core PR #32359, Remove arbitrary limits on OP_Return (Peter Todd, Apr 2025)"
    primary: true
  - url: "https://www.coindesk.com/tech/2025/05/06/bitcoin-developers-plan-op_return-removal-in-next-release"
    label: "CoinDesk, Bitcoin Developers Plan OP_RETURN Removal (May 6, 2025)"
  - url: "https://oakresearch.io/en/analyses/fundamentals/update-op-return-bitcoin-core-v30-core-knots-war"
    label: "OAK Research, OP_RETURN, Bitcoin Core v30, and the Core-Knots War"
---

Bitcoin has an argument it cannot finish. It surfaces every few years under a new name, and it is always the same argument: is bitcoin money, or is it a place to put things. The catalog records an earlier round as the Block Size Wars. The OP_RETURN War is the round that ran through 2025.

OP_RETURN is a small provision in bitcoin's scripting language that lets a transaction carry a few bytes of arbitrary data in a provably unspendable output. For years the software most of the network ran, Bitcoin Core, relayed only transactions whose OP_RETURN held eighty bytes or less. The limit was a convention, not a consensus rule, but it worked as a statement of taste: the chain was for coins, and data was tolerated in small doses.

Then the doses stopped being small. Ordinals had shown in 2023 that images and text could be inscribed into bitcoin; Runes, in 2024, built a token scheme that leaned on OP_RETURN directly. Data was arriving regardless of the limit, often through uglier workarounds that bloated the set of unspent outputs every node must track. The proposal to end the limit arrived as a pull request. On April 27, 2025, the developer Peter Todd opened one titled "Remove arbitrary limits on OP_Return (datacarrier) outputs," arguing the cap was already bypassed by miners and by rival software, and that an honest channel beat a limit that only rewarded evasion.

The reaction was a referendum in miniature. Todd's pull request drew four hundred and twenty-two thumbs-down against a hundred and five thumbs-up; Luke Dashjr, a longtime Core developer who treats inscriptions as spam, called the removal "utter insanity." The disagreement was not really about eighty bytes. It was about whether making data cheaper and cleaner to store was harm reduction or surrender.

Todd's pull request was closed under the weight of the objections, but the idea outlived it. On October 10, 2025, Bitcoin Core released version 30, carrying a companion change that raised the default OP_RETURN limit to a hundred thousand bytes, effectively uncapping it. Those who objected did the most bitcoin thing available to them: they ran different software. Node operators migrated to Bitcoin Knots, Dashjr's stricter implementation, which kept the old filters. Knots had been a rounding error, a few hundred nodes; through 2025 its share of the network climbed past a fifth. For the first time in years, a meaningful minority of the network was deliberately relaying by different rules than Core.

Nothing about bitcoin's consensus changed. No coins moved that should not have; no valid transaction became invalid. What changed was the picture of who agreed with whom, rendered in node counts. The war produced no winner because the question underneath it has no technical answer. A protocol that lets anyone transact also lets anyone inscribe, and the same neutrality that makes bitcoin useful as money makes it available as a ledger for everything else.

The fight did not end there. Within a year it hardened into an attempt to legislate the data away at the consensus level, and that attempt, BIP-110, failed in two blocks. The OP_RETURN War is the entry that explains why anyone tried.

Eighty bytes was never the point. The point was that bitcoin does not come with an opinion about what it is for, and its holders have never stopped supplying their own.
