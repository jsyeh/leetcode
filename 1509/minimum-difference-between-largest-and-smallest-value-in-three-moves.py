# LeetCode 1509. Minimum Difference Between Largest and Smallest Value 
# in Three Moves 可改變 nums 裡面的3個數字後，問「最大、最小值」最小差多少
# 翻譯：若可刪掉3個數字，剩下的「最大、最小值」差多少
# 翻譯：如果把數字「小到大」排好，能刪掉 左端＋右端，共3個
# 0 1 2 3 4 5
#       x x x 左0右3
# x       x x 左1右2
# x x       x 左2右1
# x x x       左3右0
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)  # 總共有幾個數呢？
        if N <= 3: return 0  # 數字太少，全刪光光，提早結束
        nums.sort()  # 小到大排好
        ans = nums[N-4] - nums[0] # 如果左端0、右端3
        for i in range(1,4):  # 像跳舞一樣，右端往右i，左端也往右i
            ans = min(ans, nums[N-4+i]-nums[0+i]) # 左1右2， 左2右1，左3右0
        return ans
