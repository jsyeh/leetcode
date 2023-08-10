class Solution:
    def numSquares(self, n: int) -> int:
        table = [i for i in range(n+1)]
        # 1一定是 perfect square

        for i in range(2, int(sqrt(n+1))+1):
            p = i*i # 下一個 perfect square 是 p
            for pp in range(p, n+1): # 依序更新
                if table[pp-p]+1 < table[pp]: #若更好
                    table[pp] = table[pp-p] + 1
        # print([i for i in range(n+1)])
        # print(table)
        return table[n]
