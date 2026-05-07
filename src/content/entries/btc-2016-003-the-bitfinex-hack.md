---
catalogId: "BTC.2016.003"
title: "The Bitfinex Hack"
deck: "119,756 bitcoin stolen, recovered six years later by a tax investigator."
era: "The Long Wait"
foundational: true
type: "Event"
date: 2016-08-02
blockHeightAtOrigin: 423300
creator: "Bitfinex (the exchange) / Ilya Lichtenstein and Heather Morgan (the hackers)"
sourcePlatform: "Bitfinex.com"
locked: true
heroImage: "/images/entries/bitfinex.jpg"
heroImageCaption: "Heather Morgan and Ilya Lichtenstein, arrested February 2022."
heroImageCredit: "Department of Justice / contemporary press coverage"
sources:
  - url: "https://www.justice.gov/opa/pr/two-arrested-alleged-conspiracy-launder-45-billion-stolen-cryptocurrency"
    label: "DOJ — Two Arrested for Alleged Conspiracy to Launder $4.5 Billion in Stolen Cryptocurrency"
  - url: "https://blog.bitfinex.com/announcements/message-individual-responsible-bitfinex-security-incident-august-2-2016/"
    label: "Bitfinex — Message to the individual responsible for the August 2, 2016 security incident"
    primary: true
related: []
---
On the afternoon of August 2, 2016, a hacker compromised the security architecture of Bitfinex, then the largest dollar-denominated bitcoin exchange in the world, and withdrew 119,756 bitcoin from customer accounts to a wallet they controlled. The exchange's security model had relied on a third-party custody arrangement with a company called BitGo that required co-signatures on every withdrawal. The arrangement, which had been intended to make large-scale theft impossible, had been bypassed. The compromise's specific mechanism was never publicly explained, though subsequent court filings indicated that the hackers had obtained the cryptographic keys necessary to authorize withdrawals through a combination of social engineering, infrastructure exploitation, and what one DOJ filing described, with characteristic dryness, as *unauthorized access*. The total theft was worth approximately $72 million at the prices then prevailing. The 119,756 stolen bitcoin would be worth approximately $10 billion at the all-time high reached eight years later.

Bitfinex's response was unconventional and, in retrospect, structurally significant for bitcoin's later corporate adoption. Rather than declare bankruptcy, the exchange socialized the loss across all customer accounts — every depositor, regardless of whether their specific funds had been stolen, took a 36 percent haircut on their balance. In exchange for the haircut, customers received a token called *BFX*, which the exchange committed to redeem at a one-for-one rate against future profits. The improvisation was widely criticized at the time as a form of involuntary equity issuance dressed up as a token. It also worked. By April 2017, every BFX token had been redeemed. Customers who had held through the entire ordeal had been made whole, in dollar terms, eight months after the theft.

The investigation, conducted primarily by the United States Internal Revenue Service's criminal investigation division, took five and a half years. The stolen bitcoin sat in the hackers' wallet for years, occasionally moved through mixing services in small batches in apparent attempts to obscure the trail. On February 8, 2022, the Department of Justice arrested a married couple living in New York City: Ilya Lichtenstein, a thirty-four-year-old technology entrepreneur, and Heather Morgan, a thirty-one-year-old self-described *serial entrepreneur* who, in addition to her cryptocurrency activities, had cultivated a side career as a rap artist performing under the name *Razzlekhan*. The investigation had recovered approximately 94,000 of the original 119,756 bitcoin from wallets the couple controlled — at the time of the recovery, the largest financial seizure in the history of the United States Department of Justice. Lichtenstein and Morgan both pleaded guilty in August 2023. Lichtenstein was sentenced in November 2024 to five years; Morgan was sentenced the same month to eighteen months.

The cultural footprint of the hack and its resolution was, in its later phases, somewhat dominated by Razzlekhan's online persona, which combined ostentatious wealth, deliberately abrasive rap performances, and a documentary aesthetic that the bitcoin community received with the kind of fascinated incredulity that the early Silk Road headlines had produced a decade earlier. The Netflix documentary *Biggest Heist Ever* covered the case in 2024. The deeper significance, however, was monetary. By 2024, the recovered bitcoin had appreciated so substantially that the Bitfinex case became, like the Mt. Gox bankruptcy, a study in what happens when a fixed-supply asset is confiscated, frozen, or held in trust during a period of substantial price appreciation. The dollar-denominated value of the recovered bitcoin, at the time of the seizure, exceeded the dollar-denominated value of the original theft by a factor of approximately fifty. Bitfinex's customers, who had been made whole in 2017 in dollars, were not entitled to the appreciation. The United States government, having seized the assets, was.

The hack and its resolution have become the canonical example of two of bitcoin's more uncomfortable structural properties. The first is that on-chain forensics work, given enough time and patience, with great precision: the stolen bitcoin were traceable for six years across thousands of transactions, and most of them were eventually recovered. The second is that the asset's appreciation makes its custody and seizure a high-stakes business in ways that traditional financial assets, with their slower and less monetary trajectories, generally are not. *Not your keys, not your coins*, after Bitfinex, acquired a corollary the slogan's authors had not intended: not the government's keys, not the government's coins. Or, increasingly, the reverse.
