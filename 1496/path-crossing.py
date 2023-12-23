# 這題想問「有沒有走過重覆的地方」 可以使用 HashMap 來做
# 用 visited = set() 來記錄走過的地方
# 一邊模擬、一邊檢查，就可以了
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set() # 走過的地方
        i, j = 0, 0 # 出發點
        def pos(i,j): # 轉成字串，以便丟入 visited
            return str(i)+' '+str(j)
        visited.add(pos(0,0)) # 走過出發點
        for c in path: # 根據每個走過的方向
            if c=='N': i-=1 # 更新 i,j座標
            if c=='E': j+=1
            if c=='W': j-=1
            if c=='S': i+=1
            if pos(i,j) in visited: # 到達走過的地方
                return True # 就是 cross
            visited.add(pos(i,j)) # 走過的要記起來
        return False # 都沒有 cross 就是 False
