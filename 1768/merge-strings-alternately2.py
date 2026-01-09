# LeetCode 1768. Merge Strings Alternately
# 將兩個字串「交錯」合併在一起
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N1, N2 = len(word1), len(word2)
        i = j = 0
        ans = []
        while i<N1 or j<N2:
            if i<N1: ans.append(word1[i])
            if j<N2: ans.append(word2[j])
            i, j = i+1, j+1
        return ''.join(ans)
