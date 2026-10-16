from pathlib import Path
import re
from html import escape

p=Path('index.html')
s=p.read_text(encoding='utf-8')
# Collect all training rows from all current course sections.
sections=list(re.finditer(r'<section class="sheet courses-page courses-page-part"[^>]*>.*?</section>', s, flags=re.S))
if not sections:
    raise SystemExit('training sections not found')
rows=[]
for m in sections:
    block=m.group(0)
    for trm in re.finditer(r'<tr(?: class="([^"]*)")?>(.*?)</tr>', block, flags=re.S):
        row_html=trm.group(2)
        if '<td ' not in row_html:
            continue
        cells={}
        for tdm in re.finditer(r'<td data-label="([^"]+)">(.*?)</td>', row_html, flags=re.S):
            cells[tdm.group(1)] = tdm.group(2)
        if cells:
            rows.append((trm.group(1) or '', cells))
if len(rows) < 6:
    raise SystemExit(f'expected at least 6 training rows, got {len(rows)}')
# Deduplicate by training name + compass number.
seen=set(); uniq=[]
for cls,cells in rows:
    key=(re.sub('<[^>]+>','',cells.get('שם ההשתלמות','')), re.sub('<[^>]+>','',cells.get('מספר במצפן','')))
    if key in seen: continue
    seen.add(key); uniq.append((cls,cells))
rows=uniq

groups=[
 ('טבלת השתלמויות — פרטים מרכזיים',['שם ההשתלמות','נושא','קהל יעד']),
 ('טבלת השתלמויות — מועדים ומפגשים',['שם ההשתלמות','מועדים ומפגש ראשון','יום / שעה / מיקום']),
 ('טבלת השתלמויות — היקף, מנחה ומצפן',['שם ההשתלמות','היקף / גמול','מנחה','מספר במצפן']),
 ('טבלת השתלמויות — מיומנויות, קישורים ואימות',['שם ההשתלמות','כישורים / מיומנויות','סילבוס','הרשמה','סטטוס אימות'])
]

def build_table(title, cols, idx):
    th=''.join(f'<th>{escape(c)}</th>' for c in cols)
    trs=[]
    for cls,cells in rows:
        td=''.join(f'<td>{cells.get(c,"—")}</td>' for c in cols)
        class_attr=f' class="{cls}"' if cls else ''
        trs.append(f'<tr{class_attr}>{td}</tr>')
    note='<p class="training-note">אותן השתלמויות מוצגות בכל חלק; העמודות מפוצלות כדי לשמור על טבלה אמיתית, קריאה מלאה וללא גלילה אופקית.</p>' if idx==1 else ''
    anchor=' id="courses"' if idx==1 else ''
    return f'''\n  <section class="sheet courses-page true-table-page"{anchor}><div class="sheet-inner wide"><p class="eyebrow">פיתוח מקצועי · תשפ״ז</p><h2>{title}</h2>{note}<div class="training-wrap"><table class="training-table true-training-table"><thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table></div></div></section>\n'''

replacement=''.join(build_table(title,cols,i+1) for i,(title,cols) in enumerate(groups))
start=sections[0].start(); end=sections[-1].end()
s=s[:start]+replacement+s[end:]
p.write_text(s,encoding='utf-8')

cssp=Path('styles.css'); css=cssp.read_text(encoding='utf-8')
marker='/* true-training-table-final */'
if marker not in css:
    css += r'''

/* true-training-table-final */
.true-table-page{overflow:hidden}
.true-training-table{display:table!important;width:100%!important;table-layout:fixed!important;border-collapse:separate!important;border-spacing:0!important}
.true-training-table thead{display:table-header-group!important;position:static!important;width:auto!important;height:auto!important;margin:0!important;overflow:visible!important;clip:auto!important;white-space:normal!important}
.true-training-table tbody{display:table-row-group!important}
.true-training-table tr{display:table-row!important;width:auto!important;border:0!important;border-radius:0!important;box-shadow:none!important;background:transparent!important}
.true-training-table th,.true-training-table td{display:table-cell!important;width:auto!important;min-width:0!important;max-width:none!important;padding:8px 7px!important;border-bottom:1px solid #f0e5e8!important;border-inline-start:1px solid #f3ecee!important;vertical-align:top!important;text-align:right!important;line-height:1.45!important;overflow-wrap:anywhere!important;word-break:break-word!important}
.true-training-table td:before{content:none!important;display:none!important}
.true-training-table thead th{background:linear-gradient(135deg,#a61d3b,#c83f59)!important;color:#fff!important}
.true-training-table tbody tr:nth-child(even){background:#fff9fa!important}
.true-training-table .verification-row{background:#fff5d9!important}
@media(max-width:720px){
  .true-table-page .sheet-inner{padding:18px 8px!important}
  .true-table-page h2{font-size:1.7rem!important;margin-bottom:10px!important}
  .true-training-table{font-size:.63rem!important}
  .true-training-table th,.true-training-table td{padding:6px 4px!important;line-height:1.35!important}
  .true-training-table a{font-size:.62rem!important}
  .true-table-page{overflow:hidden!important}
  .true-table-page .training-wrap{overflow:hidden!important;width:100%!important}
}
@media(max-width:390px){
  .true-training-table{font-size:.57rem!important}
  .true-training-table th,.true-training-table td{padding:5px 3px!important}
  .true-table-page .sheet-inner{padding-inline:5px!important}
}
'''
cssp.write_text(css,encoding='utf-8')
print(f'created {len(groups)} true tables for {len(rows)} trainings')
