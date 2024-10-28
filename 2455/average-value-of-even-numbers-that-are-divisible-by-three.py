# LeetCode 2455. Average Value of Even Numbers That Are Divisible by Three
# nums 裡，找到所有「偶數、且為3的倍數」，其實就是「找6個倍數」的平均
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, N = 0, 0
        for num in nums:
            if num % 6 == 0:
                total += num
                N += 1
        if N==0: return 0
        return total // N
        
