# LeetCode 2644. Find the Maximum Divisibility Score
# 問 nums[i] 能被 divisors[j] 整除最多的那個 divisors[j] 是哪個
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()  # 因為「小的divisor優先」
        ans = divisors[0]  # 最小的可能是答案，先塞進來
        score = 0
        for d in divisors:
            score2 = 0
            for num in nums:
                if num % d == 0: score2 += 1
            if score2 > score:
                ans = d
                score = score2
        return ans
