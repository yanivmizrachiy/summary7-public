from pathlib import Path
import re

path = Path('index.html')
html = path.read_text(encoding='utf-8')
original = html

# 1) Remove malformed nested opening <style> that appears inside a style block
# before the contrast-safety section. Keep the actual CSS content.
html = html.replace('\n<style>\n/* Contrast safety: explicit opaque backgrounds and text colors across screen/print. */', '\n/* Contrast safety: explicit opaque backgrounds and text colors across screen/print. */')

# 2) Keep only the LAST premium-v4 block; earlier copy is redundant legacy output.
blocks = list(re.finditer(r'<style id="summary7-premium-v4">.*?</style>', html, flags=re.S))
if len(blocks) > 1:
    keep = blocks[-1]
    pieces = []
    pos = 0
    for m in blocks[:-1]:
        pieces.append(html[pos:m.start()])
        pos = m.end()
    pieces.append(html[pos:])
    html = ''.join(pieces)

# 3) Remove obsolete training CSS generations. The current full-training-table-v2
# block remains authoritative and mobile-safe.
patterns = [
    r'/\* Training schedule: true table on wide screens, readable stacked rows on phones \*/.*?(?=/\* Mobile-first, accessible training schedule \*/)',
    r'/\* Mobile-first, accessible training schedule \*/.*?(?=\n\.weekly-updates)',
    r'/\* Mobile training schedule hotfix: no sideways movement on narrow phones\. \*/.*?(?=/\* full-training-table-v2 \*/)',
]
for pat in patterns:
    html = re.sub(pat, '', html, flags=re.S)

# 4) Collapse excessive blank lines introduced by incremental patching.
html = re.sub(r'\n{4,}', '\n\n', html)

if html != original:
    path.write_text(html, encoding='utf-8')

print('changed=', html != original)
print('premium_v4_blocks=', html.count('id="summary7-premium-v4"'))
print('full_training_marker=', html.count('full-training-table-v2'))
print('training_tables=', html.count('class="training-table"'))
print('open_style_tags=', html.count('<style'))
print('close_style_tags=', html.count('</style>'))
