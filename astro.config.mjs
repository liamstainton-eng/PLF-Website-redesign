import { defineConfig } from 'astro/config';
export default defineConfig({
  output: 'static',
  site: process.env.PLF_SITE_URL,
  base: process.env.PLF_BASE_PATH || '/',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
});
