# 找出有幾姐 bad pair: i<j and j-i != nums[j] - nums[i]
# 不過10^5 不能用暴力法。
# 查看 grawlixes 的 Solutions，他建議「反過來」解
# return total - good
# totoal 是 i<j 的排列組合，即 N*(N-1)//2
# good 是 j-i == nums[j] - nums[i] 的可能個數，
# 改成 j-nums[j] == i-nums[i] 能使用 dict 來碰撞「相同值」
# 能用 DP 來加速。它的解法太美妙了！
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        table = defaultdict(int)
        good = 0
        for i in range(N): # 量測 i - nums[i] 
            diff = i - nums[i]
            good += table[diff]
            table[diff] += 1
        return N*(N-1)//2 - good

