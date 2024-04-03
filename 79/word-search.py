# 要在格子裡, 找到 word 是否存在 (用過的格子, 不能重覆使用)
# 格子是6x6 範圍不大, 字最長是 15, 所以4個方向 4^15 暴力試,可能會超時。
# 感覺使用 DFS 可能可以。
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        T = len(word)
        visited = [[False]*N for _ in range(M)] # 避免某格重覆
        def trace(i, j, t): # 找到第t個字 word[t]
            if t==T: return True # 找到最後的字母, 順利結束
            if i<0 or j<0 or i>=M or j>=N: return False # 超過範圍, 不走
            if visited[i][j]: return False # 這輪這個格子有走過了, 不走
            if board[i][j]!=word[t]: return False # 字母不對, 不走
            visited[i][j] = True
            if trace(i, j+1, t+1): return True
            if trace(i, j-1, t+1): return True
            if trace(i+1, j, t+1): return True
            if trace(i-1, j, t+1): return True
            # 以上任一個「有善終」就 return True
            visited[i][j] = False # 還原成沒走過的樣子
            return False # 都沒成功, 就是失敗了
        
        for i in range(M):
            for j in range(N): # 每個格子, 都試看看
                if trace(i,j,0): return True
        return False
