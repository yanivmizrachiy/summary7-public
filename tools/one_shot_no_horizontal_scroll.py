from pathlib import Path
p=Path('styles.css')
s=p.read_text(encoding='utf-8')
marker='/* no-horizontal-scroll-2026-10-16 */'
if marker not in s:
    s += '''\n\n/* no-horizontal-scroll-2026-10-16 */
html,body{max-width:100%;overflow-x:hidden!important}
main,.sheet,.sheet-inner,.cover-inner,.grade-sheet,.story,.science-a4-card,.training-wrap,.training-table,.event-list,.task-list,.workbook-grid,.important-links,.video{max-width:100%;min-width:0}
img,iframe,video,svg,table{max-width:100%}
a,p,span,strong,h1,h2,h3,h4,li,td,th{overflow-wrap:anywhere;word-break:break-word}
.training-wrap{overflow-x:hidden!important}
.training-table{width:100%!important;max-width:100%!important}
.link-row,.date-row,.author-card,.workbook-grid a,.event-list article{min-width:0;max-width:100%}
@media(max-width:720px){
  html,body,main{width:100%;max-width:100%;overflow-x:hidden!important}
  .sheet{width:100%!important;max-width:100%!important;min-width:0!important;aspect-ratio:auto!important;overflow:hidden!important}
  .sheet-inner,.sheet-inner.wide,.cover-inner,.grade-page-inner,.science-a4-inner{width:100%;max-width:100%;min-width:0}
  .date-row{width:auto!important;max-width:calc(100% - 34px)!important;left:17px!important;right:17px!important}
  .training-wrap,.training-table,.training-table tbody,.training-table tr,.training-table td{max-width:100%!important;min-width:0!important}
  .training-table td{grid-template-columns:minmax(0,34%) minmax(0,1fr)!important}
  .link-row a,.task-list a,.important-links a,.event-register-link,.science-register{max-width:100%!important;white-space:normal!important;text-align:center}
  .video iframe{width:100%!important;max-width:100%!important}
  .science-a4-page{min-height:calc(100vw * 1.4142)}
}
@media(max-width:390px){
  .training-table td{grid-template-columns:1fr!important}
  .date-row{gap:6px!important;font-size:.66rem!important}
}
'''
for token in ['overflow-x:hidden!important','aspect-ratio:auto!important','training-table td{grid-template-columns:minmax(0,34%) minmax(0,1fr)!important}']:
    assert token in s
p.write_text(s,encoding='utf-8')
print('horizontal scroll guards applied')
