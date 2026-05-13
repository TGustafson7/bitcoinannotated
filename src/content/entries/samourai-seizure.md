---
title: "The Samourai Seizure"
deck: "The DOJ arrested two bitcoin developers for writing privacy software. The privacy-tools cluster collapsed in a day."
era: "Institutional Takeover"
type: "Event"
date: 2024-04-24
sourcePlatform: "DOJ / Southern District of New York"
heroImage: "/images/entries/samourai-seizure.png"
heroImageCaption: "Samourai Wallet seizure notice, April 24, 2024"
heroImageCredit: "U.S. Department of Justice"
locked: true
creator: "U.S. Department of Justice (action); Keonne Rodriguez and William Lonergan Hill (Samourai developers)"
blockHeightAtOrigin: 840588
foundational: false
related: []
sources:
  - url: "https://www.justice.gov/usao-sdny/pr/founders-and-ceo-cryptocurrency-mixing-service-arrested-and-charged-money-laundering"
    label: "DOJ Southern District of New York — press release (April 24, 2024)"
    primary: true
  - url: "https://bitcoinmagazine.com/politics/the-samourai-wallet-trial-a-test-of-financial-privacy-and-developer-freedoms"
    label: "Bitcoin Magazine — The Samourai Wallet Trial: A Test of Financial Privacy"
---

On the morning of April 24, 2024, the U.S. Attorney's Office for the Southern District of New York announced the arrests of Keonne Rodriguez and William Lonergan Hill, the two developers behind Samourai Wallet — a non-custodial bitcoin wallet whose CoinJoin-based privacy features had been operating since 2015. Rodriguez was thirty-five and based in the United States; Hill was sixty-five and based in Portugal. The charges were conspiracy to operate an unlicensed money-transmitting business and conspiracy to commit money laundering. The indictment alleged that Samourai had facilitated more than two billion dollars in transactions and that approximately one hundred million dollars of that volume was tied to criminal proceeds, primarily from darknet markets including Silk Road and Hydra Market.

By the end of that day, Samourai's website had been seized by U.S. authorities working with Iceland, where the servers were hosted. The Google Play Store had received a federal seizure warrant for the mobile application. The wallet, after nine years of continuous operation, was offline.

The legal theory was novel. Samourai was non-custodial software — it never held users' funds, it never custodied private keys, and FinCEN had previously stated, in 2019 guidance, that non-custodial wallet providers were not money services businesses subject to registration requirements. Prosecutors reportedly asked FinCEN, during the Samourai investigation, whether CoinJoin or non-custodial wallets qualified as money transmission. FinCEN's answer was no. The charges proceeded regardless.

This created what privacy advocates and civil-liberties groups described as a fair-notice problem of constitutional dimensions. Software developers had been told for years that writing non-custodial privacy software was legally distinct from operating a money services business; they had structured their projects around that distinction; and the DOJ had now adopted a contrary position without warning. The Cato Institute argued that the prosecution would have a chilling effect on cryptocurrency defenders, human rights activists, privacy defenders, and software developers. It did. Within weeks of the arrests, Wasabi Wallet announced it was blocking U.S. users. Phoenix Wallet, widely considered the best self-custodial Lightning wallet, withdrew from the U.S. market entirely. The privacy-tools cluster around bitcoin contracted sharply.

The case raised the question of code as speech, the doctrine established in Bernstein v. United States in the late 1990s — itself a case the catalog has covered in the PGP entry — that source code is protected expression under the First Amendment. The Samourai prosecution did not formally challenge that doctrine, but it functioned as a workaround: rather than prosecuting the code, the government prosecuted the operation around the code, treating the developers' continued maintenance and marketing of the software as the offense. Whether this distinction holds up under appeal remains undecided as of 2026.

In July 2025, after fifteen months of pretrial proceedings, Rodriguez and Hill changed their pleas. They pleaded guilty to conspiracy to operate an unlicensed money-transmitting business — the lesser of the two original charges — but not to money laundering. The plea deal allowed them to forfeit Samourai's $6.3 million in earned fees and accept prison terms substantially shorter than the maximum exposure. In November 2025, Rodriguez was sentenced to five years and Hill to four. Both were ordered to pay $250,000 fines and three years of supervised release. Rodriguez began his sentence at FPC Morgantown, a federal prison camp in West Virginia. In May 2026, writing from prison and with hopes for a presidential pardon faded, Rodriguez published an appeal to the bitcoin community asking for help with more than two million dollars in legal debt. The appeal raised approximately sixty-five thousand dollars in its first week.

The artifact is what the seizure means as a precedent rather than what happened to the two specific defendants, though the latter is real. The U.S. legal system has now established that writing and maintaining non-custodial privacy software for bitcoin is, under at least one prosecutorial theory, an unlicensed money-transmitting business. This is a precedent that will be cited in every subsequent privacy-tools case, including ongoing cases against the Tornado Cash developers. It is also a precedent that has not yet been tested at the appellate level for non-custodial bitcoin software specifically, and the eventual resolution will determine whether a substantial portion of bitcoin's original cypherpunk inheritance — the right to transact with privacy — survives in the United States.

The Samourai seizure is the moment at which the bitcoin privacy-tools community lost its first major battle to the U.S. government. The catalog records it without optimism about the next battle. Rodriguez wrote from prison in December 2025 that other bitcoin developers should be looking at what the government has done in his case and shoring up their defenses, because they would be the next targets. The catalog will not predict whether he is right.
