from pathlib import Path
import re

p = Path('index.html')
cssp = Path('styles.css')
s = p.read_text(encoding='utf-8')
styles = cssp.read_text(encoding='utf-8')

pat = re.compile(r'\n  <section class="sheet moodle-page" id="moodle">.*?\n  </section>\n\n  <section class="sheet workbooks-page" id="workbooks">', re.S)
m = pat.search(s)
if not m:
    raise SystemExit('moodle section not found')

new = '''
  <section class="sheet moodle-page" id="moodle">
    <div class="sheet-inner">
      <p class="eyebrow">Moodle · משימות לאורך שנת הלימודים</p>
      <h2>משימות חובה ומשימות הערכה — מה חשוב לדעת?</h2>
      <p class="lead">במהלך שנת הלימודים התלמידים יגישו שני סוגים של משימות במרחבי ה־Moodle: <strong>משימות חובה</strong> ו<strong>משימות הערכה</strong>. חשוב להבחין ביניהן, לדעת היכן הן מופיעות בפריסות, ולשלוח לתלמידים את הקישור הנכון מתוך מרחב הלמידה של המורה.</p>

      <div class="moodle-guidance-grid">
        <article class="moodle-guide mandatory-guide">
          <span class="guide-kicker">משימות חובה</span>
          <h3>איפה מוצאים את משימות החובה?</h3>
          <p>משימות החובה מופיעות בתוך <strong>הפריסות</strong>, בעמודה השמאלית. בסיכומים השבועיים נצרף כאן גם קישורים למשימות, לאחר אימות המקור המתאים.</p>
          <div class="teacher-warning"><strong>חשוב מאוד למורה:</strong> אין לשלוח לתלמידים את הקישור שמופיע בפריסה. יש להיכנס למרחב ה־Moodle של קבוצת הלימוד ולשלוח לתלמידים את הקישור מתוך המרחב של המורה. רק כך ניתן לעקוב אחר התקדמות התלמידים, לראות מי נכנס למשימה ומי הגיש אותה.</div>
        </article>
        <article class="moodle-guide assessment-guide">
          <span class="guide-kicker">משימות הערכה</span>
          <h3>איפה רואים את מועדי משימות ההערכה?</h3>
          <p>מתחת לפריסות נמצאות <strong>טבלאות משימות ההערכה</strong>. בטבלאות מופיעים חלונות הזמן שבהם כל שכבה מבצעת את משימת ההערכה. כדאי לבדוק את הטבלה הרלוונטית לשכבה לפני תכנון ההוראה וההגשה.</p>
        </article>
      </div>

      <div class="october-required">
        <p class="eyebrow">משימות החובה לתקופת אוקטובר</p>
        <h3>איזו משימת חובה צריך להגיש בכל שכבה?</h3>
        <div class="required-task-grid">
          <article><span class="grade-pill">שכבת ז׳</span><h4>גיימינג־אפ</h4><p>מערכת הצירים ומספרים חיוביים.</p><p class="task-link-note">הקישור המאומת למשימה יצורף כאן לאחר שנקשר אותו למקור שתפנה אליו.</p></article>
          <article><span class="grade-pill">שכבת ח׳</span><h4>ציור קיר</h4><p>יחס, פרופורציה וקנה מידה.</p><p class="task-link-note">הקישור המאומת למשימה יצורף כאן לאחר שנקשר אותו למקור שתפנה אליו.</p></article>
        </div>
      </div>

      <div class="assessment-dates">
        <p class="eyebrow">מועדי משימות ההערכה</p>
        <h3>מתי מתקיימת משימת ההערכה בכל שכבה?</h3>
        <div class="assessment-date-grid">
          <article><span class="grade-pill">שכבת ח׳</span><strong dir="ltr">25.10–06.11.2026</strong><p>חלון משימת ההערכה כפי שמופיע כעת בלוח המועדים של הסיכום.</p></article>
          <article><span class="grade-pill">שכבת ז׳</span><strong dir="ltr">01.11–13.11.2026</strong><p>חלון משימת ההערכה כפי שמופיע כעת בלוח המועדים של הסיכום.</p></article>
        </div>
      </div>
    </div>
  </section>

  <section class="sheet workbooks-page" id="workbooks">'''

s = s[:m.start()] + '\n' + new + s[m.end():]

marker = '/* moodle-tasks-guidance-2026-10-16 */'
if marker not in styles:
    styles += '''\n\n/* moodle-tasks-guidance-2026-10-16 */
.moodle-guidance-grid,.required-task-grid,.assessment-date-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:24px}
.moodle-guide,.october-required,.assessment-dates{position:relative;border:1px solid rgba(108,84,167,.18);border-radius:24px;background:rgba(255,255,255,.94);box-shadow:0 14px 32px rgba(87,62,140,.08)}
.moodle-guide{padding:22px}.moodle-guide h3,.october-required h3,.assessment-dates h3{margin:6px 0 10px;color:#4d3e82}.moodle-guide p,.october-required p,.assessment-dates p{line-height:1.72;color:#536a7d}
.guide-kicker,.grade-pill{display:inline-flex;align-items:center;min-height:30px;padding:5px 10px;border-radius:999px;font:800 .76rem/1.2 "Rubik",Arial,sans-serif}
.mandatory-guide .guide-kicker{background:#fff0c9;color:#835711}.assessment-guide .guide-kicker{background:#e8f2ff;color:#205f94}
.teacher-warning{margin-top:16px;padding:16px 18px;border-radius:18px;background:linear-gradient(135deg,#fff5db,#fffaf0);border:1px solid rgba(190,132,32,.24);color:#6d4d14;line-height:1.7}
.teacher-warning strong{color:#8a5d09}.october-required,.assessment-dates{margin-top:18px;padding:22px}.required-task-grid,.assessment-date-grid{margin-top:14px}
.required-task-grid article,.assessment-date-grid article{padding:18px;border-radius:18px;background:#fff;border:1px solid rgba(108,84,167,.14)}
.required-task-grid article:nth-child(1) .grade-pill,.assessment-date-grid article:nth-child(2) .grade-pill{background:#e7f7ff;color:#176e98}
.required-task-grid article:nth-child(2) .grade-pill,.assessment-date-grid article:nth-child(1) .grade-pill{background:#fff0d4;color:#8b5b13}
.required-task-grid h4{margin:12px 0 6px;color:#304f67;font-size:1.22rem}.task-link-note{margin-top:12px!important;padding-top:12px;border-top:1px dashed #d8d3e7;font-size:.92rem}
.assessment-date-grid strong{display:block;margin-top:12px;color:#3f356d;font:900 1.25rem/1.2 "Rubik",Arial,sans-serif}
@media(max-width:720px){.moodle-guidance-grid,.required-task-grid,.assessment-date-grid{grid-template-columns:1fr;gap:12px}.moodle-guide,.october-required,.assessment-dates{border-radius:20px}.moodle-guide,.october-required,.assessment-dates,.required-task-grid article,.assessment-date-grid article{padding:18px}.teacher-warning{padding:14px 15px;border-radius:16px}}
'''

for token in [
    'משימות חובה ומשימות הערכה',
    'הפריסות',
    'בעמודה השמאלית',
    'אין לשלוח לתלמידים את הקישור שמופיע בפריסה',
    'טבלאות משימות ההערכה',
    '25.10–06.11.2026',
    '01.11–13.11.2026',
    'גיימינג־אפ',
    'ציור קיר',
    'id="workbooks"'
]:
    if token not in s:
        raise SystemExit('missing token: ' + token)
if marker not in styles:
    raise SystemExit('CSS marker missing')

p.write_text(s, encoding='utf-8')
cssp.write_text(styles, encoding='utf-8')
print('Moodle tasks guidance updated')
