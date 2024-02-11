# n 可以由哪些「Prime Pair」加起來，n<=10^6 超大
# ex. 10 = 3+7 = 5+5
# 但其實「加到一半」就好了，看
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n<=3: return [] # 最小質數是 2， 2+2=4，故3以下無解
        table = [True]*n # 用篩子法
        for i in range(2,n):
            if table[i]: # 是質數
                for k in range(i*i, n, i): # 殺掉i的倍數
                    table[k] = False
        # 以上建立 prime table, 若 i 是質數，table[i]==True
        ans = []
        for i in range(2,n//2+1):
            if table[i] and table[n-i]: # 兩個都質數
                ans.append([i,n-i])
        return ans

