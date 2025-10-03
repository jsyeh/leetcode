# LeetCode 407. Trapping Rain Water II
# 下雨時，雨水會填在凹洞裡，問有多少雨水「在凹洞裡」。
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])  # 先算出地圖的長、寬
        heap = []  # 用 heap 來找到「高度最低」的「短板」，當「水位高」
        visited = set()  # 走過的格子「不會再走」
        def addHeap(height, i, j):  # 寫個 addHeap()函式，簡化 addHeap簡化
            heappush(heap, (height, i, j))
            visited.add((i,j))
        for i in range(M):  # 繞邊界（直邊）
            addHeap(heightMap[i][0], i, 0)
            addHeap(heightMap[i][N-1], i, N-1)
        for j in range(1,N-1):  # 繞邊界（橫邊），並避開走過的2端
            addHeap(heightMap[0][j], 0, j)
            addHeap(heightMap[M-1][j], M-1, j)
        ans = 0
        while heap:  # 利用 heap 資料結構，（從邊界開始）每次找出「最低」的邊，再擴展到鄰居
            height, i, j = heappop(heap)  # 目前 heap 中「高度最低」的「短板」height
            if height > heightMap[i][j]: ans += height - heightMap[i][j]  # 高度差、積水
            for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 前後左右的鄰居
                if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 超過地圖範圍，避開
                if (ii,jj) in visited: continue  # 走過的，避開
                if heightMap[ii][jj] >= height: addHeap(heightMap[ii][jj], ii, jj)
                else: addHeap(height, ii, jj)  # 這格可積水的格子（上面那行是過高的山）
        return ans
