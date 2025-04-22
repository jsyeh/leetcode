# LeetCode 2338. Count the Number of Ideal Arrays
# 陣列長度 n 裡面值介於 1 ... maxValue 之間，且 arr[i] 可被 arr[i-1] 整除
# 有幾種可能的陣列？（答案可能很大，要取 10^9+7 的餘數）
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        @cache
        def C(k):  # 陣列總長 n 目前收集 k 個數，第1個數固定，剩下 n-1 個數，放 k-1 個數
            return comb(n-1,k-1)  # 排列組合是 C(n-1,k-1) 在n-1中取k-1的全部可能
        @cache  # 利用「函式呼叫函式」進行 DP
        # 先解「遞增」的問題：比now大的倍數、目前數集到k個數，有幾種。
        def helper(now, k):  # 目前挑的數是 now，已挑了 k 個數
            if k==n: return 1  # 若收齊 n 個數，答案是 1（挑到1組）
            ans = C(k)  # 先用「排列組合」在現有 k 數間，插入重覆的數，省下大量 helper() 呼叫
            for i in range(now+now, maxValue+1, now):  # 這些 i 都是 now 的倍數
                ans += helper(i, k+1)  # 如果接下來挑 i 的話，就挑了 k+1 個數了
            return ans  # 各種挑法都試過次，就是答案
        MOD = 10**9+7  # 答案要 % MOD 取餘數
        ans = 0
        for i in range(1, maxValue+1):  # 第1個數，要排什麼數呢？就挑 i 吧！
            ans = (ans + helper(i, 1)) % MOD  # helper(i,1)是「第1個數挑i」已挑了1個數
        return ans
