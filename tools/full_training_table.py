from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

rows = [
('קהילת רכזי מתמטיקה','רכזי מתמטיקה בחטיבת הביניים','13.10.2026 — לפי סילבוס; נדרש אימות מחזור','8 מפגשים לפי הסילבוס; מועדים מלאים דורשים אימות','טרם אומת סופית','טרם אומת סופית','201020','https://drive.google.com/file/d/1QHYojSXEUtFHHtRDhhAb9guiXE4tF-oR/view','טרם אומת קישור הרשמה ישיר','מצפן וסילבוס אומתו; לוח המפגשים דורש אימות מחזור'),
('בינה מלאכותית ו־MOODLE בהוראת המתמטיקה ז׳–ח׳ — יישום עדכון ת״ל','מורי מתמטיקה ז׳–ח׳','28.10.2026 — פתיחה במסגרת יום העיון','המשך מפגשים מופיע בסילבוס; פירוט מלא דורש הצלבה','טרם אומת סופית','טרם אומת סופית','201590','https://drive.google.com/file/d/1MPTDPrM6no1dOwKkayU4RSEpfFDbijTH/view','טרם אומת קישור הרשמה ישיר','מצפן, סילבוס ומפגש פתיחה זוהו; יתר הפרטים בהצלבה'),
('הוראת התלמיד המתקשה בכיתתו וחנ״מ','מורי מתמטיקה בחטיבת הביניים וחינוך מיוחד','28.10.2026 — לפי הסילבוס','10 מפגשים לפי הסילבוס; רוב המפגשים 19:00–21:30','טרם אומת סופית','טרם אומת סופית','201530','https://drive.google.com/file/d/1aVlPA5UMQfbSIAmPs0bhoCsPJ86VStGe/view','טרם אומת קישור הרשמה ישיר','מצפן וסילבוס אומתו; פרטי מנחה/היקף דורשים אימות'),
('הוראת המתמטיקה בכיתות ט׳ — בדגש לקראת 4 ו־5 יח״ל','מורי כיתות ט׳, בדגש לקראת 4–5 יח״ל','13.10.2026 · 19:00–21:30','10 מפגשים · ימי ג׳ · 13.10.2026–16.02.2027','30 שעות','עידן אחוון / ויקטוריה צורי — כתיב השם דורש אימות סופי','201041','https://drive.google.com/file/d/14ybA9ao125SbMv4yqwa_u0inSpCcMQh-/view','טרם אומת קישור הרשמה ישיר','מועד, שעות, היקף וסילבוס אומתו במקור'),
('גיאומטריה מהשטח — מהמחשה פיזית להבנה מתמטית','מורי מתמטיקה בחטיבת הביניים','28.10.2026 · 15:00–19:00 · פסג״ה מודיעין','9 מפגשים לפי הסילבוס','טרם אומת סופית','איילת קריספין — לפי תיעוד המקור','204781','https://drive.google.com/file/d/1FTEh4Lt5sBqd1kHF_riunRx6m4IjdxlS/view','טרם אומת קישור הרשמה ישיר','204781 הוא עדכון מאוחר לעומת עלון ישן שבו נכתב ״בקרוב״'),
]

def td(label, val):
    return f'<td data-label="{label}">{val}</td>'

body=[]
for name,aud,first,sched,hours,fac,code,syll,reg,ver in rows:
    body.append('<tr>'+td('השתלמות',f'<strong>{name}</strong>')+td('קהל יעד',aud)+td('מפגש ראשון',first)+td('מועדים / שעות',sched)+td('היקף',hours)+td('מנחה',fac)+td('מצפן',f'<b dir="ltr">{code}</b>')+td('סילבוס',f'<a href="{syll}" target="_blank" rel="noopener noreferrer">פתיחת סילבוס ↗</a>')+td('הרשמה',reg)+td('סטטוס אימות',ver)+'</tr>')

section = '''<section id="courses"><h2>השתלמויות לחטיבת הביניים</h2><p class="training-note">כל השדות נשמרים גם בנייד. פרטים שלא אומתו מסומנים במפורש ולא הושלמו בהשערה.</p><div class="training-wrap"><table class="training-table"><thead><tr><th>השתלמות</th><th>קהל יעד</th><th>מפגש ראשון</th><th>מועדים / שעות</th><th>היקף</th><th>מנחה</th><th>מצפן</th><th>סילבוס</th><th>הרשמה</th><th>סטטוס אימות</th></tr></thead><tbody>''' + ''.join(body) + '''</tbody></table></div><p class="training-warning"><strong>2014777:</strong> לא פורסם עד הכרעה בסתירה בין המקורות.</p></section>'''

s, n = re.subn(r'<section id="courses">.*?</section>', section, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('courses section not found')

css='''\n/* full-training-table-v2 */\n.training-note,.training-warning{color:#5b6f7f;font-size:14px}.training-warning{margin-top:12px}.training-table{min-width:1100px}.training-table th,.training-table td{overflow-wrap:anywhere}\n@media(max-width:700px){#courses .training-wrap{overflow:visible!important;border:0!important;box-shadow:none!important}#courses .training-table{display:block!important;min-width:0!important;width:100%!important;border:0!important;background:transparent!important}#courses .training-table thead{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important}#courses .training-table tbody{display:block!important}#courses .training-table tbody tr{display:block!important;width:100%!important;margin:0 0 14px!important;padding:14px!important;border:1px solid #cfdeea!important;border-radius:15px!important;background:#fff!important;box-shadow:0 5px 16px #0e314b12!important}#courses .training-table tbody td{display:grid!important;grid-template-columns:minmax(105px,38%) minmax(0,1fr)!important;gap:9px!important;width:100%!important;padding:9px 0!important;border-bottom:1px solid #e5edf3!important;font-size:13px!important;white-space:normal!important}#courses .training-table tbody td:last-child{border-bottom:0!important}#courses .training-table tbody td:before{content:attr(data-label)!important;font-weight:800!important;color:#365b74!important}#courses .training-table tbody td strong{font-size:15px!important}}\n'''
if '/* full-training-table-v2 */' not in s:
    s=s.replace('</style>',css+'</style>',1)

p.write_text(s,encoding='utf-8')
print('Updated full 10-column training table')
