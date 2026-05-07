---
catalogId: "BTC.2005.001"
title: "Bit Gold"
deck: "Nick Szabo's 2005 sketch of a digital scarce resource — the third of bitcoin's three pre-bitcoin protocol ancestors."
era: "Pre-Genesis"
type: "Document"
date: 2005-12-29
blockHeightAtOrigin: "Pre-chain"
sourcePlatform: "Unenumerated blog"
creator: "Nick Szabo"
locked: true
heroImage: "/images/entries/bit-gold.png"
heroImageCaption: "The original Bit Gold post on Szabo's Unenumerated blog, published December 29, 2005."
heroImageCredit: "unenumerated.blogspot.com / Nick Szabo"
sources:
  - url: "https://unenumerated.blogspot.com/2005/12/bit-gold.html"
    label: "Nick Szabo — Bit Gold (Unenumerated, December 29, 2005)"
    primary: true
  - url: "https://nakamotoinstitute.org/library/bit-gold/"
    label: "Bit Gold, archived at the Satoshi Nakamoto Institute"
  - url: "https://en.wikipedia.org/wiki/Nick_Szabo"
    label: "Nick Szabo — Wikipedia, biographical and historical context"
related: []
---
On December 29, 2005, the cryptographer and legal scholar Nick Szabo published a long blog post titled simply *Bit Gold* on his personal site, Unenumerated. The opening line was a quiet announcement of a much older idea: *A long time ago I hit upon the idea of bit gold.* Szabo had been describing the concept privately since 1998, the same year Wei Dai had posted b-money to the cypherpunks list. The 2005 essay was the first time he set the design out in public, in detail, on a platform that would still be reachable two decades later.

Bit Gold's design rested on the same primitive that Hashcash and b-money had introduced — proof of work, the costly-to-produce, easy-to-verify computational puzzle. In Szabo's version, a participant would expend computing power to solve a cryptographic challenge whose difficulty was tunable. Each solution was timestamped through a Byzantine-fault-tolerant public registry, assigned to the solver's public key, and chained to become part of the next puzzle. The result was what Szabo called *unforgeable costliness* — a digital property that, like gold, derived its value from the physical effort required to produce it. He was, in his own words, trying to mimic as closely as possible in cyberspace the security and trust characteristics of gold, with the property that it didn't depend on a trusted central authority.

The design left a problem unsolved. Different generations of computing hardware would produce solutions at radically different costs; the value of any particular bit of bit gold would be unclear without some way to standardize its difficulty across time. Szabo proposed a market-based valuation layer — a cryptographic equivalent of a commodity exchange — to handle this. The proposal acknowledged its own incompleteness. Bit Gold solved the unforgeable scarcity problem and the chained-timestamping problem; it did not solve the consensus problem of how mutually distrustful participants would agree on a single ordered history of who owned what. That last piece would have to wait three more years.

The strange asymmetry of Bit Gold's place in the bitcoin record is bibliographical. The bitcoin whitepaper, published in October 2008, cites Hashcash and b-money explicitly. It does *not* cite Bit Gold. Satoshi Nakamoto would, however, write on the Bitcointalk forum in 2010 that *Bitcoin is an implementation of Wei Dai's b-money proposal and Nick Szabo's Bitgold proposal* — a retrospective acknowledgment that the design lineage was three-handed, not two. Some have read this as evidence that Nakamoto encountered Bit Gold only after the whitepaper went out. Others have read it as evidence that Nakamoto *was* Szabo, or at least had been close enough to his work that the omission was deliberate. The speculation has not abated. Szabo has consistently denied being Nakamoto. *I'm afraid you got it wrong doxing me as Satoshi,* he wrote in a 2014 email, *but I'm used to it.*

What Bit Gold contributed, more than any specific mechanism, was the metaphor. Szabo named the thing. The phrase *bit gold* was already imagining digital money as a scarce physical commodity at a time when most digital cash schemes were imagining it as a kind of electronic check. The framing — money as something that costs energy to produce, that exists because of thermodynamic effort, that derives its monetary properties from being expensive to make — would become bitcoin's own. Three years after Szabo posted the essay, an unsigned email arrived on a different mailing list announcing a working implementation of substantially the same idea. The Unenumerated post still sits where Szabo published it, comments and all, including one from a reader named Sebastian Schepis written months after bitcoin's launch: *One day, people will look upon this post as the actual genesis moment of Bitcoin.*
