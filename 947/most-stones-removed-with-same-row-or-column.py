# LeetCode 947. Most Stones Removed with Same Row or Column
# 題目：有「共同row」或「共同col」的石頭，可消掉1顆，最多可消掉幾顆石頭？
# Discussions 有人暗示：可看成「石頭像西洋棋城堡移動/相連最多位置」
# lee215解釋：其實只要看有幾組相鄰的「島」islands，N-islands數，就是答案
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        adj = defaultdict(list) # adjacent 相鄰的資料結構
        for i in range(N): # 用最笨的法，暴力2層迴圈，找出stones[i] stones[j] 相鄰
            for j in range(i+1,N): # 測試 stones[i] stones[j] 是否「城堡式相鄰」（有相同row或col）
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]: 
                    adj[i].append(j)
                    adj[j].append(i)
                    
        visited = [False]*N  # 標示「有沒有走過」 stones[i]，避免重覆走
        def dfs(i):  # 用「函式呼叫函式」找所有相鄰的點
            if visited[i]: return # 走過就不要走
            visited[i] = True
            for j in adj[i]: # 所有相鄰 stones[i] 的 stones[j]
                dfs(j)  # 函式呼叫函式

        islands = 0
        for i in range(N):  # 依序檢查所有的 stons[i]
            if not visited[i]:  # 還沒走過的話
                islands += 1
                dfs(i)
        return N - islands
