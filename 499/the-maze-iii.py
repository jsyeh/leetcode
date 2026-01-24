# LeetCode 499. The Maze III
# 在迷宮裡踢球，球撞到牆才會停、才能變換方向，希望滾動的格子數最少
# 請給「每次踢的方向」對應的字串，若有相同，則先挑「字母序小」的字串
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        M, N = len(maze), len(maze[0])
        d = {'d':(1,0),'l':(0,-1),'r':(0,1),'u':(-1,0)}
        table = [[{'d':inf, 'l':inf, 'r':inf, 'u':inf, '':inf} for j in range(N)] for i in range(M)]
        heap = []
        heappush(heap, (0, '', False, ball[0], ball[1]))
        while heap:
            step, op, moving, i, j = heappop(heap)
            if moving==False:  # 停止移動，可再踢一步
                for c in d:
                    i2, j2 = i + d[c][0], j + d[c][1]
                    if i2<0 or j2<0 or i2>=M or j2>=N or table[i2][j2][c]<= step+1:
                        continue
                    if maze[i2][j2]==0:  # 前方空格，可踢
                        table[i2][j2][c] = step + 1
                        heappush(heap, (step+1, op+c, c, i2, j2))
                        if [i2,j2]==hole: return op+c
            else:
                i2, j2 = i + d[moving][0], j + d[moving][1]
                if i2<0 or j2<0 or i2>=M or j2>=N or maze[i2][j2]==1:  # 撞牆
                    if table[i][j]['']>step:
                        heappush(heap, (step, op, False, i, j))  # 新的開始、可踢
                    continue
                if table[i2][j2][moving]<=step+1: continue
                if maze[i2][j2]==0:  # 前方空格，可繼續滾
                    table[i2][j2][moving] = step + 1
                    heappush(heap, (step+1, op, moving, i2, j2))
                    if [i2,j2]==hole: return op
        return 'impossible'
