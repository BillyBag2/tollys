"""Build the committed GitHub Pages menu: python menu/build_menu.py.

Uses only Python's standard library. Paths are relative to this script, so the
command also works from other directories. No server or browser JavaScript is
needed to read the generated menu. Run again whenever its sources change.
"""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'MENU.md'
TEMPLATE = ROOT / 'menu' / 'template.html'
OUTPUT = ROOT / 'docs' / 'menu.html'


def inline(text):
    """Escape HTML first, then render the inline Markdown used in MENU.md.

    Support strong/emphasised text and links. Raw HTML is displayed as text;
    links only accept HTTPS, HTTP, mailto, anchors and relative file paths.
    """
    text = escape(text, quote=True)

    def link(match):
        label, url = match.groups()
        if re.match(r'^[a-z][a-z0-9+.-]*:', url, re.I) and not url.lower().startswith(
            ('https:', 'http:', 'mailto:')
        ):
            raise ValueError('Unsupported link scheme in MENU.md')
        return f'<a href="{url}">{label}</a>'

    text = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)


def cells(line):
    """Split a Markdown table row, retaining blank cells (unknown prices)."""
    return [part.strip() for part in line.strip().strip('|').split('|')]


def separator(line):
    return line.strip().startswith('|') and all(
        re.fullmatch(r':?-{3,}:?', cell) for cell in cells(line)
    )


def render(markdown):
    """Convert headings, paragraphs, lists and tables into semantic HTML.

    This deliberately supports the Markdown subset in our reference menu,
    rather than depending on a third-party Markdown package. Malformed tables
    and unsupported block syntax fail the build instead of losing content.
    """
    lines = markdown.splitlines()
    output, navigation = [], []
    used_ids = set()
    title = None
    i = 0

    def heading(line):
        return re.fullmatch(r'(#{1,6})\s+(.+)', line)

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        match = heading(line)
        if match:
            level, label = len(match[1]), match[2]
            if level == 1:
                if title is not None:
                    raise ValueError('MENU.md must have exactly one main heading')
                title = label
            # The photo page numbers are useful in the reference file, but
            # web section headings read more naturally as Food / Drinks, etc.
            if level == 2:
                label = re.sub(r'^Page \d+:\s*', '', label)
            slug = re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-') or 'section'
            anchor, suffix = slug, 2
            while anchor in used_ids:
                anchor = f'{slug}-{suffix}'
                suffix += 1
            used_ids.add(anchor)
            output.append(f'<h{level} id="{anchor}">{inline(label)}</h{level}>')
            if level == 2:
                navigation.append(f'<a href="#{anchor}">{inline(label)}</a>')
            i += 1
            continue

        if line.strip().startswith('|'):
            if i + 1 >= len(lines) or not separator(lines[i + 1]):
                raise ValueError(f'Table missing separator at line {i + 1}')
            headers = cells(line)
            output.append('<div class="menu-table"><table><thead><tr>')
            output.extend(f'<th scope="col">{inline(h)}</th>' for h in headers)
            output.append('</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = cells(lines[i])
                if len(row) != len(headers):
                    raise ValueError(f'Table column count differs at line {i + 1}')
                output.append('<tr>')
                for column, value in enumerate(row):
                    # Row headings help screen readers relate each price to
                    # its item. Empty values stay empty; never invent a price.
                    tag = 'th scope="row"' if column == 0 else 'td'
                    end_tag = 'th' if column == 0 else 'td'
                    output.append(f'<{tag}>{inline(value)}</{end_tag}>')
                output.append('</tr>')
                i += 1
            output.append('</tbody></table></div>')
            continue

        if line.startswith('- '):
            output.append('<ul>')
            while i < len(lines) and lines[i].startswith('- '):
                output.append(f'<li>{inline(lines[i][2:])}</li>')
                i += 1
            output.append('</ul>')
            continue

        paragraph = []
        while i < len(lines) and lines[i].strip():
            line = lines[i]
            if heading(line) or line.startswith('- ') or line.strip().startswith('|'):
                break
            if re.match(r'^\s*(>|```|~~~|\d+\.\s|!\[|---\s*$)', line):
                raise ValueError(f'Unsupported Markdown block at line {i + 1}')
            # Two trailing spaces are a Markdown hard line break; all other
            # consecutive paragraph lines are joined with an ordinary space.
            paragraph.append(inline(line.rstrip()) + ('<br>' if line.endswith('  ') else ''))
            i += 1
        output.append('<p>' + ' '.join(paragraph) + '</p>')

    if title is None:
        raise ValueError('MENU.md needs a main heading')
    return title, '\n'.join(navigation), '\n'.join(output)


def main():
    # Complete rendering and validate template slots before writing anything,
    # leaving the previous published page intact if the source has an error.
    title, navigation, content = render(SOURCE.read_text(encoding='utf-8-sig'))
    page = TEMPLATE.read_text(encoding='utf-8')
    slots = {'{{TITLE}}': escape(title), '{{NAVIGATION}}': navigation, '{{CONTENT}}': content}
    for token in slots:
        if page.count(token) != 1:
            raise ValueError(f'Template must contain exactly one {token} slot')
    # Substitute in one pass so text from the menu is never treated as a slot.
    page = re.sub(r'\{\{(?:TITLE|NAVIGATION|CONTENT)\}\}', lambda m: slots[m[0]], page)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(page, encoding='utf-8', newline='\n')
    print(f'Generated {OUTPUT.relative_to(ROOT)} from MENU.md and menu/template.html')
    print('Include docs/menu.html in your commit so GitHub Pages serves the latest menu.')


if __name__ == '__main__':
    main()
