import { defineCollection, z } from 'astro:content';
const entries = defineCollection({
  type: 'content',
  schema: z.object({
    catalogId: z.string().optional(),         // e.g. "BTC.2010.002"
    title: z.string(),             // e.g. "The Pizza"
    pronunciation: z.string().optional(),
    deck: z.string(),              // italic subhead, ~1 sentence
    era: z.enum(['Genesis', 'First Bull', 'Dark Forest', '2017 Run', 'The Long Wait', 'Pandemic Era', 'Institutional Entry', 'Frauds', 'Institutional Takeover', 'Now']),
    status: z.enum(['Living', 'Dormant', 'Foundational']),
    type: z.string(),              // "Catchphrase", "Iconography", "Event", etc.
    date: z.date(),                // origin date
    btcPriceAtOrigin: z.string().optional(),  // e.g. "$0.0041"
    creator: z.string().optional(),
    sourcePlatform: z.string().optional(),
    locked: z.boolean().default(false),
    sources: z.array(z.object({
      url: z.string().url(),
      label: z.string(),
    })).optional(),
    heroImage: z.string().optional(),         // e.g. "/images/entries/genesis-block.jpg"
    heroImageCaption: z.string().optional(),  // figcaption text
    heroImageCredit: z.string().optional(),   // attribution line
    related: z.array(z.string()).optional(),  // catalog IDs of related entries
  }),
});
export const collections = { entries };