# LeetCode 3634. Minimum Removals to Balance Array
# nums 陣列「要刪掉幾個數」後，最大值 <= 最小值 * k
# 直覺想到：迴圈決定左邊（小），用 binary search 找右邊（大）
# lo=right加速用的技巧，因為下次的答案，會在right的右邊
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        N = len(nums)  # 有 N 個數字
        nums.sort()  # 將數字「小到大」排好
        ans = N - 1  # 最差的狀況，會刪 N-1 個數（剩1個）
        right = 0  # 供 binary search 時，設定 lo=right加速用
        for left in range(N):  # 先決定「左邊最小值」的位置
            right = bisect_right(nums, nums[left]*k, lo=right)
            ans = min(ans, N - right + left)
        return ans
