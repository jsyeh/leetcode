# LeetCode 3427. Sum of Variable Length Subarrays
# 從 max(0,i-nums[i]) ... i 一直加起來
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        N = len(nums)
        table = [0] * (N+1)  # 用來「增減」的對照表
        for i in range(N):
            table[max(0,i-nums[i])] += 1  # 開始的位置，增
            table[i+1] -= 1  # 結束的位置右邊，減
        ans = 0
        prefix = 0
        for i in range(N):
            prefix += table[i]  # 「目前為止」的增減量
            ans += prefix * nums[i]  # 乘上增減量
        return ans
        # 上面是利用「增減」的對照表
        # 下面是照著題目講的方法，不過用了兩層迴圈
        ans = [sum(nums[max(0,i-nums[i]):i+1]) for i in range(len(nums))]
        return sum(ans)
