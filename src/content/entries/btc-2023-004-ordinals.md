---
title: "Ordinals"
deck: "On January 20, 2023, Casey Rodarmor released ord v0.4.0 and bitcoin acquired NFTs, an internal civil war, and a new fee market."
era: "Frauds"
type: "Event"
date: 2023-01-20
sourcePlatform: "rodarmor.com / Bitcoin mainnet"
locked: true
foundational: false
creator: "Casey Rodarmor"
btcPriceAtOrigin: "~$22,700"
blockHeightAtOrigin: 774464
heroImage: "/images/entries/ordinals.png"
heroImageCaption: "Inscription #0 — a black-and-white pixel-art skull, inscribed by Casey Rodarmor on December 14, 2022, six weeks before the public launch."
heroImageCredit: "Casey Rodarmor / ordinals.com"
related: []
sources:
  - url: "https://rodarmor.com/blog/inscribing-mainnet/"
    label: "Casey Rodarmor, Inscribing Mainnet (Jan 20, 2023)"
    primary: true
  - url: "https://docs.ordinals.com/"
    label: "Ordinal Theory Handbook"
  - url: "https://www.coindesk.com/consensus-magazine/2023/12/04/casey-rodarmor-bitcoin-ordinals-theory-nfts/"
    label: "CoinDesk, Casey Rodarmor: The Bitcoin Artist (Dec 2023)"
---

On January 20, 2023, Casey Rodarmor published a blog post titled Inscribing Mainnet announcing the release of ord version 0.4.0, the first version of his software capable of inscribing arbitrary data onto individual satoshis on the bitcoin mainnet. The post was four paragraphs long. The protocol it announced — ordinal theory, with its associated practice of inscriptions — would within months produce the largest sustained increase in bitcoin transaction fees since 2017, the first non-fungible tokens native to the bitcoin blockchain, and the deepest internal cultural fracture in bitcoin since the Block Size Wars.

Inscriptions had existed in Rodarmors testnet code since 2022. The first mainnet-ready inscription, inscription number zero, was a black-and-white pixel-art skull he inscribed on December 14, 2022, six weeks before the public launch. The protocol itself relied on the Taproot upgrade activated in November 2021 — without Taproots witness data structure, the technique would not have been viable. In a sense, ordinals had been latent in the protocol for fourteen months before anyone built them.

Rodarmors framing was deliberately playful. Make Bitcoin Fun Again, he tweeted on January 29, with its echoes of a different slogan. He drew inspiration from generative art collectives on Ethereum, particularly Erick Calderons Art Blocks, but found Ethereums developer experience repugnant. He called inscriptions digital artifacts, not NFTs, partly because the term NFT was already culturally compromised and partly because inscriptions worked differently — the data lived directly on bitcoin Layer 1, not in a smart contract pointing at IPFS.

The reaction was immediate and bifurcated. NFT enthusiasts who had been priced out of Ethereum by gas fees flooded in. Bitcoin Maximalists, especially those who had spent the Block Size Wars defending small blocks against perceived chain-bloat threats, were apoplectic. The arguments were familiar in shape, novel in target: ordinals broke fungibility (a marked sat could be identified and discriminated against), reduced privacy, raised fees for ordinary users, and treated the worlds most secure blockchain as a database for cartoon JPEGs. The pro-ordinal argument was equally direct: inscriptions paid miners in fees, reinforcing the long-term security budget as block subsidies declined; they used capacity that would otherwise be wasted; and bitcoin is a permissionless system, which meant no one had standing to object.

The numbers did not slow down. By April 8, 2023, total inscriptions passed one million. By August 4, twenty-one million. The BRC-20 token standard, an experiment by an anonymous on-chain analyst named Domo on March 8, 2023, demonstrated that inscriptions could be used to issue fungible tokens on bitcoin — a development Rodarmor had not anticipated and did not encourage. By mid-2023, ordinal-related transactions regularly accounted for over half of all bitcoin transactions by count.

Rodarmor himself, who had been willing to engage critics in the early months, grew quieter. The Bitcoin Improvement Proposal he submitted to formalize ordinals into bitcoin documentation was never accepted by Bitcoin Core developers — though, as Rodarmor pointed out, it was not requesting any change to the codebase, merely documenting what had already happened. He went on to build the Runes protocol, which launched at the April 2024 halving and aimed to do for fungible tokens what ordinals did for non-fungible ones, with less chain bloat.

The catalog records ordinals without taking a position on whether they belong on bitcoin. The reasons to include the entry are independent of that question. Ordinals are an artifact whose presence in bitcoin culture is undeniable, whose origin is precisely datable, and whose effects — on fees, on the developer community, on the question of what bitcoin is for — will be visible in the protocol for as long as the protocol exists. The internal fracture they produced is itself part of bitcoin's cultural record.

A community that cannot tolerate disagreement about its own purpose is not the community the cypherpunks were trying to build.
