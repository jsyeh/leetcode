# LeetCode 2976. Minimum Cost to Convert String I
# 將字母從original[i]變成changed[i]需要花費cost[i]
# 那將字串從 source 變成 target 要花費多少？（失敗就return -1）
# 小心！把字母b 變成字母e 可能要「經過」中途的字母c幫忙
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        a_z = list("abcdefghijklmnopqrstuvwxyz")  # 26個小寫字母
        dist = {a : {b : inf for b in a_z} for a in a_z}  # 建出 26 個字母的距離對照表
        for a,b,c in zip(original, changed, cost):  # 字母 a 到 字母 b 需要 cost c
            dist[a][b] = min(dist[a][b], c)  # len(cost)<=2000 表示有一堆重覆，取「最短距離」
        for a in a_z:  # 26個字母
            dist[a][a] = 0  # 自己到自己，距離是0

        for k in a_z:  # 用 Floyd-Warshall O(n^3) 找最短距離
            for i in a_z:
                for j in a_z:
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        ans = 0
        for a,b in zip(source, target):
            if dist[a][b]==inf: return -1 # 無法走到，提早結束
            ans += dist[a][b]  # 累積答案（最短距離）
        return ans
