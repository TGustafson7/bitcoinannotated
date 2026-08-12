---
title: "The Coldcard Hack"
deck: "The largest self-custody failure to date was not stolen keys but a build flag that quietly weakened how one device generated them."
era: "Now"
type: "Event"
date: 2026-07-30
blockHeightAtOrigin: 960267
heroImage: "/images/entries/the-coldcard-hack.png"
heroImageCaption: "Coinkite security advisory, July 30, 2026, disclosing the Coldcard seed-generation flaw."
heroImageCredit: "Coinkite"
sourcePlatform: "Coinkite Blog"
locked: false
related:
  - "be-your-own-bank"
  - "not-your-keys"
  - "dont-trust-verify"
  - "the-seed-phrase"
  - "the-mt-gox-collapse"
  - "the-ftx-collapse"
sources:
  - url: "https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/"
    label: "Coinkite, COLDCARD Security Advisory (Jul 30, 2026)"
    primary: true
  - url: "https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack"
    label: "TRM Labs, Inside the $116 Million Coldcard Hack"
  - url: "https://crypto.news/coldcard-hack-bitcoin-self-custody-entropy/"
    label: "crypto.news, How a build flag drained $116M in bitcoin"
---

For as long as bitcoin has had a culture, that culture has told people to hold their own keys. The catalog is full of the instruction: be your own bank, not your keys not your coins, don't trust, verify. What the phrases never specified was what happens when the tool you verify with is the thing that fails.

On July 30, 2026, Coinkite, the maker of the Coldcard hardware wallet, published a security advisory. Over the following six days, roughly 1,816 BTC, about $116 million, moved out of more than 5,200 addresses in four distinct waves. The first wave alone drained around 594 BTC from some 500 wallets in about twenty-five minutes. No device was touched. No seed phrase was phished. Nobody clicked anything.

The cause was a single build flag. In firmware 4.0.1, shipped in March 2021, a configuration macro that was meant to enable the device's hardware random number generator was left disabled, because Coinkite supplied its own. A supporting library checked whether the macro existed rather than whether it was switched on, concluded hardware randomness was unavailable, and fell back to a software generator seeded only from the chip's serial number and a timer. Seeds that were supposed to carry a hundred and twenty-eight bits of entropy carried perhaps forty on older devices and seventy-two on newer ones. Forty bits is roughly a trillion possibilities: few enough to be searched, off-device, by anyone willing to generate candidate seeds and check the resulting addresses against the public chain.

The flaw sat in open-source code for five years. Auditors, researchers, and the wider development community all had access to it; none of them found it. That is the part the community has found hardest to absorb. This was not the failure of self-custody as an idea. It was the failure of one company's firmware, discoverable by anyone, discovered by no one, for half a decade.

The register of the event was set by its victims. "Perhaps the hardest part about this is that I did everything right," said one, who lost more than eighteen bitcoin. Coinkite's guidance, that a seed made with fifty or more private dice rolls and a strong passphrase remained safe, drew the obvious retort from a rival wallet maker: you cannot ask ordinary people to roll dice to be secure. The advisory frames the problem through that dice-roll feature; independent researchers frame it through the build flag. They are the same failure seen from opposite ends.

The catalog keeps a shelf of custodial disasters: Mt. Gox, FTX, Bitfinex, each a lesson in what happens when someone else holds the keys. The Coldcard hack belongs beside them as the inverse case, the one where the user held the keys correctly and the tooling betrayed them anyway. The lesson is not that self-custody does not work. It is that self-custody moves the single point of failure from a custodian you must trust to a codebase you must verify, and almost nobody can verify a random number generator by looking at it.

The keys were never stolen. They were simply never as random as the people holding them believed.
