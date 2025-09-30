# LeetCode 2221. Find Triangular Sum of an Array
# nums 陣列「像倒金字塔」兩兩相加，最後得到的數
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)  # 先了解陣列「有幾個數」
        for i in range(N-1):  # N 個數，要 N-1 回合
            for k in range(N-1-i):  
                # 0,1 相加，放在0；1,2 相加，放在1 ...
                nums[k] = (nums[k] + nums[k+1]) % 10
        return nums[0]  # 最後的答案
