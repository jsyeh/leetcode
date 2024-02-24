# 「我只跟你講秘密哦！」八卦就這樣傳了出去。
# 要小心，同一個時間當好友，也會「馬上互享資訊」
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = defaultdict(list) # g[a] a會把八卦在t時間講給b聽
        for a,b,t in meetings: # 針對見面的狀況
            g[a].append((t,b)) # 記錄「八掛圈」會在何時「跟誰講」
            g[b].append((t,a))
        
        knownT = [inf]*n # knowT[i] 是 i 知道秘密的時間，用來加速用
        #knownT[0] = 0 # 0 知道秘密的時間
        #knownT[firstPerson] = 0 # 第1好友 知道秘密的時間

        heap = [] # heap裡，會照著「知道的時間」，從早到晚秀出來
        heappush(heap, (0,0)) # 第0時間，0知道答案
        heappush(heap, (0,firstPerson)) # 第0時間，第1個知道秘密的人
        while len(heap)>0: # 照時間來處理「知道的人」
            t, p = heappop(heap) # p 在 t 時間知道秘密
            if t<knownT[p]: # 比預計的更早知道的話
                knownT[p] = t # 更新時間
                for t2, p2 in g[p]: # p 會告訴 p2 嗎？看時間
                    if t2>=t: # 可告訴 p2
                        heappush(heap, (t2,p2))
        return [i for i in range(n) if knownT[i]!=inf]

        '''
        # 下面是錯誤的寫法（只能在簡單測資成功）在大家同時就可能出錯
        # ex. n = 5, meetings = [[4,3,1],[3,2,1],[2,1,1]], firstPerson=1
        meetings.sort(key=lambda x:x[2]) # 先以「時間」排序
        print(meetings)
        ans = set([0,firstPerson]) # 一開始，就0本人+好友firstPerson
        for x,y,t in meetings: # 按照時間，逐一「講秘密」的模擬
            if x in ans: ans.add(y) # 一人知，天下知（另一人也知）
            elif y in ans: ans.add(x) # 一人知，天下知（另一人也知）
            #比較麻煩的狀況：現在兩人，其中一人「在（同時的）下一筆」知秘密
        return list(ans)
        '''
