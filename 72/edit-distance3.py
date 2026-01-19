# LeetCode 72. Edit Distance
# 典型「動態規劃」的問題：word1 要經過「幾次編輯」，會變成 word2
# 編輯包括「插入1個字母、刪掉1個字母、換掉1個字母」
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        @cache
        def helper(i,j):
            if i==N1 and j==N2: return 0
            if i==N1: return N2-j
            if j==N2: return N1-i
            ans = min(helper(i+1,j), helper(i,j+1), helper(i+1,j+1)) + 1
            if word1[i]==word2[j]: return min(ans, helper(i+1,j+1))
            return ans
        return helper(0,0)
