from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='id="tnufa-2026"'
if marker not in s:
    block='''\n  <section class="sheet tnufa-page" id="tnufa-2026">\n    <div class="sheet-inner tnufa-inner">\n      <p class="eyebrow tnufa-eyebrow">לקראת מבחן תנופה · כיתה ט׳</p>\n      <h2>מבחן תנופה במתמטיקה</h2>\n      <div class="tnufa-date">\n        <strong>יום רביעי · 25.11.2026</strong>\n        <span>ט״ו בכסלו תשפ״ז · משך הבחינה: 90 דקות</span>\n      </div>\n      <div class="tnufa-copy">\n        <p>באתר המחוז ריכזנו עבורכם את כל המידע לקראת מבחן תנופה במתמטיקה לכיתה ט׳.</p>\n        <p><strong>באתר תמצאו את נושאי המבחן, חומרי הכנה ותרגול, מבחנים לדוגמה, קישורים רשמיים וכל הפרטים המעודכנים.</strong></p>\n      </div>\n      <div class="tnufa-actions">\n        <a href="https://jerusalem2.vercel.app/chativat-beynayim/t/collections/t-mivchanim/tnufa/" target="_blank" rel="noopener noreferrer">לכל הפרטים והחומרים באתר המחוז ←</a>\n      </div>\n    </div>\n  </section>\n'''
    # place after grade pages and before science/news pages
    anchor='  <section class="sheet science-a4-page"'
    if anchor not in s:
        raise SystemExit('science page anchor not found')
    s=s.replace(anchor, block+'\n'+anchor, 1)
    p.write_text(s,encoding='utf-8')

cssp=Path('styles.css')
css=cssp.read_text(encoding='utf-8')
css_marker='/* tnufa-green-a4 */'
if css_marker not in css:
    css += r'''

/* tnufa-green-a4 */
.tnufa-page{
  background:
    radial-gradient(circle at 84% 12%,rgba(79,191,129,.22),transparent 28%),
    radial-gradient(circle at 10% 88%,rgba(20,120,86,.16),transparent 30%),
    linear-gradient(145deg,#effcf3 0%,#f8fff9 52%,#e4f7ec 100%);
}
.tnufa-page:before{content:"";position:absolute;inset:20px;border:1px solid rgba(30,126,82,.18);border-radius:26px;pointer-events:none}
.tnufa-inner{position:relative;z-index:1;display:grid;align-content:start;gap:22px;padding-top:clamp(34px,5vw,58px)!important}
.tnufa-eyebrow{color:#287f58}
.tnufa-page h2{color:#176b49;margin-bottom:0}
.tnufa-date{display:grid;gap:6px;padding:18px 20px;border-radius:20px;background:rgba(255,255,255,.86);border:1px solid rgba(37,137,89,.18);box-shadow:0 12px 30px rgba(25,102,67,.09)}
.tnufa-date strong{color:#145d41;font:900 clamp(1.35rem,3.5vw,2rem)/1.2 "Rubik",Arial,sans-serif}
.tnufa-date span{color:#4b6f60;font-weight:700}
.tnufa-copy{padding:24px;border-radius:22px;background:rgba(255,255,255,.9);border:1px solid rgba(37,137,89,.14)}
.tnufa-copy p{color:#3f6254;line-height:1.8;font-size:1.05rem}
.tnufa-copy p:last-child{margin-bottom:0}
.tnufa-actions a{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:13px 20px;border-radius:999px;background:linear-gradient(135deg,#176b49,#2f9a68);color:#fff;text-decoration:none;font:900 .96rem "Rubik",Arial,sans-serif;box-shadow:0 10px 24px rgba(23,107,73,.2)}
@media(max-width:720px){
  .tnufa-inner{padding:24px 16px!important;gap:16px}
  .tnufa-page h2{font-size:2rem!important}
  .tnufa-date{padding:16px}
  .tnufa-copy{padding:18px}
  .tnufa-actions a{width:100%;white-space:normal;text-align:center}
}
@media print{
  .tnufa-page{break-before:page;break-after:page;page-break-before:always;page-break-after:always}
}
'''
    cssp.write_text(css,encoding='utf-8')
print('tnufa page ready')
