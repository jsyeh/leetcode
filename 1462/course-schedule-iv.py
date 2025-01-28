# LeetCode 1462. Course Schedule IV
# 要修一些課，它們有對應的「先修課程」 prerequisites 一堆 [a,b] 對應 a 修完，再修 b
# 問 queries 裡一堆 [u,v] 的是否有相關的「先修課程」前後關係（題目保證沒有 cycle 發生）
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)  # 可先把 prerequisites 建出對應的 graph
        for a, b in prerequisites:
            graph[a].append(b)
        # Hint 1 建議 isReachable[i][j] 對應 node i （千辛萬苦）可到 node j
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        # Hint 2 建議用 BFS 來建出「相依關係」
        for i in range(numCourses):
            visited = set([i])  # 從 i 開始 BFS 走
            queue = deque([i])  # 從 i 開始 BFS 走
            while queue:
                ii = queue.popleft()  # 現在走到 ii
                isReachable[i][ii] = True
                for jj in graph[ii]:  # 往下可走到 jj 
                    if jj not in visited:  # 若 jj 還沒有走過
                        visited.add(jj)  # 標示走過，繼續往下走
                        queue.append(jj)  # 繼續往下走
        ans = [ isReachable[u][v] for u,v in queries]
        return ans
