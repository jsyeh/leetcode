# 每個 rectangle 「長x寬」，希望裁成正方形
# 想知道「能裁出」「最大的正方型」的長方形有幾個
# 先巡一輪，了解「最大」是多大，再巡第二輪，數有幾個
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        for L, W in rectangles:
            maxLen = max(maxLen, min(L,W)) # 短邊為主，截出正方形
            # 找到最大的正方形
        # 再巡第二輸，數數有幾個
        ans = 0
        for L, W in rectangles:
            if min(L,W) == maxLen: # 能裁出的正方形邊，剛好==maxLen
                ans += 1
        return ans
