# LeetCode 1182. Shortest Distance to Target Color
# colors 裡有 1,2,3 三種色彩的分布狀況，queries 問 [i,c] 離 index i 最近的 color c 距離
# 策略：先「左到右、右到左」建出「距離對照表」，了解「某格對某色彩」的最近距離
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        N = len(colors)  # 陣列的長度
        table = [[inf] * 4 for i in range(N)]  # 三種色彩的距離對照表，因 1~3 所以陣列開4
        pos = [inf] * 4  # 3個色彩的最近值（左到右巡）
        for i in range(N):  # 左到右巡，便能知道某一格「左邊最近的 color 距離是多少」
            pos[colors[i]] = -1  # 自己的色彩最近，配合下面 += 1 剛好變成距離0
            for k in range(1,4):  # 三種色彩 1，2，3
                pos[k] += 1  # 距離都+1
                table[i][k] = pos[k]
        pos = [inf] * 4  # 3個色彩的最近值（右到左巡）
        for i in range(N-1,-1,-1):  # 倒過來的迴圈，右到左巡
            pos[colors[i]] = -1
            for k in range(1,4):
                pos[k] += 1
                table[i][k] = min(table[i][k], pos[k])
        print(table)
        ans = []
        for i, c in queries:  # 接下來針對 queries 問題，逐一找答案
            if table[i][c]==inf: ans.append(-1)  # 塞入 -1
            else: ans.append(table[i][c])  # 塞入答案
        return ans












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
