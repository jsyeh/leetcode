class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        N = len(coordinates)
        for i in range(1, N-1):
            dx2 = coordinates[i+1][0] - coordinates[i][0]
            dy2 = coordinates[i+1][1] - coordinates[i][1]
            # dx/dy vs. dx2/dy2 比值相同，其實就是交叉相乘的結果相同 
            if dx*dy2 != dx2*dy: return False
        
        return True

