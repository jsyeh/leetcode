# LeetCode 812. Largest Triangle Area
# 最大的三角形面積：給一堆 poits，任3點可構成「三角形」，面積最大是多少？
# 另外一種作法，可用「向量外積」的絕對值 = 兩向量夾出的「平行四邊形面積」
# 所以 cross / 2 即是「三角形面積」。（外積 就是 「交叉相乘」）
# 程式碼就簡單很多了。
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        ans = 0
        for i in range(N-2):
            for j in range(i+1,N-1):
                # 使用向量外積 來算面積
                x1, y1 = points[j][0] - points[i][0], points[j][1] - points[i][1]
                for k in range(j+1,N):
                    x2, y2 = points[k][0] - points[i][0], points[k][1] - points[i][1]
                    cross = x1*y2 - x2*y1  # 外積（交叉相乘）
                    ans = max(ans, abs(cross)/2)  # 三角形面積 = 外積絕對值/2 
        return ans
