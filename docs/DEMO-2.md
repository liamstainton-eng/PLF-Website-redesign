# Demo 2 — stronger photography and a more expressive PLF identity

The second design is available at `/demo-2/`. Demo 1 remains at `/` for direct comparison. This is a frontend proposal; the live PLF website has not been changed.

## Design direction

The first demo made the content easier to navigate but reduced the original site's personality. Demo 2 gives the PLF community more visual presence through larger original photographs, a blue-and-yellow hero, condensed display typography, and varied layouts rather than repeated cards. Manrope supports readable body text; Barlow Condensed gives key statements a distinct visual voice. Both fonts are hosted locally.

The homepage combines an immediate donation action and support access with three service cards, an interactive activity explorer, a giving section, an honest events empty state, Paul's story, a photo gallery and practical questions. It keeps the full published homepage information in an expandable section.

## Interaction and accessibility

- Sticky navigation keeps Get support, Donate and Quick Exit reachable. On mobile, the menu opens with a labelled button and closes with Escape or link selection.
- Activity tabs support click, Left/Right Arrow, Home and End, with matching tab/panel relationships. A non-script link still reaches the activity information.
- The photograph viewer uses a native modal dialog, labelled controls, previous/next arrows, Escape to close and focus return. The page does not scroll behind an open photograph.
- Hover feedback, intersection-based reveals and optional native cross-document view transitions add motion without requiring a framework runtime. Content is visible if JavaScript is unavailable, and reduced-motion preferences disable movement.
- An optional scroll progress indicator appears in browsers that support CSS scroll timelines. Unsupported browsers keep the same page content and navigation.
- Responsive composition handles small phones, tablets and desktop screens. The 320-pixel layout was checked for horizontal overflow.

## Content and journeys

Both versions use the same captured content through a shared page component. The 75 captured routes and all 471 source paragraphs remain present in each version; five additional navigation pages are also provided in each. Internal Demo 2 links keep visitors within the second version, except the explicit comparison link and shared document downloads.

Donation links lead to the existing provider handoff. There are no simulated payments or invented impact amounts. Events remain explicitly historic where applicable; no upcoming events have been invented. Support and referral information remains available without collecting private answers in this preview. Quick Exit opens Google UK and does not clear browser history.

Before launch, PLF still needs to confirm the conflicting addresses, activity information, policies, permissions and referral endpoints identified in the original handover.

## Review

Start with the homepage at `/demo-2/`, then try the activity tabs and photo viewer. Review `/demo-2/donate/`, `/demo-2/events/`, `/demo-2/get-support/`, `/demo-2/our-story/` and the original archive routes under the new prefix. Use Compare designs in either version to open `/compare/`, with both designs on one page and desktop/mobile preview controls.

Validation commands are `npm run check`, `npm run build` and `npm run verify`. The verifier checks both route sets, preserved source paragraphs, local links and assets, image attributes, headings, preview indexing controls, historic event status and the referral/provider boundaries.
