# LeetCode 2685. Count the Number of Complete Components
# 有 0..n-1 個 nodes，以 edges 相連。問有幾個「完全相連」的物件？
# 完全相連 complete onnected components 是指「裡面nodes全部相連」
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # 利用 union-find 技巧，看有幾個 group 並適時合併，再用
        boss = [i for i in range(n)]  # 每個人是自己的group
        groupSize = [1] * n  # 每個 group 大小是1
        groupEdges = [0] * n  # 每個 group 內含的 edges 還是0，之後用 size 及 edges
        groupLeader = [True] * n  # 每個人，一開始都是 Leader
        def find(a):  # 找出 node a 所在集團的領導者 boss[a]
            if a == boss[a]: return a  # 自己是自己的老板
            boss[a] = find(boss[a])  # 我的老板的老板，當我的老板
            return boss[a]  # 更新後，找到大老板了
        for i,(a,b) in enumerate(edges):  # 看是否需要「集團合併」
            a, b = find(a), find(b)  # 找到各自的大老板
            if a != b:  # 兩個大老板不同，是兩個分開的集團
                boss[a] = b  # 將兩集團合併，boss b 當成更大的老板
                groupSize[b] += groupSize[a]  # 集團變大了!
                groupEdges[b] += groupEdges[a]  # 內含 edges 數也增加
                groupLeader[a] = False  # a 集團被消滅
            groupEdges[b] += 1  # 現在再多1個 edge i
        ans = 0
        for i in range(n):
            if groupLeader[i] and groupEdges[i]==groupSize[i]*(groupSize[i]-1)//2:
                ans += 1  # 是 leader 且「數學公式」符合「全部相連」的 edges 數目，就是答案
        return ans
