class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        N = len(colors)
        table = [[999999]*N for _ in range(3)]
        # table[c][i] 表示最近i 的 color c 的距離
        
        near = [-999999, -999999, -999999]
        for i in range(N):
            c = colors[i] - 1 # 把 1,2,3 轉換成 0,1,2
            near[c] = i
            for cc in range(3):
                table[cc][i] = i - near[cc]
        near = [1999999, 1999999, 1999999]
        for i in range(N-1, -1, -1):
            c = colors[i] -1
            near[c] = i
            for cc in range(3):
                table[cc][i] = min(table[cc][i], near[cc] - i)
        print(table)
        Q = len(queries)
        ans = [0]*Q
        for k in range(Q):
            i, c = queries[k][0], queries[k][1]-1
            ans[k] = table[c][i]
            if ans[k] >= 999999: ans[k] = -1
        return ans
# case 19/20: [2,1,2,2,1]
# [[1,1],[4,3],[1,3],[4,2],[2,1]]
