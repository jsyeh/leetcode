# 正方形 nxn 的 matrix 裡, 是否「每一個」 row 或 col 裡都收集滿 1..n 的值
# 因為 n<=100 所以暴力法就可以成功了
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        for i in range(N): # 針對 row[i] 想看裡面是否「數字全部都有」
            count = [0]*(N+1) # 因 0-inddex vs. 1-index 差1
            for j in range(N): # 因題目規定 matrix裡介於1..n,所以不用檢查
                count[ matrix[i][j] ] += 1
                if count[ matrix[i][j] ] > 1:
                    return False # 只要有任何不合理, 就 False
        
        for j in range(N): # 針對 col[j] 想看裡面是否「數字全部都有」
            bad = 0
            count = [0]*(N+1) # 因 0-inddex vs. 1-index 差1
            for i in range(N):
                count[ matrix[i][j] ] += 1
                if count[ matrix[i][j] ] > 1:
                    return False # 只要有任何不合理, 就 False

        return True # 都沒有 False, 就成功了
