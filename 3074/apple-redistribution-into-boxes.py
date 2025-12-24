# LeetCode 3074. Apple Redistribution into Boxes
# 每個箱子的容量 capacity 不同。有一堆蘋果 apple 最少要幾個箱子, 便能全部裝起來
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)  # 先了解「總共有幾顆蘋果
        capacity.sort(reverse=True)  # 大的箱子在前面、小的在後面
        ans = 0  # 總共要裝幾箱呢? 
        for c in capacity:  # 由大到小, 依序使用箱子
            ans += 1  # 又用了1個箱子
            total -= c  # 蘋果裝箱後, 剩下多少蘋果?
            if total <= 0: break  # 蘋果裝完了
        return ans
