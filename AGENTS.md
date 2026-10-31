# Tolly's Cafe static website

## Structure and publication

- `docs/` is the publishable static site for GitHub Pages. Keep every required runtime file inside it. There is no framework, package installation, backend or server build.
- `docs/index.html` is the landing page; `docs/styles.css` holds its responsive styles; `docs/map.js` initialises the interactive map.
- `MENU.md` is the editable reference for menu items, descriptions, prices and dietary labels.
- `menu/template.html` is the menu page template. `menu/build_menu.py` converts the reference Markdown into `docs/menu.html` using Python's standard library (Python 3.10+).
- `ABOUT-TOLLYS.md` records cafe details, opening hours, contact links and the preferred OpenStreetMap location. Keep site content consistent with it when details change.
- `assets/` contains original supplied photos and logos. Web assets live in `docs/assets/`. Preserve originals and save edited assets separately. The hero uses `interior-enhanced.jpg`.

## Menu workflow

1. Edit `MENU.md` for content or `menu/template.html` for presentation. Change the converter only when its supported syntax or generation behaviour needs to change.
2. Run `python menu/build_menu.py` from the repository root. The script resolves paths relative to its own location, so it also works from another directory.
3. Review the generated `docs/menu.html`. Keep it in version control alongside source changes: GitHub Pages will not run the converter. Do not hand-edit generated HTML.
4. Preview with `host.bat`, then open `http://localhost:8000/menu.html`. The landing page is at `http://localhost:8000/`. Stop the server with Ctrl+C.

The converter supports headings, paragraphs, unordered lists, pipe tables, bold/italic text, inline links and two-space hard line breaks. It escapes raw HTML and rejects unsupported block syntax and malformed tables. Use UTF-8. Preserve blank prices; do not guess missing values. The generated page must retain the example menu notice that items, availability and prices are subject to change, plus the dietary key and allergen notice. Never infer dietary or allergen claims beyond the source.

## Content and design requirements

- Tolly's is already open for business. Do not reintroduce website-coming-soon notices.
- Display the address starting at **Tarlings Yard**, without unit numbers: Bishops Cleeve, Cheltenham, GL52 8RN, United Kingdom. It is just off Church Road.
- Opening hours are provisional for early November 2026, following Gwen's Cafe: Monday-Friday 8am-4pm, Saturday 9am-1pm, Sunday closed. Every opening hours/times reference should include **subject to change**. Do not imply these are confirmed permanent hours.
- Email: `hello@tollys.uk`. Facebook: `https://www.facebook.com/profile.php?id=61594570964511`. Instagram: `https://www.instagram.com/tollys.uk/`.
- Visitors follow social accounts and enable notifications there. There is no browser push service, mailing list or subscription backend.
- Preserve the warm cream, brown and olive branding, cafe photography, readable contrast, keyboard accessibility and phone layouts. Keep the pale hours footnote removed.
- Use relative site links (`menu.html`, `index.html#visit`, `assets/...`), avoiding root-relative paths that break GitHub Pages project sites.

## Map

The map uses Leaflet 1.9.4 from unpkg with integrity attributes, and OpenStreetMap tiles with visible attribution. Its labelled Tolly's marker is centred at `[51.947765, -2.060414]`, matching the preferred map link in `ABOUT-TOLLYS.md`. Keep map links, coordinates and documentation aligned when the owner changes the location. Preserve the centre button and resize/pageshow handling; avoid automatic popup panning that pushes the pin off-screen.

External map resources need an internet connection. Preview over HTTP using `host.bat`: `file://` can cause tile requests to be blocked because they lack a website referrer. Keep address/directions links usable if external map resources fail. GitHub Pages hosts the static HTML/CSS/JS; no API key is configured.

## Checks and handoff

After menu changes, run the converter and check that the output contains all menu sections, unchanged prices, the disclaimer and allergen notice, and no unresolved template placeholders. Confirm links/assets resolve inside `docs/` and JavaScript syntax when editing `map.js` (`node --check docs/map.js`). Review desktop/mobile layout when browser preview is available; report any visual verification limits. Do not commit, push or change hosting settings unless requested. Ensure generated output is present for the user's commit.
