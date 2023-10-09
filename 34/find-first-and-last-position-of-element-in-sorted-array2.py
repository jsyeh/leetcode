# 都排序好了，只要簡單利用 for 迴圈，就能找到第1個、最後一個的位置
# 不過題目希望用 O(logN) 的速度，所以想讓大家用 binary search來找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 方法1: for迴圈 O(N)
        '''
        ans = [-1, -1]
        for i in range(len(nums)):
            if nums[i]==target and ans[0]==-1: # 第一次遇到
                ans[0] = i
                ans[1] = i
            elif nums[i]==target: # 之後遇到
                ans[1] = i
        return ans
        '''
        # 方法2: binary search O(logN)
        N = len(nums)
        left, right = 0, N
        while left<right:
            mid = (left+right)//2
            if nums[mid]<=target:
                left = mid + 1 # 這樣便能找到 nums[left]是更大（不包含）
            else:
                right = mid
        ans = [-1, -1]
        # print(nums, target)
        # print("left:", left)
        if left-1>=0 and nums[left-1]==target:
            ans[1] = left-1

        left, right = 0, N
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1 # 這樣便能找到 nums[left]是包含
            else:
                right = mid
        # print("left:", left)
        if 0<=left<N and nums[left]==target:
            ans[0] = left
        return ans

