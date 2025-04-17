# LeetCode 2176. Count Equal and Divisible Pairs in an Array
# 請問有幾組 nums[i]==nums[j] and (i*j)%k==0
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):  # 左手i
            for j in range(i+1,N):  # 右手j 直接暴力試即可
                if nums[i]==nums[j] and (i*j)%k==0:
                    ans += 1
        return ans
