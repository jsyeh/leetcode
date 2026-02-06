# LeetCode 3634. Minimum Removals to Balance Array
# nums 陣列「要刪掉幾個數」後，最大值 <= 最小值 * k
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        N = len(nums)  # 有幾個數字
        nums.sort()
        ans = N - 1  # 最差的狀況，會刪 N-1 個數「剩1個」，
        for left in range(N):  # 先決定「左邊最小值」
            # 再用 binary search 找右邊最大的，要 <= 最小值 * k
            right = bisect_left(nums, nums[left]*k+1)
            ans = min(ans, N - right + left)
        return ans
