# LeetCode 2976. Minimum Cost to Convert String I
# 將字母從original[i]變成changed[i]需要花費cost[i]
# 將字串從 source 變 target 要花費多少？（無法完成就return -1）
# 小心！把字母b 變成字母e 可能要「經過」中途的字母c幫忙
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        path = defaultdict(defaultdict)  # 建 graph 的 path
        for a,b,c in zip(original,changed,cost):  # a 變 b 需 cost c
            if b not in path[a] or path[a][b]>c:  # 更小、更值得更新
                path[a][b]=c  # 更新 a 變 b 的 cost c
        heap = []  # 接下來用 graph 的 path 更新「經過轉接後」更短的 Path
        for a in path:  # 依序將全部的 path[a][b] 依 cost 加入 heap
            for b in path[a]: 
                heappush(heap, (path[a][b], a, b))
        while heap:  # 經由 BFS (Best First Search) 依序慢慢展開
            now, a, b = heappop(heap)  #  a 變 b 需 cost now
            if b in path[a] and path[a][b] < now: continue  # 已更好，不用更新
            path[a][b] = now  # 更新
            for e in path[b]:  # node a 到 node b，再到 node e，變成 node a 到 node e
                if e not in path[a] or now + path[b][e] < path[a][e]:  # 找到更小的走法
                    heappush(heap, (now+path[b][e], a, e))
        ans = 0
        for a,b in zip(source,target):  # 逐字分析
            if a==b: continue  # 字相同，就不用變換
            if b not in path[a]:  # a 無法變成 b
                return -1  # 失敗
            ans += path[a][b]  # 累加答案
        return ans

