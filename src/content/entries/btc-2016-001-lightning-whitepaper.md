---
catalogId: "BTC.2016.001"
title: "The Lightning Network Whitepaper"
deck: "The scaling answer the small-blockers had been promising."
era: "The Long Wait"
type: "Document"
foundational: true
date: 2016-01-14
blockHeightAtOrigin: 393244
creator: "Joseph Poon and Thaddeus Dryja"
sourcePlatform: "lightning.network"
locked: true
heroImage: "/images/entries/lightning.png"
heroImageCaption: "The Lightning Network whitepaper, January 14, 2016."
heroImageCredit: "Joseph Poon and Thaddeus Dryja"
sources:
  - url: "https://lightning.network/lightning-network-paper.pdf"
    label: "The Bitcoin Lightning Network — Scalable Off-Chain Instant Payments (Poon & Dryja, January 2016)"
    primary: true
  - url: "https://bitcoinmagazine.com/technical/the-lightning-network-the-second-layer-explained"
    label: "Bitcoin Magazine — The Lightning Network Explained"
related: []
---
The Lightning Network whitepaper was published on January 14, 2016, by two engineers named Joseph Poon and Thaddeus Dryja. It ran to fifty-nine pages, was titled *The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments*, and proposed a system for routing bitcoin transactions through a network of payment channels that would settle to the bitcoin blockchain only when the channels closed. The core idea — already informally circulating in the developer community for several years — was that two parties could open a long-lived bilateral channel by jointly committing funds to a multi-signature address on the main chain, then conduct any number of subsequent transactions between themselves by exchanging signed but unbroadcast updates to the channel's balance. Only the eventual closing transaction would touch the blockchain. The intermediate transactions, however numerous, would not.

The paper's larger claim was that channels could be chained. If Alice had a channel with Bob and Bob had a channel with Carol, Alice could pay Carol by routing the payment through Bob using a cryptographic technique called a *hashed timelock contract* — a kind of conditional payment that would either complete in full or roll back in full, with no possibility of any intermediate routing node stealing funds. The implication, scaled across a sufficiently large network of interconnected channels, was that bitcoin could process arbitrary numbers of small payments at near-zero cost without requiring any change to the underlying protocol's block size or transaction throughput. The base layer would handle final settlement. The second layer would handle commerce.

The political timing of the paper's publication was not accidental. The Block Size Wars were then at their most intense, and the central argument of the small-block faction — that scaling could be achieved without raising the block size limit — required some plausible alternative mechanism. The Lightning Network was the alternative. Its publication gave Pieter Wuille, Adam Back, and the other Bitcoin Core developers concrete intellectual property to point at when their large-block opponents demanded to know how the network was supposed to handle ten thousand transactions per second on a one-megabyte block. The answer, after January 14, 2016, was: through Lightning. Whether Lightning would actually work was, on the day of publication, an open question. Whether the small-block argument now had a credible technical foundation was no longer one.

Implementation took longer than the bitcoin community is generally willing to admit. The protocol's reference specifications — the *BOLT* documents, *Basis of Lightning Technology* — were not finalized until December 2017. The first widely reported Lightning payment on the bitcoin mainnet was conducted by Alex Bosworth in late December 2017, who paid an actual phone bill through the prepaid-mobile service Bitrefill and announced the transaction on Twitter on December 28. Network capacity, measured in bitcoin locked into channels, grew slowly through 2018 and 2019, then more rapidly after El Salvador's 2021 legal-tender adoption made Lightning a sovereign payment rail. By 2025, mainnet Lightning capacity exceeded eight thousand bitcoin, channel counts exceeded fifty thousand, and the protocol's user-facing wallets — Phoenix, Wallet of Satoshi, Mutiny, Strike — had collectively processed billions of dollars in payments. The transaction fees, on Lightning, are typically denominated in single-digit satoshis, which is to say fractions of a cent, which is to say what the original Bitcoin whitepaper had promised in 2008 and the base layer had not been able to deliver since 2017.

Whether Lightning has *succeeded* depends on what one expected of it. As an answer to the small-block faction's scaling promise, it succeeded in establishing a functional second layer that the bitcoin protocol could grow into. As a vehicle for global retail payments — the *coffee transaction* test that bitcoiners cite when arguing for the asset's monetary case — Lightning has been less than fully transformative. It works. It is faster than Visa and cheaper than wire transfers. It has not, however, displaced any major payment system. The thirty-foot view, ten years after the whitepaper, is that Lightning is an essential piece of bitcoin's monetary infrastructure that the bitcoin community uses, the bitcoin-curious have heard of, and the broader payment industry has mostly ignored. Whether the broader payment industry's view changes is, like most questions in bitcoin, a question the protocol is content to wait out.
