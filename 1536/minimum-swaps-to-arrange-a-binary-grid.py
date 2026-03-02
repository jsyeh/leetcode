# LeetCode 1536. Minimum Swaps to Arrange a Binary Grid
# n x n 格子，每次挑「上下相鄰兩rows」交換，幾步後「對角線以上」都是0
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        zeros = [0] * N  # 每個row「「右往左」連續有幾個0
        for i in range(N):
            for j in range(N-1,-1,-1):  # 右到左「倒過來的迴圈」
                if grid[i][j]==0:  # 「右往左」連續的0
                    zeros[i] += 1  # 「連續累積」多1個0
                else:  # 遇到不是0，就中斷
                    break
        # 以下「修改Bubble Sort」完成任務
        ans = 0  # 針對每個 row「連續累積的0」進行排序 swap 幾次
        for i in range(N):  # 「上到下」逐 row 檢查
            target = N - 1 - i  # 第 i row 需要 target 個 0
            k = i  # 從 i 往下找，看何時 zeros[k] >= target
            while zeros[k] < target:  # 0的數目不夠，k要往下挑
                k += 1  # 換下一個 k
                if k==N:  # 往下超過邊界（盡頭）
                    return -1  # 失敗、無法找到合格數量的 zeros
            # 離開 while迴圈，代表找到 zeros[k] 合格，可開始搬運（交換）
            for k2 in range(k, i, -1):  # k 要往上、慢慢搬運（交換）到 i 的位置
                zeros[k2-1], zeros[k2] = zeros[k2], zeros[k2-1]  # 搬運（交換）
                ans += 1  # 搬運（交換）1次
        return ans  # 沒有失敗的話，ans 是搬運（交換）的次數
