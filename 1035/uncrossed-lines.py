# 其實題目看起來就是 LCS Longest Common Subsequence 的長度
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        table = [[0]*(N2+1) for _ in range(N1+1)]
        # table[i][j] 都設 0 ，不用再為 table[i][0] 及 table[0][j]清0

        for i in range(1,N1+1):
            for j in range(1,N2+1):
                if nums1[i-1] == nums2[j-1]: # 有相同的數字
                    table[i][j] = table[i-1][j-1] + 1 # 就多1條不交叉的線
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[N1][N2]
