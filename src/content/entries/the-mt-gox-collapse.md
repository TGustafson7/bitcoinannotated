---
catalogId: "BTC.2014.002"
title: "The Mt. Gox Collapse"
deck: "850,000 bitcoin, gone."
era: "Dark Forest"
foundational: true
type: "Event"
date: 2014-02-24
blockHeightAtOrigin: 287515
creator: "Mark Karpelès / Mt. Gox"
sourcePlatform: "mtgox.com"
locked: true
heroImage: "/images/entries/mt-gox-2014.png"
heroImageCaption: "Mt. Gox's bankruptcy announcement, February 24, 2014."
heroImageCredit: "Mt. Gox Co., Ltd. / archived"
sources:
  - url: "https://www.mtgox.com/"
    label: "MtGox.com — bankruptcy trustee's official communications site (active since February 2014 collapse)"
    primary: true
  - url: "https://blog.wizsec.jp/2017/07/breaking-open-mtgox-1.html"
    label: "WizSec — Breaking open the Mt. Gox case"
related: []
---
On the morning of Monday, February 24, 2014, Mt. Gox went dark. The website returned a blank page. The Twitter account fell silent. Mark Karpelès, the chief executive officer of what was then still the largest bitcoin exchange in the world, posted a single statement to the homepage in Japanese and English announcing that the company was suspending all transactions. The reason given was vague: a bug in the bitcoin protocol called *transaction malleability* had, the statement implied, caused unspecified problems. Customers seeking to withdraw funds were referred to a future announcement that did not arrive on the schedule promised.

The actual situation, established four days later when the company filed for bankruptcy protection in a Tokyo court on February 28, was substantially worse than a protocol bug. Approximately 850,000 bitcoin — about 750,000 belonging to customers and 100,000 belonging to the exchange itself — were missing. At the prices then prevailing, the loss was on the order of $473 million. By the cryptocurrency-denominated accounting that subsequent developments would compel, the loss was much larger. The 850,000 bitcoin would, at bitcoin's all-time highs in the years that followed, be worth on the order of $90 billion — a change in denominator that the bankruptcy proceedings would, eventually, have to reckon with.

The forensic analysis, conducted over the following several years primarily by the Tokyo-based security firm WizSec, established that systematic theft from Mt. Gox's hot wallet had begun in late 2011 — within months of the public 2011 incident — and had continued, undetected and uncorrected, until early 2014. The 2023 indictment unsealed in the Southern District of New York attributed the long-running theft to two Russian nationals — Alexey Bilyuchenko and Aleksandr Verner — together with unnamed co-conspirators, who had obtained unauthorized access to a Mt. Gox server housing the exchange's wallet keys and had drained at least 647,000 of the missing bitcoin between 2011 and 2014. A substantial share of the stolen bitcoin was laundered through BTC-e, the exchange that Bilyuchenko ran together with Alexander Vinnik, until BTC-e was seized by United States law enforcement in 2017. Karpelès, in this telling, had not stolen the missing bitcoin. He had simply failed, for more than two years, to discover that they were being stolen, and the company's accounting infrastructure had been incapable of detecting the discrepancy. Karpelès was arrested by Japanese police in August 2015 on charges of falsifying records and personal embezzlement. He was acquitted of the embezzlement charges in March 2019 and given a suspended sentence on the records charge. He has, in subsequent years, written a book and given interviews. He has not run another exchange.

The bankruptcy proceedings have, in their patient way, become one of the longest-running creditor recovery efforts in cryptocurrency history. The trustee, Nobuaki Kobayashi, recovered approximately 200,000 bitcoin from a wallet that Karpelès had inadvertently preserved. Those recovered coins, which had appreciated dramatically during the proceedings, made the case unusual: by 2018, the bankruptcy estate's assets were worth more than the original creditor claims, denominated in dollars. Distributions to creditors began in 2024, ten years after the collapse, and continue. Most creditors, having waited a decade to recover their funds, will receive substantially more than they lost in dollar terms.

The cultural significance was that Mt. Gox provided, for the first time, the full version of the lesson that the 2011 incident had only sketched. *Not your keys, not your coins* was no longer a slogan. It was a documented case study with eleven hundred court filings and a sentencing in Tokyo District Court. The phrase, though it would not be widely associated with Andreas Antonopoulos for another two years, was taught in February 2014 by ten months of customer support emails that were never answered, by a CEO whose statements grew progressively more evasive, and by a quantity of bitcoin sufficient to fund a small national treasury, all of which had simply ceased, on a Tuesday in February, to be where it was supposed to be.
