# LeetCode 1619. Mean of Array After Removing Some Elements
# 把 arr 陣列裡「前5%」及「後5%」刪除後，平均是多少？
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        N = len(arr)  # 數字的總數
        p5 = N // 20  # N 是 20 的倍數, 5% 的數量「設成p5」
        return sum(arr[p5:-p5]) / (N-p5-p5)
