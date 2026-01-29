# LeetCode 2976. Minimum Cost to Convert String I
# 將字母從original[i]變成changed[i]需要花費cost[i]
# 將字串從 source 變 target 要花費多少？（無法完成就return -1）
# 小心！把字母b 變成字母e 可能要「經過」中途的字母c幫忙
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        a_z = "abcdefghijklmnopqrstuvwxyz"  # 26個字母
        # table[a][b]是a到b的花費，用了倒裝句，讓 table[a][a]=0， 其他都是 inf
        table = { a:{b:0 if a==b else inf for b in a_z} for a in a_z }
        for a,b,c in zip(original, changed, cost):
            table[a][b] = min(table[a][b], c)
        for a,b,c in zip(original,changed,cost):  # 針對 a 到 b 需 cost c
            table[a][b] = min(table[a][b], c)  # 持續更新，記錄「最小」的花費
        for k in a_z:  # 中間中繼的字母 k
            for i in a_z:  # 出發點 i
                for j in a_z:  # 終點 j，經過中間中繼的字母 k，持續更新「最小」的花費
                    table[i][j] = min(table[i][j], table[i][k]+table[k][j])
        ans = sum( [table[a][b] for a,b in zip(source,target) ] )
        if ans==inf: return -1
        return ans
