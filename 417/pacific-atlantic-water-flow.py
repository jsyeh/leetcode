# LeetCode 417. Pacific Atlantic Water Flow
# m x n 長方形島嶼，左邊、上面接太平洋；右邊、下面接大西洋
# 水往低處流，heights[r][c] 對應高度，有的流到太平洋、有的流到大西洋
# 找出「分水嶼」的格子，剛好同時可以流到「太平洋、大西洋」
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])  # 島的長、寬
        def climb(queue: deque):  # 反過來，從「海邊」往上爬，能到到地點，便是答案
            visited = set(queue)  # 能走到的地方（一開始的起點，也是在「流域」裡）
            while queue:
                i, j = queue.popleft()
                for ii, jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 往4方向走
                    if ii<0 or jj<0 or ii>=M or jj>=N: continue  # 避開外面
                    if (ii,jj) in visited: continue  # 避開「走過的地方」
                    if heights[ii][jj] >= heights[i][j]:  # 可以「往上爬」
                        queue.append((ii,jj))  # 加入 queue
                        visited.add((ii,jj))  # 標注「走過了」
            return visited  # 走過的地方，便是「對應的流域」
        queue1, queue2 = deque(), deque()  # 「左上方」太平洋、「右下方」大西洋
        for i in range(M):
            queue1.append((i,0))  # 「左上方」的左
            queue2.append((i,N-1))  # 「右下方」的右
        for j in range(N):
            queue1.append((0,j))  # 「左上方」的上
            queue2.append((M-1,j))  # 「右下方」的下
        return list( climb(queue1) & climb(queue2) )  # 兩個流域「交集」的地方
