class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        words = {}
        for n in nums:
            if n in words: return True
            else: words[n] = 1
        
        return False
