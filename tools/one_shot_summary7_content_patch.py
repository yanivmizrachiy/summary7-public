from pathlib import Path

html_path = Path('index.html')
css_path = Path('styles.css')
html = html_path.read_text(encoding='utf-8')
css = css_path.read_text(encoding='utf-8')

# Teaching headings
html = html.replace('<h2>מה אנחנו מלמדים?</h2>', '<h2>מה אנחנו מלמדים באוקטובר</h2>')
html = html.replace('<section class="sheet grade-page grade-7" id="grade-7"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>', '<section class="sheet grade-page grade-7" id="grade-7"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים באוקטובר · שכבת ז׳</p>')
html = html.replace('<section class="sheet grade-page grade-8" id="grade-8"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>', '<section class="sheet grade-page grade-8" id="grade-8"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים באוקטובר · שכבת ח׳</p>')
html = html.replace('<section class="sheet grade-page grade-9-high" id="grade-9-high"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>', '<section class="sheet grade-page grade-9-high" id="grade-9-high"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים באוקטובר · שכבת ט׳ רגילה</p>')
html = html.replace('<section class="sheet grade-page grade-9-three" id="grade-9-three"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים? · אוקטובר</p>', '<section class="sheet grade-page grade-9-three" id="grade-9-three"><div class="sheet-inner grade-page-inner"><p class="eyebrow">מה אנחנו מלמדים באוקטובר · שכבת ט׳ מצומצמת</p>')

# Conference registration
old_conf = '<article><time>17.11.2026</time><div><strong>כנס רכזים</strong><span>14:30–19:00 · פסג״ה מודיעין</span></div></article>'
new_conf = '<article><time>17.11.2026</time><div><strong>כנס רכזים</strong><span>14:30–19:00 · פסג״ה מודיעין</span><p class="event-register-note">למי שעדיין לא נרשם: יש למלא את טופס ההרשמה, ובנוסף להירשם גם במצפן.</p><a class="event-register-link" href="https://forms.gle/gj1cjouKDD5cD3WdA" target="_blank" rel="noopener noreferrer">הרשמה לכנס</a></div></article>'
if old_conf in html:
    html = html.replace(old_conf, new_conf)

# Science in the classroom 2027 WhatsApp-like news card
science_marker = 'https://qrco.de/bh31gu'
if science_marker not in html:
    anchor = '<div class="story-list">'
    science = '''<div class="story-list"><article class="story whatsapp-story science-story"><div class="whatsapp-label">🔬 תוכנית מיוחדת לכיתות ט׳</div><h3>מדע בכיתה 2027 יוצאת לדרך!</h3><p><strong>מזמינים אתכם להצטרף לתוכנית מדע בכיתה</strong>, המיועדת לתלמידי ותלמידות כיתות ט׳, במסגרת מרתון ישראל ריאלית — ינואר 2027.</p><p>התוכנית מפגישה את התלמידים עם אנשי ונשות מקצוע מעולמות המדע, הטכנולוגיה, האקדמיה ומערכת הביטחון למפגש השראה, רגע לפני בחירת המגמות.</p><p>במפגש אישי ובגובה העיניים, התלמידים יכירו את החיבור בין מקצועות ה־STEM לעשייה בתעשייה ובמחקר, וישמעו על מסלולי קריירה ועל הדרך האישית והמקצועית של העוסקים בתחומים אלה.</p><div class="link-row"><a class="science-register" href="https://qrco.de/bh31gu" target="_blank" rel="noopener noreferrer">🔗 לפרטים נוספים ולהרשמה לתוכנית</a></div></article>'''
    if anchor not in html:
        raise SystemExit('news story list marker missing')
    html = html.replace(anchor, science, 1)

# Styles for top date, conference link and WhatsApp-like science card
marker = '/* summary7-content-polish-2026-10-16 */'
if marker not in css:
    css += '''\n\n/* summary7-content-polish-2026-10-16 */
.cover-inner{min-height:92svh;align-content:center}
.date-row{position:absolute;top:28px;inset-inline:28px;width:auto}
.event-register-note{margin:8px 0 10px;color:#5e7180;line-height:1.55}
.event-register-link{display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:8px 14px;border-radius:999px;background:linear-gradient(135deg,var(--blue),#2787c9);color:#fff;text-decoration:none;font-weight:800}
.whatsapp-story{border:1px solid rgba(36,170,92,.28);background:linear-gradient(145deg,#f4fff7,#fff 58%,#eefbf2);box-shadow:0 16px 36px rgba(31,126,72,.10)}
.whatsapp-story:before{content:"";position:absolute;inset-inline-start:0;top:0;bottom:0;width:5px;background:linear-gradient(#25d366,#128c7e)}
.whatsapp-label{display:inline-flex;align-items:center;min-height:32px;padding:6px 11px;margin-bottom:10px;border-radius:999px;background:#e7f9ed;color:#167446;font:800 .78rem/1.2 "Rubik",Arial,sans-serif}
.science-story h3{color:#17613d;font-size:clamp(1.45rem,3vw,2rem)}
.science-story p{color:#3f6250}
.science-register{background:linear-gradient(135deg,#128c7e,#25d366)!important;box-shadow:0 10px 22px rgba(18,140,126,.22)!important}
@media(max-width:720px){.cover-inner{min-height:100svh;padding-top:76px}.date-row{top:18px;inset-inline:17px}.event-register-link,.science-register{width:100%}.whatsapp-story{padding:18px!important}}
@media print{.grade-page{break-before:page;break-after:page;min-height:297mm}.date-row{position:static;width:100%}.cover-inner{min-height:0}}
'''

required = [
    'מה אנחנו מלמדים באוקטובר',
    'מה אנחנו מלמדים באוקטובר · שכבת ז׳',
    'מה אנחנו מלמדים באוקטובר · שכבת ח׳',
    'מה אנחנו מלמדים באוקטובר · שכבת ט׳ רגילה',
    'מה אנחנו מלמדים באוקטובר · שכבת ט׳ מצומצמת',
    'https://qrco.de/bh31gu',
    'https://forms.gle/gj1cjouKDD5cD3WdA',
    'להירשם גם במצפן',
]
for token in required:
    if token not in html:
        raise SystemExit(f'missing required token: {token}')

html_path.write_text(html, encoding='utf-8')
css_path.write_text(css, encoding='utf-8')
print('Summary 7 content patch complete')
