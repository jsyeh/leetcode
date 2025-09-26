# LeetCode 611. Valid Triangle Number
# nums 裡，「能構成三角形」3個邊長，可挑出幾組？
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # 三角形3個邊：兩邊相加>長邊，所以先排序
        N = len(nums)
        ans = 0
        for i in range(N-2): # 第1個最短邊
            for j in range(i+1, N-1): # 第2個邊
                now = nums[i] + nums[j]
                # 用 binary search 找第3個邊的最大值位置(的右邊)，它的左邊就全是答案
                ans += bisect_left(nums, now, lo=j+1) - (j+1)
                # 在 binary search 時，從 lo=j+1 往右找，找完後，要扣掉 -(j+1)
        return ans
