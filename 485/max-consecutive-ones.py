class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        
        ans = 0
        one = 0
        for bit in nums:
            if bit==1:
                one += 1
            else:
                if one>ans:
                    ans = one
                one = 0
        if one>ans:
            ans = one
        return ans
