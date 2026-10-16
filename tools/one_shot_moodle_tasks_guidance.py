from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

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

p.write_text(s, encoding='utf-8')
print('Moodle tasks guidance updated')
