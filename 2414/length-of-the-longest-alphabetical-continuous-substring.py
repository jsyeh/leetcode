# 字串裡，「連續增加的字母」最長有多長
# 
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        N = len(s)
        # table = [0]*N # 裡面存「到s[i]為止「已有最長的有多長」
        ans = 1
        prevMax = 1 # 存到 s[i] 結束的最長有多長
        for i in range(1,N):
            if ord(s[i])==ord(s[i-1])+1: # 遞增1個字母序 ord(c)
                prevMax += 1
                ans = max(ans, prevMax)
            else:
                prevMax = 1 # 新的開始
        return ans
