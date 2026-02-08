# LeetCode 650. 2 Keys Keyboard
class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def helper(n):
            if n==1: return 0  # 一開始就有1個字母
            if n==2: return 2  # Ctrl-C Ctrl-V
            if n==3: return 3  # Ctrl-C Ctrl-V Ctrl-V
            if n==4: return 4  # Ctrl-C Ctrl-V Ctrl-V Ctrl-V 或 Ctrl-C Ctrl-V Ctrl-C Ctrl-V
            ans = n
            for i in range(2,int(sqrt(n))+1):
                if n%i==0:
                    ans = min(ans, helper(n//i) + i)
            return ans
        return helper(n)
