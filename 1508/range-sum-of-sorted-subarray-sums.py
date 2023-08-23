# 要計算 left...right(包含) 1-index 加總
# 暴力法時，1000*1000=10^6 個數
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        table = []
        N = len(nums)
        for i in range(N):
            running = 0 # running sum from i to j
            for j in range(i, N):
                running += nums[j]
                table.append(running) 
        table.sort()
        return sum(table[left-1:right]) % 1000000007
        # 要把 1-index 轉成電腦的 0-index
