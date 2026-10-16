from pathlib import Path

p=Path('styles.css')
css=p.read_text(encoding='utf-8')
html=Path('index.html').read_text(encoding='utf-8')

if 'class="cards"' in html:
    raise SystemExit('ABORT: cards is active')
for marker in ['id="teaching"','class="cal-table"']:
    if marker not in html:
        raise SystemExit(f'ABORT: required HTML marker missing: {marker}')

removed=0
replacements={
    '.cards a,.panel{': '.panel{',
    '.cards a,.panel{box-shadow:none!important': '.panel{box-shadow:none!important',
    '.cards a,.panel{padding:17px}': '.panel{padding:17px}',
}
for old,new in replacements.items():
    if old in css:
        css=css.replace(old,new)
        removed+=1

dup='.cal-table .cal-date{font-weight:800;font-variant-numeric:tabular-nums;white-space:normal;line-height:1.65}'
first=css.find(dup)
second=css.find(dup,first+1) if first!=-1 else -1
if second!=-1:
    css=css[:second]+css[second+len(dup):]
    removed+=1

if removed < 1:
    raise SystemExit('ABORT: no verified cleanup target found')
for required in ['#teaching{position:relative','#teaching:before{content:','.cal-table .cal-date{font-weight:800;color:#22577f','.training-table','.workbooks-table','.lux-hero','.panel{']:
    if required not in css:
        raise SystemExit(f'ABORT: critical CSS missing: {required}')

p.write_text(css,encoding='utf-8')
print('cleanup_targets=',removed)
print('styles_bytes=',len(css.encode('utf-8')))
