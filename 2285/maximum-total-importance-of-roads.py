# LeetCode 2285. Maximum Total Importance of Roads
# roads 會連續許多城市，每個城市，就會有不同的對外的道路。
# 有越多路的城市「越重要」，要變比較大的權重weight。把全部路「兩端」的城市權重「加起來」
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        weight = [0]*n  # weight[i] 表示城市i的權重，一開始是0
        for a, b in roads:  # 在迴圈裡，逐一增加 城市的 weight
            weight[a] += 1
            weight[b] += 1
        weight.sort() # 把 weight 照著重要性（小到大）排序
        ans = 0  # 接下來，要把「重要性」加起來。而重要性，剛好就是 weight 的排名
        for i in range(n):
            ans += weight[i] * (i+1) # 第i小的城市(0-index)，重要性是i+1 (1-index)
        return ans
        
