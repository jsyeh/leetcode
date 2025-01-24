# LeetCode 802. Find Eventual Safe States
# graph[i] 記錄 node i 可到達的其他 nodes。terminal node 是終點（出不去）
# safe node 「安全的」點，是「出發後，能走到終點」。將「安全的」點全部找出來
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)  # 先知道「有幾個nodes」
        state = [0]*N  # 每個點的狀態 0:沒走過 1:安全 2:不安全
        def dfs(i):  # 利用「函式呼叫函式」的 DFS 深度優先搜尋，確認「能不能」全部走到「安全的目標」
            if state[i]==1: return True  # 安全 （之前已標示「安全」）
            if state[i]==2: return False  # 不安全 （之前已標示「不安全」）
            state[i] = 2  # 先設成「不安全」以避免 dfs()函式呼叫函式「又重覆進來」發生cycle loop
            for j in graph[i]: # 能走到的地方
                if dfs(j) == False:  # 下游不安全，那你也不安全囉
                    return False  # 「不安全」提早結束
            state[i] = 1  # 都沒有「不安全」，那就是安全囉。標示成「安全」
            return True  # 回覆「這段安全」
        ans = []
        for i in range(N):  # 從小到大，依序去做
            if dfs(i)==True:  # 若檢測後，確認安全
                ans.append(i)  # 更新、加入「答案」
        return ans
