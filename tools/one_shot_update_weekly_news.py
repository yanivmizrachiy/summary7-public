from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
old='<section id="news"><h2>מה חדש השבוע</h2><div class="weekly-updates"><article class="weekly-update"><h3>פורסמו חוברות עבודה בנושא גליל וחרוט</h3>'
new='<section id="news"><h2>מה חדש השבוע</h2><div class="weekly-updates"><article class="weekly-update"><h3>קיימנו הדרכה בנושא Moodle</h3><p>קיימנו הדרכה בנושא Moodle על פתיחת מרחבי למידה והגשת משימות החובה בשכבות ז׳–ח׳.</p></article><article class="weekly-update"><h3>פורסמו חוברות עבודה בנושא גליל וחרוט</h3>'
if old not in s:
    raise SystemExit('ABORT: weekly news anchor not found')
if 'קיימנו הדרכה בנושא Moodle' in s:
    raise SystemExit('ABORT: weekly training item already exists')
s=s.replace(old,new,1)
for required in ['פורסמו חוברות עבודה בנושא גליל וחרוט','פורסם סרטון המחשה של איילת קריספין בנושא חרוט','id="news"']:
    if required not in s:
        raise SystemExit('ABORT: required weekly item missing: '+required)
p.write_text(s,encoding='utf-8')
print('weekly news updated')
