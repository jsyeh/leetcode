# 1637. Widest Vertical Area Between Two Points Containing No Points
# 題目有一堆點，以x座標為基準，想知道「x距離最大」是多少
# 所以，就先把全部的點，以x座標來排序
# 接下來，兩兩比較，看 x2 - x1 的距離，如果比 ans 大，ans 就更新
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        N = len(points)
        # ans = points[N-1][0]-points[0][0]
        ans = 0
        for i in range(N-1):
            diff = points[i+1][0] - points[i][0] 
            # if diff==0: continue
            if diff>ans: ans = diff

        return ans
        
