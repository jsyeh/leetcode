class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        # 直接用 binary search 就可以了
        left, right = 0, M*N
        while left < right:
            print(left, right)
            mid = int((left+right)/2)
            i, j = int(mid/N), int(mid%N)
            now = matrix[i][j]
            # print("matrix[i][j]:", now)
            if now==target: return True;
            if now > target: right = mid
            else: left = mid + 1
        
        return False
        
