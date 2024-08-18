# LeetCode 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        M = len(strs)
        N = min(len(strs[i]) for i in range(M))  # min(每條的長度)
        ans = 0  # 答案的長度

        for j in range(N):
            for i in range(1,M):
                if strs[i][j]!= strs[0][j]: # 有不一致，直接結束
                    return strs[0][:ans]
            ans += 1
        return strs[0][:ans]
