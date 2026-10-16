from pathlib import Path
import re

htmlp=Path('index.html'); cssp=Path('styles.css')
html=htmlp.read_text(encoding='utf-8'); css=cssp.read_text(encoding='utf-8')
pat=re.compile(r'<article class="story whatsapp-story science-story">.*?</article>',re.S)
m=pat.search(html)
if not m:
    raise SystemExit('science story card not found')
card=m.group(0)
article=card.replace('<article class="story whatsapp-story science-story">','<article class="science-a4-card">',1)
science='''\n  <section class="sheet science-a4-page" id="science-2027"><div class="sheet-inner science-a4-inner"><p class="eyebrow">מה חדש השבוע? · תוכנית לכיתות ט׳</p>'''+article+'''</div></section>\n\n'''
html=html[:m.start()]+html[m.end():]
anchor='  <section class="sheet news-page" id="news">'
if anchor not in html: raise SystemExit('news section marker missing')
html=html.replace(anchor,science+anchor,1)
marker='/* a4-pages-2026-10-16 */'
if marker not in css:
    css += '''\n\n/* a4-pages-2026-10-16 */
.sheet{aspect-ratio:210/297;min-height:clamp(560px,calc((100vw - 32px)*1.4142),1584px);overflow:hidden}
.science-a4-page{background:radial-gradient(circle at 86% 8%,rgba(37,211,102,.22),transparent 25%),linear-gradient(145deg,#eefcf3,#fff 55%,#e7f8ef)}
.science-a4-inner{min-height:100%;display:grid;align-content:start;gap:18px;padding-top:clamp(34px,5vw,58px)!important}
.science-a4-card{position:relative;max-width:820px;margin:0 auto;padding:clamp(26px,5vw,46px);border:1px solid rgba(36,170,92,.28);border-radius:28px;background:rgba(255,255,255,.94);box-shadow:0 18px 42px rgba(31,126,72,.11)}
.science-a4-card:before{content:"";position:absolute;inset-inline-start:0;top:0;bottom:0;width:6px;background:linear-gradient(#25d366,#128c7e);border-radius:28px 0 0 28px}
.science-a4-card h3{margin-bottom:18px;color:#17613d;font:900 clamp(2rem,5vw,3.2rem)/1.05 "Frank Ruhl Libre",serif}
.science-a4-card p{font-size:clamp(1rem,2.2vw,1.16rem);line-height:1.82;color:#3f6250}
@media(max-width:720px){.sheet{min-height:560px;aspect-ratio:210/297;overflow:hidden}.science-a4-inner{padding:24px 16px!important}.science-a4-card{padding:22px 18px;border-radius:20px}.science-a4-card h3{font-size:2.1rem}}
@media print{.sheet{width:210mm;min-height:297mm;aspect-ratio:auto;break-after:page;page-break-after:always;overflow:visible}.science-a4-page{break-before:page;page-break-before:always}.science-a4-inner{min-height:297mm}}
'''
for token in ['id="science-2027"','science-a4-card','https://qrco.de/bh31gu','מדע בכיתה 2027 יוצאת לדרך!']:
    if token not in html: raise SystemExit('missing '+token)
htmlp.write_text(html,encoding='utf-8'); cssp.write_text(css,encoding='utf-8')
print('A4 science page applied')
