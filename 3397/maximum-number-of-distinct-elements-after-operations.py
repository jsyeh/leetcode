# LeetCode 3397. Maximum Number of Distinct Elements After Operations
# nums 陣列裡，可「上下k以內」調整，最多能變出幾個「不同的數」
# 可用 Greedy 法，讓「小的數更小」、讓「大的數更大」儘量展開
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()  # 「小到大」排好
        ans = 0  # 能湊出幾個數呢？
        now = nums[0] - k  # 從最小開始，現在可用的數(將慢慢抬昇)
        for num in nums:  # 逐一檢查，看能湊出幾個數
            if num - k <= now <= num + k:  # 在合理範圍，可用 now
                ans += 1  # 多1個答案
                now += 1  # 抬昇1格，給下一個數使用
            elif now < num - k:  # now 太低了
                ans += 1  # 也可以多1個答案，即使用 num - k
                now = (num - k) + 1  # 下一個數能用的是「再+1」的數
        return ans
        
