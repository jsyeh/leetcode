# LeetCode 2389. Longest Subsequence With Limited Sum
# queries[i] 給個數字，問 nums 能挑出的「最長」有多長。
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        nums.sort()  # 先「小到大」排好，之後「小到大」挑數字即可
        # 因僅 1000 個數，暴力加起來即可。若數字大，可用 prefixSum 配 binary search
        for query in queries:  # 現在的限制數字
            nowSum, nowN = 0, 0
            for i in range(N):  # 「小到大」逐項加加看
                if nowSum + nums[i] <= query: # 加起來「不超過」
                    nowSum += nums[i]  # 就加起來吧
                    nowN += 1  # 恭喜，又多了1個數
            ans.append(nowN)
        return ans

