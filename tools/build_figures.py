#!/usr/bin/env python3
"""Render original, accessible book diagrams from a small JSON content ledger.

SVG output is dependency-free. Rasterize with tools/rasterize.cjs and sharp.
"""
import json, html, math, pathlib, re, textwrap

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'figures'
PAPER='#fbfbfa'; INK='#37352f'; MUTED='#6b6b68'; RULE='#e1e1dd'; BLUE='#1f70c1'; TINT='#edf4fa'
FONT="'Noto Sans TC','PingFang TC','Heiti TC',sans-serif"
E=lambda s:html.escape(str(s),quote=True)

def lines(s, budget=19):
    result=[]; line=''; n=0
    for c in s:
        if c=='\n': result.append(line); line=''; n=0; continue
        w=1 if ord(c)>255 else .55
        if n+w>budget and line: result.append(line); line=''; n=0
        line+=c; n+=w
    if line: result.append(line)
    return result

def box_h(it,w):
    return 40+len(lines(it['label'],(w-44)/28))*40+(len(lines(it.get('detail',''),(w-44)/24))*36+4 if it.get('detail') else 0)

class Canvas:
    def __init__(self,spec,h):
        self.s=spec; self.h=h; self.a=[]
        self.rect(0,0,720,h,PAPER,stroke='none',r=0)
    def rect(self,x,y,w,h,fill='white',stroke=RULE,r=8):
        self.a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    def text(self,x,y,s,size=28,color=INK,weight=400,anchor='start',budget=22):
        for i,l in enumerate(lines(str(s),budget)):
            self.a.append(f'<text x="{x}" y="{y+i*(size+12)}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{E(l)}</text>')
    def path(self,d,color=MUTED,arrow=True,dash=False):
        self.a.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3"'+(' stroke-dasharray="8 8"' if dash else '')+(f' marker-end="url(#{self.s["id"]}-arrow)"' if arrow else '')+'/>')
    def arrow(self,x,y,X,Y):
        if x==X or y==Y: self.path(f'M {x} {y} L {X} {Y}'); return
        mid=(y+Y)/2; sign=1 if X>x else -1
        self.path(f'M {x} {y} V {mid-8} Q {x} {mid} {x+sign*8} {mid} H {X-sign*8} Q {X} {mid} {X} {mid+8} V {Y}')
    def circle(self,x,y,r,fill=TINT,stroke=BLUE):
        self.a.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    def label(self,x,y,w,label,detail='',focus=False,num=None):
        lablines=lines(label,(w-44)/28)
        detail_lines=lines(detail,(w-44)/24)
        h=40+len(lablines)*40+(len(detail_lines)*36+4 if detail else 0)
        self.rect(x,y,w,h,TINT if focus else 'white',BLUE if focus else RULE)
        self.text(x+24,y+40,label,28,weight=600,budget=(w-44)/28)
        if detail:self.text(x+24,y+44+len(lablines)*40,detail,24,MUTED,budget=(w-44)/24)
        return h
    def header(self):
        self.text(32,44,'TAIONE / 開源基礎設施圖解',20,MUTED)
        self.text(32,96,self.s['title'],32,weight=600,budget=20)
        self.text(32,148,self.s.get('subtitle','概念示意'),24,MUTED,budget=27)
    def footer(self):
        self.path(f'M 32 {self.h-132} H 688',RULE,False)
        self.text(32,self.h-92,self.s['takeaway'],24,BLUE,500,budget=27)
        self.text(32,self.h-20,'概念示意 · 詳細條件與來源見章節正文',20,MUTED)
    def write(self):
        id=self.s['id']; self.header(); self.footer()
        defs=f'<defs><marker id="{id}-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{MUTED}"/></marker></defs>'
        out=f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {self.h}" role="img" aria-labelledby="{id}-title {id}-desc"><title id="{id}-title">{E(self.s["title"])}</title><desc id="{id}-desc">{E(self.s["alt"])}</desc>{defs}<g font-family="{E(FONT)}">'+''.join(self.a)+'</g></svg>\n'
        (OUT/f'{id}.svg').write_text(out)
        return id

def figure(s):
    from scenes import special
    result=special(s,Canvas)
    if result:return result
    items=s['items']; kind=s['kind']; n=len(items)
    if kind=='compare':
        # Two full-width panels make the comparison readable on a phone.
        c=Canvas(s,764); y=208
        for i,it in enumerate(items):
            c.rect(32,y,656,168,TINT if i==1 else 'white',BLUE if i==1 else RULE)
            c.circle(76,y+44,20,TINT if i else PAPER,BLUE if i else MUTED)
            c.text(76,y+52,str(i+1),24,BLUE if i else MUTED,600,'middle')
            c.text(116,y+48,it['label'],28,weight=600,budget=18)
            c.text(56,y+108,it['detail'],24,MUTED,budget=25)
            y+=188
    elif kind=='branch' and n>=3:
        # One upstream actor, two or three independently routed branches.
        if n>4:return generic(s,'layers')
        first_h=box_h(items[0],432)
        y=208+first_h+64
        total=y+sum(box_h(it,400)+28 for it in items[1:])+160
        c=Canvas(s,total)
        c.label(144,208,432,items[0]['label'],items[0]['detail'],True)
        for i,it in enumerate(items[1:]):
            port=216-i*24
            c.path(f'M {port} {208+first_h} V {y+48-8} Q {port} {y+48} {port+8} {y+48} H 276')
            c.label(280,y,400,it['label'],it['detail'])
            y+=box_h(it,400)+28
        # More than 4 branches is rendered as an explicit responsibility list.
        if n>4:return generic(s,'layers')
    elif kind=='roles':
        # Distinct participants, no fabricated chain of authority.
        heights=[box_h(i,576) for i in items]
        h=208+sum(heights)+20*(n-1)+168; c=Canvas(s,h); y=208
        for i,(it,rh) in enumerate(zip(items,heights)):
            c.circle(64,y+36,24,TINT if i==0 else PAPER,BLUE if i==0 else MUTED)
            # Numbered roles; portraits would imply actors even in a quality checklist.
            c.text(64,y+44,str(i+1),24,BLUE if i==0 else MUTED,600,'middle')
            c.label(112,y,576,it['label'],it['detail'],i==0)
            y+=rh+20
    else: return generic(s,kind)
    return c.write()

def generic(s,kind):
    items=s['items']; n=len(items)
    # Vertical diagrams prioritize reading in the GitHub body column.
    heights=[]
    for i in items:
        heights.append(box_h(i,576 if kind=='timeline' else 592))
    gap=44 if kind in ['flow','timeline'] else 20
    h=208+sum(heights)+gap*(n-1)+168; c=Canvas(s,h); y=208
    for idx,(it,rh) in enumerate(zip(items,heights)):
        if kind=='timeline':
            if idx<n-1:c.path(f'M 64 {y+48} V {y+rh+gap+12}',RULE,False)
            c.circle(64,y+28,24,TINT,BLUE)
            c.text(64,y+36,str(idx+1),24,BLUE,600,'middle')
            c.label(112,y,576,it['label'],it['detail'],idx==n-1)
        elif kind=='layers':
            c.rect(32,y,656,rh,TINT if idx==0 else 'white',BLUE if idx==0 else RULE)
            c.text(56,y+40,it['label'],28,weight=600,budget=22)
            c.text(56,y+88,it['detail'],24,MUTED,budget=25)
        else:
            if idx<n-1:c.arrow(360,y+rh,360,y+rh+gap-8)
            c.label(64,y,592,it['label'],it['detail'],idx==min(1,n-1))
        y+=rh+gap
    return c.write()

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    inputs=sorted((ROOT/'.work').glob('figures-*.json'))
    if not inputs:inputs=[ROOT/'sources'/'figures.json']
    allspec=[]
    for p in inputs:allspec+=json.loads(p.read_text())
    seen=set()
    for s in allspec:
        assert s['id'] not in seen,s['id'];seen.add(s['id'])
        assert 1<len(s['items'])<=6,s['id']
        print(figure(s))
    (ROOT/'sources'/'figures.json').write_text(json.dumps(allspec,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
