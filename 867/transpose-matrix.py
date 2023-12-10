class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        ans = [[matrix[i][j] for i in range(M)] for j in range(N)]
        # 上面這行蠻酷的，能利用迴圈直接生成2D陣列的內容
        # 原本的matrix[i][j] 左手i 右手 j 對應的範圍是 M, N
        # 在生成時，用一樣的方法，找到 matrix[i][j] 的值
        # 只是在生成的順序上反過來（for右手生出i，再for左手生出j），
        # 所以直接長出 Transpose 後的矩陣
        return ans
