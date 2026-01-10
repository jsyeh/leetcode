# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
# n 個城市，有n-1條路相接，原本 connections 裡「城市a」單向到「城市b」
# 但你需要將一些路「轉向」，讓「每條路都會到城市0」即「條條大路通羅馬」的意思
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 技巧：可反過來想，從「城市0」出發，要能到全部的城市。再相反即可
        path = defaultdict(list)  # 「正常」的路
        path2 = defaultdict(list)  # 「反過來」的路
        for a,b in connections:
            path[a].append(b)  # 正常的路
            path2[b].append(a)  # 反過來的路
        self.ans = 0
        visited = set()
        def helper(i):  # 從城市 i 出發
            visited.add(i)  # 「標示」走過i不再走
            for b in path[i]:  # 可「順利」走到的城市
                if b not in visited:  # 還沒走過的，就走
                    self.ans += 1  # 反過來思考，才能到
                    helper(b)  # 函式呼叫函式
            for b in path2[i]:  # 「反過來」的城市
                if b not in visited:
                    helper(b)
        helper(0)  # 從「城市0」出發
        return self.ans  # 反過來思考
