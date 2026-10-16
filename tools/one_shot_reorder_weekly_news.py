from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')
pat=r'<section class="sheet news-page" id="news">.*?</section>\n\n  <section class="sheet courses-page" id="courses">'
m=re.search(pat,s,re.S)
if not m: raise SystemExit('news section not found')
new='''<section class="sheet news-page" id="news">
    <div class="sheet-inner">
      <p class="eyebrow">עדכוני השבוע</p>
      <h2>מה חדש השבוע?</h2>
      <div class="story-list">
        <article class="story feature-story"><h3>סרטון המחשה של איילת קריספין בנושא חרוט</h3><p>פורסם סרטון המחשה שמסייע להמחיש באופן חזותי וברור את מבנה החרוט ואת הרעיונות המתמטיים המרכזיים בנושא.</p><div class="video"><iframe src="https://www.youtube-nocookie.com/embed/eAW0AnHfQC8" title="סרטון המחשה של איילת קריספין בנושא חרוט" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div></article>
        <article class="story"><h3>דפי עבודה בנושא חרוט</h3><p>פורסמו דפי עבודה בנושא חרוט לתרגול ולהעמקת ההבנה.</p><div class="link-row"><a href="https://yanivmizrachiy.github.io/harut/" target="_blank" rel="noopener noreferrer">פתיחת דפי העבודה בנושא חרוט</a></div></article>
        <article class="story"><h3>דפי עבודה בנושא גליל</h3><p>פורסמו דפי עבודה בנושא גליל לתרגול ולהעמקת ההבנה.</p><div class="link-row"><a href="https://galil-new.vercel.app" target="_blank" rel="noopener noreferrer">פתיחת דפי העבודה בנושא גליל</a></div></article>
        <article class="story"><h3>קיימנו הדרכה בנושא Moodle</h3><p>עסקנו בפתיחת מרחבי למידה, בחיבור התלמידים למרחבים ובהגשת משימות החובה בשכבות ז׳–ח׳.</p></article>
      </div>
    </div>
  </section>

  <section class="sheet courses-page" id="courses">'''
s=s[:m.start()]+new+s[m.end():]
for t in ['סרטון המחשה של איילת קריספין בנושא חרוט','דפי עבודה בנושא חרוט','דפי עבודה בנושא גליל','קיימנו הדרכה בנושא Moodle','id="courses"']:
    if t not in s: raise SystemExit('missing '+t)
p.write_text(s,encoding='utf-8')
print('weekly news reordered')