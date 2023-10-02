# 要先「最大值」再看AND最長有幾個。所以，直接挑最大值，再數有幾個就好了。
# 等等，不對! 要 subarray 必須相連。所以要逐個去數
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = max(nums)
        # print(ans)
        # return countOf(nums, ans)
# case 25/51: [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]
        # 所以只好老老實實的逐個去數「有幾個連續」的
        count, longest = 0, 0
        for n in nums:
            if n == ans:
                count += 1
                if count > longest: longest = count
            else:
                count = 0
        return longest

