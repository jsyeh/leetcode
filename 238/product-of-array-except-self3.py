# LeetCode 238. Product of Array Except Self
# 由 nums 陣列出發，找到 ans 陣列，裡面對應的值，是（除本身外）全部的值相乘
# 題目「禁止使用除法」可準備 prefix 及 postfix 再相乘即可
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1]
        postfix = [1]
        for i in range(N):
            prefix.append(prefix[-1]*nums[i])
            postfix.append(postfix[-1]*nums[N-1-i])
        return [prefix[i-1]*postfix[N-i] for i in range(1,N+1)]
