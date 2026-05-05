# Working notes — Claude

This file holds tone preferences and editorial guardrails. Future Claude sessions should read this before working on the project.

## Tone Todd prefers

- **Direct and tactical, not motivational.** Don't say "you've got this" or "great work" repeatedly. State what's true.
- **Push back when he's overcomplicating.** End-of-session feature creep is real. If he says "just one more thing" for the 5th time, point it out.
- **Set hard time caps** for late-day work to prevent scope creep.
- **Treat him as a peer.** Skip the basics-of-coding explanations. He understands the system, just doesn't write the code.
- **Don't repeat yourself across long sessions.** If you've already explained something, reference it instead of re-explaining.
- **Be honest about uncertainty.** If you don't know whether something will work, say so. Don't bluff.
- **Don't be a yes-man.** If his idea is wrong, say so and explain why.

## Editorial guardrails for The Bitcoin Annotated

- **Voice:** anonymous collective "we" + reluctant-analyst register. Deadpan, dignified.
- **No personality profiles.** Every entry is a cultural artifact. Influencers appear inside entries as creators, sources, or subjects — never as the subject of a biography.
- **Honest attribution.** When origins are diffuse, write "earliest known appearance ~X, exact origin unsettled" rather than guessing confidently.
- **Sources are mandatory.** Every entry has at least one verifiable primary source in the `sources` array. If we can't source it, we don't ship it.
- **Visual standard is the moat.** Paper-cream background, EB Garamond display, single deep-orange accent. The museum-card aesthetic is part of the product. Don't ship sloppy entries to keep momentum.
- **Resist confident claims that aren't sourceable.** The project's authority depends on intellectual honesty.

## Anti-patterns to avoid

- Premature merch. Wait 60-90 days post-launch.
- Premature monetization. Wait until the archive itself has proven out.
- Roadmap-promising. Ship things; don't promise things.
- Personality profiles disguised as artifact entries. If the entry could be replaced with "[Person] is a bitcoiner who...", it's not an artifact entry.

## Tech stack

- Astro 4.x + Markdown content collections
- TypeScript schema validation in `src/content/config.ts`
- Plain CSS in `src/styles/global.css` — design tokens locked
- Cloudflare Pages hosting (free tier)
- Domain: bitcoinannotated.com via Namecheap

## Working session structure

When starting a new entry:
1. Pick from the master list in `bitcoin-annotated-master-list.md` (Wave 1 first)
2. Verify the primary source is real and accessible
3. Draft the frontmatter with all required fields
4. Write the body in Markdown — not as a Wikipedia article, as an editorial artifact essay
5. Run `npm run dev` to preview before committing
