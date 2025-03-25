# LeetCode 3394. Check if Grid can be Cut into Sections
# n x n 的地圖中，有許多 rectangles 裡面有「開始座標、結束座標」
# 能不能「橫切2刀」or「縱切2刀」把地圖分3區，每區至少有1個長方形，且不會跨區
# 其實等價於：橫向分析，再縱向分析，中間「不重疊」的區段「有幾個」（要有2個）
# 註：interval merge 的題目，要先排序，再依序處理「重疊」部分
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # 嘗試分析 x 方向
        clearCut = 0  # 現在找到幾個能「乾淨下刀」的「不重疊」區段
        rectangles.sort(key = lambda r: r[0])  # 用 x 座標排序
        p0, p1 = rectangles[0][0], rectangles[0][2]  # 前一筆的x0,x1資料
        for x0, y0, x1, y1 in rectangles:  # 依序處理
            if p1 <= x0:  # 前段尾、後段頭，中間存在能切的間隔，很好
                clearCut += 1  # 兩的長方形之間，可以「切1刀」
                p0, p1 = x0, x1  # 換下一筆 的 x 座標
            else:  # 但若不能分開，那就要 merge interval 合併
                p1 = max(p1, x1)  # 合併後的尾/結束位置/右邊界
        if clearCut >= 2: return True
        # 嘗試分析 y 方向
        clearCut = 0
        rectangles.sort(key = lambda r: (r[1],r[3]))  # 用 y 座標排序
        p0, p1 = rectangles[0][1], rectangles[0][3]  # 前一筆的y0,y1資料
        for x0, y0, x1, y1 in rectangles:
            if p1 <= y0:
                clearCut += 1
                p0, p1 = y0, y1  # 換下一筆 的 y 座標
            else:
                p1 = max(p1, y1)
        if clearCut >= 2: return True
        return False
