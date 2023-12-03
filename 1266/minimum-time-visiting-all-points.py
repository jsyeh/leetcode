# 這題超簡單：照順序，把每個點走過，要花多少時間。
# 就直接 for 迴圈，配合 max(dx,dy) 加起來便是答案
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            ans += max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
        
        return ans
        
