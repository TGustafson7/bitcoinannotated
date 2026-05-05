---
catalogId: "BTC.2009.001"
title: "The Genesis Block"
deck: "The first block in bitcoin's chain carried a headline from a London newspaper. Fifteen years on, that headline is the closest thing bitcoin has to scripture."
era: "Genesis"
status: "Foundational"
type: "Quote / Embedded artifact"
date: 2009-01-03
btcPriceAtOrigin: "—"
creator: "Satoshi Nakamoto"
sourcePlatform: "Bitcoin protocol"
locked: true
heroImage: "/images/entries/genesis-block.jpg"
heroImageCaption: "The raw hex of Block 0. The embedded Times headline is visible in the right column, beginning at memory address 0x80."
heroImageCredit: "Public domain — bitcoin's first block."
sources:
  - url: "https://en.bitcoin.it/wiki/Genesis_block"
    label: "Bitcoin Wiki: Genesis block"
  - url: "https://www.blockchain.com/explorer/blocks/btc/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    label: "Block 0 on the blockchain"
  - url: "https://www.thetimes03jan2009.com/"
    label: "The Times, 03/Jan/2009 — surviving copies"
related:
  - "BTC.2010.001"
  - "BTC.2010.002"
---

On the third of January, 2009, an unknown person operating under the name Satoshi Nakamoto mined the first block of the bitcoin blockchain. Inside it, in the section of the block reserved for arbitrary data, they embedded a single sentence:

> *The Times 03/Jan/2009 Chancellor on brink of second bailout for banks*

The sentence is a verbatim quotation of the front-page headline of *The Times* of London, published the same day. It refers to Alistair Darling, then the British Chancellor of the Exchequer, who was reportedly considering a second round of taxpayer-funded bank rescues following the 2008 financial crisis.

The message has no technical function. It is not required by the protocol. It does not affect how bitcoin works. It is simply *there* — encoded in the chain, immutable, replicated to every full node on earth.

It has become, by general agreement, the closest thing bitcoin has to scripture.

## What it accomplishes

There are at least three things the message does at once.

The first is timestamp. By embedding a headline from a specific newspaper on a specific day, Nakamoto proved that the genesis block could not have been mined before that date. No one — not Nakamoto, not anyone else — could later claim to have pre-mined the chain. The newspaper headline is a cryptographic anchor: this happened on or after January 3, 2009, and not a moment earlier.

The second is commentary. The headline Nakamoto chose was not random. They could have quoted the weather, the sports section, the obituaries. They chose a story about taxpayer bailouts of insolvent banks. The choice reads as deliberate. Bitcoin was being released, in 2009, as an alternative to a banking system whose failures were at that moment being absorbed by the public.

The third is foundational text. A new financial system needs a kind of origin story. Nakamoto, by embedding a recognizable artifact of the old system in the first block of the new one, gave bitcoin one. Whether or not that was the intention is unclear. It is, regardless, what the message has come to mean.

## The six-day gap

There is a small mystery about the genesis block worth noting. The timestamp on Block 0 is January 3, 2009. The timestamp on Block 1 is January 9, 2009 — six full days later. Bitcoin's protocol targets ten minutes between blocks. Six days is forty-eight thousand percent longer than the design target.

Several explanations have been proposed. The most widely accepted is that Nakamoto mined the genesis block, then spent six days running tests on the bitcoin software using that block as a known starting point, and only on January 9 began the live chain in earnest. Another suggests Nakamoto had been working on bitcoin for some time before the public release and timed the genesis block specifically to match the *Times* headline. A third suggests they were simply mining the block itself for several days — its hash is unusually low even by 2009 standards, suggesting more computational effort than was strictly necessary.

The truth is unknown. Nakamoto, who corresponded with early bitcoin developers for two years before disappearing in 2010, has never publicly addressed the question.

## What is in Block 0

The genesis block contains a single transaction — a coinbase transaction, the kind that creates new bitcoin out of nothing as a reward to the miner. The transaction sends fifty bitcoin to the address `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`.

Those fifty bitcoin cannot be spent. Due to a quirk of the way the genesis block is hardcoded into the bitcoin software — one which appears in every full-node implementation of bitcoin since 2009 — the coinbase transaction of Block 0 is treated as a special case and excluded from the unspent-transaction-output set. Whether this was intentional or accidental on Nakamoto's part has been debated for years and not resolved.

The address itself, however, has continued to receive bitcoin from sympathetic donors for more than a decade. As of late 2025 it holds well over a hundred bitcoin in addition to the original fifty. None of those donations are unspendable; they could in principle be moved by anyone holding the private key. They have not been.

## The newspaper itself

A footnote worth preserving. *The Times* of London printed roughly six hundred thousand copies of its January 3, 2009 edition. Most were thrown away within a week, as most newspapers are. Of the verified surviving complete copies — meaning the full newspaper, not just the front page — only two are publicly accounted for, both acquired from the British National Archives by collectors in 2014.

This is, perhaps, the smaller miracle of the genesis block. The newspaper that Nakamoto cited as proof of bitcoin's birth has become, almost entirely, a paper artifact preserved only inside the blockchain itself.
