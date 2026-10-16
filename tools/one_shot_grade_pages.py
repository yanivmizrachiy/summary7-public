from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'\n\s*<section class="sheet teaching-page teaching-intro" id="teaching">.*?</section>\n','\n',s,count=1,flags=re.S)
repls={
'מה אנחנו מלמדים באוקטובר · שכבת ז׳':'מה אנחנו מלמדים בשכבת ז׳',
'מה אנחנו מלמדים באוקטובר · שכבת ח׳':'מה אנחנו מלמדים בשכבת ח׳',
'מה אנחנו מלמדים באוקטובר · שכבת ט׳ רגילה':'מה אנחנו מלמדים בשכבת ט׳ רגילה',
'מה אנחנו מלמדים באוקטובר · שכבת ט׳ מצומצמת':'מה אנחנו מלמדים בשכבת ט׳ מצומצמת',
}
for a,b in repls.items(): s=s.replace(a,b)
s=s.replace('<p class="eyebrow">מה אנחנו מלמדים בשכבת ז׳</p><article class="grade-sheet"><h3>שכבת ז׳</h3>', '<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ז׳</h2><article class="grade-sheet"><h3>שכבת ז׳</h3>')
s=s.replace('<p class="eyebrow">מה אנחנו מלמדים בשכבת ח׳</p><article class="grade-sheet"><h3>שכבת ח׳</h3>', '<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ח׳</h2><article class="grade-sheet"><h3>שכבת ח׳</h3>')
s=s.replace('<p class="eyebrow">מה אנחנו מלמדים בשכבת ט׳ רגילה</p><article class="grade-sheet"><h3>שכבת ט׳ — רגילה</h3>', '<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ט׳ רגילה</h2><article class="grade-sheet"><h3>שכבת ט׳ — רגילה</h3>')
s=s.replace('<p class="eyebrow">מה אנחנו מלמדים בשכבת ט׳ מצומצמת</p><article class="grade-sheet"><h3>שכבת ט׳ — מצומצמת</h3>', '<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ט׳ מצומצמת</h2><article class="grade-sheet"><h3>שכבת ט׳ — מצומצמת</h3>')
for x in ['מה אנחנו מלמדים בשכבת ז׳','מה אנחנו מלמדים בשכבת ח׳','מה אנחנו מלמדים בשכבת ט׳ רגילה','מה אנחנו מלמדים בשכבת ט׳ מצומצמת']:
    if x not in s: raise SystemExit('missing '+x)
if 'teaching-intro' in s or '<h2>מה אנחנו מלמדים באוקטובר</h2>' in s: raise SystemExit('generic teaching page still present')
p.write_text(s,encoding='utf-8')
cssp=Path('styles.css'); css=cssp.read_text(encoding='utf-8')
if '/* grade-page-title-final */' not in css:
    css += '\n\n/* grade-page-title-final */\n.grade-page-title{margin:0 0 18px;color:var(--blue);font:900 clamp(2rem,5vw,3.4rem)/1.05 "Frank Ruhl Libre",serif;letter-spacing:-.02em}\n@media(max-width:720px){.grade-page-title{margin:0 0 14px;font-size:2rem;line-height:1.08}}\n'
cssp.write_text(css,encoding='utf-8')
print('grade pages corrected')
