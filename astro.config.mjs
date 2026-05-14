import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkParagraphAnchors from './src/lib/remark-paragraph-anchors.mjs';

export default defineConfig({
  trailingSlash: 'always',
  site: 'https://bitcoinannotated.com',
  integrations: [sitemap()],
  markdown: {
    remarkPlugins: [remarkParagraphAnchors],
  },
});
