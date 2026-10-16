from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')
original=s
body=s.split('</style>')[-1]
# Safety: these legacy structures must not exist in rendered markup.
for token in ['<header','class="cards"','class="actions"','class="weekly-cover"','class="district-cover"','class="cover-frame"']:
    if token in body:
        raise SystemExit(f'ABORT: active markup still uses {token}')

# Remove legacy pre-premium CSS at the start of the first style block, keeping the current premium system.
s=re.sub(r'<style>.*?(?=/\* Premium editorial design system — production, no mock content \*/)', '<style>', s, count=1, flags=re.S)

# Remove two obsolete cover systems that target markup no longer present.
s=re.sub(r'/\* Shared visual identity from the canonical SIKUMSHVUI weekly bulletins \*/.*?(?=/\* Edition 7 cover: historical weekly summaries use logo on cover, author portrait inside \*/)', '', s, count=1, flags=re.S)
s=re.sub(r'/\* Edition 7 cover: historical weekly summaries use logo on cover, author portrait inside \*/.*?(?=/\* Per-topic section colors)', '', s, count=1, flags=re.S)

# Remove old standalone Editorial cover layer; current summary7-premium-v4 + light-cover are authoritative.
s=re.sub(r'<style>\s*/\* Editorial cover: intentional typography, restrained jewel palette, original vector ornament\. \*/.*?</style>', '', s, count=1, flags=re.S)

s=re.sub(r'\n{4,}', '\n\n', s)

# Structural safety checks.
assert '<section id="courses">' in s
assert 'full-training-table-v2' in s
assert 'class="training-table"' in s
assert 'id="summary7-premium-v4"' in s
assert 'id="s7-light-cover-v1"' in s
assert s.count('<style') == s.count('</style>')

if s != original:
    p.write_text(s, encoding='utf-8')
print('changed=', s != original)
print('bytes_before=', len(original.encode('utf-8')))
print('bytes_after=', len(s.encode('utf-8')))
print('style_pairs=', s.count('<style'))
