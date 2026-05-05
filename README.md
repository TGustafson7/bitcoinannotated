# The Bitcoin Annotated

An annotated archive of bitcoin's cultural artifacts.

## How this site works

Static site built with Astro. Each catalog entry is a Markdown file in `src/content/entries/`. The design system lives in `src/styles/global.css` and the page templates live in `src/layouts/`. Push to main → Cloudflare Pages auto-deploys.

## Adding a new entry

1. Create a new `.md` file in `src/content/entries/` named like `btc-2013-001-hodl.md`
2. Fill in the frontmatter (the YAML between `---` markers at the top)
3. Write the body in Markdown
4. `npm run dev` to preview locally at `http://localhost:4321`
5. `git add . && git commit -m "added [entry name]" && git push`
6. Site rebuilds and deploys automatically in ~30 seconds

## Frontmatter schema

```yaml
catalogId: "BTC.2013.001"      # required, format: BTC.YYYY.NNN
title: "HODL"                   # required
pronunciation: "/ˈhɒdəl/"       # optional, IPA or pronunciation guide
deck: "..."                     # required, italic subhead, ~1 sentence
era: "First Bull"               # required, see config.ts for valid values
status: "Foundational"          # required: Living | Dormant | Foundational
type: "Catchphrase"             # required, free-form
date: 2013-12-18                # required, origin date
btcPriceAtOrigin: "$522"        # optional
creator: "GameKyuubi"           # optional
sourcePlatform: "BitcoinTalk"   # optional
locked: true                    # optional, true = origin verified
sources:                        # optional but strongly encouraged
  - url: "..."
    label: "..."
related:                        # optional, catalog IDs of linked entries
  - "BTC.2010.002"
```

## File structure

```
bitcoin-annotated/
├── astro.config.mjs            # framework config
├── package.json                # dependencies
├── public/                     # static assets (images, etc.)
└── src/
    ├── content/
    │   ├── config.ts           # entry schema definition
    │   └── entries/            # one markdown file per entry
    │       ├── btc-2009-001-genesis-block.md
    │       ├── btc-2010-002-the-pizza.md
    │       └── btc-2013-001-hodl.md
    ├── layouts/
    │   ├── BaseLayout.astro    # shared topbar/nav
    │   └── EntryLayout.astro   # single-entry template
    ├── pages/
    │   ├── index.astro         # homepage / catalog
    │   └── entries/
    │       └── [...slug].astro # dynamic route for entries
    └── styles/
        └── global.css          # design system
```

## Local development

```bash
npm install
npm run dev          # starts local preview at http://localhost:4321
```

## Deployment

Connect the GitHub repo to Cloudflare Pages. Build command: `npm run build`. Output directory: `dist`. Push to main → live in ~30s.
