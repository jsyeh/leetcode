# inverse pair 是 nums[i]>nums[j]
# 問 1...n 的 array 裡，能做多幾種「剛好有k組inverse pair」的擺法
# 應該還是 DP 的題目：能把大門題拆成小問題嗎？」
# kInversePairs(n,k) kInversePairs(n-1,k) 再把最大數 n 塞在最右邊
# kInversePairs(n-1, k-0)...kInversePairs(n-1, k-k或k-(n-1) ) 
# 查看 Editorial 方法2 的講法，是「往左移」的總數是k即可做出 k inverse pair 的效果
# 但使用 top-down DP 的方法，超過時間
# 後來模仿 Editorial 方法6 的寫法，才成功。這題有夠難：題目難、想法難、觀念難
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        # 模仿 Editorial 方法6 函式呼叫函式的解法
        @cache
        def helper(n, k):
            if n==0: return 0
            if k==0: return 1
            # 下面寫法，可省掉「for迴圈大量加法」的時間
            ans = helper(n, k-1) + helper(n-1, k)
            if k-n>=0: ans -= helper(n-1, k-n) # 可能變負的

            return (ans+MOD) % MOD # 不要變負的
        
        ans = helper(n, k)
        if k>0: ans -= helper(n, k-1)
        return (ans+MOD) % MOD

    '''
    # 以下的寫法，模依Editorial方法2，但超過時間。需要重寫
    def kInversePairs(self, n: int, k: int) -> int:
        @ cache
        def helper(n, k):
            if n==0: return 0 # n被減太多了，不可能
            if k==0: return 1 # 一種可能，就是都沒有k
            ans = 0
            # 第n個數，可以放的位置，有 n-1 種可能，會用掉i個inverse
            for i in range(min(k,n-1)+1): # min() 能避免把k減成負的
                ans = (ans + helper(n-1,k-i)) % (10**9+7)
                # 所以子問題，
            return ans
        return helper(n, k)    
    '''
# case 35/80: n=1000, k=1000 超過時間
