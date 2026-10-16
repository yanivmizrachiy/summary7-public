from pathlib import Path

hp=Path('index.html')
cp=Path('styles.css')
html=hp.read_text(encoding='utf-8')
css=cp.read_text(encoding='utf-8')

start=html.find('<section class="lux-hero"')
end=html.find('</section><section class="intro-section">', start)
if start<0 or end<0:
    raise SystemExit('ABORT: current cover boundaries not found')
end += len('</section>')

cover='''<section class="modern-cover" aria-label="שער סיכום שבועי 7">
  <div class="modern-cover-grid">
    <div class="modern-date-row"><span dir="ltr">16.10.2026</span><span dir="rtl">בס״ד · יום שישי · תשפ״ז</span></div>
    <div class="modern-logo-orbit"><img src="assets/logo.png" alt="לוגו מחוז ירושלים" class="modern-logo" width="94" height="94"></div>
    <h1>סיכום שבועי</h1>
    <div class="modern-edition">סיכום מס׳ <b>7</b></div>
    <p class="modern-district">הדרכה במחוז ירושלים והעיר ירושלים – מנח״י, בהובלת איילת קריספין</p>
    <div class="modern-author"><img src="https://jerusalem2.vercel.app/media/team/yaniv.jpg" alt="יניב רז"><div class="modern-author-copy"><p class="modern-author-name">יניב רז</p><div class="modern-author-role">מדריך מחוזי חט״ב בעיר ירושלים</div></div></div>
  </div>
</section>'''

html=html[:start]+cover+html[end:]

marker='/* modern-cover-v1 */'
if marker not in css:
    css += '''\n\n/* modern-cover-v1 — aligned with latest weekly-summary cover language */
.modern-cover{position:relative;min-height:min(920px,92svh);display:grid;place-items:center;overflow:hidden;border-radius:28px;background:radial-gradient(circle at 16% 12%,rgba(70,213,255,.21),transparent 22%),radial-gradient(circle at 86% 18%,rgba(215,170,66,.17),transparent 23%),linear-gradient(145deg,#fff 0,#f5fbff 60%,#fff9eb 100%);box-shadow:0 24px 70px rgba(7,27,45,.17)}
.modern-cover:before{content:"";position:absolute;inset:18px;border:1px solid rgba(20,87,143,.13);border-radius:24px}
.modern-cover-grid{position:relative;z-index:2;width:min(100%,720px);padding:34px 26px;display:grid;justify-items:center;text-align:center;gap:18px}
.modern-date-row{width:100%;display:flex;justify-content:space-between;gap:12px;color:#698094;font:700 .84rem/1.3 "Rubik",Arial,sans-serif;direction:ltr}
.modern-date-row span:last-child{direction:rtl}
.modern-logo-orbit{position:relative;width:112px;height:112px;display:grid;place-items:center}
.modern-logo-orbit:before{content:"";position:absolute;inset:-7px;border-radius:50%;border:1.5px solid rgba(20,87,143,.20);border-top-color:#d7aa42}
.modern-logo{width:94px;height:94px;border-radius:50%;object-fit:cover;background:#fff;box-shadow:0 12px 30px rgba(31,78,118,.15)}
.modern-cover h1{margin:0;color:#14578f;font:900 clamp(3rem,9vw,5.4rem)/.96 "Frank Ruhl Libre",serif}
.modern-edition{color:#47647b;font:800 clamp(1rem,2.8vw,1.3rem)/1.3 "Rubik",Arial,sans-serif}
.modern-edition b{display:inline-grid;place-items:center;width:42px;height:42px;border:1px solid rgba(215,170,66,.7);border-radius:50%;color:#8d6d1b;background:#fff}
.modern-district{max-width:610px;margin:0;color:#526d82;font:600 clamp(.98rem,2.6vw,1.2rem)/1.7 "Rubik",Arial,sans-serif}
.modern-author{display:flex;align-items:center;gap:15px;padding-top:18px;border-top:1px solid rgba(20,87,143,.11);width:min(100%,460px);justify-content:center}
.modern-author img{width:82px;height:82px;border-radius:50%;object-fit:cover;border:3px solid #fff;box-shadow:0 8px 24px rgba(9,40,66,.19)}
.modern-author-copy{text-align:right}.modern-author-name{margin:0;color:#214f76;font:800 1.55rem/1.2 "Frank Ruhl Libre",serif}.modern-author-role{margin-top:4px;color:#687f91;font:600 .95rem/1.45 "Rubik",Arial,sans-serif}
@media(max-width:640px){.modern-cover{min-height:100svh;border-radius:0;box-shadow:none}.modern-cover:before{inset:10px;border-radius:18px}.modern-cover-grid{padding:24px 18px;gap:14px}.modern-date-row{font-size:.76rem}.modern-logo-orbit{width:88px;height:88px}.modern-logo{width:72px;height:72px}.modern-cover h1{font-size:clamp(3rem,15vw,4.4rem)}.modern-district{font-size:1rem}.modern-author{width:100%;gap:12px}.modern-author img{width:74px;height:74px}.modern-author-name{font-size:1.45rem}.modern-author-role{font-size:.9rem}}
@media(min-width:641px){.modern-cover{aspect-ratio:210/297}}
@media print{.modern-cover{width:210mm;height:297mm;min-height:0;border-radius:0;box-shadow:none;page-break-after:always}.modern-cover:before{inset:18mm}.modern-cover-grid{padding:28mm 20mm}}
'''

for required in ['<section class="modern-cover"','סיכום מס׳ <b>7</b>','יניב רז','id="courses"','id="teaching"']:
    if required not in html:
        raise SystemExit('ABORT: required content missing: '+required)

hp.write_text(html,encoding='utf-8')
cp.write_text(css,encoding='utf-8')
print('modern cover applied')
