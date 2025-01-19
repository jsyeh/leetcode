# LeetCode 407. Trapping Rain Water II
# 下雨時，雨水會填在凹洞裡，問有多少雨水「在凹洞裡」。
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap) ,len(heightMap[0])  # 長寬
        heap = []  # 從外往內圍，供 BFS 的 heap，把處理中「低的」先取出
        visited = set()
        for i in range(M):  # 先把「邊緣」無法聚水的格子，都加入
            for j in range(N):  # 先把「邊緣」無法聚水的格子，都加入
                if i==0 or j==0 or i==M-1 or j==N-1:  # 邊緣當出發點，也當邊界
                    heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i,j))  # 加入 heap 的格子(i,j)，不會再進去第2次
        ans = 0
        level = 0  # 從外往內圍，目前能圍住凹洞的高度（更低可聚水、更高會流掉）
        # （根據「木桶原理」，水面高與「最短的高度」有關。這個 level 就是目前處理中的高度）
        while heap:  # 用 BFS 由外往內圍
            h, i, j = heappop(heap)
            level = max(h, level)  # 目前能圍住凹洞的高度，更高會流掉
            for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 四個方向都試
                if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 超過邊界，不做
                if (ii,jj) in visited: continue  # 走過，不再走
                heappush(heap, (heightMap[ii][jj], ii, jj))  # 將能走到的鄰居，加入 heap
                visited.add((ii,jj))  # 加入 heap 的格子(ii,jj)，不會再進去第2次
                if heightMap[ii][jj] < level:  # 這格比較低，能存水
                    ans += level - heightMap[ii][jj]  # 這格存下來的水量
        return ans
