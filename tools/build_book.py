#!/usr/bin/env python3
"""Assemble navigation and source index without rewriting chapter prose."""
import json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
PARTS=[(1,5,'第一篇 · 建立全景'),(6,7,'第二篇 · 模型與分散運算'),(8,10,'第三篇 · 算力與系統管理'),(11,14,'第四篇 · 資料的流動與計算'),(15,16,'第五篇 · 可靠的工作流程'),(17,18,'第六篇 · 回到計畫意圖')]

def main():
    chapters=sorted((ROOT/'chapters').glob('*.md'))
    assert len(chapters)==18,f'Expected 18 chapters, found {len(chapters)}'
    titles=[p.read_text().splitlines()[0].removeprefix('# ') for p in chapters]
    entries=[]
    for i,p in enumerate(chapters):
        n=i+1; part=next(t for a,b,t in PARTS if a<=n<=b)
        prev=chapters[i-1].name if i else '../README.md'
        nxt=chapters[i+1].name if i<17 else '../SOURCES.md'
        pn=f'第 {i:02} 章' if i else '閱讀入口'
        nn=f'第 {i+2:02} 章' if i<17 else '來源索引'
        nav=f'| [**← {pn}**]({prev}) | [**回總目錄**](../README.md#閱讀目錄) | [**{nn} →**]({nxt}) |\n| :--- | :---: | ---: |'
        body=re.sub(r'<!-- BOOK-NAV-START -->.*?<!-- BOOK-NAV-END -->\n*','',p.read_text(),flags=re.S)
        head,rest=body.split('\n',1)
        block=f'<!-- BOOK-NAV-START -->\n\n{part} · 第 **{n:02} / 18** 章\n\n{nav}\n\n<!-- BOOK-NAV-END -->\n'
        bottom=f'\n<!-- BOOK-NAV-START -->\n\n---\n\n'+(f'接著讀：**{titles[i+1]}**。\n\n' if i<17 else '讀完本書，可到來源索引核對資料或回目錄重讀。\n\n')+nav+'\n\n<!-- BOOK-NAV-END -->\n'
        p.write_text(head+'\n\n'+block+rest.strip()+'\n'+bottom)
        entries.append({'number':n,'file':'chapters/'+p.name,'title':titles[i],'part':part})
    (ROOT/'sources'/'chapters.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
    allsrc=[]
    for f in (ROOT/'.work').glob('sources-*.json'):allsrc+=json.loads(f.read_text())
    if not allsrc:allsrc=json.loads((ROOT/'sources'/'references.json').read_text())
    byurl={}
    for s in allsrc:
        u=s['url'];s['chapters']=[str(x).zfill(2) for x in s['chapters']]
        if u not in byurl:byurl[u]=s
        else:
            byurl[u]['chapters']=sorted(set(byurl[u]['chapters']+s['chapters']))
            if s['supports'] not in byurl[u]['supports']:byurl[u]['supports']+='；'+s['supports']
    sources=list(byurl.values())
    (ROOT/'sources'/'references.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
    out=['# 來源索引與查證方式','','[← 回到第 18 章](chapters/18-maintainers-and-taiwan.md) · [回總目錄](README.md#閱讀目錄)','','本書以計畫官方、上游專案文件、治理規則與企業自身工程說明為來源。下列日期是閱讀查核日，不是文章發布日。動態文件後續可能改動。','','## 如何看待證據','','- **官方目的**：支持主辦單位明確宣示的目標，不能直接證明目標已實現。','- **技術與治理文件**：支持目前描述的功能和角色；版本差異需另看正文。','- **企業案例**：支持該公司自述的使用或投入，不能推論整體市占或公司控制權。','- **本書分析**：從上述資料推導可能的影響，不冒充主辦方未公開的選題決策。','','未取得逐項 Track 遴選紀錄、維護投入預算及所有企業貢獻占比，因此不為這些資訊填入推測數字。','']
    for n,p in enumerate(chapters,1):
        out+=['## '+titles[n-1],'',f'[閱讀本章](chapters/{p.name})','', '| 來源 | 能支持什麼 | 查核日 |','| --- | --- | --- |']
        for s in sources:
            if f'{n:02}' in s['chapters']:
                sup=s['supports'].replace('|','／'); title=s['title'].replace('|','／')
                out.append(f'| [{title}]({s["url"]}) · {s["publisher"]} | {sup} | {s["accessed"]} |')
        out.append('')
    out+=['## 維護本書','','更正內容時，請同時提供可支持更正的第一手來源、適用版本與日期。PNG 是固定呈現的閱讀版，SVG 是可編輯的向量原圖；每圖的文字稿保存在 [圖解資料](sources/figures.json)。','','[← 最後一章](chapters/18-maintainers-and-taiwan.md) · [回總目錄](README.md#閱讀目錄)','']
    (ROOT/'SOURCES.md').write_text('\n'.join(out))
    print(f'assembled {len(chapters)} chapters / {len(sources)} primary sources')

if __name__=='__main__':main()
