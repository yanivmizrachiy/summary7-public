from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

# Idempotent light-cover override. Content and document structure stay untouched.
html = re.sub(r'<style id="s7-light-cover-v1">.*?</style>', '', html, flags=re.S)

css = r'''
<style id="s7-light-cover-v1">
/* Summary 7 — luminous editorial cover. Presentation only; content is untouched. */
:root{--s7-cover-paper:#fbfaf6;--s7-cover-paper-2:#f4f0e7;--s7-cover-ink:#102d47;--s7-cover-muted:#5f7180;--s7-cover-gold:#b78a47;--s7-cover-line:#d9c49c}

main>.lux-hero,.weekly-cover{
  color:var(--s7-cover-ink)!important;
  background:
    radial-gradient(circle at 12% 10%,rgba(183,138,71,.13),transparent 24rem),
    radial-gradient(circle at 90% 82%,rgba(61,105,132,.08),transparent 27rem),
    linear-gradient(145deg,#fffefa 0%,var(--s7-cover-paper) 52%,var(--s7-cover-paper-2) 100%)!important;
  box-shadow:0 24px 64px rgba(16,45,71,.12)!important;
  border-bottom:1px solid rgba(183,138,71,.28)!important;
}
main>.lux-hero:before{
  inset:18px!important;border:1px solid rgba(183,138,71,.52)!important;border-radius:3px 3px 28px 28px!important;
}
main>.lux-hero:after{
  opacity:.62!important;background:
    linear-gradient(118deg,transparent 0 48%,rgba(183,138,71,.10) 48.08% 48.17%,transparent 48.25%),
    radial-gradient(circle at 18% 78%,rgba(16,45,71,.07) 0 1px,transparent 1.5px) 0 0/28px 28px!important;
}
.weekly-cover:before{border-color:rgba(183,138,71,.26)!important;box-shadow:0 0 0 48px rgba(183,138,71,.04),0 0 0 100px rgba(183,138,71,.025)!important}
.cover-frame{border-color:rgba(183,138,71,.58)!important}
.cover-frame:before,.cover-frame:after{border-color:var(--s7-cover-gold)!important}
.cover-rule,.masthead-line{background:var(--s7-cover-gold)!important}

.hero-art{opacity:.42!important}.art-seven{color:rgba(16,45,71,.035)!important}.art-line{opacity:.18!important}.art-sun{opacity:.16!important}

.masthead,.cover-district{color:var(--s7-cover-ink)!important}
.masthead small,.cover-lead,.cover-lead-name,.cover-series,.hero-bottom,.cover-bottom{color:var(--s7-cover-muted)!important}
.lux-top img,.cover-emblem{background:#fff!important;border-color:#c9a363!important;box-shadow:0 0 0 7px rgba(183,138,71,.07),0 14px 34px rgba(16,45,71,.12)!important}

.lux-body{max-width:850px!important}
.lux-eyebrow{color:#516b80!important}.edition-dot{background:var(--s7-cover-gold)!important;box-shadow:0 0 0 5px rgba(183,138,71,.11)!important}.eyebrow-rule{background:rgba(183,138,71,.48)!important}
.lux-hero h1,.lux-hero h1 span,.weekly-cover h1{color:var(--s7-cover-ink)!important;text-shadow:none!important}
.lux-hero h1 em,.cover-number{color:#a87834!important;text-shadow:none!important}
.lux-subtitle{color:#334f65!important;border-inline-start-color:var(--s7-cover-gold)!important;font-weight:500!important}
.lux-chips span{border-color:rgba(16,45,71,.13)!important;background:rgba(255,255,255,.72)!important;color:#355268!important;box-shadow:0 5px 18px rgba(16,45,71,.04)!important}
.hero-divider{color:var(--s7-cover-gold)!important}.hero-divider span{background:linear-gradient(90deg,rgba(183,138,71,.48),transparent)!important}

.shabbat-feature{
  border:1px solid rgba(183,138,71,.30)!important;
  background:rgba(255,255,255,.72)!important;
  backdrop-filter:blur(16px) saturate(120%);
  box-shadow:0 18px 46px rgba(16,45,71,.08)!important;
  color:var(--s7-cover-ink)!important;
}
.shabbat-info strong{color:#9a6d2e!important}.shabbat-info>span{color:#38556a!important}
.shabbat-clock{border-color:rgba(183,138,71,.28)!important;background:linear-gradient(145deg,#fff,#f3ede1)!important;box-shadow:inset 0 1px #fff,0 10px 26px rgba(16,45,71,.08)!important}
.clock-title{color:#647686!important}.clock-digits{background:#102d47!important;color:#fff!important;box-shadow:inset 0 1px 8px rgba(0,0,0,.18)!important}
.cover-dates{border-top-color:rgba(16,45,71,.16)!important;color:#496477!important}
.cover-bottom span{color:#9f7438!important}

@media(max-width:700px){
  main>.lux-hero{min-height:650px!important;padding-top:26px!important}
  main>.lux-hero:before{inset:10px!important}
  .lux-body{padding-top:48px!important}
}
@media print{
  main>.lux-hero,.weekly-cover{background:#fff!important;color:#102d47!important;box-shadow:none!important;border:1px solid #cbb17f!important}
  main>.lux-hero:after,.hero-art{display:none!important}
}
</style>
'''

if '</head>' not in html:
    raise SystemExit('No </head> found in index.html')
html = html.replace('</head>', css + '\n</head>', 1)
path.write_text(html, encoding='utf-8')
print('Applied Summary 7 light luxury cover override')
