# LeetCode 2367. Number of Arithmetic Triplets
# 請問有幾組 i<j<k 使得 nums[i] nums[j] nums[k] 距離 diff
# 用暴力3層迴圈，太慢了。因為 nums[i] 是「嚴格遞增」越來越大
# 所以一定不會重覆，可利用 set() 來記下「之前出現過的數」
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        history = set()  # 用來存「出現過的數」

        ans = 0
        for num in nums:
            if num-diff in history and num-diff*2 in history:
                ans += 1
            history.add(num)
        return ans
        
