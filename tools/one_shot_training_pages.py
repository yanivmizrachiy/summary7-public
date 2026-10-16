from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
pat=re.compile(r'<section class="sheet courses-page" id="courses"><div class="sheet-inner wide">(?P<head>.*?<table class="training-table"><thead>(?P<thead>.*?)</thead><tbody>)(?P<tbody>.*?)(?P<tail></tbody></table></div></div></section>)',re.S)
m=pat.search(s)
if not m: raise SystemExit('courses section not found')
rows=re.findall(r'<tr(?: class="verification-row")?>.*?</tr>',m.group('tbody'),flags=re.S)
if len(rows)<6: raise SystemExit(f'expected >=6 rows, got {len(rows)}')
thead=m.group('thead')
chunks=[rows[i:i+2] for i in range(0,len(rows),2)]
pages=[]
for i,ch in enumerate(chunks,1):
    title='השתלמויות לחטיבת הביניים' if i==1 else 'השתלמויות לחטיבת הביניים — המשך'
    intro='<p class="eyebrow">פיתוח מקצועי · תשפ״ז</p><h2>'+title+'</h2>'
    if i==1:
        intro+='<p class="training-note">כל השדות נשמרים גם בנייד. פרט שלא אומת מסומן במפורש ואינו מושלם בהשערה.</p>'
    page=f'<section class="sheet courses-page courses-page-part" id="courses{("" if i==1 else f"-{i}")}"><div class="sheet-inner wide">{intro}<div class="training-wrap"><table class="training-table"><thead>{thead}</thead><tbody>{"".join(ch)}</tbody></table></div></div></section>'
    pages.append(page)
new='\n'.join(pages)
s=s[:m.start()]+new+s[m.end():]
p.write_text(s,encoding='utf-8')
cssp=Path('styles.css'); css=cssp.read_text(encoding='utf-8')
marker='/* training-a4-pages-final */'
if marker not in css:
    css+='\n\n'+marker+'\n.courses-page-part{overflow:hidden!important}\n.courses-page-part .sheet-inner{padding-top:10px!important}\n@media(max-width:720px){.courses-page-part{overflow:visible!important;min-height:auto!important}.courses-page-part .training-table td{grid-template-columns:minmax(0,34%) minmax(0,1fr)!important}}\n@media(max-width:390px){.courses-page-part .training-table td{grid-template-columns:1fr!important}}\n@media print{.courses-page-part{break-after:page;page-break-after:always;overflow:visible!important}}\n'
cssp.write_text(css,encoding='utf-8')
print('training table split into',len(chunks),'A4 pages')
