# LeetCode 3005. Count Elements With Maximum Frequency
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = [0]*101
        best = 0
        for now in nums:
            a[now]+=1
            if a[now]>best: best = a[now]
        
        ans = 0
        for now in nums:
            if a[now]==best: ans += 1
        return ans
