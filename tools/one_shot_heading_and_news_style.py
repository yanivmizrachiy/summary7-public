from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

repls={
'<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ז׳</h2>':'<h2 class="grade-page-title"><span class="grade-title-main">מה אנחנו מלמדים?</span><span class="grade-title-sub">בשכבת ז׳</span></h2>',
'<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ח׳</h2>':'<h2 class="grade-page-title"><span class="grade-title-main">מה אנחנו מלמדים?</span><span class="grade-title-sub">בשכבת ח׳</span></h2>',
'<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ט׳ רגילה</h2>':'<h2 class="grade-page-title"><span class="grade-title-main">מה אנחנו מלמדים?</span><span class="grade-title-sub">בשכבת ט׳ רגילה</span></h2>',
'<h2 class="grade-page-title">מה אנחנו מלמדים בשכבת ט׳ מצומצמת</h2>':'<h2 class="grade-page-title"><span class="grade-title-main">מה אנחנו מלמדים?</span><span class="grade-title-sub">בשכבת ט׳ מצומצמת</span></h2>',
'<h3>סרטון המחשה של איילת קריספין בנושא חרוט</h3>':'<h3>פורסם סרטון המחשה של איילת קריספין בנושא חרוט</h3>',
'<h3>דפי עבודה בנושא חרוט</h3>':'<h3>פורסמו דפי עבודה בנושא חרוט</h3>',
'<h3>דפי עבודה בנושא גליל</h3>':'<h3>פורסמו דפי עבודה בנושא גליל</h3>',
}
for a,b in repls.items():
    s=s.replace(a,b)
p.write_text(s,encoding='utf-8')

cssp=Path('styles.css')
css=cssp.read_text(encoding='utf-8')
marker='/* grade-heading-hierarchy-final */'
if marker not in css:
    css += r'''

/* grade-heading-hierarchy-final */
.grade-page-title{display:grid;gap:5px!important;margin-bottom:18px!important}
.grade-title-main{display:block;font:900 clamp(2.5rem,7vw,4.8rem)/.95 "Frank Ruhl Libre",serif;letter-spacing:-.035em}
.grade-title-sub{display:block;font:800 clamp(1rem,2.2vw,1.35rem)/1.3 "Rubik",Arial,sans-serif;letter-spacing:0;color:#5e7181}
@media(max-width:720px){
  .grade-title-main{font-size:clamp(2.2rem,12vw,3.35rem)}
  .grade-title-sub{font-size:1rem}
}
'''
    cssp.write_text(css,encoding='utf-8')
print('updated grade heading hierarchy and news style')
