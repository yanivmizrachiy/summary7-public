from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='/* mobile-fit-v1 */'
if marker in s:
    raise SystemExit('already patched')
css=r'''
<style id="mobile-fit-v1">
/* mobile-fit-v1: zero page-level horizontal drift; phone-native layouts */
*,*::before,*::after{box-sizing:border-box}
html,body{width:100%;max-width:100%;overflow-x:hidden}
img,iframe,video,svg{max-width:100%}

@media screen and (max-width:820px){
  main{width:100%!important;max-width:100%!important;margin:0!important;overflow-x:hidden!important}
  main>*{min-width:0;max-width:100%}
  main>.lux-hero{width:auto;max-width:none}
  nav.quick{flex-wrap:wrap!important;overflow-x:visible!important;justify-content:center!important;margin-inline:0!important}
  nav.quick a{flex:1 1 auto!important;min-width:max-content}
  .training-wrap,.cal-wrap,.workbooks-table-wrap{max-width:100%!important}
}

@media screen and (max-width:700px){
  body{overscroll-behavior-x:none}
  main{padding-inline:max(12px,env(safe-area-inset-left)) max(12px,env(safe-area-inset-right))!important}
  main>.lux-hero{margin-inline:calc(-1 * max(12px,env(safe-area-inset-left))) calc(-1 * max(12px,env(safe-area-inset-right)))!important;padding-inline:20px!important}
  .lux-top,.lux-body,.shabbat-feature,.author-intro,.green-page,#courses,#news,#calendar,#moodle,#workbooks,#teaching,footer{min-width:0!important;max-width:100%!important}
  h1,h2,h3,h4,p,li,a,strong,span{overflow-wrap:anywhere}
  .hero-title-line{white-space:normal!important}

  /* Training rows are already cards; enforce zero intrinsic width. */
  #courses .training-wrap{overflow:visible!important}
  #courses .training-table{min-width:0!important;max-width:100%!important;width:100%!important}
  #courses .training-table tbody tr,#courses .training-table tbody td{min-width:0!important;max-width:100%!important}
  #courses .training-table tbody td{grid-template-columns:minmax(88px,34%) minmax(0,1fr)!important}

  /* Calendar becomes phone-native cards instead of a 720px table. */
  #calendar .cal-wrap{overflow:visible!important;border:0!important;box-shadow:none!important;background:transparent!important}
  #calendar .cal-table,#calendar .cal-table tbody,#calendar .cal-table tr,#calendar .cal-table td{display:block!important;width:100%!important;min-width:0!important;max-width:100%!important}
  #calendar .cal-table{border:0!important;background:transparent!important}
  #calendar .cal-table thead{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important}
  #calendar .cal-table tbody tr{margin:0 0 12px!important;padding:13px 14px!important;border:1px solid #e3d3b4!important;border-radius:14px!important;background:#fff!important;box-shadow:0 5px 16px rgba(97,73,30,.08)!important}
  #calendar .cal-table tbody td{display:grid!important;grid-template-columns:82px minmax(0,1fr)!important;gap:9px!important;padding:7px 0!important;border:0!important;white-space:normal!important;overflow-wrap:anywhere!important}
  #calendar .cal-table tbody td:nth-child(1)::before{content:'תאריך';font-weight:800;color:#7a5a1f}
  #calendar .cal-table tbody td:nth-child(2)::before{content:'שעה';font-weight:800;color:#7a5a1f}
  #calendar .cal-table tbody td:nth-child(3)::before{content:'אירוע';font-weight:800;color:#7a5a1f}

  /* Workbooks become compact two-part cards, no sideways table scrolling. */
  #workbooks .workbooks-table-wrap{overflow:visible!important;border:0!important;box-shadow:none!important;background:transparent!important}
  #workbooks .workbooks-table,#workbooks .workbooks-table tbody,#workbooks .workbooks-table tr,#workbooks .workbooks-table th,#workbooks .workbooks-table td{display:block!important;width:100%!important;min-width:0!important;max-width:100%!important}
  #workbooks .workbooks-table{border:0!important;background:transparent!important}
  #workbooks .workbooks-table thead{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important}
  #workbooks .workbooks-table tbody tr{margin:0 0 12px!important;padding:14px!important;border:1px solid #d9d2e8!important;border-radius:14px!important;background:#fff!important;box-shadow:0 5px 16px rgba(58,43,92,.08)!important}
  #workbooks .workbooks-table tbody th{padding:0 0 11px!important;border:0!important;background:transparent!important;font-size:16px!important}
  #workbooks .workbooks-table tbody td{padding:0!important;border:0!important;background:transparent!important}
  #workbooks .workbook-3d-button{width:100%!important;max-width:100%!important;min-width:0!important}

  /* Keep all decorative pieces inside the viewport. */
  .hero-art,.art-seven,.art-orbit{max-width:100vw!important}
}

@media screen and (max-width:360px){
  nav.quick{gap:5px!important;padding:6px!important}
  nav.quick a{font-size:11px!important;padding:8px 9px!important}
  #courses .training-table tbody td{grid-template-columns:1fr!important;gap:3px!important}
  #calendar .cal-table tbody td{grid-template-columns:68px minmax(0,1fr)!important}
}
</style>
'''
s=s.replace('</head>', css+'\n</head>',1)
assert marker in s
assert s.count('<style')==s.count('</style>')
p.write_text(s,encoding='utf-8')
print('patched mobile fit')
