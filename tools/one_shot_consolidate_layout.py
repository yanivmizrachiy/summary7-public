from pathlib import Path

p=Path('styles.css')
s=p.read_text(encoding='utf-8')
start=s.find('/* force-top-alignment-2026-10-16 */')
if start < 0:
    raise SystemExit('expected legacy override marker not found')
s=s[:start].rstrip()
final=r'''

/* final-layout-2026-10-16 */
html,body{max-width:100%;overflow-x:hidden!important}
main,.sheet,.sheet-inner,.cover-inner,.grade-sheet,.story,.science-a4-card,.training-wrap,.training-table,.event-list,.task-list,.workbook-grid,.important-links,.video{max-width:100%;min-width:0}
img,iframe,video,svg,table{max-width:100%}
a,p,span,strong,h1,h2,h3,h4,li,td,th{overflow-wrap:anywhere;word-break:break-word}
.sheet{aspect-ratio:210/297;min-height:clamp(560px,calc((100vw - 32px)*1.4142),1584px);overflow:hidden}
.sheet:not(.cover){display:block!important;align-items:start!important;justify-content:start!important}
.sheet:not(.cover)>.sheet-inner,.sheet:not(.cover)>.sheet-inner.wide,.grade-page-inner,.science-a4-inner,.teaching-head{padding-top:10px!important}
.closing-page{display:block!important;text-align:right!important;min-height:0!important}
.closing-inner{padding-top:10px!important;justify-items:start!important;text-align:right!important}
.cover-inner{min-height:92svh;align-content:start;padding-top:96px}
.date-row{position:absolute;top:24px;inset-inline:28px;width:auto}
.event-register-note{margin:8px 0 10px;color:#5e7180;line-height:1.55}
.event-register-link{display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:8px 14px;border-radius:999px;background:linear-gradient(135deg,var(--blue),#2787c9);color:#fff;text-decoration:none;font-weight:800}
.whatsapp-label{display:inline-flex;align-items:center;min-height:32px;padding:6px 11px;margin-bottom:10px;border-radius:999px;background:#e7f9ed;color:#167446;font:800 .78rem/1.2 "Rubik",Arial,sans-serif}
.science-register{background:linear-gradient(135deg,#128c7e,#25d366)!important;box-shadow:0 10px 22px rgba(18,140,126,.22)!important}
.science-a4-page{background:radial-gradient(circle at 86% 8%,rgba(37,211,102,.22),transparent 25%),linear-gradient(145deg,#eefcf3,#fff 55%,#e7f8ef)}
.science-a4-inner{min-height:100%;display:grid;align-content:start;gap:18px}
.science-a4-card{position:relative;max-width:820px;margin:0 auto;padding:clamp(26px,5vw,46px);border:1px solid rgba(36,170,92,.28);border-radius:28px;background:rgba(255,255,255,.94);box-shadow:0 18px 42px rgba(31,126,72,.11)}
.science-a4-card:before{content:"";position:absolute;inset-inline-start:0;top:0;bottom:0;width:6px;background:linear-gradient(#25d366,#128c7e);border-radius:28px 0 0 28px}
.science-a4-card h3{margin-bottom:18px;color:#17613d;font:900 clamp(2rem,5vw,3.2rem)/1.05 "Frank Ruhl Libre",serif}
.science-a4-card p{font-size:clamp(1rem,2.2vw,1.16rem);line-height:1.82;color:#3f6250}
.training-wrap{overflow-x:hidden!important}
.training-table{width:100%!important;max-width:100%!important}
.link-row,.date-row,.author-card,.workbook-grid a,.event-list article{min-width:0;max-width:100%}
@media(max-width:720px){
  html,body,main{width:100%;max-width:100%;overflow-x:hidden!important}
  .sheet{width:100%!important;max-width:100%!important;min-width:0!important;aspect-ratio:auto!important;min-height:calc(100vw * 1.4142);overflow:hidden!important}
  .sheet-inner,.sheet-inner.wide,.cover-inner,.grade-page-inner,.science-a4-inner{width:100%;max-width:100%;min-width:0}
  .sheet:not(.cover)>.sheet-inner,.sheet:not(.cover)>.sheet-inner.wide,.grade-page-inner,.science-a4-inner,.teaching-head{padding-top:8px!important}
  .cover-inner{min-height:100svh;align-content:start;padding-top:76px}
  .date-row{top:16px;inset-inline:17px;width:auto!important;max-width:calc(100% - 34px)!important;left:17px!important;right:17px!important}
  .training-wrap,.training-table,.training-table tbody,.training-table tr,.training-table td{max-width:100%!important;min-width:0!important}
  .training-table td{grid-template-columns:minmax(0,34%) minmax(0,1fr)!important}
  .link-row a,.task-list a,.important-links a,.event-register-link,.science-register{max-width:100%!important;white-space:normal!important;text-align:center}
  .event-register-link,.science-register{width:100%}
  .video iframe{width:100%!important;max-width:100%!important}
  .science-a4-card{padding:22px 18px;border-radius:20px}
  .science-a4-card h3{font-size:2.1rem}
}
@media(max-width:390px){.training-table td{grid-template-columns:1fr!important}.date-row{gap:6px!important;font-size:.66rem!important}}
@media print{
  .sheet{width:210mm;min-height:297mm;aspect-ratio:auto;break-after:page;page-break-after:always;overflow:visible}
  .science-a4-page,.grade-page{break-before:page;page-break-before:always;break-after:page;page-break-after:always}
  .science-a4-inner{min-height:297mm}
  .date-row{position:static;width:100%}
  .cover-inner{min-height:0;padding-top:0}
}
'''
s += final
for marker in ('/* force-top-alignment-2026-10-16 */','/* summary7-content-polish-2026-10-16 */','/* a4-pages-2026-10-16 */','/* no-horizontal-scroll-2026-10-16 */'):
    if marker in s:
        raise SystemExit('legacy marker remains: '+marker)
if '/* final-layout-2026-10-16 */' not in s:
    raise SystemExit('final block missing')
p.write_text(s,encoding='utf-8')
print('layout consolidated')
