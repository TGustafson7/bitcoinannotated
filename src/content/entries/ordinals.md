---
catalogId: "BTC.2023.001"
title: "Ordinals"
deck: "JPEGs on bitcoin. The community is still arguing about whether to allow it."
era: "Now"
type: "Event"
date: 2023-01-21
blockHeightAtOrigin: 772887
creator: "Casey Rodarmor"
sourcePlatform: "Bitcoin protocol / ord client"
locked: true
heroImage: "/images/entries/ordinals.png"
heroImageCaption: "The first ordinal inscription. Casey Rodarmor, December 14, 2022, block 767,430."
heroImageCredit: "Casey Rodarmor / Ordinal Theory"
sources:
  - url: "https://docs.ordinals.com/"
    label: "Ordinal Theory documentation (Casey Rodarmor)"
    primary: true
  - url: "https://github.com/ordinals/ord"
    label: "ord — the reference Ordinals client on GitHub"
related: []
---
On December 14, 2022, an engineer named Casey Rodarmor inscribed an image of a small grey skull onto the bitcoin blockchain. The image was 793 bytes. It was embedded into the witness data of a single transaction in block 767,430. The Ordinals protocol's public mainnet launch followed on January 21, 2023, and the trickle of inscriptions became a flood within days. The technique that made the inscription possible — assigning sequential ordinal numbers to individual satoshis and using bitcoin's existing transaction infrastructure to attach arbitrary content to specific satoshis — had been documented by Rodarmor in a paper called *Ordinal Theory* published the previous month. The skull was the first non-financial artifact ever inscribed onto the bitcoin blockchain. By February 2023, there were tens of thousands of such inscriptions. By February 2024, there were tens of millions.

The technical mechanism that made Ordinals possible was, in a sense, latent in the protocol since 2021. The Taproot soft-fork upgrade, activated in November of that year, had restructured how transaction witness data was organized in ways that incidentally permitted significantly larger arbitrary data payloads than had previously been practical. Rodarmor's contribution was not to add a new capability to bitcoin but to recognize that an existing capability — designed and approved for other purposes — could also be used to embed images, audio files, executable code, and arbitrary text. The protocol had not been changed. The community's understanding of what the protocol could be used for had been.

The reception was, immediately and durably, divided. The supportive view — held primarily by users who saw bitcoin as a programmable platform and by miners whose fee revenue grew substantially as Ordinals demand pushed transaction fees up — was that Ordinals demonstrated the chain's flexibility, attracted new users and developers, increased the security budget through fee revenue, and were no different in principle from any other use of bitcoin's transaction layer. The opposing view — held primarily by the maxi-aligned wing of the community — was that Ordinals constituted *spam*, congested the chain with non-monetary use cases, displaced legitimate financial transactions, drove up costs for users who actually wanted to send bitcoin, and represented a fundamental confusion about what the protocol was for. Luke Dashjr, a long-tenured Bitcoin Core developer, attempted to advocate for protocol-level mitigations. The mitigations were not adopted. The Ordinals continued. The fee market remained transformed.

The cultural artifact that Ordinals produced is in some ways more interesting than the technical one. By the end of 2023, the bitcoin community had divided itself into roughly two camps on the question of whether Ordinals should exist at all. The division crossed previously stable factions: some longtime small-block advocates supported Ordinals because they generated fee revenue that secured the network; some maxi-aligned commentators opposed them because they considered the resulting blockchain bloat as ideologically corrosive as a block size increase. The argument was bitter, sustained, and occasionally personal in ways that recalled the Block Size Wars of 2015–2017. As of 2025, no resolution has been reached. Ordinals continue to be inscribed. Some users continue to oppose their existence. Both sides agree that the question of *what bitcoin is for* is now openly contested in a way it had not been for several years.

The deeper significance is that Ordinals demonstrated the limits of bitcoin's social consensus mechanisms when applied to use-case questions rather than protocol-rule questions. The Block Size Wars had been about whether to change the protocol. Ordinals are about whether to use the protocol in a particular way that the protocol does not prohibit. The community's tools for resolving the first kind of question — soft forks, hard forks, full-node validation, the slow accretion of running consensus — do not work cleanly on the second kind. There is no soft fork that can prevent Ordinals; preventing them would require a protocol change that the community is unable to coordinate. The result is a kind of standoff: the maxi faction continues to argue that Ordinals shouldn't exist, the Ordinals faction continues to inscribe them, and the chain processes both points of view with the same indifference it has always brought to its participants' opinions about it.
