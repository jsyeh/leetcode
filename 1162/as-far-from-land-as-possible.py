# 陸地是1，海是0，想問「離陸地最遠」是多少
# 其實直接從陸地開始，用 BFS 就可以算完了。
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque() # 配合 append() 及 popleft()
        visited = set() # 去過的地方
        N = len(grid) # 題目說是「正方形」
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1: # 是陸地，加入 queue裡
                    queue.append((i,j,0)) # 陸地的距離是0
                    visited.add( str(i)+' '+str(j) ) # 將座標變字串，加入set
        if len(queue)==0: return -1 # 如果沒有陸地，return -1
        if len(queue)==N*N: return -1 # 如果沒有海，也要return -1 (要小心)

        def checkAndAdd(i,j,d):
            if i<0 or j<0 or i>=N or j>=N: return # 超過邊界，離開
            if str(i)+' '+str(j) in visited: return # 走過，也離開
            queue.append((i,j,d)) # 可以走，就塞進queue
            visited.add(str(i)+' '+str(j))

        ans = 0
        while len(queue)>0: # 只要 queue裡還有東西，就繼續 BFS
            i,j,dist = queue.popleft() # 取出 queue 
            ans = max(ans, dist) # 更新 ans 對應的距離

            checkAndAdd(i+1,j,dist+1) # 四個方向去探索
            checkAndAdd(i-1,j,dist+1)
            checkAndAdd(i,j+1,dist+1)
            checkAndAdd(i,j-1,dist+1)

        return ans
# case 37/38: [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# 我以為是0，結果是-1 原來「沒有陸地」or「沒有海」都要 retur -1
