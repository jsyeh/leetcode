# LeetCode 909. Snakes and Ladders 
# 蛇梯 每個格子編號「繞來繞去」同時有許多「直達車」，踩到時「瞬間」換位置
# 每次可以「增加1～6格」，什麼時候可到「最後1格」。看起來BFS 可解。
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)  # 格子是正方形 N x N 的大小
        table =  {} # 格子從「下到上」，像蛇一樣「左右輪流繞」，需換算「二維陣列」與「一維陣列」
        for k in range(N*N):  # 一維陣列的迴圈
            i, j = k // N, k % N  # 傳統變二維陣列的 i, j 座標
            if i%2==1:  j = N - 1 - j  # 在奇數層，會「反過來」變成「右到左」
            i = N - 1 - i  # 把「上下」倒過來，變成從下到下走
            table[k+1] = board[i][j]  # 把「二維陣列」的蛇梯，換算成「一維陣列」，從1開始
        # 接下來，使用 BFS 的方式，試著走走看，看何時能走到 table[N*N] 的這格
        queue = deque()  # 用 queue 進行 BFS
        queue.append( (0,1) )  # 第0步，站在 table[1] 的位置
        visited = set()  # 走過的格子，不要再走
        visited.add(1)  # 出發點算有走過囉！
        while queue:  # 進行 BFS
            step, k = queue.popleft()  # 第 step 步，能走到第 k 格
            if k == N*N: return step  # 到達「終點」
            for i in range(1,7):  # 可往下走 1 格到 6 格
                if k+i > N*N or (k+i) in visited: continue  # 起過邊界 or 走過，就避開這輪
                visited.add(k+i)
                if table[k+i] == -1:  # 簡單走、沒有變化
                    queue.append( (step+1, k+i) )  # 下一步可走到這些格
                else:  # 遇到瞬間移動的格子
                    queue.append( (step+1, table[k+i]) )  # 下一步可瞬間到 table[k+i] 對應格子
        return -1  # 無法到達「終點」就 return -1
