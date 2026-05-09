---
catalogId: "BTC.1997.001"
title: "Hashcash"
deck: "The proof-of-work primitive that bitcoin would, eleven years later, repurpose into a money."
era: "Pre-Genesis"
type: "Document"
date: 1997-03-28
blockHeightAtOrigin: "Pre-chain"
sourcePlatform: "cypherpunks mailing list"
creator: "Adam Back"
locked: true
heroImage: "/images/entries/hashcash.png"
heroImageCaption: "The original [ANNOUNCE] email to the cypherpunks mailing list, March 28, 1997."
heroImageCredit: "hashcash.org / Adam Back"
sources:
  - url: "http://www.hashcash.org/papers/announce.txt"
    label: "Original cypherpunks announcement (March 28, 1997)"
    primary: true
  - url: "http://www.hashcash.org/hashcash.pdf"
    label: "Adam Back — Hashcash: A Denial of Service Counter-Measure (2002)"
  - url: "https://bitcoin.org/bitcoin.pdf"
    label: "Bitcoin whitepaper, citing Hashcash as reference [6]"
related: []
---
On the morning of March 28, 1997, the roughly two thousand subscribers of the cypherpunks mailing list received an email from a twenty-six-year-old British postdoc named Adam Back. The subject line was *[ANNOUNCE] hash cash postage implementation*. The body described what Back called a partial hash collision based postage scheme — a way to require senders of email or users of anonymous remailers to burn a small, verifiable amount of computational work before their messages would be accepted. The work was costly to produce and trivial to check. The idea, Back wrote, was that partial hashes could be made arbitrarily expensive to compute and yet verified instantly.

The proposal was directed at a problem the early internet was just beginning to take seriously: spam. Cynthia Dwork and Moni Naor had sketched a related idea five years earlier in a paper called *Pricing via Processing or Combatting Junk Mail*, proposing that senders be required to perform some moderately hard cryptographic puzzle as a kind of postage. Back's contribution was a working implementation, built around the SHA-1 hash function, that could plausibly run on a 1997 personal computer. The system worked by requiring the sender to find an input whose hash began with a specified number of zero bits — a problem with no shortcut other than guessing. Twenty bits of zero meant, on average, about a million guesses. Twenty-five bits meant about thirty-two million. The number could be tuned to whatever level of friction the receiver wanted to impose.

The mailing list response was muted. A single subscriber wrote back with a technical question about the choice of hash function. Hashcash did not become the spam solution its author hoped for; the broader internet, when it eventually addressed spam at scale, did so through filtering and reputation systems rather than computational postage. Back published a more formal paper describing the system in August 2002, by which point the original proposal had been five years old and was, in any meaningful commercial sense, dormant.

It would have stayed dormant. What rescued Hashcash from the footnotes of cryptographic history was an unsigned email sent eleven and a half years later, on October 31, 2008, to a different mailing list. The author identified himself as Satoshi Nakamoto and attached a paper proposing an electronic cash system. Reference six in that paper's bibliography was Adam Back's 2002 Hashcash document. The proof-of-work mechanism Hashcash had originally been designed to throttle email — costly to produce, trivial to verify, with difficulty tunable by the verifier — was the same primitive Nakamoto had selected to secure transactions in a distributed ledger. Bitcoin's miners, in 2008 and ever after, would be running a slightly modified Hashcash.

Back has remained, in the years since, a careful and slightly bemused custodian of his role. He was one of the first two people Nakamoto emailed before publishing the whitepaper, contacted to confirm the correct citation. He has consistently denied being Nakamoto, despite recurring speculation. He went on to co-found Blockstream in 2014. The original 1997 announcement, with its terse compilation instructions and its remailer use cases, is preserved on his own website at hashcash.org, where it has lived continuously for nearly three decades. The artifact's modesty is part of what makes it foundational. Hashcash was not designed to underwrite a global monetary system. It was designed to slow down spammers. That it became something else is a story about what the cypherpunks built without meaning to.
