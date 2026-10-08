# PLF frontend demonstration: implementation plan

Prepared 8 October 2026. Status: proposed for user review; frontend implementation has not started.

Repository: https://github.com/liamstainton-eng/PLF-Website-redesign (private).

## 1. Outcome and design direction

Build a polished, navigable demonstration of the Paul Lavelle Foundation website. The primary journey is giving; the secondary journey is joining in-person events and community activities. Support, referrals and Quick Exit remain independently accessible.

Minimalism means removing visual competition, repetition and unnecessary steps while preserving substantive information. Use PLF's existing blue/yellow identity, its original logo and authentic photographs. White or warm off-white backgrounds, dark-blue headings, restrained yellow actions, generous spacing and readable typography will give the site a calm, welcoming character. Avoid stock template imagery, fabricated counters, decorative motion, carousels and unnecessary card grids. The consulting deck's green is not the proposed website palette.

Use one consistent visual system: two button hierarchies, a restrained spacing scale, a readable content width, accessible contrast and simple image/text sections. Body text should be at least 16px, preferably 18px in reading sections. Make important actions visibly distinct without placing text over people's faces. Mobile layouts are designed deliberately rather than obtained by shrinking the desktop view.

## 2. Frontend foundation

Create an isolated project in `plf-website-redesign/` after this plan is accepted. Use Astro, TypeScript and a small shared style system for a static, content-led demo. Adapt selected AstroWind layout/image patterns; borrow ScrewFast's image/text spacing where useful. Retain licence notices for any reused source. Avoid copying the entire marketing template or combining several frameworks.

React and shadcn/ui are optional references rather than mandatory dependencies. Use native links, buttons, details/summary and form controls where they meet the need. Check the copied AstroWind project's instructions and applicable component skills before reusing its implementation. Resolve compatible package versions from the actual installed/copied project at build time and commit the lockfile.

Keep route content, activities, event metadata, image selection and external destinations in typed data files, separate from layout components. Separate the demonstrator from the live WordPress website; the demo does not decide a CMS migration. Exclude raw crawl archives, all third-party repository copies, deck build files and the full image archive from the application repository.

## 3. Pages and navigation

The first visual milestone is the homepage. The completed demonstration includes all principal journeys and supporting information needed to review the design:

| Page or template | Required content and behaviour |
| --- | --- |
| Homepage | Compact header, concise mission, original community image, Donate and Join actions, short explanation of the work, giving purpose, current event availability, activities, Paul's story, contact/policy footer |
| Donate | What gifts support; charity identity; clearly labelled JustGiving handoff; supported frequency/amount choices only if verified; fundraising pack and fundraising information |
| Events listing | Upcoming/past separation; an honest empty state based on the supplied audit; archive entries with dates; activities remain reachable |
| Event detail | Title, status, date/time, location, cost, suitability, arrival instructions, organiser contact, original matching poster and a descriptive provider link where appropriate |
| Community activities | Running, cycling and swimming; original photographs; distinct ability and equipment information; joining instructions, safety guidance and disclaimer access |
| Our work / service detail | Frontline support, healthy relationship education, LGBTQ+ support, For You Project, spaces/hubs and relevant app/information resources |
| Get support | Clear contact options, self-referral and professional referral entry points, service information and persistent Quick Exit; no fundraising prompts in screening journeys |
| Paul's story / news / historic content | Preserve the memorial narrative and substantive captured articles; reusable reading layouts with original dates and contextual photographs |
| Contact and resources | Distinguish support from general enquiries; hub/appointment context; policies, privacy, cookies, fundraising and activity downloads |
| Not found / unresolved route | Useful recovery navigation and a clear state; never silently present the broken agency-referral route as a functioning submission service |

Top-level navigation stays concise: Our work, Join us, Our story, Get support and Donate. Join us exposes events and activities. Contact, news, app resources and policies remain findable through relevant pages and the footer. Quick Exit is persistently visible and keyboard reachable on desktop and mobile.

Preserve source routes where practical. Keep every captured historic event/article address mapped to its corresponding content or explicitly documented destination. Repeated archive/filter views may share a template. Do not redirect every old URL to the homepage.

## 4. Preserve detail through a content ledger

Before coding page content, use `research/demo-route-coverage.csv` to account for all 75 captured internal URLs and the two external donation screens. It is an implementation ledger, not proof the pages have already been migrated.

For each unique content item, record its source URL, proposed route, substantive copy, contact/eligibility facts, documents, image provenance and review status. Remove duplicated navigation, cookie banners and repeated site chrome from body copy, but preserve the source extraction unchanged. Every item must be classified as represented locally, a deliberate external destination, an archive view, or an unresolved issue requiring confirmation.

Do not simplify away important distinctions:

- The foundation supports male victims/survivors, provides education and runs wider community activities; activity participation must not be described as male-only
- Keep LGBTQ+ support and the For You Project reachable; preserve the project's stated audience and age information from the source
- Cycling specifically requires experience of rides of 20+ miles; running describes three ability groups
- Preserve Paul's history and the distinction between historic activity photos and forthcoming events
- Keep the app, fundraising pack, policies and activity guidance accessible
- Preserve required referral screening information in the coverage ledger; the demo does not recreate a working sensitive-data form
- Retain document versions and provenance; do not silently rewrite safeguarding or legal material

Resolve conflicting address references with the charity before production. The demo should distinguish captured content from approved current information in review documentation and avoid displaying an unverified address as a confirmed appointment destination. Published policy placeholders, review dates and activity disclaimer wording belong in an explicit review list.

## 5. Image plan

Keep the existing 538-file preservation library intact. Select the best relevant originals using `research/photo-candidates.json` and the image manifest; copy only chosen files into the frontend project.

| Placement | Original candidate |
| --- | --- |
| Homepage community hero | PLF LEJOG team at Claire House; consider a split layout and preserve group faces and the photo's context |
| Cycling | Cycling-club-pic original |
| Swimming | Open-swimming-pic original |
| Running | running-club original |
| Paul's story | PLF-Home_0009_IMG10 portrait, in the memorial context |
| Support locations | Existing room/hub photographs with verified context |
| Historic event | The original poster and photos belonging to that event |

Inspect selected files at full size. Generate responsive WebP/AVIF variants where supported, with suitable fallbacks. Reserve dimensions, eagerly load the hero and lazy-load supporting imagery. Create desktop and mobile crops that keep faces visible. Write context-specific alt text. Record original URLs, hashes, captions and any editorial approval needed. Never imply that pictured community members are support clients.

## 6. Demo interaction boundaries

Navigation, mobile menus, archive controls and internal page links should work. Optional event sharing and calendar downloads can work only from complete, accurate event data; calendar download is not booking confirmation. A historic event is labelled past and does not offer an active booking action.

Donation entry can link to the captured JustGiving charity profile, clearly labelled as the existing external destination. Replace it with an approved direct hosted checkout only after verification. Do not invent checkout URLs, fee claims, gift impact amounts or a payment-success screen. If choices cannot be passed to the provider, place selection in its own checkout rather than losing a choice made on PLF.

The supplied audit has no confirmed upcoming events as of 8 October 2026. Use that dated content snapshot until current organiser information is supplied; do not fabricate an event schedule. Demonstrate an actual historic detail page, visibly marked as past. Put cancelled/postponed/sold-out component states in a separate review fixture if needed, not into public-looking event records.

The support entry should provide source-backed information and genuine existing destinations. Self-referral stays an explicit external handoff to the current service rather than collecting demo answers. The broken agency-referral route gets a useful explanation and confirmed general contact alternative, without implying a referral has been submitted. Keep all sensitive screening, marketing subscriptions, registration handling and payment processing out of the local frontend.

Quick Exit uses the observed Google UK destination. Implement an immediate keyboard-accessible exit in the demo and document that it does not clear history. The full production implementation still needs inspection before a live replacement.

Use a discreet, consistent demo indicator; keep technical implementation notes in the review documentation. No public deployment or live-site change is included in this phase.

## 7. Implementation sequence

1. **Content and assets:** complete the route/content ledger, define typed content records, select originals and document unresolved facts
2. **Design foundation:** build the shared page shell, responsive header/footer, Quick Exit, typography, colour/spacing tokens and image handling
3. **Homepage milestone:** implement the full homepage; inspect desktop and mobile composition before applying the system to remaining pages
4. **Principal journeys:** build giving, event list/detail, community activities and support entry, including truthful empty and past states
5. **Supporting detail:** migrate service information, Paul's story, relevant news/history, contact, resources and source-route mappings through reusable templates
6. **Review and delivery:** run the build/type checks, route/content checks and browser reviews; repair issues; provide a local preview, screenshots and an implementation handover

## 8. Acceptance checks

- Build and type checks pass; no broken internal links, missing selected images, console errors or accidental horizontal overflow
- Every captured internal URL has an explicit ledger disposition; all unique substantive content and documents are accounted for
- A donor reaches giving from any public template; provider destination and prototype limitations are clear
- A social visitor can understand an event without first visiting the homepage; past events cannot appear open for booking
- Community ability requirements, referral options and contact distinctions remain intact
- Get support and Quick Exit work from every page, including mobile navigation; keyboard focus is visible and the menu handles focus predictably
- Review at representative mobile, tablet and desktop widths, with keyboard navigation, 200% zoom and reduced-motion settings
- Check colour contrast, meaningful headings, labels, link names, alt text, readable text and touch targets
- Images use appropriate sizes and reserved space; confirm the hero is prioritised and supporting images do not shift the layout
- No form submission, payment, ticket purchase, marketing opt-in or fabricated completion occurs during testing
- Record unresolved provider, address, event and policy questions for production rather than hiding them behind a finished-looking interface

## 9. Deliverables

An editable frontend project with selected original PLF assets, a lockfile and run instructions; a working local preview; desktop/mobile screenshots of principal pages; route/content coverage and asset provenance records; retained third-party licence notices; and a concise review of what is functional and what needs live configuration.

The project will be versioned in the private GitHub repository. Initial repository creation is complete; frontend files, deployment and production integrations wait for acceptance of this plan. The existing audit, research, deck and original archives stay intact outside the application project.

## 10. Research basis

- `PLF Website Redesign Handover/CODEX-REDESIGN-HANDOVER.md`
- `research/REDESIGN-RESEARCH.md`, `research/repository-sources.json` and `research/photo-candidates.json`
- `PLF Website Redesign Handover/site-extraction.json`, `page-content.md`, image manifests and linked document extracts
- Charity: water for giving hierarchy, Refuge for distinct support access, BHF for event essentials and Movember for authentic community presentation
- AstroWind, ScrewFast and shadcn/ui source inspection; code licences retained, without assuming their assets or reported quality automatically transfer to PLF

These references inform design decisions. No conversion or attendance uplift has been measured or promised.
