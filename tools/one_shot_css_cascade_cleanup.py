from pathlib import Path

p = Path('styles.css')
css = p.read_text(encoding='utf-8')
html = Path('index.html').read_text(encoding='utf-8')

if '<header' in html or '</header>' in html:
    raise SystemExit('ABORT: header is active')
if 'class="actions"' in html:
    raise SystemExit('ABORT: actions is active')

replacements = {
    '#moodle{padding:27px 30px 30px;background:#f5f8fb;border:1px solid #e2eaf0;border-radius:16px}\n': '',
    'header:before,header:after{display:none}\n': '',
    'header p,header small{color:#102d47!important}': '',
    'nav.quick,.actions{display:none!important}': 'nav.quick{display:none!important}',
    '@media(max-width:360px){header h1{font-size:38px}main{': '@media(max-width:360px){main{',
    'section{margin-top:36px}#moodle{padding:18px}.grades{grid-template-columns:1fr}': 'section{margin-top:36px}.grades{grid-template-columns:1fr}',
}

removed = 0
for old, new in replacements.items():
    if old in css:
        css = css.replace(old, new)
        removed += 1

if removed < 5:
    raise SystemExit(f'ABORT: expected cleanup targets not found; removed={removed}')

for required in ['.lux-hero', '.author-intro', '.training-table', '.cal-table', '.workbooks-table', '#courses', '#moodle', '#teaching', 'nav.quick', '.panel', '.grades']:
    if required not in css:
        raise SystemExit(f'ABORT: critical selector missing: {required}')

p.write_text(css, encoding='utf-8')
print('cleanup_targets=', removed)
print('styles_bytes=', len(css.encode('utf-8')))
