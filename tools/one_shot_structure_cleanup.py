from pathlib import Path
import re

idx = Path('index.html')
html = idx.read_text(encoding='utf-8')

# Extract all style blocks in current cascade order into one stylesheet.
blocks = re.findall(r'<style(?:\s+[^>]*)?>(.*?)</style>', html, flags=re.S|re.I)
if not blocks:
    raise SystemExit('ABORT: no style blocks found')
css = '\n\n'.join(b.strip() for b in blocks if b.strip())
css += r'''

/* canonical final overrides — keep author identity visible and mobile-safe */
.author-intro{display:flex!important;align-items:center!important;gap:14px!important}
.author-intro img{display:block!important;width:64px!important;height:64px!important;flex:0 0 64px!important;border-radius:50%!important;object-fit:cover!important;border:2px solid #d3bd95!important}
@media(max-width:700px){.author-intro img{width:54px!important;height:54px!important;flex-basis:54px!important}}
'''

# Replace all embedded style blocks with one external stylesheet link.
html = re.sub(r'<style(?:\s+[^>]*)?>.*?</style>\s*', '', html, flags=re.S|re.I)
if 'href="styles.css"' not in html:
    html = html.replace('</head>', '<link rel="stylesheet" href="styles.css">\n</head>', 1)

# Restore the author portrait in the intro using the canonical historical source.
old = '<div class="author-intro"><div><strong>שלום לכולם,</strong></div></div>'
new = '<div class="author-intro"><img src="https://jerusalem2.vercel.app/media/team/yaniv.jpg" alt="יניב רז" width="64" height="64"><div><strong>שלום לכולם,</strong></div></div>'
if old in html:
    html = html.replace(old, new, 1)
elif 'class="author-intro"' in html and 'yaniv.jpg' not in html:
    raise SystemExit('ABORT: author-intro shape changed; manual review required')

# Remove presentation-only inline footer style; stylesheet owns layout.
html = html.replace(' class="weekly-footer" style="margin-top:45px;border-top:1px solid #c6d9ea;padding-top:15px;font-size:14px"', ' class="weekly-footer"')

# Safety checks.
assert '<section id="courses">' in html
assert 'class="training-table"' in html
assert 'id="green-page"' in html
assert 'id="teaching"' in html
assert 'styles.css' in html
assert '<style' not in html.lower()
assert 'yaniv.jpg' in html

Path('styles.css').write_text(css+'\n', encoding='utf-8')
idx.write_text(html, encoding='utf-8')
print('style_blocks_extracted=', len(blocks))
print('index_bytes=', len(html.encode('utf-8')))
print('css_bytes=', len(css.encode('utf-8')))
