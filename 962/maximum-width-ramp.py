# LeetCode 962. Maximum Width Ramp
# Ramp 是上升坡道，題目想在 nums 裡，找兩點 i<j距離最遠，讓nums[i]<=nums[j]
# 若用兩層 for 迴圈，對所有可能的 i,j 暴力去找，會超過時間，
# 可使用 monostack 技巧，像金字塔一樣，記錄「漸減」的歷史記錄，再從右到左，逐項拆開
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        monostack = [(nums[0],0)]  # 記錄一開始的值，及其 index
        for i in range(1,len(nums)):  # 比較 nums[i] 及 monostack 歷史記錄
            if monostack[-1][0] > nums[i]: # 對應的值更小，就塞入 monostack
                monostack.append((nums[i], i))  # 往上蓋金字塔
        # 建好 monostack 後，再從右到左，逐項拆開（如果還能當成左小右大的 Ramp，就一邊更新、一邊拆）
        ans = 0  # 左小右大、成為 Ramp 的長度。一開始預設是0
        for i in range(len(nums)-1, -1, -1):  # 倒過來的迴圈，從右到左量資料
            # 只還還合乎 Ramp 左小右大，就用 while 迴圈一直做、一直拆金字塔
            while len(monostack)>0 and monostack[-1][0] <= nums[i]:  # 還有 stack 且 stack最上方（左小）「要拆掉」
                ans = max(ans, i - monostack.pop()[1])  # 就更新答案（並拆掉1層 monostack) 
        return ans
