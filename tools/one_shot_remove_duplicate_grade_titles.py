from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
repls={
'<article class="grade-sheet"><h3>שכבת ז׳</h3>':'<article class="grade-sheet">',
'<article class="grade-sheet"><h3>שכבת ח׳</h3>':'<article class="grade-sheet">',
'<article class="grade-sheet"><h3>שכבת ט׳ — רגילה</h3>':'<article class="grade-sheet">',
'<article class="grade-sheet"><h3>שכבת ט׳ — מצומצמת</h3>':'<article class="grade-sheet">',
}
for a,b in repls.items():
    s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
print('removed duplicate grade titles')
