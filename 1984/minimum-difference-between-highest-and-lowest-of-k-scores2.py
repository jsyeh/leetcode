# LeetCode 1984. Minimum Difference Between Highest and Lowest of K Scores
# nums 是學生的分數，挑k位學生，希望「最高分-最低分」最小
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  # 分數「小到大」排好
        ans = nums[k-1] - nums[0]  # 要持續更新的答案「最高分-最低分」
        for i in range(k,len(nums)):  # 迴圈往右走
            ans = min(ans, nums[i]-nums[i-k+1])  # 持續更新
        return ans
