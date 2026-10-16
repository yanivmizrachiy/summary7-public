from pathlib import Path
import re

html = Path('index.html').read_text(encoding='utf-8')
css_path = Path('styles.css')
css = css_path.read_text(encoding='utf-8')

# Only selectors proven absent from current HTML.
dead_markers = ['class="actions"','class="cards"','class="panel"','class="grades"','<header','</header>']
for marker in dead_markers:
    if marker in html:
        raise SystemExit(f'ABORT: legacy marker still active: {marker}')

selectors = [
    'header','header:before','header:after','header small','header h1','header p',
    '.actions','.actions button,.actions a','.actions button:hover,.actions a:hover',
    '.cards','.cards a,.panel','.cards a','.cards a:hover',
    '.panel','.panel b',
    '.grades','.grades .panel','.grades h3','.grades h4','.grades ul','.grades li'
]
removed = 0
for selector in selectors:
    pattern = re.compile(r'(?m)(?<![^}\n])\s*' + re.escape(selector) + r'\s*\{[^{}]*\}\s*')
    css, n = pattern.subn('\n', css)
    removed += n

# Collapse excessive blank lines only; preserve cascade/order.
css = re.sub(r'\n{4,}', '\n\n\n', css).strip() + '\n'

if removed == 0:
    raise SystemExit('ABORT: no proven-dead CSS rules were removed')

# Safety: active critical selectors must remain.
for required in ['.lux-hero', '.author-intro', '.training-table', '.cal-table', '.workbooks-table', '#courses', '#teaching', 'nav.quick']:
    if required not in css:
        raise SystemExit(f'ABORT: critical selector missing after cleanup: {required}')

css_path.write_text(css, encoding='utf-8')
print('removed_rules=', removed)
print('styles_bytes=', len(css.encode('utf-8')))
