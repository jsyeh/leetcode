# LeetCode 1566. Detect Pattern of Length M Repeated K or More Times
# 問 arr 陣列裡，有沒有「連續M個數」「連續重覆k次」。這題不太容易想。
# 想像成「滑動」檢測，如果「距離m個字母」有相對，可能性增加了
# 總共 m*k個字母，那「距離m個字母相同」的連續 combo 數量是 m*(k-1)次
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        N = len(arr)
        combo = 0  # 連續幾個「距離跨M相同」
        for i in range(len(arr)-m):
            if arr[i]==arr[i+m]: combo += 1
            else: combo = 0
            if combo >= m*(k-1): return True
        return False
