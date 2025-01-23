# LeetCode 1064. Fixed Point
# arr 已經小到大排序好，想找到 arr[i]==i 的座標
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # 最簡單的方法，直接用迴圈測
        for i in range(len(arr)):
            if arr[i]==i: return i  # 符合題目條件
            if arr[i]>i: break  # 數字跳超過、沒機會了
        return -1  # 失敗
