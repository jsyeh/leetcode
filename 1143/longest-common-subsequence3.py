# LeetCode 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        @cache
        def helper(i,j):
            if i==N1 or j==N2: return 0
            if text1[i]==text2[j]: return 1 + helper(i+1,j+1)
            return max(helper(i+1,j), helper(i,j+1))
        return helper(0,0)
