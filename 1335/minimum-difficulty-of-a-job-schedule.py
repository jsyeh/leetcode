# 工作要照順序做。每天可排很多工作，以最難的那個來算
# 有d天要排工作。求「每日難度」加起來最小。
# 看了 Editorial 的解釋，可以先從「暴力法」開始想，再變成DP
# 後來我看了 lee215的作法，被拆解得很清爽，看起來很舒服
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty) # 有幾份工作
        if N<d: return -1 # 天數太多，工作不夠分

        @cache
        def dfs(i,d): # 現在處理第i個job,剩下d天
            if d==1: # 剩下最後一天，全上，找最大值
                return max(jobDifficulty[i:])
            ans = inf
            maxd = 0 # job[i]...job[j] 的最大值
            # 把 job[i]...job[j] 放在今天處理
            for j in range(i, N+1-d): # 要扣掉d天
                maxd = max(maxd, jobDifficulty[j]) # job[i]...job[j]的最大值，要在今天做事
                ans = min(ans, maxd + dfs(j+1, d-1))
                # 今天做了 job[i]...job[j], j+1繼續，並少掉一天囉
            return ans # 處理 i,d 對應的最小值
        return dfs(0, d)
