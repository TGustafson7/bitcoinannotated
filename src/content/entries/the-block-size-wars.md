---
title: "The Block Size Wars"
deck: "The civil war that decided what bitcoin actually is."
era: "2017 Run"
type: "Event"
date: 2017-08-01
blockHeightAtOrigin: 478558
sourcePlatform: "Bitcoin protocol, BitcoinTalk, GitHub, r/bitcoin"
locked: true
heroImage: "/images/entries/block-size-wars.jpg"
heroImageCaption: "The chain split: bitcoin and Bitcoin Cash, August 1, 2017."
heroImageCredit: "Contemporary diagram"
sources:
  - url: "https://www.goodreads.com/book/show/57429394-the-blocksize-war"
    label: "Jonathan Bier — The Blocksize War (2021)"
  - url: "https://bitcoinmagazine.com/culture/the-long-road-to-segwit-how-bitcoins-biggest-protocol-upgrade-became-reality"
    label: "Bitcoin Magazine — The long road to SegWit"
  - url: "https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki"
    label: "BIP 148 — Shaolinfry's mandatory activation of segwit deployment proposal (the document the war pivoted on)"
    primary: true
related:
  - "the-whitepaper"
  - "hodl"
---
The dispute that became known as the Block Size Wars was, in its narrowest framing, an argument about a single number. The bitcoin protocol, as Satoshi Nakamoto had configured it in 2010, limited each block of transactions to one megabyte. As bitcoin's user base grew through 2014, 2015, and into 2016, that limit began producing visible congestion: transactions would queue in a backlog called the *mempool*, fees would rise, and confirmations would take hours rather than minutes. One faction, broadly aligned with large bitcoin businesses and exchanges, argued that the obvious solution was to raise the limit — to two megabytes, to eight, to thirty-two — and let the protocol scale by handling more transactions on-chain. The other faction, broadly aligned with the protocol's core developers and a network of node operators, argued that increasing the block size would centralize the network by making it economically impossible for ordinary users to run a full node, and that scaling should instead happen through cleverer protocol design that kept block sizes small.

The argument took three years to resolve and consumed the bitcoin community to a degree that is difficult to convey in retrospect. There were proposals — Bitcoin XT, Bitcoin Classic, Bitcoin Unlimited, SegWit, the New York Agreement — and there were factions and there were Twitter wars and there were forums full of accusations of conspiracy, betrayal, and bad faith. The Reddit forum r/bitcoin imposed an editorial policy against discussion of large-block proposals that critics characterized as censorship and that defenders characterized as legitimate moderation. A parallel forum, r/btc, was established and became the home of the large-block faction. The two communities, by 2017, were not on speaking terms.

The deadlock broke through a mechanism that had no precedent. In early 2017, an internet handle named Shaolinfry proposed BIP 148 — a coordinated user-activated soft fork (UASF) that would, on a fixed date, cause nodes to reject any block that did not signal support for SegWit. The proposal placed the burden of activation not on miners, who had been stalling, but on the network's full nodes. UASF caps and t-shirts circulated as a kind of insurgent uniform. By late July 2017, with BIP 148's August 1 deadline approaching, miners capitulated and signaled SegWit support. The Block Size Wars' resolution had been forced from below.

The resolution came in two phases. On August 1, 2017, the large-block faction executed what they had been threatening: a hard fork at block 478,558 creating a new chain called Bitcoin Cash, with an eight-megabyte block size. Twenty-three days later, on August 24, 2017, a soft-fork upgrade called Segregated Witness — *SegWit* — activated on the original bitcoin network at block 481,824. SegWit restructured how transaction data was organized to effectively increase block capacity without raising the formal one-megabyte limit. It had been authored primarily by Pieter Wuille, a long-tenured core developer, and shipped after a complex multi-year coordination effort. Roger Ver, an early bitcoin investor, became Bitcoin Cash's most prominent advocate. A second hard fork in November 2018 split Bitcoin Cash itself, creating Bitcoin SV. Subsequent splits produced a long tail of forks no one remembers.

The cultural meaning of the conflict, more than its technical specifics, is what mattered. The Block Size Wars established that bitcoin could not be unilaterally changed by the people who ran companies on top of it, by the developers who maintained the reference client, by exchanges, by miners, or by any combination of the above acting without the rough consent of the network's full nodes. The protocol turned out to be more conservative than any of its constituencies. The phrase *bitcoin is the chain you run* — meaning the chain whose rules you, individually, validate — became one of the war's lasting bequests. So did a habit of suspicion toward governance proposals, no matter how reasonable, that would have made the network easier to change.

The large-block forks have not prospered. Bitcoin Cash trades, as of 2025, at roughly one percent of bitcoin's price. Bitcoin SV trades at less. The original chain, the one that retained the one-megabyte limit and shipped SegWit, kept the name and the network effect. What the war established was that the name *bitcoin* refers, definitionally, to the protocol that does not change easily. Whether that property is a feature or a bug depends on what one wants the protocol for, and the war's veterans are, by and large, still arguing about it.
