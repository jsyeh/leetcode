# LeetCode 1905. Count Sub Islands  有幾個「島中之島」？給 m x n 矩陣裡面1是陸地、0是海
# 「島中之島」是指，grid2 裡某個島的「每個cell」都屬於 grid1 裡「同一個編號的島」
# 可用 DFS 或 BFS 分別把 grid1 和 grid2 裡的每個島都「編號」。這裡用「函式呼叫函式」DFS來完成。
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M, N = len(grid1), len(grid1[0])  # 寬、高
        def markID(i, j, id):  # 函式1：把grid1的相鄰陸地格子，標示id編號
            if i<0 or j<0 or i>=M or j>=N or grid1[i][j]!=1: return  # 超過邊界or「非陸地」，就不處理
            grid1[i][j] = id  # 標示id編號
            markID(i+1, j, id)  # 利用「函式呼叫函式」
            markID(i-1, j, id)  # 在 grid1 將整個島「標記同一編號」
            markID(i, j+1, id)
            markID(i, j-1, id)
        ans, id = 0, 2 # ans: 想找出「有幾個島中之島」, id: 島的編號（從2開始，因為0是海、1是陸，都用掉了）
        for i in range(M):  # 第1張地圖，先「標記編號」
            for j in range(N):
                if grid1[i][j]==1:  # 遇到「還沒標記」的陸地
                    markID(i, j, id)  # 用「函式呼叫函式」標記「島的編號」
                    id += 1  # 下一個島的編號+1
        def verifyID(i, j, id):  # 函式2：逐格檢查「編號是否一致
            if i<0 or j<0 or i>=M or j>=N or grid2[i][j]!=1: return True  # 超過邊界or「非陸地」，就不處理（沒事）
            grid2[i][j] = 0  # 這裡是陸地，先將陸地「弄沉」，避免「之後」重覆處理
            t1 = verifyID(i+1, j, id)  # 利用「函式呼叫函式」
            t2 = verifyID(i-1, j, id)  # 在 grid2 處理相鄰的陸地
            t3 = verifyID(i, j+1, id)  # 並將測試確認的結果 t1 t2 t3 t4 都分別算出來
            t4 = verifyID(i, j-1, id)  # 以便最後檢查
            return grid1[i][j]==id and t1 and t2 and t3 and t4  # 最後檢查「是否id都正確」。都正確，就是合格
        for i in range(M):  # 第2張地圖，一邊「找全部的島」一邊確認「id相同」
            for j in range(N):  # 若是陸地，就開始「一系列相鄰陸地」進行處理
                if grid2[i][j]==1 and verifyID(i,j, grid1[i][j]) and grid1[i][j]>=2: ans += 1
        return ans
