# LeetCode 2579. Count Total Number of Colored Cells
# 如圖「有很多格子」，從中間出發，慢慢往外著色，問 n 秒後，有多少格子「有著色」
# 觀察看看，能不能找到公式「描述格子的數量」，看到以下規則：
# 1: 1, 2: +2+2+0+0, 3: +3+3+1+1, 4: +4+4+2+2, 5: +5+5+3+3 ...
class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        for i in range(1, n+1):
            ans += i*2 + (i-2)*2
        return ans
