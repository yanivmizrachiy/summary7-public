from pathlib import Path

p=Path('styles.css')
css=p.read_text(encoding='utf-8')
html=Path('index.html').read_text(encoding='utf-8')

for marker in ['id="teaching"','class="cal-table"']:
    if marker not in html:
        raise SystemExit(f'ABORT: required HTML marker missing: {marker}')

removed=0
pairs=[
('#courses,#news,#calendar,#moodle,#workbooks,#teaching{margin-top:30px;padding:28px clamp(18px,3.5vw,34px) 32px;border-radius:18px;border:1px solid transparent;box-shadow:0 6px 24px #18334d0a;position:relative;overflow:hidden}', '#courses,#news,#calendar,#moodle,#workbooks{margin-top:30px;padding:28px clamp(18px,3.5vw,34px) 32px;border-radius:18px;border:1px solid transparent;box-shadow:0 6px 24px #18334d0a;position:relative;overflow:hidden}'),
('#courses:before,#news:before,#calendar:before,#moodle:before,#workbooks:before,#teaching:before{content:"";position:absolute;inset-block:0;inset-inline-start:0;width:5px}', '#courses:before,#news:before,#calendar:before,#moodle:before,#workbooks:before{content:"";position:absolute;inset-block:0;inset-inline-start:0;width:5px}'),
('@media(max-width:700px){#courses,#news,#calendar,#moodle,#workbooks,#teaching{margin-top:22px;padding:19px 16px 21px;border-radius:14px}main{', '@media(max-width:700px){#courses,#news,#calendar,#moodle,#workbooks{margin-top:22px;padding:19px 16px 21px;border-radius:14px}main{'),
('@media(max-width:360px){main{padding-left:max(11px,env(safe-area-inset-left));padding-right:max(11px,env(safe-area-inset-right))}#courses,#news,#calendar,#moodle,#workbooks,#teaching{padding:16px 13px 18px}}', '@media(max-width:360px){main{padding-left:max(11px,env(safe-area-inset-left));padding-right:max(11px,env(safe-area-inset-right))}#courses,#news,#calendar,#moodle,#workbooks{padding:16px 13px 18px}}'),
('@media print{#courses,#news,#calendar,#moodle,#workbooks,#teaching{background:#fff!important;border:0;box-shadow:none;padding:0;margin-top:18px}#courses:before,#news:before,#calendar:before,#moodle:before,#workbooks:before,#teaching:before{display:none}}', '@media print{#courses,#news,#calendar,#moodle,#workbooks{background:#fff!important;border:0;box-shadow:none;padding:0;margin-top:18px}#courses:before,#news:before,#calendar:before,#moodle:before,#workbooks:before{display:none}}')
]
for old,new in pairs:
    if old in css:
        css=css.replace(old,new); removed+=1

for old in ['#teaching{background-color:#e9f4f6;border-color:#cfe6ea}','#teaching:before{background:#2b7d8c}','#teaching h2:before{background:#2b7d8c}']:
    if old in css:
        css=css.replace(old,''); removed+=1

old='.cal-table .cal-date{font-weight:800;color:#22577f;white-space:nowrap}'
new='.cal-table .cal-date{font-weight:800;color:#22577f;font-variant-numeric:tabular-nums;white-space:normal;line-height:1.65}'
if old in css:
    css=css.replace(old,new); removed+=1
later='.cal-table .cal-date{font-weight:800;font-variant-numeric:tabular-nums;white-space:normal;line-height:1.65}'
first=css.find(later)
second=css.find(later, first+1) if first!=-1 else -1
if second!=-1:
    css=css[:second]+css[second+len(later):]; removed+=1

if removed < 7:
    raise SystemExit(f'ABORT: expected cleanup targets not found; removed={removed}')
for required in ['#teaching{position:relative','#teaching:before{content:','.cal-table .cal-date{font-weight:800;color:#22577f','.training-table','.workbooks-table','.lux-hero']:
    if required not in css:
        raise SystemExit(f'ABORT: critical CSS missing: {required}')
p.write_text(css,encoding='utf-8')
print('cleanup_targets=',removed)
print('styles_bytes=',len(css.encode('utf-8')))
