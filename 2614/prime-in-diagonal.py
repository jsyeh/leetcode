# 對角線上「最大的質數」
# 判斷nums[i][j]是否為質數的方法，是測 2...sqrt(nums[i][j])
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = len(nums)
        candidate = [nums[i][i] for i in range(N)]
        candidate += [nums[i][N-1-i] for i in range(N)]
        ans = 0
        for n in candidate:
            if n==1: continue # 1不是質數
            bad = False
            for i in range(2,int(sqrt(n))+1):
                if n%i==0: # 若能整除，就不是質數
                    bad = True
                    break
            if not bad: # 沒有壞掉，便是質數
                ans = max(ans, n) # 更新答案
        return ans
