# LeetCode 812. Largest Triangle Area
# 最大的三角形面積：給一堆 poits，任3點可構成「三角形」，面積最大是多少？
# 50個點，使用「暴力3層」for迴圈應該「還行」
# 三角形面積，最近TAICA交大温宏斌老師「基礎程式設計」課，用到「海龍公式」
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def dist(i, j):  # 想知道 points[i] points[j] 的距離
            dx, dy = points[i][0]-points[j][0], points[i][1]-points[j][1]
            return sqrt(dx*dx + dy*dy)  # 距離公式
        def HeronArea(a,b,c):  # 古希臘數學家「海龍」發明的「海龍公式」算面積
            s = (a+b+c)/2
            inside = s * (s-a) * (s-b) * (s-c)  # 有可能運算時0被算成 -0
            if inside<0: return 0  # 所以保護一下，直接 return 0
            return sqrt(inside)
        N = len(points)
        ans = 0
        for i in range(N-2):  # 只有50個點，可暴力3層迴圈
            for j in range(i+1,N-1):  # 將全部「任3點」都試過
                for k in range(j+1,N):
                    a, b, c = dist(i,j), dist(j,k), dist(i,k)  # 3條邊長
                    ans = max(ans, HeronArea(a,b,c) ) # 套公式算面積，找最大值
        return ans
