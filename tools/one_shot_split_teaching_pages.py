from pathlib import Path
import re

index = Path('index.html')
css = Path('styles.css')
html = index.read_text(encoding='utf-8')
styles = css.read_text(encoding='utf-8')

old = re.search(r'\n  <section class="sheet teaching-page" id="teaching">.*?\n  </section>\n\n  <section class="sheet news-page" id="news">', html, re.S)
if not old:
    raise SystemExit('teaching section not found')

replacement = '''
  <section class="sheet teaching-page teaching-intro" id="teaching">
    <div class="sheet-inner teaching-head">
      <p class="eyebrow">אוקטובר · תוכנית הלימודים</p>
      <h2>מה אנחנו מלמדים?</h2>
      <p class="teaching-lead">כל שכבה מוצגת בנפרד כדי לאפשר קריאה מהירה וברורה בנייד.</p>
    </div>
  </section>

  <section class="sheet grade-page grade-7" id="grade-7">
    <div class="sheet-inner grade-page-inner">
      <p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>
      <article class="grade-sheet"><h3>שכבת ז׳</h3><h4>תחום מספרי</h4><ul><li>מספרים שליליים ומספרים נגדיים</li><li>חיבור וחיסור מספרים מכוונים</li><li>הרחבת מערכת הצירים</li></ul><h4>תחום גאומטרי</h4><ul><li>חוצה זווית</li><li>סכום והפרש זוויות</li><li>זוויות צמודות וקודקודיות</li></ul><h4>משימת חובה</h4><p>גיימינג־אפ — מערכת צירים ומספרים חיוביים</p></article>
    </div>
  </section>

  <section class="sheet grade-page grade-8" id="grade-8">
    <div class="sheet-inner grade-page-inner">
      <p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>
      <article class="grade-sheet"><h3>שכבת ח׳</h3><h4>תחום מספרי</h4><ul><li>יחס</li><li>פרופורציה</li><li>קנה מידה</li><li>אחוזים</li></ul><h4>גאומטריה</h4><ul><li>משפט פיתגורס</li><li>גליל</li><li>חרוט</li></ul><h4>אי־ודאות וסטטיסטיקה</h4><ul><li>איסוף מידע</li><li>קריאת מידע</li><li>שכיחות</li></ul><h4>משימת חובה</h4><p>ציור קיר — יחס, פרופורציה וקנה מידה</p></article>
    </div>
  </section>

  <section class="sheet grade-page grade-9-high" id="grade-9-high">
    <div class="sheet-inner grade-page-inner">
      <p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>
      <article class="grade-sheet"><h3>שכבת ט׳ — 4–5 יח״ל</h3><h4>אלגברה</h4><ul><li>פירוק לגורמים</li><li>תלת־איבר ריבועי</li><li>נוסחאות הכפל המקוצר</li><li>משוואות ריבועיות בסיסיות</li><li>שברים אלגבריים</li></ul><h4>גאומטריה</h4><ul><li>משפטים הפוכים במשולש שווה שוקיים</li><li>חוצה זווית הראש, גובה ותיכון</li><li>שילוב במערכת צירים</li></ul></article>
    </div>
  </section>

  <section class="sheet grade-page grade-9-three" id="grade-9-three">
    <div class="sheet-inner grade-page-inner">
      <p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>
      <article class="grade-sheet"><h3>שכבת ט׳ — 3 יח״ל</h3><h4>פונקציה קווית</h4><ul><li>שיפוע וקצב שינוי</li><li>ייצוג אלגברי וגרפי</li><li>נקודות חיתוך עם הצירים</li><li>מציאת משוואת ישר</li></ul><h4>אלגברה</h4><ul><li>חוק הפילוג והפילוג המורחב</li><li>פתרון משוואות פשוטות</li></ul><h4>גאומטריה</h4><ul><li>משפט פיתגורס</li><li>חישובי צלעות, היקפים ושטחים</li></ul></article>
    </div>
  </section>

  <section class="sheet news-page" id="news">'''
html = html[:old.start()] + '\n' + replacement + html[old.end():]

marker = '/* split-teaching-pages-2026-10-16 */'
if marker not in styles:
    styles += '''\n\n/* split-teaching-pages-2026-10-16 */
.teaching-intro{background:#fff;box-shadow:none;border-radius:0}
.teaching-head{padding-top:18px!important;padding-bottom:12px!important}
.teaching-lead{margin:0;color:#607487;font-size:1rem;line-height:1.6}
.grade-page{min-height:72svh;display:block}
.grade-page-inner{padding-top:24px!important;padding-bottom:34px!important}
.grade-sheet{max-width:820px;margin:0 auto;padding:clamp(22px,4vw,34px);border-radius:26px;background:rgba(255,255,255,.90);border:1px solid rgba(255,255,255,.72);box-shadow:0 20px 50px rgba(30,45,70,.10);backdrop-filter:blur(10px)}
.grade-sheet h3{margin:0 0 18px;font:900 clamp(2.1rem,7vw,3.8rem)/1 "Frank Ruhl Libre",serif}
.grade-sheet h4{margin:20px 0 8px;font-size:1rem;letter-spacing:.01em}
.grade-sheet ul{margin:0;padding-inline-start:22px}
.grade-sheet li,.grade-sheet p{font-size:1.02rem;line-height:1.75;color:#314e64}
.grade-7{background:radial-gradient(circle at 88% 10%,rgba(39,190,255,.26),transparent 28%),linear-gradient(135deg,#dff7ff,#f7fdff 52%,#eaf2ff)}
.grade-7 .grade-sheet h3,.grade-7 .grade-sheet h4{color:#126e9b}
.grade-8{background:radial-gradient(circle at 14% 12%,rgba(255,181,64,.30),transparent 28%),linear-gradient(135deg,#fff0c9,#fffaf0 52%,#fff4e4)}
.grade-8 .grade-sheet h3,.grade-8 .grade-sheet h4{color:#9b6412}
.grade-9-high{background:radial-gradient(circle at 84% 10%,rgba(157,111,255,.28),transparent 28%),linear-gradient(135deg,#efe7ff,#fbf9ff 52%,#edf0ff)}
.grade-9-high .grade-sheet h3,.grade-9-high .grade-sheet h4{color:#6842a8}
.grade-9-three{background:radial-gradient(circle at 12% 10%,rgba(55,196,139,.28),transparent 28%),linear-gradient(135deg,#ddf8ed,#f8fffc 52%,#eaf9f1)}
.grade-9-three .grade-sheet h3,.grade-9-three .grade-sheet h4{color:#21745a}
@media(max-width:720px){.teaching-head{padding:16px 17px 8px!important}.teaching-head h2{margin-bottom:8px}.grade-page{min-height:0;border-radius:0}.grade-page-inner{padding:18px 14px 24px!important}.grade-sheet{padding:20px 18px;border-radius:20px;box-shadow:0 10px 26px rgba(30,45,70,.08)}.grade-sheet h3{font-size:2.35rem;margin-bottom:14px}.grade-sheet h4{margin-top:17px}.grade-sheet li,.grade-sheet p{font-size:1rem;line-height:1.65}}
@media print{.teaching-intro{display:none}.grade-page{min-height:297mm;page-break-after:always}.grade-page-inner{padding:14mm!important}.grade-sheet{box-shadow:none}}
'''

# safety checks
for token in ['id="grade-7"','id="grade-8"','id="grade-9-high"','id="grade-9-three"','class="training-table"','id="news"']:
    if token not in html:
        raise SystemExit(f'missing {token}')
if 'split-teaching-pages-2026-10-16' not in styles:
    raise SystemExit('css marker missing')

index.write_text(html, encoding='utf-8')
css.write_text(styles, encoding='utf-8')
print('updated index.html and styles.css')
