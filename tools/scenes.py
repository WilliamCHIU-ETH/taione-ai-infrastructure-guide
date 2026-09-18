"""Purpose-built conceptual scenes: topology and objects carry the explanation."""
PAPER='#fbfbfa';INK='#37352f';MUTED='#6b6b68';RULE='#e1e1dd';BLUE='#1f70c1';TINT='#edf4fa'

def server(c,x,y,label,down=False,w=160):
    c.rect(x,y,w,104,PAPER if down else 'white',MUTED if down else BLUE)
    for j in range(3):
        c.rect(x+16,y+16+j*24,w-32,16,PAPER,RULE,r=4)
        c.circle(x+w-28,y+24+j*24,3,MUTED if down else BLUE,MUTED if down else BLUE)
    c.text(x+w/2,y+140,label,24,MUTED if down else INK,500,'middle',budget=8)

def special(s,C):
    id=s['id']
    if id=='02-b':
        c=C(s,984)
        c.label(144,208,432,'提出修改','交代問題、做法與測試',True)
        c.arrow(360,332,360,380)
        c.label(144,396,432,'共同審查','正確性、相容性與維護成本')
        c.arrow(252,520,188,592)
        c.arrow(468,520,532,592)
        c.label(48,608,280,'需要調整','補測試、改設計')
        c.label(392,608,280,'獲得接受','合併後依程序發布')
        c.path('M 48 680 H 32 Q 24 680 24 672 V 468 Q 24 460 32 460 H 136')
        c.text(48,816,'需要調整時，回到審查繼續討論',24,MUTED,budget=27)
        return c.write()
    if id=='03-b':
        c=C(s,824)
        c.rect(32,208,656,208,'white',RULE)
        c.circle(84,272,24,PAPER,MUTED);c.circle(84,256,8,'white',MUTED)
        c.path('M 64 308 V 296 Q 64 288 72 288 H 96 Q 104 288 104 296 V 308',MUTED,False)
        server(c,168,236,'自己維護',False,128)
        c.text(336,260,'自行營運',28,weight=600,budget=11)
        c.text(336,308,'部署、更新、值班\n由自己的團隊負責',24,MUTED,budget=12)
        c.rect(32,444,656,208,TINT,BLUE)
        c.circle(96,500,28,'white',BLUE);c.circle(132,496,40,'white',BLUE);c.circle(172,504,28,'white',BLUE)
        c.rect(84,504,100,36,'white','white',r=0)
        c.text(132,604,'服務商營運',24,INK,500,'middle',budget=8)
        c.text(336,496,'購買託管服務',28,weight=600,budget=11)
        c.text(336,544,'付費取得營運能力\n責任依合約分工',24,MUTED,budget=12)
        return c.write()
    if id=='06-a':
        c=C(s,836)
        c.text(32,236,'多個人的請求，同時到來',28,weight=600)
        for i,x in enumerate([48,244,440]):
            c.rect(x,264,180,76,'white',RULE)
            c.text(x+90,312,['寫摘要','回答問題','產生文字'][i],24,anchor='middle',budget=7)
            c.arrow(x+90,340,x+90,380)
        c.label(48,396,624,'vLLM 協調請求','排程、記憶體管理與運算執行',True)
        c.arrow(360,520,360,560)
        c.rect(48,576,624,84,'white',BLUE)
        c.text(72,628,'GPU 資源',28,weight=600,budget=10)
        for j in range(7):c.rect(296+j*48,600,36,36,TINT if j%3 else BLUE,BLUE,r=4)
        return c.write()
    if id=='07-a':
        c=C(s,860)
        c.label(120,208,480,'一批影片處理工作','拆成可分派的任務與批次',True)
        for i,(x,port) in enumerate([(80,216),(280,360),(480,504)]):
            c.arrow(port,332,x+80,480)
            server(c,x,488,['批次 A','批次 B','批次 C'][i],False,160)
        c.text(360,704,'任務分散執行，結果再協調匯集',26,INK,500,'middle',budget=24)
        return c.write()
    if id=='08-a':
        c=C(s,888)
        c.text(32,232,'設定期望：維持 3 份服務',28,weight=600)
        for i,x in enumerate([48,272,496]):
            c.rect(x,268,176,88,'white' if i<2 else PAPER,BLUE if i<2 else MUTED)
            c.text(x+88,320,'運行中' if i<2 else '已故障',28,BLUE if i<2 else MUTED,600,'middle',budget=6)
        c.arrow(360,364,360,412)
        c.label(80,428,560,'控制器發現差異','現況只有 2 份，與期望不一致',True)
        c.arrow(360,552,360,592)
        c.rect(80,608,560,88,'white',BLUE)
        c.text(360,660,'嘗試建立替代實例',28,INK,600,'middle',budget=20)
        c.path('M 80 652 H 48 Q 40 652 40 644 V 484 Q 40 476 48 476 H 72')
        c.text(80,740,'持續觀察，反覆接近期望狀態',24,MUTED,budget=26)
        return c.write()
    if id=='09-a':
        c=C(s,864)
        c.text(32,232,'有限的叢集資源',28,weight=600)
        for row in range(3):
            for col in range(8):
                c.rect(48+col*80,260+row*56,64,40,BLUE if col<3 else (TINT if col<6 else 'white'),BLUE if col<6 else RULE,r=4)
        c.text(32,480,'不同團隊，需求同時進來',28,weight=600)
        for i,x in enumerate([40,264,488]):
            c.rect(x,512,192,112,'white',RULE)
            c.text(x+96,552,['資料工作','分析工作','AI 工作'][i],28,anchor='middle',budget=6)
            c.text(x+96,596,['需要容量','等待排程','需要算力'][i],24,MUTED,anchor='middle',budget=7)
        c.text(32,692,'佇列與規則，決定資源如何分配',26,BLUE,500,budget=25)
        return c.write()
    if id=='11-b':
        c=C(s,824)
        c.text(32,232,'事件持續寫入可保留的紀錄',28,weight=600)
        for i in range(6):
            x=48+i*104;c.rect(x,268,88,64,TINT,BLUE,r=4);c.text(x+44,312,str(i+1),28,BLUE,600,'middle')
        c.path('M 48 356 H 676',MUTED)
        c.text(32,404,'不同讀者可以走到不同位置',26,weight=600)
        readers=[('即時分析',5),('資料儲存',3),('特徵處理',1)]
        for i,(label,pos) in enumerate(readers):
            y=456+i*72;c.text(32,y,label,24,weight=500,budget=7)
            c.path(f'M 192 {y-8} H 664',RULE,False)
            c.circle(208+pos*80,y-8,12,TINT,BLUE)
            c.text(672,y,str(pos+1),24,BLUE,anchor='end',budget=3)
        return c.write()
    if id=='12-b':
        c=C(s,836)
        c.label(120,208,480,'資料讀寫入口','物件與資料區塊由系統管理',True)
        for x,port in [(48,216),(496,504)]:c.arrow(port,332,x+88,436)
        c.path('M 360 332 V 436',MUTED,False,True)
        for i,x in enumerate([48,272,496]):server(c,x,448,'離線' if i==1 else '儲存節點',i==1,176)
        c.text(32,688,'保護方式與容錯程度，依設定而定',26,BLUE,500,budget=25)
        return c.write()
    if id=='16-a':
        c=C(s,1000)
        c.label(120,208,480,'準備資料','留下可追蹤的成果')
        c.arrow(360,332,360,372)
        c.label(120,380,480,'執行模型','各任務有資源與錯誤設定',True)
        c.arrow(224,504,180,612)
        c.arrow(496,504,536,612)
        c.text(116,584,'成功',26,BLUE)
        c.text(552,584,'失敗',26,MUTED)
        c.label(32,620,296,'比較結果','核對版本再重用')
        c.label(392,620,296,'需要時處理失敗','依政策重試或恢復')
        c.path('M 688 680 H 704 V 440 H 608')
        c.text(32,816,'失敗路徑依設定處理，不保證自動恢復',24,MUTED,budget=27)
        return c.write()
    if id=='15-b':
        c=C(s,856)
        c.text(32,232,'相同流程，不同日期的執行',28,weight=600)
        cols=[240,424,608]
        for x,t in zip(cols,['擷取','整理','發布']):c.text(x,296,t,28,INK,600,'middle')
        runs=[('週一',['完成','完成','完成']),('週二',['完成','失敗','等待']),('補跑',['沿用','重試','接續'])]
        for i,(day,states) in enumerate(runs):
            y=332+i*112;c.text(48,y+48,day,28,weight=500,budget=4)
            for x,state in zip(cols,states):
                c.rect(x-72,y,144,76,TINT if state in ['失敗','重試'] else 'white',BLUE if state in ['失敗','重試'] else RULE)
                c.text(x,y+48,state,28,BLUE if state in ['失敗','重試'] else INK,500,'middle')
        c.text(32,712,'補跑範圍與資料正確性，仍需設計',24,MUTED,budget=27)
        return c.write()
    return None
