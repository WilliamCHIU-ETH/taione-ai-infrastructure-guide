#!/usr/bin/env python3
"""Validate the public book's reading paths, figures and source coverage."""
import json,pathlib,re,sys,urllib.parse,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
    if not ok: errors.append(msg)
chapters=sorted((ROOT/'chapters').glob('*.md'))
check(len(chapters)==18,'Chapter count must be 18')
sources=json.loads((ROOT/'sources/references.json').read_text())
known={s['url'] for s in sources}
for f in [ROOT/'README.md',ROOT/'SOURCES.md']+chapters:
    text=f.read_text()
    check(text.count('<details>')==text.count('</details>'),f'{f.name}: unbalanced details')
    check(not re.search(r'/Users/|/private/tmp/|TODO|TBD|turn\d+(?:search|view)',text),f'{f.name}: private path or placeholder')
    for href in re.findall(r'\]\(([^\s]+?)(?:\s+"[^"]*")?\)',text):
        if href.startswith(('https://','http://','mailto:')):continue
        clean,_,anchor=href.partition('#')
        target=(f.parent/urllib.parse.unquote(clean)).resolve() if clean else f
        check(target.exists(),f'{f.name}: missing link {href}')
        if anchor and target.exists() and target.suffix=='.md':
            heads=re.findall(r'^#{1,6}\s+(.+)$',target.read_text(),re.M)
            slugs=[re.sub(r'[^\w\-\s]','',h.lower()).replace(' ','-') for h in heads]
            check(urllib.parse.unquote(anchor) in slugs,f'{f.name}: missing anchor {href}')
    for alt,path in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',text):
        check(len(alt)>12,f'{f.name}: weak image alt')
    if f in chapters:
        i=chapters.index(f)
        check(text.count('回總目錄')==2,f'{f.name}: top/bottom navigation')
        check((chapters[i+1].name if i<17 else '../SOURCES.md') in text,f'{f.name}: next link')
        urls=re.findall(r'\]\((https://[^)]+)\)',text)
        check(len(set(urls))>=3,f'{f.name}: too few sources')
        for url in urls:
            check(url in known,f'{f.name}: source absent from registry {url}')
figs=json.loads((ROOT/'sources/figures.json').read_text())
check(len(figs)==32,'32 figures including cover expected')
for f in figs:
    svg=ROOT/'assets/figures'/f'{f["id"]}.svg';png=svg.with_suffix('.png')
    check(svg.exists() and png.exists(),f'missing figure {f["id"]}')
    root=ET.parse(svg).getroot();ns={'s':'http://www.w3.org/2000/svg'}
    check(root.find('s:title',ns) is not None and root.find('s:desc',ns) is not None,f'SVG accessibility {svg.name}')
    check(not re.search(r'<script|foreignObject|https?://(?!www.w3.org)',svg.read_text()),f'SVG dependency {svg.name}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(chapters)} chapters; {len(figs)} SVG/PNG pairs; {len(sources)} sources; navigation, local links, anchors, details, privacy and citation coverage.')
