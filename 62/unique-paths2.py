# LeetCode 62. Unique Paths
# 從 0,0 出發，到 m-1,n-1 有幾種走法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(i,j):  # 現在站在 i,j 到終點有幾種走法
            if i==m-1 and j==n-1: return 1  # 順利走到終點
            if i==m or j==n: return 0  # 走出界
            return helper(i,j+1) + helper(i+1,j)
        helper.cache_clear()
        return helper(0,0)
