class Solution:
    def numSquares(self, n: int) -> int:
        table = [i for i in range(n+1)] # 若全用1組合出來 table[i] = i
        # print(table)

        for ii in range(2, int(n**0.5)+1): # 接下來試 2*2, 3*3, ... 
            p = (ii*ii) # 2*2=4
            for k in range(p, n+1): # 往前數p格，看table[k-p]+1是否更好
                table[k] = min(table[k], table[k-p]+1)

        return table[n]
