# 本題, 要找到「天平」中間的點, 讓 左邊總合 == 右邊總合
class Solution:
    def pivotInteger(self, n: int) -> int:
        total = 0 # 先算出全部的總合 TOTAL
        for i in range(1, n+1):
            total += i
            
        left = 0 # 再算出左邊的總合
        for i in range(1, n+1):
            left += i
            if left == (total-left+i): return i
            # 如果左邊的總合 == 右邊的總合, 那就找到答案了
        return -1 # 沒有找到答案的話 -1
