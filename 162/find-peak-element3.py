# LeetCode 162. Find Peak Element
# 全部巡一次，就可找到任一個 peak element
# 不過題目希望用 O(log n) 找到。任一個local maximum 就可以。可用斜率法來做
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        def helper(i):
            toLeft = i==N-1 or (nums[i] > nums[i+1])  # 1:應該左走
            toRight = i==0 or (nums[i-1] < nums[i])  # 1:應該右走
            return toLeft - toRight  # 正：會往左走
        #for i in range(N): print(helper(i), end=' ')
        return bisect_left(range(N), 0, key=helper)
