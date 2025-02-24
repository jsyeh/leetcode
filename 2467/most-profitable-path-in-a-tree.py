# LeetCode 2467. Most Profitable Path in a Tree
# 0...N-1 共 N 個 nodes，有 N-1 條 edges，先走到 node i 的人可賺 amount[i]，一起到的話，平分。
# Bob 從 「bob 往 0 走」，Alice 從 0 出發，走往任一片葉子走，問 Alice 最多賺多少錢？
# 把 0 當 tree root 出發，計算「到每個 node」對應的 depth 及 「得分最大值」。
# 看了 lee215 解說，更帥氣：dfs()同時，會有 depthBob 和 depth 的值，程式碼會更短
# 當 dfs() 走到某點時的 depthB == depth 就「吃一半」，若 depthB < depth 被 bob 先拿走，就是 0
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        path = defaultdict(list)
        for a,b in edges:  # 先把 edges 轉換成 path 資料結構
            path[a].append(b)  # a 能到 b
            path[b].append(a)  # b 能到 a
        visited = set()
        def dfs(a, depth):  # 現在處理 node a, 從 0 出發、到 a 的深度 depth
            visited.add(a)  # 標註「走過 node a」
            ans, depthB = -inf, inf  # subtree 最佳 ans 值 vs. bob 的深度
            if a==bob: depthB = 0  # 剛好現在在 bob 出發點，對應深度是0
            for b in path[a]:
                if b in visited: continue  # 走過，就避開
                now, nowDepthB = dfs(b, depth+1)  # 試走 b 小樹
                ans = max(ans, now)  # 這個小樹得分「更新答案」
                depthB = min(depthB, nowDepthB)  # 若 bob 在這個小樹，更新 depthB
            if ans==-inf: ans = 0  # 剛好是 Leaf node，就沒有其他分支。下面再處理 node a 的值
            if depthB == depth: ans += amount[a] // 2  # 此點距離「相同」，Alice 得一半
            if depthB > depth: ans += amount[a]  # 此 node 是 Alice 先到，全拿
            return ans, depthB+1  # 小樹的「最佳解」，若 bob 在裡面，bob的深度也回傳
        ans, depthB = dfs(0, 0)  # 從 node 0 出發，此時深度 0，將得到「最佳解」
        return ans
