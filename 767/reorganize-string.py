# 讓相鄰的字母不同。失敗的話回傳空字串""
# 如果最多的字母超過一半, 就一定失敗。
# 先多打
# 1. 把字母出現的次數,數一數，放入資料結構（大的會自動取出來）
# 2. 取出最多的a：要用它？不用它？
# 2.1. 如果 ans 是空的，用它。如果 ans[-1]最後一個不是a它，用a它
# 2.2. sorry連續/重覆了，再抽下一位b，塞進去。再把第一多a、第二多的b，都塞回資料結構

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        table = {} # 大家都空空的，字典，裡面會存「字母出現幾次」
        for c in s:
            if c in table: table[c] += 1
            else: table[c] = 1
        # 用一個神奇的資料結構heap（會把最多的印出來）
        heap = []
        for c in table: # 每一個出現的字母，把它的次數、字母，都存入heap中
            heap.append( (-table[c], c) )  # 因heap是小到大，所以加負號以合需求
        heapify(heap) # 把 heap 變成真正的 heap, 也就是取出的永遠是最小的/最大的

        ans = ""
        while len(heap)>0: # 只要 heap 裡還有，就能取出
            t, c = heappop(heap) # 小心，t是很負很負的數，對應「出現很多次」
            if ans=="" or ans[-1]!=c: # 可以使用「最多的」c
                ans += c # 把字母排在答案裡
                # 再把用過1次的c塞回去隊伍裡
                if t+1!=0 : heappush(heap, (t+1,c) ) # 若還有剩，再塞回去
            else: # 不能使用「最多的c」，就再抽下一個
                if len(heap)==0: # 全部用完，沒辦法抽下一個的話
                    return "" # 就沒辦法完成
                t2, c2 = heappop(heap) # 再抽下一個
                ans += c2 # 把字母排在答案裡
                # 再把沒用的 c 與用過1次的c2塞回去隊伍裡
                heappush(heap,  (t,c)  ) # 再塞回去
                if t2+1 != 0: heappush(heap,  (t2+1,c2) ) # 若還有剩，再塞回去
        return ans
