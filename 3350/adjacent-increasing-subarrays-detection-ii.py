# LeetCode 3350. Adjacent Increasing Subarrays Detection II
# 這題跟 3349 Easy 題非常相似，但差在 k 的長度「要你自己找出來」
# 最多有 20萬個數「不能用暴力for迴圈」。可用「左到右combo」「右到左combo」
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)  # 陣列的長度
        left, right = [1]*N, [1]*N  # 「左到右combo」「右到左combo」
        for i in range(1,N):  # 建立「左到右combo」
            if nums[i-1]<nums[i]: left[i] = left[i-1] + 1
        for i in range(N-1-1, -1, -1):  # 反過來，建立「右到左combo」
            if nums[i]<nums[i+1]: right[i] = right[i+1] + 1
        ans = 0
        for i in range(N-1):  # 迴圈巡一輪，找到最大的 k 值
            now = min(left[i], right[i+1])  # 現在這格的 k 值
            ans = max(ans, now)  # 更新答案
        return ans   
        
