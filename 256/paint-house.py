class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # cost[i][k] 表示 house i 著色 color k 的 cost
        # 總共有 3 colors: red, blue, green
        N = len(costs)
        table0 = [0]*N # table0[i] 表示第i間漆red的cost
        table1 = [0]*N # table1[i] 表示第i間漆blue的cost
        table2 = [0]*N # table2[i] 表示第i間漆green的cost
        table = [table0, table1, table2]
        
        table[0][0] = costs[0][0]
        table[1][0] = costs[0][1]
        table[2][0] = costs[0][2]
        # table[k][i] 是倒過來的哦！

        for i in range(1,N):
            for k in range(3):
                prevCost = 999999999
                # 我突然想到的奇怪技巧，當成初始值，下面再看能否變小
                for kk in range(3): # 暴力加法
                    if kk!=k and table[kk][i-1] < prevCost:
                        prevCost = table[kk][i-1] # 小心kk
                # prevCost 是之前不同色的最小值
                table[k][i] = costs[i][k] + prevCost
        #print(table)
        return min(table[0][N-1], table[1][N-1], table[2][N-1])

