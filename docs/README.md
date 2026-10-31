# Tolly’s Cafe landing page

Static website: open `index.html` in a browser, or serve this directory with a static web server. No build or dependencies are required. The directory is ready to use as the `/docs` source for GitHub Pages; deployment is not configured by this change.

The example menu is at `menu.html`, generated from `../MENU.md` and `../menu/template.html`. After editing either source, run `python menu/build_menu.py` from the repository root and include `docs/menu.html` in your commit. GitHub Pages serves the generated page directly. See `../menu/README.md` for details. Use `../host.bat` to preview over HTTP.

Update provisional hours in `index.html` when confirmed. Early November 2026 hours follow Gwen’s Cafe: Monday–Friday 8am–4pm, Saturday 9am–1pm, Sunday closed. Source: [Blacks Brokers, 12 June 2026](https://www.blacksbrokers.com/featured-listing-gwens-cafe-2/), checked 31 October 2026. These are not independently confirmed final Tolly’s hours.

Facebook and Instagram links let visitors follow updates and enable notifications on those platforms. This page does not collect subscriptions or send browser push notifications.

Images come from the supplied `../assets` files, with responsive crops and subtle CSS colour adjustments. `interior-enhanced.jpg` is an AI edited version of `../assets/inside.jpg` with improved exposure, warmth and sharpness. Keep originals in `../assets`. The interactive map uses Leaflet 1.9.4 from unpkg and OpenStreetMap tiles, so it needs an internet connection. A fixed Tarlings Yard location (51.947765, -2.060414) keeps the custom Tolly's marker centred on load and resize. Coordinates follow the updated OpenStreetMap link in `../ABOUT-TOLLYS.md`: https://www.openstreetmap.org/#map=18/51.947765/-2.060414. The address and location links remain available if the map cannot load.
