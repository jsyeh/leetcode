# 都排序好了，只要簡單利用 for 迴圈，就能找到第1個、最後一個的位置
# 不過題目希望用 O(logN) 的速度，所以想讓大家用 binary search來找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 方法1: for迴圈 O(N)
        ans = [-1, -1]
        for i in range(len(nums)):
            if nums[i]==target and ans[0]==-1: # 第一次遇到
                ans[0] = i
                ans[1] = i
            elif nums[i]==target: # 之後遇到
                ans[1] = i
        return ans
