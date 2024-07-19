# LeetCode 909. Snakes and Ladders 
# 蛇梯 每個格子編號「繞來繞去」同時有許多「直達車」，踩到時「瞬間」換位置
# 每次可以「增加1～6格」，什麼時候可到「最後1格」。看起來BFS 可解。
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        table = {}  # 先將 table[k] 找到對應的 i,j 的值 (-1 or 目標)
        N = len(board)  # 格子是正方形
        for k in range(N*N):
            i, j = k // N, k % N
            if i%2==1: j = N - 1 - j  # j倒過來
            i = N - 1 - i
            table[k+1] =  board[i][j]
        queue = deque()
        queue.append((1,0)) # 要0步，能到達格子1
        visited = defaultdict(bool)
        while queue:
            pos, step = queue.popleft()
            for i in range(pos+1,pos+7): # 可往前6步
                if visited[i] or i > N*N: continue # 離開這一輪
                visited[i] = True
                if i == N*N: return step+1 # 走到目的地
                if table[i]==-1: queue.append((i,step+1))
                else:
                    if table[i]==N*N: return step+1 # 也能到目的地 
                    queue.append((table[i],step+1))  # 遇到直達車
        return -1  # 沒辦法走到目的地
# case 4/215: [[-1,-1,-1],[-1,9,8],[-1,8,9]]
# case 157/215: [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
