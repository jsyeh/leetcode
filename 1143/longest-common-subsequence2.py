# LeetCode 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        @cache
        def helper(i,j):  # 利用「函式呼叫函式」來解
            if i==N1 or j==N2: return 0  # 終止條件（終點）
            if text1[i]==text2[j]:  # 有相同字母
                return helper(i+1,j+1) + 1  # 答案 + 1
            return max(helper(i+1,j), helper(i,j+1))  # 兩種走法，找最大的 LCS
        #helper.cache_clear()
        return helper(0,0)  # 從 0,0 開始走
