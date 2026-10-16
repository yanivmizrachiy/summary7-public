from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

old_sub='<p class="lux-subtitle">השתלמויות, עדכונים, מועדים, Moodle, חוברות עבודה ומה אנחנו מלמדים</p><div class="lux-chips"><span>מתמטיקה בחטיבת הביניים</span><span>כיתות ז׳–ט׳</span><span>בהובלת איילת קריספין</span></div>'
new_sub='<p class="lux-subtitle">הדרכה במתמטיקה · מחוז ירושלים והעיר ירושלים – מנח״י · בהובלת איילת קריספין</p>'

old_intro='<div class="author-intro"><img src="https://jerusalem2.vercel.app/media/team/yaniv.jpg" alt="יניב רז" width="64" height="64"><div><strong>שלום לכולם,</strong></div></div><nav class="quick" aria-label="ניווט לפי נושא"><a href="#courses">השתלמויות</a><a href="#news">מה חדש</a><a href="#calendar">מה צפוי</a><a href="#moodle">Moodle</a><a href="#workbooks">חוברות</a><a href="#teaching">מה אנחנו מלמדים</a></nav>'
new_intro='<section class="intro-section"><div class="author-intro"><img src="https://jerusalem2.vercel.app/media/team/yaniv.jpg" alt="יניב רז" width="64" height="64"><div><strong>שלום לכולם,</strong></div></div><p class="intro-copy">בסיכום השבועי ריכזתי עבורכם את העדכונים המרכזיים להמשך חודש אוקטובר: ההשתלמויות הקרובות, ההיערכות למשימות ה־Moodle בשכבות ז׳–ח׳, חוברות העבודה והחומרים החדשים, וכן המועדים המרכזיים להמשך אוקטובר ונובמבר. המטרה היא לאפשר לכל מורה להתעדכן במהירות, לזהות מה דורש תשומת לב ולחזור בקלות לחומרים הרלוונטיים להוראה.</p></section>'

if old_sub not in s:
    raise SystemExit('ABORT: hero demo copy not found')
if old_intro not in s:
    raise SystemExit('ABORT: intro/navigation block not found')

s=s.replace(old_sub,new_sub,1)
s=s.replace(old_intro,new_intro,1)

# Safety checks: remove demo-like homepage controls while preserving real content/actions.
for forbidden in ['class="lux-chips"','<nav class="quick"']:
    if forbidden in s:
        raise SystemExit(f'ABORT: homepage demo control still present: {forbidden}')
for required in ['id="green-page"','id="courses"','id="news"','id="calendar"','id="moodle"','id="workbooks"','id="teaching"','שלום לכולם,','class="intro-copy"']:
    if required not in s:
        raise SystemExit(f'ABORT: required content missing: {required}')

p.write_text(s,encoding='utf-8')
print('homepage copy cleaned')
