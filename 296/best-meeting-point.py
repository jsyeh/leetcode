# 200x200＝4萬 的格子，如果用暴力法試全部的點，需16億次
# 觀察發現 distance 算法是 dx+dy, 所以可分開挑選 ansI,ansJ
# 因為互相獨立，分開考量都是最佳時，合起來也是最佳。
# 不過耗時 991ms 是最差的 5%, 不甘心，重寫！
# 重寫之後，耗時 93ms 打敗 99.32% 很開心！
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        iAll = [0]*M # 橫向統計
        jAll = [0]*N # 直向統計
        for i in range(M): # 統計到座標軸上
            for j in range(N):
                if grid[i][j]==1:
                    iAll[i]+=1
                    jAll[j]+=1
        minTotalII, minTotalJJ = -1, -1
        for ii in range(M): # 所有可能的位置 ii
            total = 0
            for i in range(M): # 由事先統計的個數，計算距離
                total += abs(i-ii)*iAll[i]
            if minTotalII==-1 or total<minTotalII:
                minTotalII = total
        for jj in range(N): # 所有可能的位置 jj
            total = 0
            for j in range(N): # 由事先統計的個數，計算距離
                total += abs(j-jj)*jAll[j]
            if minTotalJJ==-1 or total<minTotalJJ:
                minTotalJJ = total
        return minTotalII + minTotalJJ # 兩個方向的最佳值，加起來

        return 0
        ''' # 下面的程式 991ms 太慢了()別人平均110ms) 重寫!
        M, N = len(grid), len(grid[0])
        minTotalII, minTotalJJ = -1, -1 
        for ii in range(M): # 挑選最佳的位置 ii
            total = 0
            for i in range(M):
                for j in range(N):
                    if grid[i][j]==1:
                        total += abs(i-ii)
            if minTotalII==-1 or total<minTotalII:
                minTotalII = total # 更新最佳 ii 對應的 minTotalII
        for jj in range(N): # 挑選最佳的位置 jj
            total = 0
            for i in range(M):
                for j in range(N):
                    if grid[i][j]==1:
                        total += abs(j-jj)
            if minTotalJJ==-1 or total<minTotalJJ:
                minTotalJJ = total # 更新最佳 jj 對應的 minTotalJJ
        #print(minTotalII, minTotalJJ)
        return minTotalII + minTotalJJ
        '''
