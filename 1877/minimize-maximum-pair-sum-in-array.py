# 有N個數, 兩兩一組, 要挑出 N/2 組 pair, 希望 Max Pair Sum 是最小。
# 我本來在想, 會不會是 binary search 去挑答案, 但想想不太對
# 偷看 Desription 的 Hint 提到 sort() 及太大的數要怎麼降。
# 想到品設系他們第1名到第20名用 S型的方式分配。
#  1  2  3  4  5  6  7  8  9 10
# 20 19 18 17 16 15 14 13 12 11
# 
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        ans = 0
        for i in range(N//2):
            now = nums[i] + nums[N-1-i]
            ans = max(now, ans)
        return ans
        
