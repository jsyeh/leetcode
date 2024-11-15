# LeetCode 1574. Shortest Subarray to be Removed to Make Array Sorted
# 刪掉「某一段」後，陣列變成「小到大排好」。
# 參考votrubac的解法，先把右端的最長先找出來，再用「毛毛蟲」法，滑動比對。
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = 0, N-1  # 左邊界、右邊界放好
        while right>0 and arr[right-1] <= arr[right]:  # 先「右界往左滑」
            right -= 1  # 只要右邊照大小順序，就繼續延長：right 左滑

        ans = right # left 要從0開始往右滑，一開始 left 是0, 答案是 right
        # 再來處理 left 左邊界：只要左邊照大小順序，就 left 往右滑
        while left < right and (left==0 or arr[left-1]<=arr[left]):
            # 左右不能重疊 and (左邊在開頭 or 左邊2項以上時，大小順序正確)
            while right<N and arr[left] > arr[right]: # 左右兩段，沒能照順序相接
                right += 1  # 右界就往右，看有無機會接起來
            # 離開迴圈，表示右邊界「做完調整」，能接起來
            ans = min(ans, right-left-1)  # 更新答案
            left += 1  # 新的左邊界，left 迴圈 += 1
        return ans
