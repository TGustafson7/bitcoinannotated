---
catalogId: "BTC.2016.004"
title: "Not Your Keys, Not Your Coins"
deck: "The phrase that became a discipline."
era: "The Long Wait"
type: "Phrase"
date: 2016-01-01
blockHeightAtOrigin: 391182
creator: "Andreas Antonopoulos (popularizer)"
sourcePlatform: "Conference circuit / Mastering Bitcoin"
locked: true
heroImage: "/images/entries/not-your-keys.svg"
heroImageCaption: "The phrase, popularized by Andreas Antonopoulos in August 2016."
heroImageCredit: "Specimen rendering"
sources:
  - url: "https://aantonop.com/"
    label: "Andreas Antonopoulos — official site (talks, books, transcripts)"
  - url: "https://github.com/bitcoinbook/bitcoinbook"
    label: "Mastering Bitcoin (Antonopoulos, 2014; second edition 2017)"
related: []
---
*Not your keys, not your coins.* The phrase has no single point of origin. It crystallized across Andreas Antonopoulos's prolific speaking and teaching activity in the period roughly between 2014 and 2016 — through Mastering Bitcoin (first edition published December 2014), through the Let's Talk Bitcoin podcast he co-hosted, through his teaching fellowship at the University of Nicosia's Digital Currencies program, and through dozens of conference talks and audience Q&A sessions delivered across multiple continents during those years. Antonopoulos was not the first person in the bitcoin community to articulate the underlying point — that a user storing bitcoin on a third-party exchange did not, in any meaningful cryptographic sense, own that bitcoin — but he was the figure most responsible for compressing the argument into a slogan that could be remembered, repeated, and printed on bumper stickers. The exact phrasing varied across his appearances. By 2016 the four-beat form *not your keys, not your coins* had stabilized as the canonical version, and by 2017 it was standard vocabulary across the bitcoin community.

The mechanics of the claim are simple. Bitcoin's security model rests on the cryptographic relationship between a private key — a 256-bit number — and the public addresses derived from it. Whoever knows the private key can authorize transactions that move the associated bitcoin. Whoever does not know the private key cannot. If a user stores their bitcoin on an exchange, the exchange holds the private keys; the user holds an entry in the exchange's database that says they are entitled to a certain quantity of bitcoin. The two are not equivalent. Database entries can be frozen, lost, contested in bankruptcy, garnished by court order, exposed to the exchange's other liabilities, deleted by an attacker who compromises the exchange's infrastructure, or — in the cases of Mt. Gox, Bitfinex, QuadrigaCX, Celsius, Voyager, and FTX — simply not paid out, because the exchange was either insolvent, fraudulent, or both. Bitcoin held under one's own private keys, by contrast, requires no counterparty's solvency. The phrase compresses this distinction into a four-beat instruction.

The cultural reception of the phrase has been substantially asymmetric across bitcoin's various constituencies. The maxi-aligned wing of the community has treated *not your keys, not your coins* as a bedrock principle, alongside the supply cap and the proof-of-work consensus mechanism. Hardware wallets, multi-signature schemes, and seed-phrase storage products have all been marketed against the slogan's underlying logic. Bitcoin podcasts end with it. Bitcoin conferences project it onto stage backdrops. New community members are taught the phrase in their first week. The exchange-aligned wing of the community — including Coinbase, Kraken, Gemini, and the various publicly traded companies whose business models depend on customers holding bitcoin in custodial accounts — has, predictably, been less enthusiastic, and has tended to argue that the phrase, however true in principle, overstates the practical risks for users with limited holdings or limited technical sophistication.

Each of the major exchange failures of the past decade has produced a fresh wave of *not your keys, not your coins* reaffirmation, accompanied by a measurable increase in withdrawals from custodial services. The pattern, by 2024, was sufficiently well-established that the bitcoin community could discuss it with a kind of weary recognition. *We told you*, the maxi-aligned response to the FTX collapse essentially ran. The phrase had been told. Approximately one million FTX customers had not internalized it in time. Several million customers across previous failures had also not internalized it. The slogan's effectiveness, as a piece of risk education, has been less complete than its proponents would prefer. Its accuracy, as a description of how bitcoin's security model actually works, has not been seriously contested.

The phrase's most lasting effect may be that it provided bitcoin with its first true moral instruction — a piece of advice the community could give that was both practical and ideological at the same time. *Hold your own keys* is technical guidance. *Not your keys, not your coins* is a worldview about whose responsibility it is when something goes wrong. Antonopoulos did not invent the underlying point. He gave it the form in which it could be remembered, repeated, and printed on bumper stickers, of which there are now several thousand. The phrase has become, in the bitcoin community's usage, less a slogan than a creed. Whether one obeys it remains, as in any creed, a separate question from whether one believes it.
