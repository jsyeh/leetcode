# LeetCode 2106. Maximum Fruits Harvested After at Most K Steps
# fruits[i] = [pos[i], amount[i]] 對應某堆水果的位置、數量（位置小到大排好）
# 你一開始在 startPos, 能左右移動 k 單位，問最多能收成多少水果？
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 因為總共有 20萬格，就直接用 prefix sum 快速找到「某一段」的水果總數
        N = max(fruits[-1][0], startPos) + 1 # 格子總數，可能是最右邊的水果位置，也可能是開始位置 + 1
        fruit = [0] * N  # 某個位置的水果數量，等一下迴圈會塞水果
        for pos, amount in fruits:
            fruit[pos] = amount  # 把水果，放在對應的位置
        preSum = [0]  # 用來速解的 prefix sum，可快速找到 fruit[i]..fruit[j] 的水果總量
        for i in range(N):  # 針對每個格子 (有歪1格哦！因為最左邊有個[0])
            preSum.append( preSum[i] + fruit[i])  # 累計水果數量
        ans = 0  # 先往左 i 格，再往右 j 格
        for i in range(k+1):  # 一開始可往左 0...k格
            left = startPos - i  # 往左走i步，用掉 i步，剩下 k-i步
            right = left + (k - i)  # 左邊界「往右再走 k-1步」
            if right < startPos: right = startPos  # 其實一開始的位置也可算右邊界
            left, right = max(0,left), min(right,N-1)  # 修正左界、右界，不要超過陣列範圍 0..N-1
            ans = max(ans, preSum[right+1]-preSum[left])  # 目前left...right的總量，是否更大
        for i in range(k+1):  # 一開始可先往右 0...k格
            right = startPos + i  # 往右走i步，用掉i步，剩 k-i步
            left = right - (k-i)  # 可再往左走 k-i步
            if startPos < left : left = startPos  # 一開始的位置可能更左邊，當左邊界
            left, right = max(0,left), min(right,N-1)  # 修正左界、右界，不要超過陣列範圍
            ans = max(ans, preSum[right+1]-preSum[left])
        return ans
