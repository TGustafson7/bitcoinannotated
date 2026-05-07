---
catalogId: "BTC.2011.002"
title: "The First Mt. Gox Hack"
deck: "The day a single account briefly bought 261,000 bitcoin for one cent each."
era: "First Bull"
foundational: true
type: "Event"
date: 2011-06-19
blockHeightAtOrigin: 131750
creator: "Mt. Gox / Mark Karpelès"
sourcePlatform: "mtgox.com"
locked: true
heroImage: "/images/entries/mt-gox-2011.png"
heroImageCaption: "The Mt. Gox price chart, June 19, 2011."
heroImageCredit: "Mt. Gox / contemporary screenshot"
sources:
  - url: "https://web.archive.org/web/20110625115413/https://mtgox.com/press_release_20110630.html"
    label: "Mt. Gox official statement on the June 2011 incident (archived)"
  - url: "https://blog.wizsec.jp/2015/04/the-missing-mtgox-bitcoins.html"
    label: "WizSec post-mortem analysis of Mt. Gox security failures"
related:
  - "BTC.2011.001"
  - "BTC.2010.002"
---

Mt. Gox began life in 2007 as a side project: a website where players of the collectible card game *Magic: The Gathering* could trade cards online. The name was an acronym — *Magic: The Gathering Online eXchange*. The card-trading site never amounted to much. In July 2010, its owner, an American programmer named Jed McCaleb, repurposed the dormant domain to launch a bitcoin exchange. Within nine months, the site was handling the majority of global bitcoin trading volume. In March 2011, McCaleb sold the operation to a French software developer living in Tokyo named Mark Karpelès. Three months later, on June 19, 2011, the wheels came off in public.

Trouble had been mounting for days. On June 13, Mt. Gox publicly disclosed that approximately 25,000 BTC had been stolen from 478 user accounts. Days later, the exchange's user database was leaked online. Karpelès initially downplayed the severity. Then, on the night of June 19 — three in the morning Tokyo time — an attacker accessed an administrator account that had been left active on a former auditor's computer. The attacker began executing trades. The largest single transaction observed was a sale of more than 260,000 bitcoin at one cent each. The price on Mt. Gox flash-crashed from \$17.50 to one penny in minutes.

The mechanics were unsubtle. The attacker was attempting to sell vast quantities of stolen bitcoin into the market and then withdraw the resulting cash. What saved the exchange from total drain was an account-level cap on daily withdrawals — set, almost incidentally, at one thousand dollars. The attacker successfully extracted approximately two thousand bitcoin before the cap throttled them. A separate user known only as *Kevin* purchased 259,684 bitcoin during the crash for roughly three thousand dollars but managed to withdraw only 643 of them before Karpelès suspended the site.

Karpelès rolled back the trades to their pre-crash state and took the exchange offline. It would not return to operation until August. Karpelès estimated the actual financial exposure at approximately two thousand bitcoin extracted before the cap held, a sum the exchange claimed it would absorb. Karpelès, in subsequent communications, described the situation as contained.

It was not contained. Subsequent forensic analysis by the security firm WizSec, conducted after the exchange's eventual collapse, would establish that systematic theft of customer bitcoin from Mt. Gox's hot wallet had begun in late 2011 and continued, undetected, for years. The June 2011 incident is best understood as the public version of a security culture that was already broken and would remain broken until the entire exchange went into bankruptcy in February 2014, with approximately 850,000 bitcoin missing.

The artifact endures because it was the first time bitcoin's central trade-off — *not your keys, not your coins* — was demonstrated at scale, in public, with real losses. Every subsequent exchange failure, from QuadrigaCX to FTX, has been a variation on the lesson Mt. Gox taught for the first time on a summer night in 2011: a custodian is a single point of failure, and the convenience of letting someone else hold your keys is exactly the cost of letting someone else lose them.
