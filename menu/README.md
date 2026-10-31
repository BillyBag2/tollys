# Static example menu

Edit `../MENU.md` for content and `template.html` for layout, then run from the repository root:

```powershell
python menu/build_menu.py
```

The script uses Python 3.10+ and only the standard library. It writes `../docs/menu.html`, which **must be committed** along with the source changes. GitHub Pages serves this generated HTML directly; it does not run the Python script. No build dependencies, API keys or client JavaScript are needed for the menu.

The template shares `../docs/styles.css` and `../docs/assets/logo.jpg` with the landing page. Its menu styles are inline so the generated page needs no extra stylesheet. All local links are relative and work beneath a GitHub Pages repository path.

Supported Markdown: headings, paragraphs, two-space hard line breaks, unordered lists, pipe tables, bold, italics and inline links. Unsupported block syntax and malformed tables raise an error. Raw HTML is escaped. Keep the example menu disclaimer and dietary/allergen information. Missing prices stay blank.

Run `../host.bat` and visit <http://localhost:8000/menu.html> to preview. Regenerate after changing the Markdown, template or converter. Do not edit `docs/menu.html` directly: the next build replaces it. The output is deterministic, with no build timestamps.
