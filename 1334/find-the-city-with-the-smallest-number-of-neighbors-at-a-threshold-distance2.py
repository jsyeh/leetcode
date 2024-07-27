# LeetCode 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# 題目的英文很難懂：有n個城市，有edges裡有a,b,w 對應「城市a」與「城市b」的距離w
# 每個城市都能往外走，預算有限下，能走到幾個（別的）好鄰居的城市？鄰居很少的城市很孤單。
# 把「最孤單」的城市找出來。有多個城市「一樣孤單」時，回傳「編號」較的城市
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 我看 lee215 解說，他發現 Floyd-Warshall 演算法，只要 N^3 的迴圈就能解
        dist = [[inf]*n for _ in range(n)]  # 二維陣列 dist[i][j] 對應 i到j的距離
        for i,j,w in edges: # 題目給 edge 資訊，用來更新 dist[i][j] 的捷徑
            dist[i][j] = dist[j][i] = w
        for i in range(n): dist[i][i] = 0 # 自己到自己，距離是0
        # 由前面一開始的資訊（直達車捷徑），再逐步更新「所有的可能」，得到「最佳解」
        for k in range(n): # 這行是重點中的重點：逐一考量「中繼點k」看「距離是否更短」
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        # 全部更新完，就是最佳解了。接下來數一數：有哪些城市的好鄰居（距離<=距離限制）最少
        # lee215 超喜歡寫「行數少」的程式，就用下面複雜的句子來完成「數數」的任務
        ans = {sum(d<=distanceThreshold for d in dist[i]) : i for i in range(n)}
        # 做出個字典，把「距離<=條件」、從i出發的數目當key, 對應到index i，再用倒裝句的for迴圈
        return ans[min(ans)]  # 最後，找「最小的key」也就是「好鄰居」最少的，查出對應的 index i
