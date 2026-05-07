import { defineCollection, z } from 'astro:content';

const entries = defineCollection({
  type: 'content',
  schema: z.object({
    catalogId: z.string().optional(),         // e.g. "BTC.2010.002"
    title: z.string(),             // e.g. "The Pizza"
    pronunciation: z.string().optional(),
    deck: z.string(),              // italic subhead, ~1 sentence
    era: z.enum(['Pre-Genesis', 'Genesis', 'First Bull', 'Dark Forest', '2017 Run', 'The Long Wait', 'Pandemic Era', 'Frauds', 'Institutional Takeover', 'Now']),
    foundational: z.boolean().optional(),
    type: z.enum(["Phrase", "Event", "Iconography", "Document"]),
    date: z.date(),                // origin date
    blockHeightAtOrigin: z.union([z.number().int(), z.literal("Pre-chain")]).optional(),
    btcPriceAtOrigin: z.string().optional(),
    creator: z.string().optional(),
    sourcePlatform: z.string().optional(),
    locked: z.boolean().default(false),
    sources: z.array(z.object({
      url: z.string().url(),
      label: z.string(),
      primary: z.boolean().optional(),  // marks the source that *is* the artifact (vs. corroborating context). Annotated-edition logic.
    })).optional(),
    heroImage: z.string().optional(),
    heroImageCaption: z.string().optional(),
    heroImageCredit: z.string().optional(),
    related: z.array(z.string()).optional(),
  }),
});

export const collections = { entries };
