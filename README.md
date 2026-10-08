# PLF Website redesign — frontend demo

A minimalist, responsive demonstration for the Paul Lavelle Foundation, using original PLF photography and its blue/yellow identity. Built with Astro and custom CSS. Content snapshot: 8 October 2026.

## Run locally

Requires Node.js 22.12 or newer.

```sh
npm ci
npm run dev
```

Open http://127.0.0.1:4321/. For a production preview:

```sh
npm run check
npm run build
npm run verify
npm run preview
```

## Review journeys

- Home → Make a difference → existing JustGiving profile.
- Join us → running, cycling or swimming → guidance and organiser contact.
- Get support → self-referral information → existing PLF referral service.
- Events → searchable archive → explicitly closed historic event.
- Our work → education, For You Project, LGBTQ+ support and service information.
- Policies & resources → original documents and preview context.

The demo represents all 75 captured PLF routes, adds five navigation pages and a 404 recovery page. 471 source paragraphs remain available, often in expandable published-information sections. Shared contact/footer text is consolidated; the captured broken agency-referral page has a useful contact replacement. See docs/route-coverage.csv and docs/shared-contact-source.txt.

## Boundaries

This is a frontend preview, not a replacement for the live WordPress site. It has no payment processor, booking system, referral database, analytics or marketing tracking. Historic ticketing is closed. No confidential referral answers are collected. External links lead to existing services. Quick Exit opens Google UK and does not erase browser history.

Before a live release, PLF should confirm addresses, activity schedules and guidance, policy versions, testimonial permissions and the current referral journey. No invented donation impact amounts, live events or outcome counters are used.

## Provenance and maintenance

src/data/content.json holds preserved source content and links; src/data/site.ts holds curated summaries. docs/asset-provenance.json records original image URLs, local source names and hashes. Original image variants live in public/images. The local extraction script scripts/prepare_content.py expects the handover folder in the parent workspace; it is not needed to run or build this packaged demo.

The design takes information-hierarchy inspiration from the research and a few AstroWind patterns. Its MIT notice is retained in docs/AstroWind-LICENSE.md. PLF branding, photographs, documents and source text remain subject to their original rights; that MIT notice does not license PLF material.

Clone this repository and run the commands above. The obsolete source ZIP is removed from the working tree so the editable source can be reviewed directly. The safeguarding PDF retains its page content, with author/application metadata removed in the privacy cleanup.
