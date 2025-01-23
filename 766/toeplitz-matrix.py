# LeetCode 766. Toeplitz Matrix
# 矩陣的「每一條斜線」值都相同，叫 Toeplitz 矩陣。檢試 matrix 是不是
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i in range(M-1):
            for j in range(N-1):
                if matrix[i][j] != matrix[i+1][j+1]:  # 若斜線不相同
                    return False  # 就不是
        return True  # 成功檢測完，就是！
# case 364/483: [[11,74,0,93],[40,11,74,7]]
# case 372/483: [[22,0,94,45,46,96],[10,22,80,94,45,46]]
# case 427/483: [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
