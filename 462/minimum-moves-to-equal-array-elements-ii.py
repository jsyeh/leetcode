# 陣列裡的數，想知道要「加減」多少次，才能都一樣。
# 等價於：查看與 ans 的距離
# 但是不能暴力去試，因 10^5 * 10^5 太多了！
# 我猜用 binary search 就可以了，但看了 Editorial 有人說 median 中位數
# 好像更快！
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        median = nums[N//2]
        ans = 0
        for now in nums:
            ans += abs(now-median)
        return ans
