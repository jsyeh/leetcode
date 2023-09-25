class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num==0:
                ans = 0
            if num>0:
                ans *= 1
            if num<0:
                ans *= -1
        return ans
