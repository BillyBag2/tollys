# Tolly's Cafe website

The static site lives in `docs/`, ready for GitHub Pages. Run `host.bat` to preview at <http://localhost:8000>.

See: [ABOUT-TOLLYS.md](ABOUT-TOLLYS.md)

Edit [MENU.md](MENU.md), then run [new-menu.bat](new-menu.bat) (requires Python 3.10 or newer) to generate `docs/menu.html`. You can also run `python menu/build_menu.py` directly. Include the generated HTML in your commit so GitHub Pages publishes the updated example menu. The page template and instructions are in [menu/](menu/README.md).

See [AGENTS.md](AGENTS.md) for site structure, content requirements and maintenance instructions.
