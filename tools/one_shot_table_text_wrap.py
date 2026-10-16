from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='id="table-wrap-fix-v1"'
if marker in s:
    raise SystemExit('already patched')
css=r'''
<style id="table-wrap-fix-v1">
/* Keep every mobile table/card value inside its own box. */
@media screen and (max-width:820px){
  .training-table,.cal-table,.workbooks-table,
  .training-table tbody,.cal-table tbody,.workbooks-table tbody,
  .training-table tr,.cal-table tr,.workbooks-table tr,
  .training-table th,.training-table td,
  .cal-table th,.cal-table td,
  .workbooks-table th,.workbooks-table td{
    max-width:100%!important;
    min-width:0!important;
    box-sizing:border-box!important;
  }
  .training-table td,.training-table th,
  .cal-table td,.cal-table th,
  .workbooks-table td,.workbooks-table th{
    overflow:hidden!important;
    overflow-wrap:anywhere!important;
    word-break:break-word!important;
    white-space:normal!important;
  }
  .training-table td>*,.training-table th>*,
  .cal-table td>*,.cal-table th>*,
  .workbooks-table td>*,.workbooks-table th>*{
    min-width:0!important;
    max-width:100%!important;
    overflow-wrap:anywhere!important;
    word-break:break-word!important;
    white-space:normal!important;
  }
  .training-table a,.cal-table a,.workbooks-table a{
    max-width:100%!important;
    overflow-wrap:anywhere!important;
    word-break:break-word!important;
    white-space:normal!important;
  }
  .training-table b,.training-table strong,
  .cal-table b,.cal-table strong,
  .workbooks-table b,.workbooks-table strong{
    white-space:normal!important;
  }
}
@media screen and (max-width:700px){
  #courses .training-table tbody td{
    grid-template-columns:minmax(76px,31%) minmax(0,1fr)!important;
    align-items:start!important;
  }
  #courses .training-table tbody td::before{
    min-width:0!important;
    overflow-wrap:anywhere!important;
    word-break:break-word!important;
  }
  #calendar .cal-table tbody td{
    grid-template-columns:70px minmax(0,1fr)!important;
    align-items:start!important;
  }
}
@media screen and (max-width:390px){
  #courses .training-table tbody td{
    display:block!important;
  }
  #courses .training-table tbody td::before{
    display:block!important;
    margin-bottom:3px!important;
  }
  #calendar .cal-table tbody td{
    display:block!important;
  }
  #calendar .cal-table tbody td::before{
    display:block!important;
    margin-bottom:2px!important;
  }
}
</style>
'''
s=s.replace('</head>',css+'\n</head>',1)
assert marker in s
assert s.count('<style')==s.count('</style>')
p.write_text(s,encoding='utf-8')
print('patched table wrapping')
