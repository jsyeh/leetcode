# LeetCode 2943. Maximize Area of Square Hole in Grid
# 窗子有 n 個橫桿、m 個直桿，組成 (n+1) x (m+1) 的格子
# 可拿掉 hBars 標示的水平橫桿（從2開始） 和 vBars 標示的直桿（從2開始）
# 問「正方形洞」最大面積
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def maxCombo(bars):  # 找到「拆開bars後」能得到的最大空間
            bars.sort()  # 將「可拆的 bars」小到大排好
            ans = combo = 2  # 因保證能拆1個bar，答案至少是2格
            for i in range(1,len(bars)):  # 左到右巡
                if bars[i-1]+1==bars[i]:  # 相鄰2根可拆
                    combo += 1  # 空間變大，連續 combo 持續 + 1
                else:  # 若不是相鄰，就只能先拆1根 bar
                    combo = 2  # 空間就是2格
                ans = max(ans, combo)  # 更新最大值
            return ans
        ans = min( maxCombo(hBars), maxCombo(vBars) )  # 正方形邊長
        return ans * ans  # 面積是「邊長*邊長」
