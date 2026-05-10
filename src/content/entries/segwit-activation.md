---
title: "SegWit Activation"
deck: "Block 481,824. The peace treaty that ended the Block Size Wars and unlocked the second layer."
era: "2017 Run"
type: "Event"
date: 2017-08-24
blockHeightAtOrigin: 481824
sourcePlatform: "Bitcoin protocol (BIP-141)"
locked: true
creator: "Pieter Wuille and Gregory Maxwell (BIP-141 authors); the broader Bitcoin Core development community"
heroImage: "/images/entries/segwit-activation.png"
heroImageCaption: "Bitcoin Magazine, August 24, 2017. SegWit activates at block 481,824."
heroImageCredit: "Bitcoin Magazine"
sources:
  - url: "https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki"
    label: "BIP-141: Segregated Witness (Consensus layer)"
    primary: true
  - url: "https://bitcoinmagazine.com/technical/segregated-witness-activates-bitcoin-what-expect"
    label: "Bitcoin Magazine — Segregated Witness Activates on Bitcoin (Aaron van Wirdum, August 24, 2017)"
  - url: "https://en.wikipedia.org/wiki/SegWit"
    label: "Wikipedia — SegWit"
related: []
---

The Block Size Wars produced a war but not a peace. The peace was SegWit. On August 24, 2017, at block 481,824, the soft fork known as Segregated Witness activated on the Bitcoin network. The proposal had been written by Pieter Wuille and Gregory Maxwell of Bitcoin Core in late 2015. It had spent eighteen months trapped in a political stalemate. Miners controlling roughly thirty percent of hash power refused to signal support, and the rest of the network could not force them. Then, in the summer of 2017, the rest of the network forced them.

The mechanism was a chain of three Bitcoin Improvement Proposals. BIP-141 was the actual SegWit protocol change: separate transaction signatures from transaction data, fix the malleability bug that had been blocking second-layer development, and accommodate a small effective block-size increase. BIP-148 was the threat — a User Activated Soft Fork written by an anonymous developer using the handle "Shaolin Fry," scheduled to begin orphaning blocks that did not signal SegWit support starting August 1, 2017. BIP-91 was the compromise — a miner-coordinated soft fork that activated on July 22 at block 477,120, once eighty percent of hash power signaled support, forcing miners to begin mandatory SegWit signaling and avoiding the chain split BIP-148 would have caused. SegWit locked in on August 9, at the end of the difficulty period ending at block 479,807, and activated fifteen days later at block 481,824.

The political achievement was as significant as the technical one. The Block Size Wars had been, at their core, a question about who decided. Did miners decide? Large businesses? Core developers? Users running full nodes? The UASF crowds answer was the last one. They were not technically wrong. A node that refused to accept blocks not signaling SegWit was, under the longest-chain rule, indistinguishable from any other node enforcing its own rules. If enough nodes did this and enough miners aligned with them, the network would coordinate around the new behavior whether large businesses approved or not. BIP-148 never had to actually fire. The threat that it would was sufficient. The miners blinked first.

The technical achievement opened doors that had been welded shut. Transaction malleability — the bug that allowed a third party to slightly modify a valid signature into another valid signature for the same transaction — had been blocking the Lightning Network for years. With SegWit, malleability was fixed. Lightning, drafted in early 2016, could finally be built. So could Taproot, four years later. So could the entire second-layer architecture that defines bitcoins scaling roadmap today. The protocols evolution after 2017 happens because of what activated at block 481,824.

The catalog includes SegWit as a discrete event because the war and the peace are different artifacts. The Block Size Wars entry covers the conflict — the actors, the stakes, the ideology. This entry covers the resolution — the block, the date, the soft fork, the unlock. The wars produced a winner. SegWit is what the winner did.
