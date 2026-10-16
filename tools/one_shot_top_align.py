from pathlib import Path
p=Path('styles.css')
s=p.read_text(encoding='utf-8')
marker='/* force-top-alignment-2026-10-16 */'
block='''\n\n/* force-top-alignment-2026-10-16 */\n.sheet:not(.cover){display:block!important;align-items:start!important;justify-content:start!important}\n.sheet:not(.cover)>.sheet-inner{padding-top:14px!important}\n.sheet:not(.cover)>.sheet-inner.wide{padding-top:14px!important}\n.closing-page{display:block!important;text-align:right!important;min-height:0!important}\n.closing-inner{padding-top:14px!important;justify-items:start!important;text-align:right!important}\n@media(max-width:720px){.sheet:not(.cover)>.sheet-inner,.sheet:not(.cover)>.sheet-inner.wide{padding-top:10px!important}.grade-page-inner{padding-top:10px!important}.teaching-head{padding-top:10px!important}.closing-inner{padding-top:10px!important}}\n'''
if marker not in s:
    s += block
p.write_text(s,encoding='utf-8')
print('forced all non-cover content to top')
