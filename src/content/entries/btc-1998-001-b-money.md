---
catalogId: "BTC.1998.001"
title: "b-money"
deck: "Wei Dai's 1998 sketch of an anonymous distributed cash system, ten years before bitcoin made it real."
era: "Pre-Genesis"
type: "Document"
date: 1998-11-01
sourcePlatform: "cypherpunks mailing list"
creator: "Wei Dai"
locked: true
heroImage: "/images/entries/b-money.png"
heroImageCaption: "The b-money proposal, preserved on Wei Dai's personal site weidai.com."
heroImageCredit: "weidai.com / Wei Dai"
sources:
  - url: "http://www.weidai.com/bmoney.txt"
    label: "Wei Dai — b-money (1998), full text on weidai.com"
    primary: true
  - url: "https://bitcoin.org/bitcoin.pdf"
    label: "Bitcoin whitepaper, citing b-money as reference [1]"
  - url: "https://bitcoinmagazine.com/technical/genesis-files-if-bitcoin-had-first-draft-wei-dais-b-money-was-it"
    label: "Bitcoin Magazine — The Genesis Files: Wei Dai's b-money"
related: []
---
In November 1998, a recent computer-science graduate of the University of Washington named Wei Dai posted a short essay to the cypherpunks mailing list. Its opening line was an admission of intellectual debt: *I am fascinated by Tim May's crypto-anarchy.* What followed was a description, in roughly two thousand words, of a protocol Dai called b-money. The proposal had two protocols, neither of which he expected anyone to actually implement. He published it anyway, and then largely walked away from the idea.

The first of Dai's two protocols required every participant to maintain a separate database recording how much money belonged to each pseudonym on the network. Money was created by broadcasting the solution to a previously unsolved computational problem; the number of monetary units credited was equal to the cost of the computation, denominated in a basket of standard commodities. Money was transferred by signed broadcast messages debiting one account and crediting another. Contracts were enforceable through a system of bonded reparations and arbitration. Dai acknowledged, in a single paragraph, that the protocol was impractical because it depended on a synchronous and unjammable broadcast channel that no actual network provided. The second protocol attempted to fix this by entrusting the account databases to a subset of participants called servers, who would post bonds and publish their ledgers periodically.

What is striking, reading the document a quarter-century later, is how many of bitcoin's eventual properties Dai had already articulated. Money created through verifiable computational work. Pseudonymous account holders identified only by public keys. Transactions executed through signed messages. A distributed set of bookkeepers required to remain honest by economic incentive. A specific concern that the bookkeepers, even in collusion, should be unable to inflate the supply. The pieces were on the table. What was missing — and Dai was the first to acknowledge it — was the mechanism by which a distributed network of mutually distrustful participants could agree on a single shared history of transactions without trusting anyone. b-money assumed the broadcast channel; bitcoin would, in 2008, replace that assumption with a chain of proofs of work and the longest-chain rule.

Dai did not stay with the design. *I didn't continue to work on the design because I had actually grown somewhat disillusioned with crypto-anarchy by the time I finished writing up b-money,* he later wrote on the rationality forum LessWrong. *I didn't foresee that a system like it, once implemented, could attract so much attention and use beyond a small group of hardcore Cypherpunks.* He went on to a career at Microsoft and TerraSciences, maintained the widely used Crypto++ cryptographic library, and gradually receded from public visibility. He is still active on rationality forums. He is among the small number of people who have been seriously proposed as candidates for being Satoshi Nakamoto, and has, like Adam Back, denied it.

The clearest evidence of b-money's standing is bibliographical. When Satoshi Nakamoto published the bitcoin whitepaper on October 31, 2008, the first reference in the paper — citation [1], placed before any other source — was Wei Dai's b-money. Hal Finney is reported to have suggested Nakamoto reach out to Dai before publication; Nakamoto did, asking Dai for the correct citation. Dai responded, suggested some changes, and never heard back. The paper went out as drafted. The original b-money document sits, untouched and undecorated, at weidai.com/bmoney.txt, exactly as it was posted in November 1998. It is short. It is unfinished. It was never implemented. It is the first reference in the document that became bitcoin.
