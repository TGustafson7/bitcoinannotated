---
catalogId: "BTC.2014.003"
title: "Trezor"
deck: "The first hardware wallet, made by two Czechs in a Prague basement."
era: "Dark Forest"
foundational: true
type: "Hardware"
date: 2014-07-29
blockHeightAtOrigin: 313000
creator: "Pavol \"Stick\" Rusnák and Marek \"Slush\" Palatinus"
sourcePlatform: "SatoshiLabs"
locked: true
heroImage: "/images/entries/trezor.jpg"
heroImageCaption: "The Trezor Model One, the first hardware wallet, 2014."
heroImageCredit: "SatoshiLabs"
sources:
  - url: "https://blog.trezor.io/the-first-bitcoin-hardware-wallet-c63c0d24f9eb"
    label: "Trezor blog — The first bitcoin hardware wallet"
  - url: "https://github.com/trezor/trezor-firmware"
    label: "Trezor firmware on GitHub (open source since launch)"
related: []
---
The first Trezor — formally, the Trezor Model One — shipped to its earliest customers on July 29, 2014, five months after Mt. Gox's collapse. It was the size of a car key fob, made of injection-molded plastic, weighed twelve grams, and contained a small monochrome display, two physical buttons, and a microcontroller that did one thing well and was incapable of doing anything else. It cost approximately one hundred dollars. It was manufactured in Prague by SatoshiLabs, a small company founded by two members of the early Czech bitcoin community: Marek *Slush* Palatinus, who had previously built the bitcoin community's most-used mining pool, and Pavol *Stick* Rusnák, a software engineer active in the early Czech bitcoin and open-source communities. The two men had begun discussing the device in 2012. Mt. Gox had given the project an obvious commercial argument it had previously lacked.

The technical proposition was straightforward. The Trezor stored a user's bitcoin private keys on a chip that was never connected to the internet. To send a transaction, the user composed it on their computer using compatible software, sent the unsigned transaction to the Trezor over USB, confirmed the details on the device's small screen, and pressed a button. The Trezor signed the transaction with the offline private key, returned the signed transaction over USB, and the computer broadcast it to the network. The private key never left the device. The device never connected to the internet. The signature happened on a chip that, by design, could not be remotely accessed by anything.

The device shipped with a particular feature that has since become standard across the entire hardware-wallet category and that the Trezor team substantially invented: a *recovery seed*. On first setup, the device displayed a sequence of twelve or twenty-four English words drawn from a standardized list — a list that itself became a Bitcoin Improvement Proposal called BIP-39. The user wrote the words down on a piece of paper. If the device was lost, stolen, or destroyed, those words could be entered into any compatible wallet to reconstruct the original keys and recover the bitcoin. The seed phrase has, in the decade since, acquired an almost liturgical weight in bitcoin culture: written in pencil, stamped into stainless-steel plates, memorized, divided among trusted family members, and treated with the kind of attention previously reserved for safety-deposit-box keys and life insurance policies. The words are, in a sense, the bitcoin.

Trezor's commercial success was modest by Silicon Valley standards and consequential by bitcoin community standards. Tens of thousands of devices shipped in the first two years; hundreds of thousands by 2018; millions by 2025. The company spawned competitors — Ledger in France in 2014, Coldcard in Canada in 2018, BitBox in Switzerland — and an entire industry of accessory manufacturers producing seed-phrase-storage products that range from twenty-dollar metal washers to thousand-dollar engraved titanium plates. The hardware-wallet category, in 2014 a curiosity, is now the recommended custody solution in essentially every responsible bitcoin guide.

The cultural significance, distinct from the commercial one, was that Trezor demonstrated the protocol's central promise was actually achievable in physical practice. Bitcoin's claim to be self-custodial money depended on individual users being able to hold their own keys. For the first six years of the asset's existence, *holding your own keys* meant either running full bitcoin software on a desktop computer with all the security pitfalls that entailed, or trusting an exchange and accepting the trade-offs the 2011 Mt. Gox incident had taught. Trezor proposed a third option, which the bitcoin community has by and large adopted: a small dedicated device, doing one thing, that turns the abstract slogan *not your keys, not your coins* into an actionable instruction. Stick and Slush built the instruction. The keys are in the box. The box is in the drawer. The bitcoin is on the network. The arrangement, which would have seemed exotic in 2014, is now the unremarkable default for anyone holding more than a few months' rent.
