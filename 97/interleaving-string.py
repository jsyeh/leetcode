# 題目想將 s1 s2 交錯做出 s3 。
# 問題可化減成 dfs(i,j)表示s1取i個、s2取j個，能做出 s3的長度i+j
# 它會再去問 dfs(i+1,j) 與 dfs(i,j+1) 若有一可行，便能有答案。
# 終止條件，是順利找到 dfs(M,N) 便是圓滿了。
# 最後看 dfs(0,0)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # self.count = 0 # 用來測測函式會跑幾次
        @cache # 這是看 r0gue_shinobi 的 solution 用的技巧，能加速函式不重覆跑
        # https://leetcode.com/problems/interleaving-string/solutions/2249509/python-simple-solution-w-explanation-recursion-dp/
        def dfs(i, j):
            # self.count += 1 # 用來測測函式會跑幾次
            if i==len(s1) and j==len(s2):
                return True
            
            result1, result2 = False, False
            if i<len(s1) and s1[i]==s3[i+j]: # 能往下走，便有機會
                result1 = dfs(i+1, j)
            if j<len(s2) and s2[j]==s3[i+j]: # 能往下走，便有機會
                result2 = dfs(i, j+1)
            # 但如果都沒順利往下走的話，就會用到預設的 False 值，而失敗
            return result1 or result2
        
        ans = dfs(0,0)
        # print(self.count) # 用來測測函式會跑幾次
        return ans
