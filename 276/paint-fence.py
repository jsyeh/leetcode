# n根柱子，k種色彩，不能有「連續3根以上」同色，問有幾種 paint 法
# 我原本的想法，是用 table[kk][i] 來處理，但3層for迴圈更新，超時了。
# 後來參考 Editorial 的 Top-Down DP 做法，其原則是：
# (1) 挑與前面不同的色彩，有(k-1)個色彩可以挑， (k-1) * total_ways(i-1)
# (2) 挑與前面相同的色彩，(k-1) * total_ways(i-2) 這要想比較久。
#     想和前面(i-1)相同，但不能和「前面的前面(i-2)」相同。
#     因此「前面的前面(i-2)」不同，在決定(i-2)後，有k-1種可能的色彩(挑選i-1及i)
class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def total_ways(i): # 想問第i根的結果
            if i==1:
                return k # 有k種可能的色彩
            if i==2:
                return k * k # 不超過，可以任意放色彩
            
            #return (k-1)*total_ways(i-1) + (k-1)*total_ways(i-2)
            return (k-1) * (total_ways(i-1)+total_ways(i-2))
            # 挑與前面不同的色彩(k-1種可能) + 挑與之前相同的色彩(也是k-1種可能*前前項)
        
        return total_ways(n)

        '''
        table = [[0]*k for _ in range(n)] # table[kk][i] 第i根，漆成kk色，有幾種漆法
        for i in range(n): # 柱子逐一去漆
            for kk in range(k): # 漆成kk色
                table[kk][i] = 0
                for ...糟糕，超時了...
        '''
