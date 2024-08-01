# LeetCode 1062. Longest Repeating Substring
# 最長的重覆的字串，有多長？(長度為1的不能算)
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # 可以用2層for迴圈：長度（長到短）、開始位置
        # 只要重覆，就找到答案了
        visited = set()
        N = len(s) # 要重覆字串，那長度要從N-1開始試
        for L in range(N-1,1,-1):  # 長度為1的不能算
            for i in range(N-L+1): # 能用的範圍就變少了
                if s[i:i+L] in visited: return L
                visited.add(s[i:i+L])
        return 0
