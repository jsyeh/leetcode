# 這個矩陣有個特質，是某個位置的左上方塊，都會比它小。右下方塊，都會比它大
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            left, right = 0, N
            while left<right:
                mid = (left+right)//2
                if matrix[i][mid]==target: return True
                if matrix[i][mid]<target:
                    left = mid + 1
                else:
                    right = mid
        return False
            

