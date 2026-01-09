# LeetCode 238. Product of Array Except Self
# 由 nums 陣列出發，找到 ans 陣列，裡面對應的值，是（除本身外）全部的值相乘
# 題目「不準使用除法」可準備 prefix 及 postfix 再相乘即可
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix, postfix = [1] * N, [1] * N
        for i in range(1, N):
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[N-1-i] = postfix[N-i] * nums[N-i]
        return [prefix[i] * postfix[i] for i in range(N)]
