# LeetCode 1765. Map of Highest Peak
# isWater[i][j] 陸地0、海洋1，希望從海平面開始「一步步變高」重建對應的「高度地圖」
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        M, N = len(isWater), len(isWater[0])
        ans = [[-1]*N for _ in range(M)]  # 答案（要重建出高度地圖）
        queue = deque()  # 利用 queue 進行 BFS 依序探索重建「高度地圖」
        for i in range(M):  # 先巡一次 isWater[i][j]
            for j in range(N):
                if isWater[i][j]:  # 如果是水/海洋的話
                    ans[i][j] = 0  # 海平面「高度是0」
                    queue.append((0, i, j))  # 將海洋加入 queue, 對應高度是0
        
        while queue:  # 接下來，針對 queue 裡的高度、座標，依序處理
            h, i, j = queue.popleft()
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 4個方向鄰居
                if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 超過範圍
                if ans[ii][jj] != -1: continue  # 有處理過了，就不再處理
                ans[ii][jj] = h + 1  # 更新 (ii,jj) 的高度
                queue.append((h+1, ii, jj))  # 新的座標，也加入 queue 裡處理
        return ans
