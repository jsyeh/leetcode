# 要找到長方形，回傳它們的「左上、右下」座標
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        M, N = len(land), len(land[0])
        ans = []
        for i in range(M):
            for j in range(N):
                if land[i][j]==1:
                    now = [i,j,i,j]
                    for i2 in range(i,M): # 查看「高度」
                        if land[i2][j]==1: 
                            now[2]=i2
                        else: break # 遇到盡頭跳開
                    for j2 in range(j,N): # 查看「寬度」
                        if land[i][j2]==1:
                            now[3]=j2
                        else: break # 遇到盡頭跳開
                    for i2 in range(i,now[2]+1):
                        for j2 in range(j,now[3]+1):
                            land[i2][j2]=0; # 清為0
                    ans.append(now)
        return ans
