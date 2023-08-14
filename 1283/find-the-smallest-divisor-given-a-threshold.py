# 除法有餘數時，商要再加1
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        N = len(nums)

        def count(divisor: int) -> int:
            total = 0
            for num in nums:
                total += num // divisor
                if num%divisor > 0 : total += 1
            return total
        
        left, right = 1, max(nums)
        while left<right:
            mid = (left+right) // 2
            if count(mid) > threshold: # 超過了，要再大一點
                left = mid + 1
            else:
                right = mid
        return left
