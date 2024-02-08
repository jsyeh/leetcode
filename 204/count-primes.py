# 請問有幾個比n小的prime質數
# 5*10^6 其實數字頗多，要有效率的找答案
class Solution:
    def countPrimes(self, n: int) -> int:
        killed = [False]*n # 篩子法，看數字有沒有被殺

        ans = 0
        for i in range(2,n):
            if killed[i]==False: # 沒有被殺，便是質數
                ans += 1
                for k in range(i+i,n,i): # 兩倍以上，全殺
                    killed[k] = True
        return ans
# case 51/66: n=2 它是質數，但題目要問<n
