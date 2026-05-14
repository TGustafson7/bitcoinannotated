import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  trailingSlash: 'never',
  site: 'https://bitcoinannotated.com',
  integrations: [sitemap()],
});
