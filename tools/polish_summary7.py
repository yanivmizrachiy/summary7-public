from pathlib import Path
import re

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# Repair accidental nested/duplicated style tags left by earlier incremental edits.
for bad, good in [
    ('<style>\n<style>', '<style>'),
    ('<style><style>', '<style>'),
    ('</style></style>', '</style>'),
]:
    while bad in html:
        html = html.replace(bad, good)

# Remove previous version of this override so the script is idempotent.
html = re.sub(r'<style id="summary7-premium-v4">.*?</style>', '', html, flags=re.S)

# Typography + browser chrome metadata.
font_link = '<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@500;700;900&family=Rubik:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
html = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Frank\+Ruhl\+Libre[^>]+>', font_link, html, count=1)
if 'name="theme-color"' not in html:
    html = html.replace('<meta name="viewport" content="width=device-width,initial-scale=1">', '<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071a2f"><meta name="color-scheme" content="light">', 1)

# The public bulletin itself must not depend on a Vercel-hosted portrait asset.
html = re.sub(r'<img src="https://jerusalem2\.vercel\.app/media/team/yaniv\.jpg"[^>]*>', '', html)

if 'class="skip-link"' not in html:
    html = html.replace('<body><main>', '<body><a class="skip-link" href="#green-page">דלגו לתוכן</a><main>', 1)

css = r'''
<style id="summary7-premium-v4">
/* SUMMARY 7 — premium editorial system v4. Content is untouched; this layer only improves presentation, accessibility and performance. */
:root{
  --s7-night:#071a2f;--s7-navy:#0d2d4b;--s7-blue:#1f5f8d;--s7-sky:#dcecf7;
  --s7-gold:#c99c55;--s7-gold-soft:#ecd3a4;--s7-ink:#102b42;--s7-muted:#5b7082;
  --s7-paper:#fffdf8;--s7-line:#dce5eb;--s7-shadow:0 22px 60px rgba(7,26,47,.12);
  --s7-radius:24px;--s7-font:"Rubik","Segoe UI",Arial,sans-serif;--s7-serif:"Frank Ruhl Libre",Georgia,serif;
}
html{scroll-behavior:smooth;background:#eaf0f5}
body{margin:0;background:
  radial-gradient(circle at 12% 6%,rgba(201,156,85,.10),transparent 25rem),
  linear-gradient(145deg,#e9f0f5 0,#f7f9fb 46%,#e5edf3 100%);
  color:var(--s7-ink);font-family:var(--s7-font);font-size:16px;line-height:1.75;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}
main{width:min(1160px,calc(100% - 32px));max-width:none;margin:18px auto 56px;padding:0 54px 70px;background:#fff;box-shadow:0 28px 90px rgba(16,43,66,.14);border:1px solid rgba(16,43,66,.06);overflow:hidden}
.skip-link{position:fixed;z-index:9999;top:10px;right:10px;transform:translateY(-160%);background:#fff;color:#071a2f;padding:10px 15px;border-radius:10px;box-shadow:var(--s7-shadow);font-weight:800}.skip-link:focus{transform:none}
::selection{background:#efd7aa;color:#071a2f}
a{text-underline-offset:3px}

/* Hero — high-contrast editorial cover, no neon, no washed-out type. */
main>.lux-hero{position:relative;isolation:isolate;min-height:720px;margin:0 -54px;padding:34px clamp(28px,5.5vw,72px) 28px;overflow:hidden;border-radius:0 0 34px 34px;color:#fff!important;background:
  radial-gradient(ellipse at 78% -4%,rgba(54,116,163,.42),transparent 40%),
  radial-gradient(ellipse at 0 100%,rgba(11,123,133,.26),transparent 36%),
  linear-gradient(135deg,#061426 0%,#0a2541 52%,#0d3858 100%)!important;
  box-shadow:0 22px 56px rgba(5,24,43,.26)}
main>.lux-hero:before{content:"";position:absolute;inset:16px;border:1px solid rgba(236,211,164,.42);border-radius:4px 4px 24px 24px;pointer-events:none;z-index:2}
main>.lux-hero:after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;opacity:.72;background:
  linear-gradient(118deg,transparent 0 48%,rgba(236,211,164,.11) 48.08% 48.18%,transparent 48.26%),
  radial-gradient(circle at 18% 78%,rgba(255,255,255,.07) 0 1px,transparent 1.5px) 0 0/24px 24px}
.hero-art{position:absolute;inset:0;z-index:-1;opacity:.8;pointer-events:none}.art-seven{color:rgba(255,255,255,.035)!important;text-shadow:none!important}.art-line{opacity:.42}.art-sun{opacity:.35}
.lux-top{position:relative;z-index:3;display:flex;align-items:center;justify-content:space-between;gap:20px}
.masthead{color:#fff!important;font-size:17px!important;font-weight:800;letter-spacing:.01em}.masthead small{color:#c6d7e4!important;font-size:12px!important;font-weight:500}.masthead-line{width:54px;height:3px;background:var(--s7-gold);margin-bottom:13px;box-shadow:none}
.lux-top img{width:80px;height:80px;object-fit:contain;background:#fff;border-radius:50%;padding:6px;border:2px solid #d7b16e;box-shadow:0 0 0 7px rgba(255,255,255,.07),0 12px 32px rgba(0,0,0,.32)}
.lux-body{position:relative;z-index:3;padding:68px 0 36px;max-width:830px}
.lux-eyebrow{display:flex;align-items:center;gap:11px;color:#d8e8f4!important;font-size:13px!important;font-weight:700;letter-spacing:.05em}.edition-dot{background:#e8bd72!important;box-shadow:0 0 0 5px rgba(232,189,114,.14)!important}.eyebrow-rule{background:rgba(232,189,114,.55)!important}
.lux-hero h1{display:flex!important;flex-direction:column;align-items:flex-start;margin:20px 0 22px!important;color:#fff!important;font-family:var(--s7-serif)!important;font-size:clamp(70px,10vw,120px)!important;font-weight:900!important;line-height:.92!important;letter-spacing:-.05em!important;text-shadow:0 8px 30px rgba(0,0,0,.24)!important}
.lux-hero h1 span{color:#fff!important}.lux-hero h1 em{color:#f0c77f!important;font-family:var(--s7-font)!important;font-size:.78em!important;font-weight:800!important;font-style:normal!important;letter-spacing:-.06em!important;margin-inline-start:16px!important;text-shadow:none!important}
.lux-subtitle{max-width:680px;margin:0 0 28px!important;padding-inline-start:18px;border-inline-start:3px solid #d9ad63;color:#f1f6fa!important;font-size:clamp(17px,2vw,21px)!important;line-height:1.65!important;font-weight:500}
.lux-chips{display:flex;flex-wrap:wrap;gap:9px}.lux-chips span{padding:7px 14px;border:1px solid rgba(217,232,243,.30);border-radius:999px;background:rgba(255,255,255,.06);color:#edf5fa!important;font-size:12px;font-weight:600;backdrop-filter:blur(5px)}
.hero-divider{position:relative;z-index:3;margin:4px 0 20px!important;color:#e0b66e!important}.hero-divider span{background:linear-gradient(90deg,rgba(224,182,110,.42),transparent)!important}
.shabbat-feature{position:relative;z-index:3;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(280px,.92fr)!important;align-items:center;gap:24px;padding:22px 26px!important;border:1px solid rgba(217,232,243,.23)!important;border-radius:18px!important;background:linear-gradient(120deg,rgba(255,255,255,.105),rgba(255,255,255,.045))!important;backdrop-filter:blur(14px) saturate(120%);box-shadow:0 18px 48px rgba(0,10,25,.26)!important;color:#fff!important}
.shabbat-info{display:flex;flex-direction:column;gap:3px}.shabbat-info strong{font-family:var(--s7-serif)!important;font-size:clamp(34px,4vw,43px)!important;color:#f0c77f!important;text-shadow:none!important}.shabbat-info>span{color:#f2f6f9!important;font-weight:600}.shabbat-clock{padding:13px 14px!important;border:1px solid rgba(236,211,164,.30)!important;border-radius:14px!important;background:linear-gradient(145deg,#0b2946,#103959)!important;box-shadow:inset 0 1px rgba(255,255,255,.09),0 11px 26px rgba(0,0,0,.23)!important;text-align:center}.clock-title{display:block;color:#cddce7!important;font-size:11px!important;font-weight:700;letter-spacing:.04em}.clock-digits{display:block;margin-top:5px;padding:7px 12px!important;border:0!important;border-radius:10px!important;background:rgba(2,15,29,.55)!important;box-shadow:inset 0 1px 10px rgba(0,0,0,.42)!important;color:#fff!important;font-family:ui-monospace,"SFMono-Regular",Consolas,monospace!important;font-size:clamp(31px,4.5vw,48px)!important;font-weight:800!important;letter-spacing:.045em!important;text-shadow:none!important;font-variant-numeric:tabular-nums}
.hero-bottom{position:relative;z-index:3;margin-top:21px!important;color:#bcd0df!important;font-size:10px!important;font-weight:600;letter-spacing:.07em}

/* Intro + navigation — compact, useful, never competes with the cover. */
.author-intro{display:block!important;margin:22px 0 0!important;padding:16px 20px!important;border:0!important;border-inline-start:4px solid var(--s7-gold)!important;border-radius:0 12px 12px 0!important;background:linear-gradient(90deg,#faf7ef,#fff)!important;box-shadow:none!important}.author-intro strong{font-family:var(--s7-serif);font-size:22px!important;color:#153a59!important}.author-intro img{display:none!important}
nav.quick{position:sticky;top:10px;z-index:50;display:flex;flex-wrap:wrap;gap:7px;margin:20px 0 6px!important;padding:8px;border:1px solid rgba(16,43,66,.08);border-radius:16px;background:rgba(255,255,255,.88);box-shadow:0 10px 28px rgba(16,43,66,.08);backdrop-filter:blur(14px) saturate(150%)}
nav.quick a{display:inline-flex;align-items:center;justify-content:center;min-height:38px;padding:7px 13px!important;border:1px solid transparent!important;border-radius:10px!important;background:transparent!important;color:#24465f!important;font-size:12px!important;font-weight:700!important;text-decoration:none!important;transition:background .18s ease,color .18s ease,transform .18s ease}
nav.quick a:hover{background:#edf4f8!important;color:#0b2d49!important;transform:translateY(-1px)}

/* Editorial chapters */
main>section:not(.lux-hero){content-visibility:auto;contain-intrinsic-size:500px;margin-top:58px;scroll-margin-top:78px}
main>section:not(.lux-hero)>h2{display:flex;align-items:center;gap:14px;margin:0 0 22px!important;color:#0c2c48!important;font-family:var(--s7-serif)!important;font-size:clamp(28px,3.7vw,39px)!important;font-weight:900!important;letter-spacing:-.025em!important;line-height:1.15!important}
main>section:not(.lux-hero)>h2:before{content:"";flex:0 0 5px;width:5px;height:34px;border-radius:6px;background:linear-gradient(#d4aa64,#b47b31)!important;box-shadow:none!important}
main>section:not(.lux-hero)>h2:after{content:"";height:1px;flex:1;background:linear-gradient(90deg,rgba(16,43,66,.16),transparent)}

/* Green A4 invitation — premium emerald stationery on screen, true A4 only in print. */
.green-page{max-width:none!important;min-height:0!important;padding:34px clamp(22px,4vw,42px)!important;border:1px solid #b6d8c0!important;border-radius:26px!important;background:
  radial-gradient(circle at 94% 8%,rgba(255,255,255,.75),transparent 18rem),
  linear-gradient(145deg,#eef8f0 0%,#fbfdf9 72%)!important;box-shadow:0 18px 48px rgba(25,81,48,.10)!important;overflow:hidden}
.green-page>h2{color:#164f32!important}.green-lead{max-width:720px;margin:0 auto 28px!important;color:#3f684f!important;font-size:16px!important;font-weight:600!important;text-align:center}
.green-actions{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:17px!important;margin-top:24px!important}.green-action{display:flex;flex-direction:column;justify-content:space-between;min-height:230px;padding:24px 20px!important;border:1px solid rgba(40,112,65,.15)!important;border-radius:18px!important;background:rgba(255,255,255,.82)!important;box-shadow:0 12px 28px rgba(23,78,43,.08)!important;text-align:center}.green-action h3{font-family:var(--s7-serif)!important;font-size:25px!important;color:#174d31!important}.green-action p{color:#557061!important;font-size:14px}.green-3d{width:100%;min-height:51px!important;padding:11px 14px!important;border:1px solid #17663b!important;border-radius:12px!important;background:linear-gradient(180deg,#2c9b5a,#1d7a46)!important;box-shadow:0 5px 0 #145b36,0 11px 22px rgba(22,86,49,.17)!important;color:#fff!important;font-size:14px!important;font-weight:800!important;text-decoration:none!important;transition:transform .16s ease,box-shadow .16s ease}.green-3d:hover{transform:translateY(-2px)!important;box-shadow:0 7px 0 #145b36,0 14px 26px rgba(22,86,49,.20)!important}.green-3d:active{transform:translateY(3px)!important;box-shadow:0 2px 0 #145b36!important}

/* Tables — real information first, refined visual rhythm. */
.training-wrap,.cal-wrap,.workbooks-table-wrap{overflow:auto;border:1px solid var(--s7-line);border-radius:18px;background:#fff;box-shadow:0 12px 34px rgba(14,49,75,.07)}
.training-table,.cal-table,.workbooks-table{width:100%;border-collapse:separate!important;border-spacing:0!important;background:#fff!important;font-size:14px!important}
.training-table thead th,.cal-table thead th,.workbooks-table thead th{position:relative;padding:15px 16px!important;border:0!important;border-bottom:1px solid #d5e0e8!important;background:#0d304f!important;color:#fff!important;font-size:12px!important;font-weight:700!important;letter-spacing:.02em!important;text-align:right!important}
.training-table tbody th,.training-table tbody td,.cal-table tbody td,.workbooks-table tbody th,.workbooks-table tbody td{padding:16px!important;border:0!important;border-bottom:1px solid #e5ebf0!important;background:#fff!important;color:#244056!important;vertical-align:top!important}
.training-table tbody tr:nth-child(even)>*,.cal-table tbody tr:nth-child(even)>*,.workbooks-table tbody tr:nth-child(even)>*{background:#f8fafb!important}.training-table tbody tr:hover>*,.cal-table tbody tr:hover>*,.workbooks-table tbody tr:hover>*{background:#f0f6fa!important}.training-table tbody tr:last-child>*,.cal-table tbody tr:last-child>*,.workbooks-table tbody tr:last-child>*{border-bottom:0!important}.training-table th[scope="row"],.workbooks-table th[scope="row"]{color:#102f49!important;font-weight:700!important}.training-table small{display:block;margin-top:5px;color:#6a7d8d;font-size:11px;line-height:1.45}.training-table a,.cal-table a{font-weight:700;color:#1b608f}.cal-date{font-weight:800;color:#173f5d!important}.cal-time{white-space:nowrap;font-variant-numeric:tabular-nums}

/* News — magazine cards, video keeps true aspect ratio. */
.weekly-updates{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px!important}.weekly-update{padding:25px!important;border:1px solid #dce5eb!important;border-radius:20px!important;background:linear-gradient(160deg,#fff,#f9fbfc)!important;box-shadow:0 12px 32px rgba(16,43,66,.07)!important}.weekly-update h3{margin:0 0 16px!important;color:#113c5c!important;font-family:var(--s7-serif)!important;font-size:25px!important;line-height:1.25!important}.weekly-update p{color:#506678}.weekly-update a{color:#155c8c;font-weight:700}.video-embed{margin:15px 0 0!important}.video-embed iframe{display:block;width:100%!important;aspect-ratio:16/9;height:auto!important;border:0;border-radius:14px;background:#0a2035;box-shadow:0 12px 28px rgba(7,26,47,.12)}.video-embed figcaption{margin-top:8px;color:#6b7e8d;font-size:12px}

/* Moodle — action panel, not a generic box. */
#moodle{position:relative;padding:30px 32px 28px!important;border:1px solid #c9dbe7!important;border-radius:22px!important;background:linear-gradient(135deg,#f0f7fb,#fbfdff)!important;box-shadow:0 14px 36px rgba(22,74,108,.08)!important;overflow:hidden}#moodle:after{content:"M";position:absolute;left:18px;bottom:-38px;font-family:var(--s7-serif);font-size:170px;font-weight:900;color:rgba(31,95,141,.045);pointer-events:none}#moodle>h2{position:relative;z-index:1}#moodle p,#moodle li{position:relative;z-index:1;color:#365369}#moodle strong,#moodle b{color:#143d5b}#moodle a{color:#135f91;font-weight:800}

/* Workbooks — tactile but restrained, no toy-like gradients. */
.workbooks-table tbody tr:nth-child(4n+1)>*{background:#fbf5e9!important}.workbooks-table tbody tr:nth-child(4n+2)>*{background:#f0f7fb!important}.workbooks-table tbody tr:nth-child(4n+3)>*{background:#f2f8f1!important}.workbooks-table tbody tr:nth-child(4n+4)>*{background:#f8f2f6!important}.workbook-3d-button{display:inline-flex!important;align-items:center;justify-content:center;gap:7px;min-height:43px;padding:9px 15px!important;border:1px solid #174c70!important;border-radius:10px!important;background:linear-gradient(180deg,#286f9f,#1d587f)!important;box-shadow:0 4px 0 #153f5c,0 8px 18px rgba(19,65,96,.14)!important;color:#fff!important;font-size:13px!important;font-weight:800!important;text-decoration:none!important;transition:transform .16s ease,box-shadow .16s ease}.workbook-3d-button:hover{transform:translateY(-2px);box-shadow:0 6px 0 #153f5c,0 11px 22px rgba(19,65,96,.18)!important}.workbook-3d-button:active{transform:translateY(2px);box-shadow:0 2px 0 #153f5c!important}

/* Teaching notebook — graph paper, rounded Hebrew, real selectable curriculum text. */
#teaching{position:relative!important;padding:32px clamp(18px,3.8vw,38px) 38px!important;border:1px solid #dbcdb9!important;border-radius:26px!important;background:
  linear-gradient(rgba(255,255,255,.80),rgba(255,255,255,.80)),
  linear-gradient(#cfe0ec 1px,transparent 1px),linear-gradient(90deg,#cfe0ec 1px,transparent 1px),#f8f3e8!important;background-size:auto,24px 24px,24px 24px,auto!important;box-shadow:0 18px 48px rgba(71,61,45,.10)!important;overflow:hidden!important}
#teaching:before{content:"x² + y² = r²   ·   y = mx + b   ·   a² + b² = c²"!important;display:block!important;margin:0 0 18px!important;padding:0!important;color:#476b8e!important;font-family:"Segoe Print","Bradley Hand",cursive!important;font-size:15px!important;font-style:italic!important;text-align:left!important;direction:ltr!important;letter-spacing:.02em!important;opacity:.82!important}
#teaching>h2{color:#163e61!important;transform:rotate(-.4deg)}#teaching .grades{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:20px!important}
#teaching .panel{position:relative!important;margin:0!important;padding:25px 23px 25px 38px!important;border:1px solid #bdced9!important;border-radius:7px 17px 15px 8px!important;background-color:rgba(255,253,247,.95)!important;background-image:linear-gradient(90deg,transparent 0,transparent 29px,rgba(211,102,102,.18) 30px,rgba(211,102,102,.18) 31px,transparent 32px),linear-gradient(#d7e6ef 1px,transparent 1px),linear-gradient(90deg,#d7e6ef 1px,transparent 1px)!important;background-size:100% 100%,24px 24px,24px 24px!important;box-shadow:4px 5px 0 #d4c5ad,0 12px 26px rgba(48,61,70,.10)!important;transform:rotate(-.35deg)!important;font-family:var(--s7-font)!important}
#teaching .panel:nth-child(even){transform:rotate(.35deg)!important}#teaching .panel:before{content:""!important;position:absolute!important;top:13px!important;bottom:13px!important;right:9px!important;width:9px!important;background:radial-gradient(circle at center,#ad9b84 3px,transparent 3.5px) center top/9px 38px repeat-y!important;opacity:.72!important}
#teaching .panel h3{display:inline-block!important;margin:0 0 13px!important;padding:2px 11px 3px!important;border:0!important;border-bottom:4px solid #e0b85f!important;background:#fff0aa!important;color:#173f60!important;font-family:var(--s7-font)!important;font-size:clamp(21px,2.6vw,27px)!important;font-weight:800!important;line-height:1.25!important;transform:rotate(-1deg)!important}#teaching .panel:nth-child(2) h3{background:#d9f1db!important;border-color:#83bd8d!important}#teaching .panel:nth-child(3) h3{background:#f4dce8!important;border-color:#dba5bf!important}#teaching .panel:nth-child(4) h3{background:#dce9f8!important;border-color:#9dbadd!important}
#teaching .panel h4{margin:16px 0 5px!important;color:#28547a!important;font-family:var(--s7-font)!important;font-size:18px!important;font-weight:800!important;text-decoration:underline wavy rgba(180,112,65,.7)!important;text-underline-offset:4px!important}#teaching .panel ul{margin:3px 0 12px!important;padding-inline-start:22px!important}#teaching .panel li{margin:5px 0!important;color:#263f52!important;font-family:var(--s7-font)!important;font-size:16px!important;font-weight:500!important;line-height:1.58!important}#teaching .panel li::marker{color:#bd7e35}

footer.weekly-footer{margin-top:60px!important;padding:24px 0 0!important;border-top:1px solid #dce5eb!important;color:#6b7d8c!important;font-size:12px!important}.weekly-signoff{display:flex;justify-content:space-between;align-items:center;gap:20px;margin-top:18px!important;padding-top:18px!important;border-top:1px solid #edf0f2!important;color:#284d67!important}.weekly-signoff strong{font-family:var(--s7-serif);font-size:19px;color:#163d5a}.weekly-signoff img{max-width:125px!important;max-height:58px!important}

/* Focus, motion and high-contrast preferences. */
:focus-visible{outline:3px solid #d29d48!important;outline-offset:4px!important}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{animation:none!important;transition:none!important}}
@media(prefers-contrast:more){body{color:#071a2f}.training-table tbody th,.training-table tbody td,.cal-table tbody td,.workbooks-table tbody th,.workbooks-table tbody td{border-bottom-color:#94a6b4!important}nav.quick{border-color:#7f94a4}.green-action,.weekly-update{border-color:#8196a5!important}}

/* Tablet / mobile — designed, not merely shrunk. */
@media(max-width:820px){
  main{width:100%;margin:0;padding:0 18px 42px;border:0;box-shadow:none}
  main>.lux-hero{min-height:0;margin:0 -18px;padding:26px 24px 22px;border-radius:0 0 24px 24px}.lux-hero:before{inset:10px;border-radius:0 0 18px 18px}.lux-top img{width:64px;height:64px}.masthead{font-size:14px!important}.masthead small{font-size:10px!important}.lux-body{padding:48px 0 30px}.lux-hero h1{font-size:clamp(55px,14vw,82px)!important}.lux-subtitle{font-size:16px!important}.shabbat-feature{grid-template-columns:1fr!important;padding:17px!important;gap:14px}.shabbat-info strong{font-size:34px!important}.clock-digits{font-size:clamp(30px,9vw,43px)!important}.hero-bottom{font-size:9px!important}
  nav.quick{top:6px;flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;scrollbar-width:none;margin-inline:-4px!important}nav.quick::-webkit-scrollbar{display:none}nav.quick a{flex:0 0 auto}
  main>section:not(.lux-hero){margin-top:42px;scroll-margin-top:68px}main>section:not(.lux-hero)>h2{font-size:30px!important}
  .green-actions,.weekly-updates,#teaching .grades{grid-template-columns:1fr!important}.green-action{min-height:0!important}
  .training-wrap,.cal-wrap,.workbooks-table-wrap{border-radius:15px}
  .training-table,.cal-table,.workbooks-table{min-width:720px}
  #moodle{padding:23px 20px!important}
  #teaching{padding:24px 13px 30px!important}#teaching .panel{padding:22px 18px 22px 31px!important;transform:none!important}#teaching .panel:nth-child(even){transform:none!important}
}
@media(max-width:480px){
  body{font-size:15px}main{padding-inline:14px}main>.lux-hero{margin-inline:-14px;padding-inline:20px}.lux-top img{width:58px;height:58px}.lux-hero h1{font-size:53px!important}.lux-chips{gap:6px}.lux-chips span{font-size:10px;padding:5px 9px}.lux-eyebrow{font-size:10px!important}.hero-bottom{gap:6px;flex-wrap:wrap}.author-intro{margin-top:16px!important}.author-intro strong{font-size:20px!important}
  main>section:not(.lux-hero)>h2{font-size:27px!important;gap:10px}main>section:not(.lux-hero)>h2:before{height:29px}.green-page{padding:25px 15px!important}.weekly-update{padding:20px!important}.workbook-3d-button{width:100%}
}

/* Print: A4, ink-safe, crisp. */
@page{size:A4;margin:12mm}
@media print{
  html,body{background:#fff!important}body{font:10.5pt/1.45 var(--s7-font)!important;color:#111!important}main{width:auto;max-width:none;margin:0;padding:0;border:0;box-shadow:none!important;overflow:visible}.skip-link,nav.quick{display:none!important}
  main>.lux-hero{min-height:0;margin:0 0 8mm;padding:9mm 8mm;border:1.5pt solid #173b58!important;border-radius:0!important;background:#fff!important;color:#102d47!important;box-shadow:none!important;break-inside:avoid}.lux-hero:before,.lux-hero:after,.hero-art{display:none!important}.lux-hero h1,.lux-hero h1 span,.masthead,.masthead small,.lux-subtitle,.lux-eyebrow,.hero-bottom{color:#102d47!important;text-shadow:none!important}.lux-hero h1 em,.shabbat-info strong{color:#805015!important}.lux-body{padding:8mm 0 5mm}.lux-chips span{color:#102d47!important;border-color:#9aabb8!important;background:#fff!important}.shabbat-feature{grid-template-columns:1fr 1fr!important;background:#f3f6f8!important;color:#102d47!important;box-shadow:none!important}.shabbat-info>span,.clock-title,.clock-digits{color:#102d47!important}.shabbat-clock,.clock-digits{background:#fff!important;box-shadow:none!important;border:1px solid #9aabb8!important}
  main>section:not(.lux-hero){content-visibility:visible;margin-top:7mm;break-inside:auto}.green-page{width:auto!important;min-height:0!important;break-before:page;break-after:page;box-shadow:none!important}.green-actions{grid-template-columns:1fr!important}.green-action{min-height:0!important;box-shadow:none!important}.green-3d,.workbook-3d-button{box-shadow:none!important;background:#fff!important;color:#123!important;border:1px solid #345!important}
  .training-wrap,.cal-wrap,.workbooks-table-wrap,.weekly-update,#moodle,#teaching{box-shadow:none!important}.training-table,.cal-table,.workbooks-table{min-width:0!important;font-size:9pt!important}.training-table thead th,.cal-table thead th,.workbooks-table thead th{background:#eef2f5!important;color:#111!important}.weekly-updates,#teaching .grades{grid-template-columns:1fr 1fr!important}.video-embed iframe{display:none!important}.video-embed:after{content:"סרטון זמין בגרסה הדיגיטלית";font-size:9pt}.weekly-signoff{break-inside:avoid}
}
</style>
'''

html = html.replace('</head>', css + '</head>', 1)
path.write_text(html, encoding='utf-8')
print('Premium v4 applied:', len(html), 'bytes')
