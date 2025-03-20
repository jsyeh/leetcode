# LeetCode 3108. Minimum Cost Walk in Weighted Graph
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        boss = [i for i in range(n)]  # 一開始：每個人都是自己的 boss，也就是 boss[i] = i
        weight = [-1 for i in range(n)]  # 一開始：都是自己一個人，-1 對應 0xFFFFFFFF 每個bit都是1

        def find(a):  # 一邊找 boss 一邊更新 boss 關係
            if a == boss[a]: return a
            boss[a] = find(boss[a])
            return boss[a]
        for a,b,w in edges:
            a, b = find(a), find(b)  # 分別找出 a, b的 boss 
            boss[a] = b  # a 的 boss 是 b
            weight[b] &= w  # 專注在 boss b 的 weight
            weight[b] &= weight[a]  # 也把 weight 合併到 boss b 
        ans = []
        for a,b in query:
            if find(a) == find(b): # 把所有能走到的地方，它們的 edges w 都 AND 起來
                ans.append(weight[find(a)])  # 查看 boss 的weight值
            else: ans.append(-1)
        return ans
            

