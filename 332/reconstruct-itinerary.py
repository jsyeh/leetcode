class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dest = {} # 建出資料結構，像 dest["JFK"] 會對應 JFK 可到的全部機場
        for s,t in tickets:
            if s in dest: # 若已有 dest[s]
                dest[s].append(t) # 就 append
            else: # 如果 dest[s] 還不存在
                dest[s] = [t] # 就是第1筆
        # 建好資料結構後，把 dest[s] 逐一做排序
        for s in dest: # 參考 vanAmsen 的 Solution
            dest[s].sort(reverse=True) # 是倒過來排序，這樣走到最後一筆，就是照字母排序的結果

        ans = [] # 答案在這裡，將倒著存答案（會殘留最後一筆答案）
        def dfs(s):
            while s in dest and dest[s]: # 若能再走下去，就倒著全部試走
                dfs(dest[s].pop()) # 全部走過，且把 dest[s] 耗盡
            ans.append(s) # 最後把s放在這一層(倒著存起來)
        
        dfs("JFK") # 第一個出發
        return ans[::-1] # 倒過來，把答案回傳
