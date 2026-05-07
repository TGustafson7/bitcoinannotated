---
catalogId: "BTC.2021.006"
title: "The Taproot Activation"
deck: "Bitcoin's first major upgrade in four years. It passed without drama."
era: "Pandemic Era"
foundational: true
type: "Protocol Upgrade"
date: 2021-11-14
blockHeightAtOrigin: 709632
creator: "Pieter Wuille, Tim Ruffing, A.J. Townes, Jonas Nick (BIP authors); Greg Maxwell (proposal)"
sourcePlatform: "Bitcoin Core / soft fork"
locked: true
heroImage: "/images/entries/taproot.png"
heroImageCaption: "Block 709,632, mined at 5:15 UTC on November 14, 2021. Taproot active."
heroImageCredit: "Bitcoin Core developers / mempool.space"
sources:
  - url: "https://www.coindesk.com/tech/2021/11/13/taproot-bitcoins-long-anticipated-upgrade-activates-this-weekend"
    label: "CoinDesk — Taproot, Bitcoin's Long-Anticipated Upgrade, Has Activated"
  - url: "https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki"
    label: "BIP 341 — Taproot: SegWit version 1 spending rules"
related:
  - "BTC.2017.002"
  - "BTC.2023.001"
---
At 5:15 UTC on Sunday, November 14, 2021, a miner produced block 709,632. The block was, by every external measure, ordinary: it contained the transactions waiting in the mempool, paid the standard reward, and propagated through the network without incident. Internally, it was the activation block for the Taproot soft fork — the most significant upgrade to bitcoin's protocol in four years, and, when it occurred, an upgrade that nearly nobody noticed.

Taproot was first proposed by the Bitcoin Core developer Greg Maxwell in 2018 and was formalized over the following two years as three Bitcoin Improvement Proposals: BIP 340 introduced Schnorr signatures, replacing bitcoin's original ECDSA signature scheme with one that was smaller, faster, and crucially *linear*, allowing multiple signatures to be aggregated into one. BIP 341 introduced Pay-to-Taproot, a new transaction type that obscured the difference between simple single-signature transactions and complex multi-signature or smart-contract transactions on the chain. BIP 342 introduced Tapscript, a redesigned scripting language that leveraged the other two. The combined effect was that bitcoin transactions could now be more private, more efficient, and structurally more flexible without any change visible to ordinary users.

The activation method mattered as much as the upgrade itself. The 2017 SegWit fork had been preceded by what is now euphemistically called the *Block Size Wars* — a period of community division so severe it produced multiple chain splits and lasting personal animosities. The Taproot deployment was deliberately designed to avoid that. The activation method, called *Speedy Trial*, asked miners to signal support over a roughly two-week window; if ninety percent signaled, the upgrade locked in for activation approximately five months later. Locked-in occurred on June 12, 2021, at block 687,284. Slush Pool — the same pool that had mined the first block ever signaled for SegWit — mined the lock-in block. The five-month wait between lock-in and activation existed to give node operators and miners time to upgrade their software. Almost all of them did.

The cultural significance of Taproot, distinct from its technical content, was that it demonstrated that bitcoin could change its own rules without civil war. The protocol had been technically capable of soft-forking the entire time; what had been in question, after the Block Size Wars, was whether the social layer could coordinate. Taproot answered the question. The fork passed. The community disagreed only on small details. The chain did not split. The activation produced a brief flurry of celebratory commentary on Bitcoin Twitter, then was overtaken by other news within forty-eight hours. The most consequential immediate beneficiaries of the upgrade were Lightning Network developers, who could now build implementations that were indistinguishable on-chain from ordinary transactions, improving privacy substantially.

The longer-term consequence of Taproot, which was not visible at the moment of activation, was the technical substrate it created. By restructuring transaction witness data in ways that permitted significantly larger arbitrary payloads, Taproot incidentally made it possible to inscribe images, audio files, and arbitrary text directly onto the blockchain — a capability that would, fourteen months later, become the basis for Ordinals. The community that had agreed unanimously to ship Taproot would, in 2023, divide bitterly over what people had begun doing with it. That fight, however, was Taproot's grandchild rather than its problem. On November 14, 2021, the only thing that happened was that block 709,632 was mined, and bitcoin's rules quietly and durably changed.
