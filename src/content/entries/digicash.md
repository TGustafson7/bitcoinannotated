---
title: "DigiCash"
deck: "The first attempt at digital cash. Centralized, patented, bankrupt by 1998."
era: "Pre-Genesis"
type: "Document"
date: 1990-01-01
sourcePlatform: "Amsterdam — DigiCash Inc."
heroImage: "/images/entries/digicash.png"
heroImageCaption: "DigiCash webserver, c. 1996. Numbers that are money."
heroImageCredit: "DigiCash Inc., archived by the Internet Archive"
locked: true
catalogId: "btc-1990-001"
creator: "David Chaum"
blockHeightAtOrigin: "Pre-chain"
foundational: true
related: []
sources:
  - url: "https://nakamotoinstitute.org/library/blind-signatures/"
    label: "David Chaum — Blind Signatures for Untraceable Payments (1982)"
    primary: true
  - url: "https://en.wikipedia.org/wiki/DigiCash"
    label: "DigiCash — Wikipedia"
---

In 1982, while a graduate student at Berkeley, David Chaum published a short paper titled Blind Signatures for Untraceable Payments. The paper described a cryptographic protocol that allowed a party to sign a digital message without seeing its contents. From this primitive, Chaum argued, an entire system of anonymous digital cash could be constructed: users could withdraw money from a bank in the form of cryptographically blinded tokens, spend them anywhere, and have them redeemed by the bank later, with no way for the bank to link withdrawals to expenditures. The user would have privacy. The bank would have certainty. The math worked.

Chaum spent the next several years refining the idea, and in 1990 founded DigiCash in Amsterdam to commercialize it. The product, eventually called eCash, was an electronic payment system based on Chaums blind-signature scheme. The first live transaction was on May 27, 1994 — a small payment from a Dutch customer to a vendor, sent over the early internet. By the mid-1990s, DigiCash had pilot agreements with Mark Twain Bank in Missouri, Deutsche Bank in Germany, Credit Suisse in Switzerland, Bank Austria, and several others. Microsoft was reportedly in negotiations to integrate eCash into Windows 95. The technology was real. The privacy was genuine. The trials processed millions of low-value transactions across multiple countries.

It failed anyway. In November 1998, DigiCash filed for Chapter 11 bankruptcy. Chaum sold the remaining assets in 1999 and ended his involvement. The technology that had been demonstrated to work, that had attracted serious bank partnerships, that had a head start of nearly two decades on bitcoin — was over.

The reasons DigiCash failed are bitcoins design specification in negative. eCash required a trusted central issuer; the bank had to be online to validate every transaction, and if the bank went down, the system went down. Chaums patents on blind signatures were broad enough that no competitor could build a compatible system, so there was no second source — eCashs ecosystem was, by enforcement, only ever DigiCash. The architecture was merchant-centric: users transacted with merchants who had to initiate connections back to user IP addresses, which assumed an internet topology that did not survive the rise of NAT and home routers. Banks were skeptical of the privacy features, which they correctly identified as a regulatory liability. And the chicken-and-egg problem of any payment network was never solved: merchants would not accept eCash without users, and users had no reason to acquire eCash without merchants.

Each of these failure modes is something bitcoin reverses. Bitcoins issuance is decentralized — there is no single bank to fail. The reference implementation is open-source and unpatented; anyone can build a compatible client. Transactions are user-to-user, not user-to-merchant — the network does not assume any particular topology. The chicken-and-egg problem was solved by years of organic community formation around a system that worked even when no merchants accepted it, because the early holders were not users in the eCash sense; they were collectors and ideologues willing to hold a thing for its own properties. And the regulatory liability of strong privacy was, in bitcoins case, distributed across the entire network rather than concentrated in any single corporate entity that could be sued or regulated out of existence.

Chaum is sometimes described as the man whose company Satoshi finished. The framing is not quite right — bitcoin uses different cryptographic primitives, and Satoshis design borrows more directly from later work by Hashcash and the cypherpunk b-money proposals than from DigiCash specifically. But DigiCash is the canonical cautionary tale that the bitcoin design seems written against. Satoshi did not cite DigiCash in the whitepaper. The whitepaper does not need to. DigiCash is the absent example, the failed predecessor that made every architectural choice in bitcoin defensible.

Chaum is still alive, still working in cryptography, and has launched several projects since. None has approached the scale of what bitcoin became from the ashes of what he originally proposed.
