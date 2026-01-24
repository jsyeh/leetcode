# LeetCode 1877. Minimize Maximum Pair Sum in Array
# 要將 nums 陣列「拆成兩兩pair」湊出答案「相加的最大值」要最小
# 想到第1名到第20名用 S型的方式分配（像高斯小時候1加到100的pair法）
#  1  2  3  4  5  6  7  8  9 10
# 20 19 18 17 16 15 14 13 12 11
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()  # 先「小到大排好」
        ans = nums[0] + nums[-1]  # 先拿一組當答案
        for i in range(len(nums)//2):  # 頭尾「兩兩相加」
            ans = max(ans, nums[i] + nums[-1-i]) 
        return ans
