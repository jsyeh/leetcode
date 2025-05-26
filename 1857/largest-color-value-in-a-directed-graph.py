# LeetCode 1857. Largest Color Value in a Directed Graph
# graph 裡找一條 path 裡面有「出現最多次數」的某個字母, 那個字母它出現幾次
# 可簡化、專注在「先試 indegree[node]==0」當「每一輪的起點」
# 同時更新到 node 為止的 freq 字母累積量, 最後再找「全部node」的「出現最多次數的字母」出現幾次
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        path = defaultdict(list)  # 建出 path 資訊, path[a] 對應 a 能到的 nodes
        indegree = defaultdict(int)  # indegree[b] 對應 有幾個 nodes 可進入 b
        for a,b in edges:
            path[a].append(b)  # node a 可以到 node b
            indegree[b] += 1  # node b 又有1個「上游」可進入 b
        visited = set()  # 走過的, 不要再走哦
        N = len(colors)  # 有幾個 nodex
        freq = [[0]*26 for i in range(N)]  # 每個 node 記錄「到它為止」累積色彩數
        start = []  # 如果 indegree是 0 就可以當「開始」node
        for a in range(N):  # 要找到 indegree 是 0 的起點
            if indegree[a]==0: start.append(a)
        while start:  # 如果還有「開始」node
            node = start.pop()  # 現在要分析的 node
            visited.add(node)  # 標記「此 node 走過了」
            color = ord(colors[node]) - ord('a')  # 對應的色彩代碼 0..25
            freq[node][color] += 1  # 更新「到達現在 node」的累積色彩數
            for node2 in path[node]:  # 從 node 出發, 能到達 node2
                freq[node2] = list(map(max, freq[node2], freq[node]))  # 更新 node2 的累積色彩
                indegree[node2] -= 1  # 用到 node 後, 就「拔掉」node2 的1個上游
                if indegree[node2]==0: start.append(node2)  # 變成 0 後,可當起點
        if len(visited) != N: return -1  # 有的點「無法走到」代表有 cycle 失敗
        return max( list(map(max, freq)) )  # 全部 nodes 對應的 freq 字母累積量, 找最大的值
