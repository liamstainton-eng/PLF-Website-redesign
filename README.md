# PLF Website redesign — frontend demo

Two responsive design demonstrations for the Paul Lavelle Foundation, using original PLF photography and its blue/yellow identity. Built with Astro and custom CSS. Content snapshot: 8 October 2026.

## Run locally

Requires Node.js 22.12 or newer.

```sh
npm ci
npm run dev
```

Run these commands inside the `plf-website-redesign` directory. Open either version:

- Demo 1: http://127.0.0.1:4321/
- Demo 2: http://127.0.0.1:4321/demo-2/
- Both on one page: http://127.0.0.1:4321/compare/

Demo 2 uses larger photographs, expressive typography, varied section layouts, activity tabs and an accessible photo viewer. Its content pages stay within `/demo-2/`; both versions link to a comparison page with independent interactive previews and desktop/mobile size controls. See [the Demo 2 design notes](docs/DEMO-2.md).

For a production preview:

```sh
npm run check
npm run build
npm run verify
npm run preview
```

## GitHub Pages preview

- Share Demo 2: https://liamstainton-eng.github.io/PLF-Website-redesign/demo-2/
- Compare both designs: https://liamstainton-eng.github.io/PLF-Website-redesign/compare/

The GitHub Actions workflow validates and publishes the static build when changes are pushed to `demo/second-design` or `main`. It sets `PLF_SITE_URL` and `PLF_BASE_PATH` for GitHub's project directory; local development keeps its existing root URLs. The deployment remains a labelled design preview and does not change PLF's live website. Source changes remain in the review pull request until the owner merges them.

To reproduce the hosted build in PowerShell:

```powershell
$env:PLF_SITE_URL = 'https://liamstainton-eng.github.io'
$env:PLF_BASE_PATH = '/PLF-Website-redesign/'
npm run build
npm run verify
npm run preview
```

Use the prefixed URL shown by the preview server. Clear those environment variables before returning to the usual local root URLs.

## Review journeys

- Home → Make a difference → existing JustGiving profile.
- Join us → running, cycling or swimming → guidance and organiser contact.
- Get support → self-referral information → existing PLF referral service.
- Events → searchable archive → explicitly closed historic event.
- Our work → education, For You Project, LGBTQ+ support and service information.
- Policies & resources → original documents and preview context.

Each demo represents all 75 captured PLF routes and adds five navigation pages. Together with the comparison page and shared 404 recovery page, the build contains 162 pages. Each version retains the 471 source paragraphs, often in expandable published-information sections. Shared contact/footer text is consolidated; the captured broken agency-referral page has a useful contact replacement. See docs/route-coverage.csv and docs/shared-contact-source.txt.

## Boundaries

This is a frontend preview, not a replacement for the live WordPress site. It has no payment processor, booking system, referral database, analytics or marketing tracking. Historic ticketing is closed. No confidential referral answers are collected. External links lead to existing services. Quick Exit opens Google UK and does not erase browser history.

Before a live release, PLF should confirm addresses, activity schedules and guidance, policy versions, testimonial permissions and the current referral journey. No invented donation impact amounts, live events or outcome counters are used.

## Provenance and maintenance

src/data/content.json holds preserved source content and links; src/data/site.ts holds curated summaries. docs/asset-provenance.json records original image URLs, local source names and hashes. Original image variants live in public/images. The local extraction script scripts/prepare_content.py expects the handover folder in the parent workspace; it is not needed to run or build this packaged demo.

The design takes information-hierarchy inspiration from the research and a few AstroWind patterns. Its MIT notice is retained in docs/AstroWind-LICENSE.md. PLF branding, photographs, documents and source text remain subject to their original rights; that MIT notice does not license PLF material.

Demo 2 hosts Manrope and Barlow Condensed locally through Fontsource. Their SIL Open Font License notices are retained in docs/Manrope-LICENSE.txt and docs/Barlow-Condensed-LICENSE.txt. No third-party font service is contacted by visitors.

Clone this repository and run the commands above. The obsolete source ZIP is removed from the working tree so the editable source can be reviewed directly. The safeguarding PDF retains its page content, with author/application metadata removed in the privacy cleanup.
