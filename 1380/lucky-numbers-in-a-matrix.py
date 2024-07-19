# LeetCode 1380. Lucky Numbers in a Matrix
# 先找到 row 裡最小的數、col 裡最大的數。再看 matrix[i][j]是否就是它
# 可使用 Python 語法 zip(*matrix) 做 transpose轉置找到 col 的部分
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        M, N = len(matrix), len(matrix[0])
        rowMin = [min(row) for row in matrix] # 每 row 最小
        colMax = [max(col) for col in zip(*matrix)] # transpose後，每col最大
        for j in range(N):
            for i in range(M): # 每個元素都去找，看誰同時是row最小、col最大
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    ans.append(matrix[i][j])
        return ans
