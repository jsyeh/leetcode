# LeetCode 773. Sliding Puzzle
# 滑動拼圖：2x3的格子，空格0 可相鄰格子交換/滑動，讓board裡依序12345要幾步？
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 可用 BFS 把全部的可能都試過，如果出現循環/走不下去，就失敗
        nowBoard = tuple(board[0]+board[1])  # nowBoard是比對用tuple
        target = (1,2,3,4,5,0)  # 最後的目標
        if nowBoard == target: return 0  # 一開始就是 target 直接0步 找到答案
        visited = set()  # 記錄「走過的盤面」避免重覆
        visited.add(nowBoard)  # Hash Set 不能用 list 要改 tuple
        for i in range(2):
            for j in range(3):
                if board[i][j]==0: startI, startJ = i, j  # 找到出發點「空格0」
        queue = deque()  # BFS 配合 queue 實作
        queue.append((0, startI, startJ, nowBoard))  # 出發的盤面資訊: 第幾步、座標、盤面
        dI = [0,1,0,-1]  # 相鄰的4個方向
        dJ = [1,0,-1,0]  # 相鄰的4個方向
        while queue:  # BFS 配合 queue 實作
            move, i, j, nowBoard = queue.popleft()  # 現在的盤面資訊
            board = list(nowBoard)  # list 才能修改內容
            for k in range(4):  # 相鄰的4個方向
                i2, j2 = i+dI[k], j+dJ[k]  # 相鄰的4個方向
                if 0 <= i2 < 2 and 0 <= j2 < 3:  # 相鄰的4個方向，在範圍內
                    board[i*3+j], board[i2*3+j2] = board[i2*3+j2], board[i*3+j]  # 調換
                    nowBoard = tuple(board)  # 交換後，轉為 tuple
                    if nowBoard == target: return move+1  # 找到 target 答案
                    if nowBoard not in visited:  # 沒走過，才能走
                        queue.append((move+1, i2, j2, nowBoard))
                        visited.add(nowBoard)
                    board[i*3+j], board[i2*3+j2] = board[i2*3+j2], board[i*3+j]  # 還原
        return -1
